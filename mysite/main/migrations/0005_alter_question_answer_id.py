# Generated by Django 4.2.3 on 2023-11-09 10:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("main", "0004_alter_question_answer_date"),
    ]

    operations = [
        migrations.AlterField(
            model_name="question_answer",
            name="ID",
            field=models.AutoField(
                auto_created=True, primary_key=True, serialize=False
            ),
        ),
    ]