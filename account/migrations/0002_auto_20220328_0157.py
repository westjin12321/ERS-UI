# Generated by Django 3.1.3 on 2022-03-27 16:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='account',
            options={'verbose_name': '사용자 계정', 'verbose_name_plural': '사용자 계정'},
        ),
        migrations.RemoveField(
            model_name='account',
            name='email',
        ),
        migrations.RemoveField(
            model_name='account',
            name='name',
        ),
        migrations.AddField(
            model_name='account',
            name='useremail',
            field=models.EmailField(default='', max_length=128, verbose_name='이메일'),
        ),
        migrations.AddField(
            model_name='account',
            name='username',
            field=models.CharField(default='', max_length=32, verbose_name='이름'),
        ),
        migrations.AlterField(
            model_name='account',
            name='password',
            field=models.CharField(default='', max_length=64, verbose_name='비밀번호'),
        ),
    ]