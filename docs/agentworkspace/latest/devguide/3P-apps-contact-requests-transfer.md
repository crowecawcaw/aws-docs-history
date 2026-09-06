

# Transfer a contact to another agent in Connect Customer agent workspace
<a name="3P-apps-contact-requests-transfer"></a>

Performs a cold transfer by transferring the given contact to another agent using a quick connect and disconnecting from the contact. The quick connect type has to be either `agent` or `queue`. Supports voice, chat, task, and email channels.

 **Signature** 

```
  transfer(
    contactId: string,
    quickConnect: AgentQuickConnect | QueueQuickConnect,
  ): Promise<void>
```

 **Usage** 

```
const routingProfile: AgentRoutingProfile = await agentClient.getRoutingProfile();
const quickConnectResult: ListQuickConnectsResult = await agentClient.listQuickConnects(routingProfile.queues[0].queueARN);
const quickConnect: QuickConnect = quickConnectResult.quickConnects[1];
await contactClient.transfer(contactId, quickConnect);
```

 **Input** 


|  **Parameter**  |  **Type**  |  **Description**  | 
| --- | --- | --- | 
|  contactId Required  |  string  |  The id of the contact to which a participant needs to be transferred. | 
|  quickConnect Required  |  QuickConnect  |  Its either AgentQuickConnect or QueueQuickConnect  | 

 **Permissions required:** 

```
Contact.Details.Edit
```