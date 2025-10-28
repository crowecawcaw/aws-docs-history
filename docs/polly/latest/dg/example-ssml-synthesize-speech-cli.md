# Using SSML

with the Synthesize-Speech command

This example shows how to use the
`synthesize-speech` command with an SSML string.
When you use the `synthesize-speech` command, you
typically provide the following:

- The input text (required)
- Opening and closing tags (required)
- The output format
- A voice
  In this example, you specify a simple text string in quotation
  marks along with the required opening and closing
  `<speak></speak>` tags.

###### Important

Although you don't use quotation marks around input text
in the Amazon Polly console, you must use them in use the AWS CLI
It's also important that you differentiate between the
quotation marks around input text and quotations required
for individual tags.

For example, you can use standard quotation marks (") to
enclose the input text, and single quotation marks (') for
interior tags, or vice versa. Either option works for Unix,
Linux, and macOS. However, with Windows you must enclose the
input text in standard quotations marks and use single
quotation marks for the tags.

For all operating systems, you can use standard quotation
marks (") to enclose the input text, and single quotation
marks (') for interior tags). For example:

```
--text "<speak>Hello <break time='300ms'/> World</speak>"
```

For Unix, Linux, and macOS, you can also use the reverse,
with single quotation marks (') enclosing the input text and
standard quotation marks (") for interior tags:

```
--text '<speak>Hello <break time="300ms"/> World</speak>'
```

The following AWS CLI example is formatted for Unix, Linux, and macOS.
For Windows, replace the backslash (\) Unix continuation character at the end of each line with a caret (^) and use full quotation marks (") around the input text with single quotes (') for interior tags.

```
aws polly synthesize-speech \
--text-type ssml \
--text '<speak>Hello world</speak>' \
--output-format mp3 \
--voice-id Joanna \
speech.mp3
```

To hear the synthesized speech, play the resulting
`speech.mp3` file using any audio player.
