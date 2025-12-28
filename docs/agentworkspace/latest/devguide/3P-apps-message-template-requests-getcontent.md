# Get content of a

message template in Amazon Connect Agent Workspace

Gets the content of a message template. This includes plaintext or html content of the
body of the message template as a string, the subject of the message template, and
attachments if they are configured on the message template. Attributes in the message
template will be filled if they are system attributes, agent attributes, or custom
attributes set up in the contact flow. More information on the attributes can be found
here: [https://docs.aws.amazon.com/connect/latest/adminguide/personalize-templates.html](../../../connect/latest/adminguide/personalize-templates.md "../../../connect/latest/adminguide/personalize-templates.md")

**Signature**

```
getContent(messageTemplateId: string, contactId: string): Promise<MessageTemplateContent>
```

**messageTemplateId**

The messageTemplateId can be either the ID or the ARN of a message template

- Passing in the ARN returned by searchMessageTemplates is recommended here,
  since this will get the content of the active version of the message
  template.
- Passing in the ID will return the content of the latest version of the
  message template. A qualifier can be appended to the messageTemplateId to
  get the content of a different version of the message template.
  More information on qualifiers can be found here:

[https://docs.aws.amazon.com/connect/latest/APIReference/API_amazon-q-connect_GetMessageTemplate.html](../../../connect/latest/APIReference/API_amazon-q-connect_GetMessageTemplate.md "../../../connect/latest/APIReference/API_amazon-q-connect_GetMessageTemplate.md")

More information on versioning can be found here:

[https://docs.aws.amazon.com/connect/latest/adminguide/about-version-message-templates.html](../../../connect/latest/adminguide/about-version-message-templates.md "../../../connect/latest/adminguide/about-version-message-templates.md")

**contactId**

The current contact to add the message template to. This is used to populate
attributes in the message template

**MessageTemplateContent Properties**

| **Parameter**             | **Type**                    | **Description**                                                                                                                                                 |
| ------------------------- | --------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| subject                   | string                      | Message subject populated in the template                                                                                                                       |
| body                      | MessageTemplateBody         | Message body content populated in the template. This can include<br>plainText or html or both                                                                   |
| attachments               | MessageTemplateAttachment[] | Attachments populated in the template                                                                                                                           |
| attributesNotInterpolated | string[]                    | List of attributes that were not automatically populated in the<br>message template. If all attributes were automatically populated,<br>this list will be empty |

**MessageTemplateBody Properties**

| **Parameter** | **Type** | **Description**                                                                                                                                                                           |
| ------------- | -------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| plainText     | string   | Plain text content of the message template as a string. It is<br>possible for both the plain text and html to be populated, or for<br>only the plain text or html content to be populated |
| html          | string   | HTML content of the message template as a string                                                                                                                                          |

**MessageTemplateAttachment Properties**

| **Parameter** | **Type** | **Description**                     |
| ------------- | -------- | ----------------------------------- |
| fileName      | string   | Name of the attachment              |
| fileId        | string   | ID of the attachment                |
| downloadUrl   | string   | URL to download the attachment from |
