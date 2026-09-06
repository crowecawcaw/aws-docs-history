

# AMAZON.QnAIntent
<a name="generative-qna"></a>

**Note**  
Before you can take advantage of the generative AI features, you must fulfill the following prerequisites  
For information about pricing for using Amazon Bedrock, see [Amazon Bedrock pricing](https://aws.amazon.com/bedrock/pricing/).
Turn on the generative AI capabilities for your bot locale. To do so, follow the steps at [Optimize Lex V2 bot creation and performance by using generative AI](generative-features.md). 

You can take advantage of Amazon Bedrock FMs to help answer customer questions in a bot conversation. Amazon Lex V2 offers a built-in `AMAZON.QnAIntent` that you can add to your bot. This intent harnesses generative AI capabilities from Amazon Bedrock by recognizing customer questions and searching for an answer from the following knowledge stores (for example, **Can you provide me details on the baggage limits for my international flight?**). This feature reduces the need to configure questions and answers using task-oriented dialogue within Amazon Lex V2 intents. This intent also recognizes follow-up questions (for example, **What about domestic flight?**) based on the conversation history and provides the answer accordingly.

Ensure that your IAM role has the proper permissions to access the `AMAZON.QnAIntent` by following the steps at [Permissions for the AMAZON.QnAIntent](qna-permissions.md).

To take advantage of the `AMAZON.QnAIntent` you must have set up one of the following knowledge stores.
+ Amazon OpenSearch Service database – For more information, see [Creating and managing Amazon OpenSearch Service domains](https://docs.aws.amazon.com/opensearch-service/latest/developerguide/createupdatedomains.html).
+ Amazon Kendra index – For more information, see [Creating an index](https://docs.aws.amazon.com/kendra/latest/dg/create-index.html).
+ Amazon Bedrock knowledge base – For more information, see [Building a knowledge base](https://docs.aws.amazon.com/bedrock/latest/userguide/knowledge-base.html).

You can set up the `AMAZON.QnAIntent` in one of two ways:

**To set up using Generative AI configurations**

1. In the Amazon Lex V2 console, select **Bots** from the left navigation pane and choose the bot for which you want to add the intent from the **Bots** section.

1. From the left navigation pane, select the language for which you want to add the intent.

1. In the **Generative AI configurations** section, select **Configure**.

1. In the **QnA configurations** section, select **Create QnA intent**.

**To set up by adding a built-in intent to your bot**

1. In the Amazon Lex V2 console, select **Bots** from the left navigation pane and choose the bot for which you want to add the intent from the **Bots** section.

1. From the left navigation pane, select **Intents** under the language for which you want to add the intent.

1. Select **Add intent** and choose **Use built-in intent** from the dropdown menu.

1. For more details about configurations for the `AMAZON.QnAIntent`, see [AMAZON.QnAIntent](built-in-intent-qna.md).

**Note**  
The `AMAZON.QnAIntent` is activated when an utterance is not classified into any of the other intents present in the bot. This intent is activated when an utterance is not classified into any of the other intents present in the bot. Note that this intent will not be activated for missed utterances when eliciting a slot value. Once recognized, the `AMAZON.QnAIntent` uses the specified Amazon Bedrock model to search the configured knowledge base and respond to the customer question.

**Topics**
+ [Permissions for the AMAZON.QnAIntent](qna-permissions.md)