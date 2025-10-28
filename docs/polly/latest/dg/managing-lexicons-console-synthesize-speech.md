# Applying lexicons (Synthesizing Speech)

The lexicons you use must conform to the Pronunciation Lexicon Specification (PLS) W3C recommendation. For more information, see [Pronunciation Lexicon Specification (PLS) Version 1.0](https://www.w3.org/TR/pronunciation-lexicon/#S4.7 "https://www.w3.org/TR/pronunciation-lexicon/#S4.7") on the W3C website.

Console
The following procedure demonstrates how to apply a lexicon to your input text by
applying the `W3c.pls` lexicon to substitute "World Wide Web Consortium" for "W3C".
If you apply multiple lexicons to your text they are applied in a top-down order
with the first match taking precedence over later matches.
A lexicon is applied to the text only if the language specified in the lexicon is
the same as the language chosen.

You can apply a lexicon to plain text or SSML input.

###### Example – Applying the W3C.pls Lexicon

To create the lexicon you'll need for this exercise,
see [Uploading a lexicon](managing-lexicons-console-upload.md "managing-lexicons-console-upload.md"). Use a plain text editor to create the W3C.pls
lexicon shown at the top of the topic. Remember where you save this file.

###### To apply the W3C.pls lexicon to your input

In this example we introduce a lexicon to substitute "World Wide Web
Consortium" for "W3C".
Compare the results of this exercise with that of [Using SSML on the console](ssml-to-speech-console.md "ssml-to-speech-console.md") for
both US English and another language.

1. Sign in to the AWS Management Console and open the Amazon Polly console at [https://console.aws.amazon.com/polly/](https://console.aws.amazon.com/polly/ "https://console.aws.amazon.com/polly/").
2. Do one of the following:
   - Turn off **SSML** and then type or paste this text into the
     text input box.

   ```
   He was caught up in the game.
   In the middle of the 10/3/2014 W3C meeting
   he shouted, "Score!" quite loudly.
   ```

   - Turn on **SSML** and then type or paste this text into the
     text input box.

   ```
   <speak>He wasn't paying attention.<break time="1s"/>
   In the middle of the 10/3/2014 W3C meeting
   he shouted, "Score!" quite loudly.</speak>
   ```

3. From the **Language** list, choose
   **English, US**, then choose the voice you want to use for this text.
4. Expand **Additional settings** and turn on
   **Customize pronunciation.**
5. From the list of lexicons, choose `W3C (English, US)`.

If the `W3C (English, US)` lexicon is not listed,
choose **Upload lexicon** and upload it, then
choose it from the list. To create this lexicon,
see [Uploading a lexicon](managing-lexicons-console-upload.md "managing-lexicons-console-upload.md"). 6. To listen to the speech immediately,
choose **Listen**. 7. To save the speech to a file,

    1. Choose **Download**.
    2. To change to a different file format,
     turn on **Speech file format settings**,
     choose the file format you want, and then choose **Download**.

Repeat the previous steps, but choose a different language and notice the difference in the output.

AWS CLI
In a call to `SynthesizeSpeech`, you can specify multiple
lexicons. In this case, the first lexicon specified (in order from left to right)
overrides any preceding lexicons.

Consider the following two lexicons. Note that each lexicon describes different
aliases for the same grapheme W3C.

- Lexicon 1: `w3c.pls`

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
</lexicon>
```

- Lexicon 2: `w3cAlternate.pls`

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
    <alias>WWW Consortium</alias>
  </lexeme>
</lexicon>
```

Suppose you store these lexicons as `w3c` and `w3cAlternate`
respectively. If you specify lexicons
in order (`w3c` followed by `w3cAlternate`)
in a `SynthesizeSpeech` call,
the alias for W3C defined in the first lexicon has precedence over the second. To test the
lexicons, do the following:

1. Save the lexicons locally in files called `w3c.pls` and `w3cAlternate.pls`.
2. Upload these lexicons using the `put-lexicon` AWS CLI command.
   - Upload the `w3c.pls` lexicon and store it as `w3c`.

   ```
   aws polly put-lexicon \
   --name w3c \
   --content file://w3c.pls

   ```

   - Upload the `w3cAlternate.pls` lexicon on the service as
     `w3cAlternate`.

   ```
   aws polly put-lexicon \
   --name w3cAlternate \
   --content file://w3cAlternate.pls
   ```

3. Run the `synthesize-speech` command to synthesize sample text to an audio stream
   (`speech.mp3`), and specify both lexicons using the
   `lexicon-name` parameter.

```
aws polly synthesize-speech \
--text 'PLS is a W3C recommendation' \
--voice-id Joanna \
--output-format mp3 \
--lexicon-names '["w3c","w3cAlternative"]' \
speech.mp3
```

4. Test the resulting `speech.mp3`. It should read as follows:

```
PLS is a World Wide Web Consortium recommendation
```
