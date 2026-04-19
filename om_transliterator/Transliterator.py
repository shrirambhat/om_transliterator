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

"""Kannada (Knda) to Latin (Latn) transliteration per ISO 15919:2001."""

from om_transliterator.charmap import charmap_iso15919, NUKTA_COMPOSITIONS

KANNADA_BLOCK_START = 0x0C80
KANNADA_BLOCK_SIZE = 128

POS_ANUSVARA = 2
POS_I = 7
POS_U = 9
POS_NUKTA = 60

MATRA_RANGE = range(62, 78)

VELARS = range(21, 26)
PALATALS = range(26, 31)
RETROFLEXES = range(31, 36)
DENTALS = range(36, 41)
LABIALS = range(42, 47)
STOPS = frozenset(VELARS) | frozenset(PALATALS) | frozenset(RETROFLEXES) | frozenset(DENTALS) | frozenset(LABIALS)

POS_VELAR_NASAL = 25
POS_PALATAL_NASAL = 30
POS_RETROFLEX_NASAL = 35
POS_DENTAL_NASAL = 40
POS_LABIAL_NASAL = 46


class Transliterator:

    def knda_to_latn(self, original_text):
        """Transliterate a Kannada unicode string to Latin per ISO 15919.

        Rules applied, in order:

        1. A vowel sign (matra) deletes the inherent 'a' of the preceding
           consonant cluster.
        2. An independent vowel i/u following a consonant+schwa is
           separated by a colon to disambiguate "ba:i" from "bai".
        3. Anusvara is rendered as the homorganic nasal of the following
           stop when one exists, otherwise as the default "ṁ".
        4. A base consonant followed by nukta (U+0CBC) composes to a
           loan-sound form (ja+nukta -> za, pha+nukta -> fa, etc).
        5. Any character outside the Kannada block passes through
           unchanged.

        Args:
            original_text (str): Source text in Kannada unicode.

        Returns:
            str: Transliterated text.
        """
        latn_map = charmap_iso15919["Latn"]
        out = []
        skip_next = False

        for index, character in enumerate(original_text):
            if skip_next:
                skip_next = False
                continue

            position = self._get_character_position(character)
            next_position = self._get_character_position(original_text[index + 1]) \
                if index + 1 < len(original_text) else -1

            if position in MATRA_RANGE:
                self._delete_schwa(out)

            if position in (POS_I, POS_U) and out and out[-1].endswith("a"):
                out.append(":")

            if 0 < position < KANNADA_BLOCK_SIZE:
                if position == POS_ANUSVARA:
                    out.append(self._anusvara_for(next_position, latn_map))
                    if next_position in STOPS:
                        self._delete_schwa(out)
                elif next_position == POS_NUKTA and position in NUKTA_COMPOSITIONS:
                    out.append(NUKTA_COMPOSITIONS[position])
                    skip_next = True
                else:
                    out.append(latn_map[position])
            else:
                out.append(character)

        return "".join(out)

    @staticmethod
    def _anusvara_for(next_position, latn_map):
        if next_position in VELARS:
            return latn_map[POS_VELAR_NASAL]
        if next_position in PALATALS:
            return latn_map[POS_PALATAL_NASAL]
        if next_position in RETROFLEXES:
            return latn_map[POS_RETROFLEX_NASAL]
        if next_position in DENTALS:
            return latn_map[POS_DENTAL_NASAL]
        if next_position in LABIALS:
            return latn_map[POS_LABIAL_NASAL]
        return latn_map[POS_ANUSVARA]

    @staticmethod
    def _get_character_position(character):
        return ord(character) - KANNADA_BLOCK_START

    @staticmethod
    def _delete_schwa(out):
        if out and out[-1].endswith("a"):
            out[-1] = out[-1][:-1]
