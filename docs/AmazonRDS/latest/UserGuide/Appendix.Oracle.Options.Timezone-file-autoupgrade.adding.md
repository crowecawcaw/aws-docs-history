

# Adding the time zone file autoupgrade option
<a name="Appendix.Oracle.Options.Timezone-file-autoupgrade.adding"></a>

When you add the option to an option group, the option group is in one of the following states:
+ An existing option group is currently attached to at least one DB instance. When you add the option, all DB instances that use this option group automatically restart. This causes a brief outage.
+ An existing option group is not attached to any DB instance. You plan to add the option and then associate the existing option group with existing DB instances or with a new DB instance.
+ You create a new option group and add the option. You plan to associate the new option group with existing DB instances or with a new DB instance.

## Console
<a name="Appendix.Oracle.Options.Timezone-file-autoupgrade.console"></a>

**To add the time zone file autoupgrade option to a DB instance**

1. Sign in to the AWS Management Console and open the Amazon RDS console at [https://console.aws.amazon.com/rds/](https://console.aws.amazon.com/rds/).

1. In the navigation pane, choose **Option groups**.

1. Determine the option group you want to use. You can create a new option group or use an existing option group. If you want to use an existing option group, skip to the next step. Otherwise, create a custom DB option group with the following settings: 

   1. For **Engine** choose the Oracle Database edition for your DB instance. 

   1. For **Major engine version** choose the version of your DB instance. 

   For more information, see [Creating an option group](USER_WorkingWithOptionGroups.md#USER_WorkingWithOptionGroups.Create). 

1. Choose the option group that you want to modify, and then choose **Add option**.

1. In the **Add option** window, do the following: 

   1. Choose **TIMEZONE\_FILE\_AUTOUPGRADE**.

   1. To enable the option on all associated DB instances as soon as you add it, for **Apply Immediately**, choose **Yes**. If you choose **No** (the default), the option is enabled for each associated DB instance during its next maintenance window.

1. When the settings are as you want them, choose **Add option**.

## AWS CLI
<a name="Appendix.Oracle.Options.Timezone-file-autoupgrade.CLI"></a>

The following example uses the AWS CLI [add-option-to-option-group](https://docs.aws.amazon.com/cli/latest/reference/rds/add-option-to-option-group.html) command to add the `TIMEZONE_FILE_AUTOUPGRADE` option to an option group called `myoptiongroup`.

For Linux, macOS, or Unix:

```
aws rds add-option-to-option-group \
    --option-group-name "{{myoptiongroup}}" \
    --options "{{OptionName=TIMEZONE_FILE_AUTOUPGRADE}}" \
    --apply-immediately
```

For Windows:

```
aws rds add-option-to-option-group ^
    --option-group-name "{{myoptiongroup}}" ^
    --options "{{OptionName=TIMEZONE_FILE_AUTOUPGRADE}}" ^
    --apply-immediately
```