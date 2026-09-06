

# Chinese (Mandarin) (cmn-CN)
<a name="ph-table-mandarin"></a>

The following table lists the Pinyin and International Phonetic Alphabet (IPA) phonemes for the Mandarin Chinese voice that is supported by Amazon Polly. Pinyin is the international standard for Standard Chinese romanization. IPA and X-SAMPA are not commonly used but are available for English support. The IPA and X-SAMPA symbols in the table are for reference only and should not be used for Chinese transcription. Pinyin examples and the corresponding visemes are also shown.

To make Amazon Polly use phonetic pronunciation with Pinyin, use the `phoneme alphabet="x-amazon-{{phonetic standard used}}"` tag.

The following examples show this with each standard.

Pinyin:

```
<speak>
     你说 <phoneme alphabet="x-amazon-pinyin" ph="bo2">薄</phoneme>。 
     我说 <phoneme alphabet="x-amazon-pinyin" ph="bao2">薄</phoneme>。
</speak>
```

IPA:

```
<speak>
     你说 <phoneme alphabet="ipa" ph="pɪˈkɑːn">pecan</phoneme>。 
     我说 <phoneme alphabet="ipa" ph="ˈpi.kæn">pecan</phoneme>。
</speak>
```

X-SAMPA:

```
<speak>
     你说 <phoneme alphabet='x-sampa' ph='pI"kA:n'>pecan</phoneme>。 
     我说 <phoneme alphabet='x-sampa' ph='"pi.k{n'>pecan</phoneme>。
</speak>
```

**Note**  
Amazon Polly accepts Mandarin Chinese input encoded in UTF-8 only. The GB 18030 encoding standard is not currently supported by Amazon Polly. 


**Phoneme/Viseme Table**  

<table>
<thead>
  <tr><th>Pinyin</th><th>IPA</th><th>X-SAMPA</th><th>Description</th><th>Pinyin Example</th><th>Viseme</th></tr>
