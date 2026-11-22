

# Global shared delivery

Global shared delivery lets email that you send through shared IP addresses benefit from warmed shared IP addresses that Amazon SES operates across AWS Regions. For each message, SES prefers a shared IP address in the AWS Region that you send from. If it improves deliverability, SES might instead choose one with established sending history in another AWS Region. This gives your email better inbox placement and deliverability that scales with your sending. Your email is still accepted, processed, and logged in the AWS Region that you send from.

## Default setting
<a name="global-shared-delivery-default"></a>

Global shared delivery is enabled by default for accounts that start using Amazon SES in an AWS Region on or after November 19, 2026. For other accounts, it is disabled until you enable it. The setting applies to your account in the current Region.

You can also override the account setting for individual configuration sets.

## Enabling or disabling Global shared delivery for your account
<a name="global-shared-delivery-account"></a>

**To enable or disable Global shared delivery for your account using the Amazon SES console**

1. Sign in to the AWS Management Console and open the Amazon SES console at [https://console.aws.amazon.com/ses/](https://console.aws.amazon.com/ses/).

1. In the navigation pane, choose **Account dashboard**.

1. In the **Global shared delivery** pane, choose **Edit**.

1. Select or clear **Enable global shared delivery**.

1. Choose **Save changes**.

## Overriding Global shared delivery for a configuration set
<a name="global-shared-delivery-config-set"></a>

By default, a configuration set uses your account-level Global shared delivery setting. You can override it so that email sent with the configuration set always has Global shared delivery enabled, or always has it disabled.

**To override Global shared delivery for a configuration set using the Amazon SES console**

1. Sign in to the AWS Management Console and open the Amazon SES console at [https://console.aws.amazon.com/ses/](https://console.aws.amazon.com/ses/).

1. In the navigation pane, under **Configuration**, choose **Configuration sets**.

1. Choose the name of the configuration set.

1. In the **Global shared delivery** pane, choose **Edit**.

1. Choose one of the following:

   1. **Use account-level settings:** In **Global shared delivery settings**, clear the **Override account level settings** box.

   1. **Enable for this configuration set:** In **Global shared delivery settings**, select the **Override account level settings** box. Then select **Enable global shared delivery**.

   1. **Disable for this configuration set:** In **Global shared delivery settings**, select the **Override account level settings** box. Then clear **Enable global shared delivery**.

1. Choose **Save changes**.

You can set the same options when you create a configuration set, in the **Global shared delivery** section.

## Using the Amazon SES API
<a name="global-shared-delivery-api"></a>

To change the account-level setting, use the `PutAccountDeliveryAttributes` operation. To view it, use `GetAccount`. For a configuration set, set `SharedPoolDeliveryMode` in `DeliveryOptions` with `CreateConfigurationSet` or `PutConfigurationSetDeliveryOptions`.


| Console | `SharedPoolDeliveryMode` value | 
| --- | --- | 
| Enabled | GLOBAL | 
| Disabled | REGIONAL | 
| Use account-level settings (configuration sets only) | ACCOUNT | 

For more information, see [`PutAccountDeliveryAttributes`](https://docs.aws.amazon.com/ses/latest/APIReference-V2/API_PutAccountDeliveryAttributes.html) in the Amazon SES API v2 reference.