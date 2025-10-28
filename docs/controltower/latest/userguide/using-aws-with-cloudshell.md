# Use AWS CloudShell to work with AWS Control Tower

AWS CloudShell is an AWS service that facilitates working in the AWS CLI — it's a
browser-based, pre-authenticated shell that you can launch directly from the AWS Management Console. There's
no need to download or install command line tools. You can run AWS CLI commands for AWS Control Tower and
other AWS services from your preferred shell (Bash, PowerShell or Z shell).

When you [launch AWS CloudShell
from the AWS Management Console](../../../cloudshell/latest/userguide/working-with-cloudshell.md#launch-options "../../../cloudshell/latest/userguide/working-with-cloudshell.md#launch-options"), the AWS credentials you used to sign in to the console are
available in a new shell session. You can skip entering your configuring credentials when you
interact with AWS Control Tower and other AWS services, and you'll be using AWS CLI version 2, which is
pre-installed on the shell's compute environment.You're pre-authenticated with AWS CloudShell.

## Obtain IAM permissions for AWS CloudShell

AWS Identity and Access Management provides access management resources that allow administrators to grant
permissions to IAM users and IAM Identity Center users for access to AWS CloudShell.

The quickest way for an administrator to grant access to users is through an AWS managed
policy. An [AWS
managed policy](../../../IAM/latest/UserGuide/access_policies_managed-vs-inline.md#aws-managed-policies "../../../IAM/latest/UserGuide/access_policies_managed-vs-inline.md#aws-managed-policies") is a standalone policy that's created and administered by AWS. The
following AWS managed policy for CloudShell can be attached to IAM identities:

- `AWSCloudShellFullAccess`: Grants permission to use AWS CloudShell with full
  access to all features.

If you want to limit the scope of actions that an IAM user or IAM Identity Center user can perform with AWS CloudShell,
you can create a custom policy that uses the `AWSCloudShellFullAccess` managed
policy as a template. For more information about limiting the actions that are available to
users in CloudShell, see [Managing AWS CloudShell access and
usage with IAM policies](../../../cloudshell/latest/userguide/sec-auth-with-identities.md "../../../cloudshell/latest/userguide/sec-auth-with-identities.md") in the _AWS CloudShell User Guide_.

###### Note

Your IAM identity also requires a policy that grants permission to make calls to
AWS Control Tower. For more information, see [Permissions required to use the AWS Control Tower console](access-control-managing-permissions.md#additional-console-required-permissions "access-control-managing-permissions.md#additional-console-required-permissions").

### Launch AWS CloudShell

From the AWS Management Console, you can launch CloudShell by choosing the following options
available on the navigation bar:

- Choose the CloudShell icon.
- Start typing "cloudshell" in Search box and then choose the CloudShell
  option.

Now that you've started CloudShell, you can enter any AWS CLI commands you require to
work with AWS Control Tower. For example, you can check your AWS Config status.
