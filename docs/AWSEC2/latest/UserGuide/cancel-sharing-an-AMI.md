# Cancel having an AMI shared with your AWS account

An Amazon Machine Image (AMI) can be [shared with specific
AWS accounts](sharingamis-explicit.md "sharingamis-explicit.md") by adding the accounts to the AMI's launch permissions. If an
AMI has been shared with your AWS account and you no longer want it shared with your
account, you can remove your account from the AMI's launch permissions. You do this by
running the `cancel-image-launch-permission` AWS CLI command. When running this
command, your AWS account is removed from the launch permissions for the specified
AMI. To find the AMIs that are shared with your AWS account, see [Find shared AMIs to use for Amazon EC2 instances](usingsharedamis-finding.md "usingsharedamis-finding.md").

You might cancel having an AMI shared with your account, for example, to reduce the
likelihood of launching an instance with an unused or deprecated AMI that was shared
with you. When you cancel having an AMI shared with your account, it no longer appears
in any AMI lists in the EC2 console or in the output for [describe-images](../../../cli/latest/reference/ec2/describe-images.md "../../../cli/latest/reference/ec2/describe-images.md").

###### Topics

- [Limitations](#cancel-sharing-an-AMI-limitations "#cancel-sharing-an-AMI-limitations")
- [Cancel having an AMI shared with your
  account](#cancel-image-launch-permission "#cancel-image-launch-permission")

## Limitations

- You can remove your account from the launch permissions of an AMI that is shared
  with your AWS account only. You can't use
  `cancel-image-launch-permission` to remove your account from the launch
  permissions of an [AMI shared
  with an organization or organizational unit (OU)](share-amis-with-organizations-and-OUs.md "share-amis-with-organizations-and-OUs.md") or to remove access to
  public AMIs.
- You can’t permanently remove your account from the launch permissions of an AMI. An AMI owner can share an AMI with your account again.
- AMIs are a Regional resource. When running `cancel-image-launch-permission`,
  you must specify the Region in which the AMI is located. Either specify the
  Region in the command, or use the AWS_DEFAULT_REGION [environment
  variable](../../../cli/latest/userguide/cli-configure-envvars.md "../../../cli/latest/userguide/cli-configure-envvars.md").
- Only the AWS CLI and SDKs support removing your account from the launch permissions of an AMI. The EC2 console does not currently support this action.

## Cancel having an AMI shared with your

account

###### Note

After you cancel having an AMI shared with your account, you can't undo it. To regain
access to the AMI, the AMI owner must share it with your account.

AWS CLI

###### To cancel having an AMI shared with your account

Use the [cancel-image-launch-permission](../../../cli/latest/reference/ec2/cancel-image-launch-permission.md "../../../cli/latest/reference/ec2/cancel-image-launch-permission.md") command.

```
aws ec2 cancel-image-launch-permission \
    --image-id `ami-0abcdef1234567890` \
    --region `us-east-1`
```

PowerShell

###### To cancel having an AMI shared with your account

Use the [Stop-EC2ImageLaunchPermission](../../../powershell/latest/reference/index.md "../../../powershell/latest/reference/index.md") cmdlet.

```
Stop-EC2ImageLaunchPermission `
    -ImageId `ami-0abcdef1234567890` `
    -Region `us-east-1`
```
