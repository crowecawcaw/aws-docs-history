# Uploading a lexicon

The lexicons you use must conform to the Pronunciation Lexicon Specification (PLS) W3C recommendation. For more information, see [Pronunciation Lexicon Specification (PLS) Version 1.0](https://www.w3.org/TR/pronunciation-lexicon/#S4.7 "https://www.w3.org/TR/pronunciation-lexicon/#S4.7") on the W3C website.

Console - Lexicons tab
To use a pronunciation lexicon, you must first upload it.
There are two locations on the console from which you can upload a lexicon,
the **Text-to-Speech** tab and the **Lexicons** tab.

The following processes describe how to add lexicons that you can use to customize
how words and phrases uncommon to the chosen language are pronounced.

###### To add a lexicon from the Lexicons tab

1. Sign in to the AWS Management Console and open the Amazon Polly console at [https://console.aws.amazon.com/polly/](https://console.aws.amazon.com/polly/ "https://console.aws.amazon.com/polly/").
2. Choose the **Lexicons** tab.
3. Choose **Upload lexicon**.
4. Provide a name for the lexicon and then use **Choose a
   lexicon file** to find the lexicon to upload. You can only
   upload PLS files with .pls or .xml extensions.
5. Choose **Upload lexicon**.
   If a lexicon by the same name (whether a .pls or .xml file) already exists, uploading the lexicon overwrites the existing lexicon.

Console - TTS tab

###### To add a lexicon from the text-to-Speech tab

1. Sign in to the AWS Management Console and open the Amazon Polly console at [https://console.aws.amazon.com/polly/](https://console.aws.amazon.com/polly/ "https://console.aws.amazon.com/polly/").
2. Choose the **Text-to-Speech** tab.
3. Expand **Additional settings**, turn on
   **Customize pronunciation,** and then choose
   **Upload lexicon**.
4. Provide a name for the lexicon and then use **Choose a lexicon
   file** to find the lexicon to upload. You can only use PLS files
   with .pls or .xml extensions.
5. Choose **Upload lexicon**.
   If a lexicon with the same name (whether a .pls or .xml file) already exists,
   uploading the lexicon overwrites the existing lexicon.

AWS CLI - one lexeme
With Amazon Polly, you can use [PutLexicon](API_PutLexicon.md "API_PutLexicon.md") to store pronunciation lexicons in a specific AWS Region for your account. Then, you can specify one or more of these stored lexicons in your [SynthesizeSpeech](API_SynthesizeSpeech.md "API_SynthesizeSpeech.md") request that you want to apply before the service starts synthesizing the text. For more information, see [Managing lexicons](managing-lexicons.md "managing-lexicons.md").

Consider the following W3C PLS-compliant lexicon.

```
<?xml version="1.0" encoding="UTF-8"?>
<lexicon version="1.0"
      xmlns="http://www.w3.org/2005/01/pronunciation-lexicon"
      xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
      xsi:schemaLocation="http://www.w3.org/2005/01/pronunciation-lexicon
        http://www.w3.org/TR/2007/CR-pronunciation-lexicon-20071212/pls.xsd"
      alphabet="ipa"
      xml:lang="en-US">
  <lexeme>
    <grapheme>W3C</grapheme>
    <alias>World Wide Web Consortium</alias>
  </lexeme>
</lexicon>
```

Note the following:

- The two attributes specified in the `<lexicon>` element:
  - The `xml:lang` attribute specifies the language code,
    `en-US`, to which the lexicon applies. Amazon Polly can use
    this example lexicon if the voice you
    specify in the `SynthesizeSpeech` call has
    the same language code (en-US).

  ###### Note

  You can use the `DescribeVoices` operation to
  find the language code associated with a voice.
  - The `alphabet` attribute specifies `IPA`, which means that
    the International Phonetic Alphabet (IPA) alphabet is used for
    pronunciations. IPA is one of the alphabets
    for writing pronunciations. Amazon Polly also supports the Extended Speech Assessment
    Methods Phonetic Alphabet (X-SAMPA).

- The `<lexeme>` element describes the mapping between `<grapheme>`
  (that is, a textual representation of the word) and `<alias>`.

To test this lexicon, do the following:

1. Save the lexicon as `example.pls`.
2. Run the `put-lexicon` AWS CLI command to store the lexicon (with
   the name `w3c`), in the us-east-2 region.

```
aws polly put-lexicon \
--name w3c \
--content file://example.pls
```

3. Run the `synthesize-speech` command to synthesize sample text
   to an audio stream (`speech.mp3`), and specify the optional
   `lexicon-name` parameter.

```
aws polly synthesize-speech \
--text 'W3C is a Consortium' \
--voice-id Joanna \
--output-format mp3 \
--lexicon-names="w3c" \
speech.mp3
```

4. Play the resulting `speech.mp3`, and notice that the word W3C in the text is
   replaced by World Wide Web Consortium.

The preceding example lexicon uses an alias. The IPA alphabet mentioned in the
lexicon is not used. The following lexicon specifies a phonetic pronunciation
using the `<phoneme>` element with the IPA alphabet.

```
<?xml version="1.0" encoding="UTF-8"?>
<lexicon version="1.0"
      xmlns="http://www.w3.org/2005/01/pronunciation-lexicon"
      xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
      xsi:schemaLocation="http://www.w3.org/2005/01/pronunciation-lexicon
        http://www.w3.org/TR/2007/CR-pronunciation-lexicon-20071212/pls.xsd"
      alphabet="ipa"
      xml:lang="en-US">
  <lexeme>
    <grapheme>pecan</grapheme>
    <phoneme>pɪˈkɑːn</phoneme>
  </lexeme>
</lexicon>
```

Follow the same steps to test this lexicon. Make sure you specify input text that
has the word "pecan" (for example, "Pecan pie is delicious").

See the following resources for additional code samples for the PutLexicon API operation:

- Java Sample: [PutLexicon](PutLexiconSample.md "PutLexiconSample.md")
- Python (Boto3) Sample: [PutLexicon](PutLexiconSamplePython.md "PutLexiconSamplePython.md")

AWS CLI - multiple lexemes
With Amazon Polly, you can use [PutLexicon](API_PutLexicon.md "API_PutLexicon.md") to store pronunciation lexicons in a specific AWS Region for your account. Then, you can specify one or more of these stored lexicons in your [SynthesizeSpeech](API_SynthesizeSpeech.md "API_SynthesizeSpeech.md") request that you want to apply before the service starts synthesizing the text. For more information, see [Managing lexicons](managing-lexicons.md "managing-lexicons.md").

In this example, the lexeme that you specify in the lexicon applies
exclusively to the input text for the synthesis. Consider the following lexicon:

```
<?xml version="1.0" encoding="UTF-8"?>
<lexicon version="1.0"
      xmlns="http://www.w3.org/2005/01/pronunciation-lexicon"
      xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
      xsi:schemaLocation="http://www.w3.org/2005/01/pronunciation-lexicon
        http://www.w3.org/TR/2007/CR-pronunciation-lexicon-20071212/pls.xsd"
      alphabet="ipa" xml:lang="en-US">

  <lexeme>
    <grapheme>W3C</grapheme>
    <alias>World Wide Web Consortium</alias>
  </lexeme>
  <lexeme>
    <grapheme>W3C</grapheme>
    <alias>WWW Consortium</alias>
  </lexeme>
  <lexeme>
    <grapheme>Consortium</grapheme>
    <alias>Community</alias>
  </lexeme>
</lexicon>
```

The lexicon specifies three lexemes, two of which define an alias for the grapheme
W3C as follows:

- The first `<lexeme`> element defines an alias (World Wide Web
  Consortium).
- The second `<lexeme>` defines an alternative alias (WWW
  Consortium).

Amazon Polly uses the first replacement for any given grapheme in a
lexicon.

The third `<lexeme>` defines a replacement (Community) for the word
Consortium.

First, let's test this lexicon. Suppose you want to synthesize the following sample
text to an audio file (`speech.mp3`), and you specify the lexicon in a call to
`SynthesizeSpeech`.

```
The W3C is a Consortium
```

`SynthesizeSpeech` first applies the lexicon as follows:

- As per the first lexeme, the word W3C is revised as World Wide Web
  Consortium. The revised text appears as follows:

```
The World Wide Web Consortium is a Consortium
```

- The alias defined in the third lexeme applies only to the word
  Consortium that was part of the original text, resulting in the
  following text:

```
The World Wide Web Consortium is a Community.
```

You can test this using the AWS CLI as follows:

1. Save the lexicon as `example.pls`.
2. Run the `put-lexicon` command to store the lexicon with name w3c in the us-east-2 region.

```
aws polly put-lexicon \
--name w3c \
--content file://example.pls
```

3. Run the `list-lexicons` command to verify that the w3c lexicon is in the list of lexicons returned.

```
aws polly list-lexicons
```

4. Run the `synthesize-speech` command to synthesize sample
   text to an audio file (`speech.mp3`), and specify the optional
   `lexicon-name` parameter.

```
aws polly synthesize-speech \
--text 'W3C is a Consortium' \
--voice-id Joanna \
--output-format mp3 \
--lexicon-names="w3c" \
speech.mp3
```

5. Play the resulting `speech.mp3` file to verify that the synthesized speech reflects the text changes.

See the following resources for additional code samples for the PutLexicon API operation:

- Java Sample: [PutLexicon](PutLexiconSample.md "PutLexiconSample.md")
- Python (Boto3) Sample: [PutLexicon](PutLexiconSamplePython.md "PutLexiconSamplePython.md")
