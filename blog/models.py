import datetime
import markdown
import hashlib

from django.db import models
from django.conf import settings

class Category(models.Model):
    name = models.CharField(max_length=60)
    value = models.CharField(max_length=60, default='')

    def __str__(self):
        return self.name


class Image(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to="blog/static/img/")

    def __str__( self ):
        return self.name


class Post(models.Model):
    title = models.CharField(max_length=255)
    brother_code = models.CharField(max_length=128, null=True)
    code = models.CharField(max_length=128)
    body = models.TextField()
    active = models.BooleanField(default=True)
    language = models.CharField(
        max_length=5,
        choices=settings.LANGUAGES,
        default='pt-br',
    )
    created_on = models.DateTimeField(auto_now_add=True)
    last_modified = models.DateTimeField(auto_now=True)
    cover = models.ImageField(upload_to='img/')
    categories = models.ManyToManyField('Category', related_name='posts')

    def __str__( self ):
        return self.title


class Comment(models.Model):
    author = models.CharField(max_length=60)
    email = models.CharField(max_length=60)
    body = models.TextField()
    gravatar = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    post = models.ForeignKey('Post', on_delete=models.CASCADE)

    def __str__( self ):
        return self.author + " - " + self.created_on.date
    
    def gravatar_url(self):
        # Get the md5 hash of the email address
        md5 = hashlib.md5(self.email.encode())
        digest = md5.hexdigest()
        return 'http://www.gravatar.com/avatar/{}'.format(digest)


def markdown_to_html( markdownText, images ):    
    image_ref = ""

    for image in images:
        image_url = settings.MEDIA_URL + image.image.url
        image_ref = "%s\n[%s]: %s" % ( image_ref, image, image_url )

    md = "%s\n%s" % ( markdownText, image_ref )
    html = markdown.markdown( md )

    return html
