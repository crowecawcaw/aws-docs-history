# Synthesizing

an SSML-enhanced document

For longer input text, you may find it easier to save your
SSML content to a file and simply specify the file name in the
`synthesize-speech` command. For example you
could save the following to a file called
`example.xml`:

```
<?xml version="1.0"?>
<speak version="1.1"
       xmlns="http://www.w3.org/2001/10/synthesis"
       xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
       xsi:schemaLocation="http://www.w3.org/2001/10/synthesis http://www.w3.org/TR/speech-synthesis11/synthesis.xsd"
       xml:lang="en-US">Hello World</speak>
```

The `xml:lang` attribute specifies
`en-US` (US English) as the language of the input
text. For information about how the language of the input text
and the language of the chosen voice affect the
`SynthesizeSpeech` operation, see [Specifying another language for
specific words](lang-tag.md "lang-tag.md").

###### To run an SSML-enhanced file

1. Save the SSML to a file (for example,
   `example.xml`).
2. Run the following `synthesize-speech`
   command from the path where the XML file is stored and
   specify the SSML file as input by substituting
   `file:\\example.xml` for the input text.
   Because this command points to a file instead of
   containing the actual input text, you don't use
   quotation marks.

###### Note

The following AWS CLI example is formatted for Unix,
Linux, and macOS. For Windows, replace the backslash
(\) Unix continuation character at the end of each
line with a caret (^).

```
aws polly synthesize-speech \
--text-type ssml \
--text file://example.xml \
--output-format mp3 \
--voice-id Joanna \
speech.mp3
```

3. To hear the synthesized speech, play the resulting
   `speech.mp3` file using any audio
   player.
