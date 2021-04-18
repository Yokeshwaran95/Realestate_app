from django.utils.text import slugify
import random
import string

DONT_USE=['create']
def random_string_generator(size=10, chars=string.ascii_lowercase + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))
'''
random_string_generator is located here:
http://joincfe.com/blog/random-string-generator-in-python/
'''

def unique_slug_generator(instance, new_slug=None):
    """
    This is for a Django project and it assumes your instance 
    has a model with a slug field and a title character (char) field.
    """
    if new_slug is not None:
        title_slug = new_slug
    else:
        title_slug = slugify(instance.title)
    if title_slug in DONT_USE:
        new_slug = "{title_slug}-{randstr}".format(
                    title_slug=title_slug,
                    randstr=random_string_generator(size=4)
                )
        return unique_slug_generator(instance, new_slug=new_slug)

    Klass = instance.__class__
    qs_exists = Klass.objects.filter(title_slug=title_slug).exists()
    if qs_exists:
        new_slug = "{slug}-{randstr}".format(
                    title_slug=title_slug,
                    randstr=random_string_generator(size=4)
                )
        return unique_slug_generator(instance, new_slug=new_slug)
    return title_slug