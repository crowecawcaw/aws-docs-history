# Generative voices

Amazon Polly's **generative** text-to-speech (TTS) engine offers
the most human-like, emotionally engaged, and adaptive conversational voices available
for the use via the Amazon Polly console.

The **Generative engine** is the largest Amazon Polly TTS model
to-date. It deploys a
billion-parameter transformer that converts raw text into speech codes, followed by a
convolution-based decoder that converts these speech codes into waveforms in an
incremental, streamable manner. This method shows the widely-reported emergent abilities
of Large Language Models (LLMs) when trained on increasing volumes of publicly available
and proprietary data comprising a variety of voices, languages, and styles.

The Generative engine creates synthetic speech which is emotionally engaged, assertive,
and highly colloquial in a way that is remarkably similar to a human voice. You can use
these voices as a knowledgeable customer assistant, a virtual trainer, or an advertiser
with a near-human synthetic speech.

###### Note

The state-of-the-art technology underlying these voices falls within the paradigm
of generative AI for language and voice modelling. A side effect of the technology is
that any updates to the training data and the model could result in slight variations
to the way the voices sound, even in case when their overall quality improves with model
updates. This could have an impact on use cases with different content parts synthesized
over a long time period – for example, a season of podcasts.

## Available generative voices

Amazon Polly currently offers 33 voices in a generative
variant. These generative voices are also available in a conversational NTTS
variant.

|     | Language                    | Language code | Name/ID                                                   | Gender                                               |
| --- | --------------------------- | ------------- | --------------------------------------------------------- | ---------------------------------------------------- |
| 1   | **English (Australian)**    | en-AU         | Olivia                                                    | Female                                               |
| 2   | **English (Indian)**        | en-IN         | Kajal                                                     | Female                                               |
| 3   | **English (Ireland)**       | en-IE         | Niamh                                                     | Female                                               |
| 4   | **English (South African)** | en-ZA         | Ayanda                                                    | Female                                               |
| 5   | **English (UK)**            | en-GB         | Amy                                                       | Female                                               |
| 6   | **English (US)**            | en-US         | Danielle<br>Joanna<br>Matthew<br>Ruth<br>Salli<br>Stephen | Female<br>Female<br>Male<br>Female<br>Female<br>Male |
| 7   | **Dutch (Belgium)**         | nl-BE         | Lisa                                                      | Female                                               |
| 8   | **Dutch (Netherlands)**     | nl-NL         | Laura                                                     | Female                                               |
| 9   | **French (Belgian)**        | fr-BE         | Isabelle                                                  | Female                                               |
| 10  | **French (Canadian)**       | fr-CA         | Gabrielle<br>Liam                                         | Female<br>Male                                       |
| 11  | **French (France)**         | fr-FR         | Céline<br>Léa<br>Rémi                                     | Female<br>Female<br>Male                             |
| 12  | **German (Austria)**        | de-AT         | Hannah                                                    | Female                                               |
| 13  | **German (Germany)**        | de-DE         | Daniel<br>Vicki                                           | Male<br>Female                                       |
| 14  | **Italian (Italy)**         | it-IT         | Bianca                                                    | Female                                               |
| 15  | **Korean (Korea)**          | ko-KR         | Seoyeon                                                   | Female                                               |
| 16  | **Polish (Poland)**         | pl-PL         | Ewa<br>Ola                                                | Female<br>Female                                     |
| 17  | **Portuguese (Brazilian)**  | pt-BR         | Camila                                                    | Female                                               |
| 18  | **Spanish (Mexican)**       | es-MX         | Andrés<br>Mía                                             | Male<br>Female                                       |
| 19  | **Spanish (Spain)**         | es-ES         | Lucia<br>Sergio                                           | Female<br>Male                                       |
| 20  | **Spanish (US)**            | es-US         | Lupe<br>Pedro                                             | Female<br>Male                                       |

###### Note

Generative voices cost is specified on the [Amazon Polly pricing information page](https://aws.amazon.com/polly/pricing/ "https://aws.amazon.com/polly/pricing/").

## Feature and region compatibility

Amazon Polly generative voices are available in the following regions:

- US East (N. Virginia): us-east-1
- Europe (Frankfurt): eu-central-1
- US West (Oregon): us-west-2
- Other Regions are not available

**The following features are supported for generative
voices:**

- Real-time and asynchronous speech synthesis operations.
- Newscaster speaking style is not supported in the **Generative** engine.
- Many (but not all) SSML tags are supported by Amazon Polly. For more
  information about NTTS-supported SSML tags, see [Supported SSML tags](supportedtags.md "supportedtags.md")
- As with standard voices, you can choose from various sampling rates to
  optimize the bandwidth and audio quality for your application. Valid
  sampling rates for standard and neural voices are 8 kHz, 16 kHz, 22 kHz, or
  24 kHz. The default for standard voices is 22 kHz. The default for
  generative voices is 24 kHz. Amazon Polly supports MP3, OGG (Vorbis), and raw PCM
  audio stream formats.

_Support for generating speech marks is currently not available._

###### Note

In the unlikely event of model hallucination, (and with the Generative engine's model
behavior of rendering the speech token by token) an imposed emergency stop mechanism is
in place. The built-in mechanism stops the model from rendering
speech any further. This safety feature is based on data analysis
where the model has the potential to hallucinate, usually at the end of the sentence.

There could be cases where the model thinks it is going to hallucinate and then might
end up cutting a word during a generation step, thus rendering half the word. This could
potentially generate inappropriate results.
