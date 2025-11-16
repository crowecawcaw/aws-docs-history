# AWS managed policies for

Amazon Lex V2

An AWS managed policy is a standalone policy that is created and administered by AWS. AWS managed policies are designed
to provide permissions for many common use cases so that you can start assigning permissions to users, groups, and roles.

Keep in mind that AWS managed policies might not grant least-privilege permissions for your specific use cases because
they're available for all AWS customers to use. We recommend that you reduce permissions further by defining
[customer managed policies](../../../IAM/latest/UserGuide/access_policies_managed-vs-inline.md#customer-managed-policies "../../../IAM/latest/UserGuide/access_policies_managed-vs-inline.md#customer-managed-policies") that are specific to your use cases.

You cannot change the permissions defined in AWS managed policies. If AWS updates the permissions defined in an AWS
managed policy, the update affects all principal identities (users, groups, and roles) that the policy is attached to. AWS is
most likely to update an AWS managed policy when a new AWS service is launched or new API operations become available for
existing services.

For more information, see [AWS managed policies](../../../IAM/latest/UserGuide/access_policies_managed-vs-inline.md#aws-managed-policies "../../../IAM/latest/UserGuide/access_policies_managed-vs-inline.md#aws-managed-policies") in the
_IAM User Guide_.

## AWS

managed policy: AmazonLexReadOnly

You can attach the `AmazonLexReadOnly` policy to your
IAM identities.

This policy grants read-only permissions that allow users to view
all actions in the Amazon Lex V2 and Amazon Lex model building
service.

**Permissions details**

This policy includes the following permissions:

- `lex` – Read-only access to Amazon Lex V2
  and Amazon Lex resources in the model building
  service.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Sid": "AmazonLexReadOnlyStatement1",
 "Effect": "Allow",
 "Action": [
 "lex:GetBot",
 "lex:GetBotAlias",
 "lex:GetBotAliases",
 "lex:GetBots",
 "lex:GetBotChannelAssociation",
 "lex:GetBotChannelAssociations",
 "lex:GetBotVersions",
 "lex:GetBuiltinIntent",
 "lex:GetBuiltinIntents",
 "lex:GetBuiltinSlotTypes",
 "lex:GetIntent",
 "lex:GetIntents",
 "lex:GetIntentVersions",
 "lex:GetSlotType",
 "lex:GetSlotTypes",
 "lex:GetSlotTypeVersions",
 "lex:GetUtterancesView",
 "lex:DescribeBot",
 "lex:DescribeBotAlias",
 "lex:DescribeBotChannel",
 "lex:DescribeBotLocale",
 "lex:DescribeBotRecommendation",
 "lex:DescribeBotReplica",
 "lex:DescribeBotVersion",
 "lex:DescribeExport",
 "lex:DescribeImport",
 "lex:DescribeIntent",
 "lex:DescribeResourcePolicy",
 "lex:DescribeSlot",
 "lex:DescribeSlotType",
 "lex:ListBots",
 "lex:ListBotLocales",
 "lex:ListBotAliases",
 "lex:ListBotAliasReplicas",
 "lex:ListBotChannels",
 "lex:ListBotRecommendations",
 "lex:ListBotReplicas",
 "lex:ListBotVersions",
 "lex:ListBotVersionReplicas",
 "lex:ListBuiltInIntents",
 "lex:ListBuiltInSlotTypes",
 "lex:ListExports",
 "lex:ListImports",
 "lex:ListIntents",
 "lex:ListRecommendedIntents",
 "lex:ListSlots",
 "lex:ListSlotTypes",
 "lex:ListTagsForResource",
 "lex:SearchAssociatedTranscripts",
 "lex:ListCustomVocabularyItems"
 ],
 "Resource": "*"
 }
 ]
}`

```

## AWS

managed policy: AmazonLexRunBotsOnly

You can attach the `AmazonLexRunBotsOnly` policy to
your IAM identities.

This policy grants read-only permissions that allow access to run
Amazon Lex V2 and Amazon Lex conversational bots. .

**Permissions details**

This policy includes the following permissions:

