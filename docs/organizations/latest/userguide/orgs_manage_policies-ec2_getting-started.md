

# Getting started with EC2 policies
<a name="orgs_manage_policies-ec2_getting-started"></a>

EC2 policies let you enforce declarative configurations across accounts in your organization. This topic walks you through the steps to enable, create, and attach EC2 policies.

## Prerequisites
<a name="orgs_manage_policies-ec2_getting-started-prerequisites"></a>

Before you begin, make sure you have the required permissions to perform declarative policy tasks. For more information, see [Prerequisites for managing declarative policies](orgs_manage_policies_prereqs.md).

## Procedure
<a name="orgs_manage_policies-ec2_getting-started-procedure"></a>

For all of these steps, you sign in as an IAM user, assume an IAM role, or sign in as the root user ([not recommended](https://docs.aws.amazon.com/IAM/latest/UserGuide/best-practices.html#lock-away-credentials)) in the organization's management account.

1. [Enable EC2 policies for your organization](enable-policy-type.md).
**Note**  
**Enabling trusted access is required**  
You must enable trusted access for Amazon EC2. This creates a read-only service-linked role that generates the account status report of the current configuration for accounts in your organization.  
**Using the console**  
If you use the Organizations console, enabling trusted access is part of the process for enabling EC2 policies.  
**Using the AWS CLI**  
If you use the AWS CLI, use two separate operations:  
[EnablePolicyType](https://docs.aws.amazon.com/organizations/latest/APIReference/API_EnablePolicyType.html) – Enables EC2 policies.
[EnableAWSServiceAccess](https://docs.aws.amazon.com/organizations/latest/APIReference/API_EnableAWSServiceAccess.html) – Enables trusted access.
For more information about how to enable trusted access for a specific service with the AWS CLI, see [AWS services that you can use with AWS Organizations](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_integrate_services_list.html).

1. [Run the account status report](orgs_manage_policies_ec2_status-report.md).

1. [Create an EC2 policy](orgs_policies_create.md).

1. [Attach the EC2 policy to your organization's root, OU, or account](orgs_policies_attach.md).

1. [View the combined effective EC2 policy that applies to an account](orgs_manage_policies_effective.md).

## Additional resources
<a name="orgs_manage_policies-ec2_getting-started-additional-resources"></a>
+ [EC2 policy syntax and examples](orgs_manage_policies_ec2_syntax.md)