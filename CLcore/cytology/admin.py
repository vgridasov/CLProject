from django.contrib import admin
from import_export import resources
from import_export.fields import Field
from .models import Analysis
from import_export.admin import ImportExportModelAdmin


class AnalysisResource(resources.ModelResource):
    reg = Field(attribute="reg", column_name="РЕГ")
    code = Field(attribute="code", column_name="CODE")
    otdelen = Field(attribute="otdelen", column_name="OTDELEN")
    last_name = Field(attribute="last_name", column_name="ФАМИЛИЯ")
    first_name = Field(attribute="first_name", column_name="ИМЯ")
    middle_name = Field(attribute="middle_name", column_name="ОТЧЕСТВО")
    gender = Field(attribute="gender", column_name="ПОЛ")
    b_date = Field(attribute="b_date", column_name="ДАТА_РОЖД")
    policy = Field(attribute="policy", column_name="ПОЛИС")
    snils = Field(attribute="snils", column_name="СНИЛС")
    address = Field(attribute="address", column_name="АДРЕС")
    kl_diag = Field(attribute="kl_diag", column_name="КЛ_ДИАГ")
    v_date = Field(attribute="v_date", column_name="ДАТА_ВЗЯТ")
    p_date = Field(attribute="p_date", column_name="ДАТА_ПОСТ")
    reg_date = Field(attribute="reg_date", column_name="ДАТА_РЕГ")
    an_object = Field(attribute="an_object", column_name="ОБЪЕКТ")
    doctor = Field(attribute="doctor", column_name="ДОКТОР")
    vyr_date = Field(attribute="vyr_date", column_name="ДАТА_ВЫРЕЗ")
    macro = Field(attribute="macro", column_name="МАКРО")
    macro_p_a = Field(attribute="macro_p_a", column_name="МАКРО_п_а")
    micro = Field(attribute="micro", column_name="МИКРО")
    zakl = Field(attribute="zakl", column_name="ЗАКЛ")
    comment = Field(attribute="comment", column_name="КОММЕНТ")
    mcode1 = Field(attribute="mcode1", column_name="кодмедусл1")
    mcode1_num = Field(attribute="mcode1_num", column_name="кол_кодмедусл1")
    mcode2 = Field(attribute="mcode2", column_name="кодмедусл2")
    mcode2_num = Field(attribute="mcode2_num", column_name="кол_кодмедусл2")
    code1 = Field(attribute="code1", column_name="код")
    complexity = Field(attribute="complexity", column_name="Сложность")
    p_a = Field(attribute="p_a", column_name="п_а")
    a_date = Field(attribute="a_date", column_name="ДАТА_ИССЛ")

    class Meta:
        model = Analysis
        import_id_fields = ('reg',)
        skip_unchanged = True


class AnalysisAdmin(ImportExportModelAdmin):
    resource_class = AnalysisResource
    fields = [
        "reg",
        "code",
        "otdelen",
        "last_name",
        "first_name",
        "middle_name",
        "gender",
        "b_date",
        "policy",
        "snils",
        "address",
        "kl_diag",
        "v_date",
        "p_date",
        "reg_date",
        "an_object",
        "doctor",
        "vyr_date",
        "macro",
        "macro_p_a",
        "micro",
        "zakl",
        "comment",
        "mcode1",
        "mcode1_num",
        "mcode2",
        "mcode2_num",
        "code1",
        "complexity",
        "p_a",
        "a_date",
    ]
    search_fields = ["last_name", "otdelen", "v_date"]
    list_filter = ["otdelen"]


admin.site.register(Analysis, AnalysisAdmin)
admin.site.site_title = "Административная панель - ГИСТОЛОГИЯ"
admin.site.site_header = "Административная панель - ГИСТОЛОГИЯ"