- `lex` – Read-only access to all actions
  in the Amazon Lex V2 and Amazon Lex runtime.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Action": [
 "lex:PostContent",
 "lex:PostText",
 "lex:PutSession",
 "lex:GetSession",
 "lex:DeleteSession",
 "lex:RecognizeText",
 "lex:RecognizeUtterance",
 "lex:StartConversation"
 ],
 "Resource": "*"
 }
 ]
}`

```

## AWS

managed policy: AmazonLexFullAccess

You can attach the `AmazonLexFullAccess` policy to your
IAM identities.

This policy grants administrative permissions that allow the user
permission to create, read, update, and delete Amazon Lex V2 and
Amazon Lex resources; and to run Amazon Lex V2 and Amazon Lex
conversational bots.

**Permissions details**

This policy includes the following permissions:

- `lex` – Allows principals read and write
  access to all actions in the Amazon Lex V2 and Amazon Lex model
  building and runtime services.
- `cloudwatch` – Allows principals to view
  Amazon CloudWatch metrics and alarms.
- `iam` – Allows principals to create and
  delete service-linked roles, pass roles, and attach and
  detach policies to a role. The permissions are restricted to
  "lex.amazonaws.com" for Amazon Lex operations and to
  "lexv2.amazonaws.com" for Amazon Lex V2 operations.
- `kendra` – Allows principals to list
  Amazon Kendra indexes.
- `kms` – Allows principals to describe
  AWS KMS keys and aliases.
- `lambda` – Allows principals to list
  AWS Lambda functions and manage permissions attached to any
  Lambda function.
