# Generated by Django 5.0 on 2023-12-23 14:01

import ckeditor.fields
import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('dashboard', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Kelas',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('kelas', models.CharField(max_length=224)),
                ('bahasa', models.CharField(blank=True, choices=[('EN', 'English'), ('JP', 'Japan'), ('SA', 'Arab'), ('CN', 'China')], max_length=3)),
                ('slug', models.SlugField(max_length=30, null=True)),
                ('photo', models.FileField(default='kelas/default.jpg', upload_to='kelas')),
                ('keterangan', models.CharField(blank=True, max_length=224)),
                ('rangkuman', ckeditor.fields.RichTextField(blank=True, null=True)),
                ('defaultget', models.BooleanField(default=False)),
                ('biaya', models.IntegerField(default=0)),
                ('discount', models.IntegerField(default=0)),
                ('premium', models.BooleanField(default=False)),
                ('mahkota', models.IntegerField(default=0)),
                ('dilihat', models.IntegerField(default=0)),
                ('certificate', models.BooleanField(default=False)),
                ('rilis', models.BooleanField(default=False)),
                ('urutan', models.IntegerField(blank=True, null=True)),
                ('kategori', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='kategori_kelas', to='dashboard.kategori')),
                ('level', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='level_kelas', to='dashboard.level')),
            ],
        ),
        migrations.CreateModel(
            name='Creator',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('perubahan', models.CharField(max_length=225)),
                ('approve', models.BooleanField(default=False)),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='user_creator', to=settings.AUTH_USER_MODEL)),
                ('Kelas', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='kelas_creator', to='teacher.kelas')),
            ],
        ),
        migrations.CreateModel(
            name='Bab',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bab', models.CharField(max_length=50)),
                ('urutan', models.IntegerField(blank=True, null=True)),
                ('rangkuman', ckeditor.fields.RichTextField(blank=True, null=True)),
                ('premium', models.BooleanField(default=False)),
                ('kelas', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='kelas_bab', to='teacher.kelas')),
            ],
        ),
        migrations.CreateModel(
            name='Pelajaran',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('urutan', models.IntegerField(blank=True, null=True)),
                ('judul', models.CharField(max_length=224)),
                ('keterangan', models.CharField(default='belum ada keterangan', max_length=224)),
                ('vidio', models.URLField(blank=True, null=True)),
                ('text', ckeditor.fields.RichTextField()),
                ('date', models.DateField(auto_now_add=True)),
                ('approve', models.BooleanField(default=False)),
                ('bab_kelas', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='bab_kelas', to='teacher.bab')),
                ('kelas', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='kelas_pelajaran', to='teacher.kelas')),
            ],
        ),
        migrations.CreateModel(
            name='Games',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('level', models.IntegerField()),
                ('soal', models.CharField(max_length=224)),
                ('answer', models.CharField(max_length=224)),
                ('dummy', models.CharField(max_length=224)),
                ('penjelasan', models.TextField(default='Belum ada penjelasan')),
                ('approve', models.BooleanField(default=False)),
                ('bab_kelas', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='bab_games', to='teacher.bab')),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='user_games', to=settings.AUTH_USER_MODEL)),
                ('kelas', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='Games_kelas', to='teacher.kelas')),
                ('pelajaran', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='games_pelajaran', to='teacher.pelajaran')),
            ],
        ),
        migrations.CreateModel(
            name='Questions',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('soal', models.CharField(max_length=224)),
                ('answer', models.CharField(max_length=224)),
                ('wrong1', models.CharField(max_length=224)),
                ('wrong2', models.CharField(max_length=224)),
                ('wrong3', models.CharField(max_length=224)),
                ('penjelasan', models.TextField(default='Belum ada penjelasan')),
                ('approve', models.BooleanField(default=False)),
                ('bab_kelas', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='bab_question', to='teacher.bab')),
                ('category', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='quest_kategori', to='dashboard.kategori')),
                ('kelas', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='quest_kelas', to='teacher.kelas')),
                ('lesson', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='quest_pelajaran', to='teacher.pelajaran')),
                ('level', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='quest_level', to='dashboard.level')),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='user_question', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Room',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bahasa', models.CharField(blank=True, choices=[('EN', 'English'), ('JP', 'Japan'), ('SA', 'Arab'), ('CN', 'China')], default=1, max_length=3)),
                ('time', models.IntegerField(blank=True, choices=[(0, '07:30'), (1, '09:00'), (2, '10:30'), (3, '13:00'), (4, '14:30'), (5, '16:00'), (6, '18:30'), (7, '20:00')], default=1)),
                ('mulai', models.DateField(blank=True, null=True)),
                ('jadwal', models.IntegerField(blank=True, choices=[(0, "senin,  rabu, jum'at"), (1, 'selasa,  kamis, sabtu'), (2, "jum'at,  sabtu, minggu")], default=1)),
                ('level', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='level_akun_room', to='dashboard.levelakun')),
                ('mentor', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='teacher_room', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Schadule',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('terlaksana', models.BooleanField(default=False)),
                ('time', models.IntegerField(blank=True, choices=[(0, '07:30'), (1, '09:00'), (2, '10:30'), (3, '13:00'), (4, '14:30'), (5, '16:00'), (6, '18:30'), (7, '20:00')], default=1)),
                ('tanggal', models.DateField(blank=True, null=True)),
                ('level', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='level_akun_schadule', to='dashboard.levelakun')),
                ('mentor', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='mentor_schadule', to=settings.AUTH_USER_MODEL)),
                ('room', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='teacher_schadule_room', to='teacher.room')),
            ],
        ),
        migrations.CreateModel(
            name='Teacher',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('link', models.CharField(default='https://zoom.us/', max_length=50, null=True)),
                ('password', models.CharField(blank=True, max_length=50, null=True)),
                ('credits', models.IntegerField(default=0)),
                ('api_key', models.CharField(max_length=50, null=True)),
                ('secret_key', models.CharField(max_length=50, null=True)),
                ('desc', models.CharField(max_length=225, null=True)),
                ('mastered', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='Master_of_teacher', to='dashboard.master')),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='user_of_teacher', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='VocabGroup',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('english', models.CharField(max_length=50)),
                ('indo', models.CharField(max_length=50)),
                ('img', models.FileField(default='media/vocabgroup/default.jpg', upload_to='media/vocabgroup')),
                ('level', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='vocab_group_level', to='dashboard.level')),
            ],
        ),
        migrations.CreateModel(
            name='Vocab',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('english', models.CharField(max_length=50)),
                ('indo', models.CharField(max_length=50)),
                ('success', models.IntegerField(default=0)),
                ('failed', models.IntegerField(default=0)),
                ('group', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='vocab_group', to='teacher.vocabgroup')),
            ],
        ),
        migrations.CreateModel(
            name='Withdrow',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('jumlah', models.IntegerField(default=0)),
                ('bank', models.CharField(max_length=30)),
                ('no_bank', models.CharField(max_length=18)),
                ('penerima', models.CharField(max_length=50)),
                ('tgl', models.DateField()),
                ('approve', models.BooleanField(default=False)),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='user_withdrow', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]