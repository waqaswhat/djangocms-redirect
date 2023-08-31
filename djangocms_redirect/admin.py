from cms.forms.widgets import PageSmartLinkWidget
from django.contrib import admin
from django.forms import ModelForm
from django.utils.translation import get_language
from import_export.admin import ImportExportModelAdmin
from import_export.tmp_storages import CacheStorage

from .models import Redirect
from .utils import normalize_url


class RedirectForm(ModelForm):
    class Meta:
        model = Redirect
        fields = ["site", "old_path", "default_path", "de_path", "en_path", "fr_path", "it_path",
                  "response_code"]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        widget = PageSmartLinkWidget(ajax_view="admin:cms_page_get_published_pagelist")
        widget.language = get_language()
        [setattr(self.fields[field], "widget", widget) for field in [x for x in self.fields if "_path" in x]]

    def clean_old_path(self):
        return normalize_url(self.cleaned_data.get("old_path"))


@admin.register(Redirect)
class RedirectAdmin(ImportExportModelAdmin):
    tmp_storage_class = CacheStorage
    list_display = ("old_path", "new_path", "response_code")
    list_filter = ("site",)
    search_fields = ("old_path", "new_path")
    radio_fields = {"site": admin.VERTICAL}
    form = RedirectForm