- `polly` – Allows principals to describe
  Amazon Polly voices and synthesize speech.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Sid": "AmazonLexFullAccessStatement1",
 "Effect": "Allow",
 "Action": [
 "cloudwatch:GetMetricStatistics",
 "cloudwatch:DescribeAlarms",
 "cloudwatch:DescribeAlarmsForMetric",
 "kms:DescribeKey",
 "kms:ListAliases",
 "lambda:GetPolicy",
 "lambda:ListFunctions",
 "lambda:ListAliases",
 "lambda:ListVersionsByFunction",
 "lex:*",
 "polly:DescribeVoices",
 "polly:SynthesizeSpeech",
 "kendra:ListIndices",
 "iam:ListRoles",
 "s3:ListAllMyBuckets",
 "logs:DescribeLogGroups",
 "s3:GetBucketLocation"
 ],
 "Resource": [
 "*"
 ]
 },
 {
 "Sid": "AmazonLexFullAccessStatement2",
 "Effect": "Allow",
 "Action": [
 "bedrock:ListFoundationModels"
 ],
 "Resource": "*"
 },
 {
 "Effect": "Allow",
 "Action": [
 "bedrock:InvokeModel"
 ],
 "Resource": "arn:aws:bedrock:*::foundation-model/*"
 },
 {
 "Effect": "Allow",
 "Action": [
 "lambda:AddPermission",
 "lambda:RemovePermission"
 ],
 "Resource": "arn:aws:lambda:*:*:function:AmazonLex*",
 "Condition": {
 "StringEquals": {
 "lambda:Principal": "lex.amazonaws.com"
 }
 }
 },
 {
 "Sid": "AmazonLexFullAccessStatement3",
 "Effect": "Allow",
 "Action": [
 "iam:GetRole",
 "iam:GetRolePolicy"
 ],
 "Resource": [
 "arn:aws:iam::*:role/aws-service-role/lex.amazonaws.com/AWSServiceRoleForLexBots",
 "arn:aws:iam::*:role/aws-service-role/channels.lex.amazonaws.com/AWSServiceRoleForLexChannels",
 "arn:aws:iam::*:role/aws-service-role/lexv2.amazonaws.com/AWSServiceRoleForLexV2Bots*",
 "arn:aws:iam::*:role/aws-service-role/channels.lexv2.amazonaws.com/AWSServiceRoleForLexV2Channels*",
 "arn:aws:iam::*:role/aws-service-role/replication.lexv2.amazonaws.com/AWSServiceRoleForLexV2Replication*"
 ]
 },
 {
 "Sid": "AmazonLexFullAccessStatement4",
 "Effect": "Allow",
 "Action": [
 "iam:CreateServiceLinkedRole"
 ],
 "Resource": [
 "arn:aws:iam::*:role/aws-service-role/lex.amazonaws.com/AWSServiceRoleForLexBots"
 ],
 "Condition": {
 "StringEquals": {
 "iam:AWSServiceName": "lex.amazonaws.com"
 }
 }
 },
 {
 "Sid": "AmazonLexFullAccessStatement5",
 "Effect": "Allow",
 "Action": [
 "iam:CreateServiceLinkedRole"
 ],
 "Resource": [
 "arn:aws:iam::*:role/aws-service-role/channels.lex.amazonaws.com/AWSServiceRoleForLexChannels"
 ],
 "Condition": {
 "StringEquals": {
 "iam:AWSServiceName": "channels.lex.amazonaws.com"
 }
 }
 },
 {
 "Sid": "AmazonLexFullAccessStatement6",
 "Effect": "Allow",
 "Action": [
 "iam:CreateServiceLinkedRole"
 ],
 "Resource": [
 "arn:aws:iam::*:role/aws-service-role/lexv2.amazonaws.com/AWSServiceRoleForLexV2Bots*"
 ],
 "Condition": {
 "StringEquals": {
 "iam:AWSServiceName": "lexv2.amazonaws.com"
 }
 }
 },
 {
 "Sid": "AmazonLexFullAccessStatement7",
 "Effect": "Allow",
 "Action": [
 "iam:CreateServiceLinkedRole"
 ],
 "Resource": [
 "arn:aws:iam::*:role/aws-service-role/channels.lexv2.amazonaws.com/AWSServiceRoleForLexV2Channels*"
 ],
 "Condition": {
 "StringEquals": {
 "iam:AWSServiceName": "channels.lexv2.amazonaws.com"
 }
 }
 },
 {
 "Sid": "AmazonLexFullAccessStatement8",
 "Effect": "Allow",
 "Action": [
 "iam:CreateServiceLinkedRole"
 ],
 "Resource": [
 "arn:aws:iam::*:role/aws-service-role/replication.lexv2.amazonaws.com/AWSServiceRoleForLexV2Replication*"
 ],
 "Condition": {
 "StringEquals": {
 "iam:AWSServiceName": "replication.lexv2.amazonaws.com"
 }
 }
 },
 {
 "Sid": "AmazonLexFullAccessStatement9",
 "Effect": "Allow",
 "Action": [
 "iam:DeleteServiceLinkedRole",
 "iam:GetServiceLinkedRoleDeletionStatus"
 ],
 "Resource": [
 "arn:aws:iam::*:role/aws-service-role/lex.amazonaws.com/AWSServiceRoleForLexBots",
 "arn:aws:iam::*:role/aws-service-role/channels.lex.amazonaws.com/AWSServiceRoleForLexChannels",
 "arn:aws:iam::*:role/aws-service-role/lexv2.amazonaws.com/AWSServiceRoleForLexV2Bots*",
 "arn:aws:iam::*:role/aws-service-role/channels.lexv2.amazonaws.com/AWSServiceRoleForLexV2Channels*",
 "arn:aws:iam::*:role/aws-service-role/replication.lexv2.amazonaws.com/AWSServiceRoleForLexV2Replication*"
 ]
 },
 {
 "Sid": "AmazonLexFullAccessStatement10",
 "Effect": "Allow",
 "Action": [
 "iam:PassRole"
 ],
 "Resource": [
 "arn:aws:iam::*:role/aws-service-role/lex.amazonaws.com/AWSServiceRoleForLexBots"
 ],
 "Condition": {
 "StringEquals": {
 "iam:PassedToService": [
 "lex.amazonaws.com"
 ]
 }
 }
 },
 {
 "Sid": "AmazonLexFullAccessStatement11",
 "Effect": "Allow",
 "Action": [
 "iam:PassRole"
 ],
 "Resource": [
 "arn:aws:iam::*:role/aws-service-role/lexv2.amazonaws.com/AWSServiceRoleForLexV2Bots*"
 ],
 "Condition": {
 "StringEquals": {
 "iam:PassedToService": [
 "lexv2.amazonaws.com"
 ]
 }
 }
 },
 {
 "Sid": "AmazonLexFullAccessStatement12",
 "Effect": "Allow",
 "Action": [
 "iam:PassRole"
 ],
 "Resource": [
 "arn:aws:iam::*:role/aws-service-role/channels.lexv2.amazonaws.com/AWSServiceRoleForLexV2Channels*"
 ],
 "Condition": {
 "StringEquals": {
 "iam:PassedToService": [
 "channels.lexv2.amazonaws.com"
 ]
 }
 }
 },
 {
 "Sid": "AmazonLexFullAccessStatement13",
 "Effect": "Allow",
 "Action": [
 "iam:PassRole"
 ],
 "Resource": [
 "arn:aws:iam::*:role/aws-service-role/replication.lexv2.amazonaws.com/AWSServiceRoleForLexV2Replication*"
 ],
 "Condition": {
 "StringEquals": {
 "iam:PassedToService": [
 "lexv2.amazonaws.com"
 ]
 }
 }
 }
 ]
}`

```

