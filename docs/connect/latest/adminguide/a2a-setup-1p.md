

# Set up collaboration with another Connect Customer AI agent
<a name="a2a-setup-1p"></a>

This page describes how to add a collaborating AI agent that runs in your Connect Customer instance. You configure collaborators through the Connect Customer API. Connect Customer manages the A2A protocol between your AI agents for you.

## Prerequisites
<a name="a2a-setup-1p-prereqs"></a>

Before you begin, confirm that you have the following:
+ **An AI agent created and published in your Connect Customer instance.** This is the orchestrating agent that calls the collaborator during a live contact. You need its `aiAgentId`.
+ **A collaborating agent that exists and is reachable.** The collaborator is another AI agent in your Connect Customer instance. You need the collaborator's `aiAgentId`.
+ **IAM permissions to call the QConnect API.** For the specific actions, see [Required permissions](#a2a-setup-1p-permissions).
+ **An Amazon Lex V2 bot with the `AMAZON.QInConnectIntent`.** All agent-to-agent collaboration requires this bot, associated with your Connect Customer instance. Any Amazon Lex speech recognition and text-to-speech settings work. For more information, see [Add the Amazon Lex bot to your Connect Customer instance](amazon-lex.md#lex-bot-add-to-connect) and [AMAZON.QInConnectIntent](https://docs.aws.amazon.com/lexv2/latest/dg/built-in-intent-qinconnect.html) in the *Amazon Lex V2 Developer Guide*.

## Add a collaborator that handles actions behind the scenes
<a name="a2a-setup-1p-delegate"></a>

To have a collaborator handle actions behind the scenes, use `delegateAgentConfiguration`. The collaborator works behind the scenes and returns results to your Connect AI agent. Your Connect AI agent stays in control of the conversation. The customer never interacts with the collaborator directly.

This is the right choice when the collaborator performs a discrete job: looking up an order, scoring a fraud risk, retrieving a claim status, or running a calculation.

Call `UpdateAIAgent` and add the collaborator under `orchestrationAIAgentConfiguration.multiAgentConfigurations`:

```
{
  "assistantId": "YOUR_ASSISTANT_ID",
  "aiAgentId": "YOUR_ORCHESTRATING_AGENT_ID",
  "visibilityStatus": "PUBLISHED",
  "configuration": {
    "orchestrationAIAgentConfiguration": {
      "orchestrationAIPromptId": "YOUR_PROMPT_ID",
      "multiAgentConfigurations": [
        {
          "delegateAgentConfiguration": {
            "agentTarget": {
              "aiAgentId": "COLLABORATOR_AGENT_ID"
            },
            "instruction": {
              "instruction": "Use this agent to look up insurance claim status. Send the claim number and the customer's policy ID. The agent returns claim status, approval dates, and expected payment timeline."
            }
          }
        }
      ]
    }
  }
}
```

The following table describes the fields in this request.


| Field | What it does | 
| --- | --- | 
| delegateAgentConfiguration | Tells Connect Customer that this collaborator handles actions behind the scenes. Your Connect AI agent stays in control of the conversation. | 
| agentTarget.aiAgentId | The identifier of the collaborating AI agent in your instance. | 
| instruction | Tells your Connect AI agent when to call this collaborator, what information to send, and what to expect back. For more information, see [Write a useful description](#a2a-setup-1p-description). | 

You can add multiple collaborators by including additional objects in the `multiAgentConfigurations` array. Each collaborator has its own instruction and target.

## Add a collaborator that talks to the customer
<a name="a2a-setup-1p-handoff"></a>

To have a collaborator talk to the customer, use `handoffAgentConfiguration`. The collaborator takes over the conversation and speaks or chats with the customer directly. Your Connect AI agent steps aside while the collaborator handles the interaction, then resumes control when the collaborator finishes.

This is the right choice when the collaborator needs to have a multi-turn conversation with the customer: gathering information, asking follow-up questions, walking through a process, or handling a specialized interaction end to end.

Before you add a collaborator that talks to the customer, review the following requirements:
+ **Hand-back tools on the collaborator.** The collaborating AI agent must have the reserved Complete tool, and should also have the Escalate tool, so it can give control back to your orchestrating AI agent. Your orchestrating AI agent is invoked again with the reason that the collaborator gives. It can continue the conversation, invoke another collaborator, or use its Complete or Escalate tool to return the contact to your flow. For more information about these tools, see [Tools for orchestrator AI agents](agentic-self-service.md#agentic-self-service-default-tools).
+ **Conversation history.** Connect Customer passes the conversation history to the collaborator automatically. You don't need to configure it.
+ **Voice.** Connect Customer handles speech for collaborators in your instance with text streaming. Collaborators in your instance don't support audio streaming (`audioStreamingEnabled`).

Call `UpdateAIAgent` and add the collaborator under `orchestrationAIAgentConfiguration.multiAgentConfigurations`:

```
{
  "assistantId": "YOUR_ASSISTANT_ID",
  "aiAgentId": "YOUR_ORCHESTRATING_AGENT_ID",
  "visibilityStatus": "PUBLISHED",
  "configuration": {
    "orchestrationAIAgentConfiguration": {
      "orchestrationAIPromptId": "YOUR_PROMPT_ID",
      "multiAgentConfigurations": [
        {
          "handoffAgentConfiguration": {
            "agentTarget": {
              "aiAgentId": "COLLABORATOR_AGENT_ID"
            },
            "instruction": {
              "instruction": "Transfer the customer to this agent when they need to schedule, reschedule, or cancel an appointment. Tell the agent the customer's account number and the type of appointment before transferring."
            },
            "immediateHandoff": false
          }
        }
      ]
    }
  }
}
```

The following table describes the fields in this request.


| Field | What it does | 
| --- | --- | 
| handoffAgentConfiguration | Tells Connect Customer that this collaborator takes over the conversation with the customer. Your Connect AI agent steps aside until the collaborator finishes. | 
| agentTarget.aiAgentId | The identifier of the collaborating AI agent in your instance. | 
| instruction | Tells your Connect AI agent when to transfer the customer to this collaborator and what context to pass along. | 
| immediateHandoff | Controls when the handoff happens. Set to false to have your Connect AI agent transfer the customer when its instruction calls for it. Set to true to have the collaborator take over the conversation on the first turn, without your Connect AI agent evaluating the instruction first. An AI agent can have at most one immediate handoff. | 
| audioStreamingEnabled | Not supported for collaborators in your instance. Omit this field. | 

## Write a useful description
<a name="a2a-setup-1p-description"></a>

The `instruction` field determines when your Connect AI agent calls the collaborator and what context it passes. A vague instruction leads to missed invocations or calls with insufficient context. A specific instruction produces reliable collaboration.

**Be explicit about when to use the collaborator.** State the trigger conditions clearly.


| Less effective | More effective | 
| --- | --- | 
| "Claims agent." | "Use this agent when the customer asks about the status of an existing insurance claim, a pending payment, or a claim denial reason." | 

**Specify the inputs the collaborator needs.** Your Connect AI agent passes only the information that the instruction tells it to pass.


| Less effective | More effective | 
| --- | --- | 
| "Send the claim info." | "Send the claim number and the customer's policy ID. If the customer does not have the claim number, ask for the date of incident and the type of claim instead." | 

**Describe what the collaborator returns.** This helps your Connect AI agent understand the response and use it naturally in the conversation.


| Less effective | More effective | 
| --- | --- | 
| "Returns claim data." | "The agent returns the claim status (open, approved, denied, or under review), the date of the most recent update, and the expected payment amount and timeline if approved." | 

**Set boundaries.** Tell your Connect AI agent what the collaborator does not handle, so it does not send requests the collaborator cannot fulfill.


| Less effective | More effective | 
| --- | --- | 
| (no boundaries) | "Do not use this agent for new claim submissions, payment disputes, or policy changes. Those require a human agent." | 

## Publish the updated configuration
<a name="a2a-setup-1p-publish"></a>

After you add or modify collaborators, create a new version to make the configuration live. The updated collaborator settings do not take effect on new contacts until you publish a version.

```
aws qconnect create-ai-agent-version \
  --assistant-id YOUR_ASSISTANT_ID \
  --ai-agent-id YOUR_ORCHESTRATING_AGENT_ID
```

The response includes the new version number. Contacts that start after this point use the new configuration. Contacts that are already in progress continue with the version that was active when they started.

## Required permissions
<a name="a2a-setup-1p-permissions"></a>

The IAM principal that makes these API calls needs the following permissions on the relevant Connect Customer resources. Attach these as an IAM policy to the user or role that manages your Connect AI agent configuration.

```
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Effect": "Allow",
      "Action": [
        "wisdom:UpdateAIAgent",
        "wisdom:CreateAIAgentVersion",
        "wisdom:GetAIAgent",
        "wisdom:ListAIAgentVersions"
      ],
      "Resource": "arn:aws:wisdom:REGION:ACCOUNT_ID:ai-agent/ASSISTANT_ID/*"
    },
    {
      "Effect": "Allow",
      "Action": [
        "wisdom:CreateAIAgent",
        "wisdom:ListAIAgents"
      ],
      "Resource": "arn:aws:wisdom:REGION:ACCOUNT_ID:assistant/ASSISTANT_ID"
    }
  ]
}
```

The following table describes what each action is required for.


| Action | Required for | 
| --- | --- | 
| wisdom:CreateAIAgent | Creating a new AI agent with collaborators already configured | 
| wisdom:UpdateAIAgent | Adding or modifying collaborators on an existing AI agent | 
| wisdom:CreateAIAgentVersion | Publishing a version so the updated configuration takes effect | 
| wisdom:GetAIAgent | Retrieving the current configuration before you update it, and verifying changes | 
| wisdom:ListAIAgents | Listing agents in your instance to find agent IDs | 
| wisdom:ListAIAgentVersions | Listing published versions to verify that the new version was created | 

## Related topics
<a name="a2a-setup-1p-related"></a>
+ [How agent-to-agent collaboration works](a2a-how-it-works.md)
+ [Set up an external AI agent integration](a2a-setup-external.md)
+ [Agent-to-agent collaboration](a2a-collaboration.md)
+ [Observability for collaborating AI agents](a2a-observability.md)
+ [Quotas and limitations for agent-to-agent collaboration](a2a-quotas.md)