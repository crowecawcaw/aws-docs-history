

# Get the timestamp of the contact in Connect Customer agent workspace
<a name="3P-apps-contact-requests-getqueuetimestamp"></a>

Returns a `Date` object with the timestamp associated with when the contact was placed in the queue in the Connect Customer agent workspace.

```
async getQueueTimestamp(contactId: string): Promise<Date | undefined>    
```

 **Permissions required:** 

```
Contact.Details.View             
```