## AWS

managed policy: AmazonLexReplicationPolicy

You can't attach `AmazonLexReplicationPolicy` to your IAM entities. This
policy is attached to a service-linked role that allows Amazon Lex V2 to perform actions on
your behalf. For more information, see [Using service-linked roles for
Amazon Lex V2](using-service-linked-roles.md "using-service-linked-roles.md").

This policy grants administrative permissions that allows Amazon Lex V2 to replicate AWS
resources across Regions on your behalf. You can attach this policy to permit a role to
easily replicate resources, including bots, locales, versions, aliases, intents, slot
types, slots, and custom vocabularies.

**Permissions details**

This policy includes the following permissions.

- `lex` – Allows principals to replicate resources in other
  Regions.
- `iam` – Allows principals to pass roles from IAM. This is
  required so that Amazon Lex V2 has permissions to replicate resources in other
  Regions.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Sid": "ReplicationPolicyStatement1",
 "Effect": "Allow",
 "Action": [
 "lex:BuildBotLocale",
 "lex:ListBotLocales",
 "lex:CreateBotAlias",
 "lex:UpdateBotAlias",
 "lex:DeleteBotAlias",
 "lex:DescribeBotAlias",
 "lex:CreateBotVersion",
 "lex:DeleteBotVersion",
 "lex:DescribeBotVersion",
 "lex:CreateExport",
 "lex:DescribeBot",
 "lex:UpdateExport",
 "lex:DescribeExport",
 "lex:DescribeBotLocale",
 "lex:DescribeIntent",
 "lex:ListIntents",
 "lex:DescribeSlotType",
 "lex:ListSlotTypes",
 "lex:DescribeSlot",
 "lex:ListSlots",
 "lex:DescribeCustomVocabulary",
 "lex:StartImport",
 "lex:DescribeImport",
 "lex:CreateBot",
 "lex:UpdateBot",
 "lex:DeleteBot",
 "lex:CreateBotLocale",
 "lex:UpdateBotLocale",
 "lex:DeleteBotLocale",
 "lex:CreateIntent",
 "lex:UpdateIntent",
 "lex:DeleteIntent",
 "lex:CreateSlotType",
 "lex:UpdateSlotType",
 "lex:DeleteSlotType",
 "lex:CreateSlot",
 "lex:UpdateSlot",
 "lex:DeleteSlot",
 "lex:CreateCustomVocabulary",
 "lex:UpdateCustomVocabulary",
 "lex:DeleteCustomVocabulary",
 "lex:DeleteBotChannel",
 "lex:ListTagsForResource",
 "lex:TagResource",
 "lex:UntagResource",
 "lex:CreateResourcePolicy",
 "lex:DeleteResourcePolicy",
 "lex:DescribeResourcePolicy",
 "lex:UpdateResourcePolicy"
 ],
 "Resource": [
 "arn:aws:lex:*:*:bot/*",
 "arn:aws:lex:*:*:bot-alias/*"
 ]
 },
 {
 "Sid": "ReplicationPolicyStatement2",
 "Effect": "Allow",
 "Action": [
 "lex:CreateUploadUrl",
 "lex:ListBots"
 ],
 "Resource": "*"
 },
 {
 "Sid": "ReplicationPolicyStatement3",
 "Effect": "Allow",
 "Action": [
 "iam:PassRole"
 ],
 "Resource": "*",
 "Condition": {
 "StringEquals": {
 "iam:PassedToService": "lexv2.amazonaws.com"
 }
 }
 }
 ]
}`

```

