from django.db import models
from accounts.models import Dept, Role

class OnboardingTrack(models.Model) :
    """온보딩 트랙 - 부서/직군 조건으로 배정되는 온보딩 트랙을 설정하는 모델"""

    role =                      models.ForeignKey(Role, on_delete=models.SET_NULL, null=True, blank=True, related_name="onboarding_tracks", verbose_name="직군 아이디")
    dept =                      models.ForeignKey(Dept, on_delete=models.SET_NULL, null=True, blank=True, related_name="onboarding_tracks", verbose_name="부서 아이디")
    onboardingtrack_name =      models.CharField(max_length=100, verbose_name="트랙명")

    class Meta :
        db_table = "onboardingtrack"

    def __str__(self) :
        return self.onboardingtrack_name

class OnboardingStep(models.Model) :
    """온보딩 단계 - 온보딩 트랙에 속하는 단계들을 설정하는 모델"""

    onboarding_track =          models.ForeignKey(OnboardingTrack, on_delete=models.CASCADE, related_name="onboarding_steps", verbose_name="온보딩 트랙 아이디")
    onboardingstep_sequence =   models.IntegerField(verbose_name="스텝 순서")
    onboardingstep_title =      models.CharField(max_length=100, verbose_name="스텝 제목")
    onboardingstep_content =    models.TextField(verbose_name="스텝 내용")

    class Meta :
        db_table = "onboardingstep"
        ordering = ["onboardingstep_sequence"]

    def __str__(self) :
        return f"[{self.onboardingstep_sequence}] - {self.onboardingstep_title}"