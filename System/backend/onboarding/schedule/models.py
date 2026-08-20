from django.db import models
from accounts.models import User

class Schedule(models.Model) :
    """스케줄"""

    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="schedules", verbose_name="사용자 아이디")
    schedule_title = models.CharField(max_length=100, verbose_name="스케줄 제목")
    schedule_content = models.TextField(verbose_name="스케줄 내용")
    schedule_date = models.DateField(verbose_name="스케줄 날짜")
    is_shared = models.BooleanField(default=False, verbose_name="공유 여부")

    class Meta :
        db_table = "schedule"

    def __str__(self) :
        return f"{self.schedule_title} - {self.user.name} - {self.schedule_date}"