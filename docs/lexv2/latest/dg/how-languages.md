

# Languages and locales supported by Amazon Lex V2
<a name="how-languages"></a>

Amazon Lex V2 supports a variety of languages and locales. This topic lists the languages that are supported and the features that support these languages.

## Supported languages and locales
<a name="supported-languages"></a>

Amazon Lex V2 supports the following languages and locales.


| Code | Language and locale | 
| --- | --- | 
| af\_ZA\* | Afrikaans (South Africa) | 
| ar\_AE | Gulf Arabic (United Arab Emirates) | 
| ar\_SA\* | Arabic (Saudi Arabia) | 
| bg\_BG\* | Bulgarian (Bulgaria) | 
| ca\_ES | Catalan (Spain) | 
| cs\_CZ\* | Czech (Czech Republic) | 
| cy\_GB\* | Welsh (United Kingdom) | 
| da\_DK\* | Danish (Denmark) | 
| de\_AT | German (Austria) | 
| de\_CH\* | German (Switzerland) | 
| de\_DE | German (Germany) | 
| en\_AB\* | English (Scotland) | 
| en\_AU | English (Australia) | 
| en\_GB | English (UK) | 
| en\_IE\* | English (Ireland) | 
| en\_IN | English (India) | 
| en\_NZ\* | English (New Zealand) | 
| en\_US | English (US) | 
| en\_WL\* | English (Wales) | 
| en\_ZA | English (South Africa) | 
| es\_419 | Spanish (Latin America) | 
| es\_ES | Spanish (Spain) | 
| es\_MX\* | Spanish (Mexico) | 
| es\_US | Spanish (US) | 
| et\_ET\* | Estonian (Estonia) | 
| fa\_IR\* | Farsi (Iran) | 
| fi\_FI | Finnish (Finland) | 
| fr\_BE\* | French (Belgium) | 
| fr\_CA | French (Canada) | 
| fr\_FR | French (France) | 
| he\_IL\* | Hebrew (Israel) | 
| hi\_IN | Hindi (India) | 
| hr\_HR\* | Croatian (Croatia) | 
| hu\_HU\* | Hungarian (Hungary) | 
| id\_ID\* | Indonesian (Indonesia) | 
| is\_IS\* | Icelandic (Iceland) | 
| it\_IT | Italian (Italy) | 
| ja\_JP | Japanese (Japan) | 
| km\_KH\* | Khmer (Cambodia) | 
| ko\_KR | Korean (Korea) | 
| lt\_LT\* | Lithuanian (Lithuania) | 
| lv\_LV\* | Latvian (Latvia) | 
| ms\_MY\* | Malay (Malaysia) | 
| nl\_BE\* | Dutch (Belgium) | 
| nl\_NL | Dutch (The Netherlands) | 
| no\_NO | Norwegian (Norway) | 
| pl\_PL | Polish (Poland) | 
| pt\_BR | Portuguese (Brazil) | 
| pt\_PT | Portuguese (Portugal) | 
| ro\_RO\* | Romanian (Romania) | 
| ru\_RU\* | Russian (Russia) | 
| sk\_SK\* | Slovak (Slovakia) | 
| sl\_SI\* | Slovenian (Slovenia) | 
| so\_SO\* | Somali (Somalia) | 
| sr\_RS\* | Serbian (Serbia) | 
| su\_ID\* | Sundanese (Indonesia) | 
| sv\_SE | Swedish (Sweden) | 
| th\_TH\* | Thai (Thailand) | 
| tl\_PH\* | Tagalog/Filipino (Philippines) | 
| tr\_TR\* | Turkish (Turkey) | 
| uk\_UA\* | Ukrainian (Ukraine) | 
| vi\_VN\* | Vietnamese (Vietnam) | 
| zh\_CN | Mandarin (PRC) | 
| zh\_HK | Cantonese (Hong Kong) | 
| zu\_ZA\* | Zulu (South Africa) | 

Locales marked with an asterisk (\*) have limited feature support via generative AI and third-party Automatic Speech Recognition (ASR) or Text-To-Speech (TTS). See the following table for a complete list of supported features.

