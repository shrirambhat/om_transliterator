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

class Transliterator:

    def __init__(self):
        self.transliterated_text = ""
    # end def

    def knda_to_latn(self, original_text):
        """Transliterate Kannada (Knda) unicode string to Latin (Latn) characters as per ISO 15919.
        
        The steps performed by this method are:

        1. Iterate through each character in the string.
        2. If the current character is diatrics (matras) for vowels, 
            delete the inherent a.
        3. If the current character is an independent vowel syllable 
            (unattached to a preceding consonant), then add a colon 
            to resolve ambiguities.
        4. If the current character is a valid Kannada character, then
            replace it with equivalent latin character.

        In step 4, check rules for anusvaara and special characters like za and fa.

        Args:
            original_text (string): Original text in Kannada unicode.
        
        Returns:
            string: Transliterated text.
        """
        index = 0
        for character in original_text:
            index += 1
            character_position = self._get_character_position(character)

            # if character_position is diatrics, then remove the last shwa
            if character_position >= 62 and character_position <= 77:
                self._delete_schwa()
            # end if

            # A colon (:) is used for resolving ambiguities in ai and au. Eg: ಬಇ is ba:i, not bai which can mean ಬೈ.
            if character_position in [7,9] and self.transliterated_text[-1:] == "a":
                self.transliterated_text += ":"
            # end if

            if character_position > 0 and character_position <= 128:
                try:
                    # if character_position is anusvaara,
                    if character_position == 2:
                        if self._get_character_position(original_text[index]) in [21,22,23,24,25]:
                            # if anusvaara is before velars, then use velar nasal.
                            self.transliterated_text += charmap_iso15919["Latn"][25]
                            self._delete_schwa()
                        elif self._get_character_position(original_text[index]) in [26,27,28,29,30]:
                            # if anusvaara is before palatals, then use palatal nasal.
                            self.transliterated_text += charmap_iso15919["Latn"][30]
                            self._delete_schwa()
                        elif self._get_character_position(original_text[index]) in [31,32,33,34,35]:
                            # if anusvaara is before retroflexes, then use retroflex nasal.
                            self.transliterated_text += charmap_iso15919["Latn"][35]
                            self._delete_schwa()
                        elif self._get_character_position(original_text[index]) in [36,37,38,39,40]:
                            # if anusvaara is before dentals, then use dental nasal.
                            self.transliterated_text += charmap_iso15919["Latn"][40]
                            self._delete_schwa()
                        elif self._get_character_position(original_text[index]) in [42,43,44,45,46]:
                            # if anusvaara is before labials, then use labial nasal.
                            self.transliterated_text += charmap_iso15919["Latn"][46]
                            self._delete_schwa()
                        else:
                            # for all other cases, use default anusvaara.
                            self.transliterated_text += charmap_iso15919["Latn"][character_position]
                        # end if anusvaara
                    elif character_position == 28 and self._get_character_position(original_text[index]) == 60:
                        # if za, use specific character.
                        self.transliterated_text += charmap_iso15919["Latn"][91]
                    elif character_position == 43 and self._get_character_position(original_text[index]) == 60:
                        # if fa, use specific character.
                        self.transliterated_text += charmap_iso15919["Latn"][94]
                    else:
                        self.transliterated_text += charmap_iso15919["Latn"][character_position]
                    # end if
                except:
                    self.transliterated_text += charmap_iso15919["Latn"][character_position]
                # end try

            else:
                # Not a Kannada character; leave it as it is.
                self.transliterated_text += character
            # end if
        # end for
        try:
            result = self.transliterated_text.decode("utf-8")
        except BaseException:
            result = self.transliterated_text
        return result
    # end def

    def _get_character_position(self, character):
        character_position = ord(character) - 0x0C80
        return character_position
    # end def

    def _delete_schwa(self):
        if self.transliterated_text[-1:] == "a":
            self.transliterated_text = self.transliterated_text[:-1]
        # end if
    # end def

# end class