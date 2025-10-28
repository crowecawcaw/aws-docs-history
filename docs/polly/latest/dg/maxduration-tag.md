# Setting a maximum duration for

synthesized speech

_<prosody amazon:max-duration>_

This tag is currently supported only by the standard TTS
format.

To control how long you want a speech to take when it is
synthesized, use the `<prosody>` tag with the
`amazon:max-duration` attribute.

The duration of synthesized speech varies slightly, depending
on the voice you select. This can make it difficult to match
synthesized speech with visuals or other activities that require
precise timing. This issue is magnified for translation
applications because the time it takes to say particular phrases
can vary widely with different languages.

The `<prosody amazon:max-duration>` tag matches
synthesized speech to the amount of time you want it to take
(the duration).

This tag uses the following syntax:

```
<prosody amazon:max-duration="`time duration`">
```

With the `<prosody amazon:max-duration>` tag,
you can specify duration in either seconds or
milliseconds:

- ``n`s`: the
  maximum duration in seconds
- ``n`ms`: the
  maximum duration in milliseconds
  For example, the following spoken text has a maximum duration
  of 2 seconds:

```
<speak>
     <prosody amazon:max-duration="2s">
          Human speech is a powerful way to communicate.
     </prosody>
</speak>
```

Text placed within the tag, it doesn't exceed the specified
duration. If the chosen voice or language would normally take
longer than that duration, Amazon Polly speeds up the speech so that it
fits into the specified duration.

If the specified duration is longer than it takes to read the
text at a normal rate, Amazon Polly reads the speech normally. It
doesn't slow down the speech or add silence, so the resulting
audio is shorter than requested.

###### Note

Amazon Polly increases the speed no more than 5 times the normal
rate. If text is spoken faster than this, it usually doesn't
make sense. If a speech cannot fit within your specified
duration even when speeded up to the maximum, the audio will
be speeded up but will last longer than the specified
duration.

You can include a single sentence or multiple sentences within
a `<prosody amazon:max-duration>` tag, and you can
use multiple `<prosody amazon:max-duration>` tags
within your text.

For example:

```
<speak>
     <prosody amazon:max-duration="2400ms">
        Human speech is a powerful way to communicate.
     </prosody>
     <break strength="strong"/>
     <prosody amazon:max-duration="5100ms">
        Even a simple ‘Hello’ can convey a lot of information depending on the pitch, intonation, and tempo.
     </prosody>
     <break strength="strong"/>
     <prosody amazon:max-duration="8900ms">
        We naturally understand this information, which is why speech is ideal for creating applications where
        a screen isn’t practical or possible, or simply isn’t convenient.
     </prosody>
</speak>
```

Using the `<prosody amazon:max-duration>` tag
can increase latency when Amazon Polly is returns synthesized speech.
The degree of latency depends on the passage and its length. We
recommend using text comprised of relatively short text
passages.

**Limitations**

There are limitations both in how you use `<prosody
 amazon:max-duration>` tag and in how it works with
other SSML tags:

- The text inside a `<prosody
amazon:max-duration>` tag can't be longer than
  1500 characters.
- You can't nest `<prosody
amazon:max-duration>` tags. If you put one
  `<prosody amazon:max-duration>` tag
  inside another, Amazon Polly ignores the inner tag.

For example, in the following, the `<prosody
 amazon:max-duration="5s">` tag is
ignored:

```
<speak>
     <prosody amazon:max-duration="16s">
          Human speech is a powerful way to communicate.

          <prosody amazon:max-duration="5s">
               Even a simple ‘Hello’ can convey a lot of information depending on the pitch, intonation, and tempo.
          </prosody>

          We naturally understand this information, which is why speech is ideal for creating applications where a screen isn’t practical or possible, or simply isn’t convenient.
     </prosody>
</speak>
```

- You can't use the `<prosody>` tags with
  the `rate` attribute within a
  `<prosody amazon:max-duration>` tag.
  This is because both affect the speed at which text is
  spoken.

In the following example, Amazon Polly ignores the
`<prosody rate="2">` tag:

```
<speak>
     <prosody amazon:max-duration="7500ms">
          Human speech is a powerful way to communicate.

          <prosody rate="2">
               Even a simple ‘Hello’ can convey a lot of information depending on the pitch, intonation, and tempo.
          </prosody>
     </prosody>
</speak>
```

**Pauses and `max-duration`**

When using `max-duration` tag, you can still insert
pauses within your text. However, Amazon Polly includes the length of
the pause when calculating the maximum duration for speech.
Additionally, Amazon Polly preserves the short pauses that occur where
commas and periods are placed within a passage and includes in
the maximum duration.

For example, in the following block, the 600 millisecond break
and the breaks caused by the commas and periods occur within the
8-second speech:

```
<speak>
     <prosody amazon:max-duration="8s">
          Human speech is a powerful way to communicate.
          <break time="600ms"/>
          Even a simple ‘Hello’ can convey a lot of information depending on the pitch, intonation, and tempo.
     </prosody>
</speak>
```
