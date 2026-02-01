• AWS Systems Manager Change Manager is no longer open to new customers. Existing customers can continue to use the service as normal. For more information, see
[AWS Systems Manager Change Manager availability change](change-manager-availability-change.md "change-manager-availability-change.md").

 

• The AWS Systems Manager CloudWatch Dashboard will no longer be available after April 30, 2026. Customers can continue to use Amazon CloudWatch console to view, create, and manage their Amazon CloudWatch dashboards, just as they do today. For more information, see
[Amazon CloudWatch Dashboard documentation](../../../AmazonCloudWatch/latest/monitoring/CloudWatch_Dashboards.md "../../../AmazonCloudWatch/latest/monitoring/CloudWatch_Dashboards.md").

# Setting an existing patch

baseline as the default

###### Important

Any default patch baseline selections you make here do not apply to
patching operations that are based on a patch policy. Patch policies use
their own patch baseline specifications. For more information about patch
policies, see [Patch policy configurations in Quick Setup](patch-manager-policies.md "patch-manager-policies.md").

When you create a custom patch baseline in Patch Manager, a tool in AWS Systems Manager, you
can set the baseline as the default for the associated operating system type as
soon as you create it. For information, see [Working with custom patch
baselines](patch-manager-manage-patch-baselines.md "patch-manager-manage-patch-baselines.md").

You can also set an existing patch baseline as the default for an operating
system type.

###### Note

The steps you follow depend on whether you first accessed Patch Manager before
or after the patch policies release on December 22, 2022. If you used
Patch Manager before that date, you can use the console procedure. Otherwise, use
the AWS CLI procedure. The **Actions** menu referenced in the
console procedure is not displayed in Regions where Patch Manager wasn't used
before the patch policies release.

###### To set a patch baseline as the default

1. Open the AWS Systems Manager console at [https://console.aws.amazon.com/systems-manager/](https://console.aws.amazon.com/systems-manager/ "https://console.aws.amazon.com/systems-manager/").
2. In the navigation pane, choose **Patch Manager**.
3. Choose the **Patch baselines** tab.
4. In the patch baselines list, choose the button of a patch baseline
   that isn't currently set as the default for an operating system
   type.

The **Default baseline** column indicates which
baselines are currently set as the defaults. 5. In the **Actions** menu, choose **Set default
patch baseline**.

###### Important

The **Actions** menu is not available if you
didn't work with Patch Manager in the current AWS account and Region
before December 22, 2022. See the **Note** earlier in this topic for more
information. 6. In the confirmation dialog box, choose **Set
default**.

###### To set a patch baseline as the default (AWS CLI)

1. Run the [describe-patch-baselines](../../../cli/latest/reference/ssm/describe-patch-baselines.md "../../../cli/latest/reference/ssm/describe-patch-baselines.md") command to view a list
   of available patch baselines and their IDs and Amazon Resource Names
   (ARNs).

```
aws ssm describe-patch-baselines
```

2. Run the [register-default-patch-baseline](../../../cli/latest/reference/ssm/register-default-patch-baseline.md "../../../cli/latest/reference/ssm/register-default-patch-baseline.md") command to set
   a baseline as the default for the operating system it's associated with.
   Replace `baseline-id-or-ARN` with the ID of the
   custom patch baseline or predefined baseline to use.

Linux & macOS

```
aws ssm register-default-patch-baseline \
    --baseline-id `baseline-id-or-ARN`
```

The following is an example of a setting a custom baseline
as the default.

```
aws ssm register-default-patch-baseline \
    --baseline-id pb-abc123cf9bEXAMPLE
```

The following is an example of a setting a predefined
baseline managed by AWS as the default.

```
aws ssm register-default-patch-baseline \
    --baseline-id arn:aws:ssm:us-east-2:733109147000:patchbaseline/pb-0574b43a65ea646e
```

Windows Server

```
aws ssm register-default-patch-baseline ^
    --baseline-id `baseline-id-or-ARN`
```

The following is an example of a setting a custom baseline
as the default.

```
aws ssm register-default-patch-baseline ^
    --baseline-id pb-abc123cf9bEXAMPLE
```

The following is an example of a setting a predefined
baseline managed by AWS as the default.

```
aws ssm register-default-patch-baseline ^
    --baseline-id arn:aws:ssm:us-east-2:733109147000:patchbaseline/pb-071da192df1226b63
```
