

# Use Amazon EC2 launch templates with AWS Batch
<a name="launch-templates"></a>

AWS Batch supports using Amazon EC2 launch templates with your EC2 compute environments. With launch templates, you can modify the default configuration of your AWS Batch compute resources without needing to create customized AMIs.

Launch templates can specify AMIs that take precedence in the AMI selection order. For more information, see [AMI selection order](ami-selection-order.md).

**Note**  
When you specify a custom launch template for a AWS Batch compute environment, AWS Batch doesn't directly attach your launch template to the underlying Auto Scaling group. Instead, AWS Batch creates a separate, Batch-managed launch template for the Auto Scaling group and incorporates the relevant settings from your custom launch template into it. As a result, the launch template that you see associated with the Auto Scaling group is different from the one you originally specified. This is expected behavior.

**Note**  
Launch templates aren't supported on AWS Fargate resources.

You must create a launch template before you can associate it with a compute environment. You can create a launch template in the Amazon EC2 console. Or, you can use the AWS CLI or an AWS SDK. For example, the following JSON file represents a launch template that resizes the Docker data volume for the default AWS Batch compute resource AMI and also sets it to be encrypted.

```
{
    "LaunchTemplateName": "increase-container-volume-encrypt",
    "LaunchTemplateData": {
        "BlockDeviceMappings": [
            {
                "DeviceName": "/dev/xvda",
                "Ebs": {
                    "Encrypted": true,
                    "VolumeSize": 100,
                    "VolumeType": "gp2"
                }
            }
        ]
    }
}
```

You can create the previous launch template by saving the JSON to a file that's called `lt-data.json` and running the following AWS CLI command.

```
aws ec2 --region {{<region>}} create-launch-template --cli-input-json file://lt-data.json
```

For more information about launch templates, see [Launching an Instance from a Launch Template](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ec2-launch-templates.html) in the *Amazon EC2 User Guide*.

If you use a launch template to create your compute environment, you can move the following existing compute environment parameters to your launch template:

**Note**  
Suppose that any of these parameters (except the Amazon EC2 tags) are specified both in the launch template and in the compute environment configuration. Then, the compute environment parameters take precedence. Amazon EC2 tags are merged between the launch template and the compute environment configuration. If there's a collision on the tag's key, the value in the compute environment configuration takes precedence.
+ Amazon EC2 key pair
+ Amazon EC2 AMI ID
+ Security group IDs
+ Amazon EC2 tags

The following launch template parameters are **ignored** by AWS Batch:
+ Instance type (specify your desired instance types when you create your compute environment)
+ Instance role (specify your desired instance role when you create your compute environment)
+ Network interface subnets (specify your desired subnets when you create your compute environment)
+ Instance market options (AWS Batch must control Spot Instance configuration)
+ Disable API termination (AWS Batch must control instance lifecycle)

AWS Batch only updates the launch template with a new launch template version during infrastructure updates. For more information, see [Update a compute environment in AWS Batch](updating-compute-environments.md).

## Default and override launch templates
<a name="default-lt-and-overrides"></a>

You can define a default launch template for the compute environment and an override launch template for specific instance types and families. This can be useful to you so that the default template is used for the majority of instance types in the compute environments.

The substitution variables `$Default` and `$Latest` can be used instead of naming a specific version. If you do not provide an override launch template, the default launch template is automatically applied.

