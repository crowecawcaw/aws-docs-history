# Create a draft email

contact in Amazon Connect Agent Workspace

Creates a draft outbound email contact; can either be an agent initiated outbound
draft email or an agent reply draft email. Upon successful draft creation, the email
contact will be in connected state. Returns an object that includes:

- `contactId: string`: The contact id of the newly created draft
  email contact

**Signature**

```
createDraftEmail(contactCreation: CreateDraftEmailContact): Promise<EmailContactId>
```

**CreateDraftEmailContact Properties**

| **Parameter**           | **Type**                                         | **Description**                                                                                                                                                                                                         |
| ----------------------- | ------------------------------------------------ | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| initiationMethod        | "AGENT_REPLY"                                    | "OUTBOUND"                                                                                                                                                                                                              | "OUTBOUND" indicates that this draft email is the start of a new email conversation; "AGENT_REPLY" indicates that this draft email is being sent in response to an incoming email contact                                                                                                                                                                                                                                                                      |
| relatedContactId        | string                                           | The id of the contact that is the reason for creating the new draft email; this is required when initiationMethod="AGENT_REPLY" and should be the contact id of the email that this email is being sent in response to. |
| expiryDurationInMinutes | number                                           | Length of time before an unsent contact expires; Minimum is 1 minute, Maximum is 1 week; Default is 12 hours.                                                                                                           |
| attributes              | Record<string, string>                           | A custom key-value pair using an attribute map. The attributes are standard Amazon Connect attributes, and can be accessed in flows just like any other contact attributes.                                             |
| references              | Record<string, { type: string; value: string; }> | Well-formed data on a contact, used by agents to complete a contact request.                                                                                                                                            | **Usage for Agent Initiated Outbound** `const contact: EmailContactId = await emailClient.createDraftEmail({ initiationMethod: "OUTBOUND", }); const { contactId } = contact;` **Usage for Agent Reply** `const acceptedInboundEmailContactId = "exampleContactId"; const contact: EmailContactId = await emailClient.createDraftEmail({ initiationMethod: "AGENT_REPLY", relatedContactId: acceptedInboundEmailContactId, }); const { contactId } = contact;` |
