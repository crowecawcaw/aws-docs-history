

# Managing Notify configurations
<a name="notify-configurations"></a>

A Notify configuration is the central resource for Notify. It defines your display name, use case, enabled channels, enabled countries, and optional settings like a default template and associated phone pool.

## Configuration properties
<a name="notify-configurations-properties"></a>

Display name  
A name that identifies your brand. Alphanumeric characters, underscores, hyphens, and spaces are allowed. Maximum 15 characters. When you submit a display name, it is automatically reviewed for profanity, URLs, and other disallowed content. See [Display name review](#notify-configurations-brand-review).

Use case  
The messaging use case. Currently, `CODE_VERIFICATION` is supported.

Enabled channels  
The channels available for sending: `SMS`, `VOICE`, or both.

Enabled countries  
The countries you can send messages to. Available countries depend on your tier. See [Notify supported countries](notify-countries.md).

Default template  
(Optional) A template used when you send a message without specifying a template ID.

Associated pool  
(Optional) A phone pool containing your own origination identities. See [Using dedicated numbers with Notify](notify-dedicated-numbers.md).

Tier  
`BASIC` (default) or `ADVANCED`. See [Upgrading to Advanced tier](notify-tiers.md#notify-tier-upgrade).

Status  
The current status: `PENDING`, `ACTIVE`, `REJECTED`, or `REQUIRES_VERIFICATION`. You can send messages only when the status is `ACTIVE`.

Deletion protection  
When enabled, the configuration cannot be deleted until deletion protection is disabled.

Tags  
Key-value pairs for organizing and tracking your configurations. Maximum 50 tags per configuration.

## Display name review
<a name="notify-configurations-brand-review"></a>

When you create a Notify configuration, your display name is automatically reviewed for profanity, URLs, and other disallowed content. This review uses [Amazon Bedrock](https://docs.aws.amazon.com/bedrock/latest/userguide/what-is-bedrock.html), an AWS AI service, to evaluate the submitted display name.

If your display name is rejected, the configuration status is set to `REJECTED` and the `RejectionReason` field provides details. If you believe the rejection was made in error, you can create a support case in the [AWS Support Center](https://console.aws.amazon.com/support/home) to appeal the decision.

**Using a display name owned by another organization**  
If you are sending messages on behalf of another organization and want to use their brand name as your display name, you must provide a letter of authorization (LOA) from the brand owner. Download the [brand verification LOA template](samples/Notify_Brand_Verification_LetterOfAuthorization.zip), have the brand owner complete and sign it, and attach it to your support case or registration. The LOA must be dated within the last 30 days.

**Opting out of AI-assisted review**  
If you prefer not to have your display name evaluated via AI-assisted review, you can create a support case in the AWS Support Center and request that a Notify configuration be created manually on your behalf instead.

## Creating a Notify configuration
<a name="notify-configurations-create"></a>

------
#### [ Console ]

1. Open the AWS End User Messaging SMS console at [https://console.aws.amazon.com/sms-voice/](https://console.aws.amazon.com/sms-voice/).

1. In the navigation pane, under **Notify**, choose **Notify configurations**.

1. Choose **Create Notify configuration**.

1. For **Display name**, enter a name for your brand.

1. For **Use case**, choose **CODE\_VERIFICATION**.

1. Select the channels to enable (**SMS**, **VOICE**, or both).

1. (Optional) Expand **Advanced settings** to select countries, a default template, an associated pool, or enable deletion protection.

1. (Optional) Expand **Tags** to add tags.

1. Choose **Create Notify configuration**.

------
#### [ AWS CLI ]

Use the `create-notify-configuration` command:

```
aws pinpoint-sms-voice-v2 create-notify-configuration \
  --display-name "{{MyBrand}}" \
  --use-case CODE_VERIFICATION \
  --enabled-channels SMS VOICE \
  --enabled-countries US CA GB \
  --tags Key=Environment,Value=Production
```

------

## Viewing Notify configurations
<a name="notify-configurations-describe"></a>

------
#### [ Console ]

1. Open the AWS End User Messaging SMS console at [https://console.aws.amazon.com/sms-voice/](https://console.aws.amazon.com/sms-voice/).

1. In the navigation pane, under **Notify**, choose **Notify configurations**.

1. Use the property filter to filter by display name, status, tier, or other properties.

1. Choose a configuration's display name to view its details.

------
#### [ AWS CLI ]

List all configurations:

```
aws pinpoint-sms-voice-v2 describe-notify-configurations
```

Describe a specific configuration:

```
aws pinpoint-sms-voice-v2 describe-notify-configurations \
  --notify-configuration-ids {{nc-1234567890abcdef0}}
```

Filter by status:

```
aws pinpoint-sms-voice-v2 describe-notify-configurations \
  --filters Name=status,Values=ACTIVE
```

------

## Updating a Notify configuration
<a name="notify-configurations-update"></a>

You can update the enabled channels, enabled countries, default template, associated pool, and deletion protection settings.

------
#### [ Console ]

1. Open the AWS End User Messaging SMS console at [https://console.aws.amazon.com/sms-voice/](https://console.aws.amazon.com/sms-voice/).

1. Navigate to the Notify configuration you want to update.

1. Choose **Edit** to update channels, or use the individual tabs (Countries, Templates, Use Dedicated Numbers, Deletion protection) to update specific settings.

1. Make your changes and choose **Save**.

------
#### [ AWS CLI ]

Update enabled countries:

```
aws pinpoint-sms-voice-v2 update-notify-configuration \
  --notify-configuration-id {{nc-1234567890abcdef0}} \
  --enabled-countries US CA GB DE FR
```

Set a default template:

```
aws pinpoint-sms-voice-v2 update-notify-configuration \
  --notify-configuration-id {{nc-1234567890abcdef0}} \
  --default-template-id {{notify-code-verification-english-001}}
```

Clear the default template:

```
aws pinpoint-sms-voice-v2 update-notify-configuration \
  --notify-configuration-id {{nc-1234567890abcdef0}} \
  --default-template-id UNSET_DEFAULT_TEMPLATE
```

Associate a pool:

```
aws pinpoint-sms-voice-v2 update-notify-configuration \
  --notify-configuration-id {{nc-1234567890abcdef0}} \
  --pool-id {{pool-1234567890abcdef0}}
```

Disassociate a pool:

```
aws pinpoint-sms-voice-v2 update-notify-configuration \
  --notify-configuration-id {{nc-1234567890abcdef0}} \
  --pool-id UNSET_DEFAULT_POOL_FOR_NOTIFY
```

Enable deletion protection:

```
aws pinpoint-sms-voice-v2 update-notify-configuration \
  --notify-configuration-id {{nc-1234567890abcdef0}} \
  --deletion-protection-enabled
```

------

## Deleting a Notify configuration
<a name="notify-configurations-delete"></a>

**Note**  
If deletion protection is enabled, you must disable it before you can delete the configuration.

------
#### [ Console ]

1. Open the AWS End User Messaging SMS console at [https://console.aws.amazon.com/sms-voice/](https://console.aws.amazon.com/sms-voice/).

1. Navigate to **Notify configurations**.

1. Select the configuration you want to delete.

1. Choose **Delete**.

1. Type `delete` in the confirmation field and choose **Delete**.

------
#### [ AWS CLI ]

```
aws pinpoint-sms-voice-v2 delete-notify-configuration \
  --notify-configuration-id {{nc-1234567890abcdef0}}
```

------