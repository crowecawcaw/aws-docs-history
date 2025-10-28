# Optimize Lex V2 bot creation and performance by using generative AI

Take advantage of Amazon Bedrock's generative AI capabilities to automate and speed up your Amazon Lex V2 bot building process. You can carry out the following processes with the help of Amazon Bedrock.

###### Note

These features uses generative AI. As you use the service, remember that it may give inaccurate or inappropriate responses. For more information, refer to [AWS Responsible AI Policy](https://aws.amazon.com/machine-learning/responsible-ai/policy/ "https://aws.amazon.com/machine-learning/responsible-ai/policy/").

Powered by Amazon Bedrock: AWS implements automated abuse detection. Because the Amazon Lex V2 generative AI features are built on Amazon Bedrock, users inherit the controls implemented in Amazon Bedrock to enforce safety, security, and the responsible use of AI.

- Create new bots and populate them with relevant intents and slot types efficiently using natural language description.
- Automatically generate sample utterances for your bot's intents.
- Improve your bots' slot resolution performance.
- Create an intent to help answer your customer's questions.
- Use Amazon Bedrock Agents and Amazon Bedrock Knowledge Bases to help answer your customer's questions.
  You can activate generative AI capabilities for Amazon Lex V2 either through the console or the API.

###### Note

Before you can take advantage of the generative AI features, you must fulfill the following prerequisites

1. Navigate to the [Amazon Bedrock console](https://console.aws.amazon.com/bedrock "https://console.aws.amazon.com/bedrock") and sign up for access
   to the Anthropic Claude model you intend to use (for more information, see [Model access](../../../bedrock/latest/userguide/model-access.md "../../../bedrock/latest/userguide/model-access.md")). For information
   about pricing for using Amazon Bedrock, see [Amazon Bedrock pricing](https://aws.amazon.com/bedrock/pricing/ "https://aws.amazon.com/bedrock/pricing/").
2. Turn on the
   generative AI capabilities for your bot locale. To do so, follow the steps at Optimize Lex V2 bot creation and performance by using generative AI.

Using the console

1. Sign in to the AWS Management Console and open the Amazon Lex V2 console at [https://console.aws.amazon.com/lexv2/home](https://console.aws.amazon.com/lexv2/home "https://console.aws.amazon.com/lexv2/home").
2. Select the bot and the locale in the bot for which you want to turn on generative AI capabilities.
3. In the **Generative AI configurations** section, select **Configure**.
4. Toggle the **Enabled** button for each feature that you want to activate. Select the model and version that you want to use for that feature. Enabling a feature may incur additional charges. For information
   about pricing for using Amazon Bedrock, see [Amazon Bedrock pricing](https://aws.amazon.com/bedrock/pricing/ "https://aws.amazon.com/bedrock/pricing/"). To learn more about a feature, select the corresponding topic from the list below. Select **Save** after you turn on the features that you want to activate. A green success banner appears to confirm that the capabilities are turned on.

Using the API

1. To enable generative AI capabilities for a new bot, use the [CreateBot](../APIReference/API_CreateBot.md "../APIReference/API_CreateBot.md") operation to create a new bot.
2. Send a [CreateBotLocale](../APIReference/API_CreateBotLocale.md "../APIReference/API_CreateBotLocale.md") request, modifying the `generativeAISettings` object as necessary. If you are enabling the capabilities for an existing bot, send a [UpdateBotLocale](../APIReference/API_UpdateBotLocale.md "../APIReference/API_UpdateBotLocale.md") request instead.
   1. To enable usage of the descriptive bot builder, modify the `descriptiveBotBuilder` object. Specify the foundation model to use in the `modelArn` field and set the `enabled` value to `True`.
   2. To enable slot resolution improvement, modify the `slotResolutionImprovement` object. Specify the foundation model to use in the `modelArn` field and set the `enabled` value to `True`.
   3. To enable sample utterance generation, modify the `sampleUtteranceGeneration` object. Specify the foundation model to use in the `modelArn` field and set the `enabled` value to `True`.

###### Topics

- [Use a description to build a bot in Lex V2 with the descriptive bot builder](nld-bots.md "nld-bots.md")
- [Use utterance generation to generate sample utterances for intent recognition](utterance-generation.md "utterance-generation.md")
- [Using assisted slot resolution to clarify slot values in Amazon Lex V2](assisted-slot.md "assisted-slot.md")
- [Using BedrockAgentIntent to use a Amazon Bedrock Agent in Amazon Lex V2](bedrock-agent-intent.md "bedrock-agent-intent.md")
- [Improve intent classification and slot resolution in Lex V2 with assisted NLU](assisted-nlu.md "assisted-nlu.md")
- [AMAZON.QnAIntent](generative-qna.md "generative-qna.md")
