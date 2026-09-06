# Using configuration overrides in Amazon SES

Most settings that control how Amazon SES processes your email are defined before you send
it, at the account level or in a configuration set. That works well for settings that are
stable across a mail stream, but not for settings that change from one recipient to the next.
For example, tracking consent is one such setting: whether a recipient has agreed to open and
click tracking is a decision that belongs to the recipient, not to your account.

_Configuration overrides_ let you change selected settings for a single
email sending request, without creating a separate configuration set for every combination of
settings you need. You specify them in the `ConfigurationOverrides` parameter of
the [`SendEmail`](../APIReference-V2/API_SendEmail.md "../APIReference-V2/API_SendEmail.md") and [`SendBulkEmail`](../APIReference-V2/API_SendBulkEmail.md "../APIReference-V2/API_SendBulkEmail.md")
operations. An override applies only to the messages in the request that contains it, and it
never changes your account-level settings or the configuration set that the request
uses.

## What are configuration overrides?

A configuration override is a set of values that take precedence, for one request only,
over the values that otherwise apply to the messages in that request. Each member of the
`ConfigurationOverrides` parameter is a category of settings that you can
override. You include only the categories that you want to change, and settings that you
don't override keep the values that your account-level and configuration set settings
define.

Key benefits of using configuration overrides include:

- Changing a setting for a single request, without maintaining a separate
  configuration set for every combination of settings that you need.
- Keeping a single configuration set per mail stream, rather than one for every
  combination of sending domain, dedicated IP pool, event destination, and the
  settings that change from one request to the next.

###### Note

Configuration overrides apply to the whole request. In a
`SendBulkEmail` request, the override applies to every entry in the
request. To send with different settings, group your recipients by the setting that
you want to override and send one request per group.

SES supports the following override categories:

| Category   | Settings that you can override                                                                                                        |
| ---------- | ------------------------------------------------------------------------------------------------------------------------------------- |
| `Tracking` | Open and click tracking for the messages in the request, through<br>the `OpenTrackingEnabled` and<br>`ClickTrackingEnabled` settings. |

## How tracking overrides work

Common uses of tracking overrides include:

- Honoring per-recipient tracking consent, including requirements such as GDPR
  and the CNIL guidance on tracking pixels, without maintaining one configuration
  set per consent state.
- Suppressing tracking for individual messages, for example, a transactional
  receipt sent from a configuration set that otherwise has tracking
  enabled.

To understand what a tracking override changes, it helps to know which settings control
tracking in the absence of one. Without an override, open and click tracking are enabled
when either of the following is true:

- The configuration set that the message uses has an event destination whose
  `MatchingEventTypes` include the `OPEN` or
  `CLICK` event types. For more information, see [Monitor email sending using Amazon SES event publishing](monitor-using-event-publishing.md "monitor-using-event-publishing.md").
- Engagement metrics are enabled for Virtual Deliverability Manager, either through the
  `EngagementMetrics` setting of the configuration set, which you
  configure using the [`PutConfigurationSetVdmOptions`](../APIReference-V2/API_PutConfigurationSetVdmOptions.md "../APIReference-V2/API_PutConfigurationSetVdmOptions.md") operation, or through
  your account-level `EngagementMetrics` setting, which you configure
  using the [`PutAccountVdmAttributes`](../APIReference-V2/API_PutAccountVdmAttributes.md "../APIReference-V2/API_PutAccountVdmAttributes.md") operation. The
  configuration set setting takes precedence over the account-level
  setting.

When you provide an override, SES uses it in place of the default behavior
described above. Each tracking type is resolved on its own, so you can override one and
inherit the other. The following table describes each value.

| Value         | Behavior                                                                                                                                                                                                                                                                                                                                         |
| ------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| `DISABLED`    | SES doesn't track the message, even when your account-level<br>or configuration set settings enable tracking. For open tracking,<br>SES doesn't add the tracking image to the message, and removes<br>the `{{ses:openTracker}}` placeholder if the message<br>contains one. For click tracking, SES doesn't rewrite the<br>links in the message. |
| `ENABLED`     | SES tracks the message, even when your account-level and<br>configuration set settings don't enable tracking.                                                                                                                                                                                                                                    |
| Not specified | SES uses the tracking setting that otherwise applies to<br>the message.                                                                                                                                                                                                                                                                          |

###### Note

Enabling open or click tracking with an override doesn't create an event
destination. SES records the resulting open and click events in Virtual Deliverability Manager, where
you can review them using Virtual Deliverability Manager metrics and Message Insights. To also receive these
events at a destination that you own, the configuration set that the message uses
must have an event destination that publishes open and click events.

