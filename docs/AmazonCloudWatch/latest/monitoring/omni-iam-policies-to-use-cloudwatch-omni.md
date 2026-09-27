

# IAM policies to use CloudWatch Omni
<a name="omni-iam-policies-to-use-cloudwatch-omni"></a>

The space operator role carries `CloudWatchOmniSpaceAccessPolicy` as its base policy, with `CloudWatchOmniModelInferencePolicy` and `CloudWatchOmniAWSIntegrationPolicy` as optional additions chosen during setup. Between them they cover using a space: querying telemetry, managing alerts and dashboards, and creating and running evaluations. None covers creating a space or a domain, so setup needs permissions you grant yourself. CloudWatch Omni provides further managed policies for other roles, including `CloudWatchOmniDomainAccessPolicy` for organization domain administration. For the complete set, see [AWS managed policies for CloudWatch Omni](omni-aws-managed-policies-for-cloudwatch-omni.md).

This page enumerates what each policy grants and why, discloses the permissions that read metadata across your whole account, and lists the permissions you must add separately. For how CloudWatch Omni works with IAM in general (resource types, condition keys, and the roles setup creates), see [Identity and access management for CloudWatch Omni](omni-identity-and-access-management-for-cloudwatch-omni.md).

**Topics**
+ Permissions in CloudWatchOmniModelInferencePolicy
+ Permissions in CloudWatchOmniSpaceAccessPolicy
+ Permissions that read across your whole account
+ Permissions you provide yourself

**Permissions in CloudWatchOmniModelInferencePolicy**

This policy grants model inference and nothing else. It is attached only to spaces that use the prompt playground or run evaluations that invoke a model. A space that only views telemetry does not receive it, and a space can create and view its evaluation configuration without it. Only running a model requires it.


| Action | Resources | Why CloudWatch Omni needs it | 
| --- | --- | --- | 
| bedrock:InvokeModel, bedrock:InvokeModelWithResponseStream | Foundation models and inference profiles | Runs the model you select in the prompt playground, and the model an evaluator uses to score a result. | 
| bedrock-mantle:CreateInference | Amazon Bedrock Mantle projects | Runs a model served through Amazon Bedrock Mantle rather than as a Bedrock foundation model. | 
| bedrock-mantle:CallWithBearerToken | All resources | Authenticates the Amazon Bedrock Mantle inference call above. | 

