# Placing a custom tag in your text

_<mark>_

This tag is supported by long-form, neural, and standard TTS formats. This tag does not do anything for generative voices because speechmarks are not available for generative voices.

To put a custom tag within the text, use the <mark> tag.
Amazon Polly takes no action on the tag, but returns the location of
the tag in the SSML metadata. This tag can be anything you want
to call out, as long as it maintains the following
format:

```
<mark name="`tag_name`"/>
```

For example, suppose that the tag name is "animal" and the
input text is:

```
<speak>
     Mary had a little <mark name="animal"/>lamb.
</speak>
```

Amazon Polly might return the following SSML metadata:

```
{"time":767,"type":"ssml","start":25,"end":46,"value":"animal"}
```
