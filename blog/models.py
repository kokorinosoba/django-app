from django.conf import settings
from django.db import models
from django.utils import timezone


class Post(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title


class Credits(models.Model):
    lessons = (
        (10010010, "スタートアップセミナー", 1),
        (10110010, "総合英語Ｉａ", 2),
        (10110020, "総合英語Ｉｂ", 2),
    )

    field = {}

    for lesson in lessons:
        user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
        field[str(lesson[0]) + "DOING"] = models.BooleanField()
        field[str(lesson[0]) + "DONE"] = models.BooleanField()

    def __str__(self):
        return "Lesson"
