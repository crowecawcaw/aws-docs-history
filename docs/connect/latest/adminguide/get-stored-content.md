

# Flow block in Connect Customer: Get stored content
<a name="get-stored-content"></a>

This topic specifies the flow block for getting stored content to be used within flows.

## Description
<a name="get-stored-content-description"></a>

Use this block to retrieve stored data from your S3 bucket when you need to make branching decisions in your flows. For example, this block can be used to access email message bodies stored in your Amazon S3 buckets. The following options are currently available for this flow block:

Email message (Plain text)  
This block will download the plain text version of the email message present in your S3 bucket and store it on the `$.Email.EmailMessage.Plaintext` flow attribute. The email message content is downloaded as a plain text file and the maximum size supported is currently 32 KB due to the maximum size of flow attributes limits. Make sure to [Enable email for your Connect Customer instance](enable-email1.md) before using this option.

## Use cases for this block
<a name="get-stored-content-use-case"></a>

This flow block is designed to be used in the following scenarios::
+ Use it with the [Check contact attributes](check-contact-attributes.md) and [Send message](send-message.md) flow blocks to configure automated email responses and routing.
  + In the [Check contact attributes](check-contact-attributes.md) block, for namespace, choose **Email** and for **Key** choose **Email Message**. Then, add conditions depending on your use case. For example, if you wanted to route to a specific queue any time an email message contained the word "Refund" (**Note**: keywords are case-sensitive). 
  + In the [Send message](send-message.md) block, select an email template or type in a message to send the automated response.

**Prevent email loops**  
If you use automated email responses, make sure that your inbound email flow filters out Non-Delivery Reports (NDRs) and other automated emails before sending replies. Without filtering, automated replies can create self-sustaining email loops. For more information, see [Prevent automated email loops](email-capabilities.md#email-capabilities-preventloops).

### Properties configuration in CheckContactAttributes
<a name="get-stored-content-property-configuration"></a>

In the [Check contact attributes](check-contact-attributes.md) block, for namespace, choose **Email** and for **Key** choose **Email Message**. Then, add conditions depending on the use case.

## Contact types
<a name="get-stored-content-channels"></a>

The following table shows how this block routes a contact for each channel.


| Channel | Supported? | 
| --- | --- | 
| Voice | No | 
| Chat | No | 
| Task | No | 
| Email | Yes | 

## Flow types
<a name="get-stored-content-agent-types"></a>

You can use this block in the following [flow types](create-contact-flow.md#contact-flow-types):
+ Inbound flow
+ Customer queue flow
+ Customer hold flow
+ Customer whisper flow
+ Outbound whisper flow
+ Agent hold flow
+ Agent whisper flow
+ Transfer to agent flow
+ Transfer to queue flow
+ Disconnect flow

## How to configure this block
<a name="get-stored-content-configure"></a>

You can configure the **Get stored content** block by using the Connect Customer admin website or by using the `LoadContactContent` in the Connect Customer Flow language.

## Flow language representation
<a name="get-stored-content-flow-language"></a>

The following code example shows how to use the `LoadContactContent` in the Connect Customer Flow language.

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
<a name="get-stored-content-error-scenarios"></a>

A contact is routed down the Error branch if the flows services runs into any of the following error scenarios:
+ When using Email message (Plain text):
  + When the size of the email message in plaintext format is more than 32KB.
  + Connect Customer is unable to download the email body from the S3 bucket. This might be due to the S3 bucket policy not being set up correctly (see [Step 4: Enable email and create an Amazon S3 bucket](enable-email1.md#enable-email-buckets)), Amazon Connect does not have proper access to the S3 bucket (see [Step 5: Configure a CORS policy](enable-email1.md#config-email-attachments-cors1)), or there is no email message in plaintext format available on the contact.