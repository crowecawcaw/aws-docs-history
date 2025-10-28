# Using templates to send personalized email

with the Amazon SES API

In Amazon SES you can send templated email either by using a _stored
template_ or by using an _inline template_.

- Stored template – Refers to the [`Template`](../APIReference-V2/API_Template.md "../APIReference-V2/API_Template.md") resource
  that is created and saved in SES by using the
  `CreateEmailTemplate` operation in the Amazon SES v2 API. The template
  contains the subject and body of the email containing variables (placeholders)
  inline with the written content. The name of the stored template and the dynamic
  data to the placeholder variables in the template are provided when calling either
  the `SendEmail` or `SendBulkEmail` v2 API
  operations.

_Stored templates_ can be easily reused and can save you time
and effort when sending similar types of emails. Instead of creating each email from
scratch, you only need to create the base structure and design once, then simply
update the dynamic content within the template.

- Inline template – The `Template`
  resource is not used, but rather, the subject and body of the email containing
  variables (placeholders) inline with the written content
  along with the values for those
  placeholder variables are provided when calling either the `SendEmail` or
  `SendBulkEmail` v2 API operations.

_Inline templates_ streamline the process for sending bulk
email by eliminating the need to manage template resources in your SES account and
simplify the integration process by allowing you to include template content
directly within your application logic. They do not count against the
20,000-template limit per AWS Region.
The following limits apply when using _stored templates_:

- You can create up to 20,000 email templates in each AWS Region.
- Each template can be up to 500 KB in size, including both the text and HTML
  parts.
  The following limit applies when using _inline templates_:

- Each input JSON file can be up to 1 MB in size, including both the text and HTML
  parts.
  The following applies to both _stored_ and _inline
  templates_:

- There are no limits to the number of replacement variables that can be
  used.
- You can send email to up to 50 destination objects in each call to the
  `SendBulkEmail` operation. The [`Destination`](../APIReference-V2/API_Destination.md "../APIReference-V2/API_Destination.md")
  object can contain multiple recipients defined in **ToAddresses**,
  **CcAddresses**, and **BccAddresses**. The
  number of destinations you can contact in a single call to the v2 API may be limited
  by your account's maximum sending rate. For more information, see [Managing your Amazon SES sending limits](manage-sending-quotas.md "manage-sending-quotas.md").
  This chapter includes procedures with examples for using both _stored
  templates_ and _inline templates_.

###### Note

The procedures in this section assume that you've already installed and configured the
AWS CLI. For more information about installing and configuring the AWS CLI, see the [AWS Command Line Interface User Guide](../../../cli/latest/userguide.md "../../../cli/latest/userguide.md").

## (Optional) Part 1: Set up

Rendering Failure event notifications

If you send an email that contains invalid personalization content, Amazon SES might
accept the message, but won't be able to deliver it. For this reason, if you plan to
send personalized email, you should configure SES to send Rendering Failure event
notifications through Amazon SNS. When you receive a Rendering Failure event notification,
you can identify which message contained the invalid content, fix the issues, and send
the message again.

The procedure in this section is optional, but highly recommended.

###### To configure Rendering Failure event notifications

1. Create an Amazon SNS topic. For procedures, see [Create a
   Topic](../../../sns/latest/dg/sns-create-subscribe-endpoint-to-topic.md "../../../sns/latest/dg/sns-create-subscribe-endpoint-to-topic.md") in the _Amazon Simple Notification Service Developer Guide_.
2. Subscribe to the Amazon SNS topic. For example, if you want to receive Rendering
   Failure notifications by email, subscribe an email endpoint (that is, your email
   address) to the topic.

For procedures, see [Subscribe to
a Topic](../../../sns/latest/dg/SubscribeTopic.md "../../../sns/latest/dg/SubscribeTopic.md") in the _Amazon Simple Notification Service Developer Guide_. 3. Complete the procedures in [Set up an Amazon SNS event
destination for event publishing](event-publishing-add-event-destination-sns.md "event-publishing-add-event-destination-sns.md") to set up your
configuration sets to publish Rendering Failure events to your Amazon SNS
topic.

