

# Get the instance details for a contact in Connect Customer agent workspace
<a name="3P-apps-contact-requests-getinstancedetails"></a>

Returns the AWS Region and the origin (URL scheme, host, and port) of the Connect Customer instance that handles the given contact.

 **Signature** 

```
getInstanceDetails(contactId: string): Promise<InstanceDetails>
```

 **Usage** 

```
const { region, origin }: InstanceDetails = await contactClient.getInstanceDetails(contactId);
```

 **Input** 


|  **Parameter**  |  **Type**  |  **Description**  | 
| --- | --- | --- | 
| contactId Required | string | The unique identifier for the contact | 

 **Output - InstanceDetails** 


|  **Parameter**  |  **Type**  |  **Description**  | 
| --- | --- | --- | 
| region | string | The AWS Region of the instance, for example us-east-1. | 
| origin | string | The origin of the instance in that Region. | 

 **Contact scope:** 

Requires an instance that is scoped to the contact that you pass in `contactId`, or an instance without a contact scope. For details, see [Connect Customer SDK Contact API](api-reference-3P-apps-contact-client.md).

 **Permissions required:** 

```
*
```