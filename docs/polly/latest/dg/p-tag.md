# Adding a pause between paragraphs

_<p>_

This tag is supported by generative, long-form, neural, and standard TTS formats.

To add a pause between paragraphs in your text, use the <p>
tag. Using this tag provides a longer pause than native speakers
usually place at commas or the end of a sentence. Use the <p>
tag to enclose the paragraph:

```
<speak>
     <p>This is the first paragraph. There should be a pause after this text is spoken.</p>
     <p>This is the second paragraph.</p>
</speak>
```

This is equivalent to specifying a pause using <break
 strength="x-strong"/>.
