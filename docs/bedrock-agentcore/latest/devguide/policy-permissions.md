# AgentCore Gateway and AgentCore Policy IAM Permissions

This guide provides the required IAM permissions for using Amazon Bedrock AgentCore Gateway with Amazon Bedrock AgentCore Policy for fine-grained authorization control using Cedar policies.

## Overview

When integrating Amazon Bedrock AgentCore Gateway with Amazon Bedrock AgentCore Policy, two distinct IAM roles are required:

1. **Gateway Execution Role** - The IAM role that Amazon Bedrock AgentCore Gateway assumes at runtime to invoke targets and evaluate Cedar policies
2. **Resource Management Role** - The IAM role that administrators use to create and manage Amazon Bedrock AgentCore Gateway and Amazon Bedrock AgentCore Policy resources

Both roles serve different purposes and require specific permissions. The Gateway Execution Role needs permissions to run Amazon Bedrock AgentCore Gateway operations, while the Resource Management Role needs permissions to configure and manage Amazon Bedrock AgentCore Gateway and Amazon Bedrock AgentCore Policy resources.

## Gateway Execution Role

The Gateway Execution Role is assumed by the Amazon Bedrock AgentCore Gateway service when processing requests. This role requires permissions to:

- Evaluate Cedar policies through the Amazon Bedrock AgentCore Policy
- Invoke targets such as Lambda functions and API Gateway endpoints
- Write logs and traces to CloudWatch and X-Ray
- Access secrets for authentication configurations

###### Critical Permissions for Amazon Bedrock AgentCore Policy Integration

The execution role must include these three permissions to use Amazon Bedrock AgentCore Gateway with Amazon Bedrock AgentCore Policy:

1. `bedrock-agentcore:AuthorizeAction` - Evaluates Cedar policies for authorization decisions
2. `bedrock-agentcore:PartiallyAuthorizeActions` - Lists tools the caller is authorized to invoke
3. `bedrock-agentcore:GetPolicyEngine` - Retrieves Amazon Bedrock AgentCore Policy configuration
   Without these permissions, the Gateway cannot perform policy authorization. This manifests in two ways: attaching a Policy Engine to an existing Gateway will result in an InternalServerException, and all tool invocations will be denied by default even if you have permit policies configured.

### Trust Policy

The Gateway Execution Role must trust the `bedrock-agentcore.amazonaws.com` service principal.

###### Important

Replace the following placeholders:

- `us-east-1` with the AWS Region
- `123456789012` with the AWS account ID

```
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Sid": "AllowBedrockAgentCoreAssumeRole",
      "Effect": "Allow",
      "Principal": {
        "Service": "bedrock-agentcore.amazonaws.com"
      },
      "Action": "sts:AssumeRole",
      "Condition": {
        "StringEquals": {
          "aws:SourceAccount": "123456789012"
        },
        "ArnLike": {
          "aws:SourceArn": "arn:aws:bedrock-agentcore:us-east-1:123456789012:*"
        }
      }
    }
  ]
}
```

### Permission Policy

This policy grants the Amazon Bedrock AgentCore Gateway the necessary permissions to evaluate Cedar policies through the Amazon Bedrock AgentCore Policy. The permissions are split into two statements following least-privilege principles.

###### Important

Replace these placeholders:

- `us-east-1` with the AWS Region
- `123456789012` with the AWS account ID
- `<gateway-id>` with the Gateway ID (or use `*` for all gateways)
- `<policy-engine-id>` with the Amazon Bedrock AgentCore Policy ID (or use `*` for all policy engines)

```
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Sid": "PolicyEngineConfiguration",
      "Effect": "Allow",
      "Action": [
        "bedrock-agentcore:GetPolicyEngine"
      ],
      "Resource": [
        "arn:aws:bedrock-agentcore:us-east-1:123456789012:policy-engine/<policy-engine-id>"
      ]
    },
    {
      "Sid": "PolicyEngineAuthorization",
      "Effect": "Allow",
      "Action": [
        "bedrock-agentcore:AuthorizeAction",
        "bedrock-agentcore:PartiallyAuthorizeActions"
      ],
      "Resource": [
        "arn:aws:bedrock-agentcore:us-east-1:123456789012:policy-engine/<policy-engine-id>",
        "arn:aws:bedrock-agentcore:us-east-1:123456789012:gateway/<gateway-id>"
      ]
    }
  ]
}
```