###### Note

An override can enable tracking only for a message that SES is already
configured to publish events for. If the configuration set that the message uses has
no event destination, and engagement metrics aren't enabled for Virtual Deliverability Manager, setting
`OpenTrackingEnabled` or `ClickTrackingEnabled` to
`ENABLED` has no effect, and SES sends the message without
returning an error. To enable tracking with an override, the configuration set must
have an event destination that matches at least one event type, or the other tracking
type must already be enabled for the message.

An override changes only the tracking behavior of the messages in the request. It
doesn't modify the configuration set, and a subsequent request that uses the same
configuration set without an override behaves as it did before.

## IAM permissions for tracking overrides

Because a tracking override changes tracking behavior at send time, SES
authorizes it separately from the send itself. A request that contains a
`Tracking` override requires both of the following:

- Permission to send the email, such as `ses:SendEmail` or
  `ses:SendBulkEmail` on the identity and configuration set that the
  request uses.
- Permission for the `ses:ApplyTrackingConfigurationOverrides` action.
  This action has no SES resource of its own, so you must grant it on
  `"Resource": "*"`.

If a principal is allowed to send but not allowed to apply tracking overrides,
SES returns an `AccessDeniedException` and doesn't send the message.
Requests that don't contain `ConfigurationOverrides` are unaffected, so adding
this action doesn't change the behavior of your existing sending
permissions.

The following policy allows a principal to send email and to apply any tracking
override:

```
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Sid": "AllowSend",
      "Effect": "Allow",
      "Action": [
        "ses:SendEmail",
        "ses:SendBulkEmail"
      ],
      "Resource": [
        "arn:aws:ses:`us-east-1`:`111122223333`:identity/`example.com`",
        "arn:aws:ses:`us-east-1`:`111122223333`:configuration-set/`my-configuration-set`"
      ]
    },
    {
      "Sid": "AllowTrackingOverrides",
      "Effect": "Allow",
      "Action": "ses:ApplyTrackingConfigurationOverrides",
      "Resource": "*"
    }
  ]
}
```

Make the following changes to the preceding policy example:

- Replace `us-east-1` with the AWS Region that you
  send from.
- Replace `111122223333` with your AWS
  account ID.
- Replace `example.com` and
  `my-configuration-set` with the identity and
  configuration set that you send with.

### Limiting which tracking overrides a principal can request

To allow some tracking overrides but not others, use the following condition keys
with the `ses:ApplyTrackingConfigurationOverrides` action. Each key
carries the value that the request supplied.

- `ses:OpenTrackingEnabled`
- `ses:ClickTrackingEnabled`

The following policy allows a principal to disable tracking, but not enable
it:

```
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Sid": "AllowDisablingTrackingOnly",
      "Effect": "Allow",
      "Action": "ses:ApplyTrackingConfigurationOverrides",
      "Resource": "*",
      "Condition": {
        "StringEquals": {
          "ses:OpenTrackingEnabled": "DISABLED",
          "ses:ClickTrackingEnabled": "DISABLED"
        }
      }
    }
  ]
}
```

###### Important

Only the tracking values that a request actually supplies are present in the
request context. Because the preceding policy conditions on both keys, it allows
a request that sets both `OpenTrackingEnabled` and
`ClickTrackingEnabled` to `DISABLED`, but denies a
request that sets only one of them. To allow a request that overrides either
tracking type on its own, write a separate statement for each key, or use the
`Null` condition operator to account for a key that isn't
present.

The following statements deny enabling either tracking type, while still allowing a
request to override one tracking type on its own. Because each key is always either
`ENABLED` or `DISABLED`, matching `ENABLED` is
enough to deny enabling tracking. Grant the sending permissions separately, scoped
to the identity and configuration set that the request uses, as shown in the previous
policy example:

```
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Sid": "AllowTrackingOverrides",
      "Effect": "Allow",
      "Action": "ses:ApplyTrackingConfigurationOverrides",
      "Resource": "*"
    },
    {
      "Sid": "DenyEnablingOpenTracking",
      "Effect": "Deny",
      "Action": "ses:ApplyTrackingConfigurationOverrides",
      "Resource": "*",
      "Condition": {
        "StringEquals": {
          "ses:OpenTrackingEnabled": "ENABLED"
        }
      }
    },
    {
      "Sid": "DenyEnablingClickTracking",
      "Effect": "Deny",
      "Action": "ses:ApplyTrackingConfigurationOverrides",
      "Resource": "*",
      "Condition": {
        "StringEquals": {
          "ses:ClickTrackingEnabled": "ENABLED"
        }
      }
    }
  ]
}
```

