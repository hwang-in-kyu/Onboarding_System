from django.db import models
from django.contrib.auth.base_user import AbstractBaseUser, BaseUserManager
from django.contrib.auth.models import PermissionsMixin

class Rank(models.Model) :
    """직급"""
    rank_name = models.CharField(max_length=50, verbose_name="직급명")

    class Meta:
        db_table = "rank"           # 기본값(accounts_rank) 대신 ERD와 동일한 rank 테이블명 사용

    def __str__(self) :
        return self.rank_name

class Dept(models.Model) :
    """부서"""
    dept_name = models.CharField(max_length=50, verbose_name="부서명")

    class Meta :
        db_table = "dept"           # 기본값(accounts_dept) 대신 ERD와 동일한 dept 테이블명 사용

    def __str__(self) :
        return self.dept_name

class Role(models.Model) :
    """직군"""
    role_name = models.CharField(max_length=50, verbose_name="직군명(ex: 개발, 기획, 디자인 등)")

    class Meta :
        db_table = "role"           # 기본값(accounts_role) 대신 ERD와 동일한 role 테이블명 사용

    def __str__(self) :
        return self.role_name

class UserManager(BaseUserManager) :
    """
    User의 objects 매니저.
    Django 기본 UserManager는 username 기준이라 그대로 못 쓰고,
    employee_num(사원번호) 기준으로 계정을 만들도록 재정의함.
    """

    def create_user(self, employee_num, name, password=None, **extra_fields) :
        """일반 사용자 계정 생성"""

        if not employee_num :
            raise ValueError("사원 번호를 입력해주세요.")
        user = self.model(employee_num=employee_num, name=name, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user


    def create_superuser(self, employee_num, name, password=None, **extra_fields) :
        """관리자(슈퍼유저) 계정 생성 - create_user를 그대로 재사용"""

        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)

        if extra_fields.get("is_staff") is not True :
            raise ValueError("직원이 아닙니다.")

        if extra_fields.get("is_superuser") is not True :
            raise ValueError("슈퍼유저가 아닙니다.")

        return self.create_user(employee_num, name, password=password, **extra_fields)

class User(AbstractBaseUser, PermissionsMixin) :
    """사용자 - 사원번호 기반 로그인"""
    dept = models.ForeignKey(Dept, on_delete=models.PROTECT, related_name="users")
    rank = models.ForeignKey(Rank, on_delete=models.PROTECT, related_name="users")
    role = models.ForeignKey(Role, on_delete=models.PROTECT, related_name="users")

    onboarding_track = models.ForeignKey("onboarding.OnboardingTrack", on_delete=models.SET_NULL, null=True, blank=True, related_name="users")

    name = models.CharField(max_length=50, verbose_name="이름")
    employee_num = models.CharField(max_length=50, unique=True, verbose_name="사원번호")

    is_first = models.BooleanField(default=True, verbose_name="최초 로그인 여부")

    hire_date = models.DateField(verbose_name="입사일")

    is_active = models.BooleanField(default=True, verbose_name="계정 활성화 여부")
    is_staff = models.BooleanField(default=False, verbose_name="관리자 페이지 접속 권한 여부")

    objects = UserManager()

    USERNAME_FIELD = "employee_num"         # abstractbaseuser에서 username_field를 employee_num으로 지정
    REQUIRED_FIELDS = ["name"]              # createsuperuser 명령어로 관리자 계정을 만들 때, 사원번호/비밀번호 외에 추가로 꼭 물어봐야 할 항목을 지정

    class Meta :
        db_table = "users"

    def __str__(self) :
        return f"{self.name}({self.employee_num})"