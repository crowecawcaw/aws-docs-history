# Set the language for

Amazon Q in Connect

You can set up Amazon Q in Connect so agents can ask Q for assistance in the [language](supported-languages.md#supported-languages-contact-lens "supported-languages.md#supported-languages-contact-lens") of your choice. Amazon Q in Connect
then provides answers and recommended step-by-step guides in that language.

###### To set the locale

1. Log in to the Amazon Connect admin website at https://`instance
name`.my.connect.aws/. Use an admin account, or an account with
   **Amazon Q** - **AI agents** -
   **Create** or **Edit** permission in it's
   security profile.
2. On the navigation menu, choose **Amazon Q**, **AI
   agents**.
3. On the **AI Agents** page, choose **Create AI
   Agent** and choose **Answer recommendation**,
   **Manual search**, **Email response**,
   **Email overview**, and **Email generative
   answer** for the AI agent type. Or choose an existing customized
   manual AI agent you want to edit.
4. On the AI agent builder page, use the _Locale_ dropdown
   menu to choose your locale.
5. Choose **Save**, and then choose **Publish**
   to create a version of the AI agent.
6. In the **Defaults** section of the page, choose the new AI
   agent version as a default for the appropriate use case.

## CLI command to set the locale

Use the following sample AWS CLI command to set the locale of a **Manual
search** AI agent.

```
{
    ...
    "configuration": {
        "manualSearchAIAgentConfiguration**"**: {
            ...
            "locale": "es_ES"
        }
    },
    ...
}
```

## Supported locale codes

Amazon Q in Connect supports agent assistance uses cases in the following locales:

- Afrikaans (South Africa) / af_ZA
- Arabic (General) / ar
- Arabic (United Arab Emirates, Gulf) / ar_AE
- Armenian (Armenia) / hy_AM
- Bulgarian (Bulgaria) / bg_BG
- Catalan (Spain) / ca_ES
- Chinese (China, Mandarin) / zh_CN
- Chinese (Hong Kong, Cantonese) / zh_HK
- Czech (Czech Republic) / cs_CZ
- Danish (Denmark) / da_DK
- Dutch (Belgium) / nl_BE
- Dutch (Netherlands) / nl_NL
- English (Australia) / en_AU
- English (India) / en_IN
- English (Ireland) / en_IE
- English (New Zealand) / en_NZ
- English (Singapore) / en_SG
- English (South Africa) / en_ZA
- English (United Kingdom) / en_GB
- English (United States) / en_US
- English (Wales) / en_CY
- Estonian (Estonia) / et_EE
- Farsi (Iran) / fa_IR
- Finnish (Finland) / fi_FI
- French (Belgium) / fr_BE
- French (Canada) / fr_CA
- French (France) / fr_FR
- Gaelic (Ireland) / ga_IE
- German (Austria) / de_AT
- German (Germany) / de_DE
- German (Switzerland) / de_CH
- Hebrew (Israel) / he_IL
- Hindi (India) / hi_IN
- Hmong (General) / hmn
- Hungarian (Hungary) / hu_HU
- Icelandic (Iceland) / is_IS
- Indonesian (Indonesia) / id_ID
- Italian (Italy) / it_IT
- Japanese (Japan) / ja_JP
- Khmer (Cambodia) / km_KH
- Korean (South Korea) / ko_KR
- Lao (Laos) / lo_LA
- Latvian (Latvia) / lv_LV
- Lithuanian (Lithuania) / lt_LT
- Malay (Malaysia) / ms_MY
- Norwegian (Norway) / no_NO
- Polish (Poland) / pl_PL
- Portuguese (Brazil) / pt_BR
- Portuguese (Portugal) / pt_PT
- Romanian (Romania) / ro_RO
- Russian (Russia) / ru_RU
- Serbian (Serbia) / sr_RS
- Slovak (Slovakia) / sk_SK
- Slovenian (Slovenia) / sl_SI
- Spanish (Mexico) / es_MX
- Spanish (Spain) / es_ES
- Spanish (United States) / es_US
- Swedish (Sweden) / sv_SE
- Tagalog (Philippines) / tl_PH
- Thai (Thailand) / th_TH
- Turkish (Turkey) / tr_TR
- Vietnamese (Vietnam) / vi_VN
- Welsh (United Kingdom) / cy_GB
- Xhosa (South Africa) / xh_ZA
- Zulu (South Africa) / zu_ZA
