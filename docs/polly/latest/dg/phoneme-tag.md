# Using phonetic pronunciation

_<phoneme>_

This tag is supported by long-form, neural, and standard TTS formats.

To make Amazon Polly use phonetic pronunciation for specific text,
use the <phoneme> tag.

Two attributes are required with the `<phoneme>`
tag. They indicate the phonetic alphabet Amazon Polly uses and
the phonetic symbols of the corrected pronunciation:

- `alphabet`
  - `ipa`— Indicates that the
    International Phonetic Alphabet (IPA) will be
    used.
  - `x-sampa`— Indicates that the
    Extended Speech Assessment Methods Phonetic
    Alphabet (X-SAMPA) will be used.

- `ph`

      + Specifies the phonetic symbols for
       pronunciation. For more information, see [Languages in Amazon Polly](supported-languages.md "supported-languages.md")

  With the `<phoneme>` tag, Amazon Polly uses the
  pronunciation specified by the `ph` attribute instead
  of the standard pronunciation associated by default with the
  language used by the selected voice.

For instance, the word "pecan" can be pronounced two ways. In
the following example, “pecan” is assigned a different
pronunciation in each line. Amazon Polly pronounces pecan as specified
in the `ph` attributes, instead of using the default
pronunciation.

International Phonetic Alphabet (IPA)

```
<speak>
     You say, <phoneme alphabet="ipa" ph="pɪˈkɑːn">pecan</phoneme>.
     I say, <phoneme alphabet="ipa" ph="ˈpi.kæn">pecan</phoneme>.
</speak>
```

Extended Speech Assessment Methods Phonetic Alphabet
(X-SAMPA)

```
<speak>
     You say, <phoneme alphabet='x-sampa' ph='pI"kA:n'>pecan</phoneme>.
     I say, <phoneme alphabet='x-sampa' ph='"pi.k{n'>pecan</phoneme>.
</speak>
```

Mandarin Chinese uses Pinyin for phonetic
pronunciation..

Pinyin

```
<speak>
     你说 <phoneme alphabet="x-amazon-pinyin" ph="bo2">薄</phoneme>。
     我说 <phoneme alphabet="x-amazon-pinyin" ph="bao2">薄</phoneme>。
</speak>
```

Japanese uses Yomigana and Pronunciation Kana.

Yomigana

```
<speak>
     名前は<phoneme alphabet="x-amazon-yomigana" ph="ひろかず">浩一</phoneme>です。
     名前は<phoneme alphabet="x-amazon-yomigana" ph="ヒロカズ">浩一</phoneme>です。
     名前は<phoneme alphabet="x-amazon-yomigana" ph="Hirokazu">浩一</phoneme>です。
</speak>
```

Pronunciation Kana

```
<speak>
     名前は<phoneme alphabet="x-amazon-pron-kana" ph="ヒロ'カズ">浩一</phoneme>です。
</speak>
```
