

# Permissions and examples for AWS CodeConnections

The following policy statements and examples can help you manage AWS CodeConnections.

For information about how to create an IAM identity-based policy using these example JSON policy documents, see [Creating policies on the JSON tab](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_create.html#access_policies_create-json-editor) in the *IAM User Guide*. 

## Example: A policy for creating AWS CodeConnections with the CLI and viewing with the console
<a name="security_iam_id-based-policy-examples-connections-clisdk"></a>

A role or user designated to use the AWS CLI or SDK to view, create, tag, or delete connections should have permissions limited to the following.

**Note**  
You cannot complete a connection in the console with only the following permissions. You need to add the permissions in the next section.

To use the console to view a list of available connections, view tags, and use a connection, use the following policy.

------
#### [ JSON ]

****  

```json
{
    "Version":"2012-10-17",		 	 	 
    "Statement": [
      {
        "Sid": "ConnectionsFullAccess",
        "Effect": "Allow",
        "Action": [
            "codeconnections:CreateConnection",
            "codeconnections:DeleteConnection",
            "codeconnections:UseConnection",
            "codeconnections:GetConnection",
            "codeconnections:ListConnections",
            "codeconnections:TagResource",
            "codeconnections:ListTagsForResource",
            "codeconnections:UntagResource"
        ],
        "Resource": "*"
     }
   ]
}
```

------

## Example: A policy for creating AWS CodeConnections with the console
<a name="security_iam_id-based-policy-examples-connections-console"></a>

A role or user designated to manage connections in the console should have the permissions required to complete a connection in the console and create an installation, which includes authorizing the handshake to the provider and creating installations for connections to use. `UseConnection` should also be added to use the connection in the console. Use the following policy to view, use, create, tag, or delete a connection in the console.

**Note**  
Beginning July 1, 2024, the console creates connections with `codeconnections` in the resource ARN. Resources with both service prefixes will continue to display in the console.

**Note**  
For resources created using the console, policy statement actions must include `codestar-connections` as the service prefix as shown in the following example.

------
#### [ JSON ]

****  

```json
{
    "Version":"2012-10-17",		 	 	 
    "Statement": [
        {
            "Effect": "Allow",
            "Action": [
                "codestar-connections:CreateConnection",
                "codestar-connections:DeleteConnection",
                "codestar-connections:GetConnection",
                "codestar-connections:ListConnections",
                "codestar-connections:GetInstallationUrl",
                "codestar-connections:GetIndividualAccessToken",
                "codestar-connections:ListInstallationTargets",
                "codestar-connections:StartOAuthHandshake",
                "codestar-connections:UpdateConnectionInstallation",
                "codestar-connections:UseConnection",
                "codestar-connections:TagResource",
                "codestar-connections:ListTagsForResource",
                "codestar-connections:UntagResource"
            ],
            "Resource": [
                "*"
            ]
        }
    ]
}
```

------

## Example: Policy for creating and completing GitHub Enterprise Cloud with data residency connections
<a name="security_iam_id-based-policy-examples-ghec-dr"></a>

To limit a role or user to creating and completing GitHub Enterprise Cloud with data residency connections, grant only the following permissions. The policy uses the `codeconnections:ProviderType` condition key to allow the connection-creation and handshake actions only when the request specifies the `GitHubEnterpriseCloudDataResidency` provider type. The policy also includes the permissions to get the connection and to list GitHub Enterprise Cloud with data residency connections while you complete the connection.

The policy includes the following statements:
+ The first statement allows `CreateConnection`, `StartOAuthHandshake`, `GetIndividualAccessToken`, and `GetInstallationUrl` only when the request specifies the `GitHubEnterpriseCloudDataResidency` provider type. The statement scopes the actions to the AWS Region and account.
+ The second statement allows `ListInstallationTargets` in the AWS Region and account. This action doesn't support the `codeconnections:ProviderType` condition key, so the statement has no condition.
+ The third statement allows `ListConnections` in the AWS Region and account only when the request uses the `codeconnections:ProviderTypeFilter` condition key to filter for the `GitHubEnterpriseCloudDataResidency` provider type.
+ The fourth statement allows `UpdateConnectionInstallation` and `GetConnection` on connections in the Region and account. These actions don't support the `codeconnections:ProviderType` condition key, so the statement has no condition.

The following example shows the complete policy. Replace {{us-west-2}} with the AWS Region where you create the connection, and {{111122223333}} with your AWS account ID.

```json
{
    "Version": "2012-10-17",		 	 	 
    "Statement": [
        {
            "Sid": "CreateGhecDrConnections",
            "Effect": "Allow",
            "Action": [
                "codeconnections:CreateConnection",
                "codeconnections:StartOAuthHandshake",
                "codeconnections:GetIndividualAccessToken",
                "codeconnections:GetInstallationUrl"
            ],
            "Resource": "arn:aws:codeconnections:{{us-west-2}}:{{111122223333}}:*",
            "Condition": {
                "StringEquals": {
                    "codeconnections:ProviderType": "GitHubEnterpriseCloudDataResidency"
                }
            }
        },
        {
            "Sid": "ListGhecDrInstallationTargets",
            "Effect": "Allow",
            "Action": [
                "codeconnections:ListInstallationTargets"
            ],
            "Resource": "arn:aws:codeconnections:{{us-west-2}}:{{111122223333}}:*"
        },
        {
            "Sid": "ListGhecDrConnections",
            "Effect": "Allow",
            "Action": [
                "codeconnections:ListConnections"
            ],
            "Resource": "arn:aws:codeconnections:{{us-west-2}}:{{111122223333}}:*",
            "Condition": {
                "StringEquals": {
                    "codeconnections:ProviderTypeFilter": "GitHubEnterpriseCloudDataResidency"
                }
            }
        },
        {
            "Sid": "CompleteGhecDrConnections",
            "Effect": "Allow",
            "Action": [
                "codeconnections:UpdateConnectionInstallation",
                "codeconnections:GetConnection"
            ],
            "Resource": "arn:aws:codeconnections:{{us-west-2}}:{{111122223333}}:connection/*"
        }
    ]
}
```

**Note**  
To add tags when you create the connection, you also need `codeconnections:TagResource`. To use the connection after it's available, you need `codeconnections:UseConnection`. For more information, see [AWS CodeConnections permissions reference](security-iam.md#permissions-reference-connections).  
The **Connections** list page in the console calls `ListConnections` without a provider type filter. To view the full list of connections in the console, you also need `codeconnections:ListConnections` without the `codeconnections:ProviderTypeFilter` condition.

For more information about creating these connections, see [Create a connection to GitHub Enterprise Cloud with data residency](connections-create-ghec-dr.md).

## Example: An administrator-level policy for managing AWS CodeConnections
<a name="security_iam_id-based-policy-examples-connections-fullaccess"></a>

In this example, you want to grant an IAM user in your AWS account full access to AWS CodeConnections so that the user can add, update, and delete connections. This is a full access policy, equivalent to the **AWSCodePipeline\_FullAccess** managed policy. Like that managed policy, you should only attach this kind of policy statement to IAM users, groups, or roles that require full administrative access to connections across your AWS account.

------
#### [ JSON ]

****  

```json
{
    "Version":"2012-10-17",		 	 	 
    "Statement": [
      {
        "Sid": "ConnectionsFullAccess",
        "Effect": "Allow",
        "Action": [
            "codeconnections:CreateConnection",
            "codeconnections:DeleteConnection",
            "codeconnections:UseConnection",
            "codeconnections:GetConnection",
            "codeconnections:ListConnections",
            "codeconnections:ListInstallationTargets",
            "codeconnections:GetInstallationUrl",
            "codeconnections:StartOAuthHandshake",
            "codeconnections:UpdateConnectionInstallation",
            "codeconnections:GetIndividualAccessToken",
            "codeconnections:TagResource",
            "codeconnections:ListTagsForResource",
            "codeconnections:UntagResource"
        ],
        "Resource": "*"
     }
   ]
}
```

------

## Example: A contributor-level policy for using AWS CodeConnections
<a name="security_iam_id-based-policy-examples-connections-contributor"></a>

In this example, you want to grant access to the day-to-day usage of AWS CodeConnections, such as creating and viewing details of connections, but not to more destructive actions, such as deleting connections.

------
#### [ JSON ]

****  

```json
{
    "Version":"2012-10-17",		 	 	 
    "Statement": [
        {
            "Sid": "AWSCodeConnectionsPowerUserAccess",
            "Effect": "Allow",
            "Action": [
                "codeconnections:CreateConnection",
                "codeconnections:UseConnection",
                "codeconnections:GetConnection",
                "codeconnections:ListConnections",
                "codeconnections:ListInstallationTargets",
                "codeconnections:GetInstallationUrl",
                "codeconnections:GetIndividualAccessToken",
                "codeconnections:StartOAuthHandshake",
                "codeconnections:UpdateConnectionInstallation",
                "codeconnections:ListTagsForResource"
            ],
            "Resource": "*"
        }
    ]
}
```

------

## Example: A read-only-level policy for using AWS CodeConnections
<a name="security_iam_id-based-policy-examples-connections-readonly"></a>

In this example, you want to grant an IAM user in your account read-only access to the connections in your AWS account. This example shows how you might create a policy that allows viewing these items.

------
#### [ JSON ]

****  

```json
{
    "Version":"2012-10-17",		 	 	 
    "Id": "ConnectionsforReadOnly",
    "Statement": [
        {
            "Sid": "ReadsAPIAccess",
            "Effect": "Allow",
            "Action": [
            "codeconnections:GetConnection",
            "codeconnections:ListConnections",
            "codeconnections:ListInstallationTargets",
            "codeconnections:GetInstallationUrl",
            "codeconnections:ListTagsForResource"
            ],
            "Resource": "*"
        }
    ]
}
```

------<a name="security_iam_id-based-policy-examples-connections-use"></a>

## Example: Limit host VPC permissions using the **VpcId** context key
<a name="security_iam_id-based-policy-examples-connections-vpc"></a>

In the following example, the customer can use the **VpcId** context key to limit creation or management of hosts to hosts with specified VPC.

------
#### [ JSON ]

****  

```json
{
    "Version":"2012-10-17",		 	 	 
    "Statement": [
        {
            "Sid": "VisualEditor0",
            "Effect": "Allow",
            "Action": [
                "codeconnections:CreateHost",
                "codeconnections:UpdateHost"
            ],
            "Resource": "*",
            "Condition": {
                "StringEquals": {
                    "codeconnections:VpcId": "vpc-EXAMPLE"
                }
            }
        }
    ]
}
```

------