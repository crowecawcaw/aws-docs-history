# Create an outbound call

to phone number in Amazon Connect Agent Workspace

Creates an outbound call to the given phone number and returns the contactId. It
takes an optional parameter `queueARN` which specifies the outbound queue
associated with the call, if omitted the default outbound queue defined in the
agent's routing profile will be used.

**Signature**

```
  createOutboundCall(
    phoneNumber: string,
    options?: CreateOutboundCallOptions,
  ): Promise<CreateOutboundCallResult>

```

**Usage**

```
const outboundCallResult:CreateOutboundCallResult = await voiceClient.createOutboundCall("+18005550100");

```

**Input**

| **Parameter**            | **Type** | **Description**                                                                                                                                            |
| ------------------------ | -------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------- |
| phoneNumber _Required_   | string   | The phone number specified in E.164 format                                                                                                                 |
| options.queueARN         | string   | It specifies the outbound queue associated with the call, if<br>omitted the default outbound queue defined in the agent's routing<br>profile will be used. |
| options.relatedContactId | string   | Optional parameter to supply related contactId                                                                                                             |

**Output -
_CreateOutboundCallResult_**

| **Parameter** | **Type** | **Description**                             |
| ------------- | -------- | ------------------------------------------- |
| contactId     | string   | The contactId of the created outbound call. |

**Permissions required:**

```
Contact.Details.Edit

```
