# Controlling volume, speaking rate,

and pitch

_<prosody>_

Prosody tag attributes are fully supported by the standard TTS
voices. Generative, Neural, and Long-Form voices support the `volume` and `rate` attributes, but don't support the `pitch` attribute. For Generative voices, the prosody tag can be used only around full sentences.

To control the volume, rate, or pitch of your selected voice,
use the `prosody` tag.

Volume, speech rate, and pitch are dependent on the specific
voice selected. In addition to differences between voices for
different languages, there are differences between individual
voices speaking the same language. Because of this, while
attributes are similar across all languages, there are clear
variations from language to language and no absolute value is
available.

The `prosody` tag has three attributes, each of
which has several available values to set the attribute. Each
attribute uses the same syntax:

```
<prosody `attribute`="`value`"></prosody>
```

- `volume`

      + `default`: Resets volume to the
       default level for the current voice.
      + `silent`, `x-soft`,
       `soft`, `medium`,
       `loud`, `x-loud`: Sets
       the volume to a predefined value for the current
       voice.
      + `+ndB`, `-ndB`: Changes
       volume relative to the current level. A value of
       `+0dB` means no change,
       `+6dB` means approximately twice
       the current volume, and `-6dB` means
       approximately half the current volume.

  For example, you could set the volume for a passage as
  follows:

```
<speak>
     Sometimes it can be useful to <prosody volume="loud">increase the volume
     for a specific speech.</prosody>
</speak>
```

Or you could set it this way:

```
<speak>
     And sometimes a lower volume <prosody volume="-6dB">is a more effective way of
     interacting with your audience.</prosody>
</speak>
```

- `rate`

      + `x-slow`, `slow`,
       `medium`,
       `fast`,`x-fast`. Sets
       the pitch to a predefined value for the selected
       voice.
      + `n%`: A non-negative percentage
       change in the speaking rate. For example, a
       value of 100% means no change in speaking rate,
       a value of 200% means a speaking rate twice the
       default rate, and a value of 50% means a
       speaking rate of half the default rate. This
       value has a range of 20-200%.

  For example, you could set the speech rate for a
  passage as follows:

```
<speak>
     For dramatic purposes, you might wish to <prosody rate="slow">slow up the speaking
     rate of your text.</prosody>
</speak>
```

Or you could set it this way:

```
<speak>
     Although in some cases, it might help your audience to <prosody rate="85%">slow
     the speaking rate slightly to aid in comprehension.</prosody>
</speak>
```

- `pitch`

      + `default`: Resets pitch to the
       default level for the current voice.
      + `x-low`, `low`,
       `medium`, `high`,
       `x-high`: Sets the pitch to a
       predefined value for the current voice.
      + `+n%` or `-n%`: Adjusts
       pitch by a relative percentage. For example, a
       value of `+0%` means no baseline
       pitch change, `+5%` gives a little
       higher baseline pitch, and `-5%`
       results in a little lower baseline pitch.

  For example, you could set the pitch for a passage as
  follows:

```
<speak>
     Do you like sythesized speech <prosody pitch="high">with a pitch that is higher
     than normal?</prosody>
</speak>
```

Or you could set it this way:

```
<speak>
     Or do you prefer your speech <prosody pitch="-10%">with a somewhat lower pitch?</prosody>
</speak>
```

The <prosody> tag must contain at least one attribute, but
can include more within the same tag.

```
<speak>
     Each morning when I wake up, <prosody volume="loud" rate="x-slow">I speak
     quite slowly and deliberately until I have my coffee.</prosody>
</speak>
```

It can also be combined with nested tags, as follows:

```
<speak>
     <prosody rate="85%">Sometimes combining attributes <prosody pitch="-10%">can
     change the impression your audience has of a voice</prosody> as well.</prosody>
</speak>
```
