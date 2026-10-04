

# Step 2: Create a Notify configuration
<a name="nx-notify-get-set-up-create"></a>

A Notify configuration is the central resource for Notify, and both sending modes require one. It represents your brand identity and messaging settings, including your display name, use case, enabled channels, enabled countries, and tier. When you create a configuration, AWS automatically validates your account, configures fraud protection, and sets tier-appropriate limits.

------
#### [ Console ]

**To create a Notify configuration**

1. Open the AWS End User Messaging console at [https://console.aws.amazon.com/end-user-messaging/](https://console.aws.amazon.com/end-user-messaging/).

1. In the navigation pane, under **Notify**, choose **Notify configurations**.

1. Choose **Create Notify configuration**.

1. For **Display name**, enter your brand name, for example `AcmeCorp`. The display name can be up to 15 characters and is automatically reviewed for profanity, URLs, and other disallowed content.

1. For **Use case**, **Code verification** is automatically selected.

1. For **Channels**, select **SMS**, **VOICE**, or both.

1. (Optional) Expand **Advanced settings** to select countries, a default template, an associated pool, or to enable deletion protection.

1. Choose **Create Notify configuration**.

Your configuration is created in **Pending** status while the system validates your account. Most configurations are activated within seconds. When the status changes to **Active**, you can start sending messages. If your brand name requires additional review, the status is **Requires verification**.

------
#### [ AWS CLI ]

Use the `create-notify-configuration` command in the `sms-voice` namespace:

```
$ aws pinpoint-sms-voice-v2 create-notify-configuration \
    --display-name "{{AcmeCorp}}" \
    --use-case CODE_VERIFICATION \
    --enabled-channels SMS
```

------

A configuration moves through the following statuses. You can send messages only when the status is `ACTIVE`.


| Status | Description | 
| --- | --- | 
| PENDING | The configuration is being validated. | 
| ACTIVE | The configuration is ready to send messages. | 
| REQUIRES\_VERIFICATION | The brand name requires verification before activation. | 
| REJECTED | The configuration was rejected. Check the RejectionReason field for details. | 

Notify messages are built from pre-approved, AWS-managed templates for OTP and verification, pre-validated across supported countries with multi-language support. You select from the available templates but cannot create or modify them. Each template has an ID, a type (such as `CODE_VERIFICATION`), the channels it supports, a language code, the countries it supports, and the tiers that can use it. A template also declares variables: placeholders you provide values for at send time. Variables with a source of `CUSTOMER` you supply; variables with a source of `SYSTEM` are populated automatically.

Browse the templates available for your tier and channel on the **Templates** tab of a Notify configuration, or with the `describe-notify-templates` command. The default template you set here is used whenever you send without specifying a template ID; if no default is set and none is provided in the send request, the request fails.

```
$ aws pinpoint-sms-voice-v2 describe-notify-templates \
    --filters '[{"Name":"channels","Values":["SMS"]},{"Name":"tier-access","Values":["BASIC"]}]'
```

You can update the enabled channels, enabled countries, default template, associated pool, and deletion protection settings at any time by choosing **Edit** on the configuration or by using the `update-notify-configuration` command. To delete a configuration, first disable deletion protection if it is enabled.