###### Note

- Additional permissions may be required depending on the Amazon Bedrock AgentCore Gateway integration type (e.g., Lambda functions, API Gateway endpoints). These permissions are not included here as they vary based on the specific integration.
- For Production: Replace the placeholders with specific resource IDs (e.g., `policy-engine/my-policy-engine-id` instead of `policy-engine/<policy-engine-id>`) to follow least-privilege principles, or use wildcards (`*`) to allow access to all resources of that type.

## Resource Management Role

The Resource Management Role is used by administrators to create and manage Amazon Bedrock AgentCore Gateway and Amazon Bedrock AgentCore Policy resources. This role requires permissions to:

- Create, update, and delete Gateways and Gateway targets
- Create, update, and delete Policy Engines and Cedar policies
- Pass the Gateway Execution Role to Amazon Bedrock AgentCore Gateway resources during creation
- Tag resources for organization and management
- Read IAM role information to validate execution role configurations

This role is separate from the Gateway Execution Role and is only needed when setting up or modifying Amazon Bedrock AgentCore Gateway and Amazon Bedrock AgentCore Policy configurations.

### Permission Policy

###### Important

Replace these placeholders:

- `us-east-1` with the AWS Region
- `123456789012` with the AWS account ID

```
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Sid": "GatewayManagement",
      "Effect": "Allow",
      "Action": [
        "bedrock-agentcore:CreateGateway",
        "bedrock-agentcore:UpdateGateway",
        "bedrock-agentcore:GetGateway",
        "bedrock-agentcore:DeleteGateway",
        "bedrock-agentcore:ListGateways",
        "bedrock-agentcore:CreateGatewayTarget",
        "bedrock-agentcore:UpdateGatewayTarget",
        "bedrock-agentcore:GetGatewayTarget",
        "bedrock-agentcore:DeleteGatewayTarget",
        "bedrock-agentcore:ListGatewayTargets"
      ],
      "Resource": [
        "arn:aws:bedrock-agentcore:us-east-1:123456789012:gateway/*"
      ]
    },
    {
      "Sid": "PolicyEngineManagement",
      "Effect": "Allow",
      "Action": [
        "bedrock-agentcore:CreatePolicyEngine",
        "bedrock-agentcore:UpdatePolicyEngine",
        "bedrock-agentcore:GetPolicyEngine",
        "bedrock-agentcore:DeletePolicyEngine",
        "bedrock-agentcore:ListPolicyEngines"
      ],
      "Resource": [
        "arn:aws:bedrock-agentcore:us-east-1:123456789012:policy-engine/*"
      ]
    },
    {
      "Sid": "PolicyManagement",
      "Effect": "Allow",
      "Action": [
        "bedrock-agentcore:CreatePolicy",
        "bedrock-agentcore:UpdatePolicy",
        "bedrock-agentcore:GetPolicy",
        "bedrock-agentcore:DeletePolicy",
        "bedrock-agentcore:ListPolicies"
      ],
      "Resource": [
        "arn:aws:bedrock-agentcore:us-east-1:123456789012:policy-engine/*/policy/*"
      ]
    },
    {
      "Sid": "PolicyGeneration",
      "Effect": "Allow",
      "Action": [
        "bedrock-agentcore:StartPolicyGeneration",
        "bedrock-agentcore:GetPolicyGeneration",
        "bedrock-agentcore:ListPolicyGenerations",
        "bedrock-agentcore:ListPolicyGenerationAssets"
      ],
      "Resource": [
        "arn:aws:bedrock-agentcore:us-east-1:123456789012:policy-engine/*/policy-generation/*"
      ]
    },
    {
      "Sid": "IAMPassRole",
      "Effect": "Allow",
      "Action": [
        "iam:PassRole"
      ],
      "Resource": [
        "arn:aws:iam::123456789012:role/*BedrockAgentCore*"
      ],
      "Condition": {
        "StringEquals": {
          "iam:PassedToService": "bedrock-agentcore.amazonaws.com"
        }
      }
    },
    {
      "Sid": "IAMReadAccess",
      "Effect": "Allow",
      "Action": [
        "iam:GetRole",
        "iam:GetRolePolicy",
        "iam:ListAttachedRolePolicies",
        "iam:ListRolePolicies"
      ],
      "Resource": [
        "arn:aws:iam::123456789012:role/*"
      ]
    },
    {
      "Sid": "PolicyScopeManagement",
      "Effect": "Allow",
      "Action": [
        "bedrock-agentcore:ManageResourceScopedPolicy",
        "bedrock-agentcore:ManageAdminPolicy"
      ],
      "Resource": [
        "arn:aws:bedrock-agentcore:us-east-1:123456789012:gateway/*"
      ]
    }
  ]
}
```

