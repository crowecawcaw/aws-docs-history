# Add policies to the Policy Engine

You can create one or more policies in your policy engine to control how agents
interact with your enterprise tools and data through Amazon Bedrock AgentCore Gateway.

###### Note

Use the policy engine ID from the previous step. The validation mode determines
how policy validation findings are handled: `FAIL_ON_ANY_FINDINGS` will
reject policies with validation issues, while `IGNORE_ALL_FINDINGS` will
accept them.

Select one of the following methods:

AWS CLI
Run the following code in a terminal to create a policy using the
AWS CLI:

```

aws bedrock-agentcore-control create-policy \
  --policy-engine-id my-policy-engine-id \
  --name my-policy \
  --validation-mode FAIL_ON_ANY_FINDINGS \
  --description "My Policy" \
  --definition '{
    "cedar": {
      "statement": "my-cedar-policy-statement"
    }
  }'

```

AWS Python SDK (Boto3)
The following Python code shows how to create a policy using the
AWS Python SDK (Boto3):

```

import boto3

client = boto3.client('bedrock-agentcore-control')

response = client.create_policy(
    policyEngineId='my-policy-engine-id',
    name='my-policy',
    validationMode='FAIL_ON_ANY_FINDINGS',
    description='My Policy',
    definition={
        'cedar': {
            'statement': 'my-cedar-policy-statement'
        }
    }
)
print(f"Policy ID: {response['policyId']}")

```
