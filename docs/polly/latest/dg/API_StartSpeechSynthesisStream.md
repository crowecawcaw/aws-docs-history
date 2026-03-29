# StartSpeechSynthesisStream

Synthesizes UTF-8 input, plain text, or SSML over a bidirectional streaming connection.
Specify synthesis parameters in HTTP/2 headers, send text incrementally as events on the input stream,
and receive synthesized audio as it becomes available.

This operation serves as a bidirectional counterpart to `SynthesizeSpeech`:

- [SynthesizeSpeech](API_SynthesizeSpeech.md "API_SynthesizeSpeech.md")

## Request Syntax

```
POST /v1/synthesisStream HTTP/1.1
x-amzn-Engine: `Engine`
x-amzn-LanguageCode: `LanguageCode`
x-amzn-LexiconNames: `LexiconNames`
x-amzn-OutputFormat: `OutputFormat`
x-amzn-SampleRate: `SampleRate`
x-amzn-VoiceId: `VoiceId`
Content-type: application/json

{
   "CloseStreamEvent": {
   },
   "TextEvent": {
      "FlushStreamConfiguration": {
         "Force": `boolean`
      },
      "Text": "`string`",
      "TextType": "`string`"
   }
}
```

## URI Request Parameters

The request uses the following URI parameters.

