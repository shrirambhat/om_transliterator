# om_transliterator

[![PyPI version](https://img.shields.io/pypi/v/om-transliterator.svg)](https://pypi.org/project/om-transliterator/)
[![Python versions](https://img.shields.io/pypi/pyversions/om-transliterator.svg)](https://pypi.org/project/om-transliterator/)
[![License](https://img.shields.io/badge/license-Apache%202.0-blue.svg)](LICENSE.txt)

**Kannada to English (Latin) transliteration in Python, following the ISO 15919 international standard.**

`om_transliterator` converts Kannada (ಕನ್ನಡ) Unicode text into romanized Latin text per [ISO 15919:2001](https://www.iso.org/standard/28333.html) — the standard transliteration scheme for Indic scripts. Use it for search indexing, linguistics, library catalogs, machine translation pipelines, name romanization, or any application that needs a deterministic Kannada-to-English conversion.

## Features

- **ISO 15919 compliant** — anusvara (ṁ), candrabindu (m̐), vocalic r/l with ring below (r̥, l̥), long vowel distinction (e/ē, o/ō), full retroflex series (ṭ, ḍ, ṇ, ṣ, ḷ).
- **Homorganic anusvara** — ಂ is rendered as the correct class nasal before stops (ಅಂಕ → `aṅka`, ಅಂತ → `anta`, ಅಂಪ → `ampa`).
- **Nukta-composed loan sounds** — ಜ಼ → `za`, ಫ಼ → `fa`, ಕ಼ → `qa`, ಖ಼ → `ḵẖa`, ಗ಼ → `ġa`, ಡ಼ → `ṛa`.
- **Dravidian letters** — ಱ → `ṟa`, ಳ → `ḷa`, ೞ → `ḻa`.
- **Ambiguity disambiguation** — `ba:i` (ಬಇ, consonant + independent vowel) vs `bai` (ಬೈ, matra) via colon insertion.
- **Pure Python, zero dependencies.** Stateless; safe for concurrent use across threads.
- **Typed str in, typed str out.** No Python 2 baggage. Non-Kannada characters pass through unchanged.

## Installation

```bash
pip install om-transliterator
```

Requires Python 3.7 or newer.

From source:

```bash
git clone https://github.com/shrirambhat/om_transliterator
cd om_transliterator
pip install .
```

## Quick start

```python
from om_transliterator import Transliterator

t = Transliterator()

print(t.knda_to_latn("ಮಹಾಭಾರತ"))
# mahābhārata

print(t.knda_to_latn("ಕೃಷ್ಣ"))
# kr̥ṣṇa

print(t.knda_to_latn("ಅಂಕ ಅಂತ ಅಂಪ"))
# aṅka anta ampa

print(t.knda_to_latn("ಜ಼ಮೀನ್ ಫ಼ೋನ್"))
# zamīn fōn
```

Mixed-script input is preserved:

```python
t.knda_to_latn("Hello, ಕನ್ನಡ!")
# 'Hello, kannaḍa!'
```

## API

### `class Transliterator`

Constructor takes no arguments. Instances are stateless — one can be reused across any number of calls or shared between threads.

#### `knda_to_latn(text: str) -> str`

Transliterate a Kannada Unicode string to ISO 15919 Latin.

- **`text`** — any string. Characters outside the Kannada block (U+0C80–U+0CFF) are copied verbatim.
- **Returns** — the transliterated string.

## Transliteration reference

| Category | Examples |
|---|---|
| Vowels (short/long) | ಅ→a, ಆ→ā, ಇ→i, ಈ→ī, ಉ→u, ಊ→ū, ಎ→e, ಏ→ē, ಒ→o, ಓ→ō, ಐ→ai, ಔ→au |
| Vocalic liquids | ಋ→r̥, ೠ→r̥̄, ಌ→l̥, ೡ→l̥̄ |
| Velars | ಕ→ka, ಖ→kha, ಗ→ga, ಘ→gha, ಙ→ṅa |
| Palatals | ಚ→ca, ಛ→cha, ಜ→ja, ಝ→jha, ಞ→ña |
| Retroflexes | ಟ→ṭa, ಠ→ṭha, ಡ→ḍa, ಢ→ḍha, ಣ→ṇa |
| Dentals | ತ→ta, ಥ→tha, ದ→da, ಧ→dha, ನ→na |
| Labials | ಪ→pa, ಫ→pha, ಬ→ba, ಭ→bha, ಮ→ma |
| Semivowels | ಯ→ya, ರ→ra, ಱ→ṟa, ಲ→la, ಳ→ḷa, ೞ→ḻa, ವ→va |
| Sibilants + h | ಶ→śa, ಷ→ṣa, ಸ→sa, ಹ→ha |
| Signs | ಂ→ṁ (anusvara), ಁ→m̐ (candrabindu), ಃ→ḥ (visarga), ್→∅ (virama), ಽ→' (avagraha) |
| Nukta loans | ಜ಼→za, ಫ಼→fa, ಕ಼→qa, ಖ಼→ḵẖa, ಗ಼→ġa |
| Digits | ೦೧೨೩೪೫೬೭೮೯ → 0123456789 |

### ISO 15919 vs IAST

`om_transliterator` follows ISO 15919, which differs from the older IAST convention in a few places:

| Character | ISO 15919 | IAST |
|---|---|---|
| Anusvara (ಂ) | **ṁ** (dot above) | ṃ (dot below) |
| Vocalic r (ಋ) | **r̥** (ring below) | ṛ (dot below) |
| Vocalic rr (ೠ) | **r̥̄** | ṝ |
| Vocalic l (ಌ) | **l̥** | ḷ |
| Short vs long e (ಎ / ಏ) | **e / ē** distinct | e / e (merged) |
| Short vs long o (ಒ / ಓ) | **o / ō** distinct | o / o (merged) |

The ring-below form for vocalic liquids also prevents collision with retroflexes — `ḷ` is reserved for the retroflex lateral ಳ (ḷa), and `ḻ` for the Dravidian retroflex approximant ೞ (ḻa).

## Development

```bash
git clone https://github.com/shrirambhat/om_transliterator
cd om_transliterator
pip install -e .[dev]
pytest
```

The test suite covers every rule: vowels, matras, virama, schwa deletion, ai/au ambiguity, homorganic anusvara across all five stop classes, nukta compositions, Dravidian letters, and end-of-string robustness.

## Contributing

Issues and pull requests are welcome at [github.com/shrirambhat/om_transliterator](https://github.com/shrirambhat/om_transliterator). When reporting a transliteration bug, please include the Kannada input, the current output, and a citation from ISO 15919 for the expected output.

## Credits

Originally created by [Shriram Bhat](https://shrirambhat.com) with contributions and guidance from Dinesh Shenoy, Prof. Purushothama Bilimale, Srikanth Lakshmanan, Sandesh B Suvarna, and Arjun Shetty.

## License

Licensed under the [Apache License, Version 2.0](http://www.apache.org/licenses/LICENSE-2.0). See [LICENSE.txt](LICENSE.txt) for details.

---

**Keywords:** Kannada transliteration Python, Kannada to English converter, ISO 15919 Python library, Kannada romanization, Kannada Latin script, ಕನ್ನಡ transliteration, Indic script transliteration, Brahmic script romanization, Kannada Unicode to Roman, Knda to Latn.
