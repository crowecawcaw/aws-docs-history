

# Japanese (ja-JP)
<a name="ph-table-japanese"></a>

Amazon Polly supports the Pronunciation Kana and Yomigana alphabets for Japanese. To make Amazon Polly use phonetic pronunciation with these alphabets, use the phoneme `alphabet="x-amazon-{{phonetic standard used}}"` attribute.
+ `x-amazon-pron-kana` – indicates that Pronunciation Kana is used. Pronunciation Kana are special Katakana characters used for phonetic transcription and can encode pitch accent.
+ `x-amazon-yomigana` – indicates that Yomigana is used. Yomigana can be conventional Katakana, Hiragana, and Latin alphabets interpreted as hepburn romanization. 

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

The following table lists the International Phonetic Alphabet (IPA) phonemes, the Extended Speech Assessment Methods Phonetic Alphabet (X-SAMPA) symbols, and the corresponding visemes for the Japanese voice supported by Amazon Polly.


<table>
<thead>
  <tr><th>IPA</th><th>X-SAMPA</th><th>Description</th><th>Example</th><th>Viseme</th></tr>
</thead>
<tbody>
  <tr><td colspan="5"><b>Consonants</b></td></tr>
  <tr><td>ɾ</td><td>4</td><td>alveolar flap</td><td>練習, <b>r</b>enshuu</td><td>t</td></tr>
  <tr><td>ʔ</td><td>?</td><td>glottal stop</td><td>あつっ, atsu<b>'</b></td><td></td></tr>
  <tr><td>b</td><td>b</td><td>voiced bilabial plosive</td><td>舞踊, <b>b</b>uyou</td><td>p</td></tr>
  <tr><td>β</td><td>B</td><td>voiced bilabial fricative</td><td>ヴィンテージ, <b>v</b>inteeji</td><td>B</td></tr>
  <tr><td>c</td><td>c</td><td>voiceless palatal plosive</td><td>ききょう, <b>k</b>i<b>ky</b>ou</td><td>k</td></tr>
  <tr><td>ç</td><td>C</td><td>voiceless palatal fricative</td><td>人, <b>h</b>ito</td><td>k</td></tr>
  <tr><td>d</td><td>d</td><td>voiced alveolar plosive</td><td>濁点, <b>d</b>akuten</td><td>t</td></tr>
  <tr><td>d͡ʑ</td><td>dz\</td><td>voiced alveolo-palatal affricate</td><td>純, <b>j</b>un</td><td>J</td></tr>
  <tr><td>ɡ</td><td>g</td><td>voiced velar plosive</td><td>ご飯, <b>g</b>ohan</td><td>k</td></tr>
  <tr><td>h</td><td>h</td><td>voiceless glottal fricative</td><td>本, <b>h</b>on</td><td>k</td></tr>
  <tr><td>j</td><td>j</td><td>palatal approximant</td><td>屋根, <b>y</b>ane</td><td>i</td></tr>
  <tr><td>ɟ</td><td>J\</td><td>voiced palatal plosive</td><td>行儀, <b>gy</b>ou<b>g</b>i</td><td>J</td></tr>
  <tr><td>k</td><td>k</td><td>voiceless velar plosive</td><td>漢字, <b>k</b>anji</td><td>k</td></tr>
  <tr><td>ɺ</td><td>l\</td><td>alveolar lateral flap</td><td>釣り, tsu<b>r</b>i</td><td>r</td></tr>
  <tr><td>ɺj</td><td>l\j</td><td>alveolar lateral flap, palatal approximant</td><td>流行, <b>ry</b>uukou</td><td>r</td></tr>
  <tr><td>m</td><td>m</td><td>bilabial nasal</td><td>飯, <b>m</b>eshi</td><td>p</td></tr>
  <tr><td>n</td><td>n</td><td>alveolar nasal</td><td>猫, <b>n</b>eko</td><td>t</td></tr>
  <tr><td>ɲ</td><td>J</td><td>palatal nasal</td><td>日本, <b>n</b>ippon</td><td>J</td></tr>
  <tr><td>ɴ</td><td>N\</td><td>uvular nasal</td><td>缶, ka<b>n</b></td><td>k</td></tr>
  <tr><td>p</td><td>p</td><td>voiceless bilabial plosive</td><td>パン, <b>p</b>an</td><td>p</td></tr>
  <tr><td>ɸ</td><td>p\</td><td>voiceless bilabial fricative</td><td>福, <b>h</b>uku</td><td>f</td></tr>
  <tr><td>s</td><td>s</td><td>voiceless alveolar fricative</td><td>層, <b>s</b>ou</td><td>s</td></tr>
  <tr><td>ɕ</td><td>s\</td><td>voiceless alveolo-palatal fricative</td><td>書簡, <b>sh</b>okan</td><td>J</td></tr>
  <tr><td>t</td><td>t</td><td>voiceless alveolar plosive</td><td>手紙, <b>t</b>egami</td><td>t</td></tr>
  <tr><td>t͡s</td><td>ts</td><td>voiceless alveolar affricate</td><td>釣り, <b>ts</b>uri</td><td>s</td></tr>
  <tr><td>t͡ɕ</td><td>ts\</td><td>voiceless alveolo-palatal affricate</td><td>吉, ki<b>ch</b>i</td><td>J</td></tr>
  <tr><td>w</td><td>w</td><td>labial-velar approximant</td><td>電話, den<b>w</b>a</td><td>u</td></tr>
  <tr><td>z</td><td>z</td><td>voiced alveolar fricative</td><td>座敷, <b>z</b>ashiki</td><td>s</td></tr>
  <tr><td colspan="5"><b>Vowels</b></td></tr>
  <tr><td>äː</td><td>a:_"</td><td>long open central unrounded vowel</td><td>羽蟻, h<b>aa</b>ri</td><td>a</td></tr>
  <tr><td>ä</td><td>a_"</td><td>open central unrounded vowel</td><td>仮名, k<b>a</b>n<b>a</b></td><td>a</td></tr>
  <tr><td>eː</td><td>e:_o</td><td>long mid front unrounded vowel</td><td>学生, gakus<b>ei</b></td><td>@</td></tr>
  <tr><td>e</td><td>e_o</td><td>mid front unrounded vowel</td><td>歴, r<b>e</b>ki</td><td>@</td></tr>
  <tr><td>i</td><td>i</td><td>close front unrounded vowel</td><td>気, k<b>i</b></td><td>i</td></tr>
  <tr><td>iː</td><td>i:</td><td>long close front unrounded vowel</td><td>詩歌, sh<b>ii</b>ka</td><td>i</td></tr>
  <tr><td>ɯ</td><td>M</td><td>close back unrounded vowel</td><td>運, <b>u</b>n</td><td>i</td></tr>
  <tr><td>ɯː</td><td>M:</td><td>long close back unrounded vowel</td><td>宗教, sh<b>uu</b>kyou</td><td>i</td></tr>
  <tr><td>oː</td><td>o:_o</td><td>long mid back rounded vowel</td><td>購読, k<b>oo</b>doku</td><td>o</td></tr>
  <tr><td>o</td><td>o_o</td><td>mid back rounded vowel</td><td>読者, d<b>o</b>kusha</td><td>o</td></tr>
</tbody>
</table>
