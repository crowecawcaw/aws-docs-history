

# Get the duration of the contact state in Connect Customer agent workspace
<a name="3P-apps-contact-requests-getstateduration"></a>

Returns the duration of the contact state in milliseconds relative to local time, in the Connect Customer agent workspace. This takes into account time skew between the JS client and the Connect Customer backend servers.

```
async getStateDuration(contactId: string): Promise<number>     
```

 **Contact scope:** 

Requires an instance that is scoped to the contact that you pass in `contactId`, or an instance without a contact scope. For details, see [Connect Customer SDK Contact API](api-reference-3P-apps-contact-client.md).

 **Permissions required:** 

```
Contact.Details.View             
```