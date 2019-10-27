from django.db import models
# from .models import File

# Create your models here.
class Note(models.Model):
	# title = models.CharField(max_length=200, default=True)
	success = models.BooleanField(default=True)
	img_url = models.TextField(default=True)
	# created_at=models.DateTimeField(auto_now_add=True)
	# file = models.FileField(blank=False, null=False)
#__str__ nadpisuje nazwę rejestru wartościami zwracanymi w funkcji
#w moim przypadku deafaultowa nazwa nadpisana zostanie przez tytuł i opis
	def __str__(self):
		return '{}'.format(self.img_url)
		# self.title, self.body
		# self.file.name
		
