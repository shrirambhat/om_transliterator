=================
OM Transliterator
=================

OM Transliterator is a Python library for transliterating text 
from Kannada (Knda) unicode script to Latin (Latn) script 
as per ISO 15919. 

Installation
============

To install OM Transliterator with pip, run: ``pip install om_transliterator``

To install OM Transliterator from source, first clone the repository and then 
run: ``python setup.py install``

Basic Usage
===========

Here's an example of typical usage::

    #!/usr/bin/env python

    from om_transliterator import Transliterator

    transliterator = Transliterator()

    transliterated_text = transliterator.knda_to_latn(original_text)

Thanks to
=========

This project is open-sourced by contributions and support from people, 
including:

* Dinesh Shenoy

* Prof. Purushothama Bilimale

* Srikanth Lakshmanan

* Sandesh B Suvarna

* Arjun Shetty


License
=======

`Apache License 2.0 <http://www.apache.org/licenses/LICENSE-2.0>`_