# Deploy your Automated Reasoning policy in your application

After you've tested your Automated Reasoning policy and are satisfied with its performance,
you can deploy it for use in your application with Amazon Bedrock Guardrails.

## Save a version of your Automated Reasoning policy

When you're done testing your policy, you can create an immutable copy of the policy to use with your application.

### Using the console

1. In the left navigation, choose **Automated Reasoning**.
2. Choose the **Automated Reasoning** policy that you want to use with your application.
3. Choose **Save as new version**. You can use this version of your policy with your guardrail.

### Using the API

You can use the `CreateAutomatedReasoningPolicyVersion` API operation to create an immutable version of your Automated Reasoning policy.

#### Request parameters

The following parameters are required when creating a policy version:

`policyArn` (required)

The Amazon Resource Name (ARN) of the Automated Reasoning policy for which to create a version.

`lastUpdatedDefinitionHash` (required)

The hash of the policy definition for the new version. You can retreive this hash from the `GetAutomatedReasoningPolicy` API action.

#### Example

The following example shows how to create a version of an Automated Reasoning policy
using the AWS CLI:

```
aws bedrock create-automated-reasoning-policy-version \
  --policy-arn "arn:aws:bedrock:`us-east-1`:`111122223333`:automated-reasoning-policy/`lnq5hhz70wgk`" \
  --last-updated-definition-hash "`583463f067a8a4f49fc1206b4642fd40b1c877a0141109ad0a3cf213f87df0ad21455e049dbe43dda94253439d9d3710f9ae161b4842d825d7bda119ffb92a5d`"
```

Example response:

```
{
  "policyArn": "arn:aws:bedrock:us-east-1:111122223333:automated-reasoning-policy/lnq5hhz70wgk",
  "version": "1",
  "name": "MyHRPolicy"
}
```

## Add your Automated Reasoning policy to your

guardrail

Once you have a saved version of your Automated Reasoning policy, you can add the policy
to your guardrail.

### Using the console

1. In the left navigation, choose **Guardrails**, then choose **Create guardrail**.
2. When you get to the **Add Automated Reasoning checks** screen, choose **Enable Automated Reasoning policy**.
3. For **Policy name**, choose a saved version of an Automated Reasoning policy, then choose **Next**.
4. Finish creating your guardrail.

### Using the API

You can use the `CreateGuardrail` or `UpdateGuardrail` API operations to add an Automated Reasoning policy to your guardrail.

#### Request parameters

When creating or updating a Amazon Bedrock Guardrails, include the following parameter to enable Automated Reasoning checks in Amazon Bedrock Guardrails:

`automatedReasoningConfig`

The configuration for Automated Reasoning checks in Amazon Bedrock Guardrails.

`policyArn` (required)

The Amazon Resource Name (ARN) of the Automated Reasoning policy version to use
with your guardrail.

#### Example

The following example shows how to create a guardrail with an Automated Reasoning
policy using the AWS CLI:

```
aws bedrock create-guardrail \
  --name "HR-Policy-Guardrail" \
  --description "Guardrail for HR policy validation" \
  --automated-reasoning-config policyArn="arn:aws:bedrock:us-west-2:123456789012:automated-reasoning-policy/t3x7y9z2a5b8:1" \
  --topic-policy-config blockedTopics=[] \
  --content-policy-config filters=[] \
  --sensitive-information-policy-config piiEntities=[]
```
