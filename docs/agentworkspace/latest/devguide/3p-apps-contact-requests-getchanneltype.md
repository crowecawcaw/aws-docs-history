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

| **Parameter**        | **Type** | **Description**                                                                                                                                |
| -------------------- | -------- | ---------------------------------------------------------------------------------------------------------------------------------------------- |
| contactId _Required_ | string   | The id of the contact to which a participant needs to be added.<br>Use `AppContactScope.CurrentContactId` to represent<br>the current contact. |

**Output - ContactChannelType**

| **Parameter** | **Type** | **Description**                                                                |
| ------------- | -------- | ------------------------------------------------------------------------------ | -------------------------------------------------------------------------- | ------------- | ------------------- | ---------------------------------------------------------------------------------------------------------------------------------- |
| type          | string   | The possible values are `voice, queue_callback, chat, task,<br>email`          |
| subtype       | string   | For the types `voice` &<br>`queue_callback`, it will be<br>`connect:Telephony` | <br>`connect:WebRTC`.<br>For the type `chat`, it will be<br>`connect:Chat` | `connect:SMS` | <br>`connect:Apple` | <br>`connect:Guide`.<br>For the type `task`, it will be<br>`connect:Task`.<br>For the type `email`, it will be<br>`connect:Email`. |

**Permissions required:**

```
Contact.Details.View

```
