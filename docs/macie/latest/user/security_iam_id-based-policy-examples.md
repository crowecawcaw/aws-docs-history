# Identity-based policy examples for Macie

By default, users and roles don't have permission to create or modify Macie
resources. To grant users permission to perform actions on the
resources that they need, an IAM administrator can create IAM policies.

To learn how to create an IAM identity-based policy by using these example JSON policy
documents, see [Create IAM policies (console)](../../../IAM/latest/UserGuide/access_policies_create-console.md "../../../IAM/latest/UserGuide/access_policies_create-console.md") in the
_IAM User Guide_.

For details about actions and resource types defined by Macie, including the format of the ARNs for each of the resource types, see [Actions, resources, and condition keys for Amazon Macie](../../../service-authorization/latest/reference/list_amazonmacie.md "../../../service-authorization/latest/reference/list_amazonmacie.md") in the _Service Authorization Reference_.

When you create a policy, be sure to resolve security warnings, errors, general warnings,
and suggestions from AWS Identity and Access Management Access Analyzer (IAM Access Analyzer) before you save the policy.
IAM Access Analyzer runs policy checks to validate a policy against IAM [policy grammar](../../../IAM/latest/UserGuide/reference_policies_grammar.md "../../../IAM/latest/UserGuide/reference_policies_grammar.md") and [best practices](../../../IAM/latest/UserGuide/best-practices.md "../../../IAM/latest/UserGuide/best-practices.md"). These checks generate
findings and provide actionable recommendations to help you author policies that are
functional and conform to security best practices. To learn about validating policies by using
IAM Access Analyzer, see [IAM Access Analyzer policy validation](../../../IAM/latest/UserGuide/access-analyzer-policy-validation.md "../../../IAM/latest/UserGuide/access-analyzer-policy-validation.md") in the _IAM User Guide_. To
review a list of the warnings, errors, and suggestions that IAM Access Analyzer can return, see
[IAM Access Analyzer
policy check reference](../../../IAM/latest/UserGuide/access-analyzer-reference-policy-checks.md "../../../IAM/latest/UserGuide/access-analyzer-reference-policy-checks.md") in the _IAM User Guide_.

###### Topics

