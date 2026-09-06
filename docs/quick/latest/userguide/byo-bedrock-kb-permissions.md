

# Setting up permissions
<a name="byo-bedrock-kb-permissions"></a>

Amazon Quick authenticates to Amazon Bedrock using IAM SigV4 credentials via the Amazon Quick service role. The service role requires the following actions on the knowledge base:
+ `bedrock:Retrieve`
+ `bedrock:GetDocumentContent`

The following example shows the ARN format for Amazon Bedrock managed knowledge bases:

```
arn:aws:bedrock:{{REGION}}:{{ACCOUNT_ID}}:knowledge-base/{{KB_ID}}
```

## Cross-account setup
<a name="byo-bedrock-kb-cross-account"></a>

Cross-account access is required when the managed knowledge base is owned by a different AWS account than the one running your Amazon Quick instance. For example, a central data team might own the knowledge base in one account while your Amazon Quick instance runs in a separate account.

In this case, you must attach a resource policy to the knowledge base in the owner's account before granting the service role access. The resource policy authorizes the Amazon Quick service role to call the knowledge base across account boundaries.

The following resource policy example grants the Amazon Quick service role permission to access your managed knowledge base. Replace the placeholder values with your specific account IDs, Region, and knowledge base ID:

```
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Effect": "Allow",
            "Principal": {
                "AWS": "arn:aws:iam::{{QUICK_ACCOUNT_ID}}:role/service-role/aws-quicksight-service-role-v0"
            },
            "Action": [
                "bedrock:Retrieve",
                "bedrock:GetDocumentContent"
            ],
            "Resource": "arn:aws:bedrock:{{REGION}}:{{KB_OWNER_ACCOUNT_ID}}:knowledge-base/{{KB_ID}}"
        }
    ]
}
```

See [Share a managed knowledge base across accounts](https://docs.aws.amazon.com/bedrock/latest/userguide/kb-managed-cross-account.html) in the *Amazon Bedrock User Guide*.

## Granting the service role access
<a name="byo-bedrock-kb-grant-service-role"></a>

For both same-account and cross-account setups, grant the Amazon Quick service role access to the managed knowledge base through the admin console:

1. Sign in to the Amazon Quick console as an administrator.

1. Navigate to **Manage account** > **AWS Resources** > **Bedrock**.

1. Add your managed knowledge base ARN to the Amazon Quick service role using the provided form. Amazon Quick attaches the necessary IAM policy to the service role, scoped to the entered ARN.