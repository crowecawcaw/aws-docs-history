# Neural voices

Amazon Polly has a **Neural text-to-speech (NTTS) engine** that
can produce even higher quality voices than its standard voices. Standard TTS voices use
concatenative synthesis. The standard engine concatenates phonemes of recorded speech,
producing very natural-sounding synthesized speech. However, the inevitable variations
in speech and the techniques used to segment the waveforms limits the quality of speech.
The Amazon Polly NTTS engine doesn't use standard concatenative synthesis to produce speech. It
has two parts:

- A neural network — that converts a sequence of phonemes (the most basic
  units of language) into a sequence of _spectrograms_. (Spectograms are snapshots of the energy levels in
  different frequency bands.)
- A vocoder — that converts spectrograms into a nearly continuous audio
  signal.
  The first component of the neural TTS system is a sequence-to-sequence model. This
  model doesn’t create its results solely from the corresponding input but also considers
  how the sequence of the elements of the input work together. The model chooses the
  spectrograms that it outputs so that their frequency bands emphasize acoustic features
  that the human brain uses when processing speech.

The output of this model then passes to a neural vocoder. This converts the
spectrograms into speech waveforms. When trained on the large datasets used to build
general-purpose concatenative-synthesis systems, this sequence-to-sequence approach will
yield higher-quality, more natural-sounding voices.

## Available neural voices

Neural voices are available in 36 languages and language variants. The following
table lists the voices.

|     | Language and language variants | Language code | Name/ID                                                                                                                          | Gender                                                                                                                                     |
| --- | ------------------------------ | ------------- | -------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------ |
| 1   | **Arabic (Gulf)**              | ar-AE         | Hala<br>Zayd                                                                                                                     | Female<br>Male                                                                                                                             |
| 2   | **Belgian Dutch (Flemish)**    | nl-BE         | Lisa                                                                                                                             | Female                                                                                                                                     |
| 3   | **Catalan**                    | ca-ES         | Arlet                                                                                                                            | Female                                                                                                                                     |
| 4   | **Czech**                      | cs-CZ         | Jitka                                                                                                                            | Female                                                                                                                                     |
| 5   | **Chinese (Cantonese)**        | yue-CN        | Hiujin                                                                                                                           | Female                                                                                                                                     |
| 6   | **Chinese (Mandarin)**         | cmn-CN        | Zhiyu                                                                                                                            | Female                                                                                                                                     |
| 7   | **Danish**                     | da-DK         | Sofie                                                                                                                            | Female                                                                                                                                     |
| 8   | **Dutch**                      | nl-NL         | Laura                                                                                                                            | Female                                                                                                                                     |
| 9   | **English (Australian)**       | en-AU         | Olivia                                                                                                                           | Female                                                                                                                                     |
| 10  | **English (British)**          | en-GB         | Amy\*<br>Emma<br>Brian<br>Arthur                                                                                                 | Female<br>Female<br>Male<br>Male                                                                                                           |
| 11  | **English (Indian)**           | en-IN         | Kajal                                                                                                                            | Female                                                                                                                                     |
| 12  | **English (Irish)**            | en-IE         | Niamh                                                                                                                            | Female                                                                                                                                     |
| 13  | **English (New Zealand)**      | en-NZ         | Aria                                                                                                                             | Female                                                                                                                                     |
| 14  | **English (Singaporean)**      | en-SG         | Jasmine                                                                                                                          | Female                                                                                                                                     |
| 15  | **English (South African)**    | en-ZA         | Ayanda                                                                                                                           | Female                                                                                                                                     |
| 16  | **English (US)**               | en-US         | Danielle<br>Gregory<br>Ivy<br>Joanna\*<br>Kendra<br>Kimberly<br>Salli<br>Joey<br>Justin<br>Kevin<br>Matthew\*<br>Ruth<br>Stephen | Female<br>Male<br>Female (child)<br>Female<br>Female<br>Female<br>Female<br>Male<br>Male (child)<br>Male (child)<br>Male<br>Female<br>Male |
| 17  | **Finnish**                    | fi-FI         | Suvi                                                                                                                             | Female                                                                                                                                     |
| 18  | **French (Belgian)**           | fr-BE         | Isabelle                                                                                                                         | Female                                                                                                                                     |
| 19  | **French (Canadian)**          | fr-CA         | Gabrielle<br>Liam                                                                                                                | Female<br>Male                                                                                                                             |
| 20  | **French**                     | fr-FR         | Léa<br>Rémi                                                                                                                      | Female<br>Male                                                                                                                             |
| 21  | **German**                     | de-DE         | Vicki<br>Daniel                                                                                                                  | Female<br>Male                                                                                                                             |
| 22  | **German (Austrian)**          | de-AT         | Hannah                                                                                                                           | Female                                                                                                                                     |
| 23  | **German (Swiss)**             | de-CH         | Sabrina                                                                                                                          | Female                                                                                                                                     |
| 24  | **Hindi**                      | hi-IN         | Kajal                                                                                                                            | Female                                                                                                                                     |
| 25  | **Italian**                    | it-IT         | Bianca<br>Adriano                                                                                                                | Female<br>Male                                                                                                                             |
| 26  | **Japanese**                   | ja-JP         | Takumi<br>Kazuha<br>Tomoko                                                                                                       | Male<br>Female<br>Female                                                                                                                   |
| 27  | **Korean**                     | ko-KR         | Seoyeon<br>Jihye                                                                                                                 | Female<br>Female                                                                                                                           |
| 28  | **Norwegian**                  | nb-NO         | Ida                                                                                                                              | Female                                                                                                                                     |
| 29  | **Polish**                     | pl-PL         | Ola                                                                                                                              | Female                                                                                                                                     |
| 30  | **Portuguese (Brazilian)**     | pt-BR         | Camila<br>Vitória/Vitoria<br>Thiago                                                                                              | Female<br>Female<br>Male                                                                                                                   |
| 31  | **Portuguese (European)**      | pt-PT         | Inês/Ines                                                                                                                        | Female                                                                                                                                     |
| 32  | **Spanish (Spain)**            | es-ES         | Lucia<br>Sergio                                                                                                                  | Female<br>Male                                                                                                                             |
| 33  | **Spanish (Mexican)**          | es-MX         | Mia<br>Andrés                                                                                                                    | Female<br>Male                                                                                                                             |
| 34  | **Spanish (US)**               | es-US         | Lupe\*<br>Pedro                                                                                                                  | Female<br>Male                                                                                                                             |
| 35  | **Swedish**                    | sv-SE         | Elin                                                                                                                             | Female                                                                                                                                     |
| 36  | **Turkish**                    | tr-TR         | Burcu                                                                                                                            | Female                                                                                                                                     |

