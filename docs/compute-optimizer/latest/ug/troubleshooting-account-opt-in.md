# Troubleshooting in Compute Optimizer

This section covers troubleshooting why fails or errors might occur while using Compute Optimizer. The solutions provided in this
section show how you can mitigate these problems.

###### Topics

- [Failed to create service-linked role](#slr-create-failed "#slr-create-failed")
- [Failed to enable trusted access](#slr-create-failed "#slr-create-failed")
- [Failed to get or update enhanced
  infrastructure metrics recommendation preferences](#accounts-eim-missing-permissions "#accounts-eim-missing-permissions")
- [Troubleshooting failed export jobs](#troubleshooting-exports "#troubleshooting-exports")

## Failed to create service-linked role

###### Description

Accounts show a **Failed** opt-in status, and a description of
**Failed to create service-linked role**.

###### Cause

Compute Optimizer uses AWS Identity and Access Management (IAM) service-linked roles. These roles include all of the
permissions that the service requires to call other AWS services on your behalf.
You must configure permissions to allow an IAM entity (a user, group, or role) to
create a service-linked role for Compute Optimizer. The user who tried to opt in to Compute Optimizer might
not have the permissions required to have the service-linked role created.

###### Solution

Add the required permissions to the user who performs the Compute Optimizer opt-in. For more
information, see [Service-linked role permissions](using-service-linked-roles.md#service-linked-role-permissions "using-service-linked-roles.md#service-linked-role-permissions").

## Failed to enable trusted access

###### Description

Accounts show a **Failed** opt-in status, and a description of
**Failed to enable trusted access**.

###### Cause

You can use _trusted access_ to enable Compute Optimizer to perform tasks in
your organization and its accounts on your behalf. For more information about
AWS Organizations trusted access, see [Using AWS Organizations with other AWS services](../../../organizations/latest/userguide/orgs_integrate_services.md "../../../organizations/latest/userguide/orgs_integrate_services.md") in the _AWS Organizations User
Guide_.When
you opt in using your organization's management account and include all member
accounts within the organization, trusted access for Compute Optimizer is automatically enabled
in your organization account. The user who tried to opt in to
Compute Optimizer might not have the permissions required to have trusted access enabled.

###### Solution

Add the required permissions to the user who perform the Compute Optimizer opt-in. For more
information, see [Permissions required to enable trusted access](../../../organizations/latest/userguide/orgs_integrate_services.md#orgs_trusted_access_perms "../../../organizations/latest/userguide/orgs_integrate_services.md#orgs_trusted_access_perms") in the _AWS Organizations
User Guide_. After you add the required permissions, opt in to Compute Optimizer
again using your organization's management account and include all member accounts
within the organization. For more information, see [Opting in to AWS Compute Optimizer](account-opt-in.md "account-opt-in.md").

## Failed to get or update enhanced

infrastructure metrics recommendation preferences

###### Description

A banner is displayed that indicates that the Compute Optimizer console could not get or update enhanced
infrastructure metrics recommendation preferences.

###### Cause

You might not have the permissions required to view or update recommendation
preferences.

###### Solution

Add the required permissions to the user who will view or edit recommendation
preferences. For more information, see [Policies to grant access
to manage Compute Optimizer recommendation preferences](security-iam.md#enhanced-infrastructure-metrics-permissions "security-iam.md#enhanced-infrastructure-metrics-permissions").

## Troubleshooting failed export jobs

When you try to export your resource recommendations, you might experience one of the following
error messages or issues. Use the information provided to try to resolve the error before trying to
export your recommendations again.

###### You don't have permissions to the Amazon S3 bucket specified. Confirm the permissions of

your S3 bucket and try again.

Confirm that you have configured the required permissions on your Amazon S3 bucket. For more
information, see [Specifying an existing S3 bucket for your recommendations export](create-s3-bucket-policy-for-compute-optimizer.md "create-s3-bucket-policy-for-compute-optimizer.md").

###### The Amazon S3 bucket specified is public. Only private S3 buckets are supported.

Your Amazon S3 bucket must be set to block public access. For more information, see [Blocking public access to your
Amazon S3 storage](../../../AmazonS3/latest/userguide/access-control-block-public-access.md "../../../AmazonS3/latest/userguide/access-control-block-public-access.md") in the _Amazon Simple Storage Service User Guide_.

###### You created a scripted or automatic export job but there is recommendation data missing

from your Amazon S3 bucket.

Call the `DescribeRecommendationExportJobs` API to verify the final status of the export job.
If the export job failed, try to call the `Export`Resource`Recommendations`
API again. For more information, see [DescribeRecommendationExportJobs](../APIReference/API_DescribeRecommendationExportJobs.md "../APIReference/API_DescribeRecommendationExportJobs.md") in the _AWS Compute Optimizer API Reference_.
