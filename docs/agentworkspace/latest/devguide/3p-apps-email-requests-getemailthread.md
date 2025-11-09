# Get a list of email contacts

in an email contact's tree in Amazon Connect Agent Workspace

Returns an array of EmailThreadContact objects (for the provided
contactAssociationId) that represent that contact's email thread. The
contactAssociationId is the root contact id which is used as a unique identifier for
all subsequent contacts in a contact tree. Returns an object that includes:

- `contacts: EmailThreadContact[]`: an array of
  EmailThreadContact objects, each an email contact in the thread
- `nextToken?: string`: The token for the next set of results;
  use the value returned in the previous response in the next request to
  retrieve the next set of results

**Signature**

```
getEmailThread(getEmailThreadParams: GetEmailThreadParams): Promise<{ contacts: EmailThreadContact[]; nextToken?: string; }>
```

**EmailThreadContact Properties**

| **Parameter**       | **Type** | **Description**                                                                                                   |
| ------------------- | -------- | ----------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| contactId           | string   | The id of the email contact                                                                                       |
| contactArn          | string   | The ARN of the email contact                                                                                      |
| previousContactId   | string   | If this contact is not the first contact, this is the ID of the<br>previous contact.                              |
| initialContactId    | string   | If this contact is related to other contacts, this is the ID of<br>the initial contact.                           |
| relatedContactId    | string   | The contactId that is related to this contact.                                                                    |
| initiationMethod    | string   | Indicates how the contact was initiated; Supported values:<br>"INBOUND" ,"OUTBOUND", "AGENT_REPLY", or "TRANSFER" |
| initiationTimestamp | Date     | The date and time this contact was initiated, in UTC<br>time.                                                     |
| disconnectTimestamp | Date     | undefined                                                                                                         | The date and time that the customer endpoint disconnected from<br>the current contact, in UTC time. In transfer scenarios, the<br>DisconnectTimestamp of the previous contact indicates the date and<br>time when that contact ended. |

**GetEmailThreadParams Properties**

| **Parameter**        | **Type** | **Description**                                                                                                                                       |
| -------------------- | -------- | ----------------------------------------------------------------------------------------------------------------------------------------------------- |
| contactAssociationId | string   | The contact association id to get the thread for.                                                                                                     |
| maxResults           | number   | The max number of email threads to return; Default is 100.<br>Minimum value of 1. Maximum value of 100.                                               |
| nextToken            | string   | The token for the next set of results. Use the value returned in<br>the previous response in the next request to retrieve the next set<br>of results. |

**Usage**

```

const inboundEmailData = await emailClient.getEmailData({
   contactId: sampleContactId, // The inbound email contact you've accepted (or is still connecting)
   activeContactId: sampleContactId, // The email contact you're actively working; in this example, its the same as the accepted inbound email
});

const emailThreadContacts = await emailClient.getEmailThread({
  contactAssociationId: inboundEmailData.contactAssociationId,
});

// OPTIONAL: Filter out contacts that have been transferred to avoid displaying duplicated email content
const previousContactIdsSet = new Set(
    emailThreadContacts
        .map(emailThreadContact => emailThreadContact.previousContactId)
        .filter(Boolean)
);

const filteredEmailContactsInEmailThread = emailThreadContacts.filter(emailContact =>
    emailContact.contactId === sampleContactId ||
    !previousContactIdsSet.includes(emailContact.contactId)
);
```

###### Note

Each time an email contact is transferred, a new contact ID is created with
initiationMethod === 'TRANSFER' and its previousContactId is the contact id
before the transfer. You may optionally filter out these transferred contacts to
avoid duplicate content when rendering the email thread.