\*The Amy, Joanna, Lupe, and Matthew voices can be used with the Newscaster
speaking style. For more information, see [Applying the newscaster voice](newscaster-voices.md "newscaster-voices.md").

## Feature and region compatibility

Neural voices aren't available in all AWS Regions, nor do they support all Amazon Polly
features.

Neural voices are supported in the following regions:

- US East (N. Virginia): us-east-1
- US West (Oregon): us-west-2
- Africa (Cape Town): af-south-1
- Asia Pacific (Tokyo): ap-northeast-1
- Asia Pacific (Seoul): ap-northeast-2
- Asia Pacific (Osaka): ap-northeast-3
- Asia Pacific (Mumbai): ap-south-1
- Asia Pacific (Singapore): ap-southeast-1
- Asia Pacific (Sydney): ap-southeast-2
- Asia Pacific (Malaysia): ap-southeast-5
- Canada (Central): ca-central-1
- Europe (Frankfurt): eu-central-1
- Europe (Ireland): eu-west-1
- Europe (London): eu-west-2
- Europe (Paris): eu-west-3
- Europe (Spain): eu-south-2
- AWS GovCloud (US-West): us-gov-west-1

Endpoints and protocols for these Regions are identical to those used for standard
voices. For more information, see [Amazon Polly endpoints and
quotas](../../../general/latest/gr/pol.md "../../../general/latest/gr/pol.md").

The following features are supported for neural voices:

- Real-time and asynchronous speech synthesis operations.
- Newscaster speaking style. For more information about the speaking styles,
  see [Applying the newscaster voice](newscaster-voices.md "newscaster-voices.md").
- All speech marks.
- Many (but not all) of the SSML tags that are supported by Amazon Polly. For more
  information about NTTS-supported SSML tags, see Supported
  Tags.

As with standard voices, you can choose from various sampling rates to optimize
the bandwidth and audio quality for your application. Valid sampling rates for
standard and neural voices are 8 kHz, 16 kHz, 22 kHz, or 24 kHz. The default for
standard voices is 22 kHz. The default for neural voices is 24 kHz. Amazon Polly supports
MP3, OGG (Vorbis), and raw PCM audio stream formats.
