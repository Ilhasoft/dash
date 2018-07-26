# -*- coding: utf-8 -*-
# Generated by Django 1.11.12 on 2018-04-27 12:04
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):
    def fix_org_config_rapidpro(apps, schema_editor):
        Org = apps.get_model("orgs", "Org")
        orgs = Org.objects.all()
        for org in orgs:
            if not org.config:
                continue

            config = org.config
            rapidpro_config = config.get("rapidpro", dict())
            if "api_token" in rapidpro_config:
                del rapidpro_config["api_token"]

            if "rapipro" in config:
                del config["rapipro"]  # remove the mistakenly added key by typo in 0024_populate_org_backend

            config["rapidpro"] = rapidpro_config
            org.config = config
            org.save()

    def noop(apps, schema_editor):
        pass

    dependencies = [("orgs", "0025_auto_20180322_1415")]

    operations = [migrations.RunPython(fix_org_config_rapidpro, noop)]
