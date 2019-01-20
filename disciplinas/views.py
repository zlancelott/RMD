from django.shortcuts import render

def disciplina(request, disciplina):
    user_logged_in = request.user

    info2 = {'disciplinas':[], 'aulas':[]}

    #Turmas em que o usuário está matriculado
    subject_classes = user_logged_in.subjectclasses.all()


    # Obtendo a turma atual
    for subject_class in subject_classes:
        if subject_class.subject.name == disciplina:
            current_class = subject_class
            break

    json_data = {
        # Turmas
        'subject_classes': [i for i in subject_classes],
        'current_class': subject_class
    }


    return render(request, 'aulas.html', json_data)

def photos_class(request, disciplina):
    current_user = request.user

    #Turmas em que o usuário está matriculado
    subject_classes = current_user.subjectclasses.all()


    # Obtendo a turma atual
    for subject_class in subject_classes:
        if subject_class.subject.name == disciplina:
            current_class = subject_class
            break

    # Obtendo Aulas dessa disciplina
    lessons = current_class.lessons.all()



    ### TEM QUE SABER EM QUE AULA ELE ESTÁ (RECEBER COMO PARAMETRO DA FUNCAO E DA URL)

    # Arquivos da Disciplina (Nesse exemplo, eu peguei a Aula da posição 0)
    # Arquivos da aula de posição 0
    lessons_files = lessons[0].lesson.all().filter(evaluated=True) # Mostra apenas as imagens avaliadas
 
    name_lessons_files = []
    for lesson_file in lessons_files:
        name_lessons_files.append(lesson_file.file_image)


    json_data = {
        #Turmas
        'subject_classes':list(subject_classes),
        'name_files':name_lessons_files
    }

    return render(request, 'photos_class.html', json_data)