# Standard voices

Amazon Polly has a **standard** engine that use concatenative
synthesis. The standard engine concatenates phonemes of recorded speech, producing very
natural-sounding synthesized speech.

## Available Standard voices

Amazon Polly currently offers 40 female and 20 male standard voices in 29 language
and language variants.

|     | Language                   | Language code | Name/ID                                                       | Gender                                                         |
| --- | -------------------------- | ------------- | ------------------------------------------------------------- | -------------------------------------------------------------- |
| 1   | **Arabic**                 | arb           | Zeina                                                         | Female                                                         |
| 2   | **Chinese (Mandarin)**     | cmn-CN        | Zhiyu                                                         | Female                                                         |
| 3   | **Danish**                 | da-DK         | Naja<br>Mads                                                  | Female<br>Male                                                 |
| 4   | **Dutch**                  | nl-NL         | Lotte<br>Ruben                                                | Female<br>Male                                                 |
| 5   | **English (Australian)**   | en-AU         | Nicole<br>Russell                                             | Female<br>Male                                                 |
| 6   | **English (British)**      | en-GB         | Amy<br>Emma<br>Brian                                          | Female<br>Female<br>Male                                       |
| 7   | **English (Indian)**       | en-IN         | Aditi<br>Raveena                                              | Female<br>Female                                               |
| 8   | **English (US)**           | en-US         | Ivy<br>Joanna<br>Kendra<br>Kimberly<br>Salli<br>Joey<br>Kevin | Female<br>Female<br>Female<br>Female<br>Female<br>Male<br>Male |
| 9   | **English (Welsh)**        | en-GB-WLS     | Geraint                                                       | Male                                                           |
| 10  | **French**                 | fr-FR         | Céline/Celine<br>Léa<br>Mathieu                               | Female<br>Female<br>Male                                       |
| 11  | **French (Canadian)**      | fr-CA         | Chantal                                                       | Female                                                         |
| 12  | **German**                 | de-DE         | Marlene<br>Vicki<br>Hans                                      | Female<br>Female<br>Male                                       |
| 13  | **Hindi**                  | hi-IN         | Aditi                                                         | Female                                                         |
| 14  | **Icelandic**              | is-IS         | Dóra/Dora<br>Karl                                             | Female<br>Male                                                 |
| 15  | **Italian**                | it-IT         | Carla<br>Bianca<br>Giorgio                                    | Female<br>Female<br>Male                                       |
| 16  | **Japanese**               | ja-JP         | Mizuki<br>Takumi                                              | Female<br>Male                                                 |
| 17  | **Korean**                 | ko-KR         | Seoyeon                                                       | Female                                                         |
| 18  | **Norwegian**              | nb-NO         | Liv                                                           | Female                                                         |
| 19  | **Polish**                 | pl-PL         | Ewa<br>Maja<br>Jacek<br>Jan                                   | Female<br>Female<br>Male<br>Male                               |
| 20  | **Portuguese (Brazilian)** | pt-BR         | Camila<br>Vitória/Vitoria<br>Ricardo                          | Female<br>Female<br>Male                                       |
| 21  | **Portuguese (European)**  | pt-PT         | Inês/Ines<br>Cristiano                                        | Female<br>Male                                                 |
| 22  | **Romanian**               | ro-RO         | Carmen                                                        | Female                                                         |
| 23  | **Russian**                | ru-RU         | Tatyana<br>Maxim                                              | Female<br>Male                                                 |
| 24  | **Spanish (Spain)**        | es-ES         | Conchita<br>Lucia<br>Enrique                                  | Female<br>Female<br>Male                                       |
| 25  | **Spanish (Mexican)**      | es-MX         | Mia                                                           | Female                                                         |
| 26  | **Spanish (US)**           | es-US         | Lupe<br>Penélope/Penelope<br>Miguel                           | Female<br>Female<br>Male                                       |
| 27  | **Swedish**                | sv-SE         | Astrid                                                        | Female                                                         |
| 28  | **Turkish**                | tr-TR         | Filiz                                                         | Male                                                           |
| 29  | **Welsh**                  | cy-GB         | Gwyneth                                                       | Female                                                         |

## Feature and region compatibility

Amazon Polly standard voices are available in the following Amazon Polly regions:

- US East (N. Virginia): us-east-1
- US East (Ohio): us-east-2
- US West (N. California): us-west-1
- US West (Oregon): us-west-2
- Africa (Cape Town): af-south-1
- Asia Pacific (Hong Kong): ap-east-1
- Asia Pacific (Tokyo): ap-northeast-1
- Asia Pacific (Seoul): ap-northeast-2
- Asia Pacific (Osaka): ap-northeast-3
- Asia Pacific (Mumbai): ap-south-1
- Asia Pacific (Singapore): ap-southeast-1
- Asia Pacific (Sydney): ap-southeast-2
- Asia Pacific (Malaysia): ap-southeast-5
- China (Ningxia): cn-northwest-1;
- Canada (Central): ca-central-1
- Europe (Frankfurt): eu-central-1
- Europe (Ireland): eu-west-1
- Europe (London): eu-west-2
- Europe (Paris): eu-west-3
- Europe (Spain): eu-south-2
- Europe (Stockholm): eu-north-1
- Middle East (Bahrain): me-south-1
- South America (São Paulo): sa-east-1
- AWS GovCloud (US-West): us-gov-west-1

Endpoints and protocols for these Regions are identical to those used for Neural
voices. For more information, see [Amazon Polly endpoints and
quotas](../../../general/latest/gr/pol.md "../../../general/latest/gr/pol.md").

**The Amazon Polly standard engine supports the following
features (TBD):**

- Real-time and asynchronous speech synthesis operations.
- All [speech marks](speechmarks.md "speechmarks.md").
- Many (but not all) SSML tags are supported by Amazon Polly. For more
  information about NTTS-supported SSML tags, see [Supported SSML tags](supportedtags.md "supportedtags.md").
- You can choose from various sampling rates to optimize the bandwidth and
  audio quality for your application. The default sampling rates for standard
  voices are 22 kHz. Amazon Polly supports MP3, OGG (Vorbis), and raw PCM audio
  stream formats.

###### Note

Standard voices cost is specified on the [Amazon Polly pricing information page](https://aws.amazon.com/polly/pricing/ "https://aws.amazon.com/polly/pricing/").