Generative AI feature support includes [Assisted NLU](https://docs.aws.amazon.com/lexv2/latest/dg/assisted-nlu.html) in Primary Mode, [Assisted Slot Resolution](https://docs.aws.amazon.com/lexv2/latest/dg/assisted-slot.html), and [Intent Disambiguation](https://docs.aws.amazon.com/lexv2/latest/dg/generative-intent-disambiguation.html).

## Languages and locales supported by Amazon Lex V2 features
<a name="language-features"></a>

The following table lists Amazon Lex V2 features that are limited to certain languages and locales. All other Amazon Lex V2 features are supported in all languages and locales.


| Feature | Supported languages and locales | 
| --- | --- | 
| [AMAZON.AlphaNumeric](built-in-slot-alphanumeric.md) | All languages and locales except Korean (ko\_KR) and limited feature support locales  | 
| [AMAZON.KendraSearchIntent](built-in-intent-kendra-search.md) | English (US) (en\_US) | 
| [Improving speech recognition with a custom vocabulary](vocab.md) | English (UK) (en\_GB)<br />English (US) (en\_US) | 
| [Automated Chatbot Designer](https://docs.aws.amazon.com/lexv2/latest/dg/designing.html) | English (US) (en\_US) | 
| Region availability | The following languages and locales are not available in the Asia Pacific (Singapore) (ap-southeast-1) and Africa (Cape Town) (ap-south-1) Regions:+  Gulf Arabic (United Arab Emirates) (ar\_AE) <br />+  Catalan (Spain) (ca\_ES) <br />+  Finnish (Finland) (fi\_FI) <br />+  Hindi (India) (hi\_IN) <br />+  Dutch (The Netherlands) (nl\_NL) <br />+  Norwegian (Norway) (no\_NO) <br />+  Polish (pl\_PL) <br />+  Portuguese (Brazil) (pt\_BR) <br />+  Portuguese (Portugal) (pt\_PT) <br />+  Swedish (sv\_SE) <br />+  Mandarin (PRC) (zh\_CN) <br />+  Cantonese (Hong Kong) (zh\_HK)  | 
| [Setting intent context for your Lex V2 bot](context-mgmt-active-context.md) | English (US) (en\_US) | 
| [Grammar slot type](building-srgs.md) | English (Australia) (en\_AU)<br />English (UK) (en\_GB)<br />English (US) (en\_US) | 
| [Using multiple values in a slot](multi-valued-slots.md) | English (US) (en\_US) | 
| [Improving recognition of slot values with runtime hints in the conversation](using-hints.md) | English (UK) (en\_GB)<br />English (US) (en\_US) | 
| [Capturing slot values with spelling styles during the conversation](spelling-styles.md) | English (Australia) (en\_AU)<br />English (UK) (en\_GB)<br />English (US) (en\_US) | 
| [Using confidence scores to improve conversation accuracy](confidence-scores.md) | English (UK) (en\_GB)<br />English (US) (en\_US) | 
| Only with Third-party ASR (Deepgram) | Dutch (Belgium) (nl\_BE)<br />French (Belgium) (fr\_BE) | 
| Only with Third-party TTS (ElevenLabs) | Afrikaans (South Africa) (af\_ZA)<br />Bulgarian (Bulgaria) (bg\_BG)<br />Croatian (Croatia) (hr\_HR)<br />English (Scotland) (en\_AB)<br />Estonian (Estonia) (et\_ET)<br />Farsi (Iran) (fa\_IR)<br />Hebrew (Israel) (he\_IL)<br />Hungarian (Hungary) (hu\_HU)<br />Indonesian (Indonesia) (id\_ID)<br />Latvian (Latvia) (lv\_LV)<br />Lithuanian (Lithuania) (lt\_LT)<br />Malay (Malaysia) (ms\_MY)<br />Serbian (Serbia) (sr\_RS)<br />Slovak (Slovakia) (sk\_SK)<br />Slovenian (Slovenia) (sl\_SI) | 

## Regions
<a name="regions"></a>

For a list of AWS Regions where Amazon Lex V2 is available, see [ AWS regions and endpoints ](https://docs.aws.amazon.com/general/latest/gr/lex.html) in the AWS General Reference.