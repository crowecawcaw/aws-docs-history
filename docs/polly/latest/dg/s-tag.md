# Adding a pause between sentences

_<s>_

This tag is supported by generative, long-form, neural, and standard TTS formats.

To add a pause between lines or sentences in your text, use
the `<s>` tag. Using this tag has the same effect
as:

- Ending a sentence with a period (.)
- Specifying a pause with `<break
 strength="strong"/>`
  Unlike the `<break>` tag, the <s> tag
  encloses the sentence. This is useful for synthesizing speech
  that is organized in lines, rather than sentence, such as
  poetry.

In the following example, the `<s>` tag
creates a short pause after both the first and second sentences.
The final sentence has no `<s>` tag, but it is
also followed by a short pause because it ends with a
period.

```
<speak>
     <s>Mary had a little lamb</s>
     <s>Whose fleece was white as snow</s>
     And everywhere that Mary went, the lamb was sure to go.
</speak>
```
