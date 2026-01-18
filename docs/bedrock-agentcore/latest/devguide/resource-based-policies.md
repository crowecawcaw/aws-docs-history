# Resource-based policies for Amazon Bedrock AgentCore

Resource-based policies in Amazon Bedrock AgentCore allow you to control which principals (AWS accounts, IAM users, or IAM roles) can invoke and manage your Amazon Bedrock AgentCore Runtime and Gateway resources. You can attach IAM-style policies directly to your resources to define rules around who can start runtime sessions, invoke a gateway, or perform other management and invocation actions.

Resource-based policies work in conjunction with identity-based IAM policies to provide fine-grained access control for your Amazon Bedrock AgentCore resources. While identity-based policies are attached to IAM identities and specify what actions they can perform, resource-based policies are attached directly to resources and specify who can access them.

###### Topics

- [Supported resources](#resource-based-policies-supported-resources "#resource-based-policies-supported-resources")
- [How resource-based policies work](#resource-based-policies-how-they-work "#resource-based-policies-how-they-work")
- [Policy structure](#resource-based-policies-structure "#resource-based-policies-structure")
- [Supported actions](#resource-based-policies-supported-actions "#resource-based-policies-supported-actions")
- [Condition keys](#resource-based-policies-condition-keys "#resource-based-policies-condition-keys")
- [Common use cases and examples](#resource-based-policies-examples "#resource-based-policies-examples")
- [Managing resource policies](#resource-based-policies-managing "#resource-based-policies-managing")
- [Security best practices](#resource-based-policies-best-practices "#resource-based-policies-best-practices")
- [Troubleshooting](#resource-based-policies-troubleshooting "#resource-based-policies-troubleshooting")

## Supported resources

Amazon Bedrock AgentCore supports resource-based policies for the following resources:

- **Agent Runtime and Agent Endpoints** - Control access to agent invocation and management operations
- **Gateway** - Control access to gateway invocation operations

## How resource-based policies work

### Identity-based vs resource-based policies

| Aspect     | Identity-Based Policy                         | Resource-Based Policy                                      |
| ---------- | --------------------------------------------- | ---------------------------------------------------------- |
| Attachment | Attached to IAM users, roles, or groups       | Attached directly to Amazon Bedrock AgentCore resources    |
| Management | Managed through AWS IAM                       | Managed through Amazon Bedrock AgentCore APIs              |
| Specifies  | Actions and Resources (Principal is implicit) | Principals, Actions, and Conditions (Resource is implicit) |
| Use Case   | Define what an identity can do                | Define who can access a resource                           |

### Policy evaluation

When a request is made to a Amazon Bedrock AgentCore resource, AWS evaluates both identity-based and resource-based policies. The following table shows how different policy combinations affect access:

| IAM Policy    | Resource Policy | Result  |
| ------------- | --------------- | ------- |
| Grants access | Silent          | Allowed |
| Grants access | Grants access   | Allowed |
| Grants access | Denies access   | Denied  |
| Silent        | Silent          | Denied  |
| Silent        | Grants access   | Allowed |
| Silent        | Denies access   | Denied  |
| Denies access | Silent          | Denied  |
| Denies access | Allows access   | Denied  |
| Denies access | Denies access   | Denied  |

Key principles:

- **Explicit Deny Always Wins**: If any policy explicitly denies the action, access is denied regardless of other policies
- **Either Policy Can Allow**: If either identity-based or resource-based policy allows the action (and no policy denies it), access is granted
- **Default Deny**: If no policy explicitly permits an action, access is denied

### Hierarchical authorization for agent runtime and endpoint

Agent endpoints are addressable access points to specific versions of an agent runtime. Each endpoint points to a particular version of the runtime configuration, with a DEFAULT endpoint automatically routing to the latest version. When authorizing runtime API operations such as `InvokeAgentRuntime`, AWS evaluates both identity-based and resource-based policies for both the agent runtime and the agent endpoint being invoked.

For a request to be authorized, the following conditions must be met:

- The identity-based policies attached to the calling principal must allow the action on both the agent runtime and agent endpoint resources
- The resource-based policy on the agent runtime must allow the action (if a policy exists)
- The resource-based policy on the agent endpoint must allow the action (if a policy exists)

###### Cross-account access requirements

To provide cross-account access to a principal, you must create resource-based policies granting access for **both** the agent runtime and the agent endpoint. If either resource denies access or lacks an explicit allow statement, the request will be denied.

Example: Granting cross-account access requires policies on both resources:

```
// Policy for Agent Runtime
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Effect": "Allow",
      "Principal": {
        "AWS": "arn:aws:iam::123456789012:role/CrossAccountRole"
      },
      "Action": "bedrock-agentcore:InvokeAgentRuntime",
      "Resource": "*"
    }
  ]
}

// Policy for Agent Endpoint (for the endpoint that points to this runtime)
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Effect": "Allow",
      "Principal": {
        "AWS": "arn:aws:iam::123456789012:role/CrossAccountRole"
      },
      "Action": "bedrock-agentcore:InvokeAgentRuntime",
      "Resource": "*"
    }
  ]
}
```

### Authentication type considerations

The way you write resource-based policies depends on the authentication type configured for your Agent Runtime or Gateway:

SigV4 Authentication

Use specific AWS principals (IAM users, roles, or accounts) in the `Principal` element. For example: `"Principal": {"AWS": "arn:aws:iam::123456789012:role/MyRole"}`. The policy is evaluated in conjunction with the caller's IAM permissions.

OAuth Authentication

Must use wildcard principal (`"Principal": "*"`) in policy statements. OAuth tokens are validated by AWS Identity Service before policy evaluation. Only authenticated OAuth users with valid JWT tokens from the registered Identity Provider (IdP) can invoke the resource. Anonymous or unauthenticated requests are rejected before policy evaluation. Use condition keys to restrict access (e.g., `aws:SourceVpc`, `aws:SourceVpce`).

###### Important

An Agent Runtime or Gateway can only be configured with either SigV4 OR OAuth authentication at creation time, not both simultaneously. This means a single resource-based policy applies to only one authentication type.

## Policy structure

A resource-based policy is a JSON document with the following structure:

```
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Sid": "StatementId",
      "Effect": "Allow",
      "Principal": {
        "AWS": "arn:aws:iam::account-id:role/role-name"
      },
      "Action": "bedrock-agentcore:ActionName",
      "Resource": "*",
      "Condition": {
        "ConditionOperator": {
          "ConditionKey": "ConditionValue"
        }
      }
    }
  ]
}
```

## Supported actions

### Agent Runtime actions

- `bedrock-agentcore:InvokeAgentRuntime` - Invoke an agent runtime
- `bedrock-agentcore:InvokeAgentRuntimeForUser` - Invoke an agent runtime endpoint with X-Amzn-Bedrock-AgentCore-Runtime-User-Id header
- `bedrock-agentcore:InvokeAgentRuntimeWithWebSocketStream` - Invoke an agent runtime with WebSocket stream
- `bedrock-agentcore:InvokeAgentRuntimeWithWebSocketStreamForUser` - Invoke an agent runtime with WebSocket stream with X-Amzn-Bedrock-AgentCore-Runtime-User-Id header
- `bedrock-agentcore:StopRuntimeSession` - Stop an active runtime session
- `bedrock-agentcore:GetAgentCard` - Retrieve agent card information

### Gateway actions

- `bedrock-agentcore:InvokeGateway` - Invoke a gateway

## Condition keys

You can use condition keys to further refine access control in your policies. For a complete list of available condition keys, see [AWS Global Condition Context Keys](../../../IAM/latest/UserGuide/reference_policies_condition-keys.md "../../../IAM/latest/UserGuide/reference_policies_condition-keys.md") in the _IAM User Guide_.

## Common use cases and examples

This section provides practical examples of resource-based policies for common scenarios. These examples use simplified syntax where `"Resource": "*"` represents the resource to which the policy is attached.

### Allow roles in another AWS account

Grant API access to specific roles in a different AWS account:

```
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Effect": "Allow",
      "Principal": {
        "AWS": [
          "arn:aws:iam::123456789012:role/DeveloperRole",
          "arn:aws:iam::123456789012:role/AdminRole"
        ]
      },
      "Action": "bedrock-agentcore:InvokeAgentRuntime",
      "Resource": "*"
    }
  ]
}
```

### Deny traffic based on source IP address

Block incoming traffic from specific IP address ranges:

```
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Effect": "Allow",
      "Principal": {
        "AWS": "arn:aws:iam::123456789012:role/ApplicationRole"
      },
      "Action": "bedrock-agentcore:InvokeAgentRuntime",
      "Resource": "*"
    },
    {
      "Effect": "Deny",
      "Principal": {
        "AWS": "arn:aws:iam::123456789012:role/ApplicationRole"
      },
      "Action": "bedrock-agentcore:InvokeAgentRuntime",
      "Resource": "*",
      "Condition": {
        "IpAddress": {
          "aws:SourceIp": [
            "192.0.2.0/24",
            "198.51.100.0/24"
          ]
        }
      }
    }
  ]
}
```

### Allow traffic only from specific VPC

Restrict access to requests from a specific VPC:

```
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Effect": "Allow",
      "Principal": {
        "AWS": "arn:aws:iam::123456789012:role/ApplicationRole"
      },
      "Action": "bedrock-agentcore:InvokeAgentRuntime",
      "Resource": "*"
    },
    {
      "Effect": "Deny",
      "Principal": {
        "AWS": "arn:aws:iam::123456789012:role/ApplicationRole"
      },
      "Action": "bedrock-agentcore:InvokeAgentRuntime",
      "Resource": "*",
      "Condition": {
        "StringNotEquals": {
          "aws:SourceVpc": "vpc-1a2b3c4d"
        }
      }
    }
  ]
}
```

### OAuth authentication with VPC restriction

When your Agent Runtime or Gateway is configured with OAuth authentication, you must use a wildcard principal. This example restricts OAuth-authenticated requests to a specific VPC:

```
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Sid": "AllowOAuthFromVPC",
      "Effect": "Allow",
      "Principal": "*",
      "Action": "bedrock-agentcore:InvokeAgentRuntime",
      "Resource": "*",
      "Condition": {
        "StringEquals": {
          "aws:SourceVpc": "vpc-1a2b3c4d"
        }
      }
    }
  ]
}
```

###### Important notes for OAuth

- The wildcard principal (`"Principal": "*"`) is **required** for OAuth authentication
- OAuth tokens are validated by AWS Identity Service before policy evaluation
- Only users with valid JWT tokens from your registered Identity Provider can access the resource
- Anonymous or unauthenticated requests are rejected before reaching policy evaluation
- Use condition keys (like `aws:SourceVpc`, `aws:SourceVpce`) to further restrict access

## Managing resource policies

Select one of the following methods:

AWS CLI

###### Create or update a resource policy

Use the `put-resource-policy` command:

```
aws bedrock-agentcore-control put-resource-policy \
    --resource-arn arn:aws:bedrock-agentcore:us-west-2:111122223333:runtime/AGENTID \
    --policy file://policy.json
```

###### Get a resource policy

Use the `get-resource-policy` command:

```
aws bedrock-agentcore-control get-resource-policy \
    --resource-arn arn:aws:bedrock-agentcore:us-west-2:111122223333:runtime/AGENTID
```

###### Delete a resource policy

Use the `delete-resource-policy` command:

```
aws bedrock-agentcore-control delete-resource-policy \
    --resource-arn arn:aws:bedrock-agentcore:us-west-2:111122223333:runtime/AGENTID
```

Python (Boto3)
The following examples show how to manage resource policies using the AWS Python SDK (Boto3):

```
import boto3
import json

client = boto3.client('bedrock-agentcore-control', region_name='us-west-2')

# Put resource policy
policy = {
    "Version": "2012-10-17",
    "Statement": [
        {
            "Effect": "Allow",
            "Principal": {"AWS": "arn:aws:iam::123456789012:role/MyRole"},
            "Action": "bedrock-agentcore:InvokeAgentRuntime",
            "Resource": "*"
        }
    ]
}

response = client.put_resource_policy(
    resourceArn='arn:aws:bedrock-agentcore:us-west-2:111122223333:runtime/AGENTID',
    policy=json.dumps(policy)
)

# Get resource policy
response = client.get_resource_policy(
    resourceArn='arn:aws:bedrock-agentcore:us-west-2:111122223333:runtime/AGENTID'
)
print(response['policy'])

# Delete resource policy
response = client.delete_resource_policy(
    resourceArn='arn:aws:bedrock-agentcore:us-west-2:111122223333:runtime/AGENTID'
)
```

## Security best practices

### Grant least privilege

Grant only the minimum permissions necessary for your use case:

```
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Effect": "Allow",
      "Principal": {
        "AWS": "arn:aws:iam::111122223333:role/ApplicationRole"
      },
      "Action": "bedrock-agentcore:InvokeAgentRuntime",
      "Resource": "*"
    }
  ]
}
```

### Prevent confused deputy

Always use condition keys when granting access to AWS services:

```
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Effect": "Allow",
      "Principal": {
        "Service": "lambda.amazonaws.com"
      },
      "Action": "bedrock-agentcore:InvokeGateway",
      "Resource": "*",
      "Condition": {
        "StringEquals": {
          "aws:SourceAccount": "111122223333"
        },
        "ArnEquals": {
          "aws:SourceArn": "arn:aws:lambda:us-west-2:111122223333:function/SpecificFunction"
        }
      }
    }
  ]
}
```

### Use explicit deny for critical controls

Use explicit deny statements for security-critical restrictions:

```
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Sid": "DenyAllExceptVPC",
      "Effect": "Deny",
      "Principal": "*",
      "Action": "bedrock-agentcore:InvokeAgentRuntime",
      "Resource": "*",
      "Condition": {
        "StringNotEquals": {
          "aws:SourceVpc": "vpc-12345678"
        },
        "Bool": {
          "aws:ViaAWSService": "false"
        }
      }
    }
  ]
}
```

## Troubleshooting

### Access denied errors

If you receive an "Access Denied" error:

- **Check both policies**: Verify both identity-based and resource-based policies
- **Look for explicit denies**: An explicit deny in any policy overrides all allows
- **Verify principal ARN**: Ensure the principal ARN in the policy matches the caller
- **Check conditions**: Verify all condition keys evaluate to true
- **Review SCPs**: Organization service control policies can override resource policies

### Policy validation errors

Common policy validation errors:

- **Invalid JSON**: Ensure your policy is valid JSON
- **Invalid ARN format**: Verify all ARNs follow the correct format
- **Unsupported actions**: Check that all actions are supported for the resource type
- **Missing required elements**: Ensure Version, Statement, Effect, Principal, and Action are present
