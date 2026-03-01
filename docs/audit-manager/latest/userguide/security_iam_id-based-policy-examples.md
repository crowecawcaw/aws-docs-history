# Identity-based policy examples for AWS Audit Manager

By default, users and roles don't have permission to create or modify Audit Manager
resources. To grant users permission to perform actions on the
resources that they need, an IAM administrator can create IAM policies.

To learn how to create an IAM identity-based policy by using these example JSON policy
documents, see [Create IAM policies (console)](../../../IAM/latest/UserGuide/access_policies_create-console.md "../../../IAM/latest/UserGuide/access_policies_create-console.md") in the
_IAM User Guide_.

For details about actions and resource types defined by AWS Audit Manager, including the format of the ARNs for each of the resource types, see [Actions, resources, and condition keys for AWS Audit Manager](../../../service-authorization/latest/reference/list_awsauditmanager.md "../../../service-authorization/latest/reference/list_awsauditmanager.md") in the _Service Authorization Reference_.

###### Contents

- [Policy best practices](security_iam_id-based-policy-examples.md#security_iam_service-with-iam-policy-best-practices "security_iam_id-based-policy-examples.md#security_iam_service-with-iam-policy-best-practices")
- [Allow the minimum permissions required to enable Audit Manager](security_iam_id-based-policy-examples.md#security_iam_id-based-policy-examples-console "security_iam_id-based-policy-examples.md#security_iam_id-based-policy-examples-console")
- [Allow users full administrator access to AWS Audit Manager](security_iam_id-based-policy-examples.md#example-2 "security_iam_id-based-policy-examples.md#example-2")
  - [Example 1 (Managed policy, AWSAuditManagerAdministratorAccess)](security_iam_id-based-policy-examples.md#full-administrator-access-managed-policy "security_iam_id-based-policy-examples.md#full-administrator-access-managed-policy")
  - [Example 2 (Assessment report destination permissions)](security_iam_id-based-policy-examples.md#full-administrator-access-assessment-report-destination "security_iam_id-based-policy-examples.md#full-administrator-access-assessment-report-destination")
  - [Example 3 (Permissions to enable evidence finder)](security_iam_id-based-policy-examples.md#full-administrator-access-enable-evidence-finder "security_iam_id-based-policy-examples.md#full-administrator-access-enable-evidence-finder")
  - [Example 4 (Permissions to disable evidence finder)](security_iam_id-based-policy-examples.md#full-administrator-access-disable-evidence-finder "security_iam_id-based-policy-examples.md#full-administrator-access-disable-evidence-finder")

- [Allow users management access to AWS Audit Manager](security_iam_id-based-policy-examples.md#management-access "security_iam_id-based-policy-examples.md#management-access")
- [Allow users read-only access to AWS Audit Manager](security_iam_id-based-policy-examples.md#read-only "security_iam_id-based-policy-examples.md#read-only")
- [Allow users to view their own permissions](security_iam_id-based-policy-examples.md#security_iam_id-based-policy-examples-view-own-permissions "security_iam_id-based-policy-examples.md#security_iam_id-based-policy-examples-view-own-permissions")
- [Allow AWS Audit Manager to send notifications to Amazon SNS topics](security_iam_id-based-policy-examples.md#sns-access "security_iam_id-based-policy-examples.md#sns-access")
  - [Example 1 (Permissions for the SNS topic)](security_iam_id-based-policy-examples.md#sns-topic-permissions "security_iam_id-based-policy-examples.md#sns-topic-permissions")
  - [Example 2 (Permissions for the KMS key that's attached to the SNS topic)](security_iam_id-based-policy-examples.md#sns-key-permissions "security_iam_id-based-policy-examples.md#sns-key-permissions")

- [Allow users to run search queries in evidence finder](security_iam_id-based-policy-examples.md#evidence-finder-query-access "security_iam_id-based-policy-examples.md#evidence-finder-query-access")

## Policy best practices

Identity-based policies determine whether someone can create, access, or delete Audit Manager resources in your
account. These actions can incur costs for your AWS account. When you create or edit identity-based policies, follow these guidelines and
recommendations:

- **Get started with AWS managed policies and move toward least-privilege permissions**
  – To get started granting permissions to your users and workloads, use the _AWS
  managed policies_ that grant permissions for many common use cases. They are
  available in your AWS account. We recommend that you reduce permissions further by
  defining AWS customer managed policies that are specific to your use cases. For more information, see
  [AWS managed policies](../../../IAM/latest/UserGuide/access_policies_managed-vs-inline.md#aws-managed-policies "../../../IAM/latest/UserGuide/access_policies_managed-vs-inline.md#aws-managed-policies") or [AWS managed policies for job functions](../../../IAM/latest/UserGuide/access_policies_job-functions.md "../../../IAM/latest/UserGuide/access_policies_job-functions.md") in the _IAM User Guide_.
- **Apply least-privilege permissions** –
  When you set permissions with IAM policies, grant only the permissions required to
  perform a task. You do this by defining the actions that can be taken on specific resources
  under specific conditions, also known as _least-privilege permissions_.
  For more information about using IAM to apply permissions, see [Policies and permissions in IAM](../../../IAM/latest/UserGuide/access_policies.md "../../../IAM/latest/UserGuide/access_policies.md") in the _IAM User Guide_.
- **Use conditions in IAM policies to further restrict access**
  – You can add a condition to your policies to limit access to actions and resources. For example, you can write a policy condition to specify that all requests must
  be sent using SSL. You can also use conditions to grant access to service actions
  if they are used through a specific AWS service, such as CloudFormation. For more information, see
  [IAM JSON policy elements: Condition](../../../IAM/latest/UserGuide/reference_policies_elements_condition.md "../../../IAM/latest/UserGuide/reference_policies_elements_condition.md") in the _IAM User Guide_.
- **Use IAM Access Analyzer to validate your IAM policies to ensure secure and functional permissions**
  – IAM Access Analyzer validates new and existing policies so that the policies adhere to the IAM policy language (JSON) and IAM best practices.
  IAM Access Analyzer provides more than 100 policy checks and actionable recommendations to help
  you author secure and functional policies. For more information, see [Validate policies with IAM Access Analyzer](../../../IAM/latest/UserGuide/access-analyzer-policy-validation.md "../../../IAM/latest/UserGuide/access-analyzer-policy-validation.md") in the _IAM User Guide_.
- **Require multi-factor authentication (MFA)** –
  If you have a scenario that requires IAM users or a root user in your AWS account, turn on MFA for additional security. To require
  MFA when API operations are called, add MFA conditions to your policies. For
  more information, see [Secure API access with MFA](../../../IAM/latest/UserGuide/id_credentials_mfa_configure-api-require.md "../../../IAM/latest/UserGuide/id_credentials_mfa_configure-api-require.md") in the _IAM User Guide_.

For more information about best practices in IAM, see [Security best practices in IAM](../../../IAM/latest/UserGuide/best-practices.md "../../../IAM/latest/UserGuide/best-practices.md") in the _IAM User Guide_.

## Allow the minimum permissions required to enable Audit Manager

This example shows how you might allow accounts without an administrator role to
enable AWS Audit Manager.

###### Note

What we provide here is a basic policy that grants the minimum permissions
needed to enable Audit Manager. All of the permissions in the following
policy are required. If you omit any part of this policy, you won't be able to
enable Audit Manager.

We recommend that you take time to customize your permissions so they meet
your specific needs. If you need help, contact your administrator or [AWS Support](https://aws.amazon.com/contact-us/ "https://aws.amazon.com/contact-us/").

To grant the minimum access required to enable Audit Manager, use the following
permissions.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Action": "auditmanager:*",
 "Resource": "*"
 },
 {
 "Effect": "Allow",
 "Action": "iam:CreateServiceLinkedRole",
 "Resource": "*",
 "Condition": {
 "StringLike": {
 "iam:AWSServiceName": "auditmanager.amazonaws.com"
 }
 }
 },
 {
 "Sid": "CreateEventsAccess",
 "Effect": "Allow",
 "Action": [
 "events:PutRule"
 ],
 "Resource": "*",
 "Condition": {
 "ForAllValues:StringEquals": {
 "events:source": [
 "aws.securityhub"
 ]
 }
 }
 },
 {
 "Sid": "EventsAccess",
 "Effect": "Allow",
 "Action": [
 "events:PutTargets"
 ],
 "Resource": "arn:aws:events:*:*:rule/AuditManagerSecurityHubFindingsReceiver"
 },
 {
 "Effect": "Allow",
 "Action": "kms:ListAliases",
 "Resource": "*",
 "Condition": {
 "StringLike": {
 "iam:AWSServiceName": "auditmanager.amazonaws.com"
 }
 }
 }
 ]
}`

```

You don't need to allow minimum console permissions for users that are making
calls only to the AWS CLI or the AWS API. Instead, allow access to only the actions
that match the API operation that you're trying to perform.

## Allow users full administrator access to AWS Audit Manager

The following example policies grant full administrator access to AWS Audit Manager.

- [Example 1 (Managed policy, AWSAuditManagerAdministratorAccess)](#full-administrator-access-managed-policy "#full-administrator-access-managed-policy")
- [Example 2 (Assessment report destination permissions)](#full-administrator-access-assessment-report-destination "#full-administrator-access-assessment-report-destination")
- [Example 3 (Permissions to enable evidence finder)](#full-administrator-access-enable-evidence-finder "#full-administrator-access-enable-evidence-finder")
- [Example 4 (Permissions to disable evidence finder)](#full-administrator-access-disable-evidence-finder "#full-administrator-access-disable-evidence-finder")

### Example 1 (Managed policy, `AWSAuditManagerAdministratorAccess`)

The [AWSAuditManagerAdministratorAccess](../../../aws-managed-policy/latest/reference/AWSAuditManagerAdministratorAccess.md "../../../aws-managed-policy/latest/reference/AWSAuditManagerAdministratorAccess.md") policy includes the ability to
enable and disable Audit Manager, the ability to change Audit Manager settings, and the ability to
manage all Audit Manager resources such as assessments, frameworks, controls, and
assessment reports.

### Example 2 (Assessment report destination permissions)

This policy grants you permission to access a specific S3 bucket, and to add
files to and delete files from it. This allows you to use the specified bucket
as an assessment report destination in Audit Manager.

Replace the `placeholder text` with your own
information. Include the S3 bucket that you use as your assessment report
destination and the KMS key that you use to encrypt your assessment
reports.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Action": [
 "s3:PutObject",
 "s3:GetObject",
 "s3:ListBucket",
 "s3:DeleteObject",
 "s3:GetBucketLocation",
 "s3:PutObjectAcl"
 ],
 "Resource": "arn:aws:s3:::example-s3-destination-bucket/*"
 },
 {
 "Effect": "Allow",
 "Action": [
 "kms:Decrypt",
 "kms:Encrypt",
 "kms:GenerateDataKey"
 ],
 "Resource": "arn:aws:kms:us-west-2:123456789012:key/1234abcd-12ab-34cd-56ef-1234567890ab"
 }
 ]
}`

```

### Example 3 (Permissions to enable evidence finder)

The following permission policy is required if you want to enable and use the
evidence finder feature. This policy statement allows Audit Manager to create a CloudTrail Lake
event data store and run search queries.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Sid": "ManageCloudTrailLakeQueryAccess",
 "Effect": "Allow",
 "Action": [
 "cloudtrail:StartQuery",
 "cloudtrail:DescribeQuery",
 "cloudtrail:GetQueryResults",
 "cloudtrail:CancelQuery"
 ],
 "Resource": "arn:aws:cloudtrail:*:*:eventdatastore/*"
 },
 {
 "Sid": "ManageCloudTrailLakeAccess",
 "Effect": "Allow",
 "Action": [
 "cloudtrail:CreateEventDataStore"
 ],
 "Resource": "arn:aws:cloudtrail:*:*:eventdatastore/*"
 }
 ]
}`

```

### Example 4 (Permissions to disable evidence finder)

This example policy grants permission to disable the evidence finder feature
in Audit Manager. This involves deleting the event data store that was created when you
first enabled the feature.

Before you use this policy, replace the `placeholder
 text` with your own information. You should specify the UUID of
the event data store that was created when you enabled evidence finder. You can
retrieve the ARN of the event data store from your Audit Manager settings. For more
information, see [GetSettings](../APIReference/API_GetSettings.md "../APIReference/API_GetSettings.md") in the _AWS Audit Manager API
Reference_.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Action": [
 "cloudtrail:DeleteEventDataStore",
 "cloudtrail:UpdateEventDataStore"
 ],
 "Resource": "arn:aws:cloudtrail:`us-east-1`:`111122223333`:eventdatastore/EventDataStoreId"
 }
 ]
}`

```

## Allow users management access to AWS Audit Manager

This example shows how you might allow non-administrator management access to
AWS Audit Manager.

This policy grants the ability to manage all Audit Manager resources (assessments,
frameworks, and controls), but does not grant the ability to enable or disable Audit Manager
or to modify Audit Manager settings.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Sid": "AuditManagerAccess",
 "Effect": "Allow",
 "Action": [
 "auditmanager:AssociateAssessmentReportEvidenceFolder",
 "auditmanager:BatchAssociateAssessmentReportEvidence",
 "auditmanager:BatchCreateDelegationByAssessment",
 "auditmanager:BatchDeleteDelegationByAssessment",
 "auditmanager:BatchDisassociateAssessmentReportEvidence",
 "auditmanager:BatchImportEvidenceToAssessmentControl",
 "auditmanager:CreateAssessment",
 "auditmanager:CreateAssessmentFramework",
 "auditmanager:CreateAssessmentReport",
 "auditmanager:CreateControl",
 "auditmanager:DeleteControl",
 "auditmanager:DeleteAssessment",
 "auditmanager:DeleteAssessmentFramework",
 "auditmanager:DeleteAssessmentFrameworkShare",
 "auditmanager:DeleteAssessmentReport",
 "auditmanager:DisassociateAssessmentReportEvidenceFolder",
 "auditmanager:GetAccountStatus",
 "auditmanager:GetAssessment",
 "auditmanager:GetAssessmentFramework",
 "auditmanager:GetControl",
 "auditmanager:GetServicesInScope",
 "auditmanager:GetSettings",
 "auditmanager:GetAssessmentReportUrl",
 "auditmanager:GetChangeLogs",
 "auditmanager:GetDelegations",
 "auditmanager:GetEvidence",
 "auditmanager:GetEvidenceByEvidenceFolder",
 "auditmanager:GetEvidenceFileUploadUrl",
 "auditmanager:GetEvidenceFolder",
 "auditmanager:GetEvidenceFoldersByAssessment",
 "auditmanager:GetEvidenceFoldersByAssessmentControl",
 "auditmanager:GetInsights",
 "auditmanager:GetInsightsByAssessment",
 "auditmanager:GetOrganizationAdminAccount",
 "auditmanager:ListAssessments",
 "auditmanager:ListAssessmentReports",
 "auditmanager:ListControls",
 "auditmanager:ListKeywordsForDataSource",
 "auditmanager:ListNotifications",
 "auditmanager:ListAssessmentControlInsightsByControlDomain",
 "auditmanager:ListAssessmentFrameworks",
 "auditmanager:ListAssessmentFrameworkShareRequests",
 "auditmanager:ListControlDomainInsights",
 "auditmanager:ListControlDomainInsightsByAssessment",
 "auditmanager:ListControlInsightsByControlDomain",
 "auditmanager:ListTagsForResource",
 "auditmanager:StartAssessmentFrameworkShare",
 "auditmanager:TagResource",
 "auditmanager:UntagResource",
 "auditmanager:UpdateControl",
 "auditmanager:UpdateAssessment",
 "auditmanager:UpdateAssessmentControl",
 "auditmanager:UpdateAssessmentControlSetStatus",
 "auditmanager:UpdateAssessmentFramework",
 "auditmanager:UpdateAssessmentFrameworkShare",
 "auditmanager:UpdateAssessmentStatus",
 "auditmanager:ValidateAssessmentReportIntegrity"
 ],
 "Resource": "*"
 },
 {
 "Sid": "ControlCatalogAccess",
 "Effect": "Allow",
 "Action": [
 "controlcatalog:ListCommonControls",
 "controlcatalog:ListDomains",
 "controlcatalog:ListObjectives"
 ],
 "Resource": "*"
 },
 {
 "Sid": "OrganizationsAccess",
 "Effect": "Allow",
 "Action": [
 "organizations:ListAccountsForParent",
 "organizations:ListAccounts",
 "organizations:DescribeOrganization",
 "organizations:DescribeOrganizationalUnit",
 "organizations:DescribeAccount",
 "organizations:ListParents",
 "organizations:ListChildren"
 ],
 "Resource": "*"
 },
 {
 "Sid": "IAMAccess",
 "Effect": "Allow",
 "Action": [
 "iam:GetUser",
 "iam:ListUsers",
 "iam:ListRoles"
 ],
 "Resource": "*"
 },
 {
 "Sid": "S3Access",
 "Effect": "Allow",
 "Action": [
 "s3:ListAllMyBuckets"
 ],
 "Resource": "*"
 },
 {
 "Sid": "KmsAccess",
 "Effect": "Allow",
 "Action": [
 "kms:DescribeKey",
 "kms:ListKeys",
 "kms:ListAliases"
 ],
 "Resource": "*"
 },
 {
 "Sid": "SNSAccess",
 "Effect": "Allow",
 "Action": [
 "sns:ListTopics"
 ],
 "Resource": "*"
 },
 {
 "Sid": "TagAccess",
 "Effect": "Allow",
 "Action": [
 "tag:GetResources"
 ],
 "Resource": "*"
 }
 ]
}`

```

## Allow users read-only access to AWS Audit Manager

This policy grants read-only access to AWS Audit Manager resources such as assessments,
frameworks, and controls.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Sid": "AuditManagerAccess",
 "Effect": "Allow",
 "Action": [
 "auditmanager:Get*",
 "auditmanager:List*"
 ],
 "Resource": "*"
 }
 ]
}`

```

## Allow users to view their own permissions

This example shows how you might create a policy that allows IAM users to view the inline and managed policies that are attached to their user
identity. This policy includes permissions to complete this action on the console or programmatically using the AWS CLI or AWS API.

```
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Sid": "ViewOwnUserInfo",
            "Effect": "Allow",
            "Action": [
                "iam:GetUserPolicy",
                "iam:ListGroupsForUser",
                "iam:ListAttachedUserPolicies",
                "iam:ListUserPolicies",
                "iam:GetUser"
            ],
            "Resource": ["arn:aws:iam::*:user/${aws:username}"]
        },
        {
            "Sid": "NavigateInConsole",
            "Effect": "Allow",
            "Action": [
                "iam:GetGroupPolicy",
                "iam:GetPolicyVersion",
                "iam:GetPolicy",
                "iam:ListAttachedGroupPolicies",
                "iam:ListGroupPolicies",
                "iam:ListPolicyVersions",
                "iam:ListPolicies",
                "iam:ListUsers"
            ],
            "Resource": "*"
        }
    ]
}
```

## Allow AWS Audit Manager to send notifications to Amazon SNS topics

The policies in this example grant Audit Manager permissions to send notifications to an
existing Amazon SNS topic.

- [Example 1](security_iam_id-based-policy-examples.md#sns-topic-permissions "security_iam_id-based-policy-examples.md#sns-topic-permissions") – If you want to receive notifications from
  Audit Manager, use this example to add permissions to your SNS topic access policy.
- [Example 2](security_iam_id-based-policy-examples.md#sns-key-permissions "security_iam_id-based-policy-examples.md#sns-key-permissions") – If your SNS topic uses AWS Key Management Service (AWS KMS) for
  server-side encryption (SSE), use this example to add permissions to the
  KMS key access policy.

In the following policies, the principal who gets the permissions is the Audit Manager
service principal, which is `auditmanager.amazonaws.com`. When the
principal in a policy statement is an [AWS service principal](../../../IAM/latest/UserGuide/reference_policies_elements_principal.md#principal-services "../../../IAM/latest/UserGuide/reference_policies_elements_principal.md#principal-services"), we strongly recommend that
you use the [`aws:SourceArn`](../../../IAM/latest/UserGuide/reference_policies_condition-keys.md#condition-keys-sourcearn "../../../IAM/latest/UserGuide/reference_policies_condition-keys.md#condition-keys-sourcearn") or [`aws:SourceAccount`](../../../IAM/latest/UserGuide/reference_policies_condition-keys.md#condition-keys-sourceaccount "../../../IAM/latest/UserGuide/reference_policies_condition-keys.md#condition-keys-sourceaccount") global condition
keys in the policy. You can use these global condition context keys to help prevent
the [confused deputy scenario](cross-service-confused-deputy-prevention.md "cross-service-confused-deputy-prevention.md").

### Example 1 (Permissions for the SNS topic)

This policy statement allows Audit Manager to publish events to the specified SNS
topic. Any request to publish to the specified SNS topic must satisfy the policy
conditions.

Before using this policy, replace the `placeholder
 text` with your own information. Take note of the
following:

- If you use the `aws:SourceArn` condition key in this
  policy, the value must be the ARN of the Audit Manager resource that the
  notification comes from. In the example below,
  `aws:SourceArn` uses a wildcard (`*`) for the
  resource ID. This allows all requests that come from Audit Manager on all Audit Manager
  resources. With the `aws:SourceArn` global condition key, you
  can use either the `StringLike` or the `ArnLike`
  condition operator. As a best practice, we recommend that you use
  `ArnLike`.
- If you use the [`aws:SourceAccount`](../../../IAM/latest/UserGuide/reference_policies_condition-keys.md#condition-keys-sourceaccount "../../../IAM/latest/UserGuide/reference_policies_condition-keys.md#condition-keys-sourceaccount")
  condition key, you can use either the `StringEquals` or the
  `StringLike` condition operator. As a best practice, we
  recommend that you use `StringEquals` to implement least
  privilege.
- If you use both `aws:SourceAccount` and
  `aws:SourceArn`, the account values must show the same
  account ID.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": {
 "Sid": "AllowAuditManagerToUseSNSTopic",
 "Effect": "Allow",
 "Principal": {
 "Service": "auditmanager.amazonaws.com"
 },
 "Action": "SNS:Publish",
 "Resource": "arn:aws:sns:`us-east-1`:`111122223333`:`topicName`",
 "Condition": {
 "StringEquals": {
 "aws:SourceAccount": "`111122223333`"
 },
 "ArnLike": {
 "aws:SourceArn": "arn:aws:auditmanager:`us-east-1`:`111122223333`:`*`"
 }
 }
 }
}`

```

The following alternative example uses just the `aws:SourceArn`
condition key, with the `StringLike` condition operator:

```
      "Condition": {
        "StringLike": {
          "aws:SourceArn": "arn:aws:auditmanager:`region`:`accountID`:*"
        }
      }
```

The following alternative example uses just the `aws:SourceAccount`
condition key, with the `StringLike` condition operator:

```
   "Condition": {
     "StringLike": {
       "aws:SourceAccount": "`accountID`"
      }
    }
```

### Example 2 (Permissions for the KMS key that's attached to the SNS topic)

This policy statement allows Audit Manager to use the KMS key to [generate the data key](../../../kms/latest/APIReference/API_GenerateDataKey.md "../../../kms/latest/APIReference/API_GenerateDataKey.md") that it uses to encrypt an SNS topic. Any
request to use the KMS key for the specified operation must satisfy the policy
conditions.

Before using this policy, replace the `placeholder
 text` with your own information. Take note of the
following:

- If you use the `aws:SourceArn` condition key in this
  policy, the value must be the ARN of the resource that’s being
  encrypted. For example, in this case, it's the SNS topic in your
  account. Set the value to the ARN or an ARN pattern with wildcard
  characters (`*`). You can use either the
  `StringLike` or the `ArnLike` condition
  operator with the `aws:SourceArn` condition key. As a best
  practice, we recommend that you use `ArnLike`.
- If you use the `aws:SourceAccount` condition key, you can
  use either the `StringEquals` or the `StringLike`
  condition operator. As a best practice, we recommend that you use
  `StringEquals` to implement least privilege. You can use
  `aws:SourceAccount` if you don't know the ARN of the SNS
  topic.
- If you use both `aws:SourceAccount` and
  `aws:SourceArn`, the account values must show the same
  account ID.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": {
 "Sid": "AllowAuditManagerToUseKMSKey",
 "Effect": "Allow",
 "Principal": {
 "Service": "auditmanager.amazonaws.com"
 },
 "Action": [
 "kms:Decrypt",
 "kms:GenerateDataKey"
 ],
 "Resource": "arn:aws:kms:`us-east-1`:`123456789012`:key/*",
 "Condition": {
 "StringEquals": {
 "aws:SourceAccount": "`123456789012`"
 },
 "ArnLike": {
 "aws:SourceArn": "arn:aws:sns:`us-east-1`:`123456789012`:`topicName`"
 }
 }
 }
}`

```

The following alternative example uses just the `aws:SourceArn`
condition key, with the `StringLike` condition operator:

```
      "Condition": {
        "StringLike": {
          "aws:SourceArn": "arn:aws:sns:`region`:`accountID`:topicName"
        }
      }
```

The following alternative example uses just the `aws:SourceAccount`
condition key, with the `StringLike` condition operator:

```
   "Condition": {
     "StringLike": {
       "aws:SourceAccount": "`accountID`"
      }
    }
```

## Allow users to run search queries in evidence finder

The following policy grants permissions to perform queries on a CloudTrail Lake event
data store. This permission policy is required if you want to use the evidence
finder feature.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Sid": "ManageCloudTrailLakeQueryAccess",
 "Effect": "Allow",
 "Action": [
 "cloudtrail:StartQuery",
 "cloudtrail:DescribeQuery",
 "cloudtrail:GetQueryResults",
 "cloudtrail:CancelQuery"
 ],
 "Resource": "*"
 }
 ]
}`

```
