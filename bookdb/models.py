from django.db import models
from django.forms import ModelForm

# Create your models here.

TITLE_CHOICES = (
	('MR', 'Mr.'),
	('MRS', 'Mrs.'),
	('MS.', 'Ms.'),
)

class Author(models.Model):
	name = model.CharField(max_length=100)
	title = model.CharField(max_length=3, choice=TITLE_CHOICES)
	birth_date = models.DateField(blank=True, null=True)

	def __unicode__(self):
		return self.name

class Book(models.Model):
	name = model.CharField(max_length=100)
	authors = models.ManyToManyField(Author)

class AuthorForm(ModelForm):
	class Meta:
		model = Author

class BookForm(ModelForm):
	class Meta:
		model = Book

