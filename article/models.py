from django.db import models
from ckeditor.fields import RichTextField
# Create your models here.
class Article(models.Model):
    author = models.ForeignKey("auth.User", verbose_name=("Yazar"), on_delete=models.CASCADE)
    title = models.CharField(max_length= 50,verbose_name=("Baslik"))
    content = RichTextField()
    
    created_date = models.DateTimeField(auto_now=False, auto_now_add=True,verbose_name=("0lusturma_tarihi"))
    a_image = models.FileField(blank = True,null = True,verbose_name=("makaleye resim"))

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-created_date']

class Comment(models.Model):
    article = models.ForeignKey(Article,verbose_name=("makale"), on_delete=models.CASCADE,related_name="comments")
    comment_author = models.CharField(max_length=51,verbose_name="yazar")
    comment_content= models.CharField(max_length=211,verbose_name="yorum")
    comment_date = models.DateTimeField(auto_now=False, auto_now_add=True,verbose_name=("yorum_tarihi"))
    def __str__(self):
        return self.comment_content
    class Meta:
        ordering = ['-comment_date']