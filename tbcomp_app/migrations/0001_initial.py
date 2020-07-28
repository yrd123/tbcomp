# Generated by Django 2.2.14 on 2020-07-28 14:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Activity',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('files', models.FileField(blank=True, null=True, upload_to='activities')),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fullName', models.CharField(max_length=20)),
                ('college', models.CharField(max_length=50)),
                ('branch', models.CharField(max_length=50)),
                ('year', models.CharField(max_length=20)),
                ('email', models.EmailField(max_length=254)),
                ('password', models.CharField(max_length=20)),
                ('confirmPassword', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Subject',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Topic',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('subject', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Topic', to='tbcomp_app.Subject')),
            ],
        ),
        migrations.CreateModel(
            name='StudentUpload',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('files', models.FileField(blank=True, null=True, upload_to='uploads')),
                ('status', models.CharField(choices=[('approved', 'approved'), ('uploaded', 'uploaded')], max_length=20)),
                ('name', models.CharField(max_length=20)),
                ('activity', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='StudentUpload', to='tbcomp_app.Activity')),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='StudentUpload', to='tbcomp_app.Student')),
            ],
        ),
        migrations.CreateModel(
            name='Document',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('files', models.FileField(blank=True, null=True, upload_to='files')),
                ('topic', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Document', to='tbcomp_app.Topic')),
            ],
        ),
        migrations.AddField(
            model_name='activity',
            name='topic',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Activity', to='tbcomp_app.Topic'),
        ),
    ]
