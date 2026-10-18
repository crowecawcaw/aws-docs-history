

# Build on an instance from an Auto Scaling group
<a name="infra-config-parent-instance"></a>

By default, Image Builder launches a new Amazon EC2 instance for every build. With a parent instance, Image Builder takes an instance that's already running in an Amazon EC2 Auto Scaling group instead, so the build doesn't wait for an instance to launch. This applies only to the build phase. For the API fields, see [ParentInstanceConfiguration](https://docs.aws.amazon.com/imagebuilder/latest/APIReference/API_ParentInstanceConfiguration.html) in the *EC2 Image Builder API Reference*. To build on one specific instance instead, use the `parentInstanceId` input of the [LaunchInstance](wfdoc-step-actions.md#wfdoc-step-action-launch-instance) step action.

To create an infrastructure configuration, see [Create an infrastructure configuration](create-infra-config.md).

## How Image Builder takes an instance
<a name="infra-config-parent-instance-how"></a>

Image Builder picks an instance at random from the instances in the group that meet all of the following conditions. You can't choose which instance Image Builder takes.
+ The instance is in the `InService` state.
+ Its SSM Agent is online in Systems Manager.
+ It runs the same platform and architecture as the image. For container builds, Image Builder compares the architecture only when the container recipe's instance configuration specifies an image.

Before the build starts, Image Builder adds the following tags to the instance and then detaches it from the group:
+ `Name`: `Build instance for {{image-name}}`. This replaces the instance's current `Name` tag.
+ `CreatedBy`: `EC2 Image Builder`. With this tag, Image Builder can run commands on the instance and terminate it.
+ `Ec2ImageBuilderArn`: the ARN of the image that Image Builder builds.
+ The resource tags from your infrastructure configuration.

These are the same tags that Image Builder adds to the instances that it launches. The group's desired capacity doesn't change, so the group launches a replacement, and the instance doesn't return to the group. For other effects of detaching, see [Detach or attach instances from your Auto Scaling group](https://docs.aws.amazon.com/autoscaling/ec2/userguide/ec2-auto-scaling-detach-attach-instances.html) in the *Amazon EC2 Auto Scaling User Guide*.

## Settings that come from the instance
<a name="infra-config-parent-instance-settings"></a>

This applies only to the build instance. Test instances launch as usual, with the settings from your infrastructure configuration and recipe.

The build instance is already running, so it keeps the settings that the group launched it with. Image Builder doesn't use the following settings from your infrastructure configuration and recipe:
+ Infrastructure configuration: the instance type, instance profile, subnet, security groups, key pair, placement, and instance metadata options.
+ Image recipe: the base image, block device mappings, and user data. Image Builder creates the output AMI from the instance's own volumes.
+ Container recipe: the instance configuration.

To change these settings, update the group's launch template.

## Requirements
<a name="infra-config-parent-instance-requirements"></a>

Before you use a parent instance, make sure that the following are true:
+ The group is in the same AWS account and AWS Region as the infrastructure configuration, and you have permissions to describe it.
+ The group's instances run the same platform and architecture as the image.
+ SSM Agent is installed and running on the group's instances, and they are online in Systems Manager. Image Builder runs your components through Systems Manager, so it takes only an instance whose agent is online. A new instance isn't online until its agent registers with Systems Manager. This requires an instance profile that allows Systems Manager, such as one with the AmazonSSMManagedInstanceCore policy, and network access to Systems Manager. For more information, see [SSM Agent](https://docs.aws.amazon.com/systems-manager/latest/userguide/ssm-agent.html) in the *AWS Systems Manager User Guide*.
+ The group's instances have an instance profile with the permissions that your build needs. For more information, see [Instance profile for the group's instances](#infra-config-parent-instance-profile).
+ For container builds, the instance is already running Docker.
+ Your pipeline has an execution role that can use the group. For more information, see [Execution role permissions](#infra-config-parent-instance-role).

## Instance profile for the group's instances
<a name="infra-config-parent-instance-profile"></a>

The instance keeps the instance profile that the group launched it with, so the instance profile in your infrastructure configuration doesn't apply. Set an instance profile in the group's launch template that has the permissions that Image Builder and your components need. For the permissions that Image Builder needs, see [IAM prerequisites](set-up-ib-env.md#image-builder-IAM-prereq). Your components might need more. For example, a component that downloads files from Amazon S3 needs `s3:GetObject` permissions for those files. To add an instance profile to the group's instances, do the following:

1. Open the Amazon EC2 console, and in the navigation pane, choose **Launch Templates**.

1. Choose the group's launch template, and then choose **Actions**, **Modify template (Create new version)**.

1. Under **Advanced details**, for **IAM instance profile**, choose your instance profile, and then create the version.

1. In the navigation pane, choose **Auto Scaling Groups**, and then choose your group. On the **Details** tab, edit the launch template, choose the new version, and then choose **Update**.

1. Replace the instances that are already running. New instances get the new instance profile, but running instances keep the old one. To replace them, start an instance refresh. For more information, see [Use an instance refresh to update instances in an Auto Scaling group](https://docs.aws.amazon.com/autoscaling/ec2/userguide/asg-instance-refresh.html) in the *Amazon EC2 Auto Scaling User Guide*.

For more information, see [IAM role for applications that run on Amazon EC2 instances](https://docs.aws.amazon.com/autoscaling/ec2/userguide/us-iam-role.html) in the *Amazon EC2 Auto Scaling User Guide*.

## Execution role permissions
<a name="infra-config-parent-instance-role"></a>

Image Builder uses the execution role of your pipeline to take the instance. The Image Builder service-linked role doesn't have permissions for Auto Scaling groups, so you must specify an execution role. In the console, set it in the **Execution role** field when you create or update the pipeline. With the API, use the `executionRole` parameter of `CreateImagePipeline`, `UpdateImagePipeline`, or `CreateImage`. For more information, see [Specify the IAM service role that Image Builder uses to run workflow actions](pipeline-workflows.md#pipeline-workflow-service-role).

In addition to the EC2ImageBuilderExecutionPolicy managed policy, the role needs the following permissions:
+ `autoscaling:DescribeAutoScalingGroups`, to find the group's `InService` instances.
+ `ec2:CreateTags` and `ec2:DeleteTags` on the group's instances, to tag an instance while it's still in the group, and to remove the tags if Image Builder can't detach it.
+ `autoscaling:DetachInstances` on the group.

The following example policy grants these permissions for one group. Attach it to the execution role with EC2ImageBuilderExecutionPolicy.

```
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Sid": "TagInstanceInASG",
            "Effect": "Allow",
            "Action": [
                "ec2:CreateTags",
                "ec2:DeleteTags"
            ],
            "Resource": "arn:aws:ec2:*:*:instance/*",
            "Condition": {
                "StringEquals": {
                    "ec2:ResourceTag/aws:autoscaling:groupName": "{{my-build-pool}}"
                }
            }
        },
        {
            "Sid": "DescribeASG",
            "Effect": "Allow",
            "Action": "autoscaling:DescribeAutoScalingGroups",
            "Resource": "*"
        },
        {
            "Sid": "DetachFromASG",
            "Effect": "Allow",
            "Action": "autoscaling:DetachInstances",
            "Resource": "arn:aws:autoscaling:*:*:autoScalingGroup:*:autoScalingGroupName/{{my-build-pool}}"
        }
    ]
}
```

Instead of writing the policy yourself, you can create a role that has EC2ImageBuilderExecutionPolicy and these permissions from the EC2ImageBuilderParentInstanceASGRoleTemplate role template. In the console, choose **Create new role with required permission** in the infrastructure configuration. With the AWS CLI, use the [acquire-role](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iam/acquire-role.html) command. The following example creates a role named `EC2ImageBuilderParentInstanceASG-{{my-build-pool}}` for the `{{my-build-pool}}` group. The role template isn't available in the AWS GovCloud (US) Regions or the China Regions.

```
aws iam acquire-role \
    --template-arn arn:aws:iam::aws:role-template/imagebuilder.amazonaws.com/EC2ImageBuilderParentInstanceASGRoleTemplate:3 \
    --replacement-values \
    'AutoScalingGroupName={Values=[{{my-build-pool}}]},RoleNameSuffix={Values=[{{my-build-pool}}]}'
```

## When the group has no instance available
<a name="infra-config-parent-instance-capacity"></a>

Image Builder waits up to `capacityWaitTimeoutSeconds`, at most one hour, for an instance that meets the conditions in [How Image Builder takes an instance](#infra-config-parent-instance-how). If none becomes available, the build fails. Image Builder doesn't fall back to launching a new instance. With 0 or no value, the build fails right away. A lower `timeoutSeconds` on the workflow step ends the wait sooner. Image Builder checks the group about every 15 seconds for the first 5 minutes, then about every 45 seconds, so the actual wait can differ from `capacityWaitTimeoutSeconds` by up to one check.

## When Image Builder terminates the instance
<a name="infra-config-parent-instance-termination"></a>

Image Builder terminates the instance like a build instance that it launched. `terminateInstanceOnFailure` applies when the build fails, and `terminateInstanceOnCompletion` applies when image creation ends without a failure. To keep the instance after a successful build, set `terminateInstanceOnCompletion` to `false`. The AWS managed build workflows follow this setting. In a custom workflow, `terminateInstanceOnCompletion` doesn't override a `TerminateInstance` step. To keep the instance, skip the step with an `if` condition on `terminateInstanceOnCompletion`, or remove the step. For more information, see [TerminateInstance](wfdoc-step-actions.md#wfdoc-step-action-terminate-instance).

For AMI builds, the `CreateImage` step stops the instance before it creates the image, so an instance that you keep is in the `stopped` state after the build. Start it to use it again. You're billed for its volumes, and for the instance while it runs, until you terminate it.