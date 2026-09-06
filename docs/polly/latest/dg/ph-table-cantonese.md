

# Chinese (Cantonese) (yue-CN)
<a name="ph-table-cantonese"></a>

The following table lists the Jyutping and International Phonetic Alphabet (IPA) phonemes for the Cantonese voice that is supported by Amazon Polly. Jyutping is a romanization system of Cantonese which is commonly used in academia and among Cantonese speakers. IPA and X-SAMPA are not commonly used but are available for English support. The IPA and X-SAMPA symbols in the table are for reference only and should not be used for Chinese transcription. Jyutping examples and the corresponding visemes are also shown. 

To make Amazon Polly use phonetic pronunciation with Jyutping, use the `phoneme alphabet="x-amazon-{{jyutping}}"`tag.

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

**Note**  
Amazon Polly accepts Cantonese input encoded in UTF-8 only. 


**Phoneme/Viseme Table**  

<table>
<thead>
  <tr><th>Jyutping</th><th>IPA</th><th>X-SAMPA</th><th>Description</th><th>Jyutping Example</th><th>Viseme</th></tr>
</thead>
<tbody>
  <tr><td colspan="6"><b>Consonants</b></td></tr>
  <tr><td>b</td><td>p </td><td>p</td><td>voiceless bilabial plosive </td><td>巴, <b>b</b>aa1</td><td>p </td></tr>
  <tr><td>c</td><td>tsʰ</td><td>ts_h</td><td>aspirated voiceless alveolar affricate </td><td>叉, <b>c</b>aa1</td><td>s</td></tr>
  <tr><td>d</td><td>t </td><td>t</td><td>voiceless alveolar plosive </td><td>打, <b>d</b>aa2 </td><td>t </td></tr>
  <tr><td>f</td><td>f</td><td>f</td><td>voiceless labiodental fricative</td><td>花, <b>f</b>aa1 </td><td>f </td></tr>
  <tr><td>g</td><td>k </td><td>k</td><td>voiceless velar plosive</td><td>家, <b>g</b>aa1</td><td>k </td></tr>
  <tr><td>gw</td><td>kʷ </td><td>k_w</td><td>labialized voiceless velar plosive</td><td>瓜, <b>gw</b>aa1 </td><td>u </td></tr>
  <tr><td>h</td><td>h </td><td>h</td><td>voiceless glottal fricative </td><td>哈, <b>h</b>aa1 </td><td>k </td></tr>
  <tr><td>k</td><td>kʰ </td><td>k_h</td><td>aspirated voiceless velar plosive</td><td>卡, <b>k</b>aa1 </td><td>k </td></tr>
  <tr><td>kw</td><td>kʷʰ</td><td>k_wh</td><td>labialized aspirated voiceless velar plosive</td><td>誇, <b>kw</b>aa1</td><td>u </td></tr>
  <tr><td>l</td><td>l</td><td>l</td><td>alveolar lateral approximant</td><td>啦, <b>l</b>aa1 </td><td>t </td></tr>
  <tr><td>m</td><td>m </td><td>m</td><td>bilabial nasal </td><td>媽, <b>m</b>aa1 </td><td>p </td></tr>
  <tr><td>m</td><td>m </td><td>m=</td><td>syllabic bilabial nasal</td><td>唔, <b>m</b>4 </td><td>p </td></tr>
  <tr><td>ng</td><td>ŋ</td><td>N</td><td>velar nasal </td><td>牙, <b>ng</b>aa4 </td><td>k </td></tr>
  <tr><td>ng</td><td>ŋ</td><td>N=</td><td>syllabic velar nasal</td><td>吳, <b>ng</b>4 </td><td>k </td></tr>
  <tr><td>n</td><td>n </td><td>n</td><td>alveolar nasal</td><td>拿, <b>n</b>aa4 </td><td>t </td></tr>
  <tr><td>p</td><td>pʰ</td><td>p_h</td><td>aspirated voiceless bilabial plosive</td><td>趴, <b>p</b>aa1 </td><td>p</td></tr>
  <tr><td>s</td><td>s</td><td>s</td><td>voiceless alveolar fricative </td><td>沙, <b>s</b>aa1 </td><td>s </td></tr>
  <tr><td>t</td><td>tʰ</td><td>t_h</td><td>aspirated voiceless alveolar plosive</td><td>他, <b>t</b>aa1 </td><td>t </td></tr>
  <tr><td>w</td><td>w</td><td>w</td><td>labio-velar approximant</td><td>娃, <b>w</b>aa1 </td><td>u </td></tr>
  <tr><td>y</td><td>j</td><td>j</td><td>palatal approximant </td><td>也, <b>j</b>aa5 </td><td>i </td></tr>
  <tr><td>z</td><td>ts</td><td>ts</td><td>voiceless alveolar affricate</td><td>渣, <b>z</b>aa1 </td><td>s </td></tr>
  <tr><td colspan="6"><b>Vowels</b></td></tr>
  <tr><td>a</td><td>ɐ </td><td>6</td><td>near-open central vowel</td><td>吉, g<b>a</b>t1 </td><td>a </td></tr>
  <tr><td>aa</td><td>ɑ</td><td>A</td><td>open back unrounded vowel</td><td>家, g<b>aa</b>1 </td><td>a</td></tr>
  <tr><td>aai</td><td>ɑi</td><td>Ai</td><td>dipthong</td><td>街, g<b>aai</b>1 </td><td>a </td></tr>
  <tr><td>aau</td><td>ɑu</td><td>Au</td><td>dipthong</td><td>交, g<b>aau</b>1 </td><td>a </td></tr>
  <tr><td>ai</td><td>ɐi</td><td>6i</td><td>dipthong</td><td>雞, g<b>ai</b>1</td><td>a </td></tr>
  <tr><td>au</td><td>ɐu</td><td>6u</td><td>dipthong</td><td>溝, k<b>au</b>1</td><td>a </td></tr>
  <tr><td>e</td><td>ɛ</td><td>E</td><td>open-mid front unrounded vowel</td><td>爹, d<b>e</b>1</td><td>E</td></tr>
  <tr><td>ei</td><td>ei</td><td>ei</td><td>dipthong</td><td>基, g<b>ei</b>1</td><td>e</td></tr>
  <tr><td>eo</td><td>ɵ</td><td>8</td><td>close-mid central rounded vowel </td><td>春, c<b>eo</b>n1</td><td>o</td></tr>
  <tr><td>eoi</td><td>ɵy</td><td>8y</td><td>diphthong </td><td>居, g<b>eoi</b>1</td><td>o</td></tr>
  <tr><td>eu</td><td>ɛu</td><td>Eu</td><td>diphthong </td><td>掉 in 掉垃圾, d<b>eu</b>6</td><td>E</td></tr>
  <tr><td>i</td><td>i </td><td>i</td><td>close front unrounded vowel</td><td>斯, <b>si</b>1</td><td>i </td></tr>
  <tr><td>i</td><td>I</td><td>l</td><td>near-close near-front unrounded vowel</td><td>激, gik<b></b>1</td><td>i </td></tr>
  <tr><td>iu</td><td>iu </td><td>iu</td><td>diphthong </td><td>驕, g<b>iu</b>1</td><td>i</td></tr>
  <tr><td>o</td><td>ɔ</td><td>O</td><td>open-mid back rounded vowel </td><td>哥, g<b>o</b>1</td><td>O </td></tr>
  <tr><td>oe</td><td>œ</td><td>9</td><td>open-mid front rounded vowel</td><td>鋸, g<b>oe</b>3</td><td>O</td></tr>
  <tr><td>oi</td><td>ɔi</td><td>Oi</td><td>dipthong</td><td>該, g<b>oi</b>1</td><td>O</td></tr>
  <tr><td>ou</td><td>ou</td><td>ou</td><td>dipthong</td><td>高, g<b>ou</b>1</td><td>o</td></tr>
  <tr><td>u</td><td>u</td><td>u</td><td>close back rounded vowel</td><td>姑, g<b>u</b>1</td><td>u</td></tr>
  <tr><td>u</td><td>ʊ</td><td>U</td><td>near-close near-back rounded vowel</td><td>谷, g<b>u</b>k5</td><td>u</td></tr>
  <tr><td>ui</td><td>ui</td><td>ui</td><td>dipthong</td><td>攰, g<b>ui</b>6</td><td>u</td></tr>
  <tr><td>yu</td><td>y</td><td>y</td><td>close front rounded vowel</td><td>於, j<b>yu</b>1</td><td>u</td></tr>
  <tr><td colspan="6"><b>Tone marks and Additional Symbols</b></td></tr>
  <tr><td>1</td><td> </td><td></td><td>high level</td><td>詩, si<b>1</b> </td><td></td></tr>
  <tr><td>2</td><td> </td><td></td><td>medium rising</td><td>史, si<b>2</b></td><td></td></tr>
  <tr><td>3</td><td> </td><td></td><td>medium level</td><td>試, si<b>3</b></td><td></td></tr>
  <tr><td>4</td><td> </td><td></td><td>very low level</td><td>時, si<b>4</b></td><td></td></tr>
  <tr><td>5</td><td> </td><td></td><td>low rising</td><td>市, si<b>5</b></td><td></td></tr>
  <tr><td>6</td><td> </td><td></td><td>low level</td><td>是, si<b>6</b></td><td></td></tr>
  <tr><td>-</td><td>.</td><td>.</td><td>syllable boundary</td><td>語音 jyu5-jam1</td><td> </td></tr>
</tbody>
</table>
