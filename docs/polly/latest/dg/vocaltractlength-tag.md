# Controlling timbre

_<amazon:effect
vocal-tract-length>_

This tag is currently supported only by the standard TTS
format.

Timbre is the tonal quality of a voice that helps you tell the
difference between voices, even when they have the same pitch
and loudness. One of the most important physiological features
that contributes to speech timbre is the length of the vocal
tract. The vocal tract is a cavity of air that spans from the
top of the vocal folds up to the edge of the lips.

To control the timbre of output speech in Amazon Polly, use the
`vocal-tract-length` tag. This tag has the effect
of changing the length of the speaker’s vocal tract, which
sounds like a change in the speaker’s size. When you increase
the `vocal-tract-length`, the speaker sounds
physically bigger. When you decrease it, the speaker sounds
smaller. You can use this tag with any of the voices in the
Amazon Polly Text-to-Speech portfolio.

To change timbre, use the following values:

- `+n%` or `-n%`: Adjusts the
  vocal tract length by a relative percentage change in
  the current voice. For example, +4% or -2%. Valid values
  range from +100% to -50%. Values outside this range are
  clipped. For example, +111% sounds like +100% and -60%
  sounds like -50%.
- `n%`: Changes the vocal tract length to an
  absolute percentage of the tract length of the current
  voice. For example, 110% or 75%. An absolute value of
  110% is equivalent to a relative value of +10%. An
  absolute value of 100% is the same as the default value
  for the current voice.
  The following example shows how to change the vocal tract
  length to change timbre:

```
<speak>
     This is my original voice, without any modifications. <amazon:effect vocal-tract-length="+15%">
     Now, imagine that I am much bigger. </amazon:effect> <amazon:effect vocal-tract-length="-15%">
     Or, perhaps you prefer my voice when I'm very small. </amazon:effect> You can also control the
     timbre of my voice by making minor adjustments. <amazon:effect vocal-tract-length="+10%">
     For example, by making me sound just a little bigger. </amazon:effect><amazon:effect
     vocal-tract-length="-10%"> Or, making me sound only somewhat smaller. </amazon:effect>
</speak>
```

**Combining Multiple
Tags**

You can combine the `vocal-tract-length` tag with
any other SSML tag that is supported by Amazon Polly. Because timbre
(vocal tract length) and pitch are closely connected, you might
get the best results by using both the
`vocal-tract-length` and the `<prosody
 pitch>` tags. To produce the most realistic voice, we
recommend that you use different percentages of change for the
two tags. Experiment with various combinations to get the
results you want.

The following example shows how to combine tags.

```
<speak>
     The pitch and timbre of a person's voice are connected in human speech.
     <amazon:effect vocal-tract-length="-15%"> If you are going to reduce the vocal tract length,
     </amazon:effect><amazon:effect vocal-tract-length="-15%"> <prosody pitch="+20%"> you
     might consider increasing the pitch, too. </prosody></amazon:effect>
     <amazon:effect vocal-tract-length="+15%"> If you choose to lengthen the vocal tract,
     </amazon:effect> <amazon:effect vocal-tract-length="+15%"> <prosody pitch="-10%">
     you might also want to lower the pitch. </prosody></amazon:effect>
</speak>
```
