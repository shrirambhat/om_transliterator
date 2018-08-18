# Copyright (C) 2018 Shriram Bhat
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""The setup.py file for OM Transliterator."""

from setuptools import setup

setup(
    name='OM Transliterator',
    version='0.1dev',
    author='Shriram Bhat',
    author_email='mail@shrirambhat.com',
    url='https://github.com/shrirambhat/om_transliterator',
    packages=['om_transliterator',],
    license='LICENSE.txt',
    keywords='kannada english latin romanization iso15919 transliteration tool',
    description='Kannada to Latin ISO 15919 (Romanisation) Transliterator.',
    long_description=open('README.txt').read(),
)