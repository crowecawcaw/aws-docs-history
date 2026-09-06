

# Check whether auto-accept is enabled for the given contact in Connect Customer agent workspace
<a name="3P-apps-contact-requests-isautoacceptenabled"></a>

Returns whether auto-accept is enabled for the given contact. When auto-accept is enabled, an incoming contact is automatically accepted on the agent's behalf without requiring an explicit [accept()](3P-apps-contact-requests-accept.md) call.

 **Signature** 

```
isAutoAcceptEnabled(contactId: string): Promise<boolean>
```

 **Usage** 

```
const enabled: boolean = await contactClient.isAutoAcceptEnabled(contactId);
```

 **Input** 


| **Parameter** | **Type** | **Description** | 
| --- | --- | --- | 
| contactId Required | string | The id of the contact to check. | 

 **Permissions required:** 

```
*
```