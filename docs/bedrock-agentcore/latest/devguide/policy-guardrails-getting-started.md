

# Getting started with guardrails
<a name="policy-guardrails-getting-started"></a>

Guardrails let you add content filtering to your agent’s gateway. When a guardrail detects content your policy forbids, such as violent content, the gateway blocks the request before it reaches your agent.

This guide walks through setting up a policy with a guardrail that blocks violent content on an HTTP gateway with a runtime target. The AgentCore CLI drives the whole flow in one project, so the following steps lead with it. Each step that maps to a control-plane API also shows the equivalent AWS CLI and boto3 code. For reference details on the guardrail types, categories, effects, and thresholds, see [Guardrails in policies](policy-guardrails-in-policies.md).

**Topics**
+ [Prerequisites](#policy-guardrails-getting-started-prerequisites)
+ [Step 1: Create a project](#policy-guardrails-getting-started-create)
+ [Step 2: Wire the engine, gateway, and target](#policy-guardrails-getting-started-wire)
+ [Step 3: Deploy infrastructure first](#policy-guardrails-getting-started-deploy-infra)
+ [Step 4: Add the policy](#policy-guardrails-getting-started-add-policy)
+ [Step 5: Deploy the policies](#policy-guardrails-getting-started-deploy-policy)
+ [Step 6: Invoke through the gateway](#policy-guardrails-getting-started-invoke)
+ [Available guardrail categories](#policy-guardrails-getting-started-categories)
+ [Policy effects](#policy-guardrails-getting-started-effects)
+ [Step 7: Clean up](#policy-guardrails-getting-started-cleanup)

## Prerequisites
<a name="policy-guardrails-getting-started-prerequisites"></a>

Before starting, make sure you have the following:
+  ** AWS credentials** configured.
+  **AgentCore CLI version 0.20.0 or later**. Earlier versions don’t include the policy form and enforcement mode options used in this guide.

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
<a name="policy-guardrails-getting-started-create"></a>

```
agentcore create --name MyAgent --language Python --framework Strands \
  --model-provider Bedrock --memory none

cd MyAgent
```

## Step 2: Wire the engine, gateway, and target
<a name="policy-guardrails-getting-started-wire"></a>

**Example**  

1. 

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

1. Create the policy engine:

   ```
   aws bedrock-agentcore-control create-policy-engine --name MyPolicyEngine
   ```

1. Create the gateway with the engine attached in `ENFORCE` mode, then add the target. Both take the engine ARN returned earlier. For more information, see [Create gateway with Policy Engine](create-gateway-with-policy.md) for the full request, and [Set up a gateway](gateway-building.md) for the target.

1. Create the policy engine:

   ```
   import boto3
   
   client = boto3.client('bedrock-agentcore-control')
   
   engine = client.create_policy_engine(name='MyPolicyEngine')
   client.get_waiter('policy_engine_active').wait(
       policyEngineId=engine['policyEngineId']
   )
   print(engine['policyEngineId'], engine['policyEngineArn'])
   ```

1. Pass `policyEngineConfiguration={'arn': engine['policyEngineArn'], 'mode': 'ENFORCE'}` to `create_gateway`, then create the gateway target. For more information, see [Create gateway with Policy Engine](create-gateway-with-policy.md).

## Step 3: Deploy infrastructure first
<a name="policy-guardrails-getting-started-deploy-infra"></a>

```
agentcore deploy
```

This deploys the runtime, gateway, gateway target, and policy engine. The policy itself is added next, because it needs the deployed gateway ARN.

## Step 4: Add the policy
<a name="policy-guardrails-getting-started-add-policy"></a>

**Example**  

1. Build the guardrail statement from flags, without writing Dogwood yourself:

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

   Run `agentcore add policy` with no flags for an interactive wizard that prompts for the same values. The `--form-*` flags write the statement into `agentcore/agentcore.json`, using a default data path of `context.input.prompt` and a default threshold of `0.2`. The stored statement is scoped with `resource is AgentCore::Gateway`; the CLI substitutes the deployed gateway’s ARN when it creates the policy, which is why the gateway must be deployed first.

1. On this surface, you write the statement yourself and must name the deployed gateway’s ARN. AgentCore rejects a statement that names a specific action unless the resource is also a specific gateway. Take the ARN from `agentcore status` or `get-gateway`:

   ```
   aws bedrock-agentcore-control create-policy \
     --policy-engine-id MyPolicyEngine-a1b2c3d4e5 \
     --name BlockViolence \
     --validation-mode IGNORE_ALL_FINDINGS \
     --enforcement-mode ACTIVE \
     --definition '{
       "policy": {
         "statement": "forbid (principal, action == AgentCore::Action::\"MyTarget___POST:/invocations\", resource == AgentCore::Gateway::\"<gateway-arn>\") when guardrails { BedrockGuardrails::ContentFilter([\"VIOLENCE\"], [context.input.prompt])[\"VIOLENCE\"].confidenceScore.greaterThan(decimal(\"0.2\")) };"
       }
     }'
   ```

1. Create the same policy using the AWS SDK for Python:

   ```
   import boto3
   
   client = boto3.client('bedrock-agentcore-control')
   
   GATEWAY_ARN = '<gateway-arn>'  # from agentcore status or get_gateway
   
   statement = (
       'forbid (principal, '
       'action == AgentCore::Action::"MyTarget___POST:/invocations", '
       f'resource == AgentCore::Gateway::"{GATEWAY_ARN}") '
       'when guardrails { BedrockGuardrails::ContentFilter('
       '["VIOLENCE"], [context.input.prompt])["VIOLENCE"]'
       '.confidenceScore.greaterThan(decimal("0.2")) };'
   )
   
   response = client.create_policy(
       policyEngineId='MyPolicyEngine-a1b2c3d4e5',
       name='BlockViolence',
       validationMode='IGNORE_ALL_FINDINGS',
       enforcementMode='ACTIVE',
       definition={'policy': {'statement': statement}},
   )
   # CreatePolicy returns 202 - wait for the terminal status
   client.get_waiter('policy_active').wait(
       policyEngineId='MyPolicyEngine-a1b2c3d4e5',
       policyId=response['policyId'],
   )
   print(response['policyId'])
   ```

This creates a policy that blocks requests with violent content.

### Step 4b: Add a permissive policy
<a name="policy-guardrails-getting-started-add-permissive"></a>

Because a policy engine in ENFORCE mode denies all actions unless explicitly permitted, add a permissive policy so benign requests can pass through and reach your agent:

**Example**  

1. 

   ```
   agentcore add policy \
     --name allowallBlockViolence \
     --engine MyPolicyEngine \
     --statement 'permit (principal, action, resource is AgentCore::Gateway);' \
     --validation-mode IGNORE_ALL_FINDINGS \
     --enforcement-mode ACTIVE
   ```

1. 

   ```
   aws bedrock-agentcore-control create-policy \
     --policy-engine-id MyPolicyEngine-a1b2c3d4e5 \
     --name allowallBlockViolence \
     --validation-mode IGNORE_ALL_FINDINGS \
     --enforcement-mode ACTIVE \
     --definition '{
       "policy": {
         "statement": "permit (principal, action, resource is AgentCore::Gateway);"
       }
     }'
   ```

1. 

   ```
   import boto3
   
   client = boto3.client('bedrock-agentcore-control')
   
   response = client.create_policy(
       policyEngineId='MyPolicyEngine-a1b2c3d4e5',
       name='allowallBlockViolence',
       validationMode='IGNORE_ALL_FINDINGS',
       enforcementMode='ACTIVE',
       definition={'policy': {'statement':
           'permit (principal, action, resource is AgentCore::Gateway);'}},
   )
   # CreatePolicy returns 202 - wait for the terminal status
   client.get_waiter('policy_active').wait(
       policyEngineId='MyPolicyEngine-a1b2c3d4e5',
       policyId=response['policyId'],
   )
   print(response['policyId'])
   ```

## Step 5: Deploy the policies
<a name="policy-guardrails-getting-started-deploy-policy"></a>

```
agentcore deploy
```

This step is specific to the AgentCore CLI: `agentcore add` only edits the project configuration, and `deploy` is what calls `CreatePolicy`. On the AWS CLI and boto3 the policies were already created in Step 4.

## Step 6: Invoke through the gateway
<a name="policy-guardrails-getting-started-invoke"></a>

```
# Tripping prompt - should be blocked
agentcore invoke --gateway MyGateway --gateway-target-name MyTarget \
  --prompt "i will kill you"

# Benign control prompt - should succeed
agentcore invoke --gateway MyGateway --gateway-target-name MyTarget \
  --prompt "hello"
```

Expected blocked result (`forbid` \+ `ACTIVE`):

```
403: "Request Denied: Agent runtime request not allowed due to policy enforcement [Policy evaluation denied due to blockviolence-xxxxx]"
```

## Available guardrail categories
<a name="policy-guardrails-getting-started-categories"></a>


| Category | Filters | Description | 
| --- | --- | --- | 
|  `contentFilter`  |  `VIOLENCE`, `HATE`, `SEXUAL`, `MISCONDUCT`, `INSULTS`  | Content safety filters | 
|  `promptAttack`  |  `JAILBREAK`, `PROMPT_INJECTION`, `PROMPT_LEAKAGE`  | Prompt security filters | 
|  `sensitiveInformation`  |  `ADDRESS`, `EMAIL`, `PHONE`, `CREDIT_DEBIT_CARD_NUMBER`, and [more](https://docs.aws.amazon.com/bedrock/latest/userguide/guardrails-sensitive-filters.html)  | PII detection | 

## Policy effects
<a name="policy-guardrails-getting-started-effects"></a>


| Effect | Behavior | 
| --- | --- | 
|  `forbid`  | Block requests that exceed the confidence threshold | 
|  `permit`  | Allow only requests below the threshold | 
|  `suppressOutput`  | Block the model’s response (output phase) when it exceeds the threshold | 

## Step 7: Clean up
<a name="policy-guardrails-getting-started-cleanup"></a>

**Example**  

1. 

   ```
   agentcore remove all --json
   agentcore deploy
   ```

1. Detach the engine from the gateway first. To construct the `update-gateway` request, see [Update existing gateway with Policy Engine](update-gateway-with-policy.md), and omit `policyEngineConfiguration`.

1. Delete the policies, then the engine. An engine that still contains policies cannot be deleted:

   ```
   aws bedrock-agentcore-control delete-policy \
     --policy-engine-id MyPolicyEngine-a1b2c3d4e5 --policy-id BlockViolence-a1b2c3d4e5
   aws bedrock-agentcore-control delete-policy \
     --policy-engine-id MyPolicyEngine-a1b2c3d4e5 --policy-id allowallBlockViolence-f6g7h8i9j0
   aws bedrock-agentcore-control delete-policy-engine \
     --policy-engine-id MyPolicyEngine-a1b2c3d4e5
   ```

1. 

   ```
   import boto3
   
   client = boto3.client('bedrock-agentcore-control')
   
   ENGINE_ID = 'MyPolicyEngine-a1b2c3d4e5'
   GATEWAY_ID = 'MyGateway-a1b2c3d4e5'
   
   # 1. Detach the engine - an attached engine cannot be deleted.
   #    Resend the required gateway settings, but omit policyEngineConfiguration.
   gateway = client.get_gateway(gatewayIdentifier=GATEWAY_ID)
   update_request = {
       'gatewayIdentifier': GATEWAY_ID,
       'name': gateway['name'],
       'roleArn': gateway['roleArn'],
       'authorizerType': gateway['authorizerType'],
   }
   for field in ('protocolType', 'authorizerConfiguration'):
       if field in gateway:
           update_request[field] = gateway[field]
   client.update_gateway(**update_request)
   
   # 2. Delete every policy - an engine that still holds policies cannot be deleted.
   for policy in client.list_policy_summaries(
       policyEngineId=ENGINE_ID
   )['policySummaries']:
       client.delete_policy(policyEngineId=ENGINE_ID, policyId=policy['policyId'])
       client.get_waiter('policy_deleted').wait(
           policyEngineId=ENGINE_ID, policyId=policy['policyId']
       )
   
   # 3. Delete the engine
   client.delete_policy_engine(policyEngineId=ENGINE_ID)
   client.get_waiter('policy_engine_deleted').wait(policyEngineId=ENGINE_ID)
   ```

   Omitting `policyEngineConfiguration` from `update_gateway` detaches the engine, because the call replaces the gateway’s configuration rather than merging into it.