

# Gets the phone number of the initial customer connection in Connect Customer agent workspace
<a name="3P-apps-voice-requests-getinitialcustomerphonenumber"></a>

 Gets the phone number of the initial customer connection. Applicable only for voice contacts. 

 **Signature** 

```
getInitialCustomerPhoneNumber(contactId: string): Promise<string>
```

 **Usage** 

```
const initialCustomerPhoneNumber: string = await voiceClient.getInitialCustomerPhoneNumber(contactId);        
```

 **Input** 


|  **Parameter**  |  **Type**  |  **Description**  | 
| --- | --- | --- | 
|  contactId Required  |  string  |  The id of the contact for which the data is requested.  | 

 **Contact scope:** 

Requires an instance that is scoped to the contact that you pass in `contactId`, or an instance without a contact scope. For details, see [Connect Customer SDK Contact API](api-reference-3P-apps-contact-client.md).

 **Permissions required:** 

```
Contact.CustomerDetails.View      
```