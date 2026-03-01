# Get the metadata for an email contact in Amazon Connect Agent Workspace

Returns the metadata for an email contact id while handling an active contact. The
activeContactId is the id of the email contact the agent is actively viewing while
contactId is the id of the email contact whose metadata should be retrieved.

**Signature**

```
getEmailData({ contactId, activeContactId }: { contactId: string; activeContactId: string; }): Promise<EmailContact>
```

**Output - _EmailContact
Properties_**

| **Parameter**        | **Type**                | **Description**                                                                                                                                                                                  |
| -------------------- | ----------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | --------------------------------------------------------------------------------------------------------------------------- |
| contactId            | string                  | The id of the email contact                                                                                                                                                                      |
| contactArn           | string                  | The ARN of the email contact                                                                                                                                                                     |
| contactAssociationId | string                  | The root contactId which is used as a unique identifier for all<br>subsequent contacts in a contact tree. Use this value with the<br>EmailClient.getEmailThread api.                             |
| relatedContactId     | string                  | This contact is in response or related to the specified related<br>contact.                                                                                                                      |
| initialContactId     | string                  | If this contact is related to other contacts, this is the id of<br>the initial contact.                                                                                                          |
| subject              | string                  | The subject of the email                                                                                                                                                                         |
| from                 | EmailAddress            | An object that includes the from email address; this value could<br>be undefined when the email contact has not been sent.                                                                       |
| to                   | EmailAddress[]          | An array of objects, each including an email address the email<br>contact was sent to                                                                                                            |
| cc                   | EmailAddress[]          | An array of objects, each including an email address that was<br>carbon copied on the email contact                                                                                              |
| deliveredTo          | EmailAddress            | An object that includes the email address associated with Amazon<br>Connect that received this message; this is only applicable when<br>direction=INBOUND.                                       |
| direction            | "INBOUND"               | "OUTBOUND"                                                                                                                                                                                       | INBOUND means the email contact was delivered to Amazon Connect;<br>OUTBOUND means the email contact is from Amazon Connect |
| bodyLocation         | EmailArtifactLocation   | An object that includes the id and associated resource ARN of the<br>file that the email contact's body is stored in; this value could be<br>undefined when the email contact has not been sent. |
| attachmentLocations  | EmailArtifactLocation[] | An array of objects, each including the id and associated<br>resource ARN, of files that have been attached to the email<br>contact                                                              |

**EmailAddress Properties**

| **Parameter** | **Type** | **Description**                                           |
| ------------- | -------- | --------------------------------------------------------- |
| emailAddress  | string   | The email address                                         |
| displayName   | string   | The name that is displayed inside the recipient's mailbox |

**EmailArtifactLocation Properties**

| **Parameter**         | **Type** | **Description**                                                         |
| --------------------- | -------- | ----------------------------------------------------------------------- |
| fileId                | string   | The id of the attached file                                             |
| associatedResourceArn | string   | The Amazon Connect resource to which the attached file is related<br>to |

**Usage**

```

const activeContactId: string = "exampleActiveContactId"; // The contact the agent is actively handling
const contactId: string = "contactIdToDescribe"; // The email contact id whose metadata should be retrieved

const emailMetadata: EmailContact = await emailClient.getEmailData({ contactId, activeContactId });

// Get the body of the email through the File Client
const bodyLocation = emailMetadata.bodyLocation;
if (bodyLocation) {
   const body: DownloadableAttachment = await fileClient.getAttachedFileUrl({
        attachment: bodyLocation,
        activeContactId,
   });

   const { downloadUrl } = body;
   const response: Response = await fetch(downloadUrl, { method: "GET" });
   const bodyContent: string = (await response.json()).messageContent;
}
```

###### Note

The EmailContact object will contain bodyLocation and attachmentLocations,
both of which will require use of the FileClient's getAttachedFileUrl to get the
relevant data for those objects.
