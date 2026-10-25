

# Disconnect the agent from the given contact in Connect Customer agent workspace
<a name="3P-apps-contact-requests-disconnectself"></a>

Disconnects the currently logged-in agent from the given contact. Other participants on the contact (such as the customer) remain connected.

 **Signature** 

```
disconnectSelf(contactId: string): Promise<void>
```

 **Usage** 

```
await contactClient.disconnectSelf(contactId);
```

 **Input** 


| **Parameter** | **Type** | **Description** | 
| --- | --- | --- | 
| contactId Required | string | The id of the contact to disconnect the agent from. | 

 **Contact scope:** 

Requires an instance that is scoped to the contact that you pass in `contactId`, or an instance without a contact scope. For details, see [Connect Customer SDK Contact API](api-reference-3P-apps-contact-client.md).

 **Permissions required:** 

```
*
```