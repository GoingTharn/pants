# coding=utf-8
# Copyright 2014 Pants project contributors (see CONTRIBUTORS.md).
# Licensed under the Apache License, Version 2.0 (see LICENSE).

from __future__ import absolute_import, division, print_function, unicode_literals

from pants.backend.jvm.tasks.jvm_compile.analysis_parser import (AnalysisParser, ParseError,
                                                                 raise_on_eof)
from pants.backend.jvm.tasks.jvm_compile.zinc.zinc_analysis import ZincAnalysis
from pants.backend.jvm.zinc.zinc_analysis_parser import ZincAnalysisParser as UnderlyingParser


class ZincAnalysisParser(AnalysisParser):
  """Parses a zinc analysis file.

  Implemented by delegating to an underlying pants.backend.jvm.zinc.ZincAnalysisParser instance.
  """

  # Implement AnalysisParser properties.
  empty_test_header = b'products'
  current_test_header = ZincAnalysis.FORMAT_VERSION_LINE

  def __init__(self):
    self._underlying_parser = UnderlyingParser()

  # Implement AnalysisParser methods.
  def parse(self, infile):
    """Parse a ZincAnalysis instance from an open text file."""
    with raise_on_eof(infile):
      try:
        return ZincAnalysis(self._underlying_parser.parse(infile))
      except UnderlyingParser.ParseError as e:
        raise ParseError(e)

  def parse_products(self, infile, classes_dir):
    """An efficient parser of just the products section."""
    with raise_on_eof(infile):
      try:
        return self._underlying_parser.parse_products(infile)
      except UnderlyingParser.ParseError as e:
        raise ParseError(e)

  def parse_deps(self, infile):
    with raise_on_eof(infile):
      try:
        return self._underlying_parser.parse_deps(infile, "")
      except UnderlyingParser.ParseError as e:
        raise ParseError(e)

  def rebase(self, infile, outfile, rebase_mappings, java_home=None):
    with raise_on_eof(infile):
      try:
        self._underlying_parser.rebase(infile, outfile, rebase_mappings, java_home)
      except UnderlyingParser.ParseError as e:
        raise ParseError(e)
