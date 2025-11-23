# Get started with AWS Launch Wizard for Active

Directory

This section contains information to set up your environment for Launch Wizard to deploy domain
controllers.

###### Topics

- [Accessing AWS Launch Wizard Active Directory](#accessing-launch-wizard-ad "#accessing-launch-wizard-ad")
- [Specialized knowledge](#launch-wizard-ad-specialized-knowledge "#launch-wizard-ad-specialized-knowledge")
- [Amazon Web Services account](#launch-wizard-ad-aws-account "#launch-wizard-ad-aws-account")
- [Technical requirements](#launch-wizard-ad-technical-requirements "#launch-wizard-ad-technical-requirements")
- [Service Quotas](#launch-wizard-ad-resource-quotas "#launch-wizard-ad-resource-quotas")
- [IAM permissions](#launch-wizard-ad-iam-permissions "#launch-wizard-ad-iam-permissions")
- [Active Directory deployment options](#launch-wizard-ad-setup "#launch-wizard-ad-setup")

## Accessing AWS Launch Wizard Active Directory

You can launch AWS Launch Wizard from the AWS Launch Wizard console located at [https://console.aws.amazon.com/launchwizard](https://console.aws.amazon.com/launchwizard "https://console.aws.amazon.com/launchwizard").

## Specialized knowledge

This deployment requires a moderate level of familiarity with AWS services. If
you’re new to AWS, see [Getting Started
Resource Center](https://aws.amazon.com/getting-started "https://aws.amazon.com/getting-started") and [AWS Training
and Certification](https://aws.amazon.com/training "https://aws.amazon.com/training"). These sites provide materials for learning how to design,
deploy, and operate your infrastructure and applications on the AWS Cloud.

This Launch Wizard deployment assumes familiarity with Active Directory concepts and
usage.

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

## Technical requirements

Before you start the Launch Wizard deployment, review the following information and make sure
that your account is properly configured. Otherwise, deployment might fail.

## Service Quotas

If necessary, [request service quota
increases](https://console.aws.amazon.com/servicequotas/ "https://console.aws.amazon.com/servicequotas/") for the resources deployed by Launch Wizard. You might need to request
increases if your existing deployment currently uses these resources and if this Launch Wizard
deployment could result in exceeding the default quotas. The [Service Quotas console](https://console.aws.amazon.com/servicequotas/ "https://console.aws.amazon.com/servicequotas/") displays your usage and quotas
for some aspects of some services. For more information, see [What is Service Quotas?](../../../servicequotas/latest/userguide/intro.md "../../../servicequotas/latest/userguide/intro.md") and
[AWS
service quotas](../../../general/latest/gr/aws_service_limits.md "../../../general/latest/gr/aws_service_limits.md").

## IAM permissions

Before deploying the Launch Wizard application, you must sign in to the
AWS Management Console with IAM permissions for the resources that the
templates deploy. The _AdministratorAccess_ managed
policy within IAM provides sufficient permissions, although your organization may
choose to use a custom policy with more restrictions. For more information, see [AWS managed policies for job functions](../../../IAM/latest/UserGuide/access_policies_job-functions.md "../../../IAM/latest/UserGuide/access_policies_job-functions.md").

## Active Directory deployment options

This section contains information on what configuration is performed for deployment of
domain controllers into a new or existing VPC. You can deploy a new Active Directory
infrastructure on Amazon EC2, deploy a new AWS Managed Microsoft AD, or extend an existing on-premises
Active Directory into the AWS Cloud.

### Active Directory

configurations

When you use Launch Wizard to deploy Active Directory, the following key operations are
performed. These operations result in the creation of new records or entries in
Active Directory.

- When you create a new Active Directory domain, Launch Wizard creates two new Amazon EC2
  instances and promotes the servers to domain controllers in your
  domain.
- When you extend an existing Active Directory domain, Launch Wizard creates two new
  Amazon EC2 instances and optionally joins them to the domain.
- When you create an AWS Managed Microsoft AD, Launch Wizard deploys the managed
  directory.
- All deployment types create ingress and egress rules to communicate with
  your domain controllers.

### On-premises Active Directory through

Direct Connect

If you are deploying domain controllers to extend an on-premises Active Directory
into an existing VPC, ensure that the following prerequisites are in place.

- Make sure that you have connectivity between your AWS account and your
  on-premises network. You can establish a dedicated network connection from
  your on-premises network to your AWS account with Direct Connect. For more
  information, see [the
  AWS Direct Connect documentation](../../../directconnect/latest/UserGuide/Welcome.md "../../../directconnect/latest/UserGuide/Welcome.md").
- The domain functional level of your Active Directory domain controller
  must be Windows Server 2012 or later.
- The IP addresses of your DNS server must be either in the same VPC CIDR
  range as the one in which your Launch Wizard domain controllers will be created, or
  in the private IP address range.
- The firewall on the Active Directory domain controllers should allow the
  connections from the VPC from which you will create the Launch Wizard deployment. At
  a minimum, your configuration should include the ports mentioned in [How to configure a firewall for Active Directory domains and
  trusts](https://support.microsoft.com/en-us/help/179442/how-to-configure-a-firewall-for-domains-and-trusts "https://support.microsoft.com/en-us/help/179442/how-to-configure-a-firewall-for-domains-and-trusts").

You can optionally perform the following step.

- Establish DNS resolution across your environments. For options on how to
  set this up, see [How to Set Up DNS Resolution Between On-Premises Networks and AWS
  using Directory Service and Amazon Route 53](https://aws.amazon.com/blogs/security/how-to-set-up-dns-resolution-between-on-premises-networks-and-aws-using-aws-directory-service-and-amazon-route-53/ "https://aws.amazon.com/blogs/security/how-to-set-up-dns-resolution-between-on-premises-networks-and-aws-using-aws-directory-service-and-amazon-route-53/") or [How to Set Up DNS Resolution Between On-Premises Networks and AWS
  Using Directory Service and Microsoft Active Directory](https://aws.amazon.com/blogs/security/how-to-set-up-dns-resolution-between-on-premises-networks-and-aws-using-aws-directory-service-and-microsoft-active-directory/ "https://aws.amazon.com/blogs/security/how-to-set-up-dns-resolution-between-on-premises-networks-and-aws-using-aws-directory-service-and-microsoft-active-directory/").
