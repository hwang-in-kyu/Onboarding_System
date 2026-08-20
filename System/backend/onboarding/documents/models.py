from django.db import models
from accounts.models import User
from onboarding.models import OnboardingStep

class Documents(models.Model) :
    """문서 - """

    uploader =          models.ForeignKey(User, on_delete=models.PROTECT, related_name="documents_uploader", verbose_name="업로더 아이디")
    onboarding_step =   models.ForeignKey(OnboardingStep, on_delete=models.SET_NULL, null=True, blank=True, related_name="documents_onboarding_step", verbose_name="온보딩 스텝 아이디")

    document_title =    models.CharField(max_length=200, verbose_name="문서 제목")
    file_path =         models.CharField(max_length=500, verbose_name="문서 경로")

    class Meta :
        db_table = "documents"

    def __str__(self) :
        return self.document_title