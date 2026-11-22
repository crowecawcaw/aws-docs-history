

# IAM policies to use CloudWatch Omni

The space operator role carries `CloudWatchOmniSpaceAccessPolicy` as its base policy, with `CloudWatchOmniModelInferencePolicy` and `CloudWatchOmniAWSIntegrationPolicy` as optional additions chosen during setup. Between them they cover using a space: querying telemetry, managing alerts and dashboards, and creating and running evaluations. None covers creating a space or a domain, so setup needs permissions you grant yourself. On the space operator role, replace `CloudWatchOmniAWSIntegrationPolicy` with `CloudWatchOmniAWSIntegrationPolicyV2`. See [The policies](omni-aws-managed-policies-for-cloudwatch-omni.md#omni-aws-managed-policies-for-cloudwatch-omni-the-policies). CloudWatch Omni provides further managed policies for other roles, including `CloudWatchOmniDomainAccessPolicy` for organization domain administration. For the complete set, see [AWS managed policies for CloudWatch Omni](omni-aws-managed-policies-for-cloudwatch-omni.md).

This page enumerates what each policy grants and why, discloses the permissions that read metadata across your whole account, and lists the permissions you must add separately. For how CloudWatch Omni works with IAM in general (resource types, condition keys, and the roles setup creates), see [Identity and access management for CloudWatch Omni](omni-identity-and-access-management-for-cloudwatch-omni.md).

**Topics**
+ [Permissions in CloudWatchOmniModelInferencePolicy](#omni-iam-policies-to-use-cloudwatch-omni-permissions-in-cloudwatchomnimodelinferencepolicy)
+ [Permissions in CloudWatchOmniSpaceAccessPolicy](#omni-iam-policies-to-use-cloudwatch-omni-permissions-in-cloudwatchomnispaceaccesspolicy)
+ [Permissions that read across your whole account](#omni-iam-policies-to-use-cloudwatch-omni-permissions-that-read-across-your-whole-account)
+ [Permissions in CloudWatchOmniAWSIntegrationPolicyV2](#omni-iam-policies-to-use-cloudwatch-omni-permissions-in-cloudwatchomniawsintegrationpolicyv2)
+ [Permissions you provide yourself](#omni-iam-policies-to-use-cloudwatch-omni-permissions-you-provide-yourself)

## Permissions in CloudWatchOmniModelInferencePolicy
<a name="omni-iam-policies-to-use-cloudwatch-omni-permissions-in-cloudwatchomnimodelinferencepolicy"></a>

This policy grants model inference and nothing else. It is attached only to spaces that use the prompt playground or run evaluations that invoke a model. A space that only views telemetry does not receive it, and a space can create and view its evaluation configuration without it. Only running a model requires it.


| Action | Resources | Why CloudWatch Omni needs it | 
| --- | --- | --- | 
| bedrock:InvokeModel, bedrock:InvokeModelWithResponseStream | Foundation models and inference profiles | Runs the model you select in the prompt playground, and the model an evaluator uses to score a result. | 
| bedrock-mantle:CreateInference | Amazon Bedrock Mantle projects | Runs a model served through Amazon Bedrock Mantle rather than as a Bedrock foundation model. | 
| bedrock-mantle:CallWithBearerToken | All resources | Authenticates the Amazon Bedrock Mantle inference call above. | 

Every action except `bedrock-mantle:CallWithBearerToken` is restricted to your own account by an `aws:ResourceAccount` condition, so a space can invoke only the models, inference profiles, and projects in the account it belongs to. `CallWithBearerToken` has no resource type in the IAM action model, so it cannot be scoped to a resource or narrowed by a condition. The same action appears with the same unscoped resource in the AWS managed policy [BedrockAgentCoreFullAccess](https://docs.aws.amazon.com/aws-managed-policy/latest/reference/BedrockAgentCoreFullAccess.html), which uses it for the same purpose.

```json
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Sid": "AgentCoreEvaluationBedrockInvoke",
            "Effect": "Allow",
            "Action": [
                "bedrock:InvokeModel",
                "bedrock:InvokeModelWithResponseStream"
            ],
            "Resource": [
                "arn:aws:bedrock:*::foundation-model/*",
                "arn:aws:bedrock:*:*:inference-profile/*"
            ],
            "Condition": {
                "StringEquals": {
                    "aws:ResourceAccount": "${aws:PrincipalAccount}"
                }
            }
        },
        {
            "Sid": "AgentCoreEvaluationBedrockMantleInference",
            "Effect": "Allow",
            "Action": "bedrock-mantle:CreateInference",
            "Resource": "arn:aws:bedrock-mantle:*:*:project/*",
            "Condition": {
                "StringEquals": {
                    "aws:ResourceAccount": "${aws:PrincipalAccount}"
                }
            }
        },
        {
            "Sid": "AgentCoreEvaluationBedrockMantleCallWithBearerToken",
            "Effect": "Allow",
            "Action": "bedrock-mantle:CallWithBearerToken",
            "Resource": "*"
        }
    ]
}
```

## Permissions in CloudWatchOmniSpaceAccessPolicy
<a name="omni-iam-policies-to-use-cloudwatch-omni-permissions-in-cloudwatchomnispaceaccesspolicy"></a>

This is the base policy, always attached. It grants the space experience and the management side of evaluation. The table groups its permissions by what they are for, and gives the condition that limits each group.


| Permission group | What it covers | How it is limited | 
| --- | --- | --- | 
| The space experience, in the cloudwatch namespace | Space and access-grant management, telemetry query sessions, temporary credentials for reading space data, the context graph, alerts, dashboards, access profiles, views, user preferences, threads, agent assets, integrations, intelligence configuration, writing GitHub change events to your account's default CloudWatch Dataset, and tagging. | Every action requires the condition cloudwatch:HasAccessGrant to be true, so a principal with no grant in the space cannot use any of them. | 
| Looking up IAM Identity Center users and groups | identitystore:ListUsers, identitystore:ListGroups, identitystore:DescribeUser, and identitystore:DescribeGroup against your Identity Store directories, users, and groups, used when you search for a person or group to grant access to a space. | The call must arrive through CloudWatch (aws:CalledVia is cloudwatch.amazonaws.com), so the role cannot call Identity Store directly. | 
| A deny on tagging outside CloudWatch Omni | An explicit Deny on the three tagging actions for every resource other than the CloudWatch Omni resource types. | Prevents a space session from tagging a classic CloudWatch resource, such as an alarm or a CloudWatch dashboard, to gain access at the resource level. | 
| Passing a role to CloudWatch Omni | iam:PassRole, so you can hand CloudWatch Omni the service role you created for the space. | Same account, and iam:PassedToService must be cloudwatch.amazonaws.com. The role name cannot be restricted by prefix because you supply your own role. | 
| Passing a role for online evaluations | iam:PassRole for the evaluation execution role, so an online evaluation can run when nobody is signed in. | Restricted to roles named service-role/AgentCoreEvaluationRole\* in your own account, passed only to bedrock-agentcore.amazonaws.com. | 
| Creating the partner integration role | iam:CreateRole, iam:PutRolePolicy, and iam:GetRoleTemplateVersion, so CloudWatch Omni can create the IAM role in your account that a partner investigation agent uses to read your CloudWatch data within your access grants, when a space admin connects a third-party agent. | Restricted to roles named service-role/CloudWatchExternalAgentIntegration-\* in your own account (aws:ResourceAccount equals ${aws:PrincipalAccount}), only when the call arrives through CloudWatch (aws:CalledVia is cloudwatch.amazonaws.com), and only for roles created from the CloudWatch-owned role template CloudWatchExternalAgentIntegrationRoleTemplate (iam:RoleTemplateARN). iam:GetRoleTemplateVersion is limited to that template. | 
| Creating the AWS DevOps Agent investigation role | iam:CreateRole, iam:AttachRolePolicy, and iam:GetRoleTemplateVersion, so CloudWatch Omni can create the investigation role in your account and attach its policy when you connect the AWS DevOps Agent integration. | Restricted to roles named service-role/CloudWatchOmniDevOpsAgentInvestigationRole-\* in your own account, only when the call arrives through CloudWatch (aws:CalledVia is cloudwatch.amazonaws.com), and only for roles created from the CloudWatch-owned template CloudWatchOmniDevOpsAgentInvestigationAccessRoleTemplate (iam:RoleTemplateARN). iam:AttachRolePolicy is further limited by iam:PolicyARN to the single AWS managed policy CloudWatchOmniDevOpsAgentInvestigationServiceRolePolicy. | 
| Reading ingestion users | iam:ListUserTags and iam:ListServiceSpecificCredentials, so the console can show the bearer tokens that already exist. | Restricted to users under the omni/ path named OmniIngestionUser-\* in your own account. Read-only: CloudWatch Omni cannot create, rotate, or delete them. | 
| Reading a customer managed key | kms:DescribeKey, so the console can validate and display a key you select. | Same account. Metadata only, and it does not permit any cryptographic operation. | 
| Encrypting space content | kms:Decrypt and kms:GenerateDataKey against the key you chose for the space. | Four conditions together: same account, the key carries the cw-omni tag, the call arrives through CloudWatch, and the encryption context names a space ARN — so the key cannot be used for any other CloudWatch resource type. | 
| Reading an encrypted IAM Identity Center directory | kms:Decrypt against the customer managed key that encrypts your IAM Identity Center directory, so the directory lookups above can read it. | The call must come through Identity Store (kms:ViaService), and the encryption context must include the aws:identitystore:identitystore-arn key, so it applies only to Identity Store data. It has no same-account condition, because the directory and its key are often in your organization's management account; the key policy remains the control. | 
| Encrypting evaluator material | kms:Decrypt and kms:GenerateDataKey for evaluator and model-provider key material at the time it is used. | Same account, the request must arrive via bedrock-agentcore.amazonaws.com, and the encryption context must name an evaluator ARN in your own account. | 
| Evaluators, datasets, and online evaluation configurations | Full lifecycle of the Amazon Bedrock AgentCore resources that back evaluation, including running an evaluation and tagging these resources. | Scoped separately to the evaluator, dataset, and online-evaluation-config resource types, each in your own account. | 
| Listing the model catalog | bedrock:ListFoundationModels and bedrock:ListInferenceProfiles, so you can pick a model when you create an evaluator or open the playground. | Listing only. Invoking a model requires the separate inference policy above. | 
| Writing evaluation results | Creating the log groups, log streams, and log events that record evaluation scores and annotations in CloudWatch Logs. | Log streams and events are written only under /aws/cloudwatch/; under /aws/bedrock-agentcore/evaluations/ only the log group itself can be created. Both in your own account. | 
| Choosing which telemetry an online evaluation reads | logs:DescribeLogGroups for the log group picker, and reading and appending a field index on the trace log group so sampling can filter spans by service name. | Same account. The picker lists any log group in the account, because telemetry does not always follow the /aws/ naming conventions. Names only, not contents. | 
| Running a code-based evaluator | lambda:InvokeFunction and lambda:GetFunction for evaluators you implement as code rather than as a prompt. | Restricted to functions named cloudwatchCodeEvaluator\* in your own account. | 
| Storing a model-provider API key | Creating, reading, updating the value of, deleting, and tagging the Secrets Manager secret that holds a model-provider API key you supply. | Restricted to secrets whose name begins cw-omni- that carry the cw-omni tag, in your own account. Creating one also requires the cw-omni tag on the request. | 
| AWS Config resource inventory | The AWS Config service-linked configuration recorder, its status, and the AWS Config service-linked role, used to collect resource inventory for your account. | Same account, and the recorder's service principal must be cloudwatch.amazonaws.com. Creating the service-linked role is restricted to the config.amazonaws.com path. | 

## Permissions that read across your whole account
<a name="omni-iam-policies-to-use-cloudwatch-omni-permissions-that-read-across-your-whole-account"></a>

Five permission groups grant permissions that the underlying API cannot restrict to a subset of resources, so they enumerate metadata across your entire account:
+ `iam:ListRoles`, `iam:GetRole`, and `iam:ListAttachedRolePolicies` reach any IAM role in the account, including its details and the managed policies attached to it.
+ `iam:ListUsers` reaches the name of any IAM user, not only the ingestion users.
+ `secretsmanager:ListSecrets` reaches the name and metadata of every secret, not only the ones CloudWatch Omni creates.
+ `sns:ListTopics` reaches the ARN of every Amazon SNS topic in the account, so you can choose a notification target for an alert. It returns topic ARNs only (no attributes, subscriptions, or messages).
+ `bedrock:ListFoundationModels` and `bedrock:ListInferenceProfiles` list the models and inference profiles available to you.

None of them permits a change, and none reads the contents of anything. Apart from creating the AWS Config service-linked role, this policy grants no permission to create, modify, or delete an IAM role, user, or policy, and reading a secret value is a separate permission limited to secrets in your own account whose name begins with `cw-omni-` and that carry the `cw-omni` tag.

For the complete policy document, see [CloudWatchOmniSpaceAccessPolicy](https://docs.aws.amazon.com/aws-managed-policy/latest/reference/CloudWatchOmniSpaceAccessPolicy.html) in the *AWS Managed Policy Reference*.

## Permissions in CloudWatchOmniAWSIntegrationPolicyV2
<a name="omni-iam-policies-to-use-cloudwatch-omni-permissions-in-cloudwatchomniawsintegrationpolicyv2"></a>

`CloudWatchOmniAWSIntegrationPolicyV2` holds every permission in [CloudWatchOmniAWSIntegrationPolicy](https://docs.aws.amazon.com/aws-managed-policy/latest/reference/CloudWatchOmniAWSIntegrationPolicy.html), plus read access to the logs, traces, and profiles in your account's `default` CloudWatch Dataset. The read covers everything stored in the `default` Dataset, in every Region of your account, such as the logs and traces that your Dataset integration forwards. These permissions read content, not only metadata. Unlike the telemetry permissions in `CloudWatchOmniSpaceAccessPolicy`, they have no `cloudwatch:HasAccessGrant` condition, so access grants do not limit them.

`CloudWatchOmniAWSIntegrationPolicyV2` grants the following permissions in addition to those in `CloudWatchOmniAWSIntegrationPolicy`:
+ `cloudwatch:StartTelemetryQuerySession`, `cloudwatch:StartTelemetryQuery`, `cloudwatch:GetTelemetryQueryResults`, `cloudwatch:StopTelemetryQuery`, `cloudwatch:StopTelemetryQuerySession`, and `cloudwatch:ListTelemetryQuerySessions` run telemetry queries, only in your own account.
+ `cloudwatch:GetRecords` and `cloudwatch:GetProfileRecords` read the logs, traces, and profiles in your own account's `default` Dataset.
+ `kms:Decrypt` works only through CloudWatch, only on keys in your account, and only for the encryption context of the `default` Dataset. CloudWatch Omni needs it only when the `default` Dataset is encrypted with a customer managed key. In that case, the key policy must also allow `kms:Decrypt` for the IAM role that has this policy attached, either by naming the role or by allowing IAM policies in your account to use the key. See [Sample key policy](omni-data-encryption-in-cloudwatch-omni.md#omni-data-encryption-in-cloudwatch-omni-sample-key-policy).

For the complete policy document, see [CloudWatchOmniAWSIntegrationPolicyV2](https://docs.aws.amazon.com/aws-managed-policy/latest/reference/CloudWatchOmniAWSIntegrationPolicyV2.html) in the *AWS Managed Policy Reference*.

## Permissions you provide yourself
<a name="omni-iam-policies-to-use-cloudwatch-omni-permissions-you-provide-yourself"></a>

The managed policies cover using a space. They do not cover creating one, and they do not cover telemetry ingestion.


| To do this | You need | 
| --- | --- | 
| Create a domain or a space | Setup actions that neither managed policy grants. See [Set up Omni](omni-set-up-omni.md). | 
| Pass a role that you supply | iam:PassRole on your own calling principal for the role you pass, including your own operator role, the domain access role, and the evaluation execution role. | 
| Send telemetry with a bearer token | Your own IAM permissions to create the ingestion user and its credential. The user carries CloudWatchOmniOTLPPolicy. Bearer tokens apply to metrics, logs, and traces, with a separate API key for each. For traces, see [Setting up bearer token authentication for traces](https://docs.aws.amazon.com/xray/latest/devguide/xray-opentelemetry-bearer-token.html) in the X-Ray Developer Guide. See [Identity and access management for CloudWatch Omni](omni-identity-and-access-management-for-cloudwatch-omni.md). | 
| Use a customer managed key | A key policy that allows the space operator role to use the key, and the cw-omni tag on the key. See [Data encryption in CloudWatch Omni](omni-data-encryption-in-cloudwatch-omni.md). | 