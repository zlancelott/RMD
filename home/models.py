from django.db import models

from django.contrib.auth.models import (
	AbstractBaseUser, BaseUserManager, AbstractUser
)


# Usuário
class User(AbstractUser):
	email = models.EmailField(max_length=255, unique=True, blank=False)
	gender = models.CharField(max_length=1, blank=False)

	USERNAME_FIELD = 'email'

	REQUIRED_FIELDS = ['username']

	def __str__(self):
		return self.first_name

	class Meta:
		db_table = 'home_user'
		managed =True


class Subject(models.Model):
	name = models.CharField(max_length=100)
	course = models.CharField(max_length=150, default="Ciências da Computação")
	semester = models.CharField(max_length=2)

	student = models.ManyToManyField(User, related_name="subjects", null=True)

	def __str__(self):
		return self.name

	class Meta:
		db_table = 'home_subject'
		managed =True


class ModerationOfSubjects(models.Model):
	student = models.OneToOneField(User, on_delete=models.CASCADE, related_name='moderador', primary_key=True)
	subject = models.OneToOneField(Subject, on_delete=models.CASCADE, null=True)

	class Meta:
		db_table = 'home_moderationofsubjects'
		managed =True

	def __str__(self):
		return self.student.first_name + " modera a disciplina " + self.subject.name



class Submission(models.Model):
	approved = models.BooleanField(default=False)
	description =  models.TextField(max_length=250)
	topic = models.CharField(max_length=100)
	submission_time = models.DateTimeField(auto_now_add=True)
	submission_date = models.DateField()

	subject = models.ForeignKey(Subject, on_delete=models.CASCADE, related_name="subject_submissions")
	
	uploader = models.ForeignKey(User, on_delete=models.DO_NOTHING, related_name="submissions")
	moderator = models.ForeignKey(ModerationOfSubjects, on_delete=models.DO_NOTHING, related_name="moderator", null=True)

	def __str__(self):
		return self.topic


class File(models.Model):
	file_image = models.ImageField(upload_to="photos/", null=False)

	submission = models.ForeignKey(Submission, on_delete=models.CASCADE, related_name="files")

	def __str__(self):
		return self.submission.topic
