

# Working with Notify templates
<a name="notify-templates"></a>

Notify templates are pre-approved, AWS-managed message templates for sending OTP and verification messages. Templates are pre-validated across supported countries. You select from available templates but cannot create or modify them.

## Template properties
<a name="notify-templates-properties"></a>

Template ID  
A unique identifier for the template.

Template type  
The use case category. Currently, `CODE_VERIFICATION` is available.

Channels  
The channels the template supports: `SMS`, `VOICE`, or both.

Language code  
The language of the template content (for example, `en`, `es`, `fr`).

Supported countries  
The countries where this template can be used.

Tier access  
Which tiers can use this template (`BASIC`, `ADVANCED`, or both).

Variables  
Placeholders in the template content that you provide values for at send time. Each variable has a name, type, and constraints. Variables with a source of `CUSTOMER` must be provided by you. Variables with a source of `SYSTEM` are populated automatically.

Content  
The message body with `{{variable}}` placeholders.

## Browsing templates
<a name="notify-templates-browse"></a>

------
#### [ Console ]

1. Open the AWS End User Messaging SMS console at [https://console.aws.amazon.com/sms-voice/](https://console.aws.amazon.com/sms-voice/).

1. Navigate to a Notify configuration and choose the **Templates** tab.

1. The **All templates** section shows all available templates. Use the property filter to filter by supported countries, language code, or other properties.

------
#### [ AWS CLI ]

List all templates:

```
aws pinpoint-sms-voice-v2 describe-notify-templates
```

Filter by template type:

```
aws pinpoint-sms-voice-v2 describe-notify-templates \
  --filters Name=template-type,Values=CODE_VERIFICATION
```

Filter by channel:

```
aws pinpoint-sms-voice-v2 describe-notify-templates \
  --filters Name=channels,Values=SMS
```

Filter by country:

```
aws pinpoint-sms-voice-v2 describe-notify-templates \
  --filters Name=supported-countries,Values=US
```

Filter by language:

```
aws pinpoint-sms-voice-v2 describe-notify-templates \
  --filters Name=language-code,Values=en
```

------

## Template variables
<a name="notify-templates-variables"></a>

Template variables are placeholders in the message content that are replaced with values you provide when sending a message. Each variable has the following metadata:
+ **Type** – The logical data type: `STRING`, `INTEGER`, or `BOOLEAN`. All values are passed as strings in the API, regardless of type. For example, pass an integer value as `"42"` and a boolean as `"true"`.
+ **Required** – Whether the variable must be provided. Required variables without a default value cause an error if omitted.
+ **Source** – Either `CUSTOMER` (you provide the value) or `SYSTEM` (automatically populated).
+ **Constraints** – Validation rules such as maximum length, minimum/maximum value, or a regex pattern.

## Setting a default template
<a name="notify-templates-default"></a>

You can set a default template on a Notify configuration. When you send a message without specifying a template ID, the default template is used. If no default template is set and no template ID is provided in the send request, the request fails.

To set or change the default template, see [Managing Notify configurations](notify-configurations.md).