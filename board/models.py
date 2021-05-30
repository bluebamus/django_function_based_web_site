from django.db import models
import os
from uuid import uuid4
from django.utils import timezone

# Create your models here.


def date_upload_to(instance, filename):
    # upload_to="%Y/%m/%d" 처럼 날짜로 세분화
    ymd_path = timezone.now().strftime("%Y/%m/%d")
    # 길이 32 인 uuid 값
    uuid_name = uuid4().hex
    # 확장자 추출
    extension = os.path.splitext(filename)[-1].lower()
    # 결합 후 return
    return "/".join(
        [
            ymd_path,
            uuid_name + extension,
        ]
    )

# def upload_to_func(instance, filename):
#     prefix = timezone.now().strftime("%Y/%m/%d")
#     file_name = uuid4().hex
#     extension = os.path.splitext(filename)[-1].lower() # 확장자 추출
#     return "/".join(
#         [prefix, file_name, extension,]
#     )


class Board(models.Model):
    title = models.CharField(max_length=128, verbose_name="제목")
    contents = models.TextField(verbose_name="내용")
    # TextField는 길이에 제한이 없음
    writer = models.ForeignKey("user.Usert", on_delete=models.CASCADE, verbose_name="글쓴이")
    tags = models.ManyToManyField("tag.Tag", verbose_name="태그", blank=True)

    registered_dttm = models.DateTimeField(auto_now_add=True, verbose_name="등록시간")
    photo = models.ImageField(upload_to=date_upload_to, verbose_name="이미지")
    #photo = models.ImageField(upload_to=date_upload_to, blank=True, null=True, default='default/no_img_lg.png', verbose_name="이미지")

    def delete(self, *args, **kwargs):
        if self.photo!='default/no_img_lg.png':
            self.photo.delete()        
        super().delete(*args, **kwargs)

    # def delete(self, *args, **kargs):
    #     if self.upload_files:
    #         os.remove(os.path.join(settings.MEDIA_ROOT, self.upload_files.path))
    #     super(Notice, self).delete(*args, **kargs)

    def __str__(self):
        return self.title

    class Meta:
        db_table = "board"
        verbose_name = "Board"
        verbose_name_plural = "Board"
