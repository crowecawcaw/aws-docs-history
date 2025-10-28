# Chinese (Cantonese) (yue-CN)

The following table lists the Jyutping and International Phonetic Alphabet (IPA)
phonemes for the Cantonese voice that is supported by Amazon Polly. Jyutping is a romanization
system of Cantonese which is commonly used in academia and among Cantonese speakers. IPA
and X-SAMPA are not commonly used but are available for English support. The IPA and
X-SAMPA symbols in the table are for reference only and should not be used for Chinese
transcription. Jyutping examples and the corresponding visemes are also shown.

To make Amazon Polly use phonetic pronunciation with Jyutping, use the `phoneme
 alphabet="x-amazon-`jyutping`"`tag.

The following examples show this with each standard.

Jyutping:

```
<speak>
     你講 <phoneme alphabet="x-amazon-jyutping" ph="sing2">醒</phoneme>。
     我講 <phoneme alphabet="x-amazon-jyutping" ph="seng2">醒</phoneme>。
</speak>
```

IPA:

```
<speak>
     你講 <phoneme alphabet="ipa" ph="pɪˈkɑːn">pecan</phoneme>。
     我講 <phoneme alphabet="ipa" ph="ˈpi.kæn">pecan</phoneme>。
</speak>
```

X-SAMPA:

```
<speak>
     你講 <phoneme alphabet='x-sampa' ph='pI"kA:n'>pecan</phoneme>。
     我講 <phoneme alphabet='x-sampa' ph='"pi.k{n'>pecan</phoneme>。
</speak>
```

###### Note

Amazon Polly accepts Cantonese input encoded in UTF-8 only.

| Phoneme/Viseme Table                  | Jyutping | IPA  | X-SAMPA                                      | Description            | Jyutping Example | Viseme      |
| ------------------------------------- | -------- | ---- | -------------------------------------------- | ---------------------- | ---------------- | ----------- |
| **Consonants**                        |
| b                                     | p        | p    | voiceless bilabial plosive                   | 巴, **b**aa1           | p                |
| c                                     | tsʰ      | ts_h | aspirated voiceless alveolar affricate       | 叉, **c**aa1           | s                |
| d                                     | t        | t    | voiceless alveolar plosive                   | 打, **d**aa2           | t                |
| f                                     | f        | f    | voiceless labiodental fricative              | 花, **f**aa1           | f                |
| g                                     | k        | k    | voiceless velar plosive                      | 家, **g**aa1           | k                |
| gw                                    | kʷ       | k_w  | labialized voiceless velar plosive           | 瓜, **gw**aa1          | u                |
| h                                     | h        | h    | voiceless glottal fricative                  | 哈, **h**aa1           | k                |
| k                                     | kʰ       | k_h  | aspirated voiceless velar plosive            | 卡, **k**aa1           | k                |
| kw                                    | kʷʰ      | k_wh | labialized aspirated voiceless velar plosive | 誇, **kw**aa1          | u                |
| l                                     | l        | l    | alveolar lateral approximant                 | 啦, **l**aa1           | t                |
| m                                     | m        | m    | bilabial nasal                               | 媽, **m**aa1           | p                |
| m                                     | m        | m=   | syllabic bilabial nasal                      | 唔, **m**4             | p                |
| ng                                    | ŋ        | N    | velar nasal                                  | 牙, **ng**aa4          | k                |
| ng                                    | ŋ        | N=   | syllabic velar nasal                         | 吳, **ng**4            | k                |
| n                                     | n        | n    | alveolar nasal                               | 拿, **n**aa4           | t                |
| p                                     | pʰ       | p_h  | aspirated voiceless bilabial plosive         | 趴, **p**aa1           | p                |
| s                                     | s        | s    | voiceless alveolar fricative                 | 沙, **s**aa1           | s                |
| t                                     | tʰ       | t_h  | aspirated voiceless alveolar plosive         | 他, **t**aa1           | t                |
| w                                     | w        | w    | labio-velar approximant                      | 娃, **w**aa1           | u                |
| y                                     | j        | j    | palatal approximant                          | 也, **j**aa5           | i                |
| z                                     | ts       | ts   | voiceless alveolar affricate                 | 渣, **z**aa1           | s                |
| **Vowels**                            |
| a                                     | ɐ        | 6    | near-open central vowel                      | 吉, g**a**t1           | a                |
| aa                                    | ɑ        | A    | open back unrounded vowel                    | 家, g**aa**1           | a                |
| aai                                   | ɑi       | Ai   | dipthong                                     | 街, g**aai**1          | a                |
| aau                                   | ɑu       | Au   | dipthong                                     | 交, g**aau**1          | a                |
| ai                                    | ɐi       | 6i   | dipthong                                     | 雞, g**ai**1           | a                |
| au                                    | ɐu       | 6u   | dipthong                                     | 溝, k**au**1           | a                |
| e                                     | ɛ        | E    | open-mid front unrounded vowel               | 爹, d**e**1            | E                |
| ei                                    | ei       | ei   | dipthong                                     | 基, g**ei**1           | e                |
| eo                                    | ɵ        | 8    | close-mid central rounded vowel              | 春, c**eo**n1          | o                |
| eoi                                   | ɵy       | 8y   | diphthong                                    | 居, g**eoi**1          | o                |
| eu                                    | ɛu       | Eu   | diphthong                                    | 掉 in 掉垃圾, d**eu**6 | E                |
| i                                     | i        | i    | close front unrounded vowel                  | 斯, **si**1            | i                |
| i                                     | I        | l    | near-close near-front unrounded vowel        | 激, gik1               | i                |
| iu                                    | iu       | iu   | diphthong                                    | 驕, g**iu**1           | i                |
| o                                     | ɔ        | O    | open-mid back rounded vowel                  | 哥, g**o**1            | O                |
| oe                                    | œ        | 9    | open-mid front rounded vowel                 | 鋸, g**oe**3           | O                |
| oi                                    | ɔi       | Oi   | dipthong                                     | 該, g**oi**1           | O                |
| ou                                    | ou       | ou   | dipthong                                     | 高, g**ou**1           | o                |
| u                                     | u        | u    | close back rounded vowel                     | 姑, g**u**1            | u                |
| u                                     | ʊ        | U    | near-close near-back rounded vowel           | 谷, g**u**k5           | u                |
| ui                                    | ui       | ui   | dipthong                                     | 攰, g**ui**6           | u                |
| yu                                    | y        | y    | close front rounded vowel                    | 於, j**yu**1           | u                |
| **Tone marks and Additional Symbols** |          | 1    |                                              |                        | high level       | 詩, si**1** |
|                                       |
| 2                                     |          |      | medium rising                                | 史, si**2**            |                  |
| 3                                     |          |      | medium level                                 | 試, si**3**            |                  |
| 4                                     |          |      | very low level                               | 時, si**4**            |                  |
| 5                                     |          |      | low rising                                   | 市, si**5**            |                  |
| 6                                     |          |      | low level                                    | 是, si**6**            |                  |
| -                                     | .        | .    | syllable boundary                            | 語音 jyu5-jam1         |                  |