###### Policy Scope Management Permissions

The `ManageResourceScopedPolicy` and `ManageAdminPolicy` actions are permission-only gates that control what types of Cedar policies administrators can create:

- `ManageResourceScopedPolicy` - Grants permission to create Cedar policies that target specific gateway ARNs (e.g., policies applying to `gateway/my-gateway-123`)
- `ManageAdminPolicy` - Grants permission to create Cedar policies with wildcards (e.g., policies applying to `gateway/*`)
  Both permissions are required for full policy management capability. These are not API operations but rather authorization checks that determine the scope of Cedar policies that can be created through the Policy Management APIs.

###### Note

While the Resource field is included for consistency, these permission-only actions primarily gate capability at the action level rather than at the resource level.

## When Are Role Updates Required?

Determine whether Amazon Bedrock AgentCore Policy permissions need to be added to the Amazon Bedrock AgentCore Gateway execution role based on how the Amazon Bedrock AgentCore Gateway was created.

**Scenario 1: Gateway Created with Starter Toolkit**

**Status:** No action needed

The starter toolkit automatically creates an execution role with `bedrock-agentcore:*` wildcard permissions that include all Amazon Bedrock AgentCore Policy actions. The role is fully configured and ready to use.

**Scenario 2: Custom Execution Role**

**Status:** Action required

Custom IAM roles require the Amazon Bedrock AgentCore Policy permissions documented in this guide to be added manually. Follow the permission policies in the sections above.

**Scenario 3: Production Least-Privilege Configuration**

**Status:** Action required

Even when using the starter toolkit, production environments may require replacing wildcard permissions with specific actions that follow least-privilege principles.

## Troubleshooting

This section covers common issues when configuring IAM permissions for Amazon Bedrock AgentCore Gateway with Amazon Bedrock AgentCore Policy.

### InternalServerException During Policy Evaluation

**Symptom:** Gateway returns `InternalServerException - Policy evaluation failed` when attaching a Policy Engine to an existing Gateway, and all tool invocations are denied by default even with permit policies configured.

**Root Cause:** The Gateway Execution Role is missing the required Amazon Bedrock AgentCore Policy permissions. Without these permissions, the Gateway cannot perform policy authorization.

**Solution:** Ensure the Gateway Execution Role includes these three permissions:

```
{
  "Effect": "Allow",
  "Action": [
    "bedrock-agentcore:PartiallyAuthorizeActions",
    "bedrock-agentcore:AuthorizeAction",
    "bedrock-agentcore:GetPolicyEngine"
  ],
  "Resource": [
    "arn:aws:bedrock-agentcore:REGION:ACCOUNT:policy-engine/*",
    "arn:aws:bedrock-agentcore:REGION:ACCOUNT:gateway/*"
  ]
}
```

###### Note

If you attach a Policy Engine to an existing Gateway using the Policy Engine console, the IAM permissions may not be automatically updated. You must manually add these permissions to the Gateway's Service-Linked Role.

### Silent Failures in LOG_ONLY Mode

**Symptom:** Amazon Bedrock AgentCore Policy appears to work in LOG_ONLY mode but fails silently without proper error messages.

**Root Cause:** Missing `bedrock-agentcore:GetPolicyEngine` permission causes silent failures that only surface when switching to ENFORCED mode.

**Solution:** Always include `bedrock-agentcore:GetPolicyEngine` in the Gateway Execution Role, even when using LOG_ONLY mode for testing.

### Policy Engine Not Found Error

**Symptom:** Amazon Bedrock AgentCore Gateway returns errors indicating it cannot find or access the Amazon Bedrock AgentCore Policy.

**Root Cause:** The Gateway Execution Role's policy uses incorrect ARN patterns or is missing the policy-engine resource.

**Solution:** Ensure both the policy-engine AND gateway ARNs are included in the Resource array:

```
"Resource": [
  "arn:aws:bedrock-agentcore:us-east-1:123456789012:policy-engine/<policy-engine-id>",
  "arn:aws:bedrock-agentcore:us-east-1:123456789012:gateway/<gateway-id>"
]
```

