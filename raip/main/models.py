from django.contrib.auth import get_user_model
from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator


User = get_user_model()

CHOICE_GEN = [
    ('w', 'Женщина'),
    ('m', 'Мужчина')
]


class Patient(models.Model):
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='patients'
    )

    name = models.SlugField(
        max_length=100,
        unique=True
    )

    age = models.PositiveIntegerField(
        verbose_name='Введите возвраст пациента',
        default=0,
        validators=[MinValueValidator(0), MaxValueValidator(100)]
    )

    gender = models.CharField(
        verbose_name='Пол пациента',
        choices=CHOICE_GEN,
        max_length=1
    )

    created = models.DateTimeField(
        verbose_name='Дата создания',
        auto_now_add=True,
        db_index=True
    )

    class Meta:
        ordering = ('-created',)

    def __str__(self):
        return self.name


class HistoryUser(models.Model):
    patient = models.ForeignKey(
        Patient,
        on_delete=models.CASCADE,
        related_name='patient_pred',
        verbose_name='Введите имя пациента'
    )

    pub_date = models.DateTimeField(
        verbose_name='Дата создания',
        auto_now_add=True,
        db_index=True
    )

    image = models.ImageField(
        verbose_name='Снимок МРТ',
        upload_to='image/'
    )

    result = models.CharField(
        verbose_name='Результат распознования',
        max_length=20
    )

    class Meta:
        ordering = ('-pub_date',)

    def __str__(self):
        return self.author.username


class VKResult(models.Model):
    patient = models.ForeignKey(
        Patient,
        on_delete=models.CASCADE,
        related_name='patient_res'
    )

    pub_date = models.DateTimeField(
        'Дата создания',
        auto_now_add=True,
        db_index=True
    )

    result_vkr = models.FloatField(
        verbose_name='Результата VKR',
        null=True, blank=True
    )

    wbc = models.FloatField(
        null=True, blank=True
    )

    lymf = models.FloatField(
        null=True, blank=True
    )

    mon = models.FloatField(
        null=True, blank=True
    )

    neu = models.FloatField(
        null=True, blank=True
    )

    eos = models.FloatField(
        null=True, blank=True
    )

    bas = models.FloatField(
        null=True, blank=True
    )

    hgb = models.FloatField(
        null=True, blank=True
    )

    plt = models.FloatField(
        null=True, blank=True
    )

    cd45_cd3 = models.FloatField(
        null=True, blank=True
    )

    cd45_cd19 = models.FloatField(
        null=True, blank=True
    )

    cd45_cd3_cd4 = models.FloatField(
        null=True, blank=True
    )

    cd3_cd4_cd3_cd8 = models.FloatField(
        null=True, blank=True
    )

    cd45_cd3_cd16_56 = models.FloatField(
        null=True, blank=True
    )

    cd45_cd3_cd16bright_cd56dim = models.FloatField(
        null=True, blank=True
    )

    circulating_immune_complex = models.FloatField(
        null=True, blank=True
    )

    hct_test_spontaneous = models.FloatField(
        null=True, blank=True
    )

    hct_test_stimulated = models.FloatField(
        null=True, blank=True
    )

    cd3_ifny_stimulated = models.FloatField(
        null=True, blank=True
    )

    cd3_ifny_spontaneous = models.FloatField(
        null=True, blank=True
    )

    index_cd3_ifny_spontaneous = models.FloatField(
        null=True, blank=True
    )

    cd3_tnfa_stimulated = models.FloatField(
        null=True, blank=True
    )

    cd3_tnfa_spontaneous = models.FloatField(
        null=True, blank=True
    )

    index_cd3_tnfa_stimulated = models.FloatField(
        null=True, blank=True
    )

    cd3_il2_stimulated = models.FloatField(
        null=True, blank=True
    )

    cd3_il2_spontaneous = models.FloatField(
        null=True, blank=True
    )

    index_cd3_il2_stimulated = models.FloatField(
        null=True, blank=True
    )

    fno = models.FloatField(
        null=True, blank=True
    )

    def __str__(self):
        return self.patient.name
