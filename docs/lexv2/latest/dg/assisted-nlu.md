

# Improve intent classification and slot resolution in Lex V2 with Assisted NLU
<a name="assisted-nlu"></a>

With Amazon Lex V2 assisted natural language understanding (NLU), you can use large language models (LLMs) to improve intent classification and slot resolution in your bot. It enhances accuracy while staying within your bot's configured intents and slots. The feature doesn't generate or modify any bot content. It uses the names and descriptions of your intents and slots to interpret user input. This lets it handle typos, complex phrasing, and requests that combine multiple pieces of information in one sentence. You don't need to configure every utterance variation by hand. The result is a more seamless and effective conversational experience for your users.

The assisted NLU feature is available in English, Spanish, Portuguese, Catalan, French, Italian, and German locales. Specifically, it supports locales that begin with `en_`, `es_`, `pt_` (pt\_BR, pt\_PT), `ca_` (ca\_ES), `fr_` (fr\_CA, fr\_FR), `it_` (it\_IT), `de_` (de\_AT, de\_DE), `zh_` (zh\_CN, zh\_HK), `ja_JP`, and `ko_KR`. For the complete list of supported locales, see the table in [Languages and locales supported by Amazon Lex V2](how-languages.md).

Amazon Lex V2 invokes Amazon Bedrock models to help classify intents and resolve slot types that fit your bot's use case. You can enable assisted NLU for your bot with the console.

**Note**  
Assisted NLU (including Primary mode, Fallback mode, and intent disambiguation) is included at no additional cost with standard Amazon Lex V2 pricing. Dialog Manager mode is available with Connect Customer pricing. For more information, see [Assisted NLU mode - Dialog Manager](generative-llm-dialog-management.md).

## Disabling Assisted NLU
<a name="disable-assisted-nlu"></a>

To disable the Assisted NLU feature, follow these steps:

1. Sign in to the AWS Management Console and open the Amazon Lex V2 console at [https://console.aws.amazon.com/lexv2/home](https://console.aws.amazon.com/lexv2/home).

1. In the **Bots** page, select your bot.

1. On the **Bot Locale** page, choose **Configure** under the **Assisted NLU** section.

1. Under the **Runtime generative AI features** section, toggle off the Assisted NLU feature.

1. Choose **Save**.

1. Build the bot to apply the changes. The build might take a few minutes.

**Topics**
+ [Disabling Assisted NLU](#disable-assisted-nlu)
+ [Assisted NLU mode - Primary and Fallback](assisted-nlu-modes.md)
+ [Assisted NLU mode - Dialog Manager](generative-llm-dialog-management.md)