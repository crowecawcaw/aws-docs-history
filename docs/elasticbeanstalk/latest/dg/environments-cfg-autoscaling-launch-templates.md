# Migrating your Elastic Beanstalk

environment to launch templates

As of October 1, 2024, Amazon EC2 Auto Scaling no longer supports launch configurations for new accounts.
Accounts created prior to that date might have launch configurations.

We recommend migrating to **launch templates** for the following benefits:

- Improved availability for your applications
- Better optimization of workloads in your Auto Scaling groups
- Access to the latest EC2 and Auto Scaling features
  For more information, see [Auto Scaling
  launch configurations](../../../autoscaling/ec2/userguide/launch-configurations.md "../../../autoscaling/ec2/userguide/launch-configurations.md") in the _Amazon EC2 Auto Scaling User Guide_.

## Option settings for

launch templates

To migrate your environment from launch configurations to launch templates, set one of
the following configuration options:

- `RootVolumeType` option set to **gp3**. You can set this option with the [console](using-features.managing.ec2.md "using-features.managing.ec2.md") or the [namespace](using-features.managing.ec2.md "using-features.managing.ec2.md") .
- `BlockDeviceMappings` option contains **gp3**. You can set this option with the [console](using-features.managing.ec2.md "using-features.managing.ec2.md") or the [namespace](using-features.managing.ec2.md "using-features.managing.ec2.md").
- `DisableIMDSv1` option set to **true**. We recommend that you set this option using the [namespace](using-features.managing.ec2.md "using-features.managing.ec2.md").
- `EnableSpot` option set to **true**.
  For more information, see [Enabling Spot
  Instances](environments-cfg-autoscaling-enable-spot.md "environments-cfg-autoscaling-enable-spot.md").

###### Important

After an environment begins using launch templates, Elastic Beanstalk does not revert to launch
configurations, even if you remove the configuration options that originally triggered the
use of launch templates.

## Confirm whether

your environment has launch configurations or launch templates

You can confirm if your environment already uses launch templates, or if it's using
launch configurations, by inspecting the CloudFormation stack template.

###### To inspect your environment's CloudFormation stack template

1. Open the AWS CloudFormation console at [https://console.aws.amazon.com/cloudformation](https://console.aws.amazon.com/cloudformation/ "https://console.aws.amazon.com/cloudformation/").
2. On the navigation bar at the top of the screen, choose the AWS Region where you
   created the environment.
3. On the **Stacks** page of the CloudFormation console,
   inspect the **Description** column.

Locate and select the stack for the Elastic Beanstalk environment. CloudFormation displays the stack
details for the environment. 4. In **Stack details** select the **Template**
tab.

Using your browser's page search, you can search the template text for
_launchtemplate_ or
_launchconfiguration_.

For more information, see [View
stack information](../../../AWSCloudFormation/latest/UserGuide/cfn-console-view-stack-data-resources.md "../../../AWSCloudFormation/latest/UserGuide/cfn-console-view-stack-data-resources.md") in the _AWS CloudFormation User Guide_.

## Required

permissions for launch templates

The default Elastic Beanstalk managed service role policy [AWSElasticBeanstalkManagedUpdatesCustomerRolePolicy](../../../aws-managed-policy/latest/reference/AWSElasticBeanstalkManagedUpdatesCustomerRolePolicy.md "../../../aws-managed-policy/latest/reference/AWSElasticBeanstalkManagedUpdatesCustomerRolePolicy.md") provides the required
permissions to create and manage launch templates. Elastic Beanstalk must manage launch templates to
complete many environment operations, including creating environments.

If you attach custom policies to an Elastic Beanstalk service role, verify that the service role
includes the following permissions for creating launch templates. These permissions enable
Elastic Beanstalk to successfully create and update environments in your account:

###### Required permissions for Amazon EC2 launch templates

- `ec2:RunInstances`
- `ec2:CreateLaunchTemplate`
- `ec2:CreateLaunchTemplateVersions`
- `ec2:DeleteLaunchTemplate`
- `ec2:DeleteLaunchTemplateVersions`
- `ec2:DescribeLaunchTemplate`
- `ec2:DescribeLaunchTemplateVersions`

The following example IAM policy includes these permissions.

```
{
  "Statement": [
    {
      "Effect": "Allow",
      "Action": [
        "ec2:RunInstances",
        "ec2:CreateLaunchTemplate",
        "ec2:CreateLaunchTemplateVersions",
        "ec2:DeleteLaunchTemplate",
        "ec2:DeleteLaunchTemplateVersions",
        "ec2:DescribeLaunchTemplate",
        "ec2:DescribeLaunchTemplateVersions"
      ],
      "Resource": [
                "*"
            ]
     }
  ]
}
```

For more information, see [Managing Elastic Beanstalk service roles](iam-servicerole.md "iam-servicerole.md") and [Managing Elastic Beanstalk user policies](AWSHowTo.iam.md "AWSHowTo.iam.md").

## More about launch

templates

To learn more about launch templates, see [Auto Scaling launch templates](../../../autoscaling/ec2/userguide/launch-templates.md "../../../autoscaling/ec2/userguide/launch-templates.md") in
the _Amazon EC2 Auto Scaling User Guide_.

To learn more about the AWS transition to launch templates and the benefits they
offer, see [Amazon EC2 Auto Scaling will no longer add support for new EC2 features to Launch
Configurations](https://aws.amazon.com/blogs/compute/amazon-ec2-auto-scaling-will-no-longer-add-support-for-new-ec2-features-to-launch-configurations/ "https://aws.amazon.com/blogs/compute/amazon-ec2-auto-scaling-will-no-longer-add-support-for-new-ec2-features-to-launch-configurations/") in the _AWS Compute Blog_.

###### Important

You don't need to follow the procedure referenced in this blog article to transition
an older environment to launch templates. To migrate an existing Elastic Beanstalk environment to
launch templates, set one of the options listed in [Option settings for
launch templates](#environments-cfg-autoscaling-launch-templates-options "#environments-cfg-autoscaling-launch-templates-options").
