

# Add another participant to a contact in Connect Customer agent workspace
<a name="3P-apps-contact-requests-addparticipant"></a>

 Add another participant to the contact. Multi-party only works for Voice at this time. For Voice, the existing participants will be put on hold when a new participant is added. 

 **Signature** 

```
addParticipant(
    contactId: string,
    quickConnect: QuickConnect,
  ): Promise<AddParticipantResult>
```

 **Usage** 

```
const routingProfile: AgentRoutingProfile = await agentClient.getRoutingProfile();
const quickConnectResult: ListQuickConnectsResult = await agentClient.listQuickConnects(routingProfile.queues[0].queueARN);
const quickConnect: QuickConnect = quickConnectResult.quickConnects[1];
const addParticipantResult: AddParticipantResult = await contactClient.addParticipant(contactId, quickConnect);
```

 **Input** 


|  **Parameter**  |  **Type**  |  **Description**  | 
| --- | --- | --- | 
|  contactId Required  |  string  |  The id of the contact to which a participant needs to be added.  | 
|  quickConnect Required  |  QuickConnect  |  Its either AgentQuickConnect or QueueQuickConnect or PhoneNumberQuickConnect which contains endpointARN and name. Additionally PhoneNumberQuickConnect contains phoneNumber  | 

 **Output - AddParticipantResult** 


|  **Parameter**  |  **Type**  |  **Description**  | 
| --- | --- | --- | 
|  participantId  |  string  | The id of the newly added participant | 

 **Contact scope:** 

Requires an instance that is scoped to the contact that you pass in `contactId`, or an instance without a contact scope. For details, see [Connect Customer SDK Contact API](api-reference-3P-apps-contact-client.md).

 **Permissions required:** 

```
Contact.Details.Edit              
```