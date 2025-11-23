# Launch EC2 instances using a launch template

An Amazon EC2 launch template stores instance launch parameters so that you don't have to
specify them every time you launch an instance.

Several instance launch services can optionally use launch templates when launching
instances, while for other services, like EC2 Fleet, instances can't be launched unless a
launch template is used. This topic describes how to use a launch template when
launching an instance using the EC2 launch instance wizard, Amazon EC2 Amazon EC2 Auto Scaling, EC2 Fleet, and
Spot Fleet.

For more information about launch templates, including how to create a launch
template, see [Store instance launch parameters in Amazon EC2 launch templates](ec2-launch-templates.md "ec2-launch-templates.md").

###### Topics

- [Launch an Amazon EC2 instance
  using a launch template](#launch-instance-from-launch-template "#launch-instance-from-launch-template")
- [Launch instances in an Amazon EC2 Auto Scaling group using a
  launch template](#launch-templates-as "#launch-templates-as")
- [Launch an EC2 Fleet using a launch
  template](#launch-templates-ec2-fleet "#launch-templates-ec2-fleet")
- [Launch a Spot Fleet using a launch
  template](#launch-templates-spot-fleet "#launch-templates-spot-fleet")

## Launch an Amazon EC2 instance

using a launch template

You can use the parameters contained in a launch template to launch an Amazon EC2
instance. After selecting the launch template, but before launching the instance,
you can modify the launch parameters.

Instances that are launched using a launch template are automatically assigned two
tags with the keys `aws:ec2launchtemplate:id` and
`aws:ec2launchtemplate:version`. You can't remove or edit these
tags.

Console

###### To launch an instance using a launch template

1. Open the Amazon EC2 console at
   [https://console.aws.amazon.com/ec2/](https://console.aws.amazon.com/ec2/ "https://console.aws.amazon.com/ec2/").
2. Use one of the following options to select the launch
   template:
   - From the Amazon EC2 console dashboard, choose the down
     arrow next to **Launch instance**,
     choose **Launch instance from
     template**, and then for **Source
     template**, select a launch
     template.
   - In the navigation pane, choose **Launch
     Templates**, select the launch template,
     and choose **Actions**,
     **Launch instance from
     template**.

3. For **Source template version**, select the
   launch template version to use.
4. (Optional) You can modify the values for any of the launch
   parameters. If you don't modify a value, the value defined by
   the launch template is used. If no value was specified in the
   launch template, the default value for the parameter is
   used.
5. In the **Summary** panel, for
   **Number of instances**, specify the number
   of instances to launch.
6. Choose **Launch instance**.

If the instance fails to launch or the state immediately goes
to `terminated` instead of `running`, see
[Troubleshoot Amazon EC2 instance launch issues](troubleshooting-launch.md "troubleshooting-launch.md").

AWS CLI

###### To launch an instance from a launch template

- Use the [run-instances](../../../cli/latest/reference/ec2/run-instances.md "../../../cli/latest/reference/ec2/run-instances.md") command and specify the
  `--launch-template` parameter. Optionally specify
  the launch template version to use. If you don't specify the
  version, the default version is used.

```
aws ec2 run-instances \
    --launch-template LaunchTemplateId=`lt-0abcd290751193123`,Version=`1`
```

- To override a launch template parameter, specify the parameter
  in the [run-instances](../../../cli/latest/reference/ec2/run-instances.md "../../../cli/latest/reference/ec2/run-instances.md") command. The following example
  overrides the instance type that's specified in the launch
  template (if any).

```
aws ec2 run-instances \
    --launch-template LaunchTemplateId=`lt-0abcd290751193123` \
    --instance-type `t2.small`
```

- If you specify a nested parameter that's part of a complex
  structure, the instance is launched using the complex structure
  as specified in the launch template plus any additional nested
  parameters that you specify.

In the following example, the instance is launched with the
tag
``Owner`=`TeamA``
as well as any other tags that are specified in the launch
template. If the launch template has an existing tag with a key
of `Owner`, the value is
replaced with
`TeamA`.

```
aws ec2 run-instances \
    --launch-template LaunchTemplateId=`lt-0abcd290751193123` \
    --tag-specifications "ResourceType=instance,Tags=[{Key=`Owner`,Value=`TeamA`}]"
```

In the following example, the instance is launched with a
volume with the device name
`/dev/xvdb` as well as
any other block device mappings that are specified in the launch
template. If the launch template has an existing volume defined
for `/dev/xvdb`, its
values are replaced with the specified values.

```
aws ec2 run-instances \
    --launch-template LaunchTemplateId=`lt-0abcd290751193123` \
    --block-device-mappings "DeviceName=`/dev/xvdb`,Ebs={VolumeSize=`20`,VolumeType=`gp2`}"
```

If the instance fails to launch or the state immediately goes to
`terminated` instead of `running`, see [Troubleshoot Amazon EC2 instance launch issues](troubleshooting-launch.md "troubleshooting-launch.md").

PowerShell

###### To launch an instance from a launch template using the

AWS Tools for PowerShell

- Use the [New-EC2Instance](../../../powershell/latest/reference/Index.md "../../../powershell/latest/reference/Index.md") command and specify the
  `-LaunchTemplate` parameter. Optionally specify
  the launch template version to use. If you don't specify the
  version, the default version is used.

```
Import-Module AWS.Tools.EC2
New-EC2Instance `
    -LaunchTemplate (
        New-Object -TypeName Amazon.EC2.Model.LaunchTemplateSpecification -Property @{
            LaunchTemplateId = '`lt-0abcd290751193123`';
            Version          = '`4`'
    }
)
```

- To override a launch template parameter, specify the parameter
  in the [New-EC2Instance](../../../powershell/latest/reference/Index.md "../../../powershell/latest/reference/Index.md") command. The following example
  overrides the instance type that's specified in the launch
  template (if any).

```
Import-Module AWS.Tools.EC2
New-EC2Instance `
    -InstanceType `t4g.small` `
    -LaunchTemplate (
        New-Object -TypeName Amazon.EC2.Model.LaunchTemplateSpecification -Property @{
            LaunchTemplateId = '`lt-0abcd290751193123`';
            Version          = '`4`'
    }
)
```

- If you specify a nested parameter that's part of a complex
  structure, the instance is launched using the complex structure
  as specified in the launch template plus any additional nested
  parameters that you specify.

In the following example, the instance is launched with the
tag
``Owner`=`TeamA``
as well as any other tags that are specified in the launch
template. If the launch template has an existing tag with a key
of `Owner`, the value is
replaced with
`TeamA`.

```
Import-Module AWS.Tools.EC2
New-EC2Instance `
    -InstanceType `t4g.small`  `
    -LaunchTemplate (
        New-Object -TypeName Amazon.EC2.Model.LaunchTemplateSpecification -Property @{
            LaunchTemplateId = '`lt-0abcd290751193123`';
            Version          = '`4`'
        }
) `
    -TagSpecification (
        New-Object -TypeName Amazon.EC2.Model.TagSpecification -Property @{
            ResourceType = 'instance';
            Tags         = @(
                @{key = "`Owner`"; value = "`TeamA`" },
                @{key = "`Department`"; value = "`Operations`" }
            )
        }
)
```

In the following example, the instance is launched with a
volume with the device name
`/dev/xvdb` as well as
any other block device mappings that are specified in the launch
template. If the launch template has an existing volume defined
for `/dev/xvdb`, its
values are replaced with the specified values.

```
Import-Module AWS.Tools.EC2
New-EC2Instance `
    -InstanceType `t4g.small`  `
    -LaunchTemplate (
        New-Object -TypeName Amazon.EC2.Model.LaunchTemplateSpecification -Property @{
            LaunchTemplateId = '`lt-0abcd290751193123`';
            Version          = '`4`'
    }
) `
    -BlockDeviceMapping  (
        New-Object -TypeName Amazon.EC2.Model.BlockDeviceMapping -Property @{
            DeviceName = '`/dev/xvdb`';
            EBS        = (
                New-Object -TypeName Amazon.EC2.Model.EbsBlockDevice -Property @{
                    VolumeSize = `25`;
                    VolumeType = '`gp3`'
                }
            )
        }
)
```

If the instance fails to launch or the state immediately goes to
`terminated` instead of `running`, see [Troubleshoot Amazon EC2 instance launch issues](troubleshooting-launch.md "troubleshooting-launch.md").

## Launch instances in an Amazon EC2 Auto Scaling group using a

launch template

You can create an Amazon EC2 Auto Scaling group and specify a launch template to use for the group.
When Amazon EC2 Auto Scaling launches instances in the Amazon EC2 Auto Scaling group, it uses the launch parameters
defined in the associated launch template.

Before you can create an Amazon EC2 Auto Scaling group using a launch template, you must first create
a launch template that includes the parameters required to launch an instance in an
Amazon EC2 Auto Scaling group. Some parameters are required, such as the ID of the AMI, and some
parameters are not available to use with an Amazon EC2 Auto Scaling group. The console provides
guidance to help you create a template that you can use with Amazon EC2 Auto Scaling.

###### To create an Amazon EC2 Auto Scaling group with a launch template using the console

- For the instructions, see Create an Auto Scaling group using a launch
  template in the _Amazon EC2 Auto Scaling User Guide_.

###### To create or update an Amazon EC2 Auto Scaling group with a launch template using the

AWS CLI

- Use the [create-auto-scaling-group](../../../cli/latest/reference/autoscaling/create-auto-scaling-group.md "../../../cli/latest/reference/autoscaling/create-auto-scaling-group.md") or the [update-auto-scaling-group](../../../cli/latest/reference/autoscaling/update-auto-scaling-group.md "../../../cli/latest/reference/autoscaling/update-auto-scaling-group.md") command and specify the
  `--launch-template` parameter.

For more information, see the following topics in the
_Amazon EC2 Auto Scaling User Guide_:

- [Create a
  launch template for an Amazon EC2 Auto Scaling group](../../../autoscaling/ec2/userguide/create-launch-template.md "../../../autoscaling/ec2/userguide/create-launch-template.md")
- [Create a launch template using advanced settings](../../../autoscaling/ec2/userguide/advanced-settings-for-your-launch-template.md "../../../autoscaling/ec2/userguide/advanced-settings-for-your-launch-template.md")
- [Examples for creating and managing launch templates with the AWS Command Line Interface
  (AWS CLI)](../../../autoscaling/ec2/userguide/examples-launch-templates-aws-cli.md "../../../autoscaling/ec2/userguide/examples-launch-templates-aws-cli.md") – Provides examples that show how to create
  launch templates with various parameter combinations.
- [Create Amazon EC2 Auto Scaling groups using launch templates](../../../autoscaling/ec2/userguide/create-auto-scaling-groups-launch-template.md "../../../autoscaling/ec2/userguide/create-auto-scaling-groups-launch-template.md")
- [Update an
  Amazon EC2 Auto Scaling group](../../../autoscaling/ec2/userguide/update-auto-scaling-group.md "../../../autoscaling/ec2/userguide/update-auto-scaling-group.md")

## Launch an EC2 Fleet using a launch

template

A launch template is a requirement when creating an EC2 Fleet request. When Amazon EC2
fulfills the EC2 Fleet request, it uses the launch parameters defined in the associated
launch template. You can override some of the parameters that are specified in the
launch template. For more information, see [Create an EC2 Fleet](create-ec2-fleet.md "create-ec2-fleet.md").

###### To create an EC2 Fleet with a launch template using the AWS CLI

- Use the [create-fleet](../../../cli/latest/reference/ec2/create-fleet.md "../../../cli/latest/reference/ec2/create-fleet.md") command. Use the
  `--launch-template-configs` parameter to specify the launch
  template and any overrides for the launch template.

## Launch a Spot Fleet using a launch

template

A launch template is optional when creating a Spot Fleet request. If you don't use a
launch template, you can manually specify the launch parameters. If you use a launch
template, when Amazon EC2 fulfills the Spot Fleet request, it uses the launch parameters
defined in the associated launch template. You can override some of the parameters
that are specified in the launch template. For more information, see [Create a Spot Fleet](create-spot-fleet.md "create-spot-fleet.md").

###### To create a Spot Fleet request using a launch template

1. Open the Amazon EC2 console at
   [https://console.aws.amazon.com/ec2/](https://console.aws.amazon.com/ec2/ "https://console.aws.amazon.com/ec2/").
2. In the navigation pane, choose **Spot Requests**.
3. Choose **Request Spot Instances**.
4. Under **Launch parameters**, choose **Use a
   launch template**.
5. For **Launch template**, choose a launch template, and
   then, from the field to the right, choose the launch template
   version.
6. Configure your Spot Fleet by selecting different options on this screen. For
   more information about the options, see [Create a Spot Fleet request using defined
   parameters](create-spot-fleet.md#create-spot-fleet-advanced "create-spot-fleet.md#create-spot-fleet-advanced").
7. When you're ready to create your Spot Fleet, choose
   **Launch**.

###### To create a Spot Fleet request using a launch template

- Use the [request-spot-fleet](../../../cli/latest/reference/ec2/request-spot-fleet.md "../../../cli/latest/reference/ec2/request-spot-fleet.md") command. Use the
  `LaunchTemplateConfigs` parameter to specify the launch
  template and any overrides for the launch template.
