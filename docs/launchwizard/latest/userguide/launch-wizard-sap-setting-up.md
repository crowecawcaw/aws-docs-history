# Set up for AWS Launch Wizard for SAP

This section describes the prerequisites that you must verify to deploy an SAP
application with AWS Launch Wizard.

###### Prerequisites

- [General](#launch-wizard-sap-prerequisites "#launch-wizard-sap-prerequisites")
- [IAM](#launch-wizard-sap-iam "#launch-wizard-sap-iam")

## General prerequisites

The following general prerequisites must be met to deploy an application with
Launch Wizard.

- You must create a VPC that consists of private subnet(s) in a minimum of
  two Availability Zones. The subnets must have outbound internet access. For
  more information on how to create and set up a VPC, see [Getting Started with Amazon VPC](../../../vpc/latest/userguide/vpc-getting-started.md "../../../vpc/latest/userguide/vpc-getting-started.md") in the _Amazon VPC
  User Guide_.
- You must create a user or role and attach the **AmazonLaunchWizardFullAccessV2** policy. See the [following sections](#launch-wizard-sap-iam "#launch-wizard-sap-iam") for the steps
  to attach the policy to the user or role.
- When using AWS Backup to back up databases on Amazon EC2 instances,
  1.  You must set up the required permissions in the role
      `AmazonEC2RoleForLaunchWizard` for Amazon EC2 to backup
      and restore SAP HANA database when setting up AWS Systems Manager for SAP with
      fully-managed backup for SAP HANA with AWS Backup.

  [The policies](../../../aws-backup/latest/devguide/security-iam-awsmanpol.md#aws-managed-policies "../../../aws-backup/latest/devguide/security-iam-awsmanpol.md#aws-managed-policies") (that need to be attached to the role
  `AmazonEC2RoleForLaunchWizard`) containing these
  required permissions are:

      + `AWSBackupDataTransferAccess`
      + `AWSBackupRestoreAccessForSAPHANA`
      + `AWSBackupServiceRolePolicyForBackup`

  For more information, see [Set up required permissions for Amazon EC2 instance for backup and
  restore of SAP HANA database](../../../ssm-sap/latest/userguide/get-started.md#backup-permissions "../../../ssm-sap/latest/userguide/get-started.md#backup-permissions") . 2. If you intend to assign one or more backup plans through
  LaunchWizard, ensure your account has the role [`AWSBackupDefaultServiceRole`](../../../aws-backup/latest/devguide/iam-service-roles.md#creating-default-service-role-console "../../../aws-backup/latest/devguide/iam-service-roles.md#creating-default-service-role-console") to ensure
  the HANA database is successfully assigned to the chosen backup plan
  and that the resulting managed backups are successful. This role is
  not required if you do not choose a backup plan though the LaunchWizard
  workflow.

- To run custom pre- and post-configuration deployment scripts, you must add
  the permissions listed in [Add permissions to run custom
  pre- and post-deployment configuration scripts](#launch-wizard-sap-iam-scripts "#launch-wizard-sap-iam-scripts") to the
  `AmazonEC2RoleForLaunchWizard` role.
- If you want to install SAP software, you must download the software from
  the SAP Software Download page and upload it to an Amazon S3 bucket. For steps on
  how to download the software and upload it to an Amazon S3 bucket, see [Make SAP HANA software available for AWS Launch Wizard
  to deploy a HANA database](launch-wizard-sap-structure.md "launch-wizard-sap-structure.md").
- Depending on the operating system version you want to use for the SAP
  deployment, an SAP Marketplace subscription may be required. For a complete
  list of supported operating system versions, see [Operating systems](launch-wizard-sap-versions.md#launch-wizard-sap-ascs-support-os "launch-wizard-sap-versions.md#launch-wizard-sap-ascs-support-os").

## AWS Identity and Access Management (IAM)

Establishing the AWS Identity and Access Management (IAM) role and setting up users with the required
permissions is typically performed by **an IAM
administrator** for your organization. The steps are as follows:

- A one-time creation of IAM roles that Launch Wizard uses to deploy SAP systems on
  AWS.
- The creation of users or roles who can grant permission for Launch Wizard to deploy
  applications.

###### Launch Wizard for SAP IAM topics

- [Sign up for an AWS account](#sign-up-for-aws "#sign-up-for-aws")
- [Create a user with administrative access](#create-an-admin "#create-an-admin")
- [One-time creation of IAM
  role](#launch-wizard-sap-iam-role "#launch-wizard-sap-iam-role")
- [Enable users to use Launch Wizard](#launch-wizard-user-setup "#launch-wizard-user-setup")
- [Add permissions to use
  AWS KMS keys](#launch-wizard-sap-iam-encryption "#launch-wizard-sap-iam-encryption")
- [Add permissions to run custom
  pre- and post-deployment configuration scripts](#launch-wizard-sap-iam-scripts "#launch-wizard-sap-iam-scripts")
- [Add permissions to save
  deployment artifacts to Amazon S3](#launch-wizard-sap-iam-s3-artifacts "#launch-wizard-sap-iam-s3-artifacts")

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

### One-time creation of IAM

role

On the **Choose Application** page of Launch Wizard, under
**Permissions**, Launch Wizard displays the IAM role
required for the Amazon EC2 instances created by Launch Wizard to access other AWS services
on your behalf. When you select **Next**, Launch Wizard attempts to
discover the IAM role in your account. If the role exists in your account, it
is attached to the instance profile for the Amazon EC2 instances that Launch Wizard launches
from your account. If the role does not exist, Launch Wizard attempts to create the role
with the same name, `AmazonEC2RoleForLaunchWizard`.

The `AmazonEC2RoleForLaunchWizard` role is comprised of two IAM
managed policies: `AmazonSSMManagedInstanceCore` and
`AmazonEC2RolePolicyForLaunchWizard`. The
`AmazonEC2RoleForLaunchWizard` role is used by the instance
profile for the Amazon EC2 instances that Launch Wizard launches into your account as part of
the deployment.

If you want to deploy AWS Backint Agent as a backup and restore solution for
your application, you must attach a policy to the
`AmazonEC2RoleForLaunchWizard` so that Launch Wizard can perform
Backint Agent operations on your behalf. The required policy and instructions
can be found in [Step 2 of the Backint Agent IAM documentation](../../../sap/latest/sap-hana/aws-backint-agent-prerequisites.md#aws-backint-agent-iam "../../../sap/latest/sap-hana/aws-backint-agent-prerequisites.md#aws-backint-agent-iam"). During a
deployment, Launch Wizard provides the policy as well as the steps to update the
role, taking user specifications into account.

After the IAM roles are created, the IAM administrator can either continue
with the deployment process or optionally delegate the application deployment
process to another user, as described in the following section. At this point in
the IAM set up process, the IAM administrator can exit the Launch Wizard service.

### Enable users to use Launch Wizard

To deploy an SAP system with Launch Wizard, your user must have the permissions
provided by the **AmazonLaunchWizardFullAccessV2**
policy. The following guidance is provided for IAM administrators to provide
permissions for users to access and deploy applications from Launch Wizard using the
**AmazonLaunchWizardFullAccessV2**
policy.

To provide access, add permissions to your users, groups, or roles:

- Users and groups in AWS IAM Identity Center:

Create a permission set. Follow the instructions in [Create a permission set](../../../singlesignon/latest/userguide/howtocreatepermissionset.md "../../../singlesignon/latest/userguide/howtocreatepermissionset.md") in the _AWS IAM Identity Center User Guide_.

- Users managed in IAM through an identity provider:

Create a role for identity federation. Follow the instructions in [Create a role for a third-party identity provider (federation)](../../../IAM/latest/UserGuide/id_roles_create_for-idp.md "../../../IAM/latest/UserGuide/id_roles_create_for-idp.md")
in the _IAM User Guide_.

- IAM users:
  - Create a role that your user can assume. Follow the instructions in [Create a role for an IAM user](../../../IAM/latest/UserGuide/id_roles_create_for-user.md "../../../IAM/latest/UserGuide/id_roles_create_for-user.md") in the _IAM User Guide_.
  - (Not recommended) Attach a policy directly to a user or add a user to a user group. Follow the instructions in [Adding permissions to a user (console)](../../../IAM/latest/UserGuide/id_users_change-permissions.md#users_change_permissions-add-console "../../../IAM/latest/UserGuide/id_users_change-permissions.md#users_change_permissions-add-console") in the _IAM User Guide_.

###### Important

You must log in with the user or assume the role associated with this
IAM policy when you use Launch Wizard.

### Add permissions to use

AWS KMS keys

AWS Launch Wizard uses AWS default encryption keys to encrypt Amazon EBS volumes. In
addition, Launch Wizard supports the use of KMS keys created and maintained in AWS KMS.
You can choose to either create new keys or use preexisting keys to encrypt your
EBS volumes. You must add permissions to the KMS key policy for your key so
that Launch Wizard can use your KMS key for encryption.

###### How to add permissions to your KMS key policy so that Launch Wizard can use your

key for encryption

1. Sign in to the AWS Management Console and open the AWS Key Management Service (AWS KMS) console at [https://console.aws.amazon.com/kms](https://console.aws.amazon.com/kms "https://console.aws.amazon.com/kms").
2. To change the AWS Region, use the Region selector in the upper-right corner of the page.
3. Choose **Customer managed keys** in the left
   navigation pane.
4. Select the alias of the KMS key that you want to use to encrypt your
   EBS volumes.
5. Under **Key users**, choose
   **Add**.
6. Select the check box next to `AmazonEC2RoleForLaunchWizard`
   and the role your users assume with Launch Wizard full access permissions.
7. Choose **Add**. Verify that
   `AmazonEC2RoleForLaunchWizard` and the user or role with
   Launch Wizard full access permissions appear in the **Key
   users** list.

### Add permissions to run custom

pre- and post-deployment configuration scripts

To run custom pre- and post-configuration deployment scripts, you must add the
following permissions to the `AmazonEC2RoleForLaunchWizard` role. The
following steps guide you through the process of adding the required permissions
for using custom scripts to the `AmazonEC2RoleForLaunchWizard`
role.

1. Sign in to the AWS Management Console and open the IAM console at [https://console.aws.amazon.com/iam/](https://console.aws.amazon.com/iam "https://console.aws.amazon.com/iam").
2. In the navigation pane, choose Policies, Create policy.
3. On the **Create policy** page, choose
   **JSON**, then copy and paste the following policy
   into the **JSON** tab. Enter the S3 paths where your
   scripts are stored.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Sid": "VisualEditor0",
 "Effect": "Allow",
 "Action": [
 "s3:GetObject",
 "s3:GetBucketLocation"
 ],
 "Resource": [
 "arn:aws:s3:::`<S3bucket1>`/`<S3prefix1`>/`<script1`>",
 "arn:aws:s3:::`<S3bucket2>`/`<S3prefix2>`/`<script2>`",
 "arn:aws:s3:::`<S3bucket1>`",
 "arn:aws:s3:::`<S3bucket2>`"
 ]
 }
 ]
}`

```

4. Choose **Next: Tags** and create any tags you
   require.
5. Choose **Next: Review** and enter a
   **Name** for the policy.
6. Choose **Create Policy**.
7. Verify that the correct policy is listed, and then choose
   **Policy actions**.
8. Choose **Attach**.
9. Search for the policy named
   **AmazonEC2RoleForLaunchWizard** and select the
   check box to the left of the policy name.
10. Choose **Attach policy**.

If the pre- or post-deployment configuration deployment scripts are expected
to run additional AWS services, the permissions to use the services must also
be manually added as policy to the
`AmazonEC2RoleForLaunchWizard`.

### Add permissions to save

deployment artifacts to Amazon S3

To create AWS Service Catalog products from successful deployments,
which include AWS CloudFormation templates and application configuration scripts, you must
provide access to an Amazon S3 location to save the generated artifacts.

The following steps guide you through adding the required permissions for
saving deployment artifacts to Amazon S3. These permissions are required in
addition the ones provided by the
`AmazonLaunchWizardFullAccessV2` role. If the S3 bucket that
you want to use to save deployment artifacts does not contain the prefix
`launchwizard` in its name, you must perform the following
steps to attach the required policy to the IAM role that will be used for
performing the deployments.

1. Sign in to the AWS Management Console and open the IAM console at [https://console.aws.amazon.com/iam/](https://console.aws.amazon.com/iam "https://console.aws.amazon.com/iam").
2. In the navigation pane, choose Policies, Create policy.
3. On the **Create policy** page, choose
   **JSON**, then copy and paste the following policy
   into the **JSON** tab. Enter the S3 path where you want
   to store your artifacts in the policy.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [

 {
 "Sid": "SaveLaunchWizardDeploymentArtifacts",
 "Effect": "Allow",
 "Action": [
 "s3:PutObject"
 ],
 "Resource": [
 "arn:aws:s3:::${bucketName}/${bucketFolder}*"
 ]
 }
 ]
 }`

```

4. Choose **Next: Tags** and create any tags you
   require.
5. Choose **Next: Review** and enter a
   **Name** for the policy.
6. Choose **Create Policy**.
7. Verify that the correct policy is listed, and then choose
   **Policy actions**.
8. Choose **Attach**.
9. Search for the role your users assume with Launch Wizard full access
   permissions and select the check box to the left of the policy name.
10. Choose **Attach policy**.
