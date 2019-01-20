from django.shortcuts import render, redirect,  get_object_or_404
from django.contrib.auth.decorators import login_required

import sys

sys.path.append("..")

# from home.models import LessonFile


# @login_required
# def user_profile(request, user_id):
#     user_logged_in = request.user

#     # Turmas em que o usuário está matriculado
#     subject_classes = user_logged_in.subjectclasses.all()

#     moderador = user_logged_in.moderador.all()[0].is_mod

#     # Arquivos submetidos por este usuário
#     lessons_files = user_logged_in.lessonFile_author.all()

#     json_data = {
#         #Turmas
#         'subject_classes':list(subject_classes),
#         'moderador': moderador,
#         'lessons_files' : lessons_files,
#     }


#     return render(request, 'user_profile.html', json_data)


# ## Aqui é melhor que seja uma avaliação de Administrador
# @login_required
# def delete_submission(request, lesson_file_id):
#     lesson_file = get_object_or_404(LessonFile, id=lesson_file_id)

#     if request.method == 'POST':
#         if 'btn_rejeitar'in request.POST:
#             lesson_file.delete()
#             return redirect('home')