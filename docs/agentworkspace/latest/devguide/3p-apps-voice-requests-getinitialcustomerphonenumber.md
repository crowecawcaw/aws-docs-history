# Gets the

phone number of the initial customer connection in Amazon Connect Agent Workspace

Gets the phone number of the initial customer connection. Applicable only for
voice contacts.

**Signature**

```
getInitialCustomerPhoneNumber(contactId: string): Promise<string>

```

**Usage**

```
const initialCustomerPhoneNumber: string = await voiceClient.getInitialCustomerPhoneNumber(AppContactScope.CurrentContactId);

```

**Input**

| **Parameter**        | **Type** | **Description**                                                                                                                       |
| -------------------- | -------- | ------------------------------------------------------------------------------------------------------------------------------------- |
| contactId _Required_ | string   | The id of the contact for which the data is requested. Use<br>`AppContactScope.CurrentContactId` to represent<br>the current contact. |

**Permissions required:**

```
Contact.CustomerDetails.View

```
