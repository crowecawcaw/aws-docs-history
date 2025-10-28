End of support notice: On May 28, 2026, AWS
will end support for AWS IQ. After May 28, 2026, you will
no longer be able to access the AWS IQ console or AWS IQ resources.
For more information, see [AWS IQ end of support](aws-iq-end-of-support.md "aws-iq-end-of-support.md").

# Working with permissions requests in AWS

IQ

After you and a customer agree on a proposal, request access to the customer's AWS account,
if necessary to complete the work. This topic explains how to create such a request.

The following permissions policies are available in AWS IQ. You can include details about
why you're requesting that level of permissions.

###### Tip

An AWS security best practice is to grant the least amount of privileges necessary to
perform a task.

## Prerequisite

- You need an accepted proposal from a customer.

Learn more about [Working with proposals in AWS IQ](working-with-proposals.md "working-with-proposals.md").

- You need a valid AWS Certification.

## Create a permissions request

Create a permissions request by using the AWS IQ console.

1. Sign in to the AWS IQ console at [https://iq.aws.amazon.com/](https://iq.aws.amazon.com/ "https://iq.aws.amazon.com/").
2. On the **Requests** page, choose
   **Conversations**.
3. Choose the customer request for which you're creating the permission request.
4. Choose **Request Permission** in the **Proposals** pane
   under the accepted proposal.
5. Choose the **Permission policy** that you need to perform the
   work.
6. Optionally, explain why this role is appropriate for your project in the
   **Description** field.
7. Choose **Request**.

The customer will receive the request and accept or decline it.

###### Note

The customer can review AWS CloudTrail logs of your activity in their account. The customer can
revoke access at any time.

## Permission levels in AWS IQ

The following AWS Identity and Access Management (IAM) managed policies for job functions are available in AWS
IQ:

**`AdministratorAccess`**

Provides full access to AWS services and resources. For more information, see [AWS Managed Policies for Job Functions](../../../IAM/latest/UserGuide/access_policies_job-functions.md#jf_administrator "../../../IAM/latest/UserGuide/access_policies_job-functions.md#jf_administrator").

**`Billing`**

Provides full access to billing and cost management. This includes viewing account usage
and viewing and modifying budgets and payment methods. For more information, see [AWS Managed Policies for Job Functions](../../../IAM/latest/UserGuide/access_policies_job-functions.md#jf_accounts-payable "../../../IAM/latest/UserGuide/access_policies_job-functions.md#jf_accounts-payable").

**`DatabaseAdministrator`**

Provides full access to AWS services and actions required to set up and configure AWS
database services. For more information, see [AWS Managed Policies for Job Functions](../../../IAM/latest/UserGuide/access_policies_job-functions.md#jf_database-administrator "../../../IAM/latest/UserGuide/access_policies_job-functions.md#jf_database-administrator").

**`NetworkAdministrator`**

Provides full access to AWS services and actions required to set up and configure AWS
network resources. For more information, see [AWS Managed Policies for Job Functions](../../../IAM/latest/UserGuide/access_policies_job-functions.md#jf_network-administrator "../../../IAM/latest/UserGuide/access_policies_job-functions.md#jf_network-administrator") in the _IAM User
Guide_.

**`PowerUserAccess`**

Provides full access to AWS services and resources but doesn't allow management of
users and groups. For more information, see [AWS Managed Policies for Job Functions](../../../IAM/latest/UserGuide/access_policies_job-functions.md#jf_developer-power-user "../../../IAM/latest/UserGuide/access_policies_job-functions.md#jf_developer-power-user").

**`SecurityAudit`**

Provides full access to read security configuration metadata. It's useful for software
that audits the configuration of an AWS account. For more information, see [AWS Managed Policies for Job Functions](../../../IAM/latest/UserGuide/access_policies_job-functions.md#jf_security-auditor "../../../IAM/latest/UserGuide/access_policies_job-functions.md#jf_security-auditor").

**`SupportUser`**

Provides full access to troubleshoot and resolve issues in an AWS account. This policy
also enables the user to contact AWS Support to create and manage cases. For more information,
see [AWS Managed Policies for Job Functions](../../../IAM/latest/UserGuide/access_policies_job-functions.md#jf_support-user "../../../IAM/latest/UserGuide/access_policies_job-functions.md#jf_support-user").

**`SystemAdministrator`**

Provides full access to resources required for application and development operations.
For more information, see [AWS Managed Policies for Job Functions](../../../IAM/latest/UserGuide/access_policies_job-functions.md#jf_system-administrator "../../../IAM/latest/UserGuide/access_policies_job-functions.md#jf_system-administrator").

**`ViewOnlyAccess`**

Provides full access to view resources and basic metadata across all AWS services. For
more information, see [AWS Managed Policies for Job Functions](../../../IAM/latest/UserGuide/access_policies_job-functions.md#jf_view-only-user "../../../IAM/latest/UserGuide/access_policies_job-functions.md#jf_view-only-user").
