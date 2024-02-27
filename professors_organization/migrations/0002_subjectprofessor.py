# Generated by Django 4.1.7 on 2023-03-07 21:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('catalogs', '0007_maritalstatus'),
        ('core', '0001_initial'),
        ('professors_organization', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='SubjectProfessor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('group_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='professors_organization.group')),
                ('professor_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.professor')),
                ('subject_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='catalogs.subject')),
            ],
        ),
    ]