# Generated by Django 4.2.7 on 2023-11-09 01:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_qna'),
    ]

    operations = [
        migrations.CreateModel(
            name='Question_Answer',
            fields=[
                ('ID', models.CharField(max_length=200, primary_key=True, serialize=False)),
                ('user_key', models.CharField(max_length=200, null=True)),
                ('Question', models.CharField(default='질문', max_length=1000)),
                ('Answer', models.CharField(default='답변', max_length=200)),
                ('upvotes', models.IntegerField(default=0)),
                ('downvotes', models.IntegerField(default=0)),
                ('is_accepted', models.BooleanField(default=False)),
                ('view_count', models.IntegerField(default=0)),
                ('Keywords', models.CharField(max_length=200, null=True)),
                ('Date', models.DateTimeField(auto_now_add=True)),
                ('Links', models.CharField(max_length=200, null=True)),
            ],
        ),
    ]