Every action except `bedrock-mantle:CallWithBearerToken` is restricted to your own account by an `aws:ResourceAccount` condition, so a space can invoke only the models, inference profiles, and projects in the account it belongs to. `CallWithBearerToken` has no resource type in the IAM action model, so it cannot be scoped to a resource or narrowed by a condition. The same action appears with the same unscoped resource in the AWS managed policy [BedrockAgentCoreFullAccess](https://docs.aws.amazon.com/aws-managed-policy/latest/reference/BedrockAgentCoreFullAccess.html), which uses it for the same purpose.

```
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

**Permissions in CloudWatchOmniSpaceAccessPolicy**

This is the base policy, always attached. It grants the space experience and the management side of evaluation. The table groups its permissions by what they are for, and gives the condition that limits each group.


| Permission group | What it covers | How it is limited | 
| --- | --- | --- | 
| The space experience, in the cloudwatch namespace | Space and access-grant management, telemetry query sessions, the context graph, alerts, dashboards, access profiles, views, user preferences, threads, integrations, intelligence configuration, and tagging. | Every action requires the condition cloudwatch:HasAccessGrant to be true, so a principal with no grant in the space cannot use any of them. | 
| A deny on tagging outside CloudWatch Omni | An explicit Deny on the three tagging actions for every resource other than the CloudWatch Omni resource types. | Prevents a space session from tagging a classic CloudWatch resource, such as an alarm or a CloudWatch dashboard, to gain access at the resource level. | 
| Passing a role to CloudWatch Omni | iam:PassRole, so you can hand CloudWatch Omni the service role you created for the space. | Same account, and iam:PassedToService must be cloudwatch.amazonaws.com. The role name cannot be restricted by prefix because you supply your own role. | 
| Passing a role for online evaluations | iam:PassRole for the evaluation execution role, so an online evaluation can run when nobody is signed in. | Restricted to roles named service-role/AgentCoreEvaluationRole\* in your own account, passed only to bedrock-agentcore.amazonaws.com. | 
| Reading ingestion users | iam:ListUserTags and iam:ListServiceSpecificCredentials, so the console can show the bearer tokens that already exist. | Restricted to users under the omni/ path named OmniIngestionUser-\* in your own account. Read-only: CloudWatch Omni cannot create, rotate, or delete them. | 
| Reading a customer managed key | kms:DescribeKey, so the console can validate and display a key you select. | Same account. Metadata only, and it does not permit any cryptographic operation. | 
| Encrypting space content | kms:Decrypt and kms:GenerateDataKey against the key you chose for the space. | Four conditions together: same account, the key carries the cw-omni tag, the call arrives through CloudWatch, and the encryption context names a space ARN — so the key cannot be used for any other CloudWatch resource type. | 
| Encrypting evaluator material | kms:Decrypt and kms:GenerateDataKey for evaluator and model-provider key material at the time it is used. | Same account, the request must arrive via bedrock-agentcore.amazonaws.com, and the encryption context must name an evaluator ARN in your own account. | 
| Evaluators, datasets, and online evaluation configurations | Full lifecycle of the Amazon Bedrock AgentCore resources that back evaluation, including running an evaluation and tagging these resources. | Scoped separately to the evaluator, dataset, and online-evaluation-config resource types, each in your own account. | 
| Listing the model catalog | bedrock:ListFoundationModels and bedrock:ListInferenceProfiles, so you can pick a model when you create an evaluator or open the playground. | Listing only. Invoking a model requires the separate inference policy above. | 
| Writing evaluation results | Creating the log groups, log streams, and log events that record evaluation scores and annotations in CloudWatch Logs. | Log streams and events are written only under /aws/cloudwatch/; under /aws/bedrock-agentcore/evaluations/ only the log group itself can be created. Both in your own account. | 
| Choosing which telemetry an online evaluation reads | logs:DescribeLogGroups for the log group picker, and reading and appending a field index on the trace log group so sampling can filter spans by service name. | Same account. The picker lists any log group in the account, because telemetry does not always follow the /aws/ naming conventions. Names only, not contents. | 
| Running a code-based evaluator | lambda:InvokeFunction and lambda:GetFunction for evaluators you implement as code rather than as a prompt. | Restricted to functions named cloudwatchCodeEvaluator\* in your own account. | 
| Storing a model-provider API key | Creating, reading, updating the value of, deleting, and tagging the Secrets Manager secret that holds a model-provider API key you supply. | Restricted to secrets whose name begins cw-omni- that carry the cw-omni tag, in your own account. Creating one also requires the cw-omni tag on the request. | 
| AWS Config resource inventory | The AWS Config service-linked configuration recorder, its status, and the AWS Config service-linked role, used to collect resource inventory for your account. | Same account, and the recorder's service principal must be cloudwatch.amazonaws.com. Creating the service-linked role is restricted to the config.amazonaws.com path. | 

**Permissions that read across your whole account**

Four permission groups grant permissions that the underlying API cannot restrict to a subset of resources, so they enumerate metadata across your entire account:
+ `iam:ListRoles`, `iam:GetRole`, and `iam:ListAttachedRolePolicies` reach any IAM role in the account, including its details and the managed policies attached to it.
+ `iam:ListUsers` reaches the name of any IAM user, not only the ingestion users.
+ `secretsmanager:ListSecrets` reaches the name and metadata of every secret, not only the ones CloudWatch Omni creates.
+ `bedrock:ListFoundationModels` and `bedrock:ListInferenceProfiles` list the models and inference profiles available to you.

None of them permits a change, and none reads the contents of anything. Apart from creating the AWS Config service-linked role, this policy grants no permission to create, modify, or delete an IAM role, user, or policy, and reading a secret value is a separate permission limited to secrets in your own account whose name begins with `cw-omni-` and that carry the `cw-omni` tag.

For the complete policy document, see [CloudWatchOmniSpaceAccessPolicy](https://docs.aws.amazon.com/aws-managed-policy/latest/reference/CloudWatchOmniSpaceAccessPolicy.html) in the *AWS Managed Policy Reference*.

**Permissions you provide yourself**

The managed policies cover using a space. They do not cover creating one, and they do not cover telemetry ingestion.


| To do this | You need | 
| --- | --- | 
| Create a domain or a space | Setup actions that neither managed policy grants. See [Set up Omni](omni-set-up-omni.md). | 
| Pass a role that you supply | iam:PassRole on your own calling principal for the role you pass, including your own operator role, the domain access role, and the evaluation execution role. | 
| Send metrics or logs with a bearer token | Your own IAM permissions to create the ingestion user and its credential. The user carries CloudWatchOmniOTLPPolicy. Bearer tokens apply to metrics and logs only. Traces are signed with Signature Version 4. See [Identity and access management for CloudWatch Omni](omni-identity-and-access-management-for-cloudwatch-omni.md). | 
| Use a customer managed key | A key policy that allows the space operator role to use the key, and the cw-omni tag on the key. See [Data encryption in CloudWatch Omni](omni-data-encryption-in-cloudwatch-omni.md). | 