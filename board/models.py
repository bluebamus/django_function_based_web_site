from django.db import models

# Create your models here.


class Board(models.Model):
    title = models.CharField(max_length=128, verbose_name="제목")
    contents = models.TextField(verbose_name="내용")
    # TextField는 길이에 제한이 없음
    writer = models.ForeignKey("user.Usert", on_delete=models.CASCADE, verbose_name="글쓴이")
    tags = models.ManyToManyField("tag.Tag", verbose_name="태그")

    registered_dttm = models.DateTimeField(auto_now_add=True, verbose_name="등록시간")

    def __str__(self):
        return self.title

    class Meta:
        db_table = "board"
        verbose_name = "Board"
        verbose_name_plural = "Board"
