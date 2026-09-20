

# Set up collaboration with an external AI agent
<a name="a2a-setup-external"></a>

This page explains how to configure your Connect AI agent to collaborate with an external AI agent built by a third-party provider. External agents run outside of your Amazon Connect Customer instance, on infrastructure the provider manages, and communicate with Connect Customer over the A2A protocol through a WebSocket connection.

By the end of this setup, your Connect AI agent can bring in the external agent during a live contact, either to handle actions behind the scenes or to talk to the customer directly.

This is an API-only feature. All setup requests must be SigV4-signed. You can drive every step with the AWS CLI or SDK. For A2A-specific shapes (the `A2A_SERVER` application type and multi-agent AI agent configuration), the installed CLI does not yet include the newest shapes, so some steps use `awscurl` to send SigV4-signed requests directly.

All steps target production endpoints in your instance's Region: `secretsmanager.<REGION>.amazonaws.com`, `app-integrations.<REGION>.amazonaws.com`, `connect.<REGION>.amazonaws.com`, and `wisdom.<REGION>.amazonaws.com` (the qconnect API).

## Prerequisites
<a name="a2a-setup-external-prereqs"></a>

Before you start, confirm that you have the following:
+ **Connect Customer tier.** Your instance must be on the Connect Customer tier. Agent-to-agent collaboration is not available on Customer Basic.
+ **A2A-compatible external agent.** The external agent must support the A2A protocol over a WebSocket endpoint. The provider gives you the endpoint URL and authentication credentials.
+ **Voice streaming review.** If the external agent uses voice streaming (bidirectional audio), work with your AWS account team or Solutions Architect to validate that the agent meets the latency and audio quality requirements before deploying to production.
+ **IAM permissions.** Use AWS credentials for an IAM principal in the account that owns your Connect instance. The principal needs, at minimum:
  + `secretsmanager:CreateSecret`, `secretsmanager:PutResourcePolicy` (Step 1)
  + `kms:CreateKey`, `kms:CreateAlias` (Step 1, if creating the customer managed key)
  + `app-integrations:CreateApplication` (Step 2)
  + `connect:CreateIntegrationAssociation`, `connect:UpdateSecurityProfile`, `connect:AssociateSecurityProfiles` (Steps 3 and 4)
  + `wisdom:CreateAssistant`, `wisdom:CreateAIAgent`, `wisdom:UpdateAIAgent`, `wisdom:CreateAIAgentVersion` (Steps 0 and 5; the qconnect API authorizes as the wisdom service)

## Step 0: Create an assistant and associate it with your Connect instance
<a name="a2a-setup-external-step0"></a>

AI agents live under an Amazon Q in Connect assistant, and the assistant must be associated with your Connect instance.

```
aws qconnect create-assistant \
  --name my-assistant \
  --type AGENT \
  --region <REGION>
```

```
aws connect create-integration-association \
  --instance-id <INSTANCE_ID> \
  --integration-type WISDOM_ASSISTANT \
  --integration-arn <ASSISTANT_ARN> \
  --region <REGION>
```

