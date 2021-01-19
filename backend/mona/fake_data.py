import os, sys
sys.path.append('/kevin/Hikari/hikari')
os.environ['DJANGO_SETTINGS_MODULE'] = 'project_name.settings'
import django
django.setup()

from mona.models import Category
from mona.constants import imagenet_classes

for (class_id, value) in imagenet_classes.items():
    name = value.split(",")[0]
    category = Category(
        name=name,
        content=value,
        class_id=class_id
    )
    category.save()