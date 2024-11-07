from django.db import models

class Category(models.Model):
    full_name = models.CharField(max_length=200)

    def __str__(self):
        return self.full_name

class Tag(models.Model):
    tag_text = models.CharField(max_length=50)
    pub_date = models.DateTimeField('date published')

    def __str__(self):
        return self.tag_text

class Article(models.Model):
    pub_date = models.DateTimeField('date published')
    headline = models.CharField(max_length=200)
    content = models.TextField()
    category = models.ForeignKey('Category', on_delete=models.CASCADE)
    tags = models.ManyToManyField('Tag')
    image = models.ImageField(upload_to='images/', blank=True,  null=True)
    additional_images = models.ManyToManyField('AdditionalImage', blank=True)
    def __str__(self):
        return self.headline
    
class AdditionalImage(models.Model):
    image = models.ImageField(upload_to='additional_images/')
    description = models.CharField(max_length=255, blank=True, null=True)

class Comment(models.Model):
    article = models.ForeignKey(Article, related_name='comments', on_delete=models.CASCADE)
    author_name = models.CharField(max_length=100)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f'Comment by {self.author_name} - {self.article.headline}'