## AWS

managed policy: AmazonLexV2BedrockAgentPolicy

Amazon Lex V2 policy for Amazon Bedrock agents

Response

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Sid": "LexV2TrustPolicy",
 "Principal": {
 "Service": "lexv2.amazonaws.com"
 },
 "Action": "sts:AssumeRole",
 "Condition": {
 "StringEquals": {
 "aws:SourceAccount": "{`accountId`}"
 }
 }
 }
 ]
}`

```

## AWS

managed policy: AmazonLexV2BedrockKnowledgeBasePolicy

Amazon Lex V2 policy for Amazon Bedrock knowledge bases

Response

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Sid": "LexV2TrustPolicy",
 "Principal": {
 "Service": "lexv2.amazonaws.com"
 },
 "Action": "sts:AssumeRole",
 "Condition": {
 "StringEquals": {
 "aws:SourceAccount": "{`accountId`}"
 }
 }
 }
 ]
}`

```

## AWS

managed policy: AmazonLexV2BedrockAgentPolicyInternal

Amazon Lex V2 internal policy for Amazon Bedrock agents

Response

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Sid": "LexV2InternalTrustPolicy",
 "Principal": {
 "Service": "lexv2.aws.internal"
 },
 "Action": "sts:AssumeRole",
 "Condition": {
 "StringEquals": {
 "aws:SourceAccount": "{`accountId`}"
 }
 }
 }
 ]
}`

```

## AWS

managed policy: AmazonLexV2BedrockKnowledgeBasePolicyInternal

Amazon Lex V2 internal policy for Amazon Bedrock knowledge bases

Response

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Sid": "LexV2InternalTrustPolicy",
 "Effect": "Allow",
 "Principal": {
 "Service": "lexv2.aws.internal"
 },
 "Action": "sts:AssumeRole",
 "Condition": {
 "StringEquals": {
 "aws:SourceAccount": "{`accountId`}"
 }
 }
 }
 ]
}`

```

## Amazon Lex V2 updates

to AWS managed policies

View details about updates to AWS managed policies for Amazon Lex V2
since this service began tracking these changes. For automatic
alerts about changes to this page, subscribe to the RSS feed on the
Amazon Lex V2 [Document history for Amazon Lex V2](doc-history.md "doc-history.md")
page.

