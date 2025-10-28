# Generating speech from SSML documents

You can use Amazon Polly to generate speech from either plain text or
from documents marked up with Speech Synthesis Markup Language (SSML).
Using SSML-enhanced text gives you additional control over how Amazon Polly
generates speech from the text you provide.

With SSML tags, you can customize and control aspects of speech
such as pronunciation, volume, and speech rate. In the AWS Management Console,
the SSML-enhanced text that you want to convert to audio is entered
on the SSML tab of the Text-to-Speech page. Although text entered in
plain text relies on default settings for the language and voice
you've chosen, text enhanced with SSML tells Amazon Polly not only what you
want to say, but how you want to say it. Except for the added SSML
tags, Amazon Polly synthesizes SSML-enhanced text in the same way as it
synthesizes plain text. See [Synthesizing speech with Amazon Polly example](synthesize-example.md "synthesize-example.md") for more
information.

When using SSML, you enclose the entire text in a
`<speak>` tag to let Amazon Polly know that you're using
SSML. For example:

```
<speak>Hi! My name is Joanna. I will read any text you type here.</speak>
```

You then use specific SSML tags on the text inside the
`<speak>` tags to customize the way you want the
text to sound. You can add a pause, change the pace of the speech,
lower or raise the volume of the voice, or add many other
customizations so that the text sounds right for you. For a full
list of the SSML tags that you can use, see [Supported SSML tags](supportedtags.md "supportedtags.md").

For example, you can include a long pause within your text, or change
the speech rate or pitch. Other options include:

- emphasizing specific words or phrases
- using phonetic pronunciation
- including breathing sounds
- whispering
- using the Newscaster speaking style.
  For complete details on the SSML tags supported by Amazon Polly and how to
  use them, see [Supported SSML tags](supportedtags.md "supportedtags.md")

When using SSML, there are several reserved characters that require
special treatment. This is because SSML uses these characters as part of
its code. In order to use them, you use a specific entity to
_escape_ them. For more information, see [Reserved characters in SSML](escapees.md "escapees.md")

Amazon Polly provides these types of control with a subset of the SSML markup
tags that are defined by [Speech Synthesis Markup Language (SSML) Version 1.1, W3C
Recommendation](https://www.w3.org/TR/2010/REC-speech-synthesis11-20100907/ "https://www.w3.org/TR/2010/REC-speech-synthesis11-20100907/").

You can use SSML within the Amazon Polly console or by using the AWS CLI. The
following topics show you how you can use SSML to generate speech and
control the output so that it precisely fits your needs.

###### Topics

- [Reserved characters in SSML](escapees.md "escapees.md")
- [Using SSML on the console](ssml-to-speech-console.md "ssml-to-speech-console.md")
- [Using SSML
  with the Synthesize-Speech command](example-ssml-synthesize-speech-cli.md "example-ssml-synthesize-speech-cli.md")
- [Synthesizing
  an SSML-enhanced document](example-ssml-synthesize-document.md "example-ssml-synthesize-document.md")
- [Supported SSML tags](supportedtags.md "supportedtags.md")
