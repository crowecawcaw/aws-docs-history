# Changing a voice speed

For certain applications, you may find that you'd prefer the voice you like be
slowed down, or speeded up. If the speed of the voice is a concern, Amazon Polly provides
the ability to modify this using SSML tags. For example, if your organization was
making an application that reads books to immigrant audiences, you may want to vary
the voice speed. Your audience may speak English, but their fluency is limited.
Amazon Polly helps you slow down the rate of speech using the SSML <prosody> tag.

**You can use a percentage:**

```
<speak>
     In some cases, it might help your audience to <prosody rate="85%">slow
     the speaking rate slightly to aid in comprehension.</prosody>
</speak>
```

**Or a preset speed:**

```
<speak>
     In some cases, it might help your audience to <prosody rate="slow">slow
     the speaking rate slightly to aid in comprehension.</prosody>
</speak>
```

Two speed options are available to you when using SSML with Amazon Polly:

- **Preset speeds:**
  `x-slow`, `slow`, `medium`,
  `fast`, and `x-fast`. In these cases, the speed of
  each option is approximate, depending on your preferred voice. The
  `medium` option is the normal speed of the voice.
- **n% of speech rate:** any percentage of the
  speech rate, between 20% and 200% can be used. In these cases, you can
  choose exactly the speed you want. However, the actual speed of the voice is
  approximate, depending on the voice you've chosen. 100% is considered to be
  the normal speed of the voice.

###### Note

Test your selected voice at various speeds. The speed of each option is
approximate and depends on the voice you choose.

For more information on using the `prosody` tag, see [Controlling volume, speaking rate,
and pitch](prosody-tag.md "prosody-tag.md") .
