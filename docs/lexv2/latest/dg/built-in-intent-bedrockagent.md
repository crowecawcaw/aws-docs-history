# AMAZON.BedrockAgentIntent

###### Note

Before you can take advantage of the generative AI features, you must fulfill the following prerequisites

1. Navigate to the [Amazon Bedrock console](https://console.aws.amazon.com/bedrock "https://console.aws.amazon.com/bedrock") and sign up for access
   to the Anthropic Claude model you intend to use (for more information, see [Model access](../../../bedrock/latest/userguide/model-access.md "../../../bedrock/latest/userguide/model-access.md")). For information
   about pricing for using Amazon Bedrock, see [Amazon Bedrock pricing](https://aws.amazon.com/bedrock/pricing/ "https://aws.amazon.com/bedrock/pricing/").
2. Turn on the
   generative AI capabilities for your bot locale. To do so, follow the steps at [Optimize Lex V2 bot creation and performance by using generative AI](generative-features.md "generative-features.md").
   Activates Amazon Bedrock Agents that are defined in the intent to respond to customer requests and activate agentic workflows
   to achieve the task defined. This feature is available in all Amazon Lex V2 supported locales and all commercial regions where
   both Amazon Lex V2 and Amazon Bedrock Agents are present.

If this intent is overriding `FallbackIntent`, the intent is activated when an utterance is not classified into any of the
other intents present in the bot, otherwise it is only activated when an utterance is classified into this intent. It’s
important to note that this intent will not be activated for missed utterances when eliciting a slot value.

Once recognized by your Amazon Lex V2 bot, the `AMAZON.BedrockAgentIntent`, activates the defined `BedrockAgent` or `BedrockKnowledgeBase` to
respond to the customer. If you are using Amazon Bedrock Agents, the conversation stays in the `BedrockAgentIntent` and the user requests
are relayed to Agents, until the Amazon Bedrock Agent determines that the conversation is marked `FINISH`. Only after that, Amazon Lex V2 assumes
control of the conversation and adheres to next steps defined in the `AMAZON.BedrockAgentIntent`.

Responds to customer questions by using an Amazon Bedrock Agents and Knowledge Bases to answer customer questions and provide detailed responses.

###### Warning

You can't use the `AMAZON.BedrockAgentIntent` without sample utterances, `AMAZON.QnAIntent` without sample utterances and
the `AMAZON.KendraSearchIntent` in the same bot locale.

If you select this intent, you configure the following fields and then select Add to add the intent.

- Amazon Bedrock Agent Id - The identifier of the Amazon Bedrock Agent. Choose the Bedrock Agent that you want to use.
- Amazon Bedrock Agent Alias Id - The Alias identifier of the Amazon Bedrock Agent.

###### Important

When creating the Amazon Bedrock Agent to be used with Amazon Lex V2, verify that **User Input** under **Additional Settings** is `ENABLED`.
This setting is critical to allow Agents to ask clarifying or follow-up questions, and it allows Amazon Lex V2 to delegate back to Agents to complete the corresponding task.

(Optional) You can also add a BedrockAgentIntent with these options:

- Amazon Bedrock model - Choose the provider and foundation model to use for this intent. Currently, some Anthropic Claude models are supported.
- Amazon Bedrock Knowledge Base - If you choose this option, specify the ID of the Amazon Bedrock Knowledge Base. You can find the ID by
  checking the details page of the Amazon Bedrock Knowledge Base in the console, or by sending a `GetKnowledgeBase` request.
  The responses from the BedrockAgentIntent will be stored into the session and request attributes as shown below:

- `x-amz-lex:bedrock-agent-search-response` – The response from the Amazon Bedrock Agent to the question or utterance.
- `x-amz-lex:bedrock-knowledge-base-search-response-source` – Points to the document, or list of documents, used to generate the response if using the Amazon Bedrock Knowledge Base configuration.
- `x-amz-lex:bedrock-agent-action-group-invocation-input` - Object containing input values collected by the agent action group. For more information on agent action groups, see ActionGroupInvocationInput.
- `x-amz-lex:bedrock-agent-knowledge-base-lookup-input` - Object containing the Amazon Bedrock Knowledge Base lookup related details.
- `x-amz-lex:bedrock-agent-agent-collaborator-details` – Object containing details of the input and output from the sub agents that were invoked as part of Multi-agent collaboration invocations.
  For more information, see [Using BedrockAgentIntent to use a Bedrock Agent in Amazon Lex V2](bedrock-agent-intent.md "bedrock-agent-intent.md").