- [Policy best
  practices](#security_iam_service-with-iam-policy-best-practices "#security_iam_service-with-iam-policy-best-practices")
- [Using the Amazon Macie
  console](#security_iam_id-based-policy-examples-console "#security_iam_id-based-policy-examples-console")
- [Example: Allow
  users to review their own permissions](#security_iam_id-based-policy-examples-view-own-permissions "#security_iam_id-based-policy-examples-view-own-permissions")
- [Example: Allow users to create
  sensitive data discovery jobs](#security_iam_id-based-policy-examples-create-job "#security_iam_id-based-policy-examples-create-job")
- [Example: Allow users to manage
  a sensitive data discovery job](#security_iam_id-based-policy-examples-access-job "#security_iam_id-based-policy-examples-access-job")
- [Example: Allow users to
  review findings](#security_iam_id-based-policy-examples-review-findings "#security_iam_id-based-policy-examples-review-findings")
- [Example: Allow users to
  review custom data identifiers based on tags](#security_iam_id-based-policy-examples-review-cdis-tags "#security_iam_id-based-policy-examples-review-cdis-tags")

## Policy best

practices

Identity-based policies determine whether someone can create, access, or delete Macie resources in your
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
  if they are used through a specific AWS service, such as AWS CloudFormation. For more information, see
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

## Using the Amazon Macie

console

To access the Amazon Macie console, you must have a minimum set of permissions.
These permissions must allow you to list and view details about the Macie resources
in your AWS account. If you create an identity-based policy that is more restrictive
than the minimum required permissions, the console won't function as intended for
entities (users or roles) with that policy.

You don't need to allow minimum console permissions for users that are making calls
only to the AWS CLI or the AWS API. Instead, allow access to only the actions that match
the API operation that they're trying to perform.

To ensure that users and roles can use the Amazon Macie console, create IAM policies
that provide them with console access. For more information, see [Policies and
permissions in IAM](../../../IAM/latest/UserGuide/access_policies.md "../../../IAM/latest/UserGuide/access_policies.md") in the _IAM User Guide_.

If you create a policy that allows users or roles to use the Amazon Macie console, ensure
that the policy allows the `macie2:GetMacieSession` action.
Otherwise, those users or roles won't be able to access any Macie resources or data on
the console.

Also ensure that the policy allows the appropriate `macie2:List`
actions for resources that those users or roles need to access on the console.
Otherwise, they won't be able to navigate to or display details about those resources on
the console. For example, to review the details of a sensitive data discovery job by
using the console, a user must be allowed to perform the
`macie2:DescribeClassificationJob` action for the job _and_ the `macie2:ListClassificationJobs` action.
If a user isn't allowed to perform the
`macie2:ListClassificationJobs` action, the user won't be able
to display a list of jobs on the **Jobs** page of the console, and
therefore won't be able to choose the job to display its details. For the details to
include information about a custom data identifier that the job uses, the user must also
be allowed to perform the `macie2:BatchGetCustomDataIdentifiers`
action for the custom data identifier.

## Example: Allow

users to review their own permissions

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

## Example: Allow users to create

sensitive data discovery jobs

This example shows how you might create a policy that allows a user to create sensitive data
discovery jobs.

In the example, the first statement grants `macie2:CreateClassificationJob`
permissions to the user. These permissions allow the user to create jobs. The statement
also grants `macie2:DescribeClassificationJob` permissions. These permissions
allow the user to access the details of existing jobs. Although these permissions aren't
required to create jobs, access to these details can help the user create jobs that have
unique configuration settings.

The second statement in the example allows the user to create, configure, and review jobs by
using the Amazon Macie console. The `macie2:ListClassificationJobs` permissions
allow the user to display existing jobs on the **Jobs** page of the
console. All other permissions in the statement allow the user to configure and create a
job by using the **Create job** pages on the console.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Sid": "CreateAndReviewJobs",
 "Effect": "Allow",
 "Action": [
 "macie2:CreateClassificationJob",
 "macie2:DescribeClassificationJob"
 ],
 "Resource": "arn:aws:macie2:*:*:classification-job/*"
 },
 {
 "Sid": "CreateAndReviewJobsOnConsole",
 "Effect": "Allow",
 "Action": [
 "macie2:ListClassificationJobs",
 "macie2:ListAllowLists",
 "macie2:ListCustomDataIdentifiers",
 "macie2:ListManagedDataIdentifiers",
 "macie2:SearchResources",
 "macie2:DescribeBuckets"
 ],
 "Resource": "*"
 }
 ]
}`

```

## Example: Allow users to manage

a sensitive data discovery job

This example shows how you might create a policy that allows a user to access the details of
a particular sensitive data discovery job, the job whose ID is
`3ce05dbb7ec5505def334104bexample`. The example also allows the user to
change the status of the job as necessary.

The first statement in the example grants
`macie2:DescribeClassificationJob` and
`macie2:UpdateClassificationJob` permissions to the user. These
permissions allow the user to retrieve the job's details and change the job's status,
respectively. The second statement grants
`macie2:ListClassificationJobs` permissions to the user, which
allows the user to access the job by using the **Jobs** page on the
Amazon Macie console.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Sid": "ManageOneJob",
 "Effect": "Allow",
 "Action": [
 "macie2:DescribeClassificationJob",
 "macie2:UpdateClassificationJob"
 ],
 "Resource": "arn:aws:macie2:*:*:classification-job/3ce05dbb7ec5505def334104bexample"
 },
 {
 "Sid": "ListJobsOnConsole",
 "Effect": "Allow",
 "Action": "macie2:ListClassificationJobs",
 "Resource": "*"
 }
 ]
}`

```

You might also allow the user to access logging data (_log
events_) that Macie publishes to Amazon CloudWatch Logs for the job. To do this, you can
add statements that grant permissions to perform CloudWatch Logs (`logs`) actions on the
log group and stream for the job. For example:

```
{
    "Sid": "AccessLogGroupForMacieJobs",
    "Effect": "Allow",
    "Action": [
        "logs:DescribeLogGroups",
        "logs:DescribeLogStreams"
    ],
    "Resource": "arn:aws:logs:*:*:log-group:aws/macie/classificationjobs"
},
{
    "Sid": "AccessLogEventsForOneMacieJob",
    "Effect": "Allow",
    "Action": "logs:GetLogEvents",
    "Resource": [
        "arn:aws:logs:*:*:log-group:aws/macie/classificationjobs/*",
        "arn:aws:logs:*:*:log-group:aws/macie/classificationjobs:log-stream:3ce05dbb7ec5505def334104bexample"
    ]
}
```

For information about managing access to CloudWatch Logs, see [Overview of
managing access permissions to your CloudWatch Logs resources](../../../AmazonCloudWatch/latest/logs/iam-access-control-overview-cwl.md "../../../AmazonCloudWatch/latest/logs/iam-access-control-overview-cwl.md") in the _Amazon CloudWatch Logs User Guide_.

## Example: Allow users to

review findings

This example shows how you might create a policy that allows a user to access findings
data.

In this example, the `macie2:GetFindings` and
`macie2:GetFindingStatistics` permissions allow the user to
retrieve the data by using the Amazon Macie API or the Amazon Macie console. The
`macie2:ListFindings` permissions allow the user to retrieve and
review the data by using the **Summary** dashboard and the
**Findings** pages on the Amazon Macie console.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Sid": "ReviewFindings",
 "Effect": "Allow",
 "Action": [
 "macie2:GetFindings",
 "macie2:GetFindingStatistics",
 "macie2:ListFindings"
 ],
 "Resource": "*"
 }
 ]
}`

```