If you use either the `$Default` or `$Latest` variable, AWS Batch will apply the current information at the time that the compute environment is created. If the default or latest version changes in the future, you must update the information through [UpdateComputeEnvironment](https://docs.aws.amazon.com/batch/latest/APIReference/API_UpdateComputeEnvironment.html) or through the AWS Management Console - AWS Batch.

To provide additional flexibility, you can define override launch templates are applied to specific compute instance types or families.

**Note**  
You can specify up to ten (10) override launch templates per compute environment.

Use the `targetInstanceTypes` parameter to select the instance type or family that should use this override launch template. The instance type or family must be first identified by the [`instanceTypes`](https://docs.aws.amazon.com/batch/latest/APIReference/API_ComputeResource.html#Batch-Type-ComputeResource-instanceTypes) parameter.

If you define launch template overrides and decide to remove them later, you can pass an empty array to unset the [`overrides`](https://docs.aws.amazon.com/batch/latest/APIReference/API_LaunchTemplateSpecification.html#Batch-Type-LaunchTemplateSpecification-overrides) parameter in the [`UpdateComputeEnvironment`](https://docs.aws.amazon.com/batch/latest/APIReference/API_LaunchTemplateSpecification.html) API operation. You can also choose to not include the `overrides` parameter when submitting the `UpdateComputeEnvironment` API operation. For more information see, [`LaunchTemplateSpecification.overrides`](https://docs.aws.amazon.com/batch/latest/APIReference/API_LaunchTemplateSpecification.html#Batch-Type-LaunchTemplateSpecification-overrides)

For more information, see [`LaunchTemplateSpecificationOverride.targetInstanceTypes`](https://docs.aws.amazon.com/batch/latest/APIReference/API_LaunchTemplateSpecificationOverride.html#Batch-Type-LaunchTemplateSpecificationOverride-targetInstanceTypes) in the AWS Batch API Reference guide.

## Amazon EC2 user data in launch templates
<a name="lt-user-data"></a>

You can supply Amazon EC2 user data in your launch template that's run by [cloud-init](https://cloudinit.readthedocs.io/en/latest/index.html) when your instances launch. Your user data can perform common configuration scenarios, including but not limited to the following:
+ [Including users or groups](https://cloudinit.readthedocs.io/en/latest/topics/examples.html#including-users-and-groups)
+ [Installing packages](https://cloudinit.readthedocs.io/en/latest/topics/examples.html#install-arbitrary-packages)
+ [Creating partitions and file systems](https://cloudinit.readthedocs.io/en/latest/topics/examples.html#create-partitions-and-filesystems)

Amazon EC2 user data in launch templates must be in the [MIME multi-part archive](https://cloudinit.readthedocs.io/en/latest/topics/format.html#mime-multi-part-archive) format. This is because your user data is merged with other AWS Batch user data that's required to configure your compute resources. You can combine multiple user data blocks together into a single MIME multi-part file. For example, you might want to combine a cloud boothook that configures the Docker daemon with a user data shell script that writes configuration information for the Amazon ECS container agent.

If you're using AWS CloudFormation, the [AWS::CloudFormation::Init](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-init.html) type can be used with the [cfn-init](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/cfn-init.html) helper script to perform common configuration scenarios.

A MIME multi-part file consists of the following components:
+ The content type and part boundary declaration: `Content-Type: multipart/mixed; boundary="==BOUNDARY=="`
+ The MIME version declaration: `MIME-Version: 1.0`
+ One or more user data blocks that contain the following components:
  + The opening boundary that signals the beginning of a user data block: `--==BOUNDARY==`. You must keep the line before this boundary blank.
  + The content type declaration for the block: `Content-Type: {{text/cloud-config}}; charset="us-ascii"`. For more information about content types, see the [Cloud-Init documentation](https://cloudinit.readthedocs.io/en/latest/topics/format.html). You must keep the line after the content type declaration blank.
  + The content of the user data, such as a list of shell commands or `cloud-init` directives.
+ The closing boundary that signals the end of the MIME multi-part file: `--==BOUNDARY==--`. You must keep the line before the closing boundary blank.

**Note**  
If you add user data to a launch template in the Amazon EC2 console, you can paste it in as plaintext. Or, you can upload it from a file. If you use the AWS CLI or an AWS SDK, you must first `base64` encode the user data and submit that string as the value of the `UserData` parameter when you call [CreateLaunchTemplate](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_CreateLaunchTemplate.html), as shown in this JSON file.  

```
{
    "LaunchTemplateName": "base64-user-data",
    "LaunchTemplateData": {
        "UserData": "{{ewogICAgIkxhdW5jaFRlbXBsYXRlTmFtZSI6ICJpbmNyZWFzZS1jb250YWluZXItdm9sdW...}}"
    }
}
```

### Reserved Amazon ECS agent configuration values
<a name="lt-reserved-ecs-config"></a>

AWS Batch writes specific Amazon ECS agent configuration values to `/etc/ecs/ecs.config` when instances launch in EC2-based managed compute environments that use Amazon ECS. AWS Batch may also overwrite these values during compute environment updates, so your changes may not persist.

**Important**  
Conflicts between your user data and AWS Batch-managed values can prevent jobs from being scheduled, cause unexpected scaling behavior, and result in unexpected costs.

**Important**  
Do not copy user data from a AWS Batch-managed launch template into your own launch template. AWS Batch-managed user data contains values that differ between compute environments and change when the compute environment is updated. If your launch template contains copied values, they may conflict with the expected values for the current compute environment.

Do not set the following values in your launch template user data. These values are managed by AWS Batch and conflicts can cause scheduling and scaling issues:
+ `ECS_CLUSTER`
+ `ECS_INSTANCE_ATTRIBUTES`

For more information about the parameters listed above, see [Amazon ECS container agent configuration](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/ecs-agent-config.html) in the *Amazon Elastic Container Service Developer Guide*.

**Topics**
+ [Default and override launch templates](#default-lt-and-overrides)
+ [Amazon EC2 user data in launch templates](#lt-user-data)
+ [Reference: Amazon EC2 launch template examples](launch-template-examples.md)