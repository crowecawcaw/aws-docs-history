# Identity-based policy

examples for Amazon Personalize

By default, users and roles don't have permission to create or modify Amazon Personalize
resources. To grant users permission to perform actions on the
resources that they need, an IAM administrator can create IAM policies.

To learn how to create an IAM identity-based policy by using these example JSON policy
documents, see [Create IAM policies (console)](../../../IAM/latest/UserGuide/access_policies_create-console.md "../../../IAM/latest/UserGuide/access_policies_create-console.md") in the
_IAM User Guide_.

For details about actions and resource types defined by Amazon Personalize, including the format of the ARNs for each of the resource types, see [Actions, resources, and condition keys for Amazon Personalize](../../../service-authorization/latest/reference/list_amazonpersonalize.md "../../../service-authorization/latest/reference/list_amazonpersonalize.md") in the _Service Authorization Reference_.

###### Topics

- [Policy best
  practices](#security_iam_service-with-iam-policy-best-practices "#security_iam_service-with-iam-policy-best-practices")
- [AWS managed policies](#using-managed-policies "#using-managed-policies")
- [Using the Amazon Personalize
  console](#security_iam_id-based-policy-examples-console "#security_iam_id-based-policy-examples-console")
- [Allow users
  to view their own permissions](#security_iam_id-based-policy-examples-view-own-permissions "#security_iam_id-based-policy-examples-view-own-permissions")
- [Allowing full access to
  Amazon Personalize resources](#security_iam_id-based-policy-examples-full-access "#security_iam_id-based-policy-examples-full-access")
- [Allowing read-only
  access to Amazon Personalize resources](#security_iam_id-based-policy-examples-read-only "#security_iam_id-based-policy-examples-read-only")

## Policy best

practices

Identity-based policies determine whether someone can create, access, or delete Amazon Personalize resources in your
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

## AWS managed policies

AWS managed polices are policies that are created and managed by AWS. The following are examples of AWS managed policies you might use
when working with Amazon Personalize.

**AmazonPersonalizeFullAccess Policy**

You can use the AWS managed `AmazonPersonalizeFullAccess` policy to give users the following permissions:

- Access all Amazon Personalize resources
- Publish and list metrics on Amazon CloudWatch
- List, read, write, and delete all objects in an Amazon S3 bucket that contains
  `Personalize` or `personalize` in the bucket name
- Pass a role to Amazon Personalize

`AmazonPersonalizeFullAccess` provides more permissions than are necessary. We recommend creating a new IAM policy that only grants the necessary permissions (see
[Giving Amazon Personalize permission to access your resources](set-up-required-permissions.md "set-up-required-permissions.md")).

**CloudWatchFullAccess**

To give your users permission to monitor Amazon Personalize with CloudWatch, attach the `CloudWatchFullAccess` policy to your role. For more information, see [Monitoring Amazon Personalize with Amazon CloudWatch](personalize-monitoring.md "personalize-monitoring.md").

The `CloudWatchFullAccess` policy is optional and grants permission for the following
actions:

- Publish and list Amazon Personalize metrics in CloudWatch
- View metrics and metric statistics.
- Set metric based alarms.

## Using the Amazon Personalize

console

To access the Amazon Personalize console, you must have a minimum set of permissions.
These permissions must allow you to list and view details about the Amazon Personalize resources
in your AWS account. If you create an identity-based policy that is more restrictive
than the minimum required permissions, the console won't function as intended for
entities (users or roles) with that policy.

You don't need to allow minimum console permissions for users that are making calls
only to the AWS CLI or the AWS API. Instead, allow access to only the actions that match
the API operation that they're trying to perform.

## Allow users

to view their own permissions

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

## Allowing full access to

Amazon Personalize resources

The following example gives an IAM user in your AWS account full access to all
Amazon Personalize resources and actions.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Action": [
 "personalize:*"
 ],
 "Resource": "*"
 }
 ]
}`

```

## Allowing read-only

access to Amazon Personalize resources

In this example, you grant an IAM user in your AWS account read-only access to
your Amazon Personalize resources, including Amazon Personalize datasets, dataset groups, solutions,
and campaigns.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Action": [
 "personalize:DescribeAlgorithm",
 "personalize:DescribeBatchInferenceJob",
 "personalize:DescribeBatchSegmentJob",
 "personalize:DescribeCampaign",
 "personalize:DescribeDataset",
 "personalize:DescribeDatasetExportJob",
 "personalize:DescribeDatasetGroup",
 "personalize:DescribeDatasetImportJob",
 "personalize:DescribeEventTracker",
 "personalize:DescribeFeatureTransformation",
 "personalize:DescribeFilter",
 "personalize:DescribeRecipe",
 "personalize:DescribeRecommender",
 "personalize:DescribeSchema",
 "personalize:DescribeSolution",
 "personalize:DescribeSolutionVersion",
 "personalize:GetSolutionMetrics",
 "personalize:ListBatchInferenceJobs",
 "personalize:ListBatchSegmentJobs",
 "personalize:ListCampaigns",
 "personalize:ListDatasetExportJobs",
 "personalize:ListDatasetGroups",
 "personalize:ListDatasetImportJobs",
 "personalize:ListDatasets",
 "personalize:ListEventTrackers",
 "personalize:ListFilters",
 "personalize:ListRecipes",
 "personalize:ListRecommenders",
 "personalize:ListSchemas",
 "personalize:ListSolutions",
 "personalize:ListSolutionVersions"
 ],
 "Resource": "*"
 }
 ]
}`

```
