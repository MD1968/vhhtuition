# Generated by Django 3.0.8 on 2021-03-02 14:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('assessments', '0002_assessment_description'),
    ]

    operations = [
        migrations.AddField(
            model_name='question',
            name='question_number',
            field=models.CharField(blank=True, max_length=2, null=True),
        ),
    ]
