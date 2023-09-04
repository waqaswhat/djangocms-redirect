from cms.forms.widgets import PageSmartLinkWidget
from django.contrib import admin
from django.forms import ModelForm
from django.utils.translation import get_language
from import_export.admin import ImportExportModelAdmin
from import_export.tmp_storages import CacheStorage

from .models import Redirect, LanguageRedirect
from .utils import normalize_url
from django.core.exceptions import ValidationError


class LanguageRedirectForm(ModelForm):
    class Meta:
        model = LanguageRedirect
        fields = "__all__"

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        widget = PageSmartLinkWidget(ajax_view="admin:cms_page_get_published_pagelist")
        widget.language = get_language()
        # adding language widget to all fields that contains '_path'
        [setattr(self.fields[field], "widget", widget) for field in [x for x in self.fields if "_path" in x]]

    def clean(self):
        cleaned_data = super().clean()
        redirect = cleaned_data.get('redirect')
        language_code = cleaned_data.get('language_code')

        # Avoid duplicates redirects to the same path for same language
        if LanguageRedirect.objects.filter(redirect=redirect, language_code=language_code).exclude(
            pk=self.instance.pk).exists():
            raise ValidationError('Language redirect already exists.')


class LanguageRedirectAdmin(admin.TabularInline):
    tmp_storage_class = CacheStorage
    list_filter = ("redirect",)
    form = LanguageRedirectForm
    model = LanguageRedirect


class RedirectForm(ModelForm):
    class Meta:
        model = Redirect
        fields = ["site", "old_path", "new_path",  "response_code"]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        widget = PageSmartLinkWidget(ajax_view="admin:cms_page_get_published_pagelist")
        widget.language = get_language()
        # adding language widget to all fields that contains '_path'
        [setattr(self.fields[field], "widget", widget) for field in [x for x in self.fields if "_path" in x]]

    def clean_old_path(self):
        return normalize_url(self.cleaned_data.get("old_path"))


@admin.register(Redirect)
class RedirectAdmin(ImportExportModelAdmin):
    tmp_storage_class = CacheStorage
    inlines = [LanguageRedirectAdmin]
    list_display = ("old_path", "response_code")
    list_filter = ("site",)
    search_fields = ("old_path",)
    radio_fields = {"site": admin.VERTICAL}
    form = RedirectForm