Each tracking type needs its own statement, because multiple keys in a single
condition block are combined with AND. With these statements:

- A request that sets only `ClickTrackingEnabled` to
  `DISABLED` is authorized to apply the override.
  `StringEquals` doesn't match a key that isn't present, so the
  open tracking `Deny` doesn't apply.
- A request that sets either tracking type to `ENABLED` is
  denied.
- A request that contains no `ConfigurationOverrides` is
  unaffected, because SES doesn't authorize the override action for
  it.

To match on whether an override is present in the request at all, use the
`Null` condition operator. A value of `false` means "the key
is present in the request." The following statement grants the override action only to
requests that state an open tracking preference explicitly:

```
{
  "Sid": "AllowTrackingOverridesOnlyWhenOpenTrackingIsSpecified",
  "Effect": "Allow",
  "Action": "ses:ApplyTrackingConfigurationOverrides",
  "Resource": "*",
  "Condition": {
    "Null": {
      "ses:OpenTrackingEnabled": "false"
    }
  }
}
```

A request that overrides only click tracking doesn't satisfy this condition, so it
isn't granted the override action. Use a value of `true` to match the
opposite case, where the key isn't present in the request.

## Using tracking overrides

To override tracking for a request, add the `Tracking` member of the
`ConfigurationOverrides` parameter to your send request. The following
example uses the AWS CLI to send a message with both open and click tracking disabled, from
a configuration set that has tracking enabled:

```
aws sesv2 send-email \
    --from-email-address "sender@example.com" \
    --destination "ToAddresses=recipient@example.com" \
    --content "Simple={Subject={Data=Test email,Charset=UTF-8},Body={Html={Data=<html><body><p>Hello</p></body></html>,Charset=UTF-8}}}" \
    --configuration-set-name `my-configuration-set` \
    --configuration-overrides '{"Tracking":{"OpenTrackingEnabled":"DISABLED","ClickTrackingEnabled":"DISABLED"}}'
```

You can override one tracking type and inherit the other. The following example
disables click tracking while leaving open tracking as the configuration set defines
it:

```
--configuration-overrides '{"Tracking":{"ClickTrackingEnabled":"DISABLED"}}'
```

The same parameter applies to `SendBulkEmail`, where the override applies to
every entry in the request:

```
aws sesv2 send-bulk-email \
    --from-email-address "sender@example.com" \
    --default-content '{"Template":{"TemplateName":"`my-template`","TemplateData":"{}"}}' \
    --bulk-email-entries '[{"Destination":{"ToAddresses":["recipient1@example.com"]}},{"Destination":{"ToAddresses":["recipient2@example.com"]}}]' \
    --configuration-set-name `my-configuration-set` \
    --configuration-overrides '{"Tracking":{"OpenTrackingEnabled":"DISABLED","ClickTrackingEnabled":"DISABLED"}}'
```

In the preceding examples, replace
`my-configuration-set` and
`my-template` with the names of your configuration set and
email template, and replace the sender and recipient addresses with your own.

## Effect of tracking overrides on events and metrics

When an override disables tracking for a message, SES doesn't generate open or
click events for it, so no `Open` or `Click` events are published to
the event destinations of the configuration set for that message. Other event types, such
as `Send`, `Delivery`, and `Bounce`, are
unaffected.

Delivery, bounce, and complaint reporting are not affected by tracking overrides, so
you can continue to monitor the deliverability of messages that you send without
tracking.

## Best practices and considerations

- Treat the override as the expression of a recipient's consent, and derive it
  from the consent state that you store for that recipient rather than hard-coding
  it per mail stream.
- Group recipients by tracking preference and send one request per group. An
  override applies to every message in the request.
- Keep your configuration sets organized around settings that are stable for a
  mail stream, such as the dedicated IP pool, event destinations, and the custom
  domain used for tracking. Use overrides for the settings that change per
  recipient.
- Use the `ses:OpenTrackingEnabled` and
  `ses:ClickTrackingEnabled` condition keys to constrain what a
  principal can request. For example, an application that only ever suppresses
  tracking doesn't need permission to enable it.
- To disable click tracking for specific links rather than for a whole message,
  use the `ses:no-track` attribute instead. For more information, see
  [Q2. Can I disable click tracking?](faqs-metrics.md#sending-metric-faqs-clicks-q2 "faqs-metrics.md#sending-metric-faqs-clicks-q2").
