# Virtual Deliverability Manager settings

You can view or change Virtual Deliverability Manager settings in your account at any time. You can enable or
disable Virtual Deliverability Manager, and can specify an on or off mode for engagement tracking and optimized shared delivery at the Virtual Deliverability Manager account
level through the Amazon SES console or the AWS CLI

Virtual Deliverability Manager options are also provided at the configuration set level so you can define custom
settings for how a configuration set will use engagement tracking and optimized shared delivery by overriding how they’ve been
defined in Virtual Deliverability Manager. This gives you the flexibility to tailor your email sending for specific
email campaigns. For example, you can enable engagement tracking and optimized shared delivery for your marketing email and
disable them for your transactional email.

## Changing your Virtual Deliverability Manager account settings using the

Amazon SES console

The following procedure shows you how to change your Virtual Deliverability Manager account settings using the
Amazon SES console.

###### To change your Virtual Deliverability Manager account settings using

the
Amazon SES console

1. Sign in to the AWS Management Console and open the Amazon SES console at [https://console.aws.amazon.com/ses/](https://console.aws.amazon.com/ses/ "https://console.aws.amazon.com/ses/").
2. In the left navigation pane, choose **Settings** under
   **Virtual Deliverability Manager**.

The **Virtual Deliverability Manager settings** page opens. The **Subscription
overview** panel indicates the status of Virtual Deliverability Manager and the
**Additional settings** panel
indicates
the status of _Engagement tracking_ and _Optimized shared delivery_. 3. To change **Engagement tracking** or **Optimized shared delivery**
settings:

    1. In the **Additional settings** panel, choose
     **Edit**.
    2. Select
     the corresponding radio button to turn either feature on or off, and
     then choose **Submit settings**.


    The **Virtual Deliverability Manager settings** page shows a summary of your
     changes in the **Additional settings** panel.


    ###### Note

    *Engagement tracking* options that you define
     here or in Virtual Deliverability Manager's configuration set overrides, control whether or
     not to report opens and clicks in the Virtual Deliverability Manager dashboard; they do not
     affect event destination configurations that publish open and click
     events. For example, if you have engagement tracking disabled here,
     it will not disable the open and click event publishing you have set
     up in [SES event
     destinations](event-destinations-manage.md "event-destinations-manage.md").

4. (Optional) To define custom settings for how a configuration set uses engagement tracking and
   optimized shared delivery by overriding how they’re defined in Virtual Deliverability Manager, reference [Virtual Deliverability Manager options](creating-configuration-sets.md#vdm-create-config-overrides "creating-configuration-sets.md#vdm-create-config-overrides") while creating or
   editing a configuration set.
5. To disable Virtual Deliverability Manager:
   1. In the **Subscription overview** panel, choose
      **Disable Virtual Deliverability Manager**.
   2. In the **Disable Virtual Deliverability Manager?** pop-up window, enter
      `*Disable*` in the confirmation
      field, and then choose **Disable Virtual Deliverability Manager**.
   3. A banner appears, confirming that you've disabled Virtual Deliverability Manager.

6. To reenable Virtual Deliverability Manager, see [Getting started with Virtual Deliverability Manager](vdm-get-started.md "vdm-get-started.md").

## Changing your Virtual Deliverability Manager account settings using the

AWS CLI

You can change your Virtual Deliverability Manager account settings using the AWS CLI.

###### To change your Virtual Deliverability Manager account settings using the AWS CLI

You can use the [`PutAccountVdmAttributes`](../APIReference-V2/API_PutAccountVdmAttributes.md "../APIReference-V2/API_PutAccountVdmAttributes.md") and [`PutConfigurationSetVdmOptions`](../APIReference-V2/API_PutConfigurationSetVdmOptions.md "../APIReference-V2/API_PutConfigurationSetVdmOptions.md") operations in the Amazon SES
API v2 to change your Virtual Deliverability Manager settings. You can call this operation from the AWS CLI, as
shown in the following examples.

- Enable or disable engagement tracking, optimized shared delivery, or both using an input file:

```
aws --region us-east-1 sesv2 put-account-vdm-attributes --cli-input-json file://attributes.json
```

In this example, where engagement tracking is `ENABLED` and optimized shared delivery is
`DISABLED`, the input file looks similar to this:

```
{
    "VdmAttributes": {
        "VdmEnabled": "ENABLED",
        "DashboardAttributes": {
            "EngagementMetrics": "ENABLED"
        },
        "GuardianAttributes": {
            "OptimizedSharedDelivery": "DISABLED"
        }
    }
}
```

You
can find more information about parameter values and related data
typesby linking from the [`VdmAttributes`](../APIReference-V2/API_VdmAttributes.md "../APIReference-V2/API_VdmAttributes.md") data type in the Amazon SES API v2
reference.

- Define custom settings for how a configuration set will use engagement tracking and optimized shared delivery by
  overriding how they’ve been defined in Virtual Deliverability Manager:

```
aws --region us-east-1 sesv2 put-configuration-set-vdm-options --cli-input-json file://config-set.json
```

In this example, where a configuration set named _example_
has both engagement tracking and optimized shared delivery enabled, the input file looks similar to this:

```
{
    "ConfigurationSetName": "example",
    "VdmOptions": {
        "DashboardOptions": {
            "EngagementMetrics": "ENABLED"
        },
        "GuardianOptions": {
            "OptimizedSharedDelivery": "ENABLED"
        }
    }
}
```

For more information about parameter values and related data types, see the
[`VdmOptions`](../APIReference-V2/API_VdmOptions.md "../APIReference-V2/API_VdmOptions.md") data type in the Amazon SES API v2
reference.

- To verify the outcome:

```
aws —region us-east-1 sesv2 get-configuration-set —configuration-set-name example
```

- Not specifying [`DashboardOptions`](../APIReference-V2/API_DashboardOptions.md "../APIReference-V2/API_DashboardOptions.md") or [`GuardianOptions`](../APIReference-V2/API_GuardianOptions.md "../APIReference-V2/API_GuardianOptions.md") options at the configuration set level
  results in your Virtual Deliverability Manager account-level settings applying to traffic sent through
  that configuration set.
