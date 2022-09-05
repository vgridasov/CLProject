from django.db import models
from django.urls import reverse
from django.utils import timezone
from django.contrib.auth.models import User


class Analysis(models.Model):
    reg = models.PositiveIntegerField(primary_key=True, verbose_name='РЕГ')  # РЕГ
    code = models.CharField(max_length=10, verbose_name='МО')  # CODE
    otdelen = models.CharField(max_length=10, verbose_name='ОТДЕЛЕНИЕ', null=True, blank=True)  # OTDELEN
    last_name = models.CharField(max_length=60, verbose_name='ФАМИЛИЯ', null=True, blank=True)  # ФАМИЛИЯ
    first_name = models.CharField(max_length=60, verbose_name='ИМЯ', null=True, blank=True)  # ИМЯ
    middle_name = models.CharField(max_length=60, verbose_name='ОТЧЕСТВО', null=True, blank=True)  # ОТЧЕСТВО
    gender = models.CharField(max_length=5, verbose_name='ПОЛ', null=True, blank=True)  # ПОЛ
    b_date = models.DateField(verbose_name='ДАТА РОЖДЕНИЯ', null=True, blank=True)  # ДАТА_РОЖД
    policy = models.CharField(max_length=18, null=True, blank=True)  # ПОЛИС
    snils = models.CharField(max_length=14, null=True, blank=True, verbose_name='СНИЛС')  # СНИЛС
    address = models.CharField(max_length=150, null=True, blank=True, verbose_name='АДРЕС')  # АДРЕС
    kl_diag = models.TextField(max_length=255, null=True, blank=True, verbose_name='КЛ_ДИАГ')  # КЛ_ДИАГ
    v_date = models.DateField(verbose_name='ДАТА ВЗЯТ', null=True, blank=True)  # ДАТА_ВЗЯТ
    p_date = models.DateField(verbose_name='ДАТА ПОСТ', null=True, blank=True)  # ДАТА_ПОСТ
    reg_date = models.DateField(verbose_name='ДАТА РЕГ', null=True, blank=True)  # ДАТА_РЕГ
    an_object = models.TextField(verbose_name='ОБЪЕКТ', null=True, blank=True)  # ОБЪЕКТ
    doctor = models.CharField(max_length=20, verbose_name='ДОКТОР', null=True, blank=True)  # ДОКТОР
    vyr_date = models.DateField(verbose_name='ДАТА ВЫРЕЗ', null=True, blank=True)#  ДАТА_ВЫРЕЗ
    macro = models.TextField(verbose_name='МАКРО', null=True, blank=True)  # МАКРО
    macro_p_a = models.CharField(max_length=20, verbose_name='МАКРО_п_а', null=True, blank=True)  # МАКРО_п_а
    micro = models.TextField(verbose_name='МИКРО', null=True, blank=True)  # МИКРО
    zakl = models.TextField(verbose_name='ЗАКЛ', null=True, blank=True)  # ЗАКЛ
    comment = models.TextField(verbose_name='КОММЕНТ', null=True, blank=True)  # КОММЕНТ
    mcode1 = models.CharField(max_length=6, verbose_name='кодмедусл1', null=True, blank=True)  # кодмедусл1
    mcode1_num = models.SmallIntegerField(verbose_name='кол_кодмедусл1', null=True, blank=True)  # кол_кодмедусл1
    mcode2 = models.CharField(max_length=6, verbose_name='кодмедусл2', null=True, blank=True)  # кодмедусл2
    mcode2_num = models.SmallIntegerField(verbose_name='кол_кодмедусл2', null=True, blank=True)  # кол_кодмедусл2
    code1 = models.CharField(max_length=5, verbose_name='код', null=True, blank=True)  # код
    complexity = models.SmallIntegerField(verbose_name='кол_кодмедусл2', null=True, blank=True)  # Сложность
    p_a = models.CharField(max_length=20, verbose_name='п_а', null=True, blank=True)  # п_а
    a_date = models.DateField(verbose_name='ДАТА ИССЛ', null=True, blank=True)  # ДАТА_ИССЛ
    # created_by = models.ForeignKey(User, on_delete=models.CASCADE)
    # last_edit_date = models.DateTimeField(verbose_name='Дата посл. изменения', auto_now=True)

    def get_age(self):
        if self.b_date:
            age = self.v_date.year - self.b_date.year
        else:
            age = None
        return age

    def get_gender(self):
        if self.gender:
            g = self.gender[2:5]
        else:
            g = "-"
        return g

    def get_fio(self):
        return '%s %s. %s.' % (str(self.last_name), str(self.first_name)[0], str(self.middle_name)[0])

    def get_absolute_url(self):
        return reverse('detail', kwargs={'pk': self.pk})

    def __str__(self):
        return '%s: [%s] %s %s' % (self.reg, self.a_date, self.last_name, self.first_name)

    class Meta:
        verbose_name = 'Исследование'
        verbose_name_plural = 'Исследования'
        ordering = ['-reg']
