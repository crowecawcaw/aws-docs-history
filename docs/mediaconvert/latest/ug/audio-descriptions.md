# Audio descriptions

AWS Elemental MediaConvert supports two different workflows for including broadcast audio
descriptions in your output.

You can mix an audio description with other audio content if your input contains an
_audio description audio signal_ and an _audio description data stream_. An audio description audio
signal is a spoken description of a video, made for people who cannot see the visual
content. An audio description data stream contains fade and pan data used by an encoder.
MediaConvert uses this data stream to temporarily lower the volume of other audio channels
while an audio description is active.

If your input already has pre-mixed audio descriptions instead of an audio signal and data
stream channel, you can signal it to downstream systems by writing audio description
metadata in your output.

For more information about audio descriptions, see [BBC WHP
198](https://downloads.bbc.co.uk/rd/pubs/whp/whp-pdf-files/WHP198.pdf "https://downloads.bbc.co.uk/rd/pubs/whp/whp-pdf-files/WHP198.pdf") and [BBC WHP
051](https://downloads.bbc.co.uk/rd/pubs/whp/whp-pdf-files/WHP051.pdf "https://downloads.bbc.co.uk/rd/pubs/whp/whp-pdf-files/WHP051.pdf").

###### Topics

- [Configuring a job that mixes audio descriptions](audio-description-use.md "audio-description-use.md")
- [Configuring a job for pre-mixed audio
  descriptions](audio-description-broadcaster-mix.md "audio-description-broadcaster-mix.md")
