

# Get the queue of the contact in Connect Customer agent workspace
<a name="3P-apps-contact-requests-getqueue"></a>

Returns the queue associated with the contact in the Connect Customer agent workspace. The `Queue` object has the following fields:
+ `name`: The name of the queue.
+ `queueARN`: The ARN of the queue.
+ `queueId`: Alias for `queueARN`.

```
async getQueue(contactId: string): Promise<Queue>     
```

 **Contact scope:** 

Requires an instance that is scoped to the contact that you pass in `contactId`, or an instance without a contact scope. For details, see [Connect Customer SDK Contact API](api-reference-3P-apps-contact-client.md).

 **Permissions required:** 

```
Contact.Details.View             
```