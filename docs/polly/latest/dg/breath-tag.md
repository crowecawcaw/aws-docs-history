# Adding the sound of breathing

_<amazon:breath> and
<amazon:auto-breaths>_

This tag is supported only by the standard TTS format.

Natural-sounding speech includes both correctly spoken words
and breathing sounds. By adding breathing sounds to synthesized
speech, you can make it sound more natural. The
`<amazon:breath>` and
`<amazon:auto-breaths>` tags provide
breaths. You have the following options:

- Manual mode: you set the location, length, and volume
  of a breath sound within the text
- Automated mode: Amazon Polly automatically inserts breathing
  sounds into the speech output
- Mixed mode: both you and Amazon Polly add breathing sounds

###### Manual Mode

In manual mode, you place the
`<amazon:breath/>` tag in the input
text where you want to locate a breath. You can customize
the length and volume of breaths with the
`duration` and `volume`
attributes, respectively:

- `duration`: Controls the length of the
  breath. Valid values are: `default`,
  `x-short`, `short`,
  `medium`, `long`,
  `x-long`. The default value is
  `medium`.
- `volume`: Controls how loud breathing
  sounds. Valid values are: `default`,
  `x-soft`, `soft`,
  `medium`, `loud`,
  `x-loud`. The default value is
  `medium`.

###### Note

The exact length and volume of each attribute value is
dependent on the specific Amazon Polly voice used.

To set a breath sound using the defaults, use
`<amazon:breath/>` without attributes.

For example, to use attributes to set the duration and volume
for a breath to medium, you would set the attributes as follows:

```
<speak>
     Sometimes you want to insert only <amazon:breath duration="medium" volume="x-loud"/>a single breath.
</speak>
```

To use the defaults, you would just use the tag:

```
<speak>
     Sometimes you need <amazon:breath/>to insert one or more average breaths <amazon:breath/> so that the
     text sounds correct.
</speak>
```

You can add individual breathing sounds within a passage, as
follows:

```
<speak>
     <amazon:breath duration="long" volume="x-loud"/> <prosody rate="120%"> <prosody volume="loud">
     Wow! <amazon:breath duration="long" volume="loud"/> </prosody> That was quite fast. <amazon:breath
     duration="medium" volume="x-loud"/> I almost beat my personal best time on this track. </prosody>
</speak>
```

###### Automated Mode

In automated mode, you use the
`<amazon:auto-breaths>` tag to tell
Amazon Polly to automatically create breathing noises at
appropriate intervals. You can set the frequency of the
intervals, their volume, and their duration. Place the
`</amazon:auto-breaths>` tag at the
beginning of the text that you want to apply automated
breathing to and then close the tag at the end.

###### Note

Unlike the manual mode tag,
`<amazon:breath/>`, the
`<amazon:auto-breaths>` tag requires a
closing tag (`</amazon:auto-breaths>`).

You can use the following optional attributes with the
`<amazon:auto-breaths>` tag:

- `volume`: Controls how loud the breathing
  sounds. Valid values are: `default`,
  `x-soft`, `soft`,
  `medium`, `loud`,
  `x-loud`. The default value is
  `medium`.
- `frequency`: Controls how often breathing
  sounds occur in the text. Valid values are:
  `default`, `x-low`,
  `low`, `medium`,
  `high`, `x-high`. The default
  value is `medium`.
- `duration`: Controls the length of the
  breath. Valid values are: `default`,
  `x-short`, `short`,
  `medium`, `long`,
  `x-long`. The default value is
  `medium`.
  By default, the frequency of breathing sounds depends on the
  input text. However, breathing sounds often occur after commas
  and periods.

The following examples show how to use the
`<amazon:auto-breaths>` tag. To decide
which options to use for your content, copy the applicable
examples to the Amazon Polly console and listen to the differences.

- Using automated mode without optional parameters.

```
<speak>
     <amazon:auto-breaths>Amazon Polly is a service that turns text into lifelike speech,
     allowing you to create applications that talk and build entirely new categories of speech-
     enabled products. Amazon Polly is a text-to-speech service that uses advanced deep learning
     technologies to synthesize speech that sounds like a human voice. With dozens of lifelike
     voices across a variety of languages, you can select the ideal voice and build speech-
     enabled applications that work in many different countries.</amazon:auto-breaths>
</speak>
```

- Using automated mode with volume control. The
  unspecified parameters (`duration` and
  `frequency`) are set to the default
  values (`medium`).

```
<speak>
     <amazon:auto-breaths volume="x-soft">Amazon Polly is a service that turns text into lifelike
     speech, allowing you to create applications that talk and build entirely new categories of
     speech-enabled products. Amazon Polly is a text-to-speech service, that uses advanced deep
     learning technologies to synthesize speech that sounds like a human voice. With dozens of
     lifelike voices across a variety of languages, you can select the ideal voice and build speech-
     enabled applications that work in many different countries.</amazon:auto-breaths>
</speak>
```

- Using automated mode with frequency control. The
  unspecified parameters (`duration` and
  `volume`) are set to the default values
  (`medium`).

```
<speak>
     <amazon:auto-breaths frequency="x-low">Amazon Polly is a service that turns text into lifelike
     speech, allowing you to create applications that talk and build entirely new categories of
     speech-enabled products. Amazon Polly is a text-to-speech service, that uses advanced deep
     learning technologies to synthesize speech that sounds like a human voice. With dozens of
     lifelike voices across a variety of languages, you can select the ideal voice and build speech-
     enabled applications that work in many different countries.</amazon:auto-breaths>
</speak>
```

- Using automated mode with multiple parameters. For
  the unspecified `Duration` parameter, Amazon Polly
  uses the default value (`medium`).

```
<speak>
     <amazon:auto-breaths volume="x-loud" frequency="x-low">Amazon Polly is a service that turns
     text into lifelike speech, allowing you to create applications that talk and build entirely new
     categories of speech-enabled products. Amazon Polly is a text-to-speech service, that uses
     advanced deep learning technologies to synthesize speech that sounds like a human voice. With
     dozens of lifelike voices across a variety of languages, you can select the ideal voice and build
     speech-enabled applications that work in many different countries.</amazon:auto-breaths>
</speak>
```
