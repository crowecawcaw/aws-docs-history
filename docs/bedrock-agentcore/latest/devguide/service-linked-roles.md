# Using service-linked roles for Amazon Bedrock AgentCore

Amazon Bedrock AgentCore uses AWS Identity and Access Management (IAM) service-linked roles. A service-linked role is a unique type of IAM role that is linked directly to AgentCore. Service-linked roles are predefined by AgentCore and include all the permissions that the service requires to call other AWS services on your behalf.

A service-linked role makes using AgentCore easier because you don't have to manually add the necessary permissions. AgentCore defines the permissions of its service-linked roles, and unless defined otherwise, only AgentCore can assume its roles. The defined permissions include the trust policy and the permissions policy, and that permissions policy cannot be attached to any other IAM entity.

You can delete the roles only after first deleting their related resources. This protects your AgentCore resources because you can't inadvertently remove permission to access the resources.

AgentCore uses the following service-linked roles:

- `AWSServiceRoleForBedrockAgentCoreNetwork` - Manages network interfaces in your VPC
- `AWSServiceRoleForBedrockAgentCoreRuntimeIdentity` - Manages workload identity access tokens and OAuth credentials for agent runtimes

## AgentCore service-linked role permissions

### Network service-linked role

AgentCore uses the service-linked role named `AWSServiceRoleForBedrockAgentCoreNetwork` to allow AgentCore to create and manage network interfaces in your VPC on your behalf.

The `AWSServiceRoleForBedrockAgentCoreNetwork` service-linked role trusts the following services to assume the role:

- `network.bedrock-agentcore.amazonaws.com`

The role permissions policy allows AgentCore to complete the following actions on the specified resources:

You can view the complete policy at [BedrockAgentCoreNetworkServiceRolePolicy](../../../aws-managed-policy/latest/reference/BedrockAgentCoreNetworkServiceRolePolicy.md "../../../aws-managed-policy/latest/reference/BedrockAgentCoreNetworkServiceRolePolicy.md").

```
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Sid": "AllowCreateEniInAnySubnet",
            "Effect": "Allow",
            "Action": "ec2:CreateNetworkInterface",
            "Resource": "arn:aws:ec2:*:*:subnet/*"
        },
        {
            "Sid": "AllowCreateEniWithSecurityGroups",
            "Effect": "Allow",
            "Action": "ec2:CreateNetworkInterface",
            "Resource": "arn:aws:ec2:*:*:security-group/*"
        },
        {
            "Sid": "AllowCreateEniWithBedrockManagedRequestTag",
            "Effect": "Allow",
            "Action": "ec2:CreateNetworkInterface",
            "Resource": "arn:aws:ec2:*:*:network-interface/*",
            "Condition": {
                "ForAllValues:StringEquals": {
                    "aws:TagKeys": [
                        "AmazonBedrockAgentCoreManaged"
                    ]
                },
                "StringEquals": {
                    "aws:RequestTag/AmazonBedrockAgentCoreManaged": "true"
                }
            }
        },
        {
            "Sid": "AllowTagEniOnCreate",
            "Effect": "Allow",
            "Action": "ec2:CreateTags",
            "Resource": "arn:aws:ec2:*:*:network-interface/*",
            "Condition": {
                "StringEquals": {
                    "ec2:CreateAction": "CreateNetworkInterface"
                }
            }
        },
        {
            "Sid": "AllowManageEniWhenBedrockManaged",
            "Effect": "Allow",
            "Action": [
                "ec2:DeleteNetworkInterface",
                "ec2:AssignPrivateIpAddresses",
                "ec2:UnassignPrivateIpAddresses",
                "ec2:CreateNetworkInterfacePermission"
            ],
            "Resource": "arn:aws:ec2:*:*:network-interface/*",
            "Condition": {
                "StringEquals": {
                    "aws:ResourceTag/AmazonBedrockAgentCoreManaged": "true"
                }
            }
        },
        {
            "Sid": "AllowGetSecurityGroupsForVpc",
            "Effect": "Allow",
            "Action": [
                "ec2:GetSecurityGroupsForVPC"
            ],
            "Resource": "arn:aws:ec2:*:*:vpc/*"
        },
        {
            "Sid": "AllowDescribeNetworkingResources",
            "Effect": "Allow",
            "Action": [
                "ec2:DescribeNetworkInterfaces",
                "ec2:DescribeSecurityGroups",
                "ec2:DescribeSubnets",
                "ec2:DescribeVpcs"
            ],
            "Resource": "*"
        }
    ]
}
```

