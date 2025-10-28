# Get the type of contact in

Amazon Connect Agent Workspace

Get the type of the contact in Amazon Connect Agent Workspace. This indicates
what type of media is carried over the connections of the contact.

**Signature**

```

 getChannelType(contactId: string): Promise<ContactChannelType>

```

**Usage**

```
const contactType: ContactChannelType = await contactClient.getChannelType(AppContactScope.CurrentContactId);

```

**Input**

| **Parameter**        | **Type** | **Description**                                                                                                                          |
| -------------------- | -------- | ---------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------- | ------------- | --------------- | ------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------ |
| contactId _Required_ | string   | The id of the contact to which a participant needs to be added. Use `AppContactScope.CurrentContactId` to represent the current contact. | **Output - ContactChannelType**                                  |
| **Parameter**        | **Type** | **Description**                                                                                                                          |
| ---                  | ---      | ---                                                                                                                                      |
| type                 | string   | The possible values are `voice, queue_callback, chat, task, email`                                                                       |
| subtype              | string   | For the types `voice` & `queue_callback`, it will be `connect:Telephony`                                                                 | `connect:WebRTC`. For the type `chat`, it will be `connect:Chat` | `connect:SMS` | `connect:Apple` | `connect:Guide`. For the type `task`, it will be `connect:Task`. For the type `email`, it will be `connect:Email`. | **Permissions required:** `Contact.Details.View` |
