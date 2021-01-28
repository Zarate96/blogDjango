from django.db import models
from ckeditor.fields import RichTextField

# Create your models here.

class Category(models.Model):
    name = models.CharField('Category name', max_length=100, null=False, blank=False)
    state = models.BooleanField('Category state', default=True)
    date_creation = models.DateField('Cretion date', auto_now=False, auto_now_add = True)

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.name

class Author(models.Model):
    name = models.CharField('Author name', max_length=100, null=False, blank=False)
    last_name = models.CharField('Category name', max_length=100, null=False, blank=False)
    facebook = models.URLField('Facebook', max_length=100, null=True, blank=True)
    instagram = models.URLField('Instagram', max_length=100, null=True, blank=True)
    site_web = models.URLField('Site web', max_length=100, null=True, blank=True)
    email = models.EmailField('Category name', max_length=100, null=False, blank=False)
    state = models.BooleanField('Author state', default=True)
    date_creation = models.DateField('Cretion date', auto_now=False, auto_now_add = True)

    class Meta:
        verbose_name = 'Author'
        verbose_name_plural = 'Authors'

    def __str__(self):
        return "{0},{1}".format(self.last_name, self.name)

class Post(models.Model):
    title = models.CharField('Title', max_length=100, null=False, blank=False)
    slug = models.CharField('Slug', max_length=100, null=False, blank=False)
    description = models.CharField('Description', max_length=150, null=False, blank=False)
    content = RichTextField('Content')
    image = models.URLField('Image', max_length=150, null=False, blank=False)
    author = models.ForeignKey(Author, on_delete = models.CASCADE)
    category = models.ForeignKey(Category, on_delete = models.CASCADE)
    state = models.BooleanField('Post state', default=True)
    date_creation = models.DateField('Cretion date', auto_now=False, auto_now_add = True)

    class Meta:
        verbose_name = 'Post'
        verbose_name_plural = 'Posts'

    def __str__(self):
        return self.title
