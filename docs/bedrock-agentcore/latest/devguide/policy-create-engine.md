# Create a policy engine

A policy engine is a collection of policies that evaluates and authorizes agent tool calls.
When associated with a gateway, the policy engine intercepts all agent requests and determines
whether to allow or deny each action based on the defined policies.

###### Topics

- [Prerequisites](#policy-engine-prerequisites "#policy-engine-prerequisites")
- [Create a policy engine](#create-policy-engine-methods "#create-policy-engine-methods")
- [Using the policy engine ARN](#policy-engine-arn-usage "#policy-engine-arn-usage")

## Prerequisites

Before creating a policy engine, ensure you have a gateway setup. For more information, see
[Building a gateway](gateway-building.md "gateway-building.md").

## Create a policy engine

The following shows how to create a policy engine.

AWS CLI
Run the following code in a terminal to create a policy engine using the AWS CLI:

```

aws policy-registry create-policy-engine \
  --name my-policy-engine \
  --description "My Policy Engine"

```

The `policyEngineArn` in the response is the ARN to use when creating policies
or associating with gateway.

AWS Python SDK (Boto3)
The following Python code shows how to create a policy engine using the
AWS Python SDK (Boto3):

```

import boto3

client = boto3.client('policy-registry')

response = client.create_policy_engine(
    name='my-policy-engine',
    description='My Policy Engine'
)

print(f"Policy Engine ID: {response['policyEngineId']}")
print(f"Policy Engine ARN: {response['policyEngineArn']}")

```

## Using the policy engine ARN

The `policyEngineArn` returned when creating a policy engine is used for two main
purposes:

- **Creating policies** - Use the ARN when adding policies to
  the engine
- **Associating with gateways** - Use the ARN to enable policy
  enforcement on gateways

For more information about creating policies, see [Create a policy](policy-create-policies.md "policy-create-policies.md").