## (Optional) Part 2: Create an

email template

If you intend on using a _stored template_, this section will show
you how to use the [`CreateEmailTemplate`](../APIReference-V2/API_CreateEmailTemplate.md "../APIReference-V2/API_CreateEmailTemplate.md") SES v2 API operation to create
the template. You can skip this step if you want to use an _inline
template_.

This procedure assumes that you've already installed and configured the AWS CLI. For
more information about installing and configuring the AWS CLI, see the [AWS Command Line Interface User Guide](../../../cli/latest/userguide.md "../../../cli/latest/userguide.md").

###### To create the template

1. In a text editor, create a new file and paste the following code customizing
   it as you need.

```
{
    "TemplateName": "MyTemplate",
    "TemplateContent": {
        "Subject": "Greetings, {{name}}!",
        "Text": "Dear {{name}},\r\nYour favorite animal is {{favoriteanimal}}.",
        "Html": "<h1>Hello {{name}},</h1><p>Your favorite animal is {{favoriteanimal}}.</p>"
    }
}
```

This code contains the following properties:

    * TemplateName – The name of the
     `Template` resource. When you send the email, you refer
     to this name.
    * TemplateContent – A container for
     the following attributes:




    	+ Subject – The subject
    	 line of the email. This property may contain replacement tags.
    	 These tags use the following format: `{{tagname}}`.
    	 When you send the email, you can specify a value for
    	 `tagname` for each destination.
    	+ Html – The HTML body of
    	 the email. This property may contain replacement tags. The
    	 preceding example includes two tags: `{{name}}` and
    	 `{{favoriteanimal}}`.
    	+ Text – The text body of
    	 the email. Recipients whose email clients don't display HTML
    	 content will see this version of the email. This property may
    	 also contain replacement tags.

2. Customize the preceding example to fit your needs, and then save the file as
   `mytemplate.json`.
3. At the command line, type the following command to create a new template using
   the [`CreateEmailTemplate`](../APIReference-V2/API_CreateEmailTemplate.md "../APIReference-V2/API_CreateEmailTemplate.md") v2 API operation:

```
aws sesv2 create-email-template --cli-input-json file://`mytemplate.json`
```

## Part 3: Sending the

personalized email

You can use the following two SES v2 API operations to send emails using either
_stored templates_ or _inline
templates_:

- The [`SendEmail`](../APIReference-V2/API_SendEmail.md "../APIReference-V2/API_SendEmail.md") operation is useful for sending a customized
  email to a single destination object. The v2 API [`Destination`](../APIReference-V2/API_Destination.md "../APIReference-V2/API_Destination.md")
  object can contain the _ToAddresses_,
  _CcAddresses_, and _BccAddresses_
  properties. These can be used in any combination and can contain one or more
  email addresses that will receive the same email.
- The [`SendBulkEmail`](../APIReference-V2/API_SendBulkEmail.md "../APIReference-V2/API_SendBulkEmail.md") operation is useful for sending
  unique emails to multiple destination objects in a single call to the v2
  API.

This section provides examples of how to use the AWS CLI to send templated email using
both of these send operations.

### Sending templated email to

a single destination object

You can use the [`SendEmail`](../APIReference-V2/API_SendEmail.md "../APIReference-V2/API_SendEmail.md") operation to send an email to one or more
recipients defined in a single destination object. All of the recipients in the
[`Destination`](../APIReference-V2/API_Destination.md "../APIReference-V2/API_Destination.md") object will receive the same email.

###### To send a templated email to a single destination object

1. Depending on whether you want to use a _stored
   template_ or _inline template_, select the
   respective code example to paste into a text editor, customizing it as you
   need.

Stored template code example
Notice that the template you created in the previous step,
_MyTemplate_, is being referenced as the
value for the `TemplateName` parameter.

```
{
    "FromEmailAddress": "Mary Major <mary.major@example.com>",
    "Destination": {
        "ToAddresses": [
            "alejandro.rosalez@example.com", "jimmy.jet@example.com"
        ]
    },
    "Content": {
        "Template": {
            "TemplateName": "MyTemplate",
            "TemplateData": "{ \"name\":\"Alejandro\", \"favoriteanimal\": \"alligator\" }"
        }
    },
    "ConfigurationSetName": "ConfigSet"
}
```