### Identity service-linked role

AgentCore uses the service-linked role named `AWSServiceRoleForBedrockAgentCoreRuntimeIdentity` to allow AgentCore to manage workload identity access tokens and OAuth credentials on your behalf.

The `AWSServiceRoleForBedrockAgentCoreRuntimeIdentity` service-linked role trusts the following services to assume the role:

- `runtime-identity.bedrock-agentcore.amazonaws.com`

The role permissions policy allows AgentCore to complete these actions on the specified resources.

You can view the complete policy at [BedrockAgentCoreRuntimeIdentityServiceRolePolicy](../../../aws-managed-policy/latest/reference/BedrockAgentCoreRuntimeIdentityServiceRolePolicy.md "../../../aws-managed-policy/latest/reference/BedrockAgentCoreRuntimeIdentityServiceRolePolicy.md").

```
{
    "Version": "2012-10-17",
    "Statement": {
        "Sid": "AllowWorkloadIdentityAccess",
        "Effect": "Allow",
        "Action": [
            "bedrock-agentcore:GetWorkloadAccessToken",
            "bedrock-agentcore:GetWorkloadAccessTokenForJWT",
            "bedrock-agentcore:GetWorkloadAccessTokenForUserId"
        ],
        "Resource": [
            "arn:aws:bedrock-agentcore:*:*:workload-identity-directory/default",
            "arn:aws:bedrock-agentcore:*:*:workload-identity-directory/default/workload-identity/*"
        ]
    }
}
```

For information about changes to this policy, see [AgentCore updates to AWS managed policies](security-iam-awsmanpol.md#security-iam-awsmanpol-updates "security-iam-awsmanpol.md#security-iam-awsmanpol-updates").

###### Understanding the Identity Feature

The service-linked role is used to support OAuth authentication and JWT bearer token features for AgentCore Runtime resources. This feature allows agent runtimes to securely manage workload identities and access external OAuth providers on behalf of users.

###### Key Benefits of Identity Management

- **Simplified Permission Management**: Eliminates the need to manually configure IAM policies for workload identity access
- **Secure Token Management**: Provides secure access to workload access tokens for OAuth flows
- **User Federation**: Enables three-legged OAuth flows for accessing external services like Google Drive, Microsoft Graph, etc.
- **Automatic Provisioning**: Service-linked role is created automatically when needed

###### How Identity Management Works

When you invoke an AgentCore Runtime with OAuth authentication or JWT bearer tokens:

1. You configure JWT authorizer settings (discovery URL, allowed clients, allowed audiences) during runtime creation
2. AgentCore creates the service-linked role automatically to manage workload identity permissions
3. The runtime uses the service-linked role to exchange JWT tokens for workload access tokens
4. Your agent code can use these tokens to access external OAuth providers and services
5. All token management is handled securely through the AgentCore Identity service

###### Migration from Legacy Approach

For existing agents (created before October 13, 2025)

- Continue to use manual IAM policies attached to the agent execution role
- No automatic migration - existing behavior is preserved

For new agents (created on or after October 13, 2025)

- Automatically use the service-linked role approach
- No manual IAM policy configuration required
- Simplified setup and management

The service-linked role ensures that AgentCore can only access workload identity resources that are explicitly associated with your agent runtimes, maintaining secure isolation and clear resource attribution.

For implementation details, see [Authenticate and authorize with Inbound Auth and Outbound Auth](runtime-oauth.md "runtime-oauth.md").

## Creating a service-linked role for AgentCore

You don't need to manually create service-linked roles. AgentCore creates them automatically when needed:

- **Network service-linked role**: Created when you create an AgentCore Runtime, Code Interpreter, or Browser resources with VPC configuration
- **Identity service-linked role**: Created when you create or update an AgentCore Runtime on or after **October 13, 2025**

If you delete a service-linked role and then need to create it again, you can use the same process to re-create the role in your account. When you create the appropriate AgentCore resources, AgentCore creates the service-linked role for you again.

### Permissions required to create a service-linked role

You must configure permissions to allow an IAM entity (such as a user, group, or role) to create, edit, or delete a service-linked role. The IAM entity needs to have the following permissions:

###### For the Network service-linked role

```
{
    "Action": "iam:CreateServiceLinkedRole",
    "Effect": "Allow",
    "Resource": "arn:aws:iam::*:role/aws-service-role/network.bedrock-agentcore.amazonaws.com/AWSServiceRoleForBedrockAgentCoreNetwork",
    "Condition": {
        "StringLike": {
            "iam:AWSServiceName": "network.bedrock-agentcore.amazonaws.com"
        }
    }
}
```

###### For the Identity service-linked role

```
{
    "Sid": "CreateBedrockAgentCoreRuntimeIdentityServiceLinkedRolePermissions",
    "Effect": "Allow",
    "Action": "iam:CreateServiceLinkedRole",
    "Resource": "arn:aws:iam::*:role/aws-service-role/runtime-identity.bedrock-agentcore.amazonaws.com/AWSServiceRoleForBedrockAgentCoreRuntimeIdentity",
    "Condition": {
        "StringEquals": {
            "iam:AWSServiceName": "runtime-identity.bedrock-agentcore.amazonaws.com"
        }
    }
}
```

These permissions are already included in the AWS managed policy
[BedrockAgentCoreFullAccess](../../../aws-managed-policy/latest/reference/BedrockAgentCoreFullAccess.md "../../../aws-managed-policy/latest/reference/BedrockAgentCoreFullAccess.md").

## Editing a service-linked role for AgentCore

AgentCore does not allow you to edit the `AWSServiceRoleForBedrockAgentCoreNetwork` or `AWSServiceRoleForBedrockAgentCoreRuntimeIdentity` service-linked roles. After you create a service-linked role, you cannot change the name of the role because various entities might reference the role. However, you can edit the description of the role using IAM. For more information, see
[Editing a service-linked role](../../../IAM/latest/UserGuide/using-service-linked-roles.md#edit-service-linked-role "../../../IAM/latest/UserGuide/using-service-linked-roles.md#edit-service-linked-role").

## Deleting a service-linked role for AgentCore

If you no longer need to use a feature or service that requires a service-linked role, we recommend that you delete that role. That way you don't have an unused entity that is not actively monitored or maintained. However, you must delete all your AgentCore resources that use the service-linked role before you can delete the role:

- **Network service-linked role**: Delete all AgentCore Runtime, Code Interpreter, and Browser resources with VPC configuration
- **Identity service-linked role**: Delete all AgentCore Runtime resources

### Cleaning up a service-linked role

Before you can use IAM to delete a service-linked role, you must first confirm that the role has no active sessions and remove any resources used by the role.

###### To check whether the service-linked role has an active session in the IAM console

1. Sign in to the AWS Management Console and open the IAM console at [https://console.aws.amazon.com/iam/](https://console.aws.amazon.com/iam/ "https://console.aws.amazon.com/iam/").
2. In the navigation pane of the IAM console, choose **Roles**, and then choose the name (not the check box) of the `AWSServiceRoleForBedrockAgentCoreNetwork` role.
3. On the **Summary** page for the selected role, choose the **Access Advisor** tab.
4. On the **Access Advisor** tab, review the recent activity for the service-linked role.

###### Note

If you are unsure whether AgentCore is using a service-linked role, you can try to delete the role. If the service is using the role, then the deletion fails and you can view the Regions where the role is being used. If the role is being used, then you must wait for the session to end before you can delete the role. You cannot revoke the session for a service-linked role.

If you want to remove a service-linked role, you must first delete the appropriate AgentCore resources:

- `AWSServiceRoleForBedrockAgentCoreNetwork`: Delete all AgentCore Runtime, Code Interpreter, and Browser resources with VPC configuration
- `AWSServiceRoleForBedrockAgentCoreRuntimeIdentity`: Delete all AgentCore Runtime resources

### Manually delete the service-linked role

Use the IAM console, the AWS CLI, or the IAM API to delete service-linked roles.
For more information, see [Deleting a service-linked role](../../../IAM/latest/UserGuide/using-service-linked-roles.md#delete-service-linked-role "../../../IAM/latest/UserGuide/using-service-linked-roles.md#delete-service-linked-role").
