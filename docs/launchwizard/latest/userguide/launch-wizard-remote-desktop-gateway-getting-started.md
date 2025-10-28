# Get Started with AWS Launch Wizard

for Remote Desktop Gateway

This section contains information to help you set up your environment to deploy RD Gateway
with Launch Wizard. When your environment is set up, you can deploy RD Gateway application with Launch Wizard by
following the steps and parameter specification details provided in this section.

###### Topics to help you get started:

- [Access AWS Launch Wizard](#launch-wizard-remote-desktop-gateway-access "#launch-wizard-remote-desktop-gateway-access")
- [Specialized
  knowledge](#launch-wizard-remote-desktop-gateway-specialized-knowledge "#launch-wizard-remote-desktop-gateway-specialized-knowledge")
- [Amazon Web Services account](#launch-wizard-remote-desktop-gateway-aws-account "#launch-wizard-remote-desktop-gateway-aws-account")
- [Service Quotas](#launch-wizard-remote-desktop-gateway-resource-quotas "#launch-wizard-remote-desktop-gateway-resource-quotas")
- [Amazon Elastic Compute Cloud key pairs](#launch-wizard-remote-desktop-gateway-key-pairs "#launch-wizard-remote-desktop-gateway-key-pairs")
- [AWS Identity and Access Management
  permissions](#launch-wizard-remote-desktop-gateway-iam-permissions "#launch-wizard-remote-desktop-gateway-iam-permissions")

## Access AWS Launch Wizard

You can launch AWS Launch Wizard from the AWS Launch Wizard console located at [https://console.aws.amazon.com/launchwizard](https://console.aws.amazon.com/launchwizard "https://console.aws.amazon.com/launchwizard").

## Specialized

knowledge

This deployment requires a moderate level of familiarity with AWS services. If you’re new
to AWS, see [Getting Started Resource
Center](https://aws.amazon.com/getting-started "https://aws.amazon.com/getting-started") and [AWS Training and
Certification](https://aws.amazon.com/training "https://aws.amazon.com/training"). These sites provide materials for learning how to design, deploy, and
operate your infrastructure and applications on the AWS Cloud.

This Launch Wizard assumes familiarity with Remote Desktop Gateway.

## Amazon Web Services account

### Sign up for an AWS account

If you do not have an AWS account, complete the following steps to create one.

###### To sign up for an AWS account

1. Open [https://portal.aws.amazon.com/billing/signup](https://portal.aws.amazon.com/billing/signup "https://portal.aws.amazon.com/billing/signup").
2. Follow the online instructions.

Part of the sign-up procedure involves receiving a phone call or text message and entering
a verification code on the phone keypad.

When you sign up for an AWS account, an _AWS account root user_ is created. The root user has access to all AWS services
and resources in the account. As a security best practice, assign administrative access to a user, and use only the root user to perform [tasks that require root user access](../../../IAM/latest/UserGuide/id_root-user.md#root-user-tasks "../../../IAM/latest/UserGuide/id_root-user.md#root-user-tasks").

AWS sends you a confirmation email after the sign-up process is
complete. At any time, you can view your current account activity and manage your account by
going to [https://aws.amazon.com/](https://aws.amazon.com/ "https://aws.amazon.com/") and choosing **My
Account**.

### Create a user with administrative access

After you sign up for an AWS account, secure your AWS account root user, enable AWS IAM Identity Center, and create an administrative user so that you
don't use the root user for everyday tasks.

###### Secure your AWS account root user

1. Sign in to the [AWS Management Console](https://console.aws.amazon.com/ "https://console.aws.amazon.com/") as the account owner by choosing **Root user** and entering your AWS account email address. On the next page, enter your password.

For help signing in by using root user, see [Signing in as the root user](../../../signin/latest/userguide/console-sign-in-tutorials.md#introduction-to-root-user-sign-in-tutorial "../../../signin/latest/userguide/console-sign-in-tutorials.md#introduction-to-root-user-sign-in-tutorial") in the _AWS Sign-In User Guide_. 2. Turn on multi-factor authentication (MFA) for your root user.

For instructions, see [Enable a virtual MFA device for your AWS account root user (console)](../../../IAM/latest/UserGuide/enable-virt-mfa-for-root.md "../../../IAM/latest/UserGuide/enable-virt-mfa-for-root.md") in the _IAM User Guide_.

###### Create a user with administrative access

1. Enable IAM Identity Center.

For instructions, see [Enabling
AWS IAM Identity Center](../../../singlesignon/latest/userguide/get-set-up-for-idc.md "../../../singlesignon/latest/userguide/get-set-up-for-idc.md") in the
_AWS IAM Identity Center User Guide_. 2. In IAM Identity Center, grant administrative access to a user.

For a tutorial about using the IAM Identity Center directory as your identity source, see [Configure user access with the default IAM Identity Center directory](../../../singlesignon/latest/userguide/quick-start-default-idc.md "../../../singlesignon/latest/userguide/quick-start-default-idc.md") in the
_AWS IAM Identity Center User Guide_.

###### Sign in as the user with administrative access

- To sign in with your IAM Identity Center user, use the sign-in URL that was sent to your email address when you created the IAM Identity Center user.

For help signing in using an IAM Identity Center user, see [Signing in to the AWS access portal](../../../signin/latest/userguide/iam-id-center-sign-in-tutorial.md "../../../signin/latest/userguide/iam-id-center-sign-in-tutorial.md") in the _AWS Sign-In User Guide_.

###### Assign access to additional users

1. In IAM Identity Center, create a permission set that follows the best practice of applying least-privilege permissions.

For instructions, see [Create a permission set](../../../singlesignon/latest/userguide/get-started-create-a-permission-set.md "../../../singlesignon/latest/userguide/get-started-create-a-permission-set.md") in the _AWS IAM Identity Center User Guide_. 2. Assign users to a group, and then assign single sign-on access to the group.

For instructions, see [Add groups](../../../singlesignon/latest/userguide/addgroups.md "../../../singlesignon/latest/userguide/addgroups.md") in the _AWS IAM Identity Center User Guide_.

## Service Quotas

If necessary, [request service quota
increases](https://console.aws.amazon.com/servicequotas/ "https://console.aws.amazon.com/servicequotas/") for the following resources. You might need to request increases if your
existing deployment currently uses these resources and if this Launch Wizard deployment could result in
exceeding the default quotas. The [Service Quotas
console](https://console.aws.amazon.com/servicequotas/ "https://console.aws.amazon.com/servicequotas/") displays your usage and quotas for some aspects of some services. For more
information, see [What
is Service Quotas?](../../../servicequotas/latest/userguide/intro.md "../../../servicequotas/latest/userguide/intro.md") and [AWS service quotas](../../../general/latest/gr/aws_service_limits.md "../../../general/latest/gr/aws_service_limits.md").

Existing VPC Service Quotas:

| Resource                                                 | Default quota     | This deployment uses |
| -------------------------------------------------------- | ----------------- | -------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Elastic IP Addresses                                     | 5 per Region      | 2                    |
| AWS Identity and Access Management (IAM) security groups | 300 per account   | 1                    |
| IAM roles                                                | 1,000 per account | 1                    |
| Auto Scaling groups                                      | 200 per Region    | 1                    |
| Amazon EC2 On-Demand Instances (Standard)                | 5 per Region      | 1-4                  | New VPC Service Quotas:                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| Resource                                                 | Default quota     | This deployment uses |
| ---                                                      | ---               | ---                  |
| VPCs                                                     | 5 per Region      | 1                    |
| Elastic IP Addresses                                     | 5 per Region      | 2                    |
| Internet Gateway                                         | 5 per Region      | 1                    |
| AWS Identity and Access Management (IAM) security groups | 300 per account   | 1                    |
| IAM roles                                                | 1,000 per account | 1                    |
| Auto Scaling groups                                      | 200 per Region    | 1                    |
| Amazon EC2 On-Demand Instances (Standard)                | 5 per Region      | 1-4                  | ## Amazon Elastic Compute Cloud key pairs Ensure that at least one Amazon EC2 key pair exists in your AWS account in the Region where you plan to deploy the Launch Wizard application. Note the key pair name because you will use it during deployment. To create a key pair, see [Amazon EC2 key pairs and EC2 instances](../../../AWSEC2/latest/UserGuide/ec2-key-pairs.md "../../../AWSEC2/latest/UserGuide/ec2-key-pairs.md"). For testing or proof-of-concept purposes, we recommend creating a new key pair instead of using one that’s already being used by a production instance. ## AWS Identity and Access Management permissions Before deploying the Launch Wizard application, you must sign in to the AWS Management Console with IAM permissions for the resources that the templates deploy. The _AdministratorAccess_ managed policy within IAM provides sufficient permissions, although your organization may choose to use a custom policy with more restrictions. For more information, see [AWS managed policies for job functions](../../../IAM/latest/UserGuide/access_policies_job-functions.md "../../../IAM/latest/UserGuide/access_policies_job-functions.md"). |
