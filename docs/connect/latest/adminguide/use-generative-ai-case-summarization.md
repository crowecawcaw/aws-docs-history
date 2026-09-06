

# Use generative AI-powered case summarization
<a name="use-generative-ai-case-summarization"></a>

To help agents to handle cases more efficiently, they can use generative AI-powered case summarization. This AI agent and Connect Customer Cases feature – available to unlimited AI customers – helps agents gather context faster and expedites their time to resolution of customer issues.

To view the permissions needed to use the feature, see [Required Cases and Agent Applications permissions to generate AI-powered case summarization](assign-security-profile-cases.md#required-cases-agent-app-ai-summary-permissions).

**Case summary field required**  
For case summarization to work, a case summary field must exist on the case template. If no summary field is configured, the AI agent has nowhere to write the generated summary and the feature does not function. Add a summary field to the case template before enabling this feature.

When an agent views a Case that is enabled with AI agents, they can use the **Generate** button to produce a summary of the Case and its Activity Feed.

![Screenshot showing Generate button for case summary.](http://docs.aws.amazon.com/connect/latest/adminguide/images/case-summary-generate-button.png)


## Case Summarization
<a name="case-summarization-details"></a>

AI agent automatically analyzes the Case and generates a summary that includes information from:
+ Fields on the case
+ Comments on the case.
+ SLAs related to the case.
+ Transcripts from chat, and voice contacts related to the case (30-day transcript retention period).
+ Details from Tasks related to the case

This summary helps agents quickly understand the context and history of the case without having to read through the entire activity feed.

The following [default AI agent and prompt](default-ai-system.md) are used to generate the case summarization:
+ QinConnectCaseSummarizationPrompt

## Actions agents can take on Case Summary
<a name="case-summary-agent-actions"></a>

After a case summary is generated, the agent can:

1. Manually edit the summary in the text box.

1. Save the summary to the case.

1. Regenerate a new summary from scratch.

1. Cancel the summary without storing it.

1. Choose **Copy** to copy the contents of the summary.

1. Choose the Thumbs up or Thumbs down icons to provide immediate feedback to their contact center manager so they can improve the AI agent responses. For more information, see [TRANSCRIPT\_RESULT\_FEEDBACK](https://docs.aws.amazon.com/connect/latest/adminguide/monitor-ai-agents.html#documenting-cw-events-ih).

![Screenshot showing case summary action options.](http://docs.aws.amazon.com/connect/latest/adminguide/images/case-summary-actions.png)


## Configure case summarization
<a name="configure-case-summarization"></a>

Following is an overview of the steps to configure case summarization for your contact center.

1. [Enable AI agents for your instance](ai-agent-initial-setup.md).

1. [Enable Cases for you instance](enable-cases.md).

1. Add the [Connect assistant](connect-assistant-block.md) block to your flows before a contact is assigned to your agent.

1. Customize the outputs of your cases generative AI-powered assistant by [defining your prompts](create-ai-prompts.md) to guide the AI agent with generating responses that match your company's language, tone, and policies for consistent customer service.

## Best practices to ensure quality responses
<a name="case-summarization-best-practices"></a>

To ensure the best quality response from AI agent, implement the following best practices:
+ Train your agents to review all AI-generated content before storing it on a case.
+ Use AI guardrails to ensure appropriate content generation. For more information, see [Create AI guardrails for AI agents](create-ai-guardrails.md).
+ Monitor AI agent performance through CloudWatch Logs logs for:
  + Response feedback from your agents. For more information, see [TRANSCRIPT\_RESULT\_FEEDBACK](https://docs.aws.amazon.com/connect/latest/adminguide/monitor-ai-agents.html#documenting-cw-events-ih).
  + Generated email responses shown to agents. For more information, see [TRANSCRIPT\_RECOMMENDATION](https://docs.aws.amazon.com/connect/latest/adminguide/monitor-ai-agents.html#documenting-cw-events-ih).