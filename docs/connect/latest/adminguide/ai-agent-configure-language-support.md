

# Set languages
<a name="ai-agent-configure-language-support"></a>

Agents can ask for assistance in the [language](supported-languages.md#supported-languages-contact-lens) of your choice when you set the locale on AI agents. AI agents then provide answers and recommended step-by-step guides in that language.

**To set the locale**

1. On the AI agent builder page, use the Locale dropdown menu to choose your locale.

1. Choose **Save**, and then choose **Publish** to create a version of the AI agent.

## CLI command to set the locale
<a name="cli-set-qic-locale"></a>

Use the following sample AWS CLI command to set the locale of a **Manual search** AI agent.

```
{
    ...
    "configuration": {
        "manualSearchAIAgentConfiguration": {
            ...
            "locale": "es_ES"
        }
    },
    ...
}
```

## Supported locale codes
<a name="supported-locale-codes-q"></a>

AI agents support the following locales for agent assistance:
+  Afrikaans (South Africa) / af\_ZA 
+  Arabic (General) / ar 
+  Arabic (United Arab Emirates, Gulf) / ar\_AE 
+  Armenian (Armenia) / hy\_AM 
+  Bulgarian (Bulgaria) / bg\_BG 
+  Catalan (Spain) / ca\_ES 
+  Chinese (China, Mandarin) / zh\_CN 
+  Chinese (Hong Kong, Cantonese) / zh\_HK 
+  Czech (Czech Republic) / cs\_CZ 
+  Danish (Denmark) / da\_DK 
+  Dutch (Belgium) / nl\_BE 
+  Dutch (Netherlands) / nl\_NL 
+  English (Australia) / en\_AU 
+  English (India) / en\_IN 
+  English (Ireland) / en\_IE 
+  English (New Zealand) / en\_NZ 
+  English (Singapore) / en\_SG 
+  English (South Africa) / en\_ZA 
+  English (United Kingdom) / en\_GB 
+  English (United States) / en\_US 
+  English (Wales) / en\_CY 
+  Estonian (Estonia) / et\_EE 
+  Farsi (Iran) / fa\_IR 
+  Finnish (Finland) / fi\_FI 
+  French (Belgium) / fr\_BE 
+  French (Canada) / fr\_CA 
+  French (France) / fr\_FR 
+  Gaelic (Ireland) / ga\_IE 
+  German (Austria) / de\_AT 
+  German (Germany) / de\_DE 
+  German (Switzerland) / de\_CH 
+  Hebrew (Israel) / he\_IL 
+  Hindi (India) / hi\_IN 
+  Hmong (General) / hmn 
+  Hungarian (Hungary) / hu\_HU 
+  Icelandic (Iceland) / is\_IS 
+  Indonesian (Indonesia) / id\_ID 
+  Italian (Italy) / it\_IT 
+  Japanese (Japan) / ja\_JP 
+  Khmer (Cambodia) / km\_KH 
+  Korean (South Korea) / ko\_KR 
+  Lao (Laos) / lo\_LA 
+  Latvian (Latvia) / lv\_LV 
+  Lithuanian (Lithuania) / lt\_LT 
+  Malay (Malaysia) / ms\_MY 
+  Norwegian (Norway) / no\_NO 
+  Polish (Poland) / pl\_PL 
+  Portuguese (Brazil) / pt\_BR 
+  Portuguese (Portugal) / pt\_PT 
+  Romanian (Romania) / ro\_RO 
+  Russian (Russia) / ru\_RU 
+  Serbian (Serbia) / sr\_RS 
+  Slovak (Slovakia) / sk\_SK 
+  Slovenian (Slovenia) / sl\_SI 
+  Spanish (Mexico) / es\_MX 
+  Spanish (Spain) / es\_ES 
+  Spanish (United States) / es\_US 
+  Swedish (Sweden) / sv\_SE 
+  Tagalog (Philippines) / tl\_PH 
+  Thai (Thailand) / th\_TH 
+  Turkish (Turkey) / tr\_TR 
+  Vietnamese (Vietnam) / vi\_VN 
+  Welsh (United Kingdom) / cy\_GB 
+  Xhosa (South Africa) / xh\_ZA 
+  Zulu (South Africa) / zu\_ZA 