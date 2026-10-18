

# Set up an external AI agent integration
<a name="a2a-setup-external"></a>

This page explains how to configure your Connect AI agent to collaborate with an external AI agent. An external agent runs outside of your Amazon Connect Customer instance, on infrastructure that you or a third-party provider manages. Agents that you host on Amazon Bedrock AgentCore are also external agents, and you set them up the same way.

External agents communicate with Connect Customer over the Agent-to-Agent (A2A) protocol with the Connect Customer A2A extensions. This page covers the setup that you perform in your AWS account. For information about what the external agent's server must implement, see [Build an external AI agent server](a2a-external-server.md) and the [A2A protocol contract for external AI agents](https://docs.aws.amazon.com/connect/latest/devguide/a2a-developer-guide.html).

By the end of this setup, your Connect AI agent can bring in the external agent during a live contact. The external agent can either handle actions behind the scenes or talk to the customer directly.

Complete the following sections in order:

1. [Store the external agent's API key](#a2a-setup-external-step1)

1. [Register the A2A server application](#a2a-setup-external-step2)

1. [Associate the application with your Connect instance](#a2a-setup-external-step3)

1. [Add the external collaborator](#a2a-setup-external-step5)

1. [Configure the security profile for your Connect AI agent](#a2a-setup-external-step4)

1. [Publish the updated configuration](#a2a-setup-external-step7)

Before you start, review the [Prerequisites](#a2a-setup-external-prereqs).

This is an API-only feature. All setup requests must be SigV4-signed. You can drive every step with the AWS CLI or an AWS SDK.

All steps target public service endpoints in your instance's Region: `secretsmanager.REGION.amazonaws.com`, `app-integrations.REGION.amazonaws.com`, `connect.REGION.amazonaws.com`, and `wisdom.REGION.amazonaws.com` (the qconnect API).

## Prerequisites
<a name="a2a-setup-external-prereqs"></a>

Before you start, confirm that you have the following:
+ **Connect Customer tier.** Your instance must be on the Connect Customer tier. Agent-to-agent collaboration is not available on Customer Basic.
+ **A Connect assistant associated with your instance.** You create the orchestrating Connect AI agent, which calls the collaborator during a live contact, under this assistant in [Add the external collaborator](#a2a-setup-external-step5). For how to set up AI agents, see [Initial set-up for AI agents](ai-agent-initial-setup.md).
+ **An external agent that supports the A2A protocol with the Connect Customer A2A extensions.** For text, the agent can accept JSON-RPC over a secure WebSocket (`wss://`) or over HTTPS (`https://`). Audio streaming is supported over secure WebSocket (`wss://`) only. The provider gives you the endpoint URL and an API key. For the full requirements, see [Build an external AI agent server](a2a-external-server.md).
+ **Voice streaming review.** If the external agent uses audio streaming (bidirectional audio), work with your AWS account team or Solutions Architect. They can help you validate that the agent meets the latency and audio quality requirements before you deploy to production.
+ **IAM permissions.** Use AWS credentials for an IAM principal in the account that owns your Connect instance. At minimum, the principal needs the following permissions:
  + `secretsmanager:CreateSecret`, `secretsmanager:PutResourcePolicy` ([Store the external agent's API key](#a2a-setup-external-step1))
  + `kms:CreateKey`, `kms:CreateAlias` ([Store the external agent's API key](#a2a-setup-external-step1), if you create the customer managed key)
  + `app-integrations:CreateApplication` ([Register the A2A server application](#a2a-setup-external-step2))
  + `connect:CreateIntegrationAssociation`, `connect:UpdateSecurityProfile`, `connect:AssociateSecurityProfiles` ([Associate the application with your Connect instance](#a2a-setup-external-step3) and [Configure the security profile for your Connect AI agent](#a2a-setup-external-step4))
  + `wisdom:CreateAIAgent`, `wisdom:UpdateAIAgent`, `wisdom:CreateAIAgentVersion` ([Add the external collaborator](#a2a-setup-external-step5) and [Publish the updated configuration](#a2a-setup-external-step7)). IAM actions for Connect AI agents use the `wisdom` service prefix.
+ **Security profile permissions.** Your Connect AI agent needs a security profile that allows the external agent's application. If you want the external agent to receive contact context, the security profile must also grant the **Access Contact Control Panel** permission. You configure both in [Configure the security profile for your Connect AI agent](#a2a-setup-external-step4).
+ **An Amazon Lex V2 bot with the `AMAZON.QInConnectIntent`.** All agent-to-agent collaboration requires this bot, associated with your Connect Customer instance. For more information, see [Add the Amazon Lex bot to your Connect Customer instance](amazon-lex.md#lex-bot-add-to-connect) and [AMAZON.QInConnectIntent](https://docs.aws.amazon.com/lexv2/latest/dg/built-in-intent-qinconnect.html) in the *Amazon Lex V2 Developer Guide*.

  For external collaborators, the bot locale settings depend on audio streaming:
  + **Audio streaming** (`audioStreamingEnabled` is `true`): The bot locale must use Amazon Nova Sonic speech-to-speech and contain a single `AMAZON.QInConnectIntent`. The bot does not perform speech-to-speech for the collaborator. Audio streams directly between Connect Customer and the external agent.
  + **Audio streaming off**: You can use any Amazon Lex speech recognition and text-to-speech settings.

## Store the external agent's API key
<a name="a2a-setup-external-step1"></a>

Your external agent authenticates inbound requests with an API key. Connect Customer presents the key as a bearer token (`Authorization: Bearer`) when it connects to the agent. Store the API key in AWS Secrets Manager.

1. **Create a customer managed KMS key** whose key policy lets Connect Customer decrypt the secret. This is required. Connect Customer cannot read a secret encrypted with the default `aws/secretsmanager` key. Add the following statement to the key policy, alongside your account's existing administrator statements. Connect Customer needs only `kms:Decrypt`, and only through AWS Secrets Manager.

   ```
   {
     "Sid": "AllowConnectToDecryptSecret",
     "Effect": "Allow",
     "Principal": { "Service": "connect.amazonaws.com" },
     "Action": "kms:Decrypt",
     "Resource": "*",
     "Condition": {
       "StringEquals": { "kms:ViaService": "secretsmanager.REGION.amazonaws.com" }
     }
   }
   ```

1. **Create the secret** encrypted with that customer managed key, containing the API key value.

1. **Attach a resource policy** to the secret with `PutResourcePolicy`. The policy lets Connect Customer read the secret with `secretsmanager:GetSecretValue`:

   ```
   {
     "Version": "2012-10-17",
     "Statement": [
       {
         "Sid": "AllowConnectToRetrieveSecret",
         "Effect": "Allow",
         "Principal": { "Service": "connect.amazonaws.com" },
         "Action": "secretsmanager:GetSecretValue",
         "Resource": "*",
         "Condition": {
           "StringEquals": { "aws:SourceAccount": "ACCOUNT_ID" },
           "ArnEquals": { "aws:SourceArn": "arn:aws:connect:REGION:ACCOUNT_ID:instance/INSTANCE_ID" }
         }
       }
     ]
   }
   ```

   The conditions restrict access to your Connect Customer instance, whose ARN is the `aws:SourceArn` value, so that another account's Connect Customer instance can't use the secret.

**Important**  
Do not use the default AWS managed key (`aws/secretsmanager`). AWS managed keys do not support cross-service grant policies, and Connect Customer cannot access secrets encrypted with them. You must create a customer managed KMS key and use it to encrypt the secret.

## Register the A2A server application
<a name="a2a-setup-external-step2"></a>

Register the external agent's endpoint as an AppIntegrations application. The `ApplicationType` must be `A2A_SERVER`, and `AuthConfig` is required.

```
aws appintegrations create-application \
  --name my-agent \
  --namespace my-agent-ns \
  --description "My external A2A agent" \
  --application-source-config '{"ExternalUrlConfig":{"AccessUrl":"wss://agent.example.com"}}' \
  --application-type A2A_SERVER \
  --auth-config '{"AuthType":"API_KEY","CredentialProviderIdentifier":"SECRET_ARN"}' \
  --region REGION
```

The response contains the application ID and ARN:

```
{"Id": "APPLICATION_ID", "Arn": "APPLICATION_ARN"}
```

The following rules apply to the application:
+ **Application type.** You cannot change `ApplicationType` after you create the application. If you create the application with the wrong type, delete it and create a new one.
+ **Namespace.** The namespace can be up to 32 characters. It cannot start with `aws.` or `amazon.`, and it must be unique in your account.
+ **Access URL.** `AccessUrl` must point to a public host and use TLS: `https://` for text over HTTP, or `wss://` for WebSocket. Audio streaming requires `wss://`.
+ **Authentication.** `AuthConfig` is required for `A2A_SERVER` applications. Set `CredentialProviderIdentifier` to the ARN of the secret that you created in [Store the external agent's API key](#a2a-setup-external-step1). Without `AuthConfig`, the request fails.

Record the returned `Id` (referenced from your Connect AI agent configuration) and `Arn` (used in [Associate the application with your Connect instance](#a2a-setup-external-step3) and [Configure the security profile for your Connect AI agent](#a2a-setup-external-step4)).

## Associate the application with your Connect instance
<a name="a2a-setup-external-step3"></a>

To make the application available to your instance, run the following command:

```
aws connect create-integration-association \
  --instance-id INSTANCE_ID \
  --integration-type APPLICATION \
  --integration-arn APPLICATION_ARN \
  --region REGION
```

## Add the external collaborator
<a name="a2a-setup-external-step5"></a>

Create your Connect AI agent through the qconnect API to reference the external agent. The configuration you use depends on the collaboration mode:
+ **Handle actions behind the scenes** (`delegateAgentConfiguration`). When your Connect AI agent decides to invoke the external agent, it builds a text message for it. The external agent performs the work and returns a text result, which your Connect AI agent uses to invoke another action or to formulate a response to the customer.
+ **Talk to the customer** (`handoffAgentConfiguration`). The external agent takes over the conversation. On voice contacts, either Connect Customer handles speech (text) or the external agent provides its own speech (audio).

Save the request body to a file (for example, `create-ai-agent.json`) and send it:

```
aws qconnect create-ai-agent \
  --cli-input-json file://create-ai-agent.json \
  --region REGION
```

For a comparison of the collaboration modes, see [Compare collaboration modes](a2a-how-it-works.md#a2a-how-it-works-modes). For limits on the number of collaborators, see [Quotas and limitations for agent-to-agent collaboration](a2a-quotas.md).

### Add a collaborator that handles actions behind the scenes
<a name="a2a-setup-external-pattern-a"></a>

Use `delegateAgentConfiguration` when the external agent performs work and returns a result, while your Connect AI agent continues talking to the customer. The customer does not interact with the collaborator. When your Connect AI agent decides to invoke the collaborator, it builds a text message for it.

```
{
  "assistantId": "YOUR_ASSISTANT_ID",
  "name": "my-orchestrator",
  "type": "ORCHESTRATION",
  "visibilityStatus": "PUBLISHED",
  "configuration": {
    "orchestrationAIAgentConfiguration": {
      "orchestrationAIPromptId": "YOUR_PROMPT_ID",
      "connectInstanceArn": "arn:aws:connect:REGION:ACCOUNT_ID:instance/INSTANCE_ID",
      "multiAgentConfigurations": [
        {
          "delegateAgentConfiguration": {
            "agentTarget": {
              "applicationId": "YOUR_APPLICATION_ID"
            },
            "instruction": {
              "instruction": "Use this agent to run a credit check. Send the customer's account number and requested loan amount. The agent returns an approval decision, credit score, and any conditions."
            }
          }
        }
      ]
    }
  }
}
```

The `delegateAgentConfiguration` field tells Connect Customer that this collaborator handles actions behind the scenes. Your Connect AI agent sends the message, waits for the result, and uses it to continue the conversation with the customer.

Each time your Connect AI agent decides to invoke the collaborator, Connect Customer opens a new connection and initializes a new session with the same session ID.

### Add a collaborator that talks to the customer
<a name="a2a-setup-external-pattern-b"></a>

Set `audioStreamingEnabled` to `false` when the external agent works with text.

On voice contacts, Connect Customer converts the caller's speech to text, sends text to the collaborator, receives text responses, and converts them to speech. If you omit the field, the default is `false`.

```
{
  "assistantId": "YOUR_ASSISTANT_ID",
  "name": "my-orchestrator",
  "type": "ORCHESTRATION",
  "visibilityStatus": "PUBLISHED",
  "configuration": {
    "orchestrationAIAgentConfiguration": {
      "orchestrationAIPromptId": "YOUR_PROMPT_ID",
      "connectInstanceArn": "arn:aws:connect:REGION:ACCOUNT_ID:instance/INSTANCE_ID",
      "multiAgentConfigurations": [
        {
          "handoffAgentConfiguration": {
            "agentTarget": {
              "applicationId": "YOUR_APPLICATION_ID"
            },
            "instruction": {
              "instruction": "Transfer the conversation to this agent when the customer wants to file a new insurance claim. The agent asks for claim details, verifies the information, and files the claim. It returns a claim confirmation number when done."
            },
            "audioStreamingEnabled": false,
            "immediateHandoff": false
          }
        }
      ]
    }
  }
}
```

The `handoffAgentConfiguration` field tells Connect Customer that this collaborator talks to the customer directly. The `immediateHandoff` field controls when the handoff happens:
+ `false`: Your Connect AI agent decides when to hand off, based on the collaborator's instruction.
+ `true`: The external agent takes over the conversation on the first turn, without your Connect AI agent evaluating the instruction first. Each Connect AI agent can have at most one collaborator with immediate handoff.

When the external agent finishes, it sends a `COMPLETE` or `ESCALATE` finish type with a reason. Control returns to your main Connect AI agent, which is invoked again with the reason. It can continue the conversation, invoke another collaborator, or use its Complete or Escalate tool to return the contact to the flow. For details, see [Build an external AI agent server](a2a-external-server.md). For the Complete and Escalate tools, see [Tools for orchestrator AI agents](agentic-self-service.md#agentic-self-service-default-tools).

### Add a collaborator that talks to the customer with audio streaming
<a name="a2a-setup-external-pattern-c"></a>

Set `audioStreamingEnabled` to `true` when the external agent has its own speech capabilities and you want it to handle the caller's audio directly. Connect Customer streams the caller's audio to the collaborator's endpoint, and the collaborator streams audio back.

```
{
  "assistantId": "YOUR_ASSISTANT_ID",
  "name": "my-orchestrator",
  "type": "ORCHESTRATION",
  "visibilityStatus": "PUBLISHED",
  "configuration": {
    "orchestrationAIAgentConfiguration": {
      "connectInstanceArn": "arn:aws:connect:REGION:ACCOUNT_ID:instance/INSTANCE_ID",
      "multiAgentConfigurations": [
        {
          "handoffAgentConfiguration": {
            "agentTarget": {
              "applicationId": "YOUR_APPLICATION_ID"
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

Audio streaming has the following constraints:
+ **External agents only.** Audio streaming is not supported when the collaborator is another Connect AI agent.
+ **Immediate handoff only.** You must set `immediateHandoff` to `true`.
+ **Only collaborator.** The audio collaborator must be the only collaborator on the Connect AI agent.
+ **Orchestrating AI agent restrictions.** The Connect AI agent that hands off to the audio collaborator must not have an orchestration prompt or a guardrail. It must have the reserved **Complete** tool, and it can also have the reserved **Escalate** tool. It cannot have any other tools. If the configuration does not meet these rules, validation fails. The preceding example does not show tool configuration. For how to add these tools, see [Tools for orchestrator AI agents](agentic-self-service.md#agentic-self-service-default-tools).
+ **Amazon Lex bot.** The bot locale must use Amazon Nova Sonic speech-to-speech and contain a single `AMAZON.QInConnectIntent`. For details, see [Prerequisites](#a2a-setup-external-prereqs).
+ **Secure WebSocket endpoint.** Audio streaming is supported over WebSocket only. The application's `AccessUrl` must use `wss://`. The external agent must send and receive PCM audio.
+ **Voice contacts only.** On chat contacts, Connect Customer does not negotiate audio, even when `audioStreamingEnabled` is `true`. The external agent must also handle text. To tell voice from chat, the external agent can read the channel from contact context, which requires the **Access Contact Control Panel** permission ([Configure the security profile for your Connect AI agent](#a2a-setup-external-step4)).
+ **One setting per collaborator.** You cannot switch a collaborator between text and audio during a contact.

**Note**  
For audio streaming, work with your AWS account team or Solutions Architect to validate that the external agent meets the latency and audio quality requirements.

## Configure the security profile for your Connect AI agent
<a name="a2a-setup-external-step4"></a>

The security profile attached to your Connect AI agent must explicitly allow the third-party application, or collaboration fails at runtime. Update the security profile to include the application ARN with type `THIRD_PARTY` in its allowed AI agents.

```
aws connect update-security-profile \
  --instance-id INSTANCE_ID \
  --security-profile-id SECURITY_PROFILE_ID \
  --allowed-ai-agents '[{"Arn":"APPLICATION_ARN","Type":"THIRD_PARTY"}]' \
  --region REGION
```

Then associate the security profile with your Connect AI agent. Run the following command once for each agent ARN: once with the unversioned ARN, and once with the versioned ARN.

```
aws connect associate-security-profiles \
  --instance-id INSTANCE_ID \
  --entity-arn YOUR_ORCHESTRATING_AGENT_ARN \
  --entity-type AI_AGENT \
  --security-profiles Id=SECURITY_PROFILE_ID
```

**Contact context.** To share contact context with an external agent that talks to the customer, add the **Access Contact Control Panel** permission to the same security profile. Contact context contains the customer address, system address, and channel. Without this permission, Connect Customer does not send contact context. For a complete list of what Connect Customer sends, see [Build an external AI agent server](a2a-external-server.md).

## Publish the updated configuration
<a name="a2a-setup-external-step7"></a>

Create a new version to make the change live. Changes to your Connect AI agent configuration do not take effect until you publish a version.

```
aws qconnect create-ai-agent-version \
  --assistant-id YOUR_ASSISTANT_ID \
  --ai-agent-id YOUR_ORCHESTRATING_AGENT_ID
```

After you publish, new contacts that reach your Connect AI agent use the updated configuration with the external collaborator.

## Trace data requirements
<a name="a2a-setup-external-trace"></a>

External collaborators must send trace data for every turn. This includes input and output messages, tool inputs and results, and valid start and end times.

Connect Customer disables external agent endpoints that do not send the required trace data. When Connect Customer disables an external endpoint, the endpoint remains in your Connect AI agent's configuration, but Connect Customer does not invoke it for new contacts. In-flight contacts that are already using the collaborator complete normally.

For the required fields, see [Trace data requirements for external AI agents](a2a-trace-enforcement.md). For information about how to send traces, see [Tracing](https://docs.aws.amazon.com/connect/latest/devguide/a2a-developer-guide.html#a2a-dg-tracing) in the A2A protocol contract.

## Related topics
<a name="a2a-setup-external-related"></a>
+ [Build an external AI agent server](a2a-external-server.md)
+ [A2A protocol contract for external AI agents](https://docs.aws.amazon.com/connect/latest/devguide/a2a-developer-guide.html)
+ [Set up collaboration with another Connect Customer AI agent](a2a-setup-1p.md) (for other Connect AI agents in your instance)
+ [Observability for collaborating AI agents](a2a-observability.md)
+ [Trace data requirements for external AI agents](a2a-trace-enforcement.md)
+ [Quotas and limitations for agent-to-agent collaboration](a2a-quotas.md)