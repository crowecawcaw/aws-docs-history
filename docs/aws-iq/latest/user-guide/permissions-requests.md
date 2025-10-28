End of support notice: On May 28, 2026, AWS
will end support for AWS IQ. After May 28, 2026, you will
no longer be able to access the AWS IQ console or AWS IQ resources.
For more information, see [AWS IQ end of support](../experts-user-guide/aws-iq-end-of-support.md "../experts-user-guide/aws-iq-end-of-support.md") in the _AWS IQ User Guide for Experts_.

# Permissions requests in AWS IQ

In AWS IQ, an expert might request a permissions policy to access your AWS account and
complete the necessary work. The level of access required depends on the scope of the project.
AWS IQ simplifies the process of granting access to experts, which allows experts to implement
projects in your account.

AWS IQ creates an IAM role for the expert to use for the duration of the proposal. You
can view AWS CloudTrail logs of the expert's activity in your account and can revoke access at any time.
Access is automatically revoked at the completion of the proposal, when the final payment is
made.

An expert might also include details about why they're requesting a level of permissions. You
can review the information in the permission request. To get started, choose the permission
request in the AWS IQ console and then choose **Accept** or
**Decline**.

###### Tip

It is an AWS security best practice to grant the least amount of privileges necessary to
perform a task. If you think the expert is requesting an inappropriate level of access, you
should decline the request. Learn more about [Granting least privilege](../../../IAM/latest/UserGuide/best-practices.md#grant-least-privilege "../../../IAM/latest/UserGuide/best-practices.md#grant-least-privilege") in the _AWS Identity and Access Management User Guide_.

## Permission levels in AWS IQ

The following AWS Identity and Access Management permission levels are available for an expert to request in AWS
IQ:

**AdministratorAccess**

Provides full access to AWS services and resources. For more information, see [Viewing CloudTrail logs in AWS IQ](#viewing-cloudtrail-logs "#viewing-cloudtrail-logs") and [AWS Managed Policies for Job Functions](../../../IAM/latest/UserGuide/access_policies_job-functions.md#jf_administrator "../../../IAM/latest/UserGuide/access_policies_job-functions.md#jf_administrator") in the _AWS Identity and Access Management (IAM) User
Guide_.

**Billing**

Grants permission for billing and cost management. This includes viewing account usage
and viewing and modifying budgets and payment methods. For more information, see [AWS Managed Policies for Job Functions](../../../IAM/latest/UserGuide/access_policies_job-functions.md#jf_accounts-payable "../../../IAM/latest/UserGuide/access_policies_job-functions.md#jf_accounts-payable") in the _IAM User
Guide_.

**DatabaseAdministrator**

Grants permission to AWS services and actions required to set up and configure AWS
database services. For more information, see [AWS Managed Policies for Job Functions](../../../IAM/latest/UserGuide/access_policies_job-functions.md#jf_database-administrator "../../../IAM/latest/UserGuide/access_policies_job-functions.md#jf_database-administrator") in the _IAM User
Guide_.

**NetworkAdministrator**

Grants permission to AWS services and actions required to set up and configure AWS
network resources. For more information, see [AWS Managed Policies for Job Functions](../../../IAM/latest/UserGuide/access_policies_job-functions.md#jf_network-administrator "../../../IAM/latest/UserGuide/access_policies_job-functions.md#jf_network-administrator") in the _IAM User
Guide_.

**PowerUserAccess**

Grants permission to AWS services and resources but doesn't allow management of users
and groups. For more information, see [AWS Managed Policies for Job Functions](../../../IAM/latest/UserGuide/access_policies_job-functions.md#jf_developer-power-user "../../../IAM/latest/UserGuide/access_policies_job-functions.md#jf_developer-power-user") in the _IAM User
Guide_.

**SecurityAudit**

Grants permission to read security configuration metadata. This is useful for software
that audits the configuration of an AWS account. For more information, see [AWS Managed Policies for Job Functions](../../../IAM/latest/UserGuide/access_policies_job-functions.md#jf_security-auditor "../../../IAM/latest/UserGuide/access_policies_job-functions.md#jf_security-auditor") in the _IAM User
Guide_.

**SupportUser**

Grants permission to troubleshoot and resolve issues in an AWS account. This policy
also enables the user to contact Support to create and manage cases. For more information, see
[AWS Managed Policies for Job Functions](../../../IAM/latest/UserGuide/access_policies_job-functions.md#jf_support-user "../../../IAM/latest/UserGuide/access_policies_job-functions.md#jf_support-user") in the _IAM User
Guide_.

**SystemAdministrator**

Grants permission for resources that are required for application and development
operations. For more information, see [AWS Managed Policies for Job Functions](../../../IAM/latest/UserGuide/access_policies_job-functions.md#jf_system-administrator "../../../IAM/latest/UserGuide/access_policies_job-functions.md#jf_system-administrator") in the _IAM User
Guide_.

**ViewOnlyAccess**

Grants permission to view resources and basic metadata across all AWS services. For
more information, see [AWS Managed Policies for Job Functions](../../../IAM/latest/UserGuide/access_policies_job-functions.md#jf_view-only-user "../../../IAM/latest/UserGuide/access_policies_job-functions.md#jf_view-only-user") in the _IAM User
Guide_.

###### Tip

If you prefer, you can grant access to your expert independent of AWS IQ. This access
isn't revoked automatically.

## Viewing CloudTrail logs in AWS IQ

You can view AWS CloudTrail logs of activities taken by using the
**AdministratorAccess** IAM role in your AWS account.

###### To view CloudTrail logs in AWS IQ

1. Sign in to the [AWS IQ console](https://iq.aws.amazon.com "https://iq.aws.amazon.com").
2. From the right menu, locate your **request** and the associated
   **proposal** card.
3. Choose the **permission request** and then select the
   **Activity** tab.

###### Note

The logs may experience a delay.

## Revoking permission in AWS IQ

If you grant an expert permission to access your AWS environment, permission is
automatically revoked when the proposal is complete. You can also revoke permissions manually
using the following process.

###### To revoke permissions manually

1. From the **Permission** page in the AWS IQ console, select your
   **permission request**.
2. Choose **Revoke**.
