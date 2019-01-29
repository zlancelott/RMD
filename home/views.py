from django.shortcuts import render, redirect,  get_object_or_404
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.decorators import user_passes_test

from .forms import SubForm, UpdateSubForm

from .models import User, Subject, Submission, File, ModerationOfSubjects

from django.http import HttpResponseRedirect, HttpResponse

import json

from django.views.decorators.csrf import csrf_exempt

from django.db.models.signals import pre_save
from .models import Submission


def my_handler(sender, **kwargs):
    global notify

    notify = True


pre_save.connect(my_handler, sender=Submission)

@login_required
def home(request):

    user_logged_in = request.user

    try:
        moderador = ModerationOfSubjects.objects.get(pk=user_logged_in.id)
    except ModerationOfSubjects.DoesNotExist:
        moderador = False
        print ("Não existe")


    # Obtendo Formulário 
    if request.method == "POST":

        form = SubForm(request.POST or None, request.FILES or None)

        print (request.POST)
        print (request.FILES)

        print (form.is_valid())

        print (form)

        if form.is_valid():
            print ("Entrando...")
            # Salvando Submissão
            submission = Submission()
            submission.subject = form.cleaned_data['subject']
            submission.submission_date = form.cleaned_data['class_date']
            submission.description = form.cleaned_data['description']
            submission.topic = form.cleaned_data['topic']
            submission.uploader = user_logged_in

            submission.save()

            # Salvando Arquivo (s)

            for image in request.FILES.getlist('files'):
                file = File()
                file.file_image = image
                file.submission = submission

                file.save()

            return redirect ('home')


    else:
        form = SubForm(request.POST or None, request.FILES or None)

        # Editando as Labels
        form.fields['subject'].label = 'Disciplina'
        form.fields['topic'].label = 'Assunto'
        form.fields['class_date'].label = 'Data da Aula'
        form.fields['description'].label = 'Descrição'
        form.fields['files'].label = 'Imagens da Aula'

        notify = False
    

    # Criando dicionario com subjects para select de In-Place element #
    subjects_dict = {"": ""}
    x=1
    for subject in user_logged_in.subjects.all():
        subjects_dict[subject.name] = subject.name
        x+=1
        
    subjects_dict["selected"] = ""

    json_data = {
        'submission_form' : form, #Formulário para Submissão
        'submissions': user_logged_in.submissions.filter(approved=True), #Apenas submissões já aprovadas
        'moderador': moderador,
        'subjects': json.dumps(subjects_dict),
        'notify': True,
        }

    return render(request, 'home.html', json_data)


def logout_view(request):
    logout(request)
    return redirect ('home')
    
@login_required
def show_image(request):
    return render(request, 'show_images.html')

def check_is_moderator(user):
    try:
        moderador = ModerationOfSubjects.objects.get(pk=user.id)
        print (moderador)
    except ModerationOfSubjects.DoesNotExist:
        moderador = False
        print ("Não existe")

    return moderador

# Apenas moderadores podem acessar esta página
@user_passes_test(check_is_moderator)
def evaluate_submissions(request):
    user_logged_in = request.user
    try:
        moderador = ModerationOfSubjects.objects.get(pk=user_logged_in.id)
        print (moderador)
    except ModerationOfSubjects.DoesNotExist:
        moderador = False
    
    submissions = (user_logged_in.submissions.filter(subject = moderador.subject)).filter(approved=False)

    print (submissions[0].submission_date)

    if request.method == "POST":
        form = UpdateSubForm(request.POST or None, request.FILES or None)

        if request.POST['btn_aceitar']:
            submission = get_object_or_404(Submission, id=request.POST['submission_id'])
            # Salvando Submissão
            submission.subject = get_object_or_404(Subject, id=request.POST['submission_subject'])
            submission.submission_date = request.POST['submission_date']
            submission.description = request.POST['submission_description']
            submission.topic = request.POST['submission_topic']
            submission.uploader = user_logged_in
            submission.approved = True
            
            submission.save()

            return redirect('home')

        # Se rejeitar a submissão ele deleta o arquivo
        if request.POST['btn_rejeitar']:
            submission.delete()
            return redirect('home')            

        print (request.POST)

    else: # O que vai ser mostrado ao entrar na página  
        form = UpdateSubForm()

    # Criando dicionario com subjects para select de In-Place element #
    subjects_dict = {"": ""}
    x=1
    for subject in Subject.objects.all():
        subjects_dict[subject.name] = subject.name
        x+=1
        
    subjects_dict["selected"] = ""

    json_data = {
        # Submissões da discipliuna do moderador e que ainda não foram aprovadas
        'submissions': submissions,
        'moderador': moderador,
        'subjects':json.dumps(subjects_dict),
        'submission_form': form,
    }

    return render(request, 'evaluate_submissions.html', json_data)
