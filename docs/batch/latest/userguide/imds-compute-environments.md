# Instance Metadata Service (IMDS) configuration

The Instance Metadata Service (IMDS) provides metadata about your EC2 instances to
applications running on those instances. Use IMDSv2 for all new workloads and migrate existing
workloads from IMDSv1 to IMDSv2 for improved security. For more information about IMDS and
configuring IMDS, see [Use instance metadata to manage your EC2 instance](../../../AWSEC2/latest/UserGuide/ec2-instance-metadata.md "../../../AWSEC2/latest/UserGuide/ec2-instance-metadata.md") and [Configure
instance metadata options for new instances](../../../AWSEC2/latest/UserGuide/configuring-IMDS-new-instances.md "../../../AWSEC2/latest/UserGuide/configuring-IMDS-new-instances.md") in the
_Amazon EC2 User Guide_.

## Configuration scenarios

Choose the appropriate configuration method based on your compute environment setup:

### Default AMI with no launch template

When you use the default AWS Batch AMI and don't specify a launch template, choose one of
these options:

1. **Use Amazon Linux 2023 default AMI** – Amazon Linux 2023
   requires IMDSv2 by default. When you create your compute environment, select **Amazon
   Linux 2023** as the image type.
2. **Set account-level IMDSv2 configuration** – Configure your
   AWS account to require IMDSv2 for all new instances. This setting affects all new instances
   that you launch in the account. For instructions, see [Set IMDSv2 as the default for the account](../../../AWSEC2/latest/UserGuide/configuring-IMDS-new-instances.md#set-imdsv2-account-defaults "../../../AWSEC2/latest/UserGuide/configuring-IMDS-new-instances.md#set-imdsv2-account-defaults") in the
   _Amazon EC2 User Guide_.

###### Note

Account-level IMDS configuration can be overridden by launch template or AMI
configuration. Launch template settings take precedence over account-level settings.

### Custom AMI with no launch template

When you use a custom AMI without a launch template, choose one of these options:

1. **Use Amazon Linux 2023 as base** – Build your custom AMI
   using Amazon Linux 2023 as the base image. For information about creating custom AMIs for
   Batch, see [Tutorial: Create a compute resource AMI](create-batch-ami.md "create-batch-ami.md").
2. **Configure IMDSv2 in your custom AMI** – When you create
   your custom AMI, configure it to require IMDSv2. For instructions, see [Configure instance metadata options for custom AMI](../../../AWSEC2/latest/UserGuide/configuring-IMDS-new-instances.md#configure-IMDS-new-instances-ami-configuration "../../../AWSEC2/latest/UserGuide/configuring-IMDS-new-instances.md#configure-IMDS-new-instances-ami-configuration") in the
   _Amazon EC2 User Guide_.
3. **Set account-level IMDSv2 configuration** – Configure your
   AWS account to require IMDSv2 for all new instances. This setting affects all new instances
   that you launch in the account. For instructions, see [Set IMDSv2 as the default for the account](../../../AWSEC2/latest/UserGuide/configuring-IMDS-new-instances.md#set-imdsv2-account-defaults "../../../AWSEC2/latest/UserGuide/configuring-IMDS-new-instances.md#set-imdsv2-account-defaults") in the
   _Amazon EC2 User Guide_.

###### Note

Account-level IMDS configuration can be overridden by launch template or AMI
configuration. Launch template settings take precedence over account-level settings.

### Using launch templates

When you use launch templates in your compute environment, add metadata options to your
launch template to require IMDSv2. For more information about using launch templates with Batch,
see [Use Amazon EC2 launch templates with AWS Batch](launch-templates.md "launch-templates.md").

```
{
    "LaunchTemplateName": "batch-imdsv2-template",
    "VersionDescription": "IMDSv2 only template for Batch",
    "LaunchTemplateData": {
        "MetadataOptions": {
            "HttpTokens": "required"
        }
    }
}
```

Create the launch template using the AWS CLI:

```
`aws ec2 create-launch-template --cli-input-json file://imds-template.json`
```
