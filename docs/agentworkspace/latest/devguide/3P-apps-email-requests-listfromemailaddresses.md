

# List the from email addresses available for an email contact in Connect Customer agent workspace
<a name="3P-apps-email-requests-listfromemailaddresses"></a>

Lists the email addresses that the agent can use as the from address of an email contact. The email addresses are the ones associated with the queue of the contact that you pass in `contactId`. If that contact does not have a queue, the agent's default outbound queue is used. Returns an object that includes:
+ `emailAddresses: FromEmailAddress[]`: An array of FromEmailAddress objects, each an email address that the email contact can be sent from
+ `nextToken?: string`: The token for the next set of results; use the value returned in the previous response in the next request to retrieve the next set of results

 **Signature** 

```
listFromEmailAddresses(params: ListFromEmailAddressesParams): Promise<{ emailAddresses: FromEmailAddress[]; nextToken?: string; }>
```

 **ListFromEmailAddressesParams Properties** 


|  **Parameter**  |  **Type**  |  **Description**  | 
| --- | --- | --- | 
| contactId | string | The id of the email contact to retrieve from email addresses for | 
| maxResults | number | Optional. The max number of email addresses to return; Default is 50. Maximum value of 50. | 
| nextToken | string | Optional. The token for the next set of results. Use the value returned in the previous response in the next request to retrieve the next set of results. | 

 **FromEmailAddress Properties** 


|  **Parameter**  |  **Type**  |  **Description**  | 
| --- | --- | --- | 
| id | string | The unique identifier of the email address | 
| emailAddress | string | The email address | 
| displayName | string | Optional. The name that is displayed inside the recipient's mailbox | 
| description | string | Optional. The description of the email address | 
| isDefaultOutboundEmail | boolean | Optional. Whether this is the default outbound email address of the queue | 

 **Usage** 

```
const { emailAddresses, nextToken } = await emailClient.listFromEmailAddresses({
   contactId: draftContactId, // The draft email contact that you want to send
   maxResults: 50,
});

const defaultFromAddress = emailAddresses.find(
   (address) => address.isDefaultOutboundEmail,
);
```

 **Contact scope:** 

Not restricted by the contact scope of the instance. The `contactId` that you pass is not checked against the contact scope. For details, see [Connect Customer SDK Contact API](api-reference-3P-apps-contact-client.md).

 **Permissions required:** 

```
*
```