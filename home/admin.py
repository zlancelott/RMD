from django.contrib import admin
from .models import User, Subject, ModerationOfSubjects, Submission, File


# Register your models here.
admin.site.register(User)
admin.site.register(Subject)
admin.site.register(ModerationOfSubjects)
admin.site.register(Submission)
admin.site.register(File)


