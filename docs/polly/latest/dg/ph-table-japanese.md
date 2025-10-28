# Japanese (ja-JP)

Amazon Polly supports the Pronunciation Kana and Yomigana alphabets for Japanese. To make
Amazon Polly use phonetic pronunciation with these alphabets, use the phoneme
`alphabet="x-amazon-`phonetic standard
used`"` attribute.

- `x-amazon-pron-kana` – indicates that Pronunciation Kana is
  used. Pronunciation Kana are special Katakana characters used for phonetic
  transcription and can encode pitch accent.
- `x-amazon-yomigana` – indicates that Yomigana is used.
  Yomigana can be conventional Katakana, Hiragana, and Latin alphabets interpreted
  as hepburn romanization.
  The following examples show how these are used:

Pronunciation Kana

```
<speak>
     名前は<phoneme alphabet="x-amazon-pron-kana" ph="ヒロカ'ズ">浩一</phoneme>です。
</speak>
```

Yomigana

```
<speak>
     名前は<phoneme alphabet="x-amazon-yomigana" ph="ひろかず">浩一</phoneme>です。
     名前は<phoneme alphabet="x-amazon-yomigana" ph="ヒロカズ">浩一</phoneme>です。
     名前は<phoneme alphabet="x-amazon-yomigana" ph="Hirokazu">浩一</phoneme>です。
</speak>
```

The following table lists the International Phonetic Alphabet (IPA) phonemes, the
Extended Speech Assessment Methods Phonetic Alphabet (X-SAMPA) symbols, and the
corresponding visemes for the Japanese voice supported by Amazon Polly.

| IPA            | X-SAMPA | Description                                | Example                    | Viseme |
| -------------- | ------- | ------------------------------------------ | -------------------------- | ------ |
| **Consonants** |
| ɾ              | 4       | alveolar flap                              | 練習, **r**enshuu          | t      |
| ʔ              | ?       | glottal stop                               | あつっ, atsu**'**          |        |
| b              | b       | voiced bilabial plosive                    | 舞踊, **b**uyou            | p      |
| β              | B       | voiced bilabial fricative                  | ヴィンテージ, **v**inteeji | B      |
| c              | c       | voiceless palatal plosive                  | ききょう, **k**i**ky**ou   | k      |
| ç              | C       | voiceless palatal fricative                | 人, **h**ito               | k      |
| d              | d       | voiced alveolar plosive                    | 濁点, **d**akuten          | t      |
| d͡ʑ             | dz\     | voiced alveolo-palatal affricate           | 純, **j**un                | J      |
| ɡ              | g       | voiced velar plosive                       | ご飯, **g**ohan            | k      |
| h              | h       | voiceless glottal fricative                | 本, **h**on                | k      |
| j              | j       | palatal approximant                        | 屋根, **y**ane             | i      |
| ɟ              | J\      | voiced palatal plosive                     | 行儀, **gy**ou**g**i       | J      |
| k              | k       | voiceless velar plosive                    | 漢字, **k**anji            | k      |
| ɺ              | l\      | alveolar lateral flap                      | 釣り, tsu**r**i            | r      |
| ɺj             | l\j     | alveolar lateral flap, palatal approximant | 流行, **ry**uukou          | r      |
| m              | m       | bilabial nasal                             | 飯, **m**eshi              | p      |
| n              | n       | alveolar nasal                             | 猫, **n**eko               | t      |
| ɲ              | J       | palatal nasal                              | 日本, **n**ippon           | J      |
| ɴ              | N\      | uvular nasal                               | 缶, ka**n**                | k      |
| p              | p       | voiceless bilabial plosive                 | パン, **p**an              | p      |
| ɸ              | p\      | voiceless bilabial fricative               | 福, **h**uku               | f      |
| s              | s       | voiceless alveolar fricative               | 層, **s**ou                | s      |
| ɕ              | s\      | voiceless alveolo-palatal fricative        | 書簡, **sh**okan           | J      |
| t              | t       | voiceless alveolar plosive                 | 手紙, **t**egami           | t      |
| t͡s             | ts      | voiceless alveolar affricate               | 釣り, **ts**uri            | s      |
| t͡ɕ             | ts\     | voiceless alveolo-palatal affricate        | 吉, ki**ch**i              | J      |
| w              | w       | labial-velar approximant                   | 電話, den**w**a            | u      |
| z              | z       | voiced alveolar fricative                  | 座敷, **z**ashiki          | s      |
| **Vowels**     |
| äː             | a:\_"   | long open central unrounded vowel          | 羽蟻, h**aa**ri            | a      |
| ä              | a\_"    | open central unrounded vowel               | 仮名, k**a**n**a**         | a      |
| eː             | e:\_o   | long mid front unrounded vowel             | 学生, gakus**ei**          | @      |
| e              | e_o     | mid front unrounded vowel                  | 歴, r**e**ki               | @      |
| i              | i       | close front unrounded vowel                | 気, k**i**                 | i      |
| iː             | i:      | long close front unrounded vowel           | 詩歌, sh**ii**ka           | i      |
| ɯ              | M       | close back unrounded vowel                 | 運, **u**n                 | i      |
| ɯː             | M:      | long close back unrounded vowel            | 宗教, sh**uu**kyou         | i      |
| oː             | o:\_o   | long mid back rounded vowel                | 購読, k**oo**doku          | o      |
| o              | o_o     | mid back rounded vowel                     | 読者, d**o**kusha          | o      |
