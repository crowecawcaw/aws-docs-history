

# Improve intent classification and slot resolution in Lex V2 with assisted NLU
<a name="assisted-nlu"></a>

Assisted NLU is a feature that uses Large Language Models (LLMs) to improve Amazon Lex V2's intent classification and slot resolution capabilities. It enhances accuracy while staying within your bot's configured intents and slots. The feature does not generate or modify any bot content. This feature helps to improve the overall accuracy of the NLU system, resulting in a more seamless and effective conversational experience for users.

The assisted NLU feature is available in English, Spanish, Portuguese, Catalan, French, Italian, and German locales. Specifically, it supports locales that begin with `en_`, `es_`, `pt_` (pt\_BR, pt\_PT), `ca_` (ca\_ES), `fr_` (fr\_CA, fr\_FR), `it_` (it\_IT), `de_` (de\_AT, de\_DE), `zh_` (zh\_CN, zh\_HK), `ja_JP`, and `ko_KR`. For the complete list of supported locales, see the table in [Languages and locales supported by Amazon Lex V2](how-languages.md).

Use assisted NLU to improve intent classification and slot resolution. Amazon Lex V2 invokes Amazon Bedrock models to help classify intents and resolve slot types that fit your bot's use case. You can enable assisted NLU for your bot with the console.

**Assisted NLU Mode**

In Primary mode, Lex will default to utilizing the LLM as the primary means of processing the user input to determine the user Intent, as well as to fill slot values.

In Fallback mode, Lex will use the LLM for determining user intent if the confidence score determined by NLU is lower than the configured threshold or otherwise routing to the FallbackIntent, as well as to determine slot values from user inputs if the traditional NLU does not capture a value. 

------
#### [ Console ]

**Using assisted NLU with your Amazon Lex V2 bot**

1. Sign in to the AWS Management Console and open the Amazon Lex V2 console at [https://console.aws.amazon.com/lexv2/home](https://console.aws.amazon.com/lexv2/home).

1. In the **Bots** page, select the bot you want to use with assisted NLU.

1. On the **Bot Locale** page, click on **Configure** under the **Assisted NLU** section.

1. Under the Runtime generative AI features section, you can see the Assisted NLU feature. Use the toggle button beside it to enable LLM Assisted NLU feature. You can then select Primary or Fallback mode, and click **Save**.

1. Verify that the LLM Assisted NLU feature is enabled under Assisted NLU section in the Bot Locale page.

1. Build the bot to see the changes are reflected in your bot in Runtime.

1. Once the bot build is completed, you can use the test panel in the console or run a test set to see the improvements after enabling LLM Assisted NLU feature.

------

**Guidance to improve the accuracy of your bot when using the LLM Assisted NLU Feature**

The following best practices can help you maximize the effectiveness of the Assisted NLU feature:

1. **Make Intent Names Self-Explanatory** — Use names that immediately convey the action or purpose of the intent. For example, if you're creating an intent for booking flights, simply call it "BookFlight".

1. **Keep Names Clean and Simple** — Avoid adding prefixes, suffixes, or unnecessary words to your intent and slot names. Extra elements like "Dev" or "Test" can confuse the LLM and make the purpose less clear.

1. **Provide Detailed Descriptions** — For each custom intent and slot, include a brief but informative description. This helps explain its specific use and context, making it easier for both humans and the LLM to understand its purpose.

**Note**  
When you enable this feature, your data might be processed across AWS Regions. For more information on Cross-Region Inference, see [https://docs.aws.amazon.com/bedrock/latest/userguide/cross-region-inference.html](https://docs.aws.amazon.com/bedrock/latest/userguide/cross-region-inference.html).

**Important**  
Enable this feature in a draft version of the bot. Test it before using it in a production alias.

## Disabling Assisted NLU
<a name="disable-assisted-nlu"></a>

To disable the Assisted NLU feature, follow these steps:

1. Sign in to the AWS Management Console and open the Amazon Lex V2 console at [https://console.aws.amazon.com/lexv2/home](https://console.aws.amazon.com/lexv2/home).

1. In the **Bots** page, select your bot.

1. On the **Bot Locale** page, click on **Configure** under the **Assisted NLU** section.

1. Under the Runtime generative AI features section, toggle off the Assisted NLU feature, and click **Save**.

1. Build the bot to apply the changes.