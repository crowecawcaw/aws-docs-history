

# Use a description to build a bot in Lex V2 with the descriptive bot builder
<a name="nld-bots"></a>

**Note**  
Before you can take advantage of the generative AI features, you must fulfill the following prerequisites  
For information about pricing for using Amazon Bedrock, see [Amazon Bedrock pricing](https://aws.amazon.com/bedrock/pricing/).
Turn on the generative AI capabilities for your bot locale. To do so, follow the steps at [Optimize Lex V2 bot creation and performance by using generative AI](generative-features.md). 

The descriptive bot builder lets you take advantage of Amazon Bedrock's access to large language models to improve the efficiency of the bot creation process. You provide a prompt using natural language that includes the purpose of the bot and the actions that it should perform. Amazon Lex V2 harnesses Amazon Bedrock's capabilities to generate relevant intents and slot types for your bot based on your description. Once you choose the intents and slot types that you want to keep, you can then iterate upon the bot to modify it to your specific use-case. The descriptive bot builder saves you time by letting you avoid having to manually create intents and slot types for the bot.

The descriptive bot builder is available in the English locales (see the locales that begin with `en_` in the table in [Languages and locales supported by Amazon Lex V2](how-languages.md)).

Before you create your bot, do the following.

1. Check that your role has the correct permissions by reviewing the steps at [Permissions needed to create a bot with natural language description in Lex V2](nld-permissions.md).

1. Decide on the description to use. You can refer to [Example bot descriptions for descriptive bot builder](nld-examples.md) for sample bot descriptions.

Create a bot by using natural language to describe what the bot should be able to do. Amazon Lex V2 invoke Amazon Bedrock models to generate intents and slot types that fit your bot's use case. You can create the bot with either the console or the API.

------
#### [ Console ]

**Create a bot using the descriptive bot builder**

1. Sign in to the AWS Management Console and open the Amazon Lex V2 console at [https://console.aws.amazon.com/lexv2/home](https://console.aws.amazon.com/lexv2/home).

1. In the **Bots** page, select **Create bot**.

1. For the **Creation method**, choose **Descriptive Bot Builder - GenAI**.

1. Give your bot a name and optional description, configure the IAM permissions, and choose whether your bot is subject to COPPA or not. Then select **Next**.

1. Select a language to create the bot in, a voice for the bot, and a confidence threshold for intent classification (for more information, see [Using intent confidence scores to improve intent selection with Lex V2](using-intent-confidence-scores.md).

1. Under **Descriptive Bot Builder - GenAI**, provide a description for the bot you want to create. Your description should be both *detailed* and *precise* to help generate appropriate and sufficient intents for your bot. Include a list of actions to improve the intent creation process.

1. Select a model provider and model under **Select model**.

1. To create the bot in another locale, choose **Add another language**. When you are finished adding languages, select **Done**. Amazon Lex V2 creates your bot and the descriptive bot builder generates intents and slots for it. When the locale has been generated, the banner turns from blue to green. Select **Review** to see the generated intents and slot types.
**Note**  
The descriptive bot builder is currently only available in English locales. However, you can copy a bot to a non-English locale after creating it.

**Review the generated intents and slot types and add them to your bot**

1. If there are enough intents and slot types that are applicable for your bot's use-case, you can review the generated intents.

   1. Review the **Generated intents**.

      1. Choose a checkbox next to an intent to remove it from the list of intents to add to the bot.

      1. Choose an intent name to view the **Sample utterances** and **Slots** generated for the intent.

      1. By default, all the utterances and slots are selected. Choose a checkbox to remove that item from the intent. Select **Add to selection** to keep the checked items in the intent.

   1. Review the **Generated slot types**.

      1. Choose a checkbox next to a slot type to remove it from the list of intents to add to the bot.

      1. You can add values to a slot type after you have added it to the bot

1. When you're satisfied with your intents and slot types, select **Add intents and slot types** at the top of the page to add the intents and slot types to your bot.

1. When the resources are finished being added, a green success banner appears. Go to **Intents** and **Slot types** to edit the generated ones and to add more values.

1. If the **Generated intents** and **Generated slot types** are mostly inapplicable to the bot you want to create, carry out the following steps.

   1. Select **New generation** in the **Descriptive bot builder details** section.

   1. Rewrite the prompt and select **Re-generate** to generate new intents and slot types. The results differ if you use a different model.
**Important**  
There is no guarantee that the same intents and slots will be generated. You are charged each time you regenerate the intents and slot types.

------
#### [ API ]

**Create the bot using natural language description**

When you use the descriptive bot builder through the API, it creates a bot definition in a .zip file in an Amazon S3 bucket. You download this file and import the bot definition into Amazon Lex V2 to create your bot.

1. Send a [CreateBot](https://docs.aws.amazon.com/lexv2/latest/APIReference/API_CreateBot.html) request to create a new bot. Then send a [CreateBotLocale](https://docs.aws.amazon.com/lexv2/latest/APIReference/API_CreateBotLocale.html) request to create a locale for the bot.

1. Send a [StartBotResourceGeneration](https://docs.aws.amazon.com/lexv2/latest/APIReference/API_StartBotResourceGeneration.html) request, specifying the ID, version, and locale of the bot. You can use `DRAFT` for the bot version. Provide your prompt in the `generationInputPrompt` field. Your description should be both *detailed* and *precise* to help generate appropriate and sufficient intents for your bot. Include a list of actions to improve the intent creation process.

1. Take note of the `generationId` in the response.

1. Send a [DescribeBotResourceGeneration](https://docs.aws.amazon.com/lexv2/latest/APIReference/API_DescribeBotResourceGeneration.html) request using the `generationId` you received in the `StartBotResourceGeneration` response. Include the bot ID, version, and locale.

1. If the `generationStatus` in the `DescribeBotResourceGeneration` response is `Complete`, the `generatedBotLocaleUrl` field will also be populated. Use this Amazon S3 URI to download the bot definition by following the steps at [Downloading an object](https://docs.aws.amazon.com/AmazonS3/latest/userguide/download-objects.html).

**Check the generated bot definition and import it**

1. Use the Amazon S3 URI from the `generationStatus` in the `DescribeBotResourceGeneration` response to download the bot definition by following the steps at [Downloading an object](https://docs.aws.amazon.com/AmazonS3/latest/userguide/download-objects.html).

1. You can directly modify the generated content for your bot's specific use-case by editing the file. You can also send another `StartBotResourceGeneration` request to regenerate intents and slots.
**Important**  
There is no guarantee that the same intents and slots will be generated. You are charged each time you regenerate the intents and slot types.

1. To import the bot definition, follow the steps at [Importing bots in Lex V2](import.md).

1. After importing, you can modify the generated intents and slots by using the [UpdateIntent](https://docs.aws.amazon.com/lexv2/latest/APIReference/API_UpdateIntent.html), [UpdateSlot](https://docs.aws.amazon.com/lexv2/latest/APIReference/API_UpdateSlot.html), and [UpdateSlotType](https://docs.aws.amazon.com/lexv2/latest/APIReference/API_UpdateSlotType.html) operations.

To list metadata about all the generated items for a bot locale, use the [ListBotResourceGenerations](https://docs.aws.amazon.com/lexv2/latest/APIReference/API_ListBotResourceGenerations.html) operation. Use any of the returned `generationId` values in a `DescribeBotResourcGeneration` request to retrieve the Amazon S3 URI for a generated bot definition.

------

**Topics**
+ [Example bot descriptions for descriptive bot builder](nld-examples.md)
+ [Permissions needed to create a bot with natural language description in Lex V2](nld-permissions.md)