For the full assistant setup walkthrough (including console steps), see [Initial set-up for AI agents](https://docs.aws.amazon.com/connect/latest/adminguide/enable-q.html) in the Amazon Connect public documentation.

If you already have an assistant associated with your instance, skip to Step 1.

## Step 1: Store the external agent's API key
<a name="a2a-setup-external-step1"></a>

Your external agent authenticates inbound requests with an API key that Connect Customer presents as a bearer token on the WebSocket upgrade. Store the API key in AWS Secrets Manager.

1. **Create a customer managed KMS key** whose key policy grants the Connect service principal decrypt access. This is required. Connect Customer cannot read a secret encrypted with the default `aws/secretsmanager` key.

   Key policy statement:

   ```
   {
     "Sid": "AllowConnectDecrypt",
     "Effect": "Allow",
     "Principal": {
       "Service": "connect.amazonaws.com"
     },
     "Action": [
       "kms:Decrypt",
       "kms:DescribeKey"
     ],
     "Resource": "*"
   }
   ```

1. **Create the secret** encrypted with that customer managed key, containing the API key value.

1. **Attach a resource policy** to the secret that grants `connect.amazonaws.com` access to read it.

**Important**  
Do not use the default AWS managed key (`aws/secretsmanager`). AWS managed keys do not support cross-service grant policies, and Connect Customer cannot access secrets encrypted with them. You must create a customer managed KMS key and use it to encrypt the secret.

## Step 2: Register the A2A server application
<a name="a2a-setup-external-step2"></a>

Register the external agent's endpoint as an AppIntegrations application. The `ApplicationType` must be `A2A_SERVER`, and `AuthConfig` is required.

```
awscurl --service app-integrations --region <REGION> -X POST \
  --header 'Content-Type: application/json' \
  --data '{
    "Name": "my-agent",
    "Namespace": "my-agent-ns",
    "Description": "My external A2A agent",
    "ApplicationSourceConfig": {
      "ExternalUrlConfig": {
        "AccessUrl": "wss://agent.example.com"
      }
    },
    "ApplicationType": "A2A_SERVER",
    "AuthConfig": {
      "AuthType": "API_KEY",
      "CredentialProviderIdentifier": "<SECRET_ARN>"
    }
  }' \
  https://app-integrations.<REGION>.amazonaws.com/applications
```

The response returns the application ID and ARN:

```
{"Id": "<APPLICATION_ID>", "Arn": "<APPLICATION_ARN>"}
```

`AccessUrl` must be a public TLS endpoint (`https://` or `wss://`). `AuthConfig` is required for `A2A_SERVER` applications. Without it, the request fails.

Record the returned `Id` (referenced from your Connect AI agent configuration) and `Arn` (used in Steps 3 and 4).

## Step 3: Associate the application with your Connect instance
<a name="a2a-setup-external-step3"></a>

```
awscurl --service connect --region <REGION> -X PUT \
  --header 'Content-Type: application/json' \
  --data '{
    "IntegrationArn": "<APPLICATION_ARN>",
    "IntegrationType": "APPLICATION"
  }' \
  https://connect.<REGION>.amazonaws.com/instance/<INSTANCE_ID>/integration-associations
```

## Step 4: Allow-list the application in the security profile
<a name="a2a-setup-external-step4"></a>

The security profile attached to your Connect AI agent must explicitly allow the third-party application, or collaboration fails at runtime. Update the security profile to include the application ARN with type `THIRD_PARTY` in its allowed AI agents.

```
awscurl --service connect --region <REGION> -X POST \
  --header 'Content-Type: application/json' \
  --data '{
    "AllowedAIAgents": [
      {
        "Arn": "<APPLICATION_ARN>",
        "Type": "THIRD_PARTY"
      }
    ]
  }' \
  https://connect.<REGION>.amazonaws.com/security-profiles/<INSTANCE_ID>/<SECURITY_PROFILE_ID>
```

Also associate the security profile with your Connect AI agent (both the unversioned and versioned agent ARN):

```
aws connect associate-security-profiles \
  --instance-id <INSTANCE_ID> \
  --entity-arn <AI_AGENT_ARN> \
  --entity-type AI_AGENT \
  --security-profiles Id=<SECURITY_PROFILE_ID>
```

## Step 5: Add the external collaborator
<a name="a2a-setup-external-step5"></a>

Create or update your Connect AI agent through the qconnect API to reference the external agent. The configuration you use depends on what you want the collaborator to do.

Save the request body to a file (for example, `create-ai-agent.json`) and send it:

```
awscurl --service wisdom --region <REGION> -X POST \
  --header 'Content-Type: application/json' \
  --data @create-ai-agent.json \
  https://wisdom.<REGION>.amazonaws.com/assistants/<ASSISTANT_ID>/aiagents
```

### Pattern A: Handle actions behind the scenes
<a name="a2a-setup-external-pattern-a"></a>

Use `delegateAgentConfiguration` when the external agent performs work and returns a result, while your Connect AI agent continues talking to the customer. The customer does not interact with the collaborator.

```
{
  "name": "my-orchestrator",
  "type": "ORCHESTRATION",
  "visibilityStatus": "PUBLISHED",
  "configuration": {
    "orchestrationAIAgentConfiguration": {
      "orchestrationAIPromptId": "<PROMPT_ID>",
      "connectInstanceArn": "arn:aws:connect:<REGION>:<ACCOUNT>:instance/<INSTANCE_ID>",
      "multiAgentConfigurations": [
        {
          "delegateAgentConfiguration": {
            "agentTarget": {
              "applicationId": "<APPLICATION_ID>"
            },
            "instruction": {
              "instruction": "Use this agent to run a credit check. Send the customer's SSN and requested loan amount. The agent returns an approval decision, credit score, and any conditions."
            }
          }
        }
      ]
    }
  }
}
```

The `delegateAgentConfiguration` field tells Connect Customer that this collaborator handles actions behind the scenes. Your Connect AI agent sends a request over text, waits for the result, and uses it to continue the conversation with the customer.

### Pattern B: Talk to the customer (Connect handles voice)
<a name="a2a-setup-external-pattern-b"></a>

Use `handoffAgentConfiguration` with `audioStreamingEnabled` set to `false` when the external agent takes over the conversation, and Connect Customer provides the voice. Connect Customer converts the caller's speech to text, sends text to the collaborator, receives text responses, and converts them to speech.

```
{
  "name": "my-orchestrator",
  "type": "ORCHESTRATION",
  "visibilityStatus": "PUBLISHED",
  "configuration": {
    "orchestrationAIAgentConfiguration": {
      "orchestrationAIPromptId": "<PROMPT_ID>",
      "connectInstanceArn": "arn:aws:connect:<REGION>:<ACCOUNT>:instance/<INSTANCE_ID>",
      "multiAgentConfigurations": [
        {
          "handoffAgentConfiguration": {
            "agentTarget": {
              "applicationId": "<APPLICATION_ID>"
            },
            "instruction": {
              "instruction": "Transfer the conversation to this agent when the customer wants to file a new insurance claim. The agent asks for claim details, verifies the information, and files the claim. It returns a claim confirmation number when done."
            },
            "audioStreamingEnabled": false,
            "immediateHandoff": true
          }
        }
      ]
    }
  }
}
```

The `handoffAgentConfiguration` field tells Connect Customer that this collaborator talks to the customer directly. Setting `audioStreamingEnabled` to `false` means Connect Customer handles speech-to-text and text-to-speech. The external agent works with text only.

Setting `immediateHandoff` to `true` means the external agent takes over the conversation on the first turn with no frontline reasoning. Audio (voice) integrations must use immediate handoff at launch.

### Pattern C: Talk to the customer (agent provides its own voice)
<a name="a2a-setup-external-pattern-c"></a>

Use `handoffAgentConfiguration` with `audioStreamingEnabled` set to `true` when the external agent takes over the conversation and provides its own AI voice. Connect Customer passes the caller's audio directly to the collaborator's endpoint, and the collaborator streams audio back.

```
{
  "name": "my-orchestrator",
  "type": "ORCHESTRATION",
  "visibilityStatus": "PUBLISHED",
  "configuration": {
    "orchestrationAIAgentConfiguration": {
      "orchestrationAIPromptId": "<PROMPT_ID>",
      "connectInstanceArn": "arn:aws:connect:<REGION>:<ACCOUNT>:instance/<INSTANCE_ID>",
      "multiAgentConfigurations": [
        {
          "handoffAgentConfiguration": {
            "agentTarget": {
              "applicationId": "<APPLICATION_ID>"
            },
            "instruction": {
              "instruction": "Transfer the conversation to this agent for all self-service voice interactions. The agent uses its own voice and handles account inquiries, balance checks, and general service questions. It returns a summary of what was resolved."
            },
            "audioStreamingEnabled": true,
            "immediateHandoff": true
          }
        }
      ]
    }
  }
}
```

Setting `audioStreamingEnabled` to `true` enables bidirectional audio streaming. The external agent must support PCM audio encoding over the A2A WebSocket connection. This option is available for voice contacts only. Bidirectional audio streaming works only with Sonic Lex bots.

**Note**  
For bidirectional audio streaming, work with your AWS account team or Solutions Architect to validate that the external agent meets the latency and audio quality requirements.

### Choosing between patterns
<a name="a2a-setup-external-choosing"></a>


| You want the collaborator to... | Configuration | Audio streaming | 
| --- | --- | --- | 
| Perform work behind the scenes and return a result | delegateAgentConfiguration | Not applicable (text only) | 
| Talk to the customer, using Connect Customer's voice | handoffAgentConfiguration | audioStreamingEnabled: false | 
| Talk to the customer, using its own AI voice | handoffAgentConfiguration | audioStreamingEnabled: true | 

## Step 6: Set up the Lex bot and contact flow
<a name="a2a-setup-external-step6"></a>

You reach your Connect AI agent from a contact flow through an Amazon Lex V2 bot. You perform these steps in the Amazon Connect admin website and flow designer (no API signing required).

### Lex bot
<a name="a2a-setup-external-lex-bot"></a>

Set up the Lex bot as follows:
+ Create a Lex V2 bot whose only intent is the built-in `AMAZON.QInConnectIntent`, configured with your Q in Connect Assistant ARN. Do not add any other intents.
+ Enable the speech to speech inference on the bot locale.
+ Build the bot, then create a version and alias.
+ Make sure the bot and assistant are in the same Region.

### Contact flow (minimal)
<a name="a2a-setup-external-contact-flow"></a>

Configure the contact flow with the following blocks:
+ **Set logging behavior:** enable (recommended).
+ **Connect assistant block:** point at your Assistant ARN. This opens the AI session and writes `$.Wisdom.SessionArn` onto the contact.
+ **Get customer input block** (Amazon Lex tab): select your bot and alias, and set these session attributes:
  + `x-amz-lex:q-in-connect:ai-agent-arn` = the versioned ARN of your ORCHESTRATION AI agent (for example, `arn:aws:wisdom:<region>:<account>:ai-agent/<assistantId>/<aiAgentId>:$LATEST`).
  + **Prelaunch only (required today, removed at public launch):** the path is gated by an opt-in session attribute. For voice: `x-amz-lex:qic-audio-passthrough = true`. For text: `x-amz-lex:qic-text-passthrough = true`. For chat: `x-amz-lex:qic-passthrough = true`. After the feature is public, these attributes are no longer needed.
+ **For chat, enable message streaming:** instances created after December 2025 have it on by default. For older instances, set the `MESSAGE_STREAMING` instance attribute to `true` using the AWS console (instance > Flows > Amazon Lex bots > "Enable message streaming in Amazon Connect").

## Step 7: Publish the updated configuration
<a name="a2a-setup-external-step7"></a>

Create a new version to make the change live. Changes to your Connect AI agent configuration do not take effect until you publish a version.

```
aws qconnect create-ai-agent-version \
  --assistant-id <ASSISTANT_ID> \
  --ai-agent-id <AI_AGENT_ID>
```

After you publish, new contacts that reach your Connect AI agent use the updated configuration with the external collaborator.

## What context Connect Customer shares
<a name="a2a-setup-external-context"></a>

When Connect Customer invokes the external collaborator, it passes the prior conversation history, the contact ARN, instance ARN, and contact system attributes (channel, customer address, system address). If your Connect AI agent has the appropriate permissions, custom contact attributes are also included. You do not configure what context is shared. Connect Customer passes this information automatically on every collaboration.

On chat, a new WebSocket connection opens for each customer message. The connection uses the same `contextId` every time, and history is re-sent on each `INIT_SESSION`. On voice, one persistent connection serves the whole session.

## Trace data requirements
<a name="a2a-setup-external-trace"></a>

External collaborators must send the required trace data, including input and output messages, tool calls and results, and per-span timing. For the complete list, see [Observability for collaborating AI agents](a2a-observability.md).

Connect Customer disables external agent endpoints that do not send the required trace data. When an external endpoint is disabled, it remains in your Connect AI agent's configuration, but Connect Customer does not invoke it for new contacts. In-flight contacts that are already using the collaborator complete normally.

For the full list of required and encouraged trace fields, see [Trace data requirements for external AI agents](a2a-trace-enforcement.md).

## Related topics
<a name="a2a-setup-external-related"></a>
+ [Set up collaboration with another Connect Customer AI agent](a2a-setup-1p.md) (for agents in your instance or on AgentCore)
+ [Observability for collaborating AI agents](a2a-observability.md)
+ [Trace data requirements for external AI agents](a2a-trace-enforcement.md)
+ [Configure voice for collaborating AI agents](a2a-voice.md)
+ [Quotas and limitations for agent-to-agent collaboration](a2a-quotas.md)
+ [A2A protocol contract for external AI agents](https://docs.aws.amazon.com/connect/latest/devguide/a2a-developer-guide.html)