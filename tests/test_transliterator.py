# Copyright (C) 2018 Shriram Bhat
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
# http://www.apache.org/licenses/LICENSE-2.0

"""Unit tests for the Kannada -> Latin ISO 15919 transliterator."""

import pytest

from om_transliterator import Transliterator


@pytest.fixture
def t():
    return Transliterator()


class TestBasicConsonantsAndVowels:
    def test_empty_string(self, t):
        assert t.knda_to_latn("") == ""

    def test_bare_consonant_keeps_schwa(self, t):
        assert t.knda_to_latn("ಕ") == "ka"

    def test_independent_vowels(self, t):
        assert t.knda_to_latn("ಅ") == "a"
        assert t.knda_to_latn("ಆ") == "ā"
        assert t.knda_to_latn("ಇ") == "i"
        assert t.knda_to_latn("ಈ") == "ī"
        assert t.knda_to_latn("ಉ") == "u"
        assert t.knda_to_latn("ಊ") == "ū"

    def test_visarga(self, t):
        assert t.knda_to_latn("ಅಃ") == "aḥ"


class TestMatras:
    def test_matra_strips_inherent_schwa(self, t):
        assert t.knda_to_latn("ಕಾ") == "kā"
        assert t.knda_to_latn("ಕಿ") == "ki"
        assert t.knda_to_latn("ಕೀ") == "kī"
        assert t.knda_to_latn("ಕು") == "ku"

    def test_virama_removes_schwa(self, t):
        # ಕ್ -> "k"
        assert t.knda_to_latn("ಕ್") == "k"

    def test_aspirate_retains_h_when_matra_applied(self, t):
        # ಭೀ -> "bhī"
        assert t.knda_to_latn("ಭೀ") == "bhī"


class TestVocalicRAndL:
    def test_independent_vocalic_r_uses_ring_below(self, t):
        # ISO 15919: r with ring below (U+0072 U+0325)
        assert t.knda_to_latn("ಋ") == "r\u0325"

    def test_independent_vocalic_l_uses_ring_below(self, t):
        # ISO 15919: l with ring below (no collision with retroflex la)
        assert t.knda_to_latn("ಌ") == "l\u0325"

    def test_matra_vocalic_r_after_consonant(self, t):
        # ಕೃ -> "kr̥"
        assert t.knda_to_latn("ಕೃ") == "kr\u0325"

    def test_krishna(self, t):
        # ಕೃಷ್ಣ -> "kr̥ṣṇa"
        assert t.knda_to_latn("ಕೃಷ್ಣ") == "kr\u0325ṣṇa"


class TestAmbiguityColon:
    def test_colon_between_consonant_schwa_and_independent_i(self, t):
        # ಬಇ should be "ba:i", not "bai"
        assert t.knda_to_latn("ಬಇ") == "ba:i"

    def test_colon_between_consonant_schwa_and_independent_u(self, t):
        assert t.knda_to_latn("ಬಉ") == "ba:u"

    def test_matra_ai_stays_single_cluster(self, t):
        # ಬೈ -> "bai" (matra, not separate i)
        assert t.knda_to_latn("ಬೈ") == "bai"


class TestAnusvara:
    def test_anusvara_default(self, t):
        # No following consonant -> default anusvara
        assert t.knda_to_latn("ಓಂ") == "ōṃ"

    def test_anusvara_before_velar(self, t):
        # ಅಂಕ -> aṅka
        assert t.knda_to_latn("ಅಂಕ") == "aṅka"

    def test_anusvara_before_palatal(self, t):
        # ಅಂಚ -> añca
        assert t.knda_to_latn("ಅಂಚ") == "añca"

    def test_anusvara_before_retroflex(self, t):
        # ಅಂಟ -> aṇṭa
        assert t.knda_to_latn("ಅಂಟ") == "aṇṭa"

    def test_anusvara_before_dental(self, t):
        # ಅಂತ -> anta
        assert t.knda_to_latn("ಅಂತ") == "anta"

    def test_anusvara_before_labial(self, t):
        # ಅಂಪ -> ampa
        assert t.knda_to_latn("ಅಂಪ") == "ampa"


class TestNukta:
    def test_ja_plus_nukta_becomes_za(self, t):
        assert t.knda_to_latn("ಜ಼") == "za"

    def test_pha_plus_nukta_becomes_fa(self, t):
        assert t.knda_to_latn("ಫ಼") == "fa"

    def test_nukta_does_not_leak_to_next_char(self, t):
        # "ಜ಼ ಫ಼" -> "za fa" (no stray chars)
        assert t.knda_to_latn("ಜ಼ ಫ಼") == "za fa"


class TestNonKannadaPassthrough:
    def test_ascii_letters_pass_through(self, t):
        assert t.knda_to_latn("hello") == "hello"

    def test_whitespace_and_punct_pass_through(self, t):
        assert t.knda_to_latn("ಕ ,") == "ka ,"

    def test_mixed_script(self, t):
        assert t.knda_to_latn("ಕ hello ಮ") == "ka hello ma"


class TestRobustness:
    def test_trailing_anusvara_no_crash(self, t):
        # Regression: lookahead past end used to raise IndexError
        assert t.knda_to_latn("ಕಂ") == "kaṃ"

    def test_trailing_ja_no_crash(self, t):
        # Regression: ja at end used to raise IndexError
        assert t.knda_to_latn("ಜ") == "ja"

    def test_trailing_pha_no_crash(self, t):
        assert t.knda_to_latn("ಫ") == "pha"

    def test_instance_state_is_not_leaked_between_calls(self, t):
        # Regression: previous implementation kept output on self
        t.knda_to_latn("ಕ")
        assert t.knda_to_latn("ಮ") == "ma"


class TestKnownWords:
    @pytest.mark.parametrize("knda,latn", [
        ("ಸಾಹಸ", "sāhasa"),
        ("ಭೀಮ", "bhīma"),
        ("ಮಹಾಭಾರತ", "mahābhārata"),
        ("ಆದಿ ಕವಿ", "ādi kavi"),
        ("ಗದಾಯುದ್ಧಂ", "gadāyuddhaṃ"),
    ])
    def test_words(self, t, knda, latn):
        assert t.knda_to_latn(knda) == latn
