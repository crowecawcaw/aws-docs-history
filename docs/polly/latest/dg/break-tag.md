# Adding a pause

_<break>_

This tag is supported by generative, long-form, neural, and standard TTS formats.

To add a pause to your text, use the <break> tag. You can
set a pause based on strength (equivalent to the pause after a
comma, a sentence, or a paragraph), or you can set it to a
specific length of time in seconds or milliseconds. If you don't
specify an attribute to determine the pause length, Amazon Polly uses
the default, which is `<break
 strength="medium"/>`, which adds a pause the length
of a pause after a comma.

`strength` attribute values:

- `none`: No pause. Use `none` to
  remove a normally occurring pause, such as after a
  period.
- `x-weak`: Has the same strength as
  `none`, no pause.
- `weak`: Sets a pause of the same duration
  as the pause after a comma.
- `medium`: Has the same strength as
  `weak`.
- `strong`: Sets a pause of the same duration
  as the pause after a sentence.
- `x-strong`: Sets a pause of the same
  duration as the pause after a paragraph.
  `time` attribute values:

- ``[number]`s`: The
duration of the pause, in seconds. The maximum duration
is `10s`.
- ``[number]`ms`:
 The duration of the pause, in milliseconds. The maximum
 duration is `10000ms`.
  For example:

```
<speak>
     Mary had a little lamb <break time="3s"/>Whose fleece was white as snow.
</speak>
```

If you don't use an attribute with the `break` tag,
the result varies depending on text:

- If there is no other punctuation next to the
  `break` tag, it creates a `<break
strength="medium"/>` (comma-length
  pause).
- If the tag is next to a comma, it upgrades the tag to
  a `<break strength="strong"/>`
  (sentence-length pause).
- If the tag is next to a period, it upgrades the tag to
  `<break strength="x-strong"/>`
  (paragraph-length pause).
