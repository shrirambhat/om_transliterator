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

"""Transliterator is a library for transliterating text from Kannada (Knda) unicode script to Latin (Latn) script as per ISO 15919."""

from om_transliterator.charmap import charmap_iso15919

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

POS_JA = 28
POS_PHA = 43
POS_ZA = 91
POS_FA = 94


class Transliterator:

    def knda_to_latn(self, original_text):
        """Transliterate Kannada (Knda) unicode string to Latin (Latn) characters as per ISO 15919.

        The steps performed by this method are:

        1. Iterate through each character in the string.
        2. If the current character is a vowel sign (matra),
            delete the inherent a from the preceding consonant.
        3. If the current character is an independent vowel syllable
            (unattached to a preceding consonant), then add a colon
            to resolve ambiguities (e.g. ba:i vs bai).
        4. If the current character is a valid Kannada character, then
            replace it with the equivalent Latin character.
            A following nukta (U+0CBC) turns ja/pha into za/fa.
        5. Anusvara is rendered as the homorganic nasal of the following
            consonant, when there is one.

        Args:
            original_text (str): Original text in Kannada unicode.

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
                elif position == POS_JA and next_position == POS_NUKTA:
                    out.append(latn_map[POS_ZA])
                    skip_next = True
                elif position == POS_PHA and next_position == POS_NUKTA:
                    out.append(latn_map[POS_FA])
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
