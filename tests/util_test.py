# Copyright 2019 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     https://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
"""Tests for the Google Ads API client library utilities."""


from unittest import TestCase

from google.ads.google_ads import util


class ResourceNameTest(TestCase):
    def test_format_composite(self):
        composite = util.ResourceName.format_composite("test", "test")
        self.assertEqual(composite, "test~test")


class ConvertStringTest(TestCase):
    def test_convert_upper_case_to_snake_case(self):
        string = "GoogleAdsServiceClientTransport"
        expected = "google_ads_service_client_transport"
        result = util.convert_upper_case_to_snake_case(string)
        self.assertEqual(result, expected)

    def test_convert_snake_case_to_upper_case(self):
        string = "google_ads_service_client_transport"
        expected = "GoogleAdsServiceClientTransport"
        result = util.convert_snake_case_to_upper_case(string)
        self.assertEqual(result, expected)
