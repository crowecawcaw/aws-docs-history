# Configure burstable performance instances

The steps for launching, monitoring, and modifying burstable performance instances (T
instances) are similar. The key difference is the default credit specification when they
launch.

Each T instance family comes with the following
_default credit specification_:

- T4g, T3a, and T3 instances launch as `unlimited`
- T3 instances on a Dedicated Host can only launch as `standard`
- T2 instances launch as `standard`
  You can [change the default credit specification](#burstable-performance-instance-set-default-credit-specification-for-account "#burstable-performance-instance-set-default-credit-specification-for-account") for the account.

###### Tasks

- [Configure the credit specification at launch](#launch-burstable-performance-instances "#launch-burstable-performance-instances")
- [Configure an Amazon EC2 Auto Scaling group to
  set the credit specification as unlimited](#burstable-performance-instances-auto-scaling-grp "#burstable-performance-instances-auto-scaling-grp")
- [Manage the credit specification
  of a burstable performance instance](#modify-burstable-performance-instances "#modify-burstable-performance-instances")
- [Manage the default credit specification for an account](#burstable-performance-instance-set-default-credit-specification-for-account "#burstable-performance-instance-set-default-credit-specification-for-account")

## Configure the credit specification at launch

You can launch your T instances with a credit specification of `unlimited`
or `standard`.

The following procedures describe how to use the EC2 console or the AWS CLI. For
information about using an Amazon EC2 Auto Scaling group, see [Configure an Amazon EC2 Auto Scaling group to
set the credit specification as unlimited](#burstable-performance-instances-auto-scaling-grp "#burstable-performance-instances-auto-scaling-grp").

Console

###### To configure the credit specification of an instance at launch

1. Follow the procedure to [launch an instance](ec2-launch-instance-wizard.md "ec2-launch-instance-wizard.md").
2. Under **Instance type**, select a T instance
   type.
3. Expand **Advanced details**. For **Credit
   specification**, select a credit specification.
4. In the **Summary** panel, review your instance
   configuration, and then choose **Launch instance**.

AWS CLI

###### To set the credit specification of an instance at launch

Use the [run-instances](../../../cli/latest/reference/ec2/run-instances.md "../../../cli/latest/reference/ec2/run-instances.md") command with the
`--credit-specification` option.

```
--credit-specification CpuCredits=unlimited
```

PowerShell

###### To set the credit specification of an instance at launch

Use the [New-EC2Instance](../../../powershell/latest/reference/items/New-EC2Instance.md "../../../powershell/latest/reference/items/New-EC2Instance.md")
cmdlet with the `-CreditSpecification_CpuCredit` parameter.

```
-CreditSpecification_CpuCredit unlimited
```

## Configure an Amazon EC2 Auto Scaling group to

set the credit specification as unlimited

When T instances are launched or started, they require CPU credits for a good
bootstrapping experience. If you use an Amazon EC2 Auto Scaling group to launch your instances, we
recommend that you configure your instances as `unlimited`. If you do, the
instances use surplus credits when they are automatically launched or restarted by the
Amazon EC2 Auto Scaling group. Using surplus credits prevents performance restrictions.

### Create a launch

template

You must use a _launch template_ for launching
instances as `unlimited` in an Amazon EC2 Auto Scaling group. A launch configuration does not
support launching instances as `unlimited`.

Console

###### To create a launch template that sets the credit specification

1. Follow the [Create a launch template using advanced settings](../../../autoscaling/ec2/userguide/advanced-settings-for-your-launch-template.md "../../../autoscaling/ec2/userguide/advanced-settings-for-your-launch-template.md") procedure
   in the _Amazon EC2 Auto Scaling User Guide_.
2. In **Launch template contents**, for
   **Instance type**, choose an instance size.
3. To launch instances as `unlimited` in an Amazon EC2 Auto Scaling group,
   under **Advanced details**, for **Credit
   specification**, choose
   **Unlimited**.
4. When you've finished defining the launch template parameters,
   choose **Create launch template**.

AWS CLI

###### To create a launch template that sets the credit specification

Use the [create-launch-template](../../../cli/latest/reference/ec2/create-launch-template.md "../../../cli/latest/reference/ec2/create-launch-template.md") command.

```
aws ec2 create-launch-template \
    --launch-template-name `my-launch-template` \
    --version-description `FirstVersion` \
    --launch-template-data CreditSpecification={CpuCredits=`unlimited`}
```

PowerShell

###### To create a launch template that sets the credit specification

Use the [New-EC2LaunchTemplate](../../../powershell/latest/reference/items/New-EC2LaunchTemplate.md "../../../powershell/latest/reference/items/New-EC2LaunchTemplate.md")
cmdlet. Define the credit specification for the launch template data as follows.

```
$creditSpec = New-Object Amazon.EC2.Model.CreditSpecificationRequest
$creditSpec.CpuCredits = "unlimited"
$launchTemplateData = New-Object Amazon.EC2.Model.RequestLaunchTemplateData
$launchTemplateData.CreditSpecification = $creditSpec

```

### Associate an Amazon EC2 Auto Scaling group with a launch template

To associate the launch template with an Amazon EC2 Auto Scaling group, create the Amazon EC2 Auto Scaling group using
the launch template, or add the launch template to an existing Amazon EC2 Auto Scaling group.

Console

###### To create an Amazon EC2 Auto Scaling group using a launch template

1. Open the Amazon EC2 console at
   [https://console.aws.amazon.com/ec2/](https://console.aws.amazon.com/ec2/ "https://console.aws.amazon.com/ec2/").
2. On the navigation bar at the top of the screen, select the same
   Region that you used when you created the launch template.
3. In the navigation pane, choose **Amazon EC2 Auto Scaling Groups**,
   **Create Amazon EC2 Auto Scaling group**.
4. Choose **Launch Template**, select your launch
   template, and then choose **Next Step**.
5. Complete the fields for the Amazon EC2 Auto Scaling group. When you've finished
   reviewing your configuration settings on the **Review
   page**, choose **Create Auto Scaling
   group**. For more information, see [Creating an Amazon EC2 Auto Scaling
   Group Using a Launch Template](../../../autoscaling/ec2/userguide/create-asg-launch-template.md "../../../autoscaling/ec2/userguide/create-asg-launch-template.md") in the
   _Amazon EC2 Auto Scaling User Guide_.

###### To add a launch template to an existing Amazon EC2 Auto Scaling group

1. Open the Amazon EC2 console at
   [https://console.aws.amazon.com/ec2/](https://console.aws.amazon.com/ec2/ "https://console.aws.amazon.com/ec2/").
2. On the navigation bar at the top of the screen, select the same
   Region that you used when you created the launch template.
3. In the navigation pane, choose **Amazon EC2 Auto Scaling
   Groups**.
4. From the Amazon EC2 Auto Scaling group list, select an Amazon EC2 Auto Scaling group, and choose
   **Actions**, **Edit**.
5. On the **Details** tab, for **Launch
   Template**, choose a launch template, and then choose
   **Save**.

AWS CLI

###### To create an Amazon EC2 Auto Scaling group using a launch template

Use the [create-auto-scaling-group](../../../cli/latest/reference/autoscaling/create-auto-scaling-group.md "../../../cli/latest/reference/autoscaling/create-auto-scaling-group.md") command and specify the
`--launch-template` parameter.

###### To add a launch template to an existing Amazon EC2 Auto Scaling group

Use the [update-auto-scaling-group](../../../cli/latest/reference/autoscaling/update-auto-scaling-group.md "../../../cli/latest/reference/autoscaling/update-auto-scaling-group.md") command and specify the
`--launch-template` parameter.

PowerShell

###### To create an Amazon EC2 Auto Scaling group using a launch template

Use the [New-ASAutoScalingGroup](../../../powershell/latest/reference/items/New-ASAutoScalingGroup.md "../../../powershell/latest/reference/items/New-ASAutoScalingGroup.md") cmdlet and specify the
`-LaunchTemplate_LaunchTemplateId` or
`-LaunchTemplate_LaunchTemplateName` parameter.

###### To add a launch template to an existing Amazon EC2 Auto Scaling group

Use the [Update-ASAutoScalingGroup](../../../powershell/latest/reference/items/Update-ASAutoScalingGroup.md "../../../powershell/latest/reference/items/Update-ASAutoScalingGroup.md") cmdlet and specify the
`-LaunchTemplate_LaunchTemplateId` or
`-LaunchTemplate_LaunchTemplateName` parameter.

## Manage the credit specification

of a burstable performance instance

You can switch the credit specification of a running or stopped T instance at any
time between `unlimited` and `standard`.

Note that in `unlimited` mode, an instance can spend surplus credits,
which might incur an additional charge. For more information, see [Surplus credits can incur
charges](burstable-performance-instances-unlimited-mode-concepts.md#unlimited-mode-surplus-credits "burstable-performance-instances-unlimited-mode-concepts.md#unlimited-mode-surplus-credits").

Console

###### To manage the credit specification of an instance

1. Open the Amazon EC2 console at
   [https://console.aws.amazon.com/ec2/](https://console.aws.amazon.com/ec2/ "https://console.aws.amazon.com/ec2/").
2. In the left navigation pane, choose
   **Instances**.
3. (Optional) Select an instance. On its **Details**
   tab, find **Credit specification**. The value is either
   `unlimited` or `standard`.
4. (Optional) To modify the credit specification for multiple
   instances at the same time, select them all.
5. Choose **Actions**, **Instance
   settings**, **Change credit specification**.
   This option is enabled only if you selected a T instance.
6. For **Unlimited mode**, select or clear the
   checkbox next to each instance ID.

AWS CLI

###### To get the credit specification of an instance

Use the [describe-instance-credit-specifications](../../../cli/latest/reference/ec2/describe-instance-credit-specifications.md "../../../cli/latest/reference/ec2/describe-instance-credit-specifications.md") command. If you do not
specify an instance ID, all instances with the credit
specification of `unlimited` are returned. The output would also
include instances that were previously configured with the `unlimited`
credit specification. For example, if you resize a T3 instance to an M4 instance,
while it is configured as `unlimited`, Amazon EC2 returns the M4
instance.

```
aws ec2 describe-instance-credit-specifications \
    --instance-id `i-1234567890abcdef0` \
    --query InstanceCreditSpecifications[].CpuCredits \
    --output text
```

The following is example output.

```
unlimited
```

###### To set the credit specification of an instance

Use the [modify-instance-credit-specification](../../../cli/latest/reference/ec2/modify-instance-credit-specification.md "../../../cli/latest/reference/ec2/modify-instance-credit-specification.md") command.

```
aws ec2 modify-instance-credit-specification \
    --region `us-east-1` \
    --instance-credit-specification "InstanceId=`i-1234567890abcdef0`,CpuCredits=`unlimited`"
```

PowerShell

###### To get the credit specification of an instance

Use the [Get-EC2CreditSpecification](../../../powershell/latest/reference/items/Get-EC2CreditSpecification.md "../../../powershell/latest/reference/items/Get-EC2CreditSpecification.md") cmdlet.

```
(Get-EC2CreditSpecification `
    -InstanceId `i-1234567890abcdef0`).CpuCredits
```

The following is example output.

```
unlimited
```

###### To set the credit specification of an instance

Use the [Edit-EC2InstanceCreditSpecification](../../../powershell/latest/reference/items/Edit-EC2InstanceCreditSpecification.md "../../../powershell/latest/reference/items/Edit-EC2InstanceCreditSpecification.md") cmdlet.

```
Edit-EC2InstanceCreditSpecification `
    -Region `us-east-1` `
    -InstanceCreditSpecification @({InstanceId="`i-1234567890abcdef0`" CpuCredits="unlimited"})
```

## Manage the default credit specification for an account

Each T instance family comes with a [default
credit specification](#default-credit-spec "#default-credit-spec"). You can change the default credit specification for each
T instance family at the account level per AWS Region. The valid values for the
default credit specification are `unlimited` and `standard`.

If you use the launch instance wizard in the EC2 console to launch instances, the
value you select for the credit specification overrides the account-level default credit
specification. If you use the AWS CLI to launch instances, all new T instances in the
account launch using the default credit specification. The credit specification for
existing running or stopped instances is not affected.

###### Consideration

The default credit specification for an instance family can be modified only once
in a rolling 5-minute period, and up to four times in a rolling 24-hour
period.

Console

###### To manage the default credit specification

1. Open the Amazon EC2 console at
   [https://console.aws.amazon.com/ec2/](https://console.aws.amazon.com/ec2/ "https://console.aws.amazon.com/ec2/").
2. To change the AWS Region, use the Region selector in the upper-right corner of the page.
3. On the left navigation pane, choose **EC2
   Dashboard**.
4. From **Account attributes**, choose **Default
   credit specification**.
5. Choose **Manage**.
6. For each instance family, choose **Unlimited** or
   **Standard**, and then choose
   **Update**.

AWS CLI

###### To get the default credit specification

Use the [get-default-credit-specification](../../../cli/latest/reference/ec2/get-default-credit-specification.md "../../../cli/latest/reference/ec2/get-default-credit-specification.md") command.

```
aws ec2 get-default-credit-specification \
    --region `us-east-1` \
    --instance-family `t2` \
    --query InstanceFamilyCreditSpecifications[].CpuCredits \
    --output text
```

The following is example output.

```
standard
```

###### To set the default credit specification

Use the [modify-default-credit-specification](../../../cli/latest/reference/ec2/modify-default-credit-specification.md "../../../cli/latest/reference/ec2/modify-default-credit-specification.md") command. The following
example sets the value to `unlimited`.

```
aws ec2 modify-default-credit-specification \
    --region `us-east-1` \
    --instance-family `t2` \
    --cpu-credits unlimited
```

PowerShell

###### To get the default credit specification

Use the [Get-EC2DefaultCreditSpecification](../../../powershell/latest/reference/items/Get-EC2DefaultCreditSpecification.md "../../../powershell/latest/reference/items/Get-EC2DefaultCreditSpecification.md") cmdlet.

```
(Get-EC2DefaultCreditSpecification `
    -Region `us-east-1` `
    -InstanceFamily `t2`).CpuCredits
```

The following is example output.

```
standard
```

###### To set the default credit specification

Use the [Edit-EC2DefaultCreditSpecification](../../../powershell/latest/reference/items/Edit-EC2DefaultCreditSpecification.md "../../../powershell/latest/reference/items/Edit-EC2DefaultCreditSpecification.md") cmdlet. The following
example sets the value to `unlimited`.

```
Edit-EC2DefaultCreditSpecification `
    -Region `us-east-1` `
    -InstanceFamily `t2` `
    -CpuCredit unlimited
```
