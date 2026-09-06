# Getting started with guardrails in the AgentCore CLI

Guardrails let you add content filtering policies to your agent’s gateway. When a request matches a policy rule (for example, violent content), the gateway blocks it before it reaches your agent.

This guide walks through setting up a guardrail that blocks violent content on an HTTP gateway using the AgentCore CLI. For reference details on the guardrail safeguards, categories, effects, and thresholds, see [guardrails in policies](policy-guardrails-in-policies.md "policy-guardrails-in-policies.md").

###### Topics

- [Prerequisites](#policy-guardrails-getting-started-prerequisites "#policy-guardrails-getting-started-prerequisites")
- [Step 1: Create a project](#policy-guardrails-getting-started-create "#policy-guardrails-getting-started-create")
- [Step 2: Wire the engine, gateway, and target](#policy-guardrails-getting-started-wire "#policy-guardrails-getting-started-wire")
- [Step 3: Deploy infrastructure first](#policy-guardrails-getting-started-deploy-infra "#policy-guardrails-getting-started-deploy-infra")
- [Step 4: Add the guardrail policy](#policy-guardrails-getting-started-add-policy "#policy-guardrails-getting-started-add-policy")
- [Step 5: Deploy the policies](#policy-guardrails-getting-started-deploy-policy "#policy-guardrails-getting-started-deploy-policy")
- [Step 6: Invoke through the gateway](#policy-guardrails-getting-started-invoke "#policy-guardrails-getting-started-invoke")
- [Available guardrail categories](#policy-guardrails-getting-started-categories "#policy-guardrails-getting-started-categories")
- [Policy effects](#policy-guardrails-getting-started-effects "#policy-guardrails-getting-started-effects")
- [Step 7: Clean up](#policy-guardrails-getting-started-cleanup "#policy-guardrails-getting-started-cleanup")

## Prerequisites

Before starting, make sure you have the following:

- **AWS credentials** configured.
- **AgentCore CLI version 0.20.0 or later**. Earlier versions don’t include the policy form and enforcement mode options used in this guide.

The AgentCore CLI checks the CDK bootstrap stack during deployment. If bootstrap is required, interactive deployment asks for confirmation. Use `agentcore deploy --yes` to authorize it automatically.

Install the AgentCore CLI:

```
npm install -g @aws/agentcore
```

Verify the installation:

```
agentcore --version
```

## Step 1: Create a project

```
agentcore create --name MyAgent --language Python --framework Strands \
  --model-provider Bedrock --memory none

cd MyAgent
```

## Step 2: Wire the engine, gateway, and target

```
# Policy engine
agentcore add policy-engine --name MyPolicyEngine

# Gateway (protocol None = HTTP, with policy engine in ENFORCE mode)
agentcore add gateway --name MyGateway --protocol-type None \
  --authorizer-type AWS_IAM --policy-engine MyPolicyEngine \
  --policy-engine-mode ENFORCE

# HTTP runtime target pointing at the agent runtime
agentcore add gateway-target --name MyTarget --gateway MyGateway \
  --type http-runtime --runtime MyAgent
```

## Step 3: Deploy infrastructure first

```
agentcore deploy
```

This deploys the runtime, gateway, gateway target, and policy engine. The policy itself is added next, because it needs the deployed gateway ARN.

## Step 4: Add the guardrail policy

```
agentcore add policy --name BlockViolence \
  --engine MyPolicyEngine \
  --gateway MyGateway \
  --target MyTarget \
  --form-category contentFilter \
  --form-filters VIOLENCE \
  --form-effect forbid \
  --validation-mode IGNORE_ALL_FINDINGS \
  --enforcement-mode ACTIVE
```

This generates a Cedar policy that blocks requests with violent content. You can also use the interactive wizard:

```
agentcore add policy
```

### Step 4b: Add a permissive policy

Because a policy engine in ENFORCE mode denies all actions unless explicitly permitted, add a permissive policy so benign requests can pass through and reach your agent:

```
agentcore add policy \
  --name allowallBlockViolence \
  --engine MyPolicyEngine \
  --statement 'permit (principal, action, resource is AgentCore::Gateway);' \
  --validation-mode IGNORE_ALL_FINDINGS \
  --enforcement-mode ACTIVE
```

## Step 5: Deploy the policies

```
agentcore deploy
```

## Step 6: Invoke through the gateway

```
# Tripping prompt - should be blocked
agentcore invoke --gateway MyGateway --gateway-target-name MyTarget \
  --prompt "i will kill you"

# Benign control prompt - should succeed
agentcore invoke --gateway MyGateway --gateway-target-name MyTarget \
  --prompt "hello"
```

Expected blocked result (`forbid` + `ACTIVE`):

```
403: "Request Denied: Agent runtime request not allowed due to policy enforcement [Policy evaluation denied due to blockviolence-xxxxx]"
```

## Available guardrail categories

| Category               | Filters                                                                                                                                                                                                    | Description             |
| ---------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------- |
| `contentFilter`        | `VIOLENCE`, `HATE`, `SEXUAL`, `MISCONDUCT`, `INSULTS`                                                                                                                                                      | Content safety filters  |
| `promptAttack`         | `JAILBREAK`, `PROMPT_INJECTION`, `PROMPT_LEAKAGE`                                                                                                                                                          | Prompt security filters |
| `sensitiveInformation` | `ADDRESS`, `EMAIL`, `PHONE`, `CREDIT_DEBIT_CARD_NUMBER`, and [more](../../../bedrock/latest/userguide/guardrails-sensitive-filters.md "../../../bedrock/latest/userguide/guardrails-sensitive-filters.md") | PII detection           |

## Policy effects

| Effect           | Behavior                                                                |
| ---------------- | ----------------------------------------------------------------------- |
| `forbid`         | Block requests that exceed the confidence threshold                     |
| `permit`         | Allow only requests below the threshold                                 |
| `suppressOutput` | Block the model’s response (output phase) when it exceeds the threshold |

## Step 7: Clean up

```
agentcore remove all --json
agentcore deploy
```
