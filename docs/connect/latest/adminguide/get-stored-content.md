# Flow block in Amazon Connect: Get stored content

This topic specifies the flow block for getting stored content to be used within flows.

## Description

Use this block to retrieve stored data from your S3 bucket when you need to make
branching decisions in your flows. For example, this block can be used to access
email message bodies stored in your Amazon S3 buckets. The following options are
currently available for this flow block:

Email message (Plain text)

This block will download the plain text version of the email message
present in your S3 bucket and store it on the
`$.Email.EmailMessage.Plaintext` flow attribute. The
email message content is downloaded as a plain text file and the maximum
size supported is currently 32 KB due to the maximum size of flow
attributes limits. Make sure to [Enable email for your Amazon Connect instance](enable-email1.md "enable-email1.md") before using this option.

## Use cases for this block

This flow block is designed to be used in the following scenarios::

- Use it with the [Check contact attributes](check-contact-attributes.md "check-contact-attributes.md") and
  [Send message](send-message.md "send-message.md") flow blocks to
  configure automated email responses and routing.
  - In the [Check contact attributes](check-contact-attributes.md "check-contact-attributes.md") block, for namespace, choose **Email**
    and for **Key** choose **Email Message**. Then, add conditions depending on
    your use case. For example, if you wanted to route to a specific
    queue any time an email message contained the word “Refund” (**Note**:
    keywords are case-sensitive).
  - In the [Send message](send-message.md "send-message.md") block, select an email template or type in a message to send the automated response.

### Properties configuration

in CheckContactAttributes

In the [Check contact
attributes](check-contact-attributes.md "check-contact-attributes.md") block, for namespace, choose
**Email** and for **Key** choose
**Email Message**. Then, add conditions depending on the use
case.

## Contact types

The following table shows how this block routes a contact for each channel.

| Channel | Supported? |
| ------- | ---------- |
| Voice   | No         |
| Chat    | No         |
| Task    | No         |
| Email   | Yes        |

## Flow types

You can use this block in the following [flow
types](create-contact-flow.md#contact-flow-types "create-contact-flow.md#contact-flow-types"):

- Inbound flow
- Customer queue flow
- Customer hold flow
- Customer whisper flow
- Outbound whisper flow
- Agent hold flow
- Agent whisper flow
- Transfer to agent flow
- Transfer to queue flow
- Disconnect flow

## How to configure this block

You can configure the **Get stored content** block by using the Amazon Connect admin
website or by using the `LoadContactContent` in the Amazon Connect Flow
language.

## Flow language representation

The following code example shows how to use the `LoadContactContent` in the Amazon Connect Flow
language.

```
{
      "Parameters": {
        "ContentType": enum "EmailMessage"
      },
      "Identifier": "string",
      "Type": "LoadContactContent",
      "Transitions": {
        "NextAction": "string",
        "Errors": [
          {
            "NextAction": "string",
            "ErrorType": "NoMatchingError"
          }
        ]
      }
    }
```

## Error scenarios

A contact is routed down the Error branch if the flows services runs into any of
the following error scenarios:

- When using Email message (Plain text):
  - When the size of the email message in plaintext format is more than 32KB.
  - Amazon Connect is unable to download the email body from the S3
    bucket. This may be due to the S3 bucket policy not being set up
    correctly (see [Step 4: Enable email and create an Amazon S3 bucket](enable-email1.md#enable-email-buckets "enable-email1.md#enable-email-buckets")),
    Amazon Connect does not have proper access to the S3 bucket (see
    [Step 5: Configure a
    CORS policy](enable-email1.md#config-email-attachments-cors1 "enable-email1.md#config-email-attachments-cors1")), or there is no email message in
    plaintext format available on the contact.
