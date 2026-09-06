

# Supported languages and language-specific features
<a name="supported-languages"></a>

The languages supported by Amazon Transcribe are listed in the following table; also listed are the features that are language-specific. Please verify that the feature you want to use is supported for the language in your media before proceeding with your transcription.

To view the complete list of Amazon Transcribe features, refer to the [Feature summary](feature-matrix.md).

In the following table, 'batch' refers to transcribing a media file located in an Amazon S3 bucket and 'streaming' refers to transcribing streamed media in real time. For Call Analytics transcriptions, 'post-call' refers to transcribing a media file located in an Amazon S3 bucket and 'real-time' refers to transcribing streamed media in real time.


|  **Language**  |  **Language code**  |  **[Data input](how-input.md)**  |  **[Transcribing numbers](how-numbers.md)**  |  **[Acronyms](custom-vocabulary-create-table.md)**  |  **[Custom language models](custom-language-models.md)**  |  **[Redaction](pii-redaction.md)**  |  **[Call Analytics\*](call-analytics.md)**  | 
| --- | --- | --- | --- | --- | --- | --- | --- | 
| [Abkhaz](charsets.md#char-abkhaz) | ab-GE | batch | no | batch | no | no | no | 
| [Afrikaans](charsets.md#char-afrikaans) | af-ZA | batch, streaming | no | batch, streaming | no | no | no | 
| Albanian | sq-AL | batch, streaming\* | no | batch, streaming\* | no | no | no | 
| Amharic | am-ET | batch, streaming\* | no | batch, streaming\* | no | no | no | 
| [Arabic](charsets.md#char-arabic), Gulf | ar-AE | batch, streaming | batch, streaming | no | no | no | post-call | 
| [Arabic](charsets.md#char-arabic), Modern Standard | ar-SA | batch, streaming | streaming | no | no | no | no | 
| [Armenian](charsets.md#char-armenian) | hy-AM | batch, streaming\* | no | batch, streaming\* | no | no | no | 
| [Asturian](charsets.md#char-asturian) | ast-ES | batch | no | batch | no | no | no | 
| [Azerbaijani](charsets.md#char-azerbaijani) | az-AZ | batch | no | batch | no | no | no | 
| [Bashkir](charsets.md#char-bashkir) | ba-RU | batch | no | batch | no | no | no | 
| [Basque](charsets.md#char-basque) | eu-ES | batch, streaming | no | batch, streaming | no | no | no | 
| [Belarusian](charsets.md#char-belarusian) | be-BY | batch, streaming\* | no | batch, streaming\* | no | no | no | 
| [Bengali](charsets.md#char-bengali) | bn-IN | batch, streaming\* | batch, streaming\* | batch, streaming\* | no | no | no | 
| [Bosnian](charsets.md#char-bosnian) | bs-BA | batch, streaming\* | no | batch, streaming\* | no | no | no | 
| Burmese | my-MM | batch, streaming\* | no | batch, streaming\* | no | no | no | 
| [Bulgarian](charsets.md#char-bulgarian) | bg-BG | batch, streaming\* | no | batch, streaming\* | no | no | no | 
| [Catalan](charsets.md#char-catalan) | ca-ES | batch, streaming | streaming | batch, streaming | no | no | no | 
| [Central Kurdish](charsets.md#char-central-kurdish), Iran | ckb-IR | batch, streaming\* | no | batch, streaming\* | no | no | no | 
| [Central Kurdish](charsets.md#char-central-kurdish), Iraq | ckb-IQ | batch, streaming\* | no | batch, streaming\* | no | no | no | 
| [Chinese, Cantonese](charsets.md#char-cantonese-hk) | zh-HK (yue-HK) | batch, streaming | batch, streaming | no | no | no | no | 
| [Chinese, Simplified](charsets.md#char-chinese-man-cn) | zh-CN | batch, streaming | batch, streaming | no | no | no | post-call | 
| [Chinese, Traditional](charsets.md#char-chinese-man-tw) | zh-TW | batch, streaming | batch, streaming | no | no | no | no | 
| [Croatian](charsets.md#char-croatian) | hr-HR | batch, streaming | no | batch, streaming | no | no | no | 
| [Czech](charsets.md#char-czech) | cs-CZ | batch, streaming | no | batch, streaming | no | no | no | 
| [Danish](charsets.md#char-danish) | da-DK | batch, streaming | batch, streaming | batch, streaming | no | no | no | 
| [Dutch](charsets.md#char-dutch) | nl-NL | batch, streaming | batch, streaming | batch, streaming | no | no | no | 
| [English](charsets.md#char-english), Australian | en-AU | batch, streaming | batch, streaming | batch, streaming | batch, streaming | batch, streaming | post-call, real-time | 
| [English](charsets.md#char-english), British | en-GB | batch, streaming | batch, streaming | batch, streaming | batch, streaming | batch, streaming | post-call, real-time | 
| [English](charsets.md#char-english), Indian | en-IN | batch, streaming | batch, streaming | batch, streaming | no | batch, streaming | post-call | 
| [English](charsets.md#char-english), Irish | en-IE | batch, streaming | batch, streaming | batch, streaming | no | batch, streaming | post-call | 
| [English](charsets.md#char-english), New Zealand | en-NZ | batch, streaming | batch, streaming | batch, streaming | no | batch, streaming | no | 
| [English](charsets.md#char-english), Scottish | en-AB | batch, streaming | batch, streaming | batch, streaming | no | batch, streaming | post-call | 
| [English](charsets.md#char-english), South African | en-ZA | batch, streaming | batch, streaming | batch, streaming | no | batch, streaming | no | 
| [English](charsets.md#char-english), US | en-US | batch, streaming | batch, streaming | batch, streaming | batch, streaming | batch, streaming | post-call, real-time | 
| [English](charsets.md#char-english), Welsh | en-WL | batch, streaming | batch, streaming | batch, streaming | no | batch, streaming | post-call | 
| [Estonian](charsets.md#char-estonian) | et-EE | batch | no | batch | no | no | no | 
| [Estonian](charsets.md#char-estonian) | et-ET | batch, streaming\* | no | batch, streaming\* | no | no | no | 
| [Farsi](charsets.md#char-farsi) | fa-IR | batch, streaming | no | no | no | no | no | 
| [Farsi](charsets.md#char-farsi), Afghan | fa-AF | batch, streaming\* | no | batch, streaming\* | no | no | no | 
| [Finnish](charsets.md#char-finnish) | fi-FI | batch, streaming | no | batch, streaming | no | no | no | 
| [French](charsets.md#char-french) | fr-FR | batch, streaming | batch, streaming | batch, streaming | no | batch, streaming | post-call, real-time | 
| [French](charsets.md#char-french), Canadian | fr-CA | batch, streaming | batch, streaming | batch, streaming | no | batch, streaming | post-call, real-time | 
| [Galician](charsets.md#char-galician) | gl-ES | batch, streaming | no | batch, streaming | no | no | no | 
| [Georgian](charsets.md#char-georgian) | ka-GE | batch, streaming\* | no | batch, streaming\* | no | no | no | 
| [German](charsets.md#char-german) | de-DE | batch, streaming | batch, streaming | batch, streaming | batch, streaming | batch, streaming | post-call, real-time | 
| [German](charsets.md#char-german), Swiss | de-CH | batch, streaming | batch, streaming | batch, streaming | no | batch, streaming | post-call | 
| [Greek](charsets.md#char-greek) | el-GR | batch, streaming | no | batch, streaming | no | no | no | 
| [Gujarati](charsets.md#char-gujarati) | gu-IN | batch, streaming\* | no | batch, streaming\* | no | no | no | 
| Haitian Creole | ht-HT | batch, streaming\* | no | batch, streaming\* | no | no | no | 
| [Hausa](charsets.md#char-hausa) | ha-NG | batch | no | batch | no | no | no | 
| [Hebrew](charsets.md#char-hebrew) | he-IL | batch, streaming | batch, streaming | no | no | no | no | 
| [Hindi](charsets.md#char-hindi), Indian | hi-IN | batch, streaming | batch, streaming | batch, streaming | batch | no | post-call | 
| [Hungarian](charsets.md#char-hungarian) | hu-HU | batch, streaming\* | no | batch, streaming\* | no | no | no | 
| [Icelandic](charsets.md#char-icelandic) | is-IS | batch, streaming\* | no | batch, streaming\* | no | no | no | 
| [Indonesian](charsets.md#char-indonesian) | id-ID | batch, streaming | batch, streaming | batch, streaming | no | no | no | 
| [Italian](charsets.md#char-italian) | it-IT | batch, streaming | batch, streaming | batch, streaming | no | batch, streaming | post-call, real-time | 
| [Japanese](charsets.md#char-japanese) | ja-JP | batch, streaming | batch, streaming | no | batch, streaming | no | post-call | 
| Javanese | jv-ID | batch, streaming\* | no | batch, streaming\* | no | no | no | 
| [Kabyle](charsets.md#char-kabyle) | kab-DZ | batch, streaming\* | no | batch, streaming\* | no | no | no | 
| [Kannada](charsets.md#char-kannada) | kn-IN | batch, streaming\* | no | batch, streaming\* | no | no | no | 
| [Kazakh](charsets.md#char-kazakh) | kk-KZ | batch, streaming\* | no | batch, streaming\* | no | no | no | 
| Khmer | km-KH | batch, streaming\* | no | batch, streaming\* | no | no | no | 
| [Kinyarwanda](charsets.md#char-kinyarwanda) | rw-RW | batch | no | batch | no | no | no | 
| [Korean](charsets.md#char-korean) | ko-KR | batch, streaming | batch, streaming | batch, streaming | no | no | post-call | 
| [Kyrgyz](charsets.md#char-kyrgyz) | ky-KG | batch | no | batch | no | no | no | 
| [Latvian](charsets.md#char-latvian) | lv-LV | batch, streaming | no | batch, streaming | no | no | no | 
| [Lithuanian](charsets.md#char-lithuanian) | lt-LT | batch, streaming\* | no | batch, streaming\* | no | no | no | 
| [Luganda](charsets.md#char-luganda) | lg-IN | batch, streaming\* | no | batch, streaming\* | no | no | no | 
| [Macedonian](charsets.md#char-macedonian) | mk-MK | batch, streaming\* | no | batch, streaming\* | no | no | no | 
| [Malay](charsets.md#char-malay) | ms-MY | batch, streaming | no | batch, streaming | no | no | no | 
| [Malayalam](charsets.md#char-malayalam) | ml-IN | batch, streaming\* | no | batch, streaming\* | no | no | no | 
| [Maltese](charsets.md#char-maltese) | mt-MT | batch | no | batch | no | no | no | 
| [Marathi](charsets.md#char-marathi) | mr-IN | batch, streaming\* | no | batch, streaming\* | no | no | no | 
| [Meadow Mari](charsets.md#char-meadow-mari) | mhr-RU | batch | no | batch | no | no | no | 
| [Mongolian](charsets.md#char-mongolian) | mn-MN | batch | no | batch | no | no | no | 
| Nepali | ne-NP | batch, streaming\* | no | batch, streaming\* | no | no | no | 
| [Norwegian Bokmål](charsets.md#char-norwegian-bokmal) | no-NO | batch, streaming | batch | batch, streaming | no | no | no | 
| [Odia/Oriya](charsets.md#char-odia-oriya) | or-IN | batch, streaming\* | no | batch, streaming\* | no | no | no | 
| [Pashto](charsets.md#char-pashto) | ps-AF | batch, streaming\* | no | batch, streaming\* | no | no | no | 
| [Polish](charsets.md#char-polish) | pl-PL | batch, streaming | batch, streaming | batch, streaming | no | no | no | 
| [Portuguese](charsets.md#char-portuguese) | pt-PT | batch, streaming | batch, streaming | batch, streaming | no | batch, streaming | post-call | 
| [Portuguese](charsets.md#char-portuguese), Brazilian | pt-BR | batch, streaming | batch, streaming | batch, streaming | no | batch, streaming | post-call, real-time | 
| [Punjabi](charsets.md#char-punjabi) | pa-IN | batch, streaming\* | no | batch, streaming\* | no | no | no | 
| [Romanian](charsets.md#char-romanian) | ro-RO | batch, streaming | batch, streaming | batch, streaming | no | no | no | 
| [Russian](charsets.md#char-russian) | ru-RU | batch, streaming | batch, streaming | batch, streaming | no | no | no | 
| [Serbian](charsets.md#char-serbian) | sr-RS | batch, streaming | no | batch, streaming | no | no | no | 
| [Sinhala](charsets.md#char-sinhala) | si-LK | batch, streaming\* | no | batch, streaming\* | no | no | no | 
| [Slovak](charsets.md#char-slovak) | sk-SK | batch, streaming | no | batch, streaming | no | no | no | 
| [Slovenian](charsets.md#char-slovenian) | sl-SI | batch, streaming\* | no | batch, streaming\* | no | no | no | 
| [Somali](charsets.md#char-somali) | so-SO | batch, streaming | batch, streaming | batch, streaming | no | no | no | 
| [Spanish](charsets.md#char-spanish) | es-ES | batch, streaming | batch, streaming | batch, streaming | no | streaming | post-call | 
| [Spanish](charsets.md#char-spanish), Mexican | es-MX | batch, streaming\* | streaming\* | batch, streaming\* | no | no | no | 
| [Spanish](charsets.md#char-spanish), US | es-US | batch, streaming | batch, streaming | batch, streaming | batch, streaming | batch, streaming | post-call, real-time | 
| [Sundanese](charsets.md#char-sundanese) | su-ID | batch, streaming\* | no | batch, streaming\* | no | no | no | 
| [Swahili](charsets.md#char-swahili), Kenya | sw-KE | batch, streaming\* | batch, streaming\* | batch, streaming\* | no | no | no | 
| [Swahili](charsets.md#char-swahili), Burundi | sw-BI | batch, streaming\* | batch | batch, streaming\* | no | no | no | 
| [Swahili](charsets.md#char-swahili), Rwanda | sw-RW | batch, streaming\* | batch | batch, streaming\* | no | no | no | 
| [Swahili](charsets.md#char-swahili), Tanzania | sw-TZ | batch, streaming\* | batch | batch, streaming\* | no | no | no | 
| [Swahili](charsets.md#char-swahili), Uganda | sw-UG | batch, streaming\* | batch | batch, streaming\* | no | no | no | 
| [Swedish](charsets.md#char-swedish) | sv-SE | batch, streaming | batch, streaming | batch, streaming | no | no | no | 
| [Tagalog/Filipino](charsets.md#char-tagalog-filipino) | tl-PH | batch, streaming | batch, streaming | batch, streaming | no | no | no | 
| [Tamil](charsets.md#char-tamil) | ta-IN | batch, streaming\* | batch, streaming\* | streaming\* | no | no | no | 
| [Tatar](charsets.md#char-tatar) | tt-RU | batch | no | batch | no | no | no | 
| [Telugu](charsets.md#char-telugu) | te-IN | batch, streaming\* | no | streaming\* | no | no | no | 
| [Thai](charsets.md#char-thai) | th-TH | batch, streaming | batch | batch, streaming | no | no | no | 
| [Turkish](charsets.md#char-turkish) | tr-TR | batch, streaming\* | batch, streaming\* | batch, streaming\* | no | no | no | 
| [Ukrainian](charsets.md#char-ukrainian) | uk-UA | batch, streaming | batch, streaming | batch, streaming | no | no | no | 
| [Uyghur](charsets.md#char-uyghur) | ug-CN | batch | no | batch | no | no | no | 
| [Uzbek](charsets.md#char-uzbek) | uz-UZ | batch, streaming\* | no | batch, streaming\* | no | no | no | 
| [Vietnamese](charsets.md#char-vietnamese) | vi-VN | batch, streaming | batch | batch, streaming | no | no | no | 
| [Welsh](charsets.md#char-welsh) | cy-WL | batch, streaming\* | no | batch, streaming\* | no | no | no | 
| [Wolof](charsets.md#char-wolof) | wo-SN | batch | no | batch | no | no | no | 
| [Zulu](charsets.md#char-zulu) | zu-ZA | batch, streaming | no | batch, streaming | no | no | no | 

\*Streaming for these languages is not available in the following AWS Regions: af-south-1 (Cape Town), ap-northeast-1 (Tokyo), ap-southeast-5 (Malaysia), ap-southeast-7 (Thailand), and cn-northwest-1 (Ningxia).

\*The following Call Analytics insights are only supported in select English dialects:
+ [Call summarization](call-analytics-batch.md#tca-summarization-batch): `en-*` (all English dialects)
+ [Issue detection](call-analytics-streaming.md#tca-issue-detection-stream): `en-AU`, `en-GB`, `en-US`

## Supported programming languages
<a name="supported-sdks"></a>

Amazon Transcribe supports the following AWS SDKs:


| Batch transcriptions | Streaming transcriptions | 
| --- | --- | 
| [.NET](https://docs.aws.amazon.com/sdkfornet/v4/apidocs/items/TranscribeService/NTranscribeService.html) | [.NET](https://docs.aws.amazon.com/sdkfornet/v4/apidocs/items/TranscribeStreaming/NTranscribeStreaming.html) (Transcribe Medical and HealthScribe is not supported) | 
| [AWS Command Line Interface (CLI)](https://docs.aws.amazon.com/cli/latest/reference/transcribe/index.html#cli-aws-transcribe) | The CLI is not supported for streaming. | 
| [C\+\+](https://sdk.amazonaws.com/cpp/api/LATEST/namespace_aws_1_1_transcribe_service.html) | [C\+\+](https://github.com/aws/aws-sdk-cpp/tree/master/aws-cpp-sdk-transcribestreaming) | 
| [Go](https://docs.aws.amazon.com/sdk-for-go/api/service/transcribeservice/) | [Go](https://docs.aws.amazon.com/sdk-for-go/api/service/transcribestreamingservice/) | 
| [Java V2](https://sdk.amazonaws.com/java/api/latest/software/amazon/awssdk/services/transcribe/TranscribeClient.html) | [Java V2](https://github.com/aws/aws-sdk-java-v2/tree/master/services/transcribestreaming) | 
| [JavaScript](https://docs.aws.amazon.com/AWSJavaScriptSDK/latest/AWS/TranscribeService.html) | [JavaScript V3](https://github.com/aws/aws-sdk-js-v3/tree/master/clients/client-transcribe-streaming) | 
| [PHP V3](https://docs.aws.amazon.com/aws-sdk-php/v3/api/namespace-Aws.TranscribeService.html) | The SDK is not supported for streaming. | 
| [Python Boto3](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/transcribe.html) | [Python Streaming SDK for Amazon Transcribe](https://github.com/awslabs/amazon-transcribe-streaming-sdk) | 
| [Ruby V3](https://docs.aws.amazon.com/sdk-for-ruby/v3/api/Aws/TranscribeService.html) | [Ruby V3](https://github.com/aws/aws-sdk-ruby/tree/version-3/gems/aws-sdk-transcribestreamingservice) | 
| [Rust](https://crates.io/crates/aws-sdk-transcribe) | [Rust](https://crates.io/crates/aws-sdk-transcribestreaming) | 

For information on using SDKs with Amazon Transcribe, refer to [Transcribing with the AWS SDKs](getting-started-sdk.md).

For more information on all available AWS SDKs and builder tools, refer to [Tools to Build on AWS](https://aws.amazon.com/developer/tools).

**Tip**  
You can find SDK code samples in these GitHub repositories:  
[AWS Code Examples](https://github.com/aws-samples)
[Amazon Transcribe Examples](https://github.com/aws-samples/amazon-transcribe-examples)