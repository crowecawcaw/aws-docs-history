

# IAM permissions for user-managed setup (3LO)
<a name="kb-managed-3lo-setup"></a>

With user-managed setup (3LO), you sign in to a third-party data source (such as SharePoint, OneDrive, or Confluence) directly from the Amazon Bedrock Knowledge Bases console, and Amazon Bedrock Managed Knowledge Base handles authentication. To complete this flow, the IAM principal that starts the sign-in must be able to request the authorization URL and exchange the resulting code for a token. The principal must also be able to create the AWS Secrets Manager secret that stores the token. This page describes the IAM permissions you must grant to that principal.

**Note**  
The permissions on this page apply to the **console user** who initiates user-managed setup (3LO). They are separate from the permissions granted to the knowledge base execution role, which needs read and write access to the secret for token refresh. For the execution role permissions, see the connector-specific setup pages, such as [User-managed setup (3LO)](kb-managed-sharepoint-3lo-setup.md), [User-managed setup (3LO)](kb-managed-onedrive-3lo-setup.md), or [User-managed setup (3LO)](kb-managed-confluence-3lo-setup.md).

## Amazon Bedrock permissions for the sign-in flow
<a name="kb-managed-3lo-setup-bedrock"></a>

You need the following Amazon Bedrock permissions to start the user-managed setup (3LO) sign-in flow. Amazon Bedrock uses `GetDataSourceAuthorizationUrl` to build the third-party authorization URL that opens in the sign-in popup. It uses `CreateDataSourceToken` to exchange the authorization code for a token after you authorize the connection.

```
{
    "Version": "2012-10-17",
    "Statement": [{
        "Sid": "BedrockManagedKb3LO",
        "Effect": "Allow",
        "Action": [
            "bedrock:GetDataSourceAuthorizationUrl",
            "bedrock:CreateDataSourceToken"
        ],
        "Resource": "*"
    }]
}
```

## AWS Secrets Manager permissions for the generated secret
<a name="kb-managed-3lo-setup-secret"></a>

When you sign in, Amazon Bedrock Managed Knowledge Base creates a secret in your AWS account to store the 3LO refresh token. You need `secretsmanager:CreateSecret` permission on the secrets that Amazon Bedrock creates.

When you choose **Sign in**, you can optionally provide a **secret name prefix**. Amazon Bedrock Managed Knowledge Base includes this prefix in the generated secret ARN. With a prefix, you can scope the `Resource` element to only the secrets that Amazon Bedrock creates for user-managed setup. If you do not provide a prefix, Amazon Bedrock uses `default` as the prefix.

The generated secret ARN follows this pattern:

```
arn:aws:secretsmanager:{{region}}:{{account-id}}:secret:bedrock-managedkb-oauth/{{your-prefix}}/{{connector-type}}/{{uuid}}
```

Attach the following policy to grant `secretsmanager:CreateSecret` scoped to secrets with your prefix:

```
{
    "Version": "2012-10-17",
    "Statement": [{
        "Sid": "BedrockManagedKb3LOCreateSecret",
        "Effect": "Allow",
        "Action": [
            "secretsmanager:CreateSecret"
        ],
        "Resource": [
            "arn:aws:secretsmanager:{{region}}:{{account-id}}:secret:bedrock-managedkb-oauth/{{your-prefix}}/*"
        ]
    }]
}
```

**Note**  
If you do not provide a secret name prefix, replace the {{your-prefix}} segment in the `Resource` element with `default`, so that it scopes to `arn:aws:secretsmanager:{{region}}:{{account-id}}:secret:bedrock-managedkb-oauth/default/*`.

## Combined policy example
<a name="kb-managed-3lo-setup-combined"></a>

The following policy combines the Amazon Bedrock and AWS Secrets Manager permissions that the console user needs to complete user-managed setup (3LO):

```
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Sid": "BedrockManagedKb3LO",
            "Effect": "Allow",
            "Action": [
                "bedrock:GetDataSourceAuthorizationUrl",
                "bedrock:CreateDataSourceToken"
            ],
            "Resource": "*"
        },
        {
            "Sid": "BedrockManagedKb3LOCreateSecret",
            "Effect": "Allow",
            "Action": [
                "secretsmanager:CreateSecret"
            ],
            "Resource": [
                "arn:aws:secretsmanager:{{region}}:{{account-id}}:secret:bedrock-managedkb-oauth/{{your-prefix}}/*"
            ]
        }
    ]
}
```