You might also allow the user to create and manage filter rules and suppression rules for
findings. To do this, you might include a statement that grants the following permissions:
`macie2:CreateFindingsFilter`,
`macie2:GetFindingsFilter`,
`macie2:UpdateFindingsFilter`, and
`macie2:DeleteFindingsFilter`. To allow the user to manage the rules
by using the Amazon Macie console, also include
`macie2:ListFindingsFilters` permissions in the policy. For
example:

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Sid": "ReviewFindings",
 "Effect": "Allow",
 "Action": [
 "macie2:GetFindings",
 "macie2:GetFindingStatistics",
 "macie2:ListFindings"
 ],
 "Resource": "*"
 },
 {
 "Sid": "ManageRules",
 "Effect": "Allow",
 "Action": [
 "macie2:GetFindingsFilter",
 "macie2:UpdateFindingsFilter",
 "macie2:CreateFindingsFilter",
 "macie2:DeleteFindingsFilter"
 ],
 "Resource": "arn:aws:macie2:*:*:findings-filter/*"
 },
 {
 "Sid": "ListRulesOnConsole",
 "Effect": "Allow",
 "Action": "macie2:ListFindingsFilters",
 "Resource": "*"
 }
 ]
}`

```

## Example: Allow users to

review custom data identifiers based on tags

In identity-based policies, you can use conditions to control access to Amazon Macie resources
based on tags. This example shows how you might create a policy that allows a user to
review custom data identifiers by using the Amazon Macie console or the Amazon Macie API.
However, permission is granted only if the value for the `Owner` tag is the
user's username.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Sid": "ReviewCustomDataIdentifiersIfOwner",
 "Effect": "Allow",
 "Action": "macie2:GetCustomDataIdentifier",
 "Resource": "arn:aws:macie2:*:*:custom-data-identifier/*",
 "Condition": {
 "StringEquals": {"aws:ResourceTag/Owner": "${aws:username}"}
 }
 },
 {
 "Sid": "ListCustomDataIdentifiersOnConsoleIfOwner",
 "Effect": "Allow",
 "Action": "macie2:ListCustomDataIdentifiers",
 "Resource": "*",
 "Condition": {
 "StringEquals": {"aws:ResourceTag/Owner": "${aws:username}"}
 }
 }
 ]
}`

```

In this example, if a user who has the username `richard-roe` attempts to review
the details of a custom data identifier, the custom data identifier must be tagged
`Owner=richard-roe` or `owner=richard-roe`. Otherwise, the
user is denied access. The condition tag key `Owner` matches both
`Owner` and `owner` because condition key names aren't case
sensitive. For more information, see [IAM JSON policy
elements: Condition](../../../IAM/latest/UserGuide/reference_policies_elements_condition.md "../../../IAM/latest/UserGuide/reference_policies_elements_condition.md") in the _IAM User Guide_.
