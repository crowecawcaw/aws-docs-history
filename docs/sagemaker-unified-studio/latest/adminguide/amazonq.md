# Amazon Q in Amazon SageMaker Unified Studio

In the current release of Amazon SageMaker Unified Studio, by default, all users of an Amazon SageMaker unified
domain have access to the Free Tier release of Amazon Q.

## Disable Amazon Q

To disable Amazon Q in your domain, you must update your permissions to use deny
statements and update your domain level configuration. Do this by completing the following
steps:

1. Update your permissions in the [AWS policy: SageMakerStudioDomainExecutionRolePolicy](security-iam-awsmanpol-SageMakerStudioDomainExecutionRolePolicy.md "security-iam-awsmanpol-SageMakerStudioDomainExecutionRolePolicy.md") to Deny
   “q:\*”.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Deny",
 "Action": [
 "q:*",
 "glue:StartCompletion",
 "glue:GetCompletion"
 ],
 "Resource": "*"
 }
 ]
}`

```

2. Update your permissions in the [AWS policy: SageMakerStudioProjectUserRolePolicy](security-iam-awsmanpol-SageMakerStudioProjectUserRolePolicy.md "security-iam-awsmanpol-SageMakerStudioProjectUserRolePolicy.md") to Deny
   “q:\*”.

```

{
        "Sid": "AmazonQChatPermissions",
        "Effect": "Deny",
        "Action": [
            "q:*",
            "glue:StartCompletion",
           "glue:GetCompletion",
           "codewhisperer:GenerateRecommendations",
           "sqlworkbench:PutQCustomContext",
           "sqlworkbench:GetQCustomContext",
           "sqlworkbench:DeleteQCustomContext",
           "sqlworkbench:GetQSqlRecommendations",
           "sqlworkbench:GetQSqlPromptQuotas"
        ],
        "Resource": "*"
    },

```

3. Update the Amazon Q parameter value through AWS Systems Manager.

```

arn:aws:ssm:<region>:<account-id>:parameter/amazon/datazone/q/<domain-id> to empty
arn:aws:ssm:<region>:<account-id>:parameter/amazon/datazone/q/<domain-id>/q-enabled to false

```
