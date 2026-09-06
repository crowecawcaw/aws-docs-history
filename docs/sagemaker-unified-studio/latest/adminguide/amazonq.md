

# Generative AI assistance in Amazon SageMaker Unified Studio
<a name="amazonq"></a>

Amazon SageMaker Unified Studio provides generative AI assistance through Amazon Q and the SageMaker Data Agent. Amazon Q provides conversational AI chat and command line tools in JupyterLab and Code Editor. The SageMaker Data Agent provides intelligent assistance for code generation, error diagnosis, and data analysis recommendations in Notebooks and Query Editor.

## Amazon Q
<a name="amazonq-section"></a>

In the current release of Amazon SageMaker Unified Studio, by default, all users of an Amazon SageMaker unified domain have access to the Free Tier release of Amazon Q.

### Disable Amazon Q
<a name="amazonq-disable"></a>

To disable Amazon Q in your domain, you must update your permissions to use deny statements and update your domain level configuration. Complete the following steps:

1. Update your permissions in the [AWS policy: SageMakerStudioDomainExecutionRolePolicy](security-iam-awsmanpol-SageMakerStudioDomainExecutionRolePolicy.md) to Deny "q:\*".

------
#### [ JSON ]

****  

   ```
   {
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
   }
   ```

------

1. Update your permissions in the [AWS policy: SageMakerStudioProjectUserRolePolicy](security-iam-awsmanpol-SageMakerStudioProjectUserRolePolicy.md) to Deny "q:\*". The following policy statement denies the required actions:

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

1. Update the Amazon Q parameter value through AWS Systems Manager. Set the following parameters to disable Amazon Q:

   ```
   arn:aws:ssm:<region>:<account-id>:parameter/amazon/datazone/q/<domain-id> to empty
   arn:aws:ssm:<region>:<account-id>:parameter/amazon/datazone/q/<domain-id>/q-enabled to false
   ```

## SageMaker Data Agent
<a name="data-agent-admin"></a>

The SageMaker Data Agent provides intelligent assistance for code generation, error diagnosis, and data analysis recommendations in Notebooks and Query Editor. The SageMaker Data Agent is available in both IAM and IAM Identity Center (IdC) domains.

### Disable the SageMaker Data Agent
<a name="data-agent-admin-disable"></a>

To disable the SageMaker Data Agent in your domain, use IAM permissions to deny the required API actions. The following IAM policy statement denies the Amazon DataZone API actions that the SageMaker Data Agent requires. Add this statement to your project role policy.

```
{
    "Sid": "SageMakerDataAgentDeny",
    "Effect": "Deny",
    "Action": [
        "datazone:SendMessage",
        "datazone:GenerateCode",
        "datazone:StartConversation",
        "datazone:GetConversation",
        "datazone:ListConversations"
    ],
    "Resource": "*"
}
```

The following list describes the denied actions:
+ `datazone:SendMessage` – Prevents sending messages to the SageMaker Data Agent.
+ `datazone:GenerateCode` – Prevents the SageMaker Data Agent from generating code suggestions.
+ `datazone:StartConversation`, `datazone:GetConversation`, `datazone:ListConversations` – Prevents users from starting, retrieving, or listing SageMaker Data Agent conversations.

In IAM Identity Center (IdC) domains, you can also disable the SageMaker Data Agent through the domain configuration page. This option provides a domain-level control to turn off the SageMaker Data Agent for all users in the domain.

The following image shows the domain configuration option for disabling the SageMaker Data Agent.

![Screenshot of the domain configuration page showing the toggle option to disable the SageMaker Data Agent.](http://docs.aws.amazon.com/sagemaker-unified-studio/latest/adminguide/images/data-agent/disable-data-agent.png)
