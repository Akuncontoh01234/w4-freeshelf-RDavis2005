from django.db import models

#Category
class Category(models.Model):
    name = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200, unique=True)

    class Meta:
        ordering = ('name',)
        verbose_name = 'category'
        verbose_name_plural = 'categories'

    def __str__(self):
        return self.name

#Book
class Book(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE,
        default=Category.objects.get(name='general'))
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=255)
    description = models.TextField()
    date_added = models.DateTimeField(auto_now=True)
    slug = models.SlugField(unique=True)
    image = models.ImageField(default='default.png', blank=True)