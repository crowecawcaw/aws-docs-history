# Step 3: Specify your configuration set when

you send email

After you [create a configuration
set](event-publishing-create-configuration-set.md "event-publishing-create-configuration-set.md") and [add an event
destination](event-publishing-add-event-destination.md "event-publishing-add-event-destination.md"), the last step to event publishing is to send your emails.

To publish events associated with an email, you must provide the name of the configuration
set to associate with the email. Optionally, you can provide message tags to categorize the
email.

You provide this information to Amazon SES as either parameters to the email sending API,
Amazon SES-specific email headers, or custom headers in your MIME message. The method you choose
depends on which email sending interface you use, as shown in the following table.

| Email Sending Interface       | Ways to Publish Events                                                                                                                                                                                                                                                                                                     |
| ----------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `SendEmail`                   | API parameters                                                                                                                                                                                                                                                                                                             |
| `SendTemplatedEmail`          | API parameters                                                                                                                                                                                                                                                                                                             |
| `SendBulkTemplatedEmail`      | API parameters                                                                                                                                                                                                                                                                                                             |
| `SendCustomVerificationEmail` | API parameters                                                                                                                                                                                                                                                                                                             |
| `SendRawEmail`                | API parameters, Amazon SES-specific email headers, or custom MIME<br>headers<br>Important If you specify message tags using both headers and API<br>parameters, Amazon SES uses only the message tags provided by the API<br>parameters. Amazon SES does not join message tags specified by API<br>parameters and headers. |
| SMTP interface                | Amazon SES-specific email headers                                                                                                                                                                                                                                                                                          |

The following sections describe how to specify the configuration set and message tags
using headers and using API parameters.

- [Using Amazon SES API
  Parameters](#event-publishing-using-ses-parameters "#event-publishing-using-ses-parameters")
- [Using Amazon SES-Specific Email
  Headers](#event-publishing-using-ses-headers "#event-publishing-using-ses-headers")
- [Using Custom Email
  Headers](#event-publishing-using-custom-headers "#event-publishing-using-custom-headers")

###### Note

You can optionally include message tags in the headers of your emails. Message tags
can include the numbers 0–9, the letters A–Z (both uppercase and lowercase),
hyphens (-), and underscores (\_).

## Using Amazon SES API

Parameters

To use [SendEmail](../APIReference/API_SendEmail.md "../APIReference/API_SendEmail.md"), [SendTemplatedEmail](../APIReference/API_SendTemplatedEmail.md "../APIReference/API_SendTemplatedEmail.md"), [SendBulkTemplatedEmail](../APIReference/API_SendBulkTemplatedEmail.md "../APIReference/API_SendBulkTemplatedEmail.md"),
[SendCustomVerificationEmail](../APIReference/API_SendCustomVerificationEmail.md "../APIReference/API_SendCustomVerificationEmail.md"), or [SendRawEmail](../APIReference/API_SendRawEmail.md "../APIReference/API_SendRawEmail.md") with event publishing,
you specify the configuration set and the message tags by passing data structures called
[ConfigurationSet](../APIReference/API_ConfigurationSet.md "../APIReference/API_ConfigurationSet.md") and
[MessageTag](../APIReference/API_MessageTag.md "../APIReference/API_MessageTag.md") to the API
call.

For more information about using the Amazon SES API, see the [Amazon Simple Email Service API Reference](../APIReference.md "../APIReference.md").

## Using Amazon SES-Specific Email

Headers

When you use `SendRawEmail` or the SMTP interface, you can specify the
configuration set and the message tags by adding Amazon SES-specific headers to the email.
Amazon SES removes the headers before sending the email. The following table shows the names
of the headers to use.

| Event Publishing Information | Header                    |
| ---------------------------- | ------------------------- |
| Configuration set            | `X-SES-CONFIGURATION-SET` |
| Message tags                 | `X-SES-MESSAGE-TAGS`      |

The following example shows how the headers might look in a raw email that you submit
to Amazon SES.

```
X-SES-MESSAGE-TAGS: tagName1=tagValue1, tagName2=tagValue2
X-SES-CONFIGURATION-SET: myConfigurationSet
From: sender@example.com
To: recipient@example.com
Subject: Subject
Content-Type: multipart/alternative;
	boundary="----=_boundary"

------=_boundary
Content-Type: text/plain; charset=UTF-8
Content-Transfer-Encoding: 7bit

body
------=_boundary
Content-Type: text/html; charset=UTF-8
Content-Transfer-Encoding: 7bit

body
------=_boundary--
```

## Using Custom Email

Headers

Although you must specify the configuration set name using the Amazon SES-specific header
`X-SES-CONFIGURATION-SET`, you can specify the message tags by using your
own MIME headers.

###### Note

Header names and values that you use for Amazon SES event publishing must be in ASCII.
If you specify a non-ASCII header name or value for Amazon SES event publishing, the
email sending call will still succeed, but the event metrics will not be emitted to
Amazon CloudWatch.