| Change                                                                                                                                                                                                      | Description                                                                                                                 | Date              |
| ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------- | ----------------- |
| [AmazonLexReplicationPolicy](#security-iam-awsmanpol-AmazonLexReplicationPolicy "#security-iam-awsmanpol-AmazonLexReplicationPolicy") – Updated policy                                                      | Amazon Lex V2 updated the policy to allow replication of tags and ResourceBasedPolicy.                                      | June 24, 2025     |
| [AmazonLexV2BedrockKnowledgeBasePolicyInternal](#security-iam-awsmanpol-AmazonLexV2BedrockKnowledgeBasePolicyInternal "#security-iam-awsmanpol-AmazonLexV2BedrockKnowledgeBasePolicyInternal") – New policy | Amazon Lex V2 added a new policy to allow replication of Amazon Bedrock knowledge base resources.                           | August 30, 2024   |
| [AmazonLexV2BedrockAgentPolicyInternal](#security-iam-awsmanpol-AmazonLexV2BedrockAgentPolicyInternal "#security-iam-awsmanpol-AmazonLexV2BedrockAgentPolicyInternal") – New policy                         | Amazon Lex V2 added a new policy to allow replication of Amazon Bedrock agent resources.                                    | August 30, 2024   |
| [AmazonLexV2BedrockKnowledgeBasePolicy](#security-iam-awsmanpol-AmazonLexV2BedrockKnowledgeBasePolicy "#security-iam-awsmanpol-AmazonLexV2BedrockKnowledgeBasePolicy") – New policy                         | Amazon Lex V2 added a new policy to allow replication of Amazon Bedrock knowledge base resources.                           | August 30, 2024   |
| [AmazonLexV2BedrockAgentPolicy](#security-iam-awsmanpol-AmazonLexV2BedrockAgentPolicy "#security-iam-awsmanpol-AmazonLexV2BedrockAgentPolicy") – New policy                                                 | Amazon Lex V2 added a new policy to allow replication of Amazon Bedrock agent resources.                                    | August 30, 2024   |
| [AmazonLexReadOnly](#security-iam-awsmanpol-AmazonLexReadOnly "#security-iam-awsmanpol-AmazonLexReadOnly") – Update to an existing<br>policy                                                                | Amazon Lex V2 added new permissions to allow read-only access replicas of bot resources.                                    | May 10, 2024      |
| [AmazonLexFullAccess](#security-iam-awsmanpol-AmazonLexFullAccess "#security-iam-awsmanpol-AmazonLexFullAccess") – Update to an existing policy                                                             | Amazon Lex V2 added new permissions to allow replication of bot resources to other regions.                                 | April 16, 2024    |
| [AmazonLexFullAccess](#security-iam-awsmanpol-AmazonLexFullAccess "#security-iam-awsmanpol-AmazonLexFullAccess") – Update to an existing policy                                                             | Amazon Lex V2 added new permissions to allow replication of bot resources to other regions.                                 | January 31, 2024  |
| [AmazonLexReplicationPolicy](#security-iam-awsmanpol-AmazonLexReplicationPolicy "#security-iam-awsmanpol-AmazonLexReplicationPolicy") – New policy                                                          | Amazon Lex V2 added a new policy to allow replication of bot resources to other regions.                                    | January 31, 2024  |
| [AmazonLexReadOnly](#security-iam-awsmanpol-AmazonLexReadOnly "#security-iam-awsmanpol-AmazonLexReadOnly") – Update to an existing<br>policy                                                                | Amazon Lex V2 added new permissions to allow read-only access to list<br>custom vocabulary items.                           | November 29, 2022 |
| [AmazonLexFullAccess](#security-iam-awsmanpol-AmazonLexFullAccess "#security-iam-awsmanpol-AmazonLexFullAccess") – Update<br>to an existing policy                                                          | Amazon Lex V2 added new permissions to allow<br>read-only access to Amazon Lex V2 model building<br>service operations.     | August 18, 2021   |
| [AmazonLexReadOnly](#security-iam-awsmanpol-AmazonLexReadOnly "#security-iam-awsmanpol-AmazonLexReadOnly") – Update to<br>an existing policy                                                                | Amazon Lex V2 added new permissions to allow<br>read-only access to Amazon Lex V2 Automated Chatbot<br>Designer operations. | December 1, 2021  |
| [AmazonLexFullAccess](#security-iam-awsmanpol-AmazonLexFullAccess "#security-iam-awsmanpol-AmazonLexFullAccess") – Update<br>to an existing policy                                                          | Amazon Lex V2 added new permissions to allow<br>read-only access to Amazon Lex V2 model building<br>service operations.     | August 18, 2021   |
| [AmazonLexReadOnly](#security-iam-awsmanpol-AmazonLexReadOnly "#security-iam-awsmanpol-AmazonLexReadOnly") – Update to<br>an existing policy                                                                | Amazon Lex V2 added new permissions to allow<br>read-only access to Amazon Lex V2 model building<br>service operations.     | August 18, 2021   |
| [AmazonLexRunBotsOnly](#security-iam-awsmanpol-AmazonLexRunBotsOnly "#security-iam-awsmanpol-AmazonLexRunBotsOnly") – Update<br>to an existing policy                                                       | Amazon Lex V2 added new permissions to allow<br>read-only access to Amazon Lex V2 runtime service<br>operations.            | August 18, 2021   |
| Amazon Lex V2<br>started tracking changes                                                                                                                                                                   | Amazon Lex V2 started tracking changes for its<br>AWS managed policies.                                                     | August 18, 2021   |
