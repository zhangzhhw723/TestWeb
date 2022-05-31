# -*- coding: utf-8 -*-
# @Time : 2022/5/31 13:36
# @Author : zhw
# @File : test_git_secret.py.py
import unittest
from mysite.config.sandbox_env import SANDBOX_ENV


class TestSecret(unittest.TestCase):
    def test_equal(self):
        self.assertEqual("api-key", SANDBOX_ENV["key"])