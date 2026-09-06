

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

 **Permissions required:** 

```
Contact.CustomerDetails.View      
```