# Resolve ambiguous user inputs with Intent Disambiguation

Intent Disambiguation is an improvement to Assisted NLU that helps resolve ambiguous user inputs when multiple intents could match. When enabled, the system presents clarifying questions to users, helping them specify their exact intent for improved conversation accuracy. The system uses a large language model (LLM) that analyzes the intent names and descriptions as context, and based on the ambiguity of the user utterance, returns the most likely matching intents. The LLM evaluates whether the user input clearly matches a single intent or multiple intents and is ambiguous enough to require disambiguation, then provides the candidate intents.

The Intent Disambiguation feature is available in English, Spanish, Portuguese, Catalan, French, Italian, German, Chinese, Japanese, and Korean locales. Specifically, it supports locales that begin with `en_`, `es_`, `pt_` (pt_BR, pt_PT), `ca_` (ca_ES), `fr_` (fr_CA, fr_FR), `it_` (it_IT), `de_` (de_AT, de_DE), `zh_` (zh_CN, zh_HK), `ja_JP`, and `ko_KR`. For the complete list of supported locales, see the table in [Languages and locales supported by
Amazon Lex V2](how-languages.md "how-languages.md").

You can configure the following options for Intent Disambiguation:

**Number of Intent Options**

Configure the maximum number of intents (2-5) to present to users when disambiguation is needed. This setting determines how many intent options will be shown to users when the system detects ambiguous input. The default value is 3, which provides a good balance between giving users sufficient options while keeping the selection manageable.

**Disambiguation Message**

Provide a custom message that will be displayed before presenting the disambiguation options to users. This message helps set the context for users and can be customized to match your bot's tone and brand. If not specified, a default message will be used.

**Intent Display Names**

Configure user-friendly display names for your intents to improve the disambiguation experience. This is recommended when your intent names are technical or not suitable for display to end users. Display names will be shown to users during disambiguation instead of the technical intent name.

Console
**Using Intent Disambiguation with your Amazon Lex V2 bot**

1. Sign in to the AWS Management Console and open the Amazon Lex V2 console at [https://console.aws.amazon.com/lexv2/home](https://console.aws.amazon.com/lexv2/home "https://console.aws.amazon.com/lexv2/home").
2. In the **Bots** page, select the bot you want to use with Intent Disambiguation.
3. On the **Bot Locale** page, click on **Configure** under the **Assisted NLU** section.
4. Enable [Assisted NLU](assisted-nlu.md "assisted-nlu.md") and select either Primary or Fallback mode (Intent Disambiguation works with both modes).
5. In the **Intent Disambiguation** section within the Assisted NLU configuration, use the toggle button to enable the Intent Disambiguation feature.
6. Configure the following optional settings:
   - **Number of Intent options:** Select the maximum number of intents (2-5) to present to users during disambiguation. Default is 3.
   - **Disambiguation Message:** Provide a custom message that will be displayed when presenting intent options. If not specified, a default message will be used.

7. Click **Save** to apply the configuration.
8. Optionally configure Intent Display Names for better user experience:
   1. Navigate to each intent in your bot that you want to configure.
   2. In the Intent Editor Page, locate the **Display name** field.
   3. Enter a user-friendly name that will be shown to users during disambiguation instead of the Intent name.

9. Build the bot to see the changes reflected in your bot at runtime.

**Guidance to improve the effectiveness of your bot when using the Intent Disambiguation Feature**

The following best practices can help you maximize the effectiveness of the Intent Disambiguation feature:

1. **Clear Intent Names and Descriptions:** Ensure intent names and descriptions are clean, clear and do not overlap with other intents, as these are the main inputs provided to the LLM for disambiguation.
2. **Descriptive Display Names:** If current Intent names are technical, use descriptive display names that clearly communicate the intent's purpose. Display names should resemble or match the intent names.
3. **Appropriate Maximum Intents:** Set max number of intent options based on your preference and testing.
4. **Custom Messages:** Create concise disambiguation messages that acknowledge the user's input and lead to the intent options.
5. **Test Scenarios:** Test with ambiguous utterances to ensure the disambiguation experience feels natural with intent names or intent display names and custom messages, and verify that the correct intent options are being presented during disambiguation prompt.

###### Important

Enable this feature in a draft version of the bot. Test it before using it in a production alias.

## Disabling Intent Disambiguation

To disable the Intent Disambiguation feature, follow these steps:

1. Sign in to the AWS Management Console and open the Amazon Lex V2 console at [https://console.aws.amazon.com/lexv2/home](https://console.aws.amazon.com/lexv2/home "https://console.aws.amazon.com/lexv2/home").
2. In the **Bots** page, select your bot.
3. On the **Bot Locale** page, click on **Configure** under the **Assisted NLU** section.
4. In the **Intent Disambiguation** section within the Assisted NLU configuration, toggle off the Intent Disambiguation feature, and click **Save**.
5. Build the bot to apply the changes.
