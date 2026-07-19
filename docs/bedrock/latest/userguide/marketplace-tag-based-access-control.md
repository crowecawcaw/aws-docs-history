# Tag-based access control for Amazon Bedrock AWS Marketplace model endpoints

When you create an Amazon Bedrock AWS Marketplace model endpoint, Amazon Bedrock applies your specified
tags to the underlying SageMaker AI endpoint. Amazon Bedrock does not support the
`aws:ResourceTag` or `aws:RequestTag` condition keys on
`bedrock:*MarketplaceModelEndpoint` actions.

To enforce tag-based access control, apply your tag conditions to the corresponding
`sagemaker:*` actions. These actions correspond to Amazon Bedrock AWS Marketplace
model endpoint operations. Amazon Bedrock uses your identity to call SageMaker AI on your behalf. SageMaker AI
then enforces your tag-based conditions.

The following Amazon Bedrock AWS Marketplace model endpoint actions support tag-based access
control through the underlying SageMaker AI actions:

- `bedrock:CreateMarketplaceModelEndpoint`
- `bedrock:UpdateMarketplaceModelEndpoint`
- `bedrock:DeleteMarketplaceModelEndpoint`
- `bedrock:GetMarketplaceModelEndpoint`
  The following actions do not support tag-based access control because they do not
  call SageMaker AI:

- `bedrock:RegisterMarketplaceModelEndpoint`
- `bedrock:DeregisterMarketplaceModelEndpoint`
  To find the corresponding SageMaker AI actions for each operation, see the
  `AmazonBedrockMarketplaceAccess` managed policy.

###### Note

`RegisterMarketplaceModelEndpoint` and
`DeregisterMarketplaceModelEndpoint` update only the association between
an existing SageMaker AI endpoint and Amazon Bedrock AWS Marketplace. These actions skip the SageMaker AI
call and ignore tag-based access control conditions. They leave the underlying
SageMaker AI endpoint and its configuration unchanged.

**Example: Deny deletion of production endpoints based on tags**

Use this policy to deny deletion of SageMaker AI endpoints tagged with
`env=prod` when requests come through Amazon Bedrock.

```
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Sid": "DenyDeleteProdMarketplaceEndpoints",
            "Effect": "Deny",
            "Action": "sagemaker:DeleteEndpoint",
            "Resource": "arn:aws:sagemaker:*:*:endpoint/*",
            "Condition": {
                "StringEquals": {
                    "aws:ResourceTag/env": "prod",
                    "aws:CalledViaLast": "bedrock.amazonaws.com"
                }
            }
        }
    ]
}
```
