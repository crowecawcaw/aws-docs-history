# Character sets for custom vocabularies and vocabulary filters

For each language Amazon Transcribe supports, there is a specific set of characters
Amazon Transcribe can recognize. When you create a custom vocabulary or vocabulary filter, use only
the characters listed in your language's character set. If you use unsupported characters, your custom
vocabulary or vocabulary filter fails.

###### Important

Be sure to check that your custom vocabulary file uses only the supported Unicode code points
and code point sequences listed within the following character sets.

Many Unicode characters can appear identical in popular fonts, even if they use different code
points. **Only the code points listed in this guide are supported**. For example, the
French word **déjà** can be rendered using _precomposed_
characters (where one Unicode value represents an accented character) or
_decomposed_ characters (where two Unicode values represent an accented
character, one value for the base character and another for the accent).

- **Precomposed version**: 0064 `00E9`
  006A `00E0` (renders as **déjà**)
- **Decomposed version**: 0064 `0065 0301`
  006A `0061 0300` (renders as
  **déjà**)

###### Topics

- [Abkhaz character set](#char-abkhaz "#char-abkhaz")
- [Afrikaans character set](#char-afrikaans "#char-afrikaans")
- [Arabic character set](#char-arabic "#char-arabic")
- [Asturian character set](#char-asturian "#char-asturian")
- [Azerbaijani character set](#char-azerbaijani "#char-azerbaijani")
- [Armenian character set](#char-armenian "#char-armenian")
- [Bashkir character set](#char-bashkir "#char-bashkir")
- [Basque character set](#char-basque "#char-basque")
- [Belarusian character set](#char-belarusian "#char-belarusian")
- [Bengali character set](#char-bengali "#char-bengali")
- [Bosnian character set](#char-bosnian "#char-bosnian")
- [Bulgarian character set](#char-bulgarian "#char-bulgarian")
- [Catalan character set](#char-catalan "#char-catalan")
- [Central Kurdish character set](#char-central-kurdish "#char-central-kurdish")
- [Chinese, Mandarin (Mainland China), Simplified character set](#char-chinese-man-cn "#char-chinese-man-cn")
- [Chinese, Mandarin (Taiwan), Traditional character set](#char-chinese-man-tw "#char-chinese-man-tw")
- [Chinese, Cantonese (Hong Kong), Traditional character set](#char-cantonese-hk "#char-cantonese-hk")
- [Croatian character set](#char-croatian "#char-croatian")
- [Czech character set](#char-czech "#char-czech")
- [Danish character set](#char-danish "#char-danish")
- [Dutch character set](#char-dutch "#char-dutch")
- [English character set](#char-english "#char-english")
- [Estonian character set](#char-estonian "#char-estonian")
- [Farsi character set](#char-farsi "#char-farsi")
- [Finnish character set](#char-finnish "#char-finnish")
- [French character set](#char-french "#char-french")
- [Galician character set](#char-galician "#char-galician")
- [Georgian character set](#char-georgian "#char-georgian")
- [German character set](#char-german "#char-german")
- [Greek character set](#char-greek "#char-greek")
- [Gujarati character set](#char-gujarati "#char-gujarati")
- [Hausa character set](#char-hausa "#char-hausa")
- [Hebrew character set](#char-hebrew "#char-hebrew")
- [Hindi character set](#char-hindi "#char-hindi")
- [Hungarian character set](#char-hungarian "#char-hungarian")
- [Icelandic character set](#char-icelandic "#char-icelandic")
- [Indonesian character set](#char-indonesian "#char-indonesian")
- [Italian character set](#char-italian "#char-italian")
- [Japanese character set](#char-japanese "#char-japanese")
- [Kabyle character set](#char-kabyle "#char-kabyle")
- [Kannada character set](#char-kannada "#char-kannada")
- [Kazakh character set](#char-kazakh "#char-kazakh")
- [Kinyarwanda character set](#char-kinyarwanda "#char-kinyarwanda")
- [Korean character set](#char-korean "#char-korean")
- [Kyrgyz character set](#char-kyrgyz "#char-kyrgyz")
- [Latvian character set](#char-latvian "#char-latvian")
- [Lithuanian character set](#char-lithuanian "#char-lithuanian")
- [Luganda character set](#char-luganda "#char-luganda")
- [Macedonian character set](#char-macedonian "#char-macedonian")
- [Malay character set](#char-malay "#char-malay")
- [Malayalam character set](#char-malayalam "#char-malayalam")
- [Maltese character set](#char-maltese "#char-maltese")
- [Marathi character set](#char-marathi "#char-marathi")
- [Meadow Mari character set](#char-meadow-mari "#char-meadow-mari")
- [Mongolian character set](#char-mongolian "#char-mongolian")
- [Norwegian Bokmål character set](#char-norwegian-bokmal "#char-norwegian-bokmal")
- [Odia/Oriya character set](#char-odia-oriya "#char-odia-oriya")
- [Pashto character set](#char-pashto "#char-pashto")
- [Polish character set](#char-polish "#char-polish")
- [Portuguese character set](#char-portuguese "#char-portuguese")
- [Punjabi character set](#char-punjabi "#char-punjabi")
- [Romanian character set](#char-romanian "#char-romanian")
- [Russian character set](#char-russian "#char-russian")
- [Serbian character set](#char-serbian "#char-serbian")
- [Sinhala character set](#char-sinhala "#char-sinhala")
- [Slovak character set](#char-slovak "#char-slovak")
- [Slovenian character set](#char-slovenian "#char-slovenian")
- [Somali character set](#char-somali "#char-somali")
- [Spanish character set](#char-spanish "#char-spanish")
- [Sundanese character set](#char-sundanese "#char-sundanese")
- [Swahili character set](#char-swahili "#char-swahili")
- [Swedish character set](#char-swedish "#char-swedish")
- [Tagalog/Filipino character set](#char-tagalog-filipino "#char-tagalog-filipino")
- [Tamil character set](#char-tamil "#char-tamil")
- [Tatar character set](#char-tatar "#char-tatar")
- [Telugu character set](#char-telugu "#char-telugu")
- [Thai character set](#char-thai "#char-thai")
- [Turkish character set](#char-turkish "#char-turkish")
- [Ukrainian character set](#char-ukrainian "#char-ukrainian")
- [Uyghur character set](#char-uyghur "#char-uyghur")
- [Uzbek character set](#char-uzbek "#char-uzbek")
- [Vietnamese character set](#char-vietnamese "#char-vietnamese")
- [Welsh character set](#char-welsh "#char-welsh")
- [Wolof character set](#char-wolof "#char-wolof")
- [Zulu character set](#char-zulu "#char-zulu")

## Abkhaz character set

For Abkhaz custom vocabularies, you can use the following characters in the
`Phrase` field:

- a - z
- - (hyphen)
- . (period)

You can also use the following Unicode characters in the `Phrase` field:

| Character | Code | Character | Code |
| --------- | ---- | --------- | ---- |
| а         | 0430 | љ         | 0459 |
| б         | 0431 | њ         | 045A |
| в         | 0432 | ћ         | 045B |
| г         | 0433 | ќ         | 045C |
| д         | 0434 | ѝ         | 045D |
| е         | 0435 | ў         | 045E |
| ж         | 0436 | џ         | 045F |
| з         | 0437 | ґ         | 0491 |
| и         | 0438 | ғ         | 0493 |
| й         | 0439 | җ         | 0497 |
| к         | 043A | ҙ         | 0499 |
| л         | 043B | қ         | 049B |
| м         | 043C | ҟ         | 049F |
| н         | 043D | ҡ         | 04A1 |
| о         | 043E | ң         | 04A3 |
| п         | 043F | ҥ         | 04A5 |
| р         | 0440 | ҩ         | 04A9 |
| с         | 0441 | ҫ         | 04AB |
| т         | 0442 | ҭ         | 04AD |
| у         | 0443 | ү         | 04AF |
| ф         | 0444 | ұ         | 04B1 |
| х         | 0445 | ҳ         | 04B3 |
| ц         | 0446 | ҵ         | 04B5 |
| ч         | 0447 | ҷ         | 04B7 |
| ш         | 0448 | һ         | 04BB |
| щ         | 0449 | ҽ         | 04BD |
| ъ         | 044A | ҿ         | 04BF |
| ы         | 044B | ӊ         | 04CA |
| ь         | 044C | ӑ         | 04D1 |
| э         | 044D | ӓ         | 04D3 |
| ю         | 044E | ӗ         | 04D7 |
| я         | 044F | ә         | 04D9 |
| ѐ         | 0450 | ӡ         | 04E1 |
| ё         | 0451 | ӣ         | 04E3 |
| ђ         | 0452 | ӧ         | 04E7 |
| ѓ         | 0453 | ө         | 04E9 |
| є         | 0454 | ӯ         | 04EF |
| ѕ         | 0455 | ӱ         | 04F1 |
| і         | 0456 | ӳ         | 04F3 |
| ї         | 0457 | ӷ         | 04F7 |
| ј         | 0458 | ӹ         | 04F9 |
| ԥ         | 0525 |

## Afrikaans character set

For Afrikaans custom vocabularies, you can use the following characters in the
`Phrase` field:

- a - z
- - (hyphen)
- . (period)

You can also use the following Unicode characters in the `Phrase` field:

| Character | Code | Character | Code |
| --------- | ---- | --------- | ---- |
| á         | 00E1 | ï         | 00EF |
| è         | 00E8 | ó         | 00F3 |
| é         | 00E9 | ô         | 00F4 |
| ê         | 00EA | ö         | 00F6 |
| ë         | 00EB | ú         | 00FA |
| í         | 00ED | û         | 00FB |
| î         | 00EE | ü         | 00FC |

## Arabic character set

For Arabic custom vocabularies, you can use the following Unicode characters in the
`Phrase` field. You can also use the hyphen (-)
character to separate words.

| Character | Code | Character | Code |
| --------- | ---- | --------- | ---- |
| ء         | 0621 | س         | 0633 |
| آ         | 0622 | ش         | 0634 |
| أ         | 0623 | ص         | 0635 |
| ؤ         | 0624 | ض         | 0636 |
| إ         | 0625 | ط         | 0637 |
| ئ         | 0626 | ظ         | 0638 |
| ا         | 0627 | ع         | 0639 |
| ب         | 0628 | غ         | 063A |
| ة         | 0629 | ف         | 0641 |
| ت         | 062A | ق         | 0642 |
| ث         | 062B | ك         | 0643 |
| ج         | 062C | ل         | 0644 |
| ح         | 062D | م         | 0645 |
| خ         | 062E | ن         | 0646 |
| د         | 062F | ه         | 0647 |
| ذ         | 0630 | و         | 0648 |
| ر         | 0631 | ى         | 0649 |
| ز         | 0632 | ي         | 064A |

## Asturian character set

For Asturian custom vocabularies, you can use the following characters in the
`Phrase` field:

- a - z
- - (hyphen)
- . (period)

You can also use the following Unicode characters in the `Phrase` field:

| Character | Code | Character | Code |
| --------- | ---- | --------- | ---- |
| á         | 00E1 | ñ         | 00F1 |
| é         | 00E9 | ó         | 00F3 |
| í         | 00ED | ú         | 00FA |
| ü         | 00FC |

## Azerbaijani character set

For Azerbaijani custom vocabularies, you can use the following characters in the
`Phrase` field:

- a - z
- - (hyphen)
- . (period)

You can also use the following Unicode characters in the `Phrase` field:

| Character | Code | Character | Code |
| --------- | ---- | --------- | ---- |
| ä         | 00E4 | ğ         | 011F |
| ç         | 00E7 | ı         | 0131 |
| ö         | 00F6 | ş         | 015F |
| ü         | 00FC | ə         | 0259 |
| ̇          | 0307 |

## Armenian character set

For Armenian custom vocabularies, you can use the following characters in the
`Phrase` field:

- a - z
- - (hyphen)
- . (period)

You can also use the following Unicode characters in the `Phrase` field:

| Character | Code | Character | Code |
| --------- | ---- | --------- | ---- |
| ա         | 0561 | մ         | 0574 |
| բ         | 0562 | յ         | 0575 |
| գ         | 0563 | ն         | 0576 |
| դ         | 0564 | շ         | 0577 |
| ե         | 0565 | ո         | 0578 |
| զ         | 0566 | չ         | 0579 |
| է         | 0567 | պ         | 057A |
| ը         | 0568 | ջ         | 057B |
| թ         | 0569 | ռ         | 057C |
| ժ         | 056A | ս         | 057D |
| ի         | 056B | վ         | 057E |
| լ         | 056C | տ         | 057F |
| խ         | 056D | ր         | 0580 |
| ծ         | 056E | ց         | 0581 |
| կ         | 056F | ւ         | 0582 |
| հ         | 0570 | փ         | 0583 |
| ձ         | 0571 | ք         | 0584 |
| ղ         | 0572 | օ         | 0585 |
| ճ         | 0573 | ֆ         | 0586 |

## Bashkir character set

For Bashkir custom vocabularies, you can use the following characters in the
`Phrase` field:

- a - z
- - (hyphen)
- . (period)

You can also use the following Unicode characters in the `Phrase` field:

| Character | Code | Character | Code |
| --------- | ---- | --------- | ---- |
| а         | 0430 | љ         | 0459 |
| б         | 0431 | њ         | 045A |
| в         | 0432 | ћ         | 045B |
| г         | 0433 | ќ         | 045C |
| д         | 0434 | ѝ         | 045D |
| е         | 0435 | ў         | 045E |
| ж         | 0436 | џ         | 045F |
| з         | 0437 | ґ         | 0491 |
| и         | 0438 | ғ         | 0493 |
| й         | 0439 | җ         | 0497 |
| к         | 043A | ҙ         | 0499 |
| л         | 043B | қ         | 049B |
| м         | 043C | ҟ         | 049F |
| н         | 043D | ҡ         | 04A1 |
| о         | 043E | ң         | 04A3 |
| п         | 043F | ҥ         | 04A5 |
| р         | 0440 | ҩ         | 04A9 |
| с         | 0441 | ҫ         | 04AB |
| т         | 0442 | ҭ         | 04AD |
| у         | 0443 | ү         | 04AF |
| ф         | 0444 | ұ         | 04B1 |
| х         | 0445 | ҳ         | 04B3 |
| ц         | 0446 | ҵ         | 04B5 |
| ч         | 0447 | ҷ         | 04B7 |
| ш         | 0448 | һ         | 04BB |
| щ         | 0449 | ҽ         | 04BD |
| ъ         | 044A | ҿ         | 04BF |
| ы         | 044B | ӊ         | 04CA |
| ь         | 044C | ӑ         | 04D1 |
| э         | 044D | ӓ         | 04D3 |
| ю         | 044E | ӗ         | 04D7 |
| я         | 044F | ә         | 04D9 |
| ѐ         | 0450 | ӡ         | 04E1 |
| ё         | 0451 | ӣ         | 04E3 |
| ђ         | 0452 | ӧ         | 04E7 |
| ѓ         | 0453 | ө         | 04E9 |
| є         | 0454 | ӯ         | 04EF |
| ѕ         | 0455 | ӱ         | 04F1 |
| і         | 0456 | ӳ         | 04F3 |
| ї         | 0457 | ӷ         | 04F7 |
| ј         | 0458 | ӹ         | 04F9 |

## Basque character set

For Basque custom vocabularies, you can use the following characters in the
`Phrase` field:

- a - z
- - (hyphen)
- . (period)

You can also use the following Unicode characters in the `Phrase` field:

| Character | Code | Character | Code |
| --------- | ---- | --------- | ---- |
| á         | 00E1 | ñ         | 00F1 |
| é         | 00E9 | ó         | 00F3 |
| í         | 00ED | ú         | 00FA |
| ü         | 00FC |

## Belarusian character set

For Belarusian custom vocabularies, you can use the following characters in the
`Phrase` field:

- a - z
- - (hyphen)
- . (period)

You can also use the following Unicode characters in the `Phrase` field:

| Character | Code | Character | Code |
| --------- | ---- | --------- | ---- |
| а         | 0430 | с         | 0441 |
| б         | 0431 | т         | 0442 |
| в         | 0432 | у         | 0443 |
| г         | 0433 | ф         | 0444 |
| д         | 0434 | х         | 0445 |
| е         | 0435 | ц         | 0446 |
| ж         | 0436 | ч         | 0447 |
| з         | 0437 | ш         | 0448 |
| й         | 0439 | ы         | 044B |
| к         | 043A | ь         | 044C |
| л         | 043B | э         | 044D |
| м         | 043C | ю         | 044E |
| н         | 043D | я         | 044F |
| о         | 043E | ё         | 0451 |
| п         | 043F | і         | 0456 |
| р         | 0440 | ў         | 045E |

## Bengali character set

For Bengali custom vocabularies, you can use the following characters in the
`Phrase` field:

- a - z
- - (hyphen)
- . (period)

You can also use the following Unicode characters in the `Phrase` field:

| Character | Code | Character | Code |
| --------- | ---- | --------- | ---- |
| ঁ         | 0981 | দ         | 09A6 |
| ং         | 0982 | ধ         | 09A7 |
| ঃ         | 0983 | ন         | 09A8 |
| অ         | 0985 | প         | 09AA |
| আ         | 0986 | ফ         | 09AB |
| ই         | 0987 | ব         | 09AC |
| ঈ         | 0988 | ভ         | 09AD |
| উ         | 0989 | ম         | 09AE |
| ঊ         | 098A | য         | 09AF |
| ঋ         | 098B | র         | 09B0 |
| এ         | 098F | ল         | 09B2 |
| ঐ         | 0990 | শ         | 09B6 |
| ও         | 0993 | ষ         | 09B7 |
| ঔ         | 0994 | স         | 09B8 |
| ক         | 0995 | হ         | 09B9 |
| খ         | 0996 | ়         | 09BC |
| গ         | 0997 | ঽ         | 09BD |
| ঘ         | 0998 | া         | 09BE |
| ঙ         | 0999 | ি         | 09BF |
| চ         | 099A | ী         | 09C0 |
| ছ         | 099B | ু         | 09C1 |
| জ         | 099C | ূ         | 09C2 |
| ঝ         | 099D | ৃ         | 09C3 |
| ঞ         | 099E | ৄ         | 09C4 |
| ট         | 099F | ে         | 09C7 |
| ঠ         | 09A0 | ৈ         | 09C8 |
| ড         | 09A1 | ো         | 09CB |
| ঢ         | 09A2 | ৌ         | 09CC |
| ণ         | 09A3 | ্         | 09CD |
| ত         | 09A4 | ৎ         | 09CE |
| থ         | 09A5 | ৗ         | 09D7 |

## Bosnian character set

For Bosnian custom vocabularies, you can use the following characters in the
`Phrase` field:

- a - z
- - (hyphen)
- . (period)

You can also use the following Unicode characters in the `Phrase` field:

| Character | Code | Character | Code |
| --------- | ---- | --------- | ---- |
| ć         | 0107 | đ         | 0111 |
| č         | 010D | š         | 0161 |
| ž         | 017E |

## Bulgarian character set

For Bulgarian custom vocabularies, you can use the following characters in the
`Phrase` field:

- a - z
- - (hyphen)
- . (period)

You can also use the following Unicode characters in the `Phrase` field:

| Character | Code | Character | Code |
| --------- | ---- | --------- | ---- |
| а         | 0430 | п         | 043F |
| б         | 0431 | р         | 0440 |
| в         | 0432 | с         | 0441 |
| г         | 0433 | т         | 0442 |
| д         | 0434 | у         | 0443 |
| е         | 0435 | ф         | 0444 |
| ж         | 0436 | х         | 0445 |
| з         | 0437 | ц         | 0446 |
| и         | 0438 | ч         | 0447 |
| й         | 0439 | ш         | 0448 |
| к         | 043A | щ         | 0449 |
| л         | 043B | ъ         | 044A |
| м         | 043C | ь         | 044C |
| н         | 043D | ю         | 044E |
| о         | 043E | я         | 044F |

## Catalan character set

For Catalan custom vocabularies, you can use the following characters in the
`Phrase` field:

- a - z
- - (hyphen)
- . (period)

You can also use the following Unicode characters in the `Phrase` field:

| Character | Code | Character | Code |
| --------- | ---- | --------- | ---- |
| à         | 00E0 | ï         | 00EF |
| ç         | 00E7 | ò         | 00F2 |
| è         | 00E8 | ó         | 00F3 |
| é         | 00E9 | ú         | 00FA |
| í         | 00ED | ü         | 00FC |
| ŀ         | 0140 |

## Central Kurdish character set

For Central Kurdish custom vocabularies, you can use the following characters in the
`Phrase` field:

- a - z
- - (hyphen)
- . (period)

You can also use the following Unicode characters in the `Phrase` field:

| Character | Code | Character | Code |
| --------- | ---- | --------- | ---- |
| ئ         | 0626 | م         | 0645 |
| ا         | 0627 | ن         | 0646 |
| ب         | 0628 | و         | 0648 |
| ت         | 062A | پ         | 067E |
| ج         | 062C | چ         | 0686 |
| ح         | 062D | ڕ         | 0695 |
| خ         | 062E | ژ         | 0698 |
| د         | 062F | ڤ         | 06A4 |
| ر         | 0631 | ک         | 06A9 |
| ز         | 0632 | گ         | 06AF |
| س         | 0633 | ڵ         | 06B5 |
| ش         | 0634 | ھ         | 06BE |
| ع         | 0639 | ۆ         | 06C6 |
| غ         | 063A | ۇ         | 06C7 |
| ف         | 0641 | ی         | 06CC |
| ق         | 0642 | ێ         | 06CE |
| ل         | 0644 | ە         | 06D5 |

## Chinese, Mandarin (Mainland China), Simplified character set

For Chinese (Simplified) custom vocabularies, the `Phrase` field can use any of
the characters listed in the following file:

- [zh-cn-character-set](samples/zh-cn-character-set.md "samples/zh-cn-character-set.md")

The `SoundsLike` field can contain the pinyin syllables listed in the following
file:

- [pinyin-character-set](samples/pinyin-character-set.md "samples/pinyin-character-set.md")

When you use pinyin syllables in the `SoundsLike` field, separate the syllables
with a hyphen (-).

Amazon Transcribe represents the four tones in Chinese (Simplified) using numbers. The following table
shows how tone marks are mapped for the word 'ma'.

| Tone   | Tone mark | Tone number |
| ------ | --------- | ----------- |
| Tone 1 | mā        | ma1         |
| Tone 2 | má        | ma2         |
| Tone 3 | mǎ        | ma3         |
| Tone 4 | mà        | ma4         |

###### Note

For the 5th (neutral) tone, you can use Tone 1, with the exception of 'er', which must
be mapped to Tone 2. For example, 打转儿 would be represented as 'da3-zhuan4-er2'.

Chinese (Simplified) custom vocabularies don't use the `IPA` field, but you must still
include the `IPA` header in the custom vocabulary table.

The following example is an input file in text format. The example uses spaces to align the
columns. Your input files should use TAB characters to separate the columns. Include spaces only
in the `DisplayAs` column.

```
Phrase       SoundsLike               IPA     DisplayAs
康健          kang1-jian4
谴责          qian3-ze2
国防大臣        guo2-fang2-da4-chen2
世界博览会      shi4-jie4-bo2-lan3-hui4          世博会
```

## Chinese, Mandarin (Taiwan), Traditional character set

For Chinese (Traditional) custom vocabularies, the `Phrase` field can use any
of the characters listed in the following file:

- [zh-tw-character-set](samples/zh-tw-character-set.md "samples/zh-tw-character-set.md")

The `SoundsLike` field can contain the zhuyin syllables listed in the following
file:

- [zhuyin-character-set](samples/zhuyin-character-set.md "samples/zhuyin-character-set.md")

When you use zhuyin syllables in the `SoundsLike` field, separate the syllables
with a hyphen (-).

Amazon Transcribe represents the four tones in Chinese (Traditional) using numbers. The following table
shows how tone marks are mapped for the word ㄇㄚ.

| Tone   | Tone mark |
| ------ | --------- |
| Tone 1 | ㄇㄚ      |
| Tone 2 | ㄇㄚˊ     |
| Tone 3 | ㄇㄚˇ     |
| Tone 4 | ㄇㄚˋ     |

Chinese (Traditional) custom vocabularies don't use the `IPA` field, but you
must still include the `IPA` header in the custom vocabulary table.

The following example is an input file in text format. The example uses spaces to align the
columns. Your input files should use TAB characters to separate the columns. Include spaces only
in the `DisplayAs` column.

```
Phrase        SoundsLike                     IPA        DisplayAs
健康          ㄐㄧㄢˋ-ㄎㄤ
譴責          ㄑㄧㄢˇ-ㄗㄜˊ
國防部長       ㄍㄨㄛˊ-ㄈㄤˊ-ㄅㄨˋ-ㄓㄤˇ
世界博覽會     ㄕˋ-ㄐㄧㄝˋ-ㄅㄛˊ-ㄌㄢˇ-ㄏㄨㄟˋ             世博會

```

## Chinese, Cantonese (Hong Kong), Traditional character set

For Chinese (Cantonese) Hong Kong custom vocabularies, the `Phrase` field can use any of
the characters listed in the following file:

- [zh-hk-character-set](samples/zh-hk-character-set.md "samples/zh-hk-character-set.md")

## Croatian character set

For Croatian custom vocabularies, you can use the following characters in the
`Phrase` field:

- a - z
- - (hyphen)
- . (period)

You can also use the following Unicode characters in the `Phrase` field:

| Character | Code | Character | Code |
| --------- | ---- | --------- | ---- |
| ć         | 0107 | đ         | 0111 |
| č         | 010D | š         | 0161 |
| ž         | 017E |

## Czech character set

For Czech custom vocabularies, you can use the following characters in the
`Phrase` field:

- a - z
- - (hyphen)
- . (period)

You can also use the following Unicode characters in the `Phrase` field:

| Character | Code | Character | Code |
| --------- | ---- | --------- | ---- |
| á         | 00E1 | ď         | 010F |
| é         | 00E9 | ě         | 011B |
| í         | 00ED | ň         | 0148 |
| ó         | 00F3 | ř         | 0159 |
| ú         | 00FA | š         | 0161 |
| ý         | 00FD | ť         | 0165 |
| č         | 010D | ů         | 016F |
| ž         | 017E |

## Danish character set

For Danish custom vocabularies, you can use the following characters in the
`Phrase` field:

- a - z
- A - Z
- - (hyphen)
- . (period)

You can also use the following Unicode characters in the `Phrase` field:

| Character | Code | Character | Code |
| --------- | ---- | --------- | ---- |
| Å         | 00C5 | æ         | 00E6 |
| Æ         | 00C6 | é         | 00E9 |
| Ø         | 00D8 | ø         | 00F8 |
| å         | 00E5 |

## Dutch character set

For Dutch custom vocabularies, you can use the following characters in the
`Phrase` field:

- a - z
- A - Z
- ' (apostrophe)
- - (hyphen)
- . (period)

You can also use the following Unicode characters in the `Phrase` field:

| Character | Code | Character | Code |
| --------- | ---- | --------- | ---- |
| à         | 00E0 | î         | 00EE |
| á         | 00E1 | ï         | 00EF |
| â         | 00E2 | ñ         | 00F1 |
| ä         | 00E4 | ò         | 00F2 |
| ç         | 00E7 | ó         | 00F3 |
| è         | 00E8 | ô         | 00F4 |
| é         | 00E9 | ö         | 00F6 |
| ê         | 00EA | ù         | 00F9 |
| ë         | 00EB | ú         | 00FA |
| ì         | 00EC | û         | 00FB |
| í         | 00ED | ü         | 00FC |

## English character set

For English custom vocabularies, you can use the following characters in the
`Phrase` field:

- a - z
- A - Z
- ' (apostrophe)
- - (hyphen)
- . (period)

## Estonian character set

For Estonian custom vocabularies, you can use the following characters in the
`Phrase` field:

- a - z
- - (hyphen)
- . (period)

You can also use the following Unicode characters in the `Phrase` field:

| Character | Code | Character | Code |
| --------- | ---- | --------- | ---- |
| ä         | 00E4 | ü         | 00FC |
| õ         | 00F5 | š         | 0161 |
| ö         | 00F6 | ž         | 017E |

## Farsi character set

For Farsi custom vocabularies, you can use the following characters in the
`Phrase` field.

| Character | Code | Character | Code |
| --------- | ---- | --------- | ---- |
| ء         | 0621 | ظ         | 0638 |
| آ         | 0622 | ع         | 0639 |
| أ         | 0623 | غ         | 063A |
| ؤ         | 0624 | ف         | 0641 |
| ئ         | 0626 | ق         | 0642 |
| ا         | 0627 | ل         | 0644 |
| ب         | 0628 | م         | 0645 |
| ت         | 062A | ن         | 0646 |
| ث         | 062B | ه         | 0647 |
| ج         | 062C | و         | 0648 |
| ح         | 062D | َ         | 064E |
| خ         | 062E | ُ         | 064F |
| د         | 062F | ِ         | 0650 |
| ذ         | 0630 | ّ         | 0651 |
| ر         | 0631 | پ         | 067E |
| ز         | 0632 | چ         | 0686 |
| س         | 0633 | ژ         | 0698 |
| ش         | 0634 | ک         | 06A9 |
| ص         | 0635 | گ         | 06AF |
| ض         | 0636 | ی         | 06CC |
| ط         | 0637 |           |      |

## Finnish character set

For Finnish custom vocabularies, you can use the following characters in the
`Phrase` field:

- a - z
- - (hyphen)
- . (period)

You can also use the following Unicode characters in the `Phrase` field:

| Character | Code | Character | Code |
| --------- | ---- | --------- | ---- |
| ä         | 00E4 | ö         | 00F6 |
| å         | 00E5 | š         | 0161 |
| ž         | 017E |

## French character set

For French custom vocabularies, you can use the following characters in the
`Phrase` field:

- a - z
- A - Z
- ' (apostrophe)
- - (hyphen)
- . (period)

You can also use the following Unicode characters in the `Phrase` field:

| Character | Code | Character | Code |
| --------- | ---- | --------- | ---- |
| À         | 00C0 | à         | 00E0 |
| Â         | 00C2 | â         | 00E2 |
| Ç         | 00C7 | ç         | 00E7 |
| È         | 00C8 | è         | 00E8 |
| É         | 00C9 | é         | 00E9 |
| Ê         | 00CA | ê         | 00EA |
| Ë         | 00CB | ë         | 00EB |
| Î         | 00CE | î         | 00EE |
| Ï         | 00CF | ï         | 00EF |
| Ô         | 00D4 | ô         | 00F4 |
| Ö         | 00D6 | ö         | 00F6 |
| Ù         | 00D9 | ù         | 00F9 |
| Û         | 00DB | û         | 00FB |
| Ü         | 00DC | ü         | 00FC |

## Galician character set

For Galician custom vocabularies, you can use the following characters in the
`Phrase` field:

- a - z
- - (hyphen)
- . (period)

You can also use the following Unicode characters in the `Phrase` field:

| Character | Code | Character | Code |
| --------- | ---- | --------- | ---- |
| á         | 00E1 | ñ         | 00F1 |
| é         | 00E9 | ó         | 00F3 |
| í         | 00ED | ú         | 00FA |
| ü         | 00FC |

## Georgian character set

For Georgian custom vocabularies, you can use the following characters in the
`Phrase` field:

- a - z
- - (hyphen)
- . (period)

You can also use the following Unicode characters in the `Phrase` field:

| Character | Code | Character | Code |
| --------- | ---- | --------- | ---- |
| ა         | 10D0 | რ         | 10E0 |
| ბ         | 10D1 | ს         | 10E1 |
| გ         | 10D2 | ტ         | 10E2 |
| დ         | 10D3 | უ         | 10E3 |
| ე         | 10D4 | ფ         | 10E4 |
| ვ         | 10D5 | ქ         | 10E5 |
| ზ         | 10D6 | ღ         | 10E6 |
| თ         | 10D7 | ყ         | 10E7 |
| ი         | 10D8 | შ         | 10E8 |
| კ         | 10D9 | ჩ         | 10E9 |
| ლ         | 10DA | ც         | 10EA |
| მ         | 10DB | ძ         | 10EB |
| ნ         | 10DC | წ         | 10EC |
| ო         | 10DD | ჭ         | 10ED |
| პ         | 10DE | ხ         | 10EE |
| ჟ         | 10DF | ჯ         | 10EF |
| ჰ         | 10F0 |

## German character set

For German custom vocabularies, you can use the following characters in the
`Phrase` field:

- a - z
- A - Z
- ' (apostrophe)
- - (hyphen)
- . (period)

You can also use the following Unicode characters in the `Phrase` field:

| Character | Code | Character | Code |
| --------- | ---- | --------- | ---- |
| ä         | 00E4 | Ä         | 00C4 |
| ö         | 00F6 | Ö         | 00D6 |
| ü         | 00FC | Ü         | 00DC |
| ß         | 00DF |           |      |

## Greek character set

For Greek custom vocabularies, you can use the following characters in the
`Phrase` field:

- a - z
- - (hyphen)
- . (period)

You can also use the following Unicode characters in the `Phrase` field:

| Character | Code | Character | Code |
| --------- | ---- | --------- | ---- |
| ά         | 03AC | ν         | 03BD |
| έ         | 03AD | ξ         | 03BE |
| ή         | 03AE | ο         | 03BF |
| ί         | 03AF | π         | 03C0 |
| ΰ         | 03B0 | ρ         | 03C1 |
| α         | 03B1 | ς         | 03C2 |
| β         | 03B2 | σ         | 03C3 |
| γ         | 03B3 | τ         | 03C4 |
| δ         | 03B4 | υ         | 03C5 |
| ε         | 03B5 | φ         | 03C6 |
| ζ         | 03B6 | χ         | 03C7 |
| η         | 03B7 | ψ         | 03C8 |
| θ         | 03B8 | ω         | 03C9 |
| ι         | 03B9 | ϊ         | 03CA |
| κ         | 03BA | ϋ         | 03CB |
| λ         | 03BB | ό         | 03CC |
| μ         | 03BC | ώ         | 03CE |
| ΐ         | 0390 |

## Gujarati character set

For Gujarati custom vocabularies, you can use the following characters in the
`Phrase` field:

- a - z
- - (hyphen)
- . (period)

You can also use the following Unicode characters in the `Phrase` field:

| Character | Code | Character | Code |
| --------- | ---- | --------- | ---- |
| ઁ         | 0A81 | દ         | 0AA6 |
| ં         | 0A82 | ધ         | 0AA7 |
| ઃ         | 0A83 | ન         | 0AA8 |
| અ         | 0A85 | પ         | 0AAA |
| આ         | 0A86 | ફ         | 0AAB |
| ઇ         | 0A87 | બ         | 0AAC |
| ઈ         | 0A88 | ભ         | 0AAD |
| ઉ         | 0A89 | મ         | 0AAE |
| ઊ         | 0A8A | ય         | 0AAF |
| ઋ         | 0A8B | ર         | 0AB0 |
| ઍ         | 0A8D | લ         | 0AB2 |
| એ         | 0A8F | ળ         | 0AB3 |
| ઐ         | 0A90 | વ         | 0AB5 |
| ઑ         | 0A91 | શ         | 0AB6 |
| ઓ         | 0A93 | ષ         | 0AB7 |
| ઔ         | 0A94 | સ         | 0AB8 |
| ક         | 0A95 | હ         | 0AB9 |
| ખ         | 0A96 | ઼         | 0ABC |
| ગ         | 0A97 | ા         | 0ABE |
| ઘ         | 0A98 | િ         | 0ABF |
| ઙ         | 0A99 | ી         | 0AC0 |
| ચ         | 0A9A | ુ         | 0AC1 |
| છ         | 0A9B | ૂ         | 0AC2 |
| જ         | 0A9C | ૃ         | 0AC3 |
| ઝ         | 0A9D | ૅ         | 0AC5 |
| ઞ         | 0A9E | ે         | 0AC7 |
| ટ         | 0A9F | ૈ         | 0AC8 |
| ઠ         | 0AA0 | ૉ         | 0AC9 |
| ડ         | 0AA1 | ો         | 0ACB |
| ઢ         | 0AA2 | ૌ         | 0ACC |
| ણ         | 0AA3 | ્         | 0ACD |
| ત         | 0AA4 | ૐ         | 0AD0 |
| થ         | 0AA5 | ૠ         | 0AE0 |

## Hausa character set

For Hausa custom vocabularies, you can use the following characters in the
`Phrase` field:

- a - z
- - (hyphen)
- . (period)

You can also use the following Unicode characters in the `Phrase` field:

| Character | Code | Character | Code |
| --------- | ---- | --------- | ---- |
| ƙ         | 0199 | ɓ         | 0253 |
| ƴ         | 01B4 | ɗ         | 0257 |
| ̃          | 0303 |

## Hebrew character set

For Hebrew custom vocabularies, you can use the following Unicode characters in the
`Phrase` field:

| Character | Code | Character | Code |
| --------- | ---- | --------- | ---- |
| -         | 002D | ם         | 05DD |
| א         | 05D0 | מ         | 05DE |
| ב         | 05D1 | ן         | 05DF |
| ג         | 05D2 | נ         | 05E0 |
| ד         | 05D3 | ס         | 05E1 |
| ה         | 05D4 | ע         | 05E2 |
| ו         | 05D5 | ף         | 05E3 |
| ז         | 05D6 | פ         | 05E4 |
| ח         | 05D7 | ץ         | 05E5 |
| ט         | 05D8 | צ         | 05E6 |
| י         | 05D9 | ק         | 05E7 |
| ך         | 05DA | ר         | 05E8 |
| כ         | 05DB | ש         | 05E9 |
| ל         | 05DC | ת         | 05EA |

## Hindi character set

For Hindi custom vocabularies, you can use the following Unicode characters in the
`Phrase` field:

| Character | Code | Character | Code |
| --------- | ---- | --------- | ---- |
| -         | 002D | थ         | 0925 |
| .         | 002E | द         | 0926 |
| ँ         | 0901 | ध         | 0927 |
| ं         | 0902 | न         | 0928 |
| ः         | 0903 | प         | 092A |
| अ         | 0905 | फ         | 092B |
| आ         | 0906 | ब         | 092C |
| इ         | 0907 | भ         | 092D |
| ई         | 0908 | म         | 092E |
| उ         | 0909 | य         | 092F |
| ऊ         | 090A | र         | 0930 |
| ऋ         | 090B | ल         | 0932 |
| ए         | 090F | व         | 0935 |
| ऐ         | 0910 | श         | 0936 |
| ऑ         | 0911 | ष         | 0937 |
| ओ         | 0913 | स         | 0938 |
| औ         | 0914 | ह         | 0939 |
| क         | 0915 | ा         | 093E |
| ख         | 0916 | ि         | 093F |
| ग         | 0917 | ी         | 0940 |
| घ         | 0918 | ु         | 0941 |
| ङ         | 0919 | ू         | 0942 |
| च         | 091A | ृ         | 0943 |
| छ         | 091B | ॅ         | 0945 |
| ज         | 091C | े         | 0947 |
| झ         | 091D | ै         | 0948 |
| ञ         | 091E | ॉ         | 0949 |
| ट         | 091F | ो         | 094B |
| ठ         | 0920 | ौ         | 094C |
| ड         | 0921 | ्         | 094D |
| ढ         | 0922 | ज़         | 095B |
| ण         | 0923 | ड़         | 095C |
| त         | 0924 | ढ़         | 095D |

Amazon Transcribe maps the following characters:

| Character | Mapped to |
| --------- | --------- |
| ऩ (0929)  | न (0928)  |
| ऱ (0931)  | र (0930)  |
| क़ (0958)  | क (0915)  |
| ख़ (0959)  | ख (0916)  |
| ग़ (095A)  | ग (0917)  |
| फ़ (095E)  | फ (092B)  |
| य़ (095F)  | य (092F)  |

## Hungarian character set

For Hungarian custom vocabularies, you can use the following characters in the
`Phrase` field:

- a - z
- - (hyphen)
- . (period)

You can also use the following Unicode characters in the `Phrase` field:

| Character | Code | Character | Code |
| --------- | ---- | --------- | ---- |
| á         | 00E1 | ö         | 00F6 |
| é         | 00E9 | ú         | 00FA |
| í         | 00ED | ü         | 00FC |
| ó         | 00F3 | ő         | 0151 |
| ű         | 0171 |

## Icelandic character set

For Icelandic custom vocabularies, you can use the following characters in the
`Phrase` field:

- a - z
- - (hyphen)
- . (period)

You can also use the following Unicode characters in the `Phrase` field:

| Character | Code | Character | Code |
| --------- | ---- | --------- | ---- |
| á         | 00E1 | ú         | 00FA |
| é         | 00E9 | ý         | 00FD |
| ð         | 00F0 | þ         | 00FE |
| í         | 00ED | æ         | 00E6 |
| ó         | 00F3 | ö         | 00F6 |

## Indonesian character set

For Indonesian custom vocabularies, you can use the following characters in the
`Phrase` field:

- a - z
- A - Z
- ' (apostrophe)
- - (hyphen)
- . (period)

## Italian character set

For Italian custom vocabularies, you can use the following characters in the
`Phrase` field:

- a - z
- A - Z
- ' (apostrophe)
- - (hyphen)
- . (period)

You can also use the following Unicode characters in the `Phrase` field:

| Character | Code | Character | Code |
| --------- | ---- | --------- | ---- |
| À         | 00C0 | à         | 00E0 |
| Ä         | 00C4 | ä         | 00E4 |
| Ç         | 00C7 | ç         | 00E7 |
| È         | 00C8 | è         | 00E8 |
| É         | 00C9 | é         | 00E9 |
| Ê         | 00CA | ê         | 00EA |
| Ë         | 00CB | ë         | 00EB |
| Ì         | 00CC | ì         | 00EC |
| Ò         | 00D2 | ò         | 00F2 |
| Ù         | 00D9 | ù         | 00F9 |
| Ü         | 00DC | ü         | 00FC |

## Japanese character set

For Japanese custom vocabularies, the `DisplayAs` field supports all hiragana,
katakana, and kanji characters, and fullwidth romaji capital letters.

The `Phrase` field supports the characters listed in the following file:

- [ja-jp-character-set](samples/ja-jp-character-set.md "samples/ja-jp-character-set.md")

## Kabyle character set

For Kabyle custom vocabularies, you can use the following characters in the
`Phrase` field:

- a - z
- - (hyphen)
- . (period)

You can also use the following Unicode characters in the `Phrase` field:

| Character | Code | Character | Code |
| --------- | ---- | --------- | ---- |
| ï         | 00EF | ḍ         | 1E0D |
| č         | 010D | ḥ         | 1E25 |
| ř         | 0159 | ṛ         | 1E5B |
| ǧ         | 01E7 | ṣ         | 1E63 |
| ɛ         | 025B | ṭ         | 1E6D |
| ɣ         | 0263 | ẓ         | 1E93 |

## Kannada character set

For Kannada custom vocabularies, you can use the following characters in the
`Phrase` field:

- a - z
- - (hyphen)
- . (period)

You can also use the following Unicode characters in the `Phrase` field:

| Character | Code | Character | Code |
| --------- | ---- | --------- | ---- |
| ಂ         | 0C82 | ಧ         | 0CA7 |
| ಃ         | 0C83 | ನ         | 0CA8 |
| ಅ         | 0C85 | ಪ         | 0CAA |
| ಆ         | 0C86 | ಫ         | 0CAB |
| ಇ         | 0C87 | ಬ         | 0CAC |
| ಈ         | 0C88 | ಭ         | 0CAD |
| ಉ         | 0C89 | ಮ         | 0CAE |
| ಊ         | 0C8A | ಯ         | 0CAF |
| ಋ         | 0C8B | ರ         | 0CB0 |
| ಎ         | 0C8E | ಲ         | 0CB2 |
| ಏ         | 0C8F | ಳ         | 0CB3 |
| ಐ         | 0C90 | ವ         | 0CB5 |
| ಒ         | 0C92 | ಶ         | 0CB6 |
| ಓ         | 0C93 | ಷ         | 0CB7 |
| ಔ         | 0C94 | ಸ         | 0CB8 |
| ಕ         | 0C95 | ಹ         | 0CB9 |
| ಖ         | 0C96 | ಼         | 0CBC |
| ಗ         | 0C97 | ಽ         | 0CBD |
| ಘ         | 0C98 | ಾ         | 0CBE |
| ಙ         | 0C99 | ಿ         | 0CBF |
| ಚ         | 0C9A | ೀ         | 0CC0 |
| ಛ         | 0C9B | ು         | 0CC1 |
| ಜ         | 0C9C | ೂ         | 0CC2 |
| ಝ         | 0C9D | ೃ         | 0CC3 |
| ಞ         | 0C9E | ೆ         | 0CC6 |
| ಟ         | 0C9F | ೇ         | 0CC7 |
| ಠ         | 0CA0 | ೈ         | 0CC8 |
| ಡ         | 0CA1 | ೊ         | 0CCA |
| ಢ         | 0CA2 | ೋ         | 0CCB |
| ಣ         | 0CA3 | ೌ         | 0CCC |
| ತ         | 0CA4 | ್         | 0CCD |
| ಥ         | 0CA5 | ೕ         | 0CD5 |
| ದ         | 0CA6 | ೖ         | 0CD6 |
| ೠ         | 0CE0 |

## Kazakh character set

For Kazakh custom vocabularies, you can use the following characters in the
`Phrase` field:

- a - z
- - (hyphen)
- . (period)

You can also use the following Unicode characters in the `Phrase` field:

| Character | Code | Character | Code |
| --------- | ---- | --------- | ---- |
| т         | 0442 | ы         | 044B |
| б         | 0431 | я         | 044F |
| о         | 043E | с         | 0441 |
| п         | 043F | һ         | 04BB |
| ш         | 0448 | д         | 0434 |
| и         | 0438 | р         | 0440 |
| ч         | 0447 | г         | 0433 |
| н         | 043D | ё         | 0451 |
| қ         | 049B | й         | 0439 |
| і         | 0456 | ө         | 04E9 |
| щ         | 0449 | в         | 0432 |
| е         | 0435 | э         | 044D |
| ә         | 04D9 | ң         | 04A3 |
| ю         | 044E | л         | 043B |
| з         | 0437 | ф         | 0444 |
| х         | 0445 | к         | 043A |
| ц         | 0446 | у         | 0443 |
| ү         | 04AF | ж         | 0436 |
| м         | 043C | ғ         | 0493 |
| ь         | 044C | а         | 0430 |
| ъ         | 044A | ұ         | 04B1 |

## Kinyarwanda character set

For Kinyarwanda custom vocabularies, you can use the following characters in the
`Phrase` field:

- a - z
- - (hyphen)
- . (period)

You can also use the following Unicode characters in the `Phrase` field:

| Character | Code | Character | Code |
| --------- | ---- | --------- | ---- |
| á         | 00E1 | ó         | 00F3 |
| â         | 00E2 | ô         | 00F4 |
| ã         | 00E3 | ú         | 00FA |
| ç         | 00E7 | ü         | 00FC |
| è         | 00E8 | ā         | 0101 |
| é         | 00E9 | ē         | 0113 |
| ê         | 00EA | ī         | 012B |
| ë         | 00EB | ō         | 014D |
| í         | 00ED | ū         | 016B |
| ï         | 00EF | ́          | 0301 |

## Korean character set

For Korean custom vocabularies, you can use any of the Hangul syllables in the
`Phrase` field. For more information, see [Hangul Syllables](https://en.wikipedia.org/wiki/Hangul_Syllables "https://en.wikipedia.org/wiki/Hangul_Syllables") on
Wikipedia.

## Kyrgyz character set

For Kyrgyz custom vocabularies, you can use the following characters in the
`Phrase` field:

- a - z
- - (hyphen)
- . (period)

You can also use the following Unicode characters in the `Phrase` field:

| Character | Code | Character | Code |
| --------- | ---- | --------- | ---- |
| а         | 0430 | љ         | 0459 |
| б         | 0431 | њ         | 045A |
| в         | 0432 | ћ         | 045B |
| г         | 0433 | ќ         | 045C |
| д         | 0434 | ѝ         | 045D |
| е         | 0435 | ў         | 045E |
| ж         | 0436 | џ         | 045F |
| з         | 0437 | ґ         | 0491 |
| и         | 0438 | ғ         | 0493 |
| й         | 0439 | җ         | 0497 |
| к         | 043A | ҙ         | 0499 |
| л         | 043B | қ         | 049B |
| м         | 043C | ҟ         | 049F |
| н         | 043D | ҡ         | 04A1 |
| о         | 043E | ң         | 04A3 |
| п         | 043F | ҥ         | 04A5 |
| р         | 0440 | ҩ         | 04A9 |
| с         | 0441 | ҫ         | 04AB |
| т         | 0442 | ҭ         | 04AD |
| у         | 0443 | ү         | 04AF |
| ф         | 0444 | ұ         | 04B1 |
| х         | 0445 | ҳ         | 04B3 |
| ц         | 0446 | ҵ         | 04B5 |
| ч         | 0447 | ҷ         | 04B7 |
| ш         | 0448 | һ         | 04BB |
| щ         | 0449 | ҽ         | 04BD |
| ъ         | 044A | ҿ         | 04BF |
| ы         | 044B | ӊ         | 04CA |
| ь         | 044C | ӑ         | 04D1 |
| э         | 044D | ӓ         | 04D3 |
| ю         | 044E | ӗ         | 04D7 |
| я         | 044F | ә         | 04D9 |
| ѐ         | 0450 | ӡ         | 04E1 |
| ё         | 0451 | ӣ         | 04E3 |
| ђ         | 0452 | ӧ         | 04E7 |
| ѓ         | 0453 | ө         | 04E9 |
| є         | 0454 | ӯ         | 04EF |
| ѕ         | 0455 | ӱ         | 04F1 |
| і         | 0456 | ӳ         | 04F3 |
| ї         | 0457 | ӷ         | 04F7 |
| ј         | 0458 | ӹ         | 04F9 |

## Latvian character set

For Latvian custom vocabularies, you can use the following characters in the
`Phrase` field:

- a - z
- - (hyphen)
- . (period)

You can also use the following Unicode characters in the `Phrase` field:

| Character | Code | Character | Code |
| --------- | ---- | --------- | ---- |
| ā         | 0101 | ķ         | 0137 |
| č         | 010D | ļ         | 013C |
| ē         | 0113 | ņ         | 0146 |
| ģ         | 0123 | š         | 0161 |
| ī         | 012B | ū         | 016B |
| ž         | 017E |

## Lithuanian character set

For Lithuanian custom vocabularies, you can use the following characters in the
`Phrase` field:

- a - z
- - (hyphen)
- . (period)

You can also use the following Unicode characters in the `Phrase` field:

| Character | Code | Character | Code |
| --------- | ---- | --------- | ---- |
| ą         | 0105 | į         | 012F |
| č         | 010D | š         | 0161 |
| ę         | 0119 | ų         | 0173 |
| ė         | 0117 | ū         | 016B |
| ž         | 017E |

## Luganda character set

For Luganda custom vocabularies, you can use the following characters in the
`Phrase` field:

- a - z
- - (hyphen)
- . (period)

You can also use the following Unicode characters in the `Phrase` field:

| Character | Code | Character | Code |
| --------- | ---- | --------- | ---- |
| ÿ         | 00FF | ŋ         | 014B |

## Macedonian character set

For Macedonian custom vocabularies, you can use the following characters in the
`Phrase` field:

- a - z
- - (hyphen)
- . (period)

You can also use the following Unicode characters in the `Phrase` field:

| Character | Code | Character | Code |
| --------- | ---- | --------- | ---- |
| а         | 0430 | љ         | 0459 |
| б         | 0431 | њ         | 045A |
| в         | 0432 | ћ         | 045B |
| г         | 0433 | ќ         | 045C |
| д         | 0434 | ѝ         | 045D |
| е         | 0435 | ў         | 045E |
| ж         | 0436 | џ         | 045F |
| з         | 0437 | ґ         | 0491 |
| и         | 0438 | ғ         | 0493 |
| й         | 0439 | җ         | 0497 |
| к         | 043A | ҙ         | 0499 |
| л         | 043B | қ         | 049B |
| м         | 043C | ҟ         | 049F |
| н         | 043D | ҡ         | 04A1 |
| о         | 043E | ң         | 04A3 |
| п         | 043F | ҥ         | 04A5 |
| р         | 0440 | ҩ         | 04A9 |
| с         | 0441 | ҫ         | 04AB |
| т         | 0442 | ҭ         | 04AD |
| у         | 0443 | ү         | 04AF |
| ф         | 0444 | ұ         | 04B1 |
| х         | 0445 | ҳ         | 04B3 |
| ц         | 0446 | ҵ         | 04B5 |
| ч         | 0447 | ҷ         | 04B7 |
| ш         | 0448 | һ         | 04BB |
| щ         | 0449 | ҽ         | 04BD |
| ъ         | 044A | ҿ         | 04BF |
| ы         | 044B | ӊ         | 04CA |
| ь         | 044C | ӑ         | 04D1 |
| э         | 044D | ӓ         | 04D3 |
| ю         | 044E | ӗ         | 04D7 |
| я         | 044F | ә         | 04D9 |
| ѐ         | 0450 | ӡ         | 04E1 |
| ё         | 0451 | ӣ         | 04E3 |
| ђ         | 0452 | ӧ         | 04E7 |
| ѓ         | 0453 | ө         | 04E9 |
| є         | 0454 | ӯ         | 04EF |
| ѕ         | 0455 | ӱ         | 04F1 |
| і         | 0456 | ӳ         | 04F3 |
| ї         | 0457 | ӷ         | 04F7 |
| ј         | 0458 | ӹ         | 04F9 |

## Malay character set

For Malay custom vocabularies, you can use the following characters in the
`Phrase` field:

- a - z
- A - Z
- ' (apostrophe)
- - (hyphen)
- . (period)

## Malayalam character set

For Malayalam custom vocabularies, you can use the following characters in the
`Phrase` field:

- a - z
- - (hyphen)
- . (period)

You can also use the following Unicode characters in the `Phrase` field:

| Character | Code | Character | Code |
| --------- | ---- | --------- | ---- |
| ം         | 0D02 | ന         | 0D28 |
| ഃ         | 0D03 | പ         | 0D2A |
| അ         | 0D05 | ഫ         | 0D2B |
| ആ         | 0D06 | ബ         | 0D2C |
| ഇ         | 0D07 | ഭ         | 0D2D |
| ഈ         | 0D08 | മ         | 0D2E |
| ഉ         | 0D09 | യ         | 0D2F |
| ഊ         | 0D0A | ര         | 0D30 |
| ഋ         | 0D0B | റ         | 0D31 |
| എ         | 0D0E | ല         | 0D32 |
| ഏ         | 0D0F | ള         | 0D33 |
| ഐ         | 0D10 | ഴ         | 0D34 |
| ഒ         | 0D12 | വ         | 0D35 |
| ഓ         | 0D13 | ശ         | 0D36 |
| ഔ         | 0D14 | ഷ         | 0D37 |
| ക         | 0D15 | സ         | 0D38 |
| ഖ         | 0D16 | ഹ         | 0D39 |
| ഗ         | 0D17 | ാ         | 0D3E |
| ഘ         | 0D18 | ി         | 0D3F |
| ങ         | 0D19 | ീ         | 0D40 |
| ച         | 0D1A | ു         | 0D41 |
| ഛ         | 0D1B | ൂ         | 0D42 |
| ജ         | 0D1C | ൃ         | 0D43 |
| ഝ         | 0D1D | െ         | 0D46 |
| ഞ         | 0D1E | േ         | 0D47 |
| ട         | 0D1F | ൈ         | 0D48 |
| ഠ         | 0D20 | ൊ         | 0D4A |
| ഡ         | 0D21 | ോ         | 0D4B |
| ഢ         | 0D22 | ൌ         | 0D4C |
| ണ         | 0D23 | ്         | 0D4D |
| ത         | 0D24 | ൺ         | 0D7A |
| ഥ         | 0D25 | ൻ         | 0D7B |
| ദ         | 0D26 | ർ         | 0D7C |
| ധ         | 0D27 | ൽ         | 0D7D |

## Maltese character set

For Maltese custom vocabularies, you can use the following characters in the
`Phrase` field:

- a - z
- - (hyphen)
- . (period)

You can also use the following Unicode characters in the `Phrase` field:

| Character | Code | Character | Code |
| --------- | ---- | --------- | ---- |
| à         | 00E0 | ù         | 00F9 |
| è         | 00E8 | ċ         | 010B |
| ì         | 00EC | ġ         | 0121 |
| ò         | 00F2 | ħ         | 0127 |
| ż         | 017C |

## Marathi character set

For Marathi custom vocabularies, you can use the following characters in the
`Phrase` field:

- a - z
- - (hyphen)
- . (period)

You can also use the following Unicode characters in the `Phrase` field:

| Character | Code | Character | Code |
| --------- | ---- | --------- | ---- |
| ँ         | 0901 | थ         | 0925 |
| ं         | 0902 | द         | 0926 |
| ः         | 0903 | ध         | 0927 |
| अ         | 0905 | न         | 0928 |
| आ         | 0906 | प         | 092A |
| इ         | 0907 | फ         | 092B |
| ई         | 0908 | ब         | 092C |
| उ         | 0909 | भ         | 092D |
| ऊ         | 090A | म         | 092E |
| ऋ         | 090B | य         | 092F |
| ऍ         | 090D | र         | 0930 |
| ए         | 090F | ल         | 0932 |
| ऐ         | 0910 | ळ         | 0933 |
| ऑ         | 0911 | व         | 0935 |
| ओ         | 0913 | श         | 0936 |
| औ         | 0914 | ष         | 0937 |
| क         | 0915 | स         | 0938 |
| ख         | 0916 | ह         | 0939 |
| ग         | 0917 | ़         | 093C |
| घ         | 0918 | ा         | 093E |
| ङ         | 0919 | ि         | 093F |
| च         | 091A | ी         | 0940 |
| छ         | 091B | ु         | 0941 |
| ज         | 091C | ू         | 0942 |
| झ         | 091D | ृ         | 0943 |
| ञ         | 091E | ॅ         | 0945 |
| ट         | 091F | े         | 0947 |
| ठ         | 0920 | ै         | 0948 |
| ड         | 0921 | ॉ         | 0949 |
| ढ         | 0922 | ो         | 094B |
| ण         | 0923 | ौ         | 094C |
| त         | 0924 | ्         | 094D |
| ॐ         | 0950 |

## Meadow Mari character set

For Meadow Mari custom vocabularies, you can use the following characters in the
`Phrase` field:

- a - z
- - (hyphen)
- . (period)

You can also use the following Unicode characters in the `Phrase` field:

| Character | Code | Character | Code |
| --------- | ---- | --------- | ---- |
| а         | 0430 | љ         | 0459 |
| б         | 0431 | њ         | 045A |
| в         | 0432 | ћ         | 045B |
| г         | 0433 | ќ         | 045C |
| д         | 0434 | ѝ         | 045D |
| е         | 0435 | ў         | 045E |
| ж         | 0436 | џ         | 045F |
| з         | 0437 | ґ         | 0491 |
| и         | 0438 | ғ         | 0493 |
| й         | 0439 | җ         | 0497 |
| к         | 043A | ҙ         | 0499 |
| л         | 043B | қ         | 049B |
| м         | 043C | ҟ         | 049F |
| н         | 043D | ҡ         | 04A1 |
| о         | 043E | ң         | 04A3 |
| п         | 043F | ҥ         | 04A5 |
| р         | 0440 | ҩ         | 04A9 |
| с         | 0441 | ҫ         | 04AB |
| т         | 0442 | ҭ         | 04AD |
| у         | 0443 | ү         | 04AF |
| ф         | 0444 | ұ         | 04B1 |
| х         | 0445 | ҳ         | 04B3 |
| ц         | 0446 | ҵ         | 04B5 |
| ч         | 0447 | ҷ         | 04B7 |
| ш         | 0448 | һ         | 04BB |
| щ         | 0449 | ҽ         | 04BD |
| ъ         | 044A | ҿ         | 04BF |
| ы         | 044B | ӊ         | 04CA |
| ь         | 044C | ӑ         | 04D1 |
| э         | 044D | ӓ         | 04D3 |
| ю         | 044E | ӗ         | 04D7 |
| я         | 044F | ә         | 04D9 |
| ѐ         | 0450 | ӡ         | 04E1 |
| ё         | 0451 | ӣ         | 04E3 |
| ђ         | 0452 | ӧ         | 04E7 |
| ѓ         | 0453 | ө         | 04E9 |
| є         | 0454 | ӯ         | 04EF |
| ѕ         | 0455 | ӱ         | 04F1 |
| і         | 0456 | ӳ         | 04F3 |
| ї         | 0457 | ӷ         | 04F7 |
| ј         | 0458 | ӹ         | 04F9 |

## Mongolian character set

For Mongolian custom vocabularies, you can use the following characters in the
`Phrase` field:

- a - z
- - (hyphen)
- . (period)

You can also use the following Unicode characters in the `Phrase` field:

| Character | Code | Character | Code |
| --------- | ---- | --------- | ---- |
| а         | 0430 | љ         | 0459 |
| б         | 0431 | њ         | 045A |
| в         | 0432 | ћ         | 045B |
| г         | 0433 | ќ         | 045C |
| д         | 0434 | ѝ         | 045D |
| е         | 0435 | ў         | 045E |
| ж         | 0436 | џ         | 045F |
| з         | 0437 | ґ         | 0491 |
| и         | 0438 | ғ         | 0493 |
| й         | 0439 | җ         | 0497 |
| к         | 043A | ҙ         | 0499 |
| л         | 043B | қ         | 049B |
| м         | 043C | ҟ         | 049F |
| н         | 043D | ҡ         | 04A1 |
| о         | 043E | ң         | 04A3 |
| п         | 043F | ҥ         | 04A5 |
| р         | 0440 | ҩ         | 04A9 |
| с         | 0441 | ҫ         | 04AB |
| т         | 0442 | ҭ         | 04AD |
| у         | 0443 | ү         | 04AF |
| ф         | 0444 | ұ         | 04B1 |
| х         | 0445 | ҳ         | 04B3 |
| ц         | 0446 | ҵ         | 04B5 |
| ч         | 0447 | ҷ         | 04B7 |
| ш         | 0448 | һ         | 04BB |
| щ         | 0449 | ҽ         | 04BD |
| ъ         | 044A | ҿ         | 04BF |
| ы         | 044B | ӊ         | 04CA |
| ь         | 044C | ӑ         | 04D1 |
| э         | 044D | ӓ         | 04D3 |
| ю         | 044E | ӗ         | 04D7 |
| я         | 044F | ә         | 04D9 |
| ѐ         | 0450 | ӡ         | 04E1 |
| ё         | 0451 | ӣ         | 04E3 |
| ђ         | 0452 | ӧ         | 04E7 |
| ѓ         | 0453 | ө         | 04E9 |
| є         | 0454 | ӯ         | 04EF |
| ѕ         | 0455 | ӱ         | 04F1 |
| і         | 0456 | ӳ         | 04F3 |
| ї         | 0457 | ӷ         | 04F7 |
| ј         | 0458 | ӹ         | 04F9 |

## Norwegian Bokmål character set

For Norwegian Bokmål custom vocabularies, you can use the following characters in the
`Phrase` field:

- a - z
- - (hyphen)
- . (period)

You can also use the following Unicode characters in the `Phrase` field:

| Character | Code | Character | Code |
| --------- | ---- | --------- | ---- |
| å         | 00E5 | æ         | 00E6 |
| ø         | 00F8 |

## Odia/Oriya character set

For Odia/Oriya custom vocabularies, you can use the following characters in the
`Phrase` field:

- a - z
- - (hyphen)
- . (period)

You can also use the following Unicode characters in the `Phrase` field:

| Character | Code | Character | Code |
| --------- | ---- | --------- | ---- |
| ଁ         | 0B01 | ଦ         | 0B26 |
| ଂ         | 0B02 | ଧ         | 0B27 |
| ଃ         | 0B03 | ନ         | 0B28 |
| ଅ         | 0B05 | ପ         | 0B2A |
| ଆ         | 0B06 | ଫ         | 0B2B |
| ଇ         | 0B07 | ବ         | 0B2C |
| ଈ         | 0B08 | ଭ         | 0B2D |
| ଉ         | 0B09 | ମ         | 0B2E |
| ଊ         | 0B0A | ଯ         | 0B2F |
| ଋ         | 0B0B | ର         | 0B30 |
| ଏ         | 0B0F | ଲ         | 0B32 |
| ଐ         | 0B10 | ଳ         | 0B33 |
| ଓ         | 0B13 | ଶ         | 0B36 |
| ଔ         | 0B14 | ଷ         | 0B37 |
| କ         | 0B15 | ସ         | 0B38 |
| ଖ         | 0B16 | ହ         | 0B39 |
| ଗ         | 0B17 | ଼         | 0B3C |
| ଘ         | 0B18 | ା         | 0B3E |
| ଙ         | 0B19 | ି         | 0B3F |
| ଚ         | 0B1A | ୀ         | 0B40 |
| ଛ         | 0B1B | ୁ         | 0B41 |
| ଜ         | 0B1C | ୂ         | 0B42 |
| ଝ         | 0B1D | ୃ         | 0B43 |
| ଞ         | 0B1E | େ         | 0B47 |
| ଟ         | 0B1F | ୈ         | 0B48 |
| ଠ         | 0B20 | ୋ         | 0B4B |
| ଡ         | 0B21 | ୌ         | 0B4C |
| ଢ         | 0B22 | ୍         | 0B4D |
| ଣ         | 0B23 | ୖ         | 0B56 |
| ତ         | 0B24 | ୟ         | 0B5F |
| ଥ         | 0B25 | ୠ         | 0B60 |
| ୱ         | 0B71 |

## Pashto character set

For Pashto custom vocabularies, you can use the following characters in the
`Phrase` field:

- a - z
- - (hyphen)
- . (period)

You can also use the following Unicode characters in the `Phrase` field:

| Character | Code | Character | Code |
| --------- | ---- | --------- | ---- |
| آ         | 0622 | و         | 0648 |
| أ         | 0623 | ي         | 064A |
| ؤ         | 0624 | ً         | 064B |
| ئ         | 0626 | ٌ         | 064C |
| ا         | 0627 | ٍ         | 064D |
| ب         | 0628 | َ         | 064E |
| ت         | 062A | ُ         | 064F |
| ث         | 062B | ِ         | 0650 |
| ج         | 062C | ّ         | 0651 |
| ح         | 062D | ْ         | 0652 |
| خ         | 062E | ٔ         | 0654 |
| د         | 062F | ٰ         | 0670 |
| ذ         | 0630 | ټ         | 067C |
| ر         | 0631 | پ         | 067E |
| ز         | 0632 | ځ         | 0681 |
| س         | 0633 | څ         | 0685 |
| ش         | 0634 | چ         | 0686 |
| ص         | 0635 | ډ         | 0689 |
| ض         | 0636 | ړ         | 0693 |
| ط         | 0637 | ږ         | 0696 |
| ظ         | 0638 | ژ         | 0698 |
| ع         | 0639 | ښ         | 069A |
| غ         | 063A | ک         | 06A9 |
| ف         | 0641 | ګ         | 06AB |
| ق         | 0642 | گ         | 06AF |
| ل         | 0644 | ڼ         | 06BC |
| م         | 0645 | ی         | 06CC |
| ن         | 0646 | ۍ         | 06CD |
| ه         | 0647 | ې         | 06D0 |

## Polish character set

For Polish custom vocabularies, you can use the following characters in the
`Phrase` field:

- a - z
- - (hyphen)
- . (period)

You can also use the following Unicode characters in the `Phrase` field:

| Character | Code | Character | Code |
| --------- | ---- | --------- | ---- |
| ó         | 00F3 | ł         | 0142 |
| ą         | 0105 | ń         | 0144 |
| ć         | 0107 | ś         | 015B |
| ę         | 0119 | ź         | 017A |
| ż         | 017C |

## Portuguese character set

For Portuguese custom vocabularies, you can use the following characters in the
`Phrase` field:

- a - z
- A - Z
- ' (apostrophe)
- - (hyphen)
- . (period)

You can also use the following Unicode characters in the `Phrase` field:

| Character | Code | Character | Code |
| --------- | ---- | --------- | ---- |
| À         | 00C0 | à         | 00E0 |
| Á         | 00C1 | á         | 00E1 |
| Â         | 00C2 | â         | 00E2 |
| Ã         | 00C3 | ã         | 00E3 |
| Ä         | 00C4 | ä         | 00E4 |
| Ç         | 00C7 | ç         | 00E7 |
| È         | 00C8 | è         | 00E8 |
| É         | 00C9 | é         | 00E9 |
| Ê         | 00CA | ê         | 00EA |
| Ë         | 00CB | ë         | 00EB |
| Í         | 00CD | í         | 00ED |
| Ñ         | 00D1 | ñ         | 00F1 |
| Ó         | 00D3 | ó         | 00F3 |
| Ô         | 00D4 | ô         | 00F4 |
| Õ         | 00D5 | õ         | 00F5 |
| Ö         | 00D6 | ö         | 00F6 |
| Ú         | 00DA | ú         | 00FA |
| Ü         | 00DC | ü         | 00FC |

## Punjabi character set

For Punjabi custom vocabularies, you can use the following characters in the
`Phrase` field:

- a - z
- - (hyphen)
- . (period)

You can also use the following Unicode characters in the `Phrase` field:

| Character | Code | Character | Code |
| --------- | ---- | --------- | ---- |
| ਅ         | 0A05 | ਧ         | 0A27 |
| ਆ         | 0A06 | ਨ         | 0A28 |
| ਇ         | 0A07 | ਪ         | 0A2A |
| ਈ         | 0A08 | ਫ         | 0A2B |
| ਉ         | 0A09 | ਬ         | 0A2C |
| ਊ         | 0A0A | ਭ         | 0A2D |
| ਏ         | 0A0F | ਮ         | 0A2E |
| ਐ         | 0A10 | ਯ         | 0A2F |
| ਓ         | 0A13 | ਰ         | 0A30 |
| ਔ         | 0A14 | ਲ         | 0A32 |
| ਕ         | 0A15 | ਵ         | 0A35 |
| ਖ         | 0A16 | ਸ         | 0A38 |
| ਗ         | 0A17 | ਹ         | 0A39 |
| ਘ         | 0A18 | ਼         | 0A3C |
| ਙ         | 0A19 | ਾ         | 0A3E |
| ਚ         | 0A1A | ਿ         | 0A3F |
| ਛ         | 0A1B | ੀ         | 0A40 |
| ਜ         | 0A1C | ੁ         | 0A41 |
| ਝ         | 0A1D | ੂ         | 0A42 |
| ਞ         | 0A1E | ੇ         | 0A47 |
| ਟ         | 0A1F | ੈ         | 0A48 |
| ਠ         | 0A20 | ੋ         | 0A4B |
| ਡ         | 0A21 | ੌ         | 0A4C |
| ਢ         | 0A22 | ੍         | 0A4D |
| ਣ         | 0A23 | ੜ         | 0A5C |
| ਤ         | 0A24 | ੰ         | 0A70 |
| ਥ         | 0A25 | ੱ         | 0A71 |
| ਦ         | 0A26 | ੲ         | 0A72 |
| ੳ         | 0A73 |

## Romanian character set

For Romanian custom vocabularies, you can use the following characters in the
`Phrase` field:

- a - z
- - (hyphen)
- . (period)

You can also use the following Unicode characters in the `Phrase` field:

| Character | Code | Character | Code |
| --------- | ---- | --------- | ---- |
| ă         | 0103 | ș         | 0219 |
| â         | 00E2 | ț         | 021B |
| î         | 00EE | ş         | 015F |
| ţ         | 0163 |

## Russian character set

For Russian custom vocabularies, you can use the following characters in the
`Phrase` field:

| Character | Code | Character | Code |
| --------- | ---- | --------- | ---- |
| '         | 0027 | п         | 043F |
| -         | 002D | р         | 0440 |
| .         | 002E | с         | 0441 |
| а         | 0430 | т         | 0442 |
| б         | 0431 | у         | 0443 |
| в         | 0432 | ф         | 0444 |
| г         | 0433 | х         | 0445 |
| д         | 0434 | ц         | 0446 |
| е         | 0435 | ч         | 0447 |
| ж         | 0436 | ш         | 0448 |
| з         | 0437 | щ         | 0449 |
| и         | 0438 | ъ         | 044A |
| й         | 0439 | ы         | 044B |
| к         | 043A | ь         | 044C |
| л         | 043B | э         | 044D |
| м         | 043C | ю         | 044E |
| н         | 043D | я         | 044F |
| о         | 043E | ё         | 0451 |

## Serbian character set

For Serbian custom vocabularies, you can use the following characters in the
`Phrase` field:

- a - z
- - (hyphen)
- . (period)

You can also use the following Unicode characters in the `Phrase` field:

| Character | Code | Character | Code |
| --------- | ---- | --------- | ---- |
| ć         | 0107 | і         | 0456 |
| č         | 010D | ї         | 0457 |
| đ         | 0111 | ј         | 0458 |
| š         | 0161 | љ         | 0459 |
| ž         | 017E | њ         | 045A |
| а         | 0430 | ћ         | 045B |
| б         | 0431 | ќ         | 045C |
| в         | 0432 | ѝ         | 045D |
| г         | 0433 | ў         | 045E |
| д         | 0434 | џ         | 045F |
| е         | 0435 | ґ         | 0491 |
| ж         | 0436 | ғ         | 0493 |
| з         | 0437 | җ         | 0497 |
| и         | 0438 | ҙ         | 0499 |
| й         | 0439 | қ         | 049B |
| к         | 043A | ҟ         | 049F |
| л         | 043B | ҡ         | 04A1 |
| м         | 043C | ң         | 04A3 |
| н         | 043D | ҥ         | 04A5 |
| о         | 043E | ҩ         | 04A9 |
| п         | 043F | ҫ         | 04AB |
| р         | 0440 | ҭ         | 04AD |
| с         | 0441 | ү         | 04AF |
| т         | 0442 | ұ         | 04B1 |
| у         | 0443 | ҳ         | 04B3 |
| ф         | 0444 | ҵ         | 04B5 |
| х         | 0445 | ҷ         | 04B7 |
| ц         | 0446 | һ         | 04BB |
| ч         | 0447 | ҽ         | 04BD |
| ш         | 0448 | ҿ         | 04BF |
| щ         | 0449 | ӊ         | 04CA |
| ъ         | 044A | ӑ         | 04D1 |
| ы         | 044B | ӓ         | 04D3 |
| ь         | 044C | ӗ         | 04D7 |
| э         | 044D | ә         | 04D9 |
| ю         | 044E | ӡ         | 04E1 |
| я         | 044F | ӣ         | 04E3 |
| ѐ         | 0450 | ӧ         | 04E7 |
| ё         | 0451 | ө         | 04E9 |
| ђ         | 0452 | ӯ         | 04EF |
| ѓ         | 0453 | ӱ         | 04F1 |
| є         | 0454 | ӳ         | 04F3 |
| ѕ         | 0455 | ӷ         | 04F7 |
| ӹ         | 04F9 |

## Sinhala character set

For Sinhala custom vocabularies, you can use the following characters in the
`Phrase` field:

- a - z
- - (hyphen)
- . (period)

You can also use the following Unicode characters in the `Phrase` field:

| Character | Code | Character | Code |
| --------- | ---- | --------- | ---- |
| ං         | 0D82 | ද         | 0DAF |
| ඃ         | 0D83 | ධ         | 0DB0 |
| අ         | 0D85 | න         | 0DB1 |
| ආ         | 0D86 | ඳ         | 0DB3 |
| ඇ         | 0D87 | ප         | 0DB4 |
| ඈ         | 0D88 | ඵ         | 0DB5 |
| ඉ         | 0D89 | බ         | 0DB6 |
| ඊ         | 0D8A | භ         | 0DB7 |
| උ         | 0D8B | ම         | 0DB8 |
| ඌ         | 0D8C | ඹ         | 0DB9 |
| ඍ         | 0D8D | ය         | 0DBA |
| එ         | 0D91 | ර         | 0DBB |
| ඒ         | 0D92 | ල         | 0DBD |
| ඓ         | 0D93 | ව         | 0DC0 |
| ඔ         | 0D94 | ශ         | 0DC1 |
| ඕ         | 0D95 | ෂ         | 0DC2 |
| ඖ         | 0D96 | ස         | 0DC3 |
| ක         | 0D9A | හ         | 0DC4 |
| ඛ         | 0D9B | ළ         | 0DC5 |
| ග         | 0D9C | ෆ         | 0DC6 |
| ඝ         | 0D9D | ්         | 0DCA |
| ඞ         | 0D9E | ා         | 0DCF |
| ඟ         | 0D9F | ැ         | 0DD0 |
| ච         | 0DA0 | ෑ         | 0DD1 |
| ඡ         | 0DA1 | ි         | 0DD2 |
| ජ         | 0DA2 | ී         | 0DD3 |
| ඣ         | 0DA3 | ු         | 0DD4 |
| ඤ         | 0DA4 | ූ         | 0DD6 |
| ඥ         | 0DA5 | ෘ         | 0DD8 |
| ට         | 0DA7 | ෙ         | 0DD9 |
| ඨ         | 0DA8 | ේ         | 0DDA |
| ඩ         | 0DA9 | ෛ         | 0DDB |
| ඪ         | 0DAA | ො         | 0DDC |
| ණ         | 0DAB | ෝ         | 0DDD |
| ඬ         | 0DAC | ෞ         | 0DDE |
| ත         | 0DAD | ෟ         | 0DDF |
| ථ         | 0DAE | ෲ         | 0DF2 |

## Slovak character set

For Slovak custom vocabularies, you can use the following characters in the
`Phrase` field:

- a - z
- - (hyphen)
- . (period)

You can also use the following Unicode characters in the `Phrase` field:

| Character | Code | Character | Code |
| --------- | ---- | --------- | ---- |
| á         | 00E1 | ň         | 0148 |
| ä         | 00E4 | ó         | 00F3 |
| č         | 010D | ô         | 00F4 |
| ď         | 010F | ŕ         | 0155 |
| é         | 00E9 | š         | 0161 |
| í         | 00ED | ť         | 0165 |
| ĺ         | 013A | ú         | 00FA |
| ľ         | 013E | ý         | 00FD |
| ž         | 017E |

## Slovenian character set

For Slovenian custom vocabularies, you can use the following characters in the
`Phrase` field:

- a - z
- - (hyphen)
- . (period)

You can also use the following Unicode characters in the `Phrase` field:

| Character | Code | Character | Code |
| --------- | ---- | --------- | ---- |
| č         | 010D | š         | 0161 |
| ž         | 017E |

## Somali character set

For Somali custom vocabularies, you can use the following characters in the
`Phrase` field:

- a - z
- - (hyphen)
- . (period)

You can also use the following Unicode characters in the `Phrase` field:

| Character | Code | Character | Code |
| --------- | ---- | --------- | ---- |
| s         | 0073 | d         | 0064 |
| t         | 0074 | a         | 0061 |
| a         | 0061 | r         | 0072 |
| n         | 006E | d         | 0064 |

## Spanish character set

For Spanish custom vocabularies, you can use the following characters in the
`Phrase` field:

- a - z
- A - Z
- ' (apostrophe)
- - (hyphen)
- . (period)

You can also use the following Unicode characters in the `Phrase` field:

| Character | Code | Character | Code |
| --------- | ---- | --------- | ---- |
| Á         | 00C1 | á         | 00E1 |
| É         | 00C9 | é         | 00E9 |
| Í         | 00CD | í         | 00ED |
| Ó         | 00D3 | ó         | 0XF3 |
| Ú         | 00DA | ú         | 00FA |
| Ñ         | 00D1 | ñ         | 0XF1 |
| ü         | 00FC |           |      |

## Sundanese character set

For Sundanese custom vocabularies, you can use the following characters in the
`Phrase` field:

- a - z
- - (hyphen)
- . (period)

You can also use the following Unicode characters in the `Phrase` field:

| Character | Code | Character | Code |
| --------- | ---- | --------- | ---- |
| s         | 0073 | d         | 0064 |
| t         | 0074 | a         | 0061 |
| a         | 0061 | r         | 0072 |
| n         | 006E | d         | 0064 |

## Swahili character set

For Swahili custom vocabularies, you can use the following characters in the
`Phrase` field:

- a - z
- - (hyphen)
- . (period)

You can also use the following Unicode characters in the `Phrase` field:

| Character | Code | Character | Code |
| --------- | ---- | --------- | ---- |
| s         | 0073 | d         | 0064 |
| t         | 0074 | a         | 0061 |
| a         | 0061 | r         | 0072 |
| n         | 006E | d         | 0064 |

## Swedish character set

For Swedish custom vocabularies, you can use the following characters in the
`Phrase` field:

- a - z
- A - Z
- ' (apostrophe)
- - (hyphen)
- . (period)

You can also use the following Unicode characters in the `Phrase` field:

| Character | Code | Character | Code |
| --------- | ---- | --------- | ---- |
| Ä         | 00C4 | ä         | 00E4 |
| Å         | 00C5 | å         | 00E5 |
| Ö         | 00D6 | ö         | 00F6 |

## Tagalog/Filipino character set

For Tagalog/Filipino custom vocabularies, you can use the following characters in the
`Phrase` field:

- a - z
- - (hyphen)
- . (period)

You can also use the following Unicode characters in the `Phrase` field:

| Character | Code |
| --------- | ---- |
| ñ         | 00F1 |

## Tamil character set

For Tamil custom vocabularies, you can use the following characters in the
`Phrase` field:

| Character | Code | Character | Code |
| --------- | ---- | --------- | ---- |
| அ         | 0B85 | ர         | 0BB0 |
| ஆ         | 0B86 | ல         | 0BB2 |
| இ         | 0B87 | வ         | 0BB5 |
| ஈ         | 0B88 | ழ         | 0BB4 |
| உ         | 0B89 | ள         | 0BB3 |
| ஊ         | 0B8A | ற         | 0BB1 |
| எ         | 0B8E | ன         | 0BA9 |
| ஏ         | 0B8F | ஜ         | 0B9C |
| ஐ         | 0B90 | ஶ         | 0BB6 |
| ஒ         | 0B92 | ஷ         | 0BB7 |
| ஓ         | 0B93 | ஸ         | 0BB8 |
| ஔ         | 0B94 | ஹ         | 0BB9 |
| ஃ         | 0B83 | ்         | 0BCD |
| க         | 0B95 | ா         | 0BBE |
| ங         | 0B99 | ி         | 0BBF |
| ச         | 0B9A | ீ         | 0BC0 |
| ஞ         | 0B9E | ு         | 0BC1 |
| ட         | 0B9F | ூ         | 0BC2 |
| ண         | 0BA3 | ெ         | 0BC6 |
| த         | 0BA4 | ே         | 0BC7 |
| ந         | 0BA8 | ை         | 0BC8 |
| ப         | 0BAA | ொ         | 0BCA |
| ம         | 0BAE | ோ         | 0BCB |
| ய         | 0BAF | ௌ         | 0BCC |

## Tatar character set

For Tatar custom vocabularies, you can use the following characters in the
`Phrase` field:

- a - z
- - (hyphen)
- . (period)

You can also use the following Unicode characters in the `Phrase` field:

| Character | Code | Character | Code |
| --------- | ---- | --------- | ---- |
| а         | 0430 | љ         | 0459 |
| б         | 0431 | њ         | 045A |
| в         | 0432 | ћ         | 045B |
| г         | 0433 | ќ         | 045C |
| д         | 0434 | ѝ         | 045D |
| е         | 0435 | ў         | 045E |
| ж         | 0436 | џ         | 045F |
| з         | 0437 | ґ         | 0491 |
| и         | 0438 | ғ         | 0493 |
| й         | 0439 | җ         | 0497 |
| к         | 043A | ҙ         | 0499 |
| л         | 043B | қ         | 049B |
| м         | 043C | ҟ         | 049F |
| н         | 043D | ҡ         | 04A1 |
| о         | 043E | ң         | 04A3 |
| п         | 043F | ҥ         | 04A5 |
| р         | 0440 | ҩ         | 04A9 |
| с         | 0441 | ҫ         | 04AB |
| т         | 0442 | ҭ         | 04AD |
| у         | 0443 | ү         | 04AF |
| ф         | 0444 | ұ         | 04B1 |
| х         | 0445 | ҳ         | 04B3 |
| ц         | 0446 | ҵ         | 04B5 |
| ч         | 0447 | ҷ         | 04B7 |
| ш         | 0448 | һ         | 04BB |
| щ         | 0449 | ҽ         | 04BD |
| ъ         | 044A | ҿ         | 04BF |
| ы         | 044B | ӊ         | 04CA |
| ь         | 044C | ӑ         | 04D1 |
| э         | 044D | ӓ         | 04D3 |
| ю         | 044E | ӗ         | 04D7 |
| я         | 044F | ә         | 04D9 |
| ѐ         | 0450 | ӡ         | 04E1 |
| ё         | 0451 | ӣ         | 04E3 |
| ђ         | 0452 | ӧ         | 04E7 |
| ѓ         | 0453 | ө         | 04E9 |
| є         | 0454 | ӯ         | 04EF |
| ѕ         | 0455 | ӱ         | 04F1 |
| і         | 0456 | ӳ         | 04F3 |
| ї         | 0457 | ӷ         | 04F7 |
| ј         | 0458 | ӹ         | 04F9 |

## Telugu character set

For Telugu custom vocabularies, you can use the following characters in the
`Phrase` field:

| Character | Code | Character | Code |
| --------- | ---- | --------- | ---- |
| -         | 002D | త         | 0C24 |
| ఁ         | 0C01 | థ         | 0C25 |
| ం         | 0C02 | ద         | 0C26 |
| ః         | 0C03 | ధ         | 0C27 |
| అ         | 0C05 | న         | 0C28 |
| ఆ         | 0C06 | ప         | 0C2A |
| ఇ         | 0C07 | ఫ         | 0C2B |
| ఈ         | 0C08 | బ         | 0C2C |
| ఉ         | 0C09 | భ         | 0C2D |
| ఊ         | 0C0A | మ         | 0C2E |
| ఋ         | 0C0B | య         | 0C2F |
| ర         | 0C30 | ఎ         | 0C0E |
| ఱ         | 0C31 | ఏ         | 0C0F |
| ల         | 0C32 | ఐ         | 0C10 |
| ళ         | 0C33 | ఒ         | 0C12 |
| వ         | 0C35 | ఓ         | 0C13 |
| శ         | 0C36 | ఔ         | 0C14 |
| ష         | 0C37 | క         | 0C15 |
| స         | 0C38 | ఖ         | 0C16 |
| హ         | 0C39 | గ         | 0C17 |
| ా         | 0C3E | ఘ         | 0C18 |
| ి         | 0C3F | ఙ         | 0C19 |
| ీ         | 0C40 | చ         | 0C1A |
| ు         | 0C41 | ఛ         | 0C1B |
| ూ         | 0C42 | జ         | 0C1C |
| ృ         | 0C43 | ఝ         | 0C1D |
| ౄ         | 0C44 | ఞ         | 0C1E |
| ే         | 0C47 | ట         | 0C1F |
| ై         | 0C48 | ఠ         | 0C20 |
| ొ         | 0C4A | డ         | 0C21 |
| ో         | 0C4B | ఢ         | 0C22 |
| ౌ         | 0C4C | ణ         | 0C23 |
| ్         | 0C4D |

## Thai character set

For Thai custom vocabularies, you can use the following characters in the
`Phrase` field:

- - (hyphen)
- . (period)

You can also use the following Unicode characters in the `Phrase` field:

| Character | Code | Character | Code |
| --------- | ---- | --------- | ---- |
| ก         | 0E01 | ล         | 0E25 |
| ข         | 0E02 | ฦ         | 0E26 |
| ฃ         | 0E03 | ว         | 0E27 |
| ค         | 0E04 | ศ         | 0E28 |
| ฅ         | 0E05 | ษ         | 0E29 |
| ฆ         | 0E06 | ส         | 0E2A |
| ง         | 0E07 | ห         | 0E2B |
| จ         | 0E08 | ฬ         | 0E2C |
| ฉ         | 0E09 | อ         | 0E2D |
| ช         | 0E0A | ฮ         | 0E2E |
| ซ         | 0E0B | ฯ         | 0E2F |
| ฌ         | 0E0C | ะ         | 0E30 |
| ญ         | 0E0D | ั         | 0E31 |
| ฎ         | 0E0E | า         | 0E32 |
| ฏ         | 0E0F | ิ         | 0E34 |
| ฐ         | 0E10 | ี         | 0E35 |
| ฑ         | 0E11 | ึ         | 0E36 |
| ฒ         | 0E12 | ื         | 0E37 |
| ณ         | 0E13 | ุ         | 0E38 |
| ด         | 0E14 | ู         | 0E39 |
| ต         | 0E15 | ฺ         | 0E3A |
| ถ         | 0E16 | เ         | 0E40 |
| ท         | 0E17 | แ         | 0E41 |
| ธ         | 0E18 | โ         | 0E42 |
| น         | 0E19 | ใ         | 0E43 |
| บ         | 0E1A | ไ         | 0E44 |
| ป         | 0E1B | ๅ         | 0E45 |
| ผ         | 0E1C | ๆ         | 0E46 |
| ฝ         | 0E1D | ็         | 0E47 |
| พ         | 0E1E | ่         | 0E48 |
| ฟ         | 0E1F | ้         | 0E49 |
| ภ         | 0E20 | ๊         | 0E4A |
| ม         | 0E21 | ๋         | 0E4B |
| ย         | 0E22 | ์         | 0E4C |
| ร         | 0E23 | ํ         | 0E4D |
| ฤ         | 0E24 |

## Turkish character set

For Turkish custom vocabularies, you can use the following characters in the
`Phrase` field:

- a - z
- A - Z
- ' (apostrophe)
- - (hyphen)
- . (period)

You can also use the following Unicode characters in the `Phrase` field:

| Character | Code | Character | Code |
| --------- | ---- | --------- | ---- |
| Ç         | 00C7 | ö         | 00F6 |
| Ö         | 00D6 | û         | 00FB |
| Ü         | 00DC | ü         | 00FC |
| â         | 00E2 | Ğ         | 011E |
| ä         | 00E4 | ğ         | 011F |
| ç         | 00E7 | İ         | 0130 |
| è         | 00E8 | ı         | 0131 |
| é         | 00E9 | Ş         | 015E |
| ê         | 00EA | ş         | 015F |
| í         | 00ED | š         | 0161 |
| î         | 00EE | ž         | 017E |
| ó         | 00F3 |           |      |

## Ukrainian character set

For Ukrainian custom vocabularies, you can use the following characters in the
`Phrase` field:

- a - z
- - (hyphen)
- . (period)

You can also use the following Unicode characters in the `Phrase` field:

| Character | Code | Character | Code |
| --------- | ---- | --------- | ---- |
| а         | 0430 | р         | 0440 |
| б         | 0431 | с         | 0441 |
| в         | 0432 | т         | 0442 |
| г         | 0433 | у         | 0443 |
| д         | 0434 | ф         | 0444 |
| е         | 0435 | х         | 0445 |
| ж         | 0436 | ц         | 0446 |
| з         | 0437 | ч         | 0447 |
| и         | 0438 | ш         | 0448 |
| й         | 0439 | щ         | 0449 |
| к         | 043A | ь         | 044C |
| л         | 043B | ю         | 044E |
| м         | 043C | я         | 044F |
| н         | 043D | є         | 0454 |
| о         | 043E | і         | 0456 |
| п         | 043F | ї         | 0457 |
| ґ         | 0491 |

## Uyghur character set

For Uyghur custom vocabularies, you can use the following characters in the
`Phrase` field:

- a - z
- - (hyphen)
- . (period)

You can also use the following Unicode characters in the `Phrase` field:

| Character | Code | Character | Code |
| --------- | ---- | --------- | ---- |
| ؑ         | 0611 | و         | 0648 |
| ؓ         | 0613 | ى         | 0649 |
| ؔ         | 0614 | ي         | 064A |
| ء         | 0621 | ً         | 064B |
| آ         | 0622 | ٌ         | 064C |
| أ         | 0623 | ٍ         | 064D |
| ؤ         | 0624 | َ         | 064E |
| إ         | 0625 | ُ         | 064F |
| ئ         | 0626 | ِ         | 0650 |
| ا         | 0627 | ّ         | 0651 |
| ب         | 0628 | ْ         | 0652 |
| ة         | 0629 | ٓ         | 0653 |
| ت         | 062A | ٔ         | 0654 |
| ث         | 062B | ٗ         | 0657 |
| ج         | 062C | ٰ         | 0670 |
| ح         | 062D | ٹ         | 0679 |
| خ         | 062E | ٺ         | 067A |
| د         | 062F | ٻ         | 067B |
| ذ         | 0630 | ټ         | 067C |
| ر         | 0631 | ٽ         | 067D |
| ز         | 0632 | پ         | 067E |
| س         | 0633 | ٿ         | 067F |
| ش         | 0634 | ڀ         | 0680 |
| ص         | 0635 | ځ         | 0681 |
| ض         | 0636 | ڃ         | 0683 |
| ط         | 0637 | ڄ         | 0684 |
| ظ         | 0638 | څ         | 0685 |
| ع         | 0639 | چ         | 0686 |
| غ         | 063A | ڇ         | 0687 |
| ـ         | 0640 | ڈ         | 0688 |
| ف         | 0641 | ډ         | 0689 |
| ق         | 0642 | ڊ         | 068A |
| ك         | 0643 | ڌ         | 068C |
| ل         | 0644 | ڍ         | 068D |
| م         | 0645 | ڏ         | 068F |
| ن         | 0646 | ڑ         | 0691 |
| ه         | 0647 | ړ         | 0693 |
| ڕ         | 0695 |

## Uzbek character set

For Uzbek custom vocabularies, you can use the following characters in the
`Phrase` field:

- a - z
- - (hyphen)
- . (period)

You can also use the following Unicode characters in the `Phrase` field:

| Character | Code | Character | Code |
| --------- | ---- | --------- | ---- |
| т         | 0442 | я         | 044F |
| б         | 0431 | с         | 0441 |
| о         | 043E | ҳ         | 04B3 |
| п         | 043F | д         | 0434 |
| ш         | 0448 | р         | 0440 |
| и         | 0438 | ў         | 045E |
| ч         | 0447 | г         | 0433 |
| н         | 043D | ё         | 0451 |
| қ         | 049B | й         | 0439 |
| е         | 0435 | в         | 0432 |
| ю         | 044E | э         | 044D |
| з         | 0437 | л         | 043B |
| х         | 0445 | ф         | 0444 |
| ц         | 0446 | к         | 043A |
| м         | 043C | у         | 0443 |
| ь         | 044C | ж         | 0436 |
| ъ         | 044A | ғ         | 0493 |
| а         | 0430 |

## Vietnamese character set

Amazon Transcribe represents the six tones in Vietnamese using numbers. The following table
shows how tone marks are mapped for the word 'ma'.

| Tone name | Tone mark | Tone number |
| --------- | --------- | ----------- |
| ngang     | ma        | ma1         |
| sắc       | má        | ma2         |
| huyền     | mà        | ma3         |
| hỏi       | mả        | ma4         |
| ngã       | mã        | ma5         |
| nặng      | mạ        | ma6         |

For Vietnamese custom vocabularies, you can use the following characters in the
`Phrase` field:

- a - z
- A - Z
- ' (apostrophe)
- - (hyphen)
- . (period)
- & (ampersand)
- ; (semicolon)
- \_ (low line)

You can also use the following Unicode characters in the `Phrase` field:

| Character | Code | Character | Code |
| --------- | ---- | --------- | ---- |
| à         | 00E0 | À         | 00C0 |
| á         | 00E1 | Á         | 00C1 |
| â         | 00E2 | Â         | 00C2 |
| ã         | 00E3 | Ã         | 00C3 |
| è         | 00E8 | È         | 00C8 |
| é         | 00E9 | É         | 00C9 |
| ê         | 00EA | Ê         | 00CA |
| ì         | 00EC | Ì         | 00CC |
| í         | 00ED | Í         | 00CD |
| ò         | 00F2 | Ò         | 00D2 |
| ó         | 00F3 | Ó         | 00D3 |
| ô         | 00F4 | Ô         | 00D4 |
| õ         | 00F5 | Õ         | 00D5 |
| ù         | 00F9 | Ù         | 00D9 |
| ú         | 00FA | Ú         | 00DA |
| ý         | 00FD | Ý         | 00DD |
| ă         | 0103 | Ă         | 0102 |
| đ         | 0111 | Đ         | 0110 |
| ĩ         | 0129 | Ĩ         | 0128 |
| ũ         | 0169 | Ũ         | 0168 |
| ơ         | 01A1 | Ơ         | 01A0 |
| ư         | 01B0 | Ư         | 01AF |
| ạ         | 1EA1 | Ạ         | 1EA0 |
| ả         | 1EA3 | Ả         | 1EA2 |
| ấ         | 1EA5 | Ấ         | 1EA4 |
| ầ         | 1EA7 | Ầ         | 1EA6 |
| ẩ         | 1EA9 | Ẩ         | 1EA8 |
| ẫ         | 1EAB | Ẫ         | 1EAA |
| ậ         | 1EAD | Ậ         | 1EAC |
| ắ         | 1EAF | Ắ         | 1EAE |
| ằ         | 1EB1 | Ằ         | 1EB0 |
| ẳ         | 1EB3 | Ẳ         | 1EB2 |
| ẵ         | 1EB5 | Ẵ         | 1EB4 |
| ặ         | 1EB7 | Ặ         | 1EB6 |
| ẹ         | 1EB9 | Ẹ         | 1EB8 |
| ẻ         | 1EBB | Ẻ         | 1EBA |
| ẽ         | 1EBD | Ẽ         | 1EBC |
| ế         | 1EBF | Ế         | 1EBE |
| ề         | 1EC1 | Ề         | 1EC0 |
| ể         | 1EC3 | Ể         | 1EC2 |
| ễ         | 1EC5 | Ễ         | 1EC4 |
| ệ         | 1EC7 | Ệ         | 1EC6 |
| ỉ         | 1EC9 | Ỉ         | 1EC8 |
| ị         | 1ECB | Ị         | 1ECA |
| ọ         | 1ECD | Ọ         | 1ECC |
| ỏ         | 1ECF | Ỏ         | 1ECE |
| ố         | 1ED1 | Ố         | 1ED0 |
| ồ         | 1ED3 | Ồ         | 1ED2 |
| ổ         | 1ED5 | Ổ         | 1ED4 |
| ỗ         | 1ED7 | Ỗ         | 1ED6 |
| ộ         | 1ED9 | Ộ         | 1ED8 |
| ớ         | 1EDB | Ớ         | 1EDA |
| ờ         | 1EDD | Ờ         | 1EDC |
| ở         | 1EDF | Ở         | 1EDE |
| ỡ         | 1EE1 | Ỡ         | 1EE0 |
| ợ         | 1EE3 | Ợ         | 1EE2 |
| ụ         | 1EE5 | Ụ         | 1EE4 |
| ủ         | 1EE7 | Ủ         | 1EE6 |
| ứ         | 1EE9 | Ứ         | 1EE8 |
| ừ         | 1EEB | Ừ         | 1EEA |
| ử         | 1EED | Ử         | 1EEC |
| ữ         | 1EEF | Ữ         | 1EEE |
| ự         | 1EF1 | Ự         | 1EF0 |
| ỳ         | 1EF3 | Ỳ         | 1EF2 |
| ỵ         | 1EF5 | Ỵ         | 1EF4 |
| ỷ         | 1EF7 | Ỷ         | 1EF6 |
| ỹ         | 1EF9 | Ỹ         | 1EF8 |

## Welsh character set

For Welsh custom vocabularies, you can use the following characters in the
`Phrase` field:

- a - z
- - (hyphen)
- . (period)

You can also use the following Unicode characters in the `Phrase` field:

| Character | Code | Character | Code |
| --------- | ---- | --------- | ---- |
| à         | 00E0 | ò         | 00F2 |
| á         | 00E1 | ó         | 00F3 |
| â         | 00E2 | ô         | 00F4 |
| ä         | 00E4 | ö         | 00F6 |
| è         | 00E8 | ù         | 00F9 |
| é         | 00E9 | ú         | 00FA |
| ê         | 00EA | û         | 00FB |
| ë         | 00EB | ü         | 00FC |
| ì         | 00EC | ý         | 00FD |
| í         | 00ED | ÿ         | 00FF |
| î         | 00EE | ŵ         | 0175 |
| ï         | 00EF | ŷ         | 0177 |
| ỳ         | 1EF3 |

## Wolof character set

For Wolof custom vocabularies, you can use the following characters in the
`Phrase` field:

- a - z
- - (hyphen)
- . (period)

You can also use the following Unicode characters in the `Phrase` field:

| Character | Code | Character | Code |
| --------- | ---- | --------- | ---- |
| à         | 00E0 | ê         | 00EA |
| ã         | 00E3 | ë         | 00EB |
| ç         | 00E7 | ñ         | 00F1 |
| è         | 00E8 | ó         | 00F3 |
| é         | 00E9 | ô         | 00F4 |
| ŋ         | 014B |

## Zulu character set

For Zulu custom vocabularies, you can use the following characters in the
`Phrase` field:

- a - z
- - (hyphen)
- . (period)

You can also use the following Unicode characters in the `Phrase` field:

| Character | Code | Character | Code |
| --------- | ---- | --------- | ---- |
| s         | 0073 | d         | 0064 |
| t         | 0074 | a         | 0061 |
| a         | 0061 | r         | 0072 |
| n         | 006E | d         | 0064 |
