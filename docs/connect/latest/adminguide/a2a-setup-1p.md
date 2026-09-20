

# Set up collaboration with another Connect Customer AI agent
<a name="a2a-setup-1p"></a>

This page covers adding a collaborating AI agent that runs in your Connect Customer instance or on Amazon Bedrock AgentCore. You configure collaborators through the Connect Customer API (QConnect, service model `qconnect-2020-10-19`). There is no console interface for this feature.

For external third-party agents, see [Set up collaboration with an external AI agent](a2a-setup-external.md) instead.

## Prerequisites
<a name="a2a-setup-1p-prereqs"></a>

Before you begin, confirm that you have the following:
+ **An AI agent created and published in your Connect Customer instance.** This is the orchestrating agent that will call the collaborator during a live contact. You need its `aiAgentId`.
+ **A collaborating agent that exists and is reachable.** The collaborator can be another AI agent in your Connect Customer instance or an agent deployed on Amazon Bedrock AgentCore. You need the collaborator's `aiAgentId`.
+ **IAM permissions to call the QConnect API.** See [Required permissions](#a2a-setup-1p-permissions) for the specific actions.

## Add a collaborator that handles actions
<a name="a2a-setup-1p-delegate"></a>

Use `delegateAgentConfiguration` when the collaborator works behind the scenes and returns results to your Connect AI agent. Your Connect AI agent stays in control of the conversation. The customer never interacts with the collaborator directly.

This is the right choice when the collaborator performs a discrete job: looking up an order, scoring a fraud risk, retrieving a claim status, or running a calculation.

Call `UpdateAIAgent` and add the collaborator under `orchestrationAIAgentConfiguration.multiAgentConfigurations`:

```
{
  "assistantId": "YOUR_ASSISTANT_ID",
  "aiAgentId": "YOUR_ORCHESTRATING_AGENT_ID",
  "configuration": {
    "orchestrationAIAgentConfiguration": {
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

**Field reference:**


| Field | What it does | 
| --- | --- | 
| delegateAgentConfiguration | Tells Connect Customer that this collaborator handles actions behind the scenes. Your Connect AI agent stays in control of the conversation. | 
| agentTarget.aiAgentId | The collaborator's AI agent identifier. Use this field for agents in your instance or on AgentCore. For external third-party agents, use applicationId instead. | 
| instruction | Tells your Connect AI agent when to call this collaborator, what information to send, and what to expect back. See [Write a useful description](#a2a-setup-1p-description). | 

You can add multiple collaborators by including additional objects in the `multiAgentConfigurations` array. Each collaborator has its own instruction and target.

## Add a collaborator that talks to the customer
<a name="a2a-setup-1p-handoff"></a>

Use `handoffAgentConfiguration` when the collaborator takes over the conversation and speaks or chats with the customer directly. Your Connect AI agent steps aside while the collaborator handles the interaction, then resumes control when the collaborator finishes.

This is the right choice when the collaborator needs to have a multi-turn conversation with the customer: gathering information, asking follow-up questions, walking through a process, or handling a specialized interaction end to end.

Call `UpdateAIAgent` and add the collaborator under `orchestrationAIAgentConfiguration.multiAgentConfigurations`:

```
{
  "assistantId": "YOUR_ASSISTANT_ID",
  "aiAgentId": "YOUR_ORCHESTRATING_AGENT_ID",
  "configuration": {
    "orchestrationAIAgentConfiguration": {
      "multiAgentConfigurations": [
        {
          "handoffAgentConfiguration": {
            "agentTarget": {
              "aiAgentId": "COLLABORATOR_AGENT_ID"
            },
            "instruction": {
              "instruction": "Transfer the customer to this agent when they need to schedule, reschedule, or cancel an appointment. Tell the agent the customer's account number and the type of appointment before transferring."
            },
            "audioStreamingEnabled": false
          }
        }
      ]
    }
  }
}
```

**Field reference:**


| Field | What it does | 
| --- | --- | 
| handoffAgentConfiguration | Tells Connect Customer that this collaborator takes over the conversation with the customer. Your Connect AI agent steps aside until the collaborator finishes. | 
| agentTarget.aiAgentId | The collaborator's AI agent identifier. Use this field for agents in your instance or on AgentCore. | 
| instruction | Tells your Connect AI agent when to transfer the customer to this collaborator and what context to pass along. | 
| audioStreamingEnabled | Controls how voice is handled during the collaboration. Set to false for text streaming (Connect Customer converts speech to text and back). Set to true for bidirectional audio streaming (the collaborator uses its own AI voice). For agents in your instance, false is the typical setting. | 

## Write a useful description
<a name="a2a-setup-1p-description"></a>

The `instruction` field determines when your Connect AI agent calls the collaborator and what context it passes. A vague instruction leads to missed invocations or calls with insufficient context. A specific instruction produces reliable collaboration.

**Be explicit about when to use the collaborator.** State the trigger conditions clearly.


| Less effective | More effective | 
| --- | --- | 
| "Claims agent." | "Use this agent when the customer asks about the status of an existing insurance claim, a pending payment, or a claim denial reason." | 

**Specify the inputs the collaborator needs.** Your Connect AI agent will only pass information that the instruction tells it to pass.


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

After adding or modifying collaborators, create a new version to make the configuration live. The updated collaborator settings do not take effect on new contacts until you publish a version.

```
aws qconnect create-ai-agent-version \
  --assistant-id YOUR_ASSISTANT_ID \
  --ai-agent-id YOUR_ORCHESTRATING_AGENT_ID
```

The response includes the new version number. Contacts that start after this point use the new configuration. Contacts that are already in progress continue with the version that was active when they started.

## Required permissions
<a name="a2a-setup-1p-permissions"></a>

The IAM principal making these API calls needs the following permissions on the relevant Connect Customer resources. Attach these as an IAM policy to the user or role that manages your Connect AI agent configuration.

```
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Effect": "Allow",
      "Action": [
        "qconnect:CreateAIAgent",
        "qconnect:UpdateAIAgent",
        "qconnect:CreateAIAgentVersion",
        "qconnect:GetAIAgent",
        "qconnect:ListAIAgents",
        "qconnect:ListAIAgentVersions"
      ],
      "Resource": "arn:aws:qconnect:REGION:ACCOUNT_ID:assistant/ASSISTANT_ID/ai-agent/*"
    }
  ]
}
```

**What each action does:**


| Action | Required for | 
| --- | --- | 
| qconnect:CreateAIAgent | Creating a new AI agent with collaborators already configured | 
| qconnect:UpdateAIAgent | Adding or modifying collaborators on an existing AI agent | 
| qconnect:CreateAIAgentVersion | Publishing a version so the updated configuration takes effect | 
| qconnect:GetAIAgent | Retrieving the current configuration to verify changes | 
| qconnect:ListAIAgents | Listing agents in your instance to find agent IDs | 
| qconnect:ListAIAgentVersions | Listing published versions to verify the new version was created | 

## Related topics
<a name="a2a-setup-1p-related"></a>
+ [How agent-to-agent collaboration works](a2a-how-it-works.md)
+ [Set up collaboration with an external AI agent](a2a-setup-external.md)
+ [Configure voice for collaborating AI agents](a2a-voice.md)
+ [Observability for collaborating AI agents](a2a-observability.md)
+ [Quotas and limitations for agent-to-agent collaboration](a2a-quotas.md)