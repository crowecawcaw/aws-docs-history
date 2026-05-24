# Getting started with EC2 policies

EC2 policies let you enforce declarative configurations across accounts in your organization. This topic walks you through the steps to enable, create, and attach EC2 policies.

## Prerequisites

Before you begin, make sure you have the required permissions to perform
declarative policy tasks. For more information, see [Prerequisites for managing
declarative policies](orgs_manage_policies_prereqs.md "orgs_manage_policies_prereqs.md").

## Procedure

For all of these steps, you sign in as an IAM user, assume an IAM role, or sign in
as the root user ([not
recommended](../../../IAM/latest/UserGuide/best-practices.md#lock-away-credentials "../../../IAM/latest/UserGuide/best-practices.md#lock-away-credentials")) in the organization's management account.

1. [Enable EC2 policies for your
   organization](enable-policy-type.md "enable-policy-type.md").

###### Note

**Enabling trusted access is required**

You must enable trusted access for Amazon EC2. This creates a read-only
service-linked role that generates the account status report of the current configuration for accounts in your organization.

**Using the console**

If you use the Organizations console, enabling trusted access is part of the process for
enabling EC2 policies.

**Using the AWS CLI**

If you use the AWS CLI, use two separate operations:

    * [EnablePolicyType](../APIReference/API_EnablePolicyType.md "../APIReference/API_EnablePolicyType.md") – Enables EC2
     policies.
    * [EnableAWSServiceAccess](../APIReference/API_EnableAWSServiceAccess.md "../APIReference/API_EnableAWSServiceAccess.md") – Enables trusted
     access.For more information about how to enable trusted access for a specific

service with the AWS CLI, see [AWS services that you can use with AWS Organizations](orgs_integrate_services_list.md "orgs_integrate_services_list.md"). 2. [Run the account
status report](orgs_manage_policies_ec2_status-report.md "orgs_manage_policies_ec2_status-report.md"). 3. [Create an EC2
policy](orgs_policies_create.md "orgs_policies_create.md"). 4. [Attach the EC2 policy to your
organization's root, OU, or account](orgs_policies_attach.md "orgs_policies_attach.md"). 5. [View the combined effective
EC2 policy that applies to an account](orgs_manage_policies_effective.md "orgs_manage_policies_effective.md").

## Additional resources

- [EC2 policy syntax and examples](orgs_manage_policies_ec2_syntax.md "orgs_manage_policies_ec2_syntax.md")
