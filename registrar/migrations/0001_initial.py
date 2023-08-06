# Generated by Django 4.2.4 on 2023-08-06 05:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=50)),
                ('middle_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
                ('date_of_birth', models.DateField()),
                ('gender', models.CharField(choices=[('M', 'male'), ('F', 'female')], max_length=50)),
                ('email', models.EmailField(max_length=254)),
                ('phone', models.CharField(max_length=50)),
                ('address', models.CharField(max_length=50)),
                ('school', models.CharField(max_length=50)),
                ('school_address', models.CharField(max_length=50)),
                ('grade', models.IntegerField()),
                ('cgpa', models.DecimalField(decimal_places=2, max_digits=4)),
                ('intended_major1', models.CharField(max_length=50)),
                ('intended_major2', models.CharField(max_length=50)),
                ('intended_major3', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Attachment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('attachment', models.FileField(upload_to='attachments/')),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='attachments', to='registrar.student')),
            ],
            options={
                'ordering': ['student__first_name', 'student__last_name', 'attachment'],
            },
        ),
    ]