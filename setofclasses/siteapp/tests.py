# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.test import TestCase
from siteapp.models import Site
from django.core.exceptions import ValidationError

class SiteValidationTest(TestCase):
    # Checks an object that is valid
    def test_valid(self):
        Site.create("http://www.google.com", "1998-09-08", 10).save()

    # Checks an object which url field is invalid
    def test_invalid_wrong_url_field(self):
        with self.assertRaises(ValidationError): Site.create(666, "1998-09-08", 10).save()
        with self.assertRaises(ValidationError): Site.create("lollipop", "1998-09-08", 10).save()

    # Checks an object which date field is invalid
    def test_invalid_wrong_date_field(self):
        with self.assertRaises(ValidationError): Site.create("http://www.google.com", "1998-90-08", 10).save()
        with self.assertRaises(TypeError): Site.create("http://www.google.com", 5, 10).save()
        with self.assertRaises(ValidationError): Site.create("http://www.google.com", "duck", 10).save()


    # Checks an object which url raring is invalid
    def test_invalid_wrong_rating_field(self):
        with self.assertRaises(ValidationError): Site.create("http://www.google.com", "1998-09-08", -1).save()
        with self.assertRaises(ValidationError): Site.create("http://www.google.com", "1998-09-08","bananana").save()

