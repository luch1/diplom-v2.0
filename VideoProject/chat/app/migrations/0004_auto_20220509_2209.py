import ckeditor_uploader.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_auto_20211013_1529'),
    ]

    operations = [
        migrations.CreateModel(
            name='Room',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('room_name', models.TextField(verbose_name='Название комнаты')),
            ],
        ),
        migrations.AddField(
            model_name='userprofile',
            name='avatar',
            field=ckeditor_uploader.fields.RichTextUploadingField(default=''),
        ),
    ]
