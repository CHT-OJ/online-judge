# Generated by Django 3.2.18 on 2024-09-03 14:33

from django.db import migrations, models


def migrate_problems_to_courselessonproblem(apps, schema_editor):
    CourseLesson = apps.get_model("judge", "CourseLesson")
    CourseLessonProblem = apps.get_model("judge", "CourseLessonProblem")

    for lesson in CourseLesson.objects.all():
        for problem in lesson.problems.all():
            CourseLessonProblem.objects.create(
                lesson=lesson, problem=problem, order=1, score=1
            )


class Migration(migrations.Migration):

    dependencies = [
        ("judge", "0192_course_lesson_problem"),
    ]

    operations = [
        migrations.RunPython(migrate_problems_to_courselessonproblem),
        migrations.RemoveField(
            model_name="courselesson",
            name="problems",
        ),
    ]