# coding=utf-8
# Copyright 2018 Pants project contributors (see CONTRIBUTORS.md).
# Licensed under the Apache License, Version 2.0 (see LICENSE).

from __future__ import absolute_import, division, print_function, unicode_literals

from pants.backend.jvm.targets.jvm_target import JvmTarget


class JavaThriftyLibrary(JvmTarget):
  """An Android-optimized Java library generated by the Microsoft Thrifty thrift compiler.

  Says Thrifty, "Thrifty is an implementation of the Apache Thrift software stack for Android,
  which uses 1/4 of the method count taken by the Apache Thrift compiler."

  For details, see https://github.com/Microsoft/thrifty
  """
  default_sources_globs = '*.thrift'
