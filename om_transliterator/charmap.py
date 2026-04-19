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

"""Character map for unicode Kannada script with Latin (ISO 15919).

The two arrays are parallel: entry i of "Knda" maps to entry i of "Latn".
Slots 88..95 are synthetic: they are not direct Kannada codepoints but
targets used by the transliterator for nukta-composed characters
(e.g. ja + nukta -> za at slot 91, pha + nukta -> fa at slot 94).
"""

# Vocalic r / l use combining ring below (U+0325) per ISO 15919, not the
# dot-below forms (which would collide with retroflex la "ḷa"). Anusvara
# uses U+1E43 (m with dot below), not U+1E41 (dot above).
_R_RING = "r\u0325"
_R_RING_MACRON = "r\u0304\u0325"
_L_RING = "l\u0325"
_L_RING_MACRON = "l\u0304\u0325"

charmap_iso15919 = {
    "Knda": [
        u"ಀ", u"ಁ", u"ಂ", u"ಃ", u"಄", u"ಅ", u"ಆ", u"ಇ", u"ಈ", u"ಉ", u"ಊ", u"ಋ", u"ಌ", u"಍", u"ಎ", u"ಏ",
        u"ಐ", u"಑", u"ಒ", u"ಓ", u"ಔ", u"ಕ", u"ಖ", u"ಗ", u"ಘ", u"ಙ", u"ಚ", u"ಛ", u"ಜ", u"ಝ", u"ಞ", u"ಟ",
        u"ಠ", u"ಡ", u"ಢ", u"ಣ", u"ತ", u"ಥ", u"ದ", u"ಧ", u"ನ", u"಩", u"ಪ", u"ಫ", u"ಬ", u"ಭ", u"ಮ", u"ಯ",
        u"ರ", u"ಱ", u"ಲ", u"ಳ", u"಴", u"ವ", u"ಶ", u"ಷ", u"ಸ", u"ಹ", u"಺", u"಻", u"಼", u"ಽ", u"ಾ", u"ಿ",
        u"ೀ", u"ು", u"ೂ", u"ೃ", u"ೄ", u"೅", u"ೆ", u"ೇ", u"ೈ", u"೉", u"ೊ", u"ೋ", u"ೌ", u"್", u"೎", u"೏",
        u"೐", u"೑", u"೒", u"೓", u"೔", u"ೕ", u"ೖ", u"೗", u"೘", u"೙", u"೚", u"೛", u"೜", u"ೝ", u"ೞ", u"೟",
        u"ೠ", u"ೡ", u"ೢ", u"ೣ", u"೤", u"೥", u"೦", u"೧", u"೨", u"೩", u"೪", u"೫", u"೬", u"೭", u"೮", u"೯",
        u"೰", u"ೱ", u"ೲ", u"ೳ", u"೴", u"೵", u"೶", u"೷", u"೸", u"೹", u"೺", u"೻", u"೼", u"೽", u"೾", u"೿"
    ],
    "Latn": [
        u"", u"m̐", u"ṃ", u"ḥ", u"", u"a", u"ā", u"i", u"ī", u"u", u"ū", _R_RING, _L_RING, u"ê", u"e", u"ē",
        u"ai", u"ô", u"o", u"ō", u"au", u"ka", u"kha", u"ga", u"gha", u"ṅa", u"ca", u"cha", u"ja", u"jha", u"ña", u"ṭa",
        u"ṭha", u"ḍa", u"ḍha", u"ṇa", u"ta", u"tha", u"da", u"dha", u"na", u"ṉa", u"pa", u"pha", u"ba", u"bha", u"ma", u"ya",
        u"ra", u"ṟa", u"la", u"ḷa", u"ḻa", u"va", u"śa", u"ṣa", u"sa", u"ha", u"", u"", u"", u"'", u"ā", u"i",
        u"ī", u"u", u"ū", _R_RING, _R_RING_MACRON, u"ê", u"e", u"ē", u"ai", u"ô", u"o", u"ō", u"au", u"", u"", u"",
        u"ōṃ", u"", u"", u"", u"", u"", u"", u"", u"qa", u"ḵẖa", u"ġa", u"za", u"ṛa", u"ṛha", u"fa", u"ẏa",
        _R_RING_MACRON, _L_RING_MACRON, _L_RING, _L_RING_MACRON, u".", u"..", u"0", u"1", u"2", u"3", u"4", u"5", u"6", u"7", u"8", u"9",
        u"…", u"", u"", u"", u"", u"", u"", u"", u"", u"", u"", u"", u"", u"", u"", u""
    ],
}
