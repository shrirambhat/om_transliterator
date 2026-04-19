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

"""Character map for unicode Kannada script with Latin (ISO 15919:2001).

ISO 15919 conventions used here (diverging from IAST where noted):
- Anusvara (ಂ) is rendered as "ṁ" (U+1E41, m with dot above), not IAST "ṃ".
- Candrabindu (ಁ) is "m̐" (m + combining candrabindu U+0310).
- Vocalic r/rr/l/ll use combining ring below U+0325: "r̥", "r̥̄", "l̥", "l̥̄".
  IAST conflates these with retroflexes as "ṛ/ṝ/ḷ/ḹ"; ISO 15919
  deliberately keeps them distinct.
- Retroflex lateral ಳ is "ḷa" (dot below, U+1E37).
- Retroflex approximant U+0CDE (ೞ) is "ḻa" (macron below, U+1E3B)
  per Tamil-Lexicon / ISO 15919 Dravidian convention.
- Dravidian trill ಱ is "ṟa" (r with line below, U+1E5F).
- Short e/o and long ē/ō are kept distinct ("e" vs "ē", "o" vs "ō").

Nukta-composed forms (ja+nukta=za, pha+nukta=fa, ...) live in
NUKTA_COMPOSITIONS, decoupled from Latn array positions to avoid
colliding with real Kannada codepoints at U+0CD8..U+0CDE.
"""

_R_RING = "r\u0325"
_R_RING_MACRON = "r\u0304\u0325"
_L_RING = "l\u0325"
_L_RING_MACRON = "l\u0304\u0325"

charmap_iso15919 = {
    # Parallel arrays indexed by (codepoint - 0x0C80), length 128.
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
        # 0x00..0x0F  (0x0C80..0x0C8F)
        u"", u"m̐", u"ṁ", u"ḥ", u"", u"a", u"ā", u"i", u"ī", u"u", u"ū", _R_RING, _L_RING, u"ê", u"e", u"ē",
        # 0x10..0x1F  (0x0C90..0x0C9F): ai, o-variants, velar/palatal/retroflex consonants
        u"ai", u"ô", u"o", u"ō", u"au", u"ka", u"kha", u"ga", u"gha", u"ṅa", u"ca", u"cha", u"ja", u"jha", u"ña", u"ṭa",
        # 0x20..0x2F  (0x0CA0..0x0CAF): retroflex/dental/labial consonants
        u"ṭha", u"ḍa", u"ḍha", u"ṇa", u"ta", u"tha", u"da", u"dha", u"na", u"ṉa", u"pa", u"pha", u"ba", u"bha", u"ma", u"ya",
        # 0x30..0x3F  (0x0CB0..0x0CBF): semivowels, sibilants, avagraha, matras
        u"ra", u"ṟa", u"la", u"ḷa", u"ḻa", u"va", u"śa", u"ṣa", u"sa", u"ha", u"", u"", u"", u"'", u"ā", u"i",
        # 0x40..0x4F  (0x0CC0..0x0CCF): matras, virama
        u"ī", u"u", u"ū", _R_RING, _R_RING_MACRON, u"ê", u"e", u"ē", u"ai", u"ô", u"o", u"ō", u"au", u"", u"", u"",
        # 0x50..0x5F  (0x0CD0..0x0CDF): length marks, rare/archaic consonants
        # 0x5D (U+0CDD) "ೝ" KANNADA LETTER NAKAARA POLLU: syllable-final n -> "n"
        # 0x5E (U+0CDE) "ೞ" KANNADA LETTER FA (historical retroflex approximant) -> "ḻa"
        u"", u"", u"", u"", u"", u"", u"", u"", u"", u"", u"", u"", u"", u"n", u"ḻa", u"",
        # 0x60..0x6F  (0x0CE0..0x0CEF): vocalic rr/ll + matras, digits 0-5
        _R_RING_MACRON, _L_RING_MACRON, _L_RING, _L_RING_MACRON, u"", u"", u"0", u"1", u"2", u"3", u"4", u"5", u"6", u"7", u"8", u"9",
        # 0x70..0x7F  (0x0CF0..0x0CFF): reserved / rare signs (jihvamuliya, upadhmaniya, etc.)
        u"", u"", u"", u"", u"", u"", u"", u"", u"", u"", u"", u"", u"", u"", u"", u""
    ],
}

# Nukta compositions: base Kannada consonant position (0..127) -> output.
# Triggered when a base consonant is followed by U+0CBC (nukta).
# Values follow ISO 15919 for Perso-Arabic and Dravidian loan sounds.
NUKTA_COMPOSITIONS = {
    21: "qa",    # ಕ಼  voiceless uvular stop /q/
    22: "ḵẖa",   # ಖ಼  voiceless uvular/velar fricative /x/
    23: "ġa",    # ಗ಼  voiced uvular/velar fricative /ɣ/
    28: "za",    # ಜ಼  voiced alveolar fricative /z/
    33: "ṛa",   # ಡ಼  retroflex flap /ɽ/
    34: "ṛha",  # ಢ಼  aspirated retroflex flap /ɽʰ/
    43: "fa",    # ಫ಼  voiceless labiodental fricative /f/
    47: "ẏa",    # ಯ಼  (Bengali-style y with nukta)
}
