# AMAZON.QinConnectIntent

###### Note

To use generative AI capabilities using Amazon Q In Connect, you must complete the following pre-requisites:

1. Navigate to the Amazon Connect console and create your instance, if you don't have one already, see [Get started with Amazon Connect](../../../connect/latest/adminguide/amazon-connect-get-started.md "../../../connect/latest/adminguide/amazon-connect-get-started.md").
2. Enable Amazon Q in Connect for your instance, see [Enable Amazon Q in Connect for your instance](../../../connect/latest/adminguide/enable-q.md "../../../connect/latest/adminguide/enable-q.md").
   AMAZON.QinConnectIntent responds to customer questions by using the LLM-enhanced evolution of Amazon Connect Wisdom that delivers real-time recommendations to help
   contact center customers and agents resolve customer issues quickly and accurately. This intent is activated when an utterance is not classified into any of the
   other intents present in the bot. Note that this intent will not be activated for missed utterances when eliciting a slot value. Once recognized, the AMAZON.QinConnectIntent,
   uses the specified Q in Connect domain to search the configured Amazon Bedrock Knowledge Base and respond to the customer question.

###### Note

- You cannot use AMAZON.QinConnectIntent along with AMAZON.QnAIntent in the same bot locale.
- If you select another language besides U.S. English, you must customize the self-service prompts (`SELF_SERVICE_PRE_PROCESSING` and `SELF_SERVICE_ANSWER_GENERATION`)
  to respond in the specified language. For more information on how to customize your prompt, see [Customize Amazon Q in Connect](../../../connect/latest/adminguide/customize-q.md#ai-prompts-customize-q "../../../connect/latest/adminguide/customize-q.md#ai-prompts-customize-q").
  If you select this intent, you need to configure the following fields and then select **Save Intent** to add the intent to the bot.

- Amazon Q In Connect Configuration - Provide the Amazon Resource Name (ARN) of the Amazon Q in Connect assistant. Assistant ARN Pattern:
  `^arn:[a-z-]*?:wisdom:[a-z0-9-]*?:[0-9]{12}:[a-z-]*?/[a-f0-9]{8}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{12}(?:/[a-f0-9]{8}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{12}){0,2}$>`.
  The responses from the QinConnectIntent will be stored into the request attributes as shown below:

- `x-amz-lex:q-in-connect-response` – The response from QinConnectIntent to the question or utterance.
  **Session Attributes Returned from QinConnectIntent**

Interaction with the QinConnect intent provides additional data about conversation through session attributes.

1. `x-amz-lex:q-in-connect:session-arn` – An unique identifier for the session
   created with Amazon Q In Connect during the conversation.
2. `x-amz-lex:q-in-connect:conversation-status` – The current status of the
   conversation with QinConnect assistant or domain. There are three values possible for this status:
   - `CLOSED`
   - `READY`
   - `PROCESSING`

3. `x-amz-lex:q-in-connect:conversation-status-reason` – Provides the reason for
   the current status reported with above attribute. The possible reasons are as follows:
   - `SUCCESS` – Indicates customer has nothing left to ask and question has
     been answered successfully.
   - `FAILED` – Indicates a failure while answering the customer's question.
     These are mostly due to failures to understand the customer's question.
   - `REJECTED` – Indicates that the assistant is rejecting to answer customer
     question, and recommending that the question be handled outside of the bot interaction, such
     as talking to person or agent, to get more information.

###### Note

When a bot with QinConnectIntent is invoked during customer interactions driven by an Amazon Connect
instance, your session arn needs to be created and passed from the Amazon Connect instance. To create
a session, Amazon Connect Flows could be configured with Amazon Q in Connect step.

**Limitations**

- You cannot use AMAZON.QinConnectIntent along with intents without specific utterances
  such as AMAZON.QnAIntent, AMAZON.BedrockAgentIntent in the same bot locale.
- When a bot with QinConnectIntent is invoked during a customer interactions driven
  by an Amazon Connect instance, your session arn needs to be created and passed from
  the Amazon Connect instance. To create a session, Amazon Connect Flows could be
  configured with Amazon Q In Connect step.
- There can be no more than one AMAZON.QinConnectIntent per bot locale.
- The Amazon Q in Connect domain used with AMAZON.QinConnectIntent must be in the same AWS Region as the Amazon Lex V2 bot.
  **Permissions**

If the QinConnect Intent is used in an Amazon Lex V2 bot, and the bot is using a Service Linked Role (SLR),
the Amazon Lex V2 service has the permissions to update the appropriate policies on the role to
integrate it with the Q in Connect assistant. If the bot is using a custom IAM role, then the user
would need to manually add these permissions to their IAM role.

The Service Linked Role will get updated with the following permissions if the QinConnect intent gets added.
A new policy will be added for QinConnect access:

**Trust Policy**

```
{
    "Effect": "Allow",
    "Sid": "LexV2InternalTrustPolicy",
    "Principal": {
        "Service": "lexv2.aws.internal"
    },
    "Action": "sts:AssumeRole",
    "Condition": {
        "StringEquals": {
            "aws:SourceAccount": "{`accountId`}"
        },
        "ArnLike": {
            "aws:SourceArn": "arn:aws:lex:*:{`accountId`}:bot-alias/{`botId`}/*"
        }
    }
}
```