This code contains the following properties:

    * FromEmailAddress
     – The email address of the sender.
    * Destination – An
     object containing the email recipients defined in the
     *ToAddresses*,
     *CcAddresses*, and
     *BccAddresses* properties. These
     can be used in any combination and can contain one or
     more email addresses that will receive the same
     email.
    * TemplateName –
     The name of the `Template` resource to apply
     to the email.
    * TemplateData – An
     escaped JSON string that contains key-value pairs. The
     keys correspond to the variables defined in the
     `TemplateContent` properties in the
     stored template, for example, `{{name}}`. The
     values represent the content that replaces the
     variables.
    * ConfigurationSetName
     – The name of the configuration set to use when
     sending the email.


    ###### Note

    We recommend that you use a configuration set that
     is configured to publish Rendering Failure events to
     Amazon SNS. For more information, see [(Optional) Part 1: Set up
     Rendering Failure event notifications](#send-personalized-email-set-up-notifications "#send-personalized-email-set-up-notifications").

Inline template code example
Notice that the `TemplateContent` properties (that
would normally be defined in a _stored
template_), are being defined
_inline_ along with the
`TemplateData` property which makes this an
_inline template_.

```
{
    "FromEmailAddress": "Mary Major <mary.major@example.com>",
    "Destination": {
        "ToAddresses": [
            "alejandro.rosalez@example.com", "jimmy.jet@example.com"
        ]
    },
    "Content": {
        "Template": {
            "TemplateContent": {
                "Subject": "Greetings, {{name}}!",
                "Text": "Dear {{name}},\r\nYour favorite animal is {{favoriteanimal}}.",
                "Html": "<h1>Hello {{name}},</h1><p>Your favorite animal is {{favoriteanimal}}.</p>"
            },
            "TemplateData": "{ \"name\":\"Alejandro\", \"favoriteanimal\": \"alligator\" }"
        }
    },
    "ConfigurationSetName": "ConfigSet"
}
```

This code contains the following properties:

    * FromEmailAddress
     – The email address of the sender.
    * Destination – An
     object containing the email recipients defined in the
     *ToAddresses*,
     *CcAddresses*, and
     *BccAddresses* properties. These
     can be used in any combination and can contain one or
     more email addresses that will receive the same
     email.
    * TemplateContent –
     A container for the following attributes:




    	+ Subject –
    	 The subject line of the email. This property may
    	 contain replacement tags. These tags use the
    	 following format: `{{tagname}}`. When
    	 you send the email, you can specify a value for
    	 `tagname` for each destination.
    	+ Html –
    	 The HTML body of the email. This property may
    	 contain replacement tags. The preceding example
    	 includes two tags: `{{name}}` and
    	 `{{favoriteanimal}}`.
    	+ Text –
    	 The text body of the email. Recipients whose email
    	 clients don't display HTML content will see this
    	 version of the email. This property may also
    	 contain replacement tags.
    * TemplateData – An
     escaped JSON string that contains key-value pairs. The
     keys correspond to the variables defined in the
     `TemplateContent` properties in this
     file, for example, `{{name}}`. The values
     represent the content that replaces the
     variables.
    * ConfigurationSetName
     – The name of the configuration set to use when
     sending the email.


    ###### Note

    We recommend that you use a configuration set that
     is configured to publish Rendering Failure events to
     Amazon SNS. For more information, see [(Optional) Part 1: Set up
     Rendering Failure event notifications](#send-personalized-email-set-up-notifications "#send-personalized-email-set-up-notifications").

2. Customize the preceding example to fit your needs, and then save the file
   as `myemail.json`.
3. At the command line, type the following v2 API command to send the
   email:

```
aws sesv2 send-email --cli-input-json file://`myemail.json`
```

### Sending templated email

to multiple destination objects

You can use the [`SendBulkEmail`](../APIReference-V2/API_SendBulkEmail.md "../APIReference-V2/API_SendBulkEmail.md") operation to send an email to multiple
destination objects in a single call to the SES v2 API. SES sends a
unique email to the recipient or recipients in each [`Destination`](../APIReference-V2/API_Destination.md "../APIReference-V2/API_Destination.md")
object.

###### To send a templated email to multiple destination objects

1. Depending on whether you want to use a _stored
   template_ or _inline template_, select the
   respective code example to paste into a text editor, customizing it as you
   need.

Stored template code example
Notice that the template you created in the previous step,
_MyTemplate_, is being referenced as the
value for the `TemplateName` parameter.

```
{
    "FromEmailAddress": "Mary Major <mary.major@example.com>",
    "DefaultContent": {
        "Template": {
            "TemplateName": "MyTemplate",
            "TemplateData": "{ \"name\":\"friend\", \"favoriteanimal\":\"unknown\" }"
        }
    },
    "BulkEmailEntries": [
        {
            "Destination": {
                "ToAddresses": [
                    "anaya.iyengar@example.com"
                ]
            },
            "ReplacementEmailContent": {
                "ReplacementTemplate": {
                    "ReplacementTemplateData": "{ \"name\":\"Anaya\", \"favoriteanimal\":\"angelfish\" }"
                }
            }
        },
        {
            "Destination": {
                "ToAddresses": [
                    "liu.jie@example.com"
                ]
            },
            "ReplacementEmailContent": {
                "ReplacementTemplate": {
                    "ReplacementTemplateData": "{ \"name\":\"Liu\", \"favoriteanimal\":\"lion\" }"
                }
            }
        },
        {
            "Destination": {
                "ToAddresses": [
                    "shirley.rodriguez@example.com"
                ]
            },
            "ReplacementEmailContent": {
                "ReplacementTemplate": {
                    "ReplacementTemplateData": "{ \"name\":\"Shirley\", \"favoriteanimal\":\"shark\" }"
                }
            }
        },
        {
            "Destination": {
                "ToAddresses": [
                    "richard.roe@example.com"
                ]
            },
            "ReplacementEmailContent": {
                "ReplacementTemplate": {
                    "ReplacementTemplateData": "{}"
                }
            }
        }
    ],
    "ConfigurationSetName": "ConfigSet"
}
```

This code contains the following properties:

    * FromEmailAddress
     – The email address of the sender.
    * DefaultContent –
     A JSON object that contains the
     `TemplateName` and
     `TemplateData` objects.
    * TemplateName –
     The name of the `Template` resource to apply
     to the email.
    * TemplateData –
     Contains key-value pairs that will be used if the
     `ReplacementEmailContent` object contains
     an empty JSON object, `{}`, in the
     `ReplacementTemplateData`
     property.
    * BulkEmailEntries
     – An array that contains one or more
     `Destination` objects.
    * Destination – An
     object containing the email recipients defined in the
     *ToAddresses*,
     *CcAddresses*, and
     *BccAddresses* properties. These
     can be used in any combination and can contain one or
     more email addresses that will receive the same
     email.
    * ReplacementTemplateData
     – An escaped JSON string that contains key-value
     pairs. The keys correspond to the variables in the
     template, for example, `{{name}}`. The values
     represent the content that replaces the variables in the
     email. (If the JSON string here is empty, indicated by
     `{}`, the key-value pairs defined in the
     `TemplateData` property within the
     `DefaultContent` object will be
     used.)
    * ConfigurationSetName
     – The name of the configuration set to use when
     sending the email.


    ###### Note

    We recommend that you use a configuration set that
     is configured to publish Rendering Failure events to
     Amazon SNS. For more information, see [(Optional) Part 1: Set up
     Rendering Failure event notifications](#send-personalized-email-set-up-notifications "#send-personalized-email-set-up-notifications").

Inline template code example
Notice that the `TemplateContent` properties (that
would normally be defined in a _stored
template_), are being defined
_inline_ along with the
`TemplateData` property which makes this an
_inline template_.

```
{
    "FromEmailAddress": "Mary Major <mary.major@example.com>",
    "DefaultContent": {
        "Template": {
            "TemplateContent": {
                "Subject": "Greetings, {{name}}!",
                "Text": "Dear {{name}},\r\nYour favorite animal is {{favoriteanimal}}.",
                "Html": "<h1>Hello {{name}},</h1><p>Your favorite animal is {{favoriteanimal}}.</p>"
            },
            "TemplateData": "{ \"name\":\"friend\", \"favoriteanimal\":\"unknown\" }"
        }
    },
    "BulkEmailEntries": [
        {
            "Destination": {
                "ToAddresses": [
                    "anaya.iyengar@example.com"
                ]
            },
            "ReplacementEmailContent": {
                "ReplacementTemplate": {
                    "ReplacementTemplateData": "{ \"name\":\"Anaya\", \"favoriteanimal\":\"angelfish\" }"
                }
            }
        },
        {
            "Destination": {
                "ToAddresses": [
                    "liu.jie@example.com"
                ]
            },
            "ReplacementEmailContent": {
                "ReplacementTemplate": {
                    "ReplacementTemplateData": "{ \"name\":\"Liu\", \"favoriteanimal\":\"lion\" }"
                }
            }
        },
        {
            "Destination": {
                "ToAddresses": [
                    "shirley.rodriguez@example.com"
                ]
            },
            "ReplacementEmailContent": {
                "ReplacementTemplate": {
                    "ReplacementTemplateData": "{ \"name\":\"Shirley\", \"favoriteanimal\":\"shark\" }"
                }
            }
        },
        {
            "Destination": {
                "ToAddresses": [
                    "richard.roe@example.com"
                ]
            },
            "ReplacementEmailContent": {
                "ReplacementTemplate": {
                    "ReplacementTemplateData": "{}"
                }
            }
        }
    ],
    "ConfigurationSetName": "ConfigSet"
}
```

This code contains the following properties:

    * FromEmailAddress
     – The email address of the sender.
    * DefaultContent –
     A JSON object that contains the
     `TemplateContent` and
     `TemplateData` objects.
    * TemplateContent –
     A container for the following attributes:




    	+ Subject –
    	 The subject line of the email. This property may
    	 contain replacement tags. These tags use the
    	 following format: `{{tagname}}`. When
    	 you send the email, you can specify a value for
    	 `tagname` for each destination.
    	+ Html –
    	 The HTML body of the email. This property may
    	 contain replacement tags. The preceding example
    	 includes two tags: `{{name}}` and
    	 `{{favoriteanimal}}`.
    	+ Text –
    	 The text body of the email. Recipients whose email
    	 clients don't display HTML content will see this
    	 version of the email. This property may also
    	 contain replacement tags.
    * TemplateData –
     Contains key-value pairs that will be used if the
     `ReplacementEmailContent` object contains
     an empty JSON object, `{}`, in the
     `ReplacementTemplateData`
     property.
    * BulkEmailEntries
     – An array that contains one or more
     `Destination` objects.
    * Destination – An
     object containing the email recipients defined in the
     *ToAddresses*,
     *CcAddresses*, and
     *BccAddresses* properties. These
     can be used in any combination and can contain one or
     more email addresses that will receive the same
     email.
    * ReplacementTemplateData
     – An escaped JSON string that contains key-value
     pairs. The keys correspond to the variables defined in
     the `TemplateContent` properties in this
     file, for example, `{{name}}`. The values
     represent the content that replaces the variables in the
     email. (If the JSON string here is empty, indicated by
     `{}`, the key-value pairs defined in the
     `TemplateData` property within the
     `DefaultContent` object will be
     used.)
    * ConfigurationSetName
     – The name of the configuration set to use when
     sending the email.


    ###### Note

    We recommend that you use a configuration set that
     is configured to publish Rendering Failure events to
     Amazon SNS. For more information, see [(Optional) Part 1: Set up
     Rendering Failure event notifications](#send-personalized-email-set-up-notifications "#send-personalized-email-set-up-notifications").

2. Change the values in the code in the previous step to meet your needs, and
   then save the file as `mybulkemail.json`.
3. At the command line, type the following v2 API command to send the bulk
   email:

```
aws sesv2 send-bulk-email --cli-input-json file://`mybulkemail.json`
```
