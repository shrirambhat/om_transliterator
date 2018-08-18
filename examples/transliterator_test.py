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

"""Test for Transliteration Module."""

if __name__ == '__main__':
    import os
    from om_transliterator import Transliterator

    input_file = os.path.join(os.path.dirname(__file__), 'input.txt')
    with open(input_file, "r", encoding = "utf-8") as f:
        original_text = f.read()
    # end with

    transliterator = Transliterator()
    transliterated_text = transliterator.knda_to_latn(original_text)

    output_file = os.path.join(os.path.dirname(__file__), 'output.txt')
    with open(output_file, "w", encoding = "utf-8") as f:
        f.write(transliterated_text)
    # end with
# end if