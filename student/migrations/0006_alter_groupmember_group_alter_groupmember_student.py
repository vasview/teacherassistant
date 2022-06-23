# Generated by Django 4.0.3 on 2022-06-18 19:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0005_studentreview_teacher'),
    ]

    operations = [
        migrations.AlterField(
            model_name='groupmember',
            name='group',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='group_members', to='student.group'),
        ),
        migrations.AlterField(
            model_name='groupmember',
            name='student',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='student_groups', to='student.student'),
        ),
    ]