</thead>
<tbody>
  <tr><td colspan="6"><b>Consonants</b></td></tr>
  <tr><td>f</td><td>f </td><td>f</td><td>voiceless labiodental fricative </td><td>发, <b>f</b>a1</td><td>f </td></tr>
  <tr><td>h</td><td>h </td><td>h</td><td>voiceless glottal fricative </td><td>和, <b>h</b>e2</td><td>k </td></tr>
  <tr><td>g</td><td>k </td><td>k</td><td>voiceless velar plosive </td><td>古, <b>g</b>u3 </td><td>k </td></tr>
  <tr><td>k</td><td>kʰ </td><td>k_h</td><td>aspirated voiceless velar plosive </td><td>苦, <b>k</b>u3 </td><td>k </td></tr>
  <tr><td>l</td><td>l </td><td>l</td><td>alveolar lateral approximant </td><td>拉, <b>l</b>a1</td><td>t </td></tr>
  <tr><td>m</td><td>m </td><td>m</td><td>bilabial nasal </td><td>骂, <b>m</b>a4 </td><td>p </td></tr>
  <tr><td>n</td><td>n </td><td>n</td><td>alveolar nasal </td><td>那, <b>n</b>a4 </td><td>t </td></tr>
  <tr><td>ng</td><td>ŋ </td><td>N</td><td>velar nasal </td><td>正, zhe<b>ng</b>4 </td><td>k </td></tr>
  <tr><td>b</td><td>p </td><td>p</td><td>voiceless bilabial plosive </td><td>爸, <b>b</b>a4</td><td>p </td></tr>
  <tr><td>p</td><td>pʰ </td><td>p_h</td><td>aspirated voiceless bilabial plosive </td><td>怕, <b>p</b>a4 </td><td>p </td></tr>
  <tr><td>s</td><td>s </td><td>s</td><td>voiceless alveolar fricative </td><td>四, <b>s</b>i4 </td><td>s </td></tr>
  <tr><td>x</td><td>ɕ </td><td>s\</td><td>voiceless alveolo-palatal fricative </td><td>西, <b>x</b>i1 </td><td>J </td></tr>
  <tr><td>sh</td><td>ʂ </td><td>s`</td><td>voiceless retroflex fricative </td><td>是, <b>sh</b>i4 </td><td>S </td></tr>
  <tr><td>d</td><td>t </td><td>t</td><td>voiceless alveolar plosive </td><td>打, <b>d</b>a3 </td><td>t </td></tr>
  <tr><td>t</td><td>tʰ </td><td>t_h</td><td>aspirated voiceless alveolar plosive </td><td>他, <b>t</b>a1 </td><td>t </td></tr>
  <tr><td>zh</td><td>ʈ͡ʂ </td><td>t`s` </td><td>voiceless retroflex affricate </td><td>之, <b>zh</b>i1 </td><td>S</td></tr>
  <tr><td>ch</td><td>ʈ͡ʂʰ </td><td>t`s`_h</td><td>aspirated voiceless retroflex affricate </td><td>吃, <b>ch</b>i1 </td><td>S </td></tr>
  <tr><td>s</td><td>t͡s </td><td>ts</td><td>voiceless alveolar affricate </td><td>字, <b>z</b>i4 </td><td>s </td></tr>
  <tr><td>j</td><td>t͡ɕ </td><td>ts\</td><td>voiceless alveolo-palatal affricate </td><td>鸡, <b>j</b>i1 </td><td>J </td></tr>
  <tr><td>q</td><td>t͡ɕʰ </td><td>ts\_h</td><td>aspirated voiceless alveolo-palatal affricate </td><td>七, <b>q</b>i1 </td><td>J </td></tr>
  <tr><td>c</td><td>t͡sʰ </td><td>ts_h</td><td>aspirated voiceless alveolar affricate </td><td>次, <b>c</b>i4 </td><td>s </td></tr>
  <tr><td>w</td><td>w </td><td>w</td><td>labio-velar approximant </td><td>我, <b>w</b>o3 </td><td>u </td></tr>
  <tr><td>r</td><td>ʐ </td><td>z`</td><td>voiced retroflex fricative </td><td>日, <b>r</b>i4 </td><td>S </td></tr>
  <tr><td colspan="6"><b>"er" and "r" colored syllables</b></td></tr>
  <tr><td>er</td><td>ɚ </td><td>@` </td><td>r-coloured mid central vowel</td><td>二, <b>er</b>4 </td><td>@ </td></tr>
  <tr><td>-r</td><td> </td><td></td><td>r-colored syllable </td><td>馅儿, xian<b>r</b>4 </td><td>@ </td></tr>
  <tr><td colspan="6"><b>Vowels</b></td></tr>
  <tr><td>e</td><td>ɤ </td><td>7</td><td>close-mid back unrounded vowel </td><td>恶, <b>e</b>4</td><td>e </td></tr>
  <tr><td>e</td><td>ə </td><td>@</td><td>mid central vowel </td><td>恩, <b>e</b>n1</td><td>@ </td></tr>
  <tr><td>a</td><td>a </td><td>a</td><td>open front unrounded vowel </td><td>安, <b>a</b>n1</td><td>a </td></tr>
  <tr><td>ai</td><td>aɪ </td><td>aI </td><td>diphthong </td><td>爱, <b>ai</b>4</td><td>a </td></tr>
  <tr><td>ao</td><td>aʊ </td><td>aU</td><td>diphthong </td><td>奥, <b>ao</b>4</td><td>a </td></tr>
  <tr><td>ei</td><td>eɪ </td><td>e</td><td>diphthong </td><td>诶, <b>ei</b>4</td><td>e </td></tr>
  <tr><td>e</td><td>ɛ </td><td>E</td><td>open-mid front unrounded vowel </td><td>姐, ji<b>e</b>3</td><td>E </td></tr>
  <tr><td>i</td><td>i </td><td>i</td><td>close front unrounded vowel </td><td>鸡, j<b>i</b>1</td><td>i </td></tr>
  <tr><td>ou</td><td>oʊ </td><td>oU</td><td>diphthong </td><td>欧, <b>ou</b>1</td><td>o </td></tr>
  <tr><td>o</td><td>ɔ </td><td>O</td><td>open-mid back rounded vowel </td><td>哦, <b>o</b>4</td><td>o </td></tr>
  <tr><td>u</td><td>u </td><td>u</td><td>close back rounded vowel </td><td>主, zh<b>u</b>3</td><td>u </td></tr>
  <tr><td>yu</td><td>y </td><td>y</td><td>close front rounded vowel </td><td>于, <b>yu</b>2</td><td>u </td></tr>
  <tr><td colspan="6"><b>Tone marks and Additional Symbols</b></td></tr>
  <tr><td>1</td><td> </td><td></td><td>high level tone</td><td>淤, yu1 </td><td></td></tr>
  <tr><td>2</td><td> </td><td></td><td>rising tone</td><td>鱼, yu2 </td><td></td></tr>
  <tr><td>3</td><td> </td><td></td><td>low (falling-rising) tone</td><td>语, yu3 </td><td></td></tr>
  <tr><td>4</td><td> </td><td></td><td>falling tone</td><td>育, yu4 </td><td></td></tr>
  <tr><td>0</td><td> </td><td></td><td>neutral tone</td><td>的, de0 </td><td></td></tr>
  <tr><td>-</td><td>.</td><td>.</td><td>syllable boundary</td><td>语音 yu3-yin1</td><td> </td></tr>
</tbody>
</table>
