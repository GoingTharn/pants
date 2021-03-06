# Copyright 2015 Pants project contributors (see CONTRIBUTORS.md).
# Licensed under the Apache License, Version 2.0 (see LICENSE).

page(
  name='readme',
  source='README.md',
)

# TODO: Get rid of all these microtargets. The entire package should be one target,
# or be split into multiple packages.

python_library(
  name = 'legacy_engine',
  sources = ['legacy_engine.py', 'round_engine.py', 'round_manager.py'],
  dependencies = [
    '3rdparty/python:future',
    '3rdparty/python/twitter/commons:twitter.common.collections',
    'src/python/pants/base:exceptions',
    'src/python/pants/base:workunit',
    'src/python/pants/goal',
    'src/python/pants/util:meta',
  ],
)

python_library(
  name='addressable',
  sources=['addressable.py'],
  dependencies=[
    '3rdparty/python:future',
    ':objects',
    'src/python/pants/build_graph',
    'src/python/pants/util:memo',
    'src/python/pants/util:objects',
  ]
)

python_library(
  name='struct',
  sources=['struct.py'],
  dependencies=[
    '3rdparty/python:future',
    ':objects',
    'src/python/pants/util:objects',
  ]
)

python_library(
  name='fs',
  sources=['fs.py'],
  dependencies=[
    '3rdparty/python/twitter/commons:twitter.common.collections',
    '3rdparty/python:future',
    ':rules',
    ':selectors',
    'src/python/pants/base:project_tree',
    'src/python/pants/option',
    'src/python/pants/source',
    'src/python/pants/util:meta',
    'src/python/pants/util:objects',
  ]
)

python_library(
  name='build_files',
  sources=['build_files.py'],
  dependencies=[
    '3rdparty/python:future',
    '3rdparty/python:six',
    ':addressable',
    ':fs',
    ':mapper',
    ':objects',
    ':selectors',
    ':struct',
    'src/python/pants/base:project_tree',
    'src/python/pants/build_graph',
    'src/python/pants/util:dirutil',
    'src/python/pants/util:filtering',
    'src/python/pants/util:objects',
  ]
)

python_library(
  name='mapper',
  sources=['mapper.py'],
  dependencies=[
    ':objects',
    ':parser',
    'src/python/pants/build_graph',
    'src/python/pants/util:memo',
  ]
)

python_library(
  name='isolated_process',
  sources=['isolated_process.py'],
  dependencies=[
    ':fs',
    ':rules',
    ':selectors',
    'src/python/pants/util:objects',
  ]
)

python_library(
  name='nodes',
  sources=['nodes.py'],
  dependencies=[
    '3rdparty/python/twitter/commons:twitter.common.collections',
    ':addressable',
    ':fs',
    ':struct',
    'src/python/pants/base:project_tree',
    'src/python/pants/build_graph',
    'src/python/pants/util:objects',
  ]
)

python_library(
  name='objects',
  sources=['objects.py'],
  dependencies=[
    'src/python/pants/util:meta',
  ]
)

python_library(
  name='parser',
  sources=['parser.py'],
  dependencies=[
    '3rdparty/python:six',
    ':addressable',
    ':objects',
    'src/python/pants/build_graph',
    'src/python/pants/util:memo',
  ]
)

python_library(
  name='rules',
  sources=['rules.py'],
  dependencies=[
    '3rdparty/python/twitter/commons:twitter.common.collections',
    ':selectors',
    'src/python/pants/base:specs',
    'src/python/pants/util:objects',
  ]
)

python_library(
  name='selectors',
  sources=['selectors.py'],
  dependencies=[
    '3rdparty/python:future',
    '3rdparty/python:six',
    'src/python/pants/util:meta',
    'src/python/pants/util:objects',
  ]
)

python_library(
  name='scheduler',
  sources=['scheduler.py'],
  dependencies=[
    '3rdparty/python:future',
    '3rdparty/python/twitter/commons:twitter.common.collections',
    ':fs',
    ':isolated_process',
    ':native',
    ':nodes',
    ':rules',
    'src/python/pants/base:exceptions',
    'src/python/pants/base:specs',
    'src/python/pants/build_graph',
    'src/python/pants/util:objects',
  ]
)

python_library(
  name='native',
  sources=['native.py'],
  dependencies=[
    '3rdparty/python:future',
    ':native_engine_shared_library',
    ':selectors',
    '3rdparty/python:cffi',
    '3rdparty/python:setuptools',
    'src/python/pants/binaries',
    'src/python/pants/util:dirutil',
    'src/python/pants/util:memo',
    'src/python/pants/util:objects'
  ],
)


python_library(
  name='console',
  sources=['console.py']
)

resources(
  name='native_engine_shared_library',
  sources=['native_engine.so']
)
