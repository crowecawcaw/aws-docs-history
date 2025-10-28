# Speaking softly

_<amazon:effect
phonation="soft">_

This tag is currently supported only by the standard TTS
format.

To specify that input text should be spoken in a
softer-than-normal voice, use the <amazon:effect
phonation="soft"> tag.

This uses the syntax:

```
<amazon:effect phonation="soft">`text`</amazon:effect>
```

For example, you might use this tag with the Matthew voice as
follows:

```
<speak>
     This is Matthew speaking in my normal voice. <amazon:effect phonation="soft">This
     is Matthew speaking in my softer voice.</amazon:effect>
</speak>
```