###### Note

Both `AuthorizeAction` and `PartiallyAuthorizeActions` require access to BOTH the policy-engine and gateway resources.

### Debugging Tips

1. **Enable CloudWatch Logs** - Configure detailed logging for the Amazon Bedrock AgentCore Gateway to capture policy evaluation details
2. **Review X-Ray Traces** - Check AWS X-Ray traces to identify where authorization checks are failing
3. **Start with LOG_ONLY Mode** - Use LOG_ONLY mode initially to test Cedar policies without blocking requests
4. **Verify All Three Permissions** - Ensure `AuthorizeAction`, `PartiallyAuthorizeActions`, AND `GetPolicyEngine` are all present
5. **Switch to ENFORCED Mode** - Only after verifying all permissions work in LOG_ONLY mode, switch to ENFORCED mode

## Example: Creating Both IAM Roles

The following example demonstrates how to create both required IAM roles using the AWS CLI.

### Step 1: Create Gateway Execution Role

```
# Create the trust policy file
cat > gateway-trust-policy.json <<EOF
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Effect": "Allow",
      "Principal": {
        "Service": "bedrock-agentcore.amazonaws.com"
      },
      "Action": "sts:AssumeRole",
      "Condition": {
        "StringEquals": {
          "aws:SourceAccount": "123456789012"
        },
        "ArnLike": {
          "aws:SourceArn": "arn:aws:bedrock-agentcore:us-east-1:123456789012:*"
        }
      }
    }
  ]
}
EOF

# Create the IAM role
aws iam create-role \
  --role-name MyGatewayExecutionRole \
  --assume-role-policy-document file://gateway-trust-policy.json
```

### Step 2: Attach Permissions to Gateway Execution Role

```
# Create the permission policy file
cat > gateway-permissions.json <<EOF
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Sid": "PolicyEngineConfiguration",
      "Effect": "Allow",
      "Action": [
        "bedrock-agentcore:GetPolicyEngine"
      ],
      "Resource": [
        "arn:aws:bedrock-agentcore:us-east-1:123456789012:policy-engine/*"
      ]
    },
    {
      "Sid": "PolicyEngineAuthorization",
      "Effect": "Allow",
      "Action": [
        "bedrock-agentcore:AuthorizeAction",
        "bedrock-agentcore:PartiallyAuthorizeActions"
      ],
      "Resource": [
        "arn:aws:bedrock-agentcore:us-east-1:123456789012:policy-engine/*",
        "arn:aws:bedrock-agentcore:us-east-1:123456789012:gateway/*"
      ]
    }
  ]
}
EOF

# Attach the policy to the role
aws iam put-role-policy \
  --role-name MyGatewayExecutionRole \
  --policy-name GatewayPolicyEnginePermissions \
  --policy-document file://gateway-permissions.json
```

###### Note

This example shows only the Amazon Bedrock AgentCore Policy permissions. Additional permissions for Amazon Bedrock AgentCore Gateway targets (Lambda, API Gateway, etc.) should be added based on your specific integration requirements.

### Step 3: Next Steps

After configuring the execution role with the required Amazon Bedrock AgentCore Policy permissions, proceed to create and configure Amazon Bedrock AgentCore Policy resources. For detailed guidance, refer to:

- Creating a Policy Engine - See the [Create a policy engine](policy-create-engine.md "policy-create-engine.md")
- Writing Cedar Policies - See the [Cedar Policy Language Reference](https://docs.cedarpolicy.com "https://docs.cedarpolicy.com")

## Best Practices

1. **Use Separate Roles** - Maintain distinct roles for Amazon Bedrock AgentCore Gateway execution and resource management
2. **Apply Least Privilege** - Start with specific resource ARNs rather than wildcards in production
3. **Test with LOG_ONLY Mode** - Always test Amazon Bedrock AgentCore Policy integration in LOG_ONLY mode before enforcing policies
4. **Enable Monitoring** - Configure CloudWatch Logs and X-Ray tracing for troubleshooting and observability
5. **Version Control Policies** - Store Cedar policies in version control alongside infrastructure code
6. **Use Resource Tags** - Apply tags to organize and manage Amazon Bedrock AgentCore Gateway and Amazon Bedrock AgentCore Policy resources
7. **Regular Security Audits** - Periodically review IAM policies to ensure they follow least privilege principles
