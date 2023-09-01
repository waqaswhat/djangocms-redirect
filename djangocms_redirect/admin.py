from cms.forms.widgets import PageSmartLinkWidget
from django.contrib import admin
from django.forms import ModelForm
from django.utils.translation import get_language
from import_export.admin import ImportExportModelAdmin
from import_export.tmp_storages import CacheStorage

from .models import Redirect, LanguageRedirect, Language
from .utils import normalize_url


class RedirectForm(ModelForm):
    class Meta:
        model = Redirect
        fields = ["site", "old_path", "response_code"]

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
    list_display = ("old_path", "response_code")
    list_filter = ("site",)
    search_fields = ("old_path",)
    radio_fields = {"site": admin.VERTICAL}
    form = RedirectForm


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


@admin.register(LanguageRedirect)
class LanguageRedirectAdmin(ImportExportModelAdmin):
    tmp_storage_class = CacheStorage
    list_display = ("redirect", "language_code", "redirect_path")
    list_filter = ("redirect",)
    form = LanguageRedirectForm

admin.site.register(Language)
