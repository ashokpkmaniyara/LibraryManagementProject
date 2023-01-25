# Generated by Django 4.1.4 on 2023-01-19 04:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Book_Name', models.CharField(max_length=30)),
                ('Author_Name', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Course_Name', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Stud_Name', models.CharField(max_length=30)),
                ('Stud_Phone', models.BigIntegerField()),
                ('Stud_Password', models.CharField(max_length=30)),
                ('Stud_Semester', models.IntegerField()),
                ('Stud_Course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='management.course')),
            ],
        ),
        migrations.CreateModel(
            name='Issue_Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Issued_Date', models.DateField()),
                ('Valid_Till', models.DateField()),
                ('Book_Name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='management.book')),
                ('Student_Name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='management.student')),
            ],
        ),
        migrations.AddField(
            model_name='book',
            name='Course_ID',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='management.course'),
        ),
    ]
