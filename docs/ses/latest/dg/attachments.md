# Working with email attachments in SES

Email attachments in SES are files that you can include with your email messages
when using the SES API v2 `SendEmail` and `SendBulkEmail`
operations. This feature enables you to enrich your email content by including documents
such as PDFs, Word files, images, or other file types that comply with SES supported
MIME types. You can also include inline images that render directly in the email content
without requiring recipients to download them separately. You can include multiple
attachments per email, up to the 40MB total message size limit.

###### Note

[`SendEmail`](../APIReference-V2/API_SendEmail.md "../APIReference-V2/API_SendEmail.md")
SES API v2 with `Raw` content type, SMTP interface, and SES API v1
continue to handle attachments through [raw email
MIME message construction](send-email-raw.md#send-email-raw-mime "send-email-raw.md#send-email-raw-mime").

## How attachments work in SES

There are two different types of encoding that happen at different stages when sending
an email with attachments:

Stage 1 – Sending data to SES:

- When you want to send an attachment to SES, the binary data (like a PDF
  or image) needs to be converted into a format that can be transmitted
  safely.
- This is where base64-encoding comes in—it's required because you can't
  send raw binary data in a JSON request.
- If you're using the AWS SDK, it handles this encoding automatically.
- If you're using the AWS CLI, you need to base64-encode the attachment yourself
  before sending it.

Stage 2 – SES creating the email:

- Once SES receives your data, it needs to create an actual email with
  the attachment.
- This is where the [ContentTransferEncoding](#attachment-structure "#attachment-structure") setting comes into play.
- SES will use whatever encoding method you specify in
  ContentTransferEncoding to automatically format the attachment in the final
  email.

Think of it like this—it's similar to sending a package through the mail.
First, you need to get the package to the post office (Stage 1 - Base64-encoding
required), then the post office will package it appropriately for final delivery (Stage
2 - ContentTransferEncoding).

## Attachment object structure

When you send an email with attachments through SES, the service handles the
complex MIME message construction automatically. You simply need to provide the
attachment content and metadata through the following the SES API v2 [`Attachment`](../APIReference-V2/API_Attachment.md "../APIReference-V2/API_Attachment.md") object
structure:

- `FileName` (Required) – The file name displayed to
  recipients (must include file extension). If not provided, SES will
  derive a `ContentType` from the extension of the
  `FileName`.
- `ContentType` (Optional) – [IANA-compliant media type identifier](https://www.iana.org/assignments/media-types/media-types.xhtml "https://www.iana.org/assignments/media-types/media-types.xhtml").
- `ContentDisposition` (Optional) – Specifies how the
  attachment should be rendered: `ATTACHMENT`
  _(default)_ or `INLINE`.
- `ContentDescription` (Optional) – Short description of the
  content.
- `RawContent` (Required) – The actual content of the
  attachment.
- `ContentTransferEncoding` (Optional) – Specifies how the
  attachment payload is encoded when it's assembled into the email's mime message:
  `SEVEN_BIT`
  _(default)_, `BASE64` or
  `QUOTED_PRINTABLE`.

All attached content must be encoded to base64 before transferring to the SES
endpoint for sending. If you're using the AWS SDK client to make API calls, this is
automatically handled for you. If you're using the AWS CLI, or have implemented your own
client, you will have to do the encoding yourself, such as:

- Plain text content: `Text attachment sample content.`
- Base64 encoded:
  `VGV4dCBhdHRhY2htZW50IHNhbXBsZSBjb250ZW50Lg==`

The following examples show how to use the attachment object structure when specifying
attachments with the SES API v2 [`SendEmail`](../APIReference-V2/API_SendEmail.md "../APIReference-V2/API_SendEmail.md") and [`SendBulkEmail`](../APIReference-V2/API_SendBulkEmail.md "../APIReference-V2/API_SendBulkEmail.md")
operations using the AWS CLI referencing a JSON file containing attachment object
elements.

###### Example– SendEmail with simple content

```
aws sesv2 send-email --cli-input-json file://request-send-email-simple.json
```

**request-send-email-simple.json**

```
{
    "FromEmailAddress": "sender@example.com",
    "Destination": {
        "ToAddresses": [
            "recipient@example.com"
        ]
    },
    "Content": {
        "Simple": {
            "Subject": {
                "Data": "Email with attachment"
            },
            "Body": {
                "Text": {
                    "Data": "Please see attached document."
                },
                "Html": {
                    "Data": "Please see attached <b>document</b>."
                }
            },
            "Attachments": [
                {
                    "RawContent": "<base64-encoded-content>",
                    "ContentDisposition": "ATTACHMENT",
                    "FileName": "document.pdf",
                    "ContentDescription": "PDF Document Attachment",
                    "ContentTransferEncoding": "BASE64"
                }
            ]
        }
    }
}
```

###### Example– SendEmail with simple content and inline attachment

```
aws sesv2 send-email --cli-input-json file://request-send-email-simple-inline-attachment.json
```

**request-send-email-simple-inline-attachment.json**

```
{
    "FromEmailAddress": "sender@example.com",
    "Destination": {
        "ToAddresses": [
            "recipient@example.com"
        ]
    },
    "Content": {
        "Simple": {
            "Subject": {
                "Data": "Email with attachment"
            },
            "Body": {
                "Html": {
                    "Data": "<html><body>Our logo:<br><img src=\"cid:logo123\" alt=\"Company Logo\"></body></html>"
                }
            },
            "Attachments": [
                {
                    "RawContent": "<base64-encoded-content>",
                    "ContentDisposition": "INLINE",
                    "FileName": "logo.png",
                    "ContentId": "logo123",
                    "ContentTransferEncoding": "BASE64"
                }
            ]
        }
    }
}
```

###### Example– SendEmail with template content

```
aws sesv2 send-email --cli-input-json file://request-send-email-template.json
```

**request-send-email-template.json**

```
{
    "FromEmailAddress": "sender@example.com",
    "Destination": {
        "ToAddresses": [
            "recipient@example.com"
        ]
    },
    "Content": {
        "Template": {
            "TemplateName": "MyTemplate",
            "TemplateData": "{\"name\":\"John\"}",
            "Attachments": [
                {
                    "RawContent": "<base64-encoded-content>",
                    "ContentDisposition": "ATTACHMENT",
                    "FileName": "document.pdf",
                    "ContentDescription": "PDF Document Attachment",
                    "ContentTransferEncoding": "BASE64"
                }
            ]
        }
    }
}
```

###### Example– SendBulkEmail with attachment content

```
aws sesv2 send-bulk-email --cli-input-json file://request-send-bulk-email.json
```

**request-send-bulk-email.json**

```
{
    "FromEmailAddress": "sender@example.com",
    "DefaultContent": {
        "Template": {
            "TemplateName": "MyTemplate",
            "TemplateData": "{}",
            "Attachments": [
                {
                    "RawContent": "<base64-encoded-content>",
                    "ContentDisposition": "ATTACHMENT",
                    "FileName": "document.pdf",
                    "ContentDescription": "PDF Document Attachment",
                    "ContentTransferEncoding": "BASE64"
                }
            ]
        }
    },
    "BulkEmailEntries": [
        {
            "Destination": {
                "ToAddresses": [
                    "recipient@example.com"
                ]
            },
            "ReplacementEmailContent": {
                "ReplacementTemplate": {
                    "ReplacementTemplateData": "{\"name\":\"John\"}"
                }
            }
        }
    ]
}
```

## Best practices

- Keep total message size (including attachments) under 40MB.
- Let SES auto-detect content types based on file extensions when
  possible.
- Explicitly specify content types only when they fall outside of the [common MIME types](https://developer.mozilla.org/en-US/docs/Web/HTTP/MIME_types/Common_types "https://developer.mozilla.org/en-US/docs/Web/HTTP/MIME_types/Common_types").
- Consider using inline images for better email rendering.
- SES supports a wide range of MIME types for attachments, except for
  those listed in [Unsupported attachment types](#mime-types "#mime-types").

## SES unsupported attachment types

You can send messages with attachments through Amazon SES by using the Multipurpose
Internet Mail Extensions (MIME) standard. Amazon SES accepts all file attachment
types _except_ for attachments with the file extensions in the
following list.

|                                                                                                                                                 |                                                                                                                                             |                                                                                                                                                           |                                                                                                                                                    |                                                                                                                                                   |
| ----------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------- |
| .ade<br>.adp<br>.app<br>.asp<br>.bas<br>.bat<br>.cer<br>.chm<br>.cmd<br>.com<br>.cpl<br>.crt<br>.csh<br>.der<br>.exe<br>.fxp<br>.gadget<br>.hlp | .hta<br>.inf<br>.ins<br>.isp<br>.its<br>.js<br>.jse<br>.ksh<br>.lib<br>.lnk<br>.mad<br>.maf<br>.mag<br>.mam<br>.maq<br>.mar<br>.mas<br>.mat | .mau<br>.mav<br>.maw<br>.mda<br>.mdb<br>.mde<br>.mdt<br>.mdw<br>.mdz<br>.msc<br>.msh<br>.msh1<br>.msh2<br>.mshxml<br>.msh1xml<br>.msh2xml<br>.msi<br>.msp | .mst<br>.ops<br>.pcd<br>.pif<br>.plg<br>.prf<br>.prg<br>.reg<br>.scf<br>.scr<br>.sct<br>.shb<br>.shs<br>.sys<br>.ps1<br>.ps1xml<br>.ps2<br>.ps2xml | .psc1<br>.psc2<br>.tmp<br>.url<br>.vb<br>.vbe<br>.vbs<br>.vps<br>.vsmacros<br>.vss<br>.vst<br>.vsw<br>.vxd<br>.ws<br>.wsc<br>.wsf<br>.wsh<br>.xnk |

Some ISPs have further restrictions (such as restrictions regarding archived
attachments), so we recommend testing your email sending through major ISPs before you
send your production email.
