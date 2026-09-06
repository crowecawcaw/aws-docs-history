

# Prerequisites
<a name="registry-prerequisites"></a>

**Migration Now Open**  
 AWS Agent Registry has launched under the new `agent-registry` namespace. Support for the public preview `bedrock-agentcore` namespace will be discontinued on September 17, 2026. For migration instructions, see [Comprehensive registry migration guide](registry-faq.md).

Before you use AWS Agent Registry, complete the following prerequisites.

## AWS account and credentials
<a name="registry-prereq-account"></a>

You need an AWS account with credentials configured. To configure credentials, install and use the AWS Command Line Interface by following the steps at [Getting started with the AWS CLI](https://docs.aws.amazon.com/cli/latest/userguide/cli-chap-getting-started.html).

```
# Verify installation
aws --version  # Should show version 2.
```

## Python and AWS SDK
<a name="registry-prereq-sdk"></a>

To access your AWS credentials and configure them for use with SDKs, follow the steps at [Using IAM Identity Center to authenticate AWS SDK and Tools](https://docs.aws.amazon.com/sdkref/latest/guide/access-sso.html). If you plan to use the AWS Python SDK (Boto3) to interact with AWS Agent Registry programmatically:

1. Install **Python 3.10\+**.

1. Install the AWS SDK: `pip install boto3` 

1. Verify your credentials are configured: `aws sts get-caller-identity` 

Please refer to [AWS Builder Tools](https://builder.aws.com/build/tools) for more information on how to setup and use AWS SDK.

## IAM permissions
<a name="registry-prereq-iam"></a>

Set up IAM permissions based on the persona that matches your role. The full list of IAM Permissions for Registry can be found in [IAM Permissions](registry-iam-permissions.md).

### Administrator permissions
<a name="registry-prereq-admin-permissions"></a>

For administrators who manage the full lifecycle of registries, records, and approve/reject/deprecate records:

**Example**  

```
{
"Version": "2012-10-17",		 	 	 
    "Statement":
    [
        {
            "Sid": "AllowCreatingAndListingRegistries",
            "Effect": "Allow",
            "Action":
            [
                "agent-registry:CreateRegistry",
                "agent-registry:ListRegistries"
            ],
            "Resource":
            [
                "arn:aws:agent-registry:*:<account>:*"
            ]
        },
        {
            "Sid": "AllowGetUpdateDeleteRegistry",
            "Effect": "Allow",
            "Action":
            [
                "agent-registry:GetRegistry",
                "agent-registry:UpdateRegistry",
                "agent-registry:DeleteRegistry"
            ],
            "Resource":
            [
                "arn:aws:agent-registry:*:<account>:registry/*"
            ]
        },
        {
            "Sid": "AllowCreatingAndListingRecords",
            "Effect": "Allow",
            "Action":
            [
                "agent-registry:CreateRegistryRecord",
                "agent-registry:ListRegistryRecords"
            ],
            "Resource":
            [
                "arn:aws:agent-registry:*:<account>:registry/*"
            ]
        },
        {
            "Sid": "AllowRecordLevelOperations",
            "Effect": "Allow",
            "Action":
            [
                "agent-registry:GetRegistryRecord",
                "agent-registry:UpdateRegistryRecord",
                "agent-registry:DeleteRegistryRecord",
                "agent-registry:SubmitRegistryRecordForApproval"
            ],
            "Resource":
            [
                "arn:aws:agent-registry:*:<account>:registry/*/record/*"
            ]
        },
        {
            "Sid": "AllowApproveRejectDeprecateRecords",
            "Effect": "Allow",
            "Action":
            [
                "agent-registry:UpdateRegistryRecordStatus"
            ],
            "Resource":
            [
                "arn:aws:agent-registry:*:<account>:registry/*/record/*"
            ]
        },
        {
            "Sid": "AdditionalPermissionForRegistryManagedWorkloadIdentity",
            "Effect": "Allow",
            "Action":
            [
                "bedrock-agentcore:*WorkloadIdentity"
            ],
            "Resource":
            [
                "arn:aws:bedrock-agentcore:*:<account>:workload-identity-directory/default/*"
            ]
        },
        {
            "Sid": "AllowPermissionForCreatingServiceLinkedRole",
            "Effect": "Allow",
            "Action":
            [
                "iam:CreateServiceLinkedRole"
            ],
            "Resource":
            [
                "arn:aws:iam::*:role/aws-service-role/agent-registry.amazonaws.com/AWSServiceRoleForAgentRegistry"
            ],
            "Condition":
            {
                "StringLike": { "iam:AWSServiceName": "agent-registry.amazonaws.com" }
            }
        }
    ]
}
```

```
{
"Version": "2012-10-17",		 	 	 
    "Statement":
    [
        {
            "Sid": "AllowCreatingAndListingRegistries",
            "Effect": "Allow",
            "Action":
            [
                "bedrock-agentcore:CreateRegistry",
                "bedrock-agentcore:ListRegistries"
            ],
            "Resource":
            [
                "arn:aws:bedrock-agentcore:*:<account>:*"
            ]
        },
        {
            "Sid": "AllowGetUpdateDeleteRegistry",
            "Effect": "Allow",
            "Action":
            [
                "bedrock-agentcore:GetRegistry",
                "bedrock-agentcore:UpdateRegistry",
                "bedrock-agentcore:DeleteRegistry"
            ],
            "Resource":
            [
                "arn:aws:bedrock-agentcore:*:<account>:registry/*"
            ]
        },
        {
            "Sid": "AllowCreatingAndListingRecords",
            "Effect": "Allow",
            "Action":
            [
                "bedrock-agentcore:CreateRegistryRecord",
                "bedrock-agentcore:ListRegistryRecords"
            ],
            "Resource":
            [
                "arn:aws:bedrock-agentcore:*:<account>:registry/*"
            ]
        },
        {
            "Sid": "AllowRecordLevelOperations",
            "Effect": "Allow",
            "Action":
            [
                "bedrock-agentcore:GetRegistryRecord",
                "bedrock-agentcore:UpdateRegistryRecord",
                "bedrock-agentcore:DeleteRegistryRecord",
                "bedrock-agentcore:SubmitRegistryRecordForApproval"
            ],
            "Resource":
            [
                "arn:aws:bedrock-agentcore:*:<account>:registry/*/record/*"
            ]
        },
        {
            "Sid": "AllowApproveRejectDeprecateRecords",
            "Effect": "Allow",
            "Action":
            [
                "bedrock-agentcore:UpdateRegistryRecordStatus"
            ],
            "Resource":
            [
                "arn:aws:bedrock-agentcore:*:<account>:registry/*/record/*"
            ]
        },
        {
            "Sid": "AdditionalPermissionForRegistryManagedWorkloadIdentity",
            "Effect": "Allow",
            "Action":
            [
                "bedrock-agentcore:*WorkloadIdentity"
            ],
            "Resource":
            [
                "arn:aws:bedrock-agentcore:*:<account>:workload-identity-directory/default/*"
            ]
        },
        {
            "Sid": "AllowPermissionForCreatingServiceLinkedRole",
            "Effect": "Allow",
            "Action":
            [
                "iam:CreateServiceLinkedRole"
            ],
            "Resource":
            [
                "arn:aws:iam::*:role/aws-service-role/agent-registry.amazonaws.com/AWSServiceRoleForAgentRegistry"
            ],
            "Condition":
            {
                "StringLike": { "iam:AWSServiceName": "agent-registry.amazonaws.com" }
            }
        }
    ]
}
```

### Curator / Approver permissions
<a name="registry-prereq-curator-permissions"></a>

For curators who review and approve/reject records but don’t perform administrative operations:

**Example**  

```
{
"Version": "2012-10-17",		 	 	 
    "Statement":
    [
        {
            "Effect": "Allow",
            "Action":
            [
                "agent-registry:ListRegistries"
            ],
            "Resource":
            [
                "arn:aws:agent-registry:*:<account>:*"
            ]
        },
        {
            "Effect": "Allow",
            "Action":
            [
                "agent-registry:GetRegistry"
            ],
            "Resource":
            [
                "arn:aws:agent-registry:*:<account>:registry/*"
            ]
        },
        {
            "Effect": "Allow",
            "Action":
            [
                "agent-registry:ListRegistryRecords"
            ],
            "Resource":
            [
                "arn:aws:agent-registry:*:<account>:registry/*"
            ]
        },
        {
            "Effect": "Allow",
            "Action":
            [
                "agent-registry:GetRegistryRecord"
            ],
            "Resource":
            [
                "arn:aws:agent-registry:*:<account>:registry/*/record/*"
            ]
        },
        {
            "Effect": "Allow",
            "Action":
            [
                "agent-registry:UpdateRegistryRecordStatus"
            ],
            "Resource":
            [
                "arn:aws:agent-registry:*:<account>:registry/*/record/*"
            ]
        }
    ]
}
```

```
{
"Version": "2012-10-17",		 	 	 
    "Statement":
    [
        {
            "Effect": "Allow",
            "Action":
            [
                "bedrock-agentcore:ListRegistries"
            ],
            "Resource":
            [
                "arn:aws:bedrock-agentcore:*:<account>:*"
            ]
        },
        {
            "Effect": "Allow",
            "Action":
            [
                "bedrock-agentcore:GetRegistry"
            ],
            "Resource":
            [
                "arn:aws:bedrock-agentcore:*:<account>:registry/*"
            ]
        },
        {
            "Effect": "Allow",
            "Action":
            [
                "bedrock-agentcore:ListRegistryRecords"
            ],
            "Resource":
            [
                "arn:aws:bedrock-agentcore:*:<account>:registry/*"
            ]
        },
        {
            "Effect": "Allow",
            "Action":
            [
                "bedrock-agentcore:GetRegistryRecord"
            ],
            "Resource":
            [
                "arn:aws:bedrock-agentcore:*:<account>:registry/*/record/*"
            ]
        },
        {
            "Effect": "Allow",
            "Action":
            [
                "bedrock-agentcore:UpdateRegistryRecordStatus"
            ],
            "Resource":
            [
                "arn:aws:bedrock-agentcore:*:<account>:registry/*/record/*"
            ]
        }
    ]
}
```

### Publisher permissions
<a name="registry-prereq-publisher-permissions"></a>

For publishers who submit MCP servers, agents, or other resources to the registry:

**Note**  
The three sync-related statements (`AllowWorkloadIdentityForSynchronization`, `AllowGetResourceOauth2TokenForOauthBasedSynchronization`, `AllowPassRoleForIamBasedSynchronization`) authorize workload identity and OAuth credential provider resources managed by AgentCore Identity. Those resources intentionally remain under the `bedrock-agentcore` namespace, so their actions, ARNs, and service principal do not change.

**Note**  
Scope the `AllowGetResourceOauth2TokenForOauthBasedSynchronization` statement to the specific OAuth credential provider ARN whose access token this identity needs. Avoid wildcards in the provider segment of the ARN — patterns such as `token-vault/ ` or `token-vault/default/oauth2credentialprovider/` grant access to every OAuth credential provider in the account, which can enable cross-team credential access. Follow the principle of least privilege by naming the specific provider in the `Resource` field, for example `arn:aws:bedrock-agentcore:<region>:<account>:token-vault/default/oauth2credentialprovider/<oauthProviderName>`.

**Example**  

```
{
"Version": "2012-10-17",		 	 	 
    "Statement":
    [
        {
            "Effect": "Allow",
            "Action":
            [
                "agent-registry:ListRegistries"
            ],
            "Resource":
            [
                "arn:aws:agent-registry:*:<account>:*"
            ]
        },
        {
            "Effect": "Allow",
            "Action":
            [
                "agent-registry:GetRegistry"
            ],
            "Resource":
            [
                "arn:aws:agent-registry:*:<account>:registry/*"
            ]
        },
        {
            "Effect": "Allow",
            "Action":
            [
                "agent-registry:CreateRegistryRecord",
                "agent-registry:ListRegistryRecords"
            ],
            "Resource":
            [
                "arn:aws:agent-registry:*:<account>:registry/*"
            ]
        },
        {
            "Effect": "Allow",
            "Action":
            [
                "agent-registry:GetRegistryRecord",
                "agent-registry:UpdateRegistryRecord",
                "agent-registry:DeleteRegistryRecord",
                "agent-registry:SubmitRegistryRecordForApproval"
            ],
            "Resource":
            [
                "arn:aws:agent-registry:*:<account>:registry/*/record/*"
            ]
        },
        {
            "Sid": "AllowWorkloadIdentityForSynchronization",
            "Effect": "Allow",
            "Action":
            [
                "bedrock-agentcore:GetWorkloadAccessToken"
            ],
            "Resource":
            [
                "arn:aws:bedrock-agentcore:*:<account>:workload-identity-directory/*"
            ]
        },
        {
            "Sid": "AllowGetResourceOauth2TokenForOauthBasedSynchronization",
            "Effect": "Allow",
            "Action":
            [
                "bedrock-agentcore:GetResourceOauth2Token"
            ],
            "Resource":
            [
                "arn:aws:bedrock-agentcore:<region>:<account>:token-vault/default/oauth2credentialprovider/<oauthProviderName>"
            ]
        },
        {
            "Sid": "AllowPassRoleForIamBasedSynchronization",
            "Effect": "Allow",
            "Action":
            [
                "iam:PassRole"
            ],
            "Resource":
            [
                "arn:aws:iam::<account>:role/<your-sync-role-name>"
            ],
            "Condition":
            {
                "StringEquals":
                {
                    "iam:PassedToService": "bedrock-agentcore.amazonaws.com"
                },
                "StringLike":
                {
                    "iam:AssociatedResourceARN": "arn:aws:bedrock-agentcore:<region>:<account>:registry/*/record/*"
                }
            }
        }
    ]
}
```

```
{
"Version": "2012-10-17",		 	 	 
    "Statement":
    [
        {
            "Effect": "Allow",
            "Action":
            [
                "bedrock-agentcore:ListRegistries"
            ],
            "Resource":
            [
                "arn:aws:bedrock-agentcore:*:<account>:*"
            ]
        },
        {
            "Effect": "Allow",
            "Action":
            [
                "bedrock-agentcore:GetRegistry"
            ],
            "Resource":
            [
                "arn:aws:bedrock-agentcore:*:<account>:registry/*"
            ]
        },
        {
            "Effect": "Allow",
            "Action":
            [
                "bedrock-agentcore:CreateRegistryRecord",
                "bedrock-agentcore:ListRegistryRecords"
            ],
            "Resource":
            [
                "arn:aws:bedrock-agentcore:*:<account>:registry/*"
            ]
        },
        {
            "Effect": "Allow",
            "Action":
            [
                "bedrock-agentcore:GetRegistryRecord",
                "bedrock-agentcore:UpdateRegistryRecord",
                "bedrock-agentcore:DeleteRegistryRecord",
                "bedrock-agentcore:SubmitRegistryRecordForApproval"
            ],
            "Resource":
            [
                "arn:aws:bedrock-agentcore:*:<account>:registry/*/record/*"
            ]
        },
        {
            "Sid": "AllowWorkloadIdentityForSynchronization",
            "Effect": "Allow",
            "Action":
            [
                "bedrock-agentcore:GetWorkloadAccessToken"
            ],
            "Resource":
            [
                "arn:aws:bedrock-agentcore:*:<account>:workload-identity-directory/*"
            ]
        },
        {
            "Sid": "AllowGetResourceOauth2TokenForOauthBasedSynchronization",
            "Effect": "Allow",
            "Action":
            [
                "bedrock-agentcore:GetResourceOauth2Token"
            ],
            "Resource":
            [
                "arn:aws:bedrock-agentcore:<region>:<account>:token-vault/default/oauth2credentialprovider/<oauthProviderName>"
            ]
        },
        {
            "Sid": "AllowPassRoleForIamBasedSynchronization",
            "Effect": "Allow",
            "Action":
            [
                "iam:PassRole"
            ],
            "Resource":
            [
                "arn:aws:iam::<account>:role/<your-sync-role-name>"
            ],
            "Condition":
            {
                "StringEquals":
                {
                    "iam:PassedToService": "bedrock-agentcore.amazonaws.com"
                },
                "StringLike":
                {
                    "iam:AssociatedResourceARN": "arn:aws:bedrock-agentcore:<region>:<account>:registry/*/record/*"
                }
            }
        }
    ]
}
```

### Consumer permissions
<a name="registry-prereq-consumer-permissions"></a>

For consumers who search for and use approved resources:

**Example**  

```
{
"Version": "2012-10-17",		 	 	 
    "Statement":
    [
        {
            "Effect": "Allow",
            "Action":
            [
                "agent-registry:ListRegistries"
            ],
            "Resource":
            [
                "arn:aws:agent-registry:*:<account>:*"
            ]
        },
        {
            "Effect": "Allow",
            "Action":
            [
                "agent-registry:GetRegistry"
            ],
            "Resource":
            [
                "arn:aws:agent-registry:*:<account>:registry/*"
            ]
        },
        {
            "Effect": "Allow",
            "Action":
            [
                "agent-registry:SearchDiscoverableRegistryRecords",
                "agent-registry:ListDiscoverableRegistryRecords",
                "agent-registry:GetDiscoverableRegistryRecord",
                "agent-registry:InvokeRegistryMcp"
            ],
            "Resource":
            [
                "arn:aws:agent-registry:*:<account>:registry/*"
            ]
        }
    ]
}
```

```
{
"Version": "2012-10-17",		 	 	 
    "Statement":
    [
        {
            "Effect": "Allow",
            "Action":
            [
                "bedrock-agentcore:ListRegistries"
            ],
            "Resource":
            [
                "arn:aws:bedrock-agentcore:*:<account>:*"
            ]
        },
        {
            "Effect": "Allow",
            "Action":
            [
                "bedrock-agentcore:GetRegistry"
            ],
            "Resource":
            [
                "arn:aws:bedrock-agentcore:*:<account>:registry/*"
            ]
        },
        {
            "Effect": "Allow",
            "Action":
            [
                "bedrock-agentcore:SearchRegistryRecords",
                "bedrock-agentcore:InvokeRegistryMcp"
            ],
            "Resource":
            [
                "arn:aws:bedrock-agentcore:*:<account>:registry/*"
            ]
        }
    ]
}
```

For example IAM policies, see [Identity and access management for Amazon Bedrock AgentCore](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/security-iam.html).

## (Optional) Identity provider for JWT authorization
<a name="registry-prereq-jwt"></a>

If you plan to use JWT authorization for inbound identity (to enable consumers to search the registry using Non-IAM identities), set up Amazon Cognito or your own identity provider before creating the registry:

1.  **Create a Cognito User Pool** (or use your existing identity provider)

1.  **Register an App Client** and note the Client ID

1.  **Create a test user** with a username and password

For detailed instructions, see [Configure inbound JWT authorizer](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/inbound-jwt-authorizer.html).