**[Engine](#API_StartSpeechSynthesisStream_RequestSyntax "#API_StartSpeechSynthesisStream_RequestSyntax")**

Specifies the engine for Amazon Polly to use when processing input text for speech synthesis.
Currently, only the `generative` engine is supported.
If you specify a voice that the selected engine doesn't support, Amazon Polly returns an error.

Valid Values: `standard | neural | long-form | generative`

Required: Yes

**[LanguageCode](#API_StartSpeechSynthesisStream_RequestSyntax "#API_StartSpeechSynthesisStream_RequestSyntax")**

An optional parameter that sets the language code for the speech synthesis request. Specify this parameter only
when using a bilingual voice. If a bilingual voice is used and no language code is specified, Amazon Polly
uses the default language of the bilingual voice.

Valid Values: `arb | cmn-CN | cy-GB | da-DK | de-DE | en-AU | en-GB | en-GB-WLS | en-IN | en-US | es-ES | es-MX | es-US | fr-CA | fr-FR | is-IS | it-IT | ja-JP | hi-IN | ko-KR | nb-NO | nl-NL | pl-PL | pt-BR | pt-PT | ro-RO | ru-RU | sv-SE | tr-TR | en-NZ | en-ZA | ca-ES | de-AT | yue-CN | ar-AE | fi-FI | en-IE | nl-BE | fr-BE | cs-CZ | de-CH | en-SG`

**[LexiconNames](#API_StartSpeechSynthesisStream_RequestSyntax "#API_StartSpeechSynthesisStream_RequestSyntax")**

The names of one or more pronunciation lexicons for the service to apply
during synthesis. Amazon Polly applies lexicons only when the lexicon language matches the voice language.

Array Members: Maximum number of 5 items.

Pattern: `[0-9A-Za-z]{1,20}`

**[OutputFormat](#API_StartSpeechSynthesisStream_RequestSyntax "#API_StartSpeechSynthesisStream_RequestSyntax")**

The audio format for the synthesized speech. Currently, Amazon Polly does not support JSON speech marks.

Valid Values: `json | mp3 | ogg_opus | ogg_vorbis | pcm`

Required: Yes

**[SampleRate](#API_StartSpeechSynthesisStream_RequestSyntax "#API_StartSpeechSynthesisStream_RequestSyntax")**

The audio frequency, specified in Hz.

**[VoiceId](#API_StartSpeechSynthesisStream_RequestSyntax "#API_StartSpeechSynthesisStream_RequestSyntax")**

The voice to use in synthesis. To get a list of available voice IDs, use the [DescribeVoices](API_DescribeVoices.md "API_DescribeVoices.md") operation.

Valid Values: `Aditi | Amy | Astrid | Bianca | Brian | Camila | Carla | Carmen | Celine | Chantal | Conchita | Cristiano | Dora | Emma | Enrique | Ewa | Filiz | Gabrielle | Geraint | Giorgio | Gwyneth | Hans | Ines | Ivy | Jacek | Jan | Joanna | Joey | Justin | Karl | Kendra | Kevin | Kimberly | Lea | Liv | Lotte | Lucia | Lupe | Mads | Maja | Marlene | Mathieu | Matthew | Maxim | Mia | Miguel | Mizuki | Naja | Nicole | Olivia | Penelope | Raveena | Ricardo | Ruben | Russell | Salli | Seoyeon | Takumi | Tatyana | Vicki | Vitoria | Zeina | Zhiyu | Aria | Ayanda | Arlet | Hannah | Arthur | Daniel | Liam | Pedro | Kajal | Hiujin | Laura | Elin | Ida | Suvi | Ola | Hala | Andres | Sergio | Remi | Adriano | Thiago | Ruth | Stephen | Kazuha | Tomoko | Niamh | Sofie | Lisa | Isabelle | Zayd | Danielle | Gregory | Burcu | Jitka | Sabrina | Jasmine | Jihye | Ambre | Beatrice | Florian | Lennart | Lorenzo | Tiffany`

Required: Yes

## Request Body

The request accepts the following data in JSON format.

**[CloseStreamEvent](#API_StartSpeechSynthesisStream_RequestSyntax "#API_StartSpeechSynthesisStream_RequestSyntax")**

An event indicating the end of the input stream.

Type: [CloseStreamEvent](API_CloseStreamEvent.md "API_CloseStreamEvent.md") object

Required: No

**[TextEvent](#API_StartSpeechSynthesisStream_RequestSyntax "#API_StartSpeechSynthesisStream_RequestSyntax")**

A text event containing content to be synthesized.

Type: [TextEvent](API_TextEvent.md "API_TextEvent.md") object

Required: No

## Response Syntax

```
HTTP/1.1 200
Content-type: application/json

{
   "AudioEvent": {
      "AudioChunk": ***blob***
   },
   "ServiceFailureException": {
   },
   "ServiceQuotaExceededException": {
   },
   "StreamClosedEvent": {
      "RequestCharacters": ***number***
   },
   "ThrottlingException": {
   },
   "ValidationException": {
   }
}
```

## Response Elements

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

**[AudioEvent](#API_StartSpeechSynthesisStream_ResponseSyntax "#API_StartSpeechSynthesisStream_ResponseSyntax")**

An audio event containing synthesized speech.

Type: [AudioEvent](API_AudioEvent.md "API_AudioEvent.md") object

**[ServiceFailureException](#API_StartSpeechSynthesisStream_ResponseSyntax "#API_StartSpeechSynthesisStream_ResponseSyntax")**

An unknown condition has caused a service failure.

Type: Exception

HTTP Status Code: 500

**[ServiceQuotaExceededException](#API_StartSpeechSynthesisStream_ResponseSyntax "#API_StartSpeechSynthesisStream_ResponseSyntax")**

An exception indicating a service quota would be exceeded.

Type: Exception

HTTP Status Code: 402

**[StreamClosedEvent](#API_StartSpeechSynthesisStream_ResponseSyntax "#API_StartSpeechSynthesisStream_ResponseSyntax")**

An event, with summary information, indicating the stream has closed.

Type: [StreamClosedEvent](API_StreamClosedEvent.md "API_StreamClosedEvent.md") object

**[ThrottlingException](#API_StartSpeechSynthesisStream_ResponseSyntax "#API_StartSpeechSynthesisStream_ResponseSyntax")**

An exception indicating the request was throttled.

Type: Exception

HTTP Status Code: 400

**[ValidationException](#API_StartSpeechSynthesisStream_ResponseSyntax "#API_StartSpeechSynthesisStream_ResponseSyntax")**

An exception indicating the input failed validation.

Type: Exception

HTTP Status Code: 400

## Errors

**ServiceFailureException**

An unknown condition has caused a service failure.

HTTP Status Code: 500

**ServiceQuotaExceededException**

The request would cause a service quota to be exceeded.

**quotaCode**

The quota code identifying the specific quota.

**serviceCode**

The service code identifying the originating service.

HTTP Status Code: 402

**ThrottlingException**

The request was denied because of request throttling.

**throttlingReasons**

A list of reasons explaining why the request was throttled.

HTTP Status Code: 400

**ValidationException**

The input fails to satisfy the constraints specified by the service.

**fields**

The fields that caused the validation error.

**reason**

The reason the request failed validation.

HTTP Status Code: 400

## See Also

For more information about using this API in one of the language-specific AWS SDKs, see the following:

- [AWS Command Line Interface V2](../../../goto/cli2/polly-2016-06-10/StartSpeechSynthesisStream.md "../../../goto/cli2/polly-2016-06-10/StartSpeechSynthesisStream.md")
- [AWS SDK for .NET V4](../../../goto/DotNetSDKV4/polly-2016-06-10/StartSpeechSynthesisStream.md "../../../goto/DotNetSDKV4/polly-2016-06-10/StartSpeechSynthesisStream.md")
- [AWS SDK for C++](../../../goto/SdkForCpp/polly-2016-06-10/StartSpeechSynthesisStream.md "../../../goto/SdkForCpp/polly-2016-06-10/StartSpeechSynthesisStream.md")
- [AWS SDK for Go v2](../../../goto/SdkForGoV2/polly-2016-06-10/StartSpeechSynthesisStream.md "../../../goto/SdkForGoV2/polly-2016-06-10/StartSpeechSynthesisStream.md")
- [AWS SDK for Java V2](../../../goto/SdkForJavaV2/polly-2016-06-10/StartSpeechSynthesisStream.md "../../../goto/SdkForJavaV2/polly-2016-06-10/StartSpeechSynthesisStream.md")
- [AWS SDK for JavaScript V3](../../../goto/SdkForJavaScriptV3/polly-2016-06-10/StartSpeechSynthesisStream.md "../../../goto/SdkForJavaScriptV3/polly-2016-06-10/StartSpeechSynthesisStream.md")
- [AWS SDK for Kotlin](../../../goto/SdkForKotlin/polly-2016-06-10/StartSpeechSynthesisStream.md "../../../goto/SdkForKotlin/polly-2016-06-10/StartSpeechSynthesisStream.md")
- [AWS SDK for PHP V3](../../../goto/SdkForPHPV3/polly-2016-06-10/StartSpeechSynthesisStream.md "../../../goto/SdkForPHPV3/polly-2016-06-10/StartSpeechSynthesisStream.md")
- [AWS SDK for Python](../../../goto/boto3/polly-2016-06-10/StartSpeechSynthesisStream.md "../../../goto/boto3/polly-2016-06-10/StartSpeechSynthesisStream.md")
- [AWS SDK for Ruby V3](../../../goto/SdkForRubyV3/polly-2016-06-10/StartSpeechSynthesisStream.md "../../../goto/SdkForRubyV3/polly-2016-06-10/StartSpeechSynthesisStream.md")
