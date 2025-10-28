# Whispering

_<amazon:effect
name="whispered">_

This tag is currently supported only by the standard TTS
format.

This tag indicates that the input text should be spoken in a
whispered voice rather than as normal speech. This can be used
with any of the voices in the Amazon Polly Text-to-Speech
portfolio.

This uses the following syntax:

```
<amazon:effect name="whispered">`text`</amazon:effect>
```

For example:

```
<speak>
     <amazon:effect name="whispered">If you make any noise, </amazon:effect>
     she said, <amazon:effect name="whispered">they will hear us.</amazon:effect>
</speak>
```

In this case, the synthesized speech spoken by the character
is whispered, but the phrase "she said" is spoken in the normal
synthesized speech of the selected Amazon Polly voice.

You can enhance the "whispered" effect by slowing down the
prosody rate by up to 10%, depending on the effect you want.

For example:

```
<speak>
     When any voice is made to whisper, <amazon:effect name="whispered">
     <prosody rate="-10%">the sound is slower and quieter than normal speech
     </prosody></amazon:effect>
</speak>
```

When generating speech marks for a whispered voice, the audio
stream must also include the whispered voice to ensure that the
speech marks match the audio stream.
