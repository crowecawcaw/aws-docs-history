

# Instance Metadata Service (IMDS) configuration
<a name="imds-compute-environments"></a>

The Instance Metadata Service (IMDS) provides metadata about your EC2 instances to applications running on those instances. Use IMDSv2 for all new workloads and migrate existing workloads from IMDSv1 to IMDSv2 for improved security. For more information about IMDS and configuring IMDS, see [Use instance metadata to manage your EC2 instance](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ec2-instance-metadata.html) and [Configure instance metadata options for new instances](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/configuring-IMDS-new-instances.html) in the *Amazon EC2 User Guide*.

## Configuration scenarios
<a name="imds-configuration-scenarios"></a>

Choose the appropriate configuration method based on your compute environment setup:

### Default AMI with no launch template
<a name="imds-default-ami-no-lt"></a>

When you use the default AWS Batch AMI and don't specify a launch template, choose one of these options:

1. **Use Amazon Linux 2023 default AMI** – Amazon Linux 2023 requires IMDSv2 by default. When you create your compute environment, select **Amazon Linux 2023** as the image type.

1. **Set account-level IMDSv2 configuration** – Configure your AWS account to require IMDSv2 for all new instances. This setting affects all new instances that you launch in the account. For instructions, see [Set IMDSv2 as the default for the account](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/configuring-IMDS-new-instances.html#set-imdsv2-account-defaults) in the *Amazon EC2 User Guide*.
**Note**  
Account-level IMDS configuration can be overridden by launch template or AMI configuration. Launch template settings take precedence over account-level settings.

### Custom AMI with no launch template
<a name="imds-custom-ami-no-lt"></a>

When you use a custom AMI without a launch template, choose one of these options:

1. **Use Amazon Linux 2023 as base** – Build your custom AMI using Amazon Linux 2023 as the base image. For information about creating custom AMIs for Batch, see [Tutorial: Create a compute resource AMI](create-batch-ami.md).

1. **Configure IMDSv2 in your custom AMI** – When you create your custom AMI, configure it to require IMDSv2. For instructions, see [Configure instance metadata options for custom AMI](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/configuring-IMDS-new-instances.html#configure-IMDS-new-instances-ami-configuration) in the *Amazon EC2 User Guide*.

1. **Set account-level IMDSv2 configuration** – Configure your AWS account to require IMDSv2 for all new instances. This setting affects all new instances that you launch in the account. For instructions, see [Set IMDSv2 as the default for the account](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/configuring-IMDS-new-instances.html#set-imdsv2-account-defaults) in the *Amazon EC2 User Guide*.
**Note**  
Account-level IMDS configuration can be overridden by launch template or AMI configuration. Launch template settings take precedence over account-level settings.

### Using launch templates
<a name="imds-launch-template"></a>

When you use launch templates in your compute environment, add metadata options to your launch template to require IMDSv2. For more information about using launch templates with Batch, see [Use Amazon EC2 launch templates with AWS Batch](launch-templates.md).

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
aws ec2 create-launch-template --cli-input-json file://imds-template.json
```