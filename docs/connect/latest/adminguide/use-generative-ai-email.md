

# Use generative AI-powered email conversation overviews and suggested responses
<a name="use-generative-ai-email"></a>

To help agents to handle emails more efficiently, they can use generative AI-powered email responses. The email AI agents help agents provide faster email responses and more consistent support to customers.

When an agent accepts an email contact that is [enabled](ai-agent-initial-setup.md#enable-ai-agents-step4) with AI agents, they automatically receive three types of proactive responses in their Connect assistant panel on the agent workspace:

1. [Email conversation overview](#email-conversation-overview). For example, it provides key information about the customer's purchase history.

1. [Knowledge base and guide recommendations](#knowledge-base-recommendations). For example, it recommends as refund resolution step-by-step guide. 

1. [Generated email responses](#generated-email-responses)

These response types are shown in the following image.

![Three types of responses in the Connect assistant panel.](http://docs.aws.amazon.com/connect/latest/adminguide/images/qic-email-automation.png)


## Email conversation overview
<a name="email-conversation-overview"></a>

The [EmailOverview agent](default-ai-system.md) automatically analyzes the email conversation (thread) and provides a structured overview that includes:
+ The customer's key issues.
+ Previous agent actions (if the email is a reply to another agent's reply on the same thread).
+ Important contextual details.
+ Required next steps.

This overview helps agents quickly understand the context and history of the email conversation without having to read through the entire thread. The EmailOverview agent focuses more weight on the current email message (contact) while maintaining context from the previous email messages in the conversation.

## Knowledge base and guide recommendations
<a name="knowledge-base-recommendations"></a>

The [EmailResponse agent](default-ai-system.md) automatically suggests relevant content from your knowledge base to assist your agent with understanding how to handle the customer's issue. It suggests:
+ [Knowledge articles](ai-agent-initial-setup.md#enable-ai-agents-step-3)
+ [Step-by-step guides associated with the knowledge article](integrate-guides-with-ai-agents.md)

The agent can choose **Sources** to view the original knowledge base articles from which the recommendation came from and choose the specific knowledge base article link to open a preview of it in their agent workspace.

The EmailResponse and EmailQueryReformulation prompts are used to generate knowledge base and guide recommendations.

## Generated email responses
<a name="generated-email-responses"></a>

The [EmailGenerativeAnswer agent](default-ai-system.md) automatically suggests a drafted response to the agent based on the context from the email overview and your knowledge base articles available. It does the following:
+ Analyzes the email conversation context
+ Incorporates relevant knowledge base content
+ Generates a professional email response draft that includes:
  + Appropriate greeting and closing
  + Response to specific customer questions
  + Relevant information from your knowledge base
  + Proper formatting and tone

When an agent chooses **Reply all**, they can:

1. Select an [email template](create-message-templates1.md) to set the branding and signature for their response.

1. Copy the generated response from the panel.

1. Paste the generated response into their response editor, and either:
   + Use the generated response as-is

    — OR —
   + Edit it before sending

1. If the generated response does not meet the agent's needs, they can choose **Regenerate** icon in the Connect assistant panel to request a new generated response.

These options are shown in the following image.

![The agent workspace when an agent chooses Reply all to an email contact.](http://docs.aws.amazon.com/connect/latest/adminguide/images/qic-generated-email-responses.png)


By default, the content copied from generated email responses in raw HTML format works best with the Connect Customer rich text editor for agents responding to email contacts. To customize the output of this response, edit **QinConnectEmailGenerativeAnswerPrompt** as part of the **QinConnectEmailGenerativeAnswerAIAgent** to output the response in your preferred format (for example, plain text or markdown).

**Important**  
You cannot use information from Connect Customer Customer Profiles, Connect Customer Cases, email templates, and quick responses in generated responses. 

The EmailGenerativeAnswer and EmailQueryReformulation prompts are used to generate email responses.

## Actions agents can take on all proactive responses
<a name="all-proactive-responses"></a>

For all proactive responses shown when the agent accepts an email contact, the agent can:
+ Choose the Show more or Show less icons to expand and collapse the response shown in the Connect assistant panel.
+ Choose the Thumbs up or Thumbs down icons to provide immediate feedback to their contact center manager so they can improve the AI agent responses. For more information, see [TRANSCRIPT\_RESULT\_FEEDBACK](monitor-ai-agents.md#documenting-cw-events-ih).
+ Choose **Copy** to copy the contents of the response. By default, the content copied from any of the responses are in raw HTML format to work best with the Connect Customer rich text editor for agents responding to email contacts. To customize the output of this response, edit the prompts and agents to output the response in your preferred format (for example, plain text or markdown).

## Configure generative email responses
<a name="configuration-steps"></a>

**Important**  
Generative email is for agent assistance with inbound email contacts.   
If an outbound email is sent to the [Connect assistant](connect-assistant-block.md) block within the [Default outbound flow](default-outbound.md), **you will be charged for the analysis of the outbound email contact**. To prevent this, add a [Check contact attributes](check-contact-attributes.md) block before [Connect assistant](connect-assistant-block.md) and route the contact accordingly. 

Following is an overview of the steps to configure generative email responses for your contact center.

1. [Initial set-up for AI agents](ai-agent-initial-setup.md).

1. Add a [Check contact attributes](check-contact-attributes.md) block to check it's an email contact, and then add the [Connect assistant](connect-assistant-block.md) block to your flows before an email contact is assigned to your agent.

1. Customize the outputs of your email generative AI-powered assistant by [adding knowledge bases](ai-agent-initial-setup.md#enable-ai-agents-step-3) and [defining your prompts](create-ai-prompts.md) to guide the AI agent with generating responses that match your company's language, tone, and policies for consistent customer service.

## Best practices to ensure quality responses
<a name="best-practices"></a>

To ensure the best quality response from AI agents, implement the following best practices:
+ Train your agents to review all AI-generated content before sending to customers or using in comments or notes.
+ Use email templates to ensure consistent formatting. For more information, see [Create message templates](create-message-templates1.md).
+ Maintain up-to-date knowledge base content to improve response quality. For more information, see [Step 3: Create an integration (knowledge base)](ai-agent-initial-setup.md#enable-ai-agents-step-3).
+ Use AI guardrails to ensure appropriate content generation. For more information, see [Create AI guardrails for AI agents](create-ai-guardrails.md).
+ Monitor AI agent performance through Amazon CloudWatch logs for:
  + Response feedback from your agents. For more information, see [TRANSCRIPT\_RESULT\_FEEDBACK](monitor-ai-agents.md#documenting-cw-events-ih).
  + Generated email responses shown to agents. For more information, see [TRANSCRIPT\_RECOMMENDATION](monitor-ai-agents.md#documenting-cw-events-ih). 