# Controlling how special types of

words are spoken

_<say-as>_

The `<say-as>`
tag is supported by generative, long-form, neural, and standard TTS engines. Note, however, that
if Amazon Polly is using a neural voice and encounters the `<say-as>`
tag with the `characters` option at runtime, the affected sentence
will be synthesized using the related standard voice. However, the affected
sentence will still be billed as if it uses a neural voice.

Use the `<say-as>` tag with the
`interpret-as` attribute to tell Amazon Polly how to say
certain characters, words, and numbers. This enables you to
provide additional context to eliminate any ambiguity on how
Amazon Polly should render the text.

The `<say-as>` tag uses one attribute,
`interpret-as`, which uses a number of possible available
values. Each uses the same syntax:

```
<say-as interpret-as="`value`">[`text to be interpreted`]</say-as>
```

The following values are available with
`interpret-as`:

- `characters` or `spell-out`:
  Spells out each letter of the text, as in a-b-c.

###### Note

This option is not currently supported for neural voices.
If you're using a neural voice and this SSML code
is encountered by Amazon Polly at run-time, the affected
sentence will be synthesized using the related standard voice.
Please note, however, that this sentence will still be
billed as if it uses a neural voice.

- `cardinal` or `number`:
  Interprets the numerical text as a cardinal number, as
  in 1,234.
- `ordinal`: Interprets the numerical text as
  an ordinal number, as in 1,234th.
- `digits`: Spells out each digit
  individually, as in 1-2-3-4.
- `fraction`: Interprets the numerical text
  as a fraction. This works for both common fractions such
  as 3/20, and mixed fractions, such as 2 ½. See below for
  more information.
- `unit`: Interprets a numerical text as a
  measurement. The value should be either a number or a
  fraction followed by a unit with no space in between as
  in `1/2inch`, or by just a unit, as in
  `1meter`.
- `date`: Interprets the text as a date. The
  format of the date must be specified with the format
  attribute. See below for more information.
- `time`: Interprets the numerical text as
  duration, in minutes and seconds, as in
  `1'21"`.
- `address`: Interprets the text as part of a
  street address.
- `expletive`: "Beeps out" the content
  included within the tag.
- `telephone`: Interprets the numerical text
  as a 7-digit or 10-digit telephone number, as in
  `2025551212`. You can also use this value
  for handle telephone extensions, as in
  `2025551212x345`. See below for more
  information.

###### Note

Currently the `telephone` option is not
available for all languages. However, it is
available for voices speaking English language
variants (en-AU, en-GB, en-IN, en-US, and
en-GB-WLS), Spanish language variants (es-ES, es-MX,
and es-US), French language variants (fr-FR and
fr-CA), and Portuguese variants (pt-BR and pt-PT),
as well as German (de-DE), Italian (it-IT), Japanese
(ja-JP), and Russian (ru-RU). It should also be
noted that in some cases, languages such as Arabic
(arb) automatically handle the number set as a
telephone number and so don't actually implement
the `telephone` SSML tag.
**Fractions**

Amazon Polly interprets values within the `say-as` tag
that have the `interpret-as="fraction"` attribute as
common fractions. The following is the syntax for
fractions:

- _Fraction_

Syntax: `cardinal
 number`/`cardinal
 number`, such as 2/9.

For example: `<say-as
 interpret-as="fraction">2/9</say-as>` is
pronounced "two ninths."

- _Non-negative Mixed Number_

Syntax: `cardinal
 number`+`cardinal
 number`/`cardinal
 number`, such as 3+1/2.

For example, `<say-as
 interpret-as="fraction">3+1/2</say-as>` is
pronounced "three and a half."

###### Note

There must be a `+` between the "3" and
the "1/2". Amazon Polly doesn't support a mixed number
without the `+`, such as "3 1/2".
**Dates**

When `interpret-as` is set to `date`,
you also need to indicate the format of the date.

This uses the following syntax:

```
<say-as interpret-as="date" format="`format`">`[date]`</say-as>
```

For example:

```
<speak>
     I was born on <say-as interpret-as="date" format="mdy">12-31-1900</say-as>.
</speak>
```

The following formats can be used with the `date`
attribute.

- `mdy`: Month-day-year.
- `dmy`: Day-month-year.
- `ymd`: Year-month-day.
- `md`: Month-day.
- `dm`: Day-month.
- `ym`: Year-month.
- `my`: Month-year.
- `d`: Day.
- `m`: Month.
- `y`: Year.
- `yyyymmdd`: Year-month-day. If you use this
  format, you can make Amazon Polly skip parts of the date using
  question marks.

For example, Amazon Polly renders the following as "September
22nd":

```
<say-as interpret-as="date">????0922</say-as>
```

`Format` is not needed.
**Telephone**

Amazon Polly attempts to interpret the text you provide correctly
based on the text’s formatting even without the
`<say-as>` tag. For example, if your text
includes "202-555-1212," Amazon Polly interprets it as a 10-digit
telephone number and says each digit individually, with a brief
pause for each dash. In this case, you don't need to use
`<say-as interpret-as="telephone">`.
However, if you provide the text “2025551212” and want Amazon Polly to
say it as a phone number, you would specify `<say-as
 interpret-as="telephone">`.

The logic for interpreting each element is language-specific.
For example, US and UK English differ in how phone numbers are
pronounced (in UK English, sequences of the same digit are
grouped together, as in "double five" or "triple four"). To see
the difference, test the following example with a US voice and
with a UK voice:

```
<speak>
     Richard's number is <say-as interpret-as="telephone">2122241555</say-as>
</speak>
```
