

# Get the timestamp of the contact in Connect Customer agent workspace

Returns a `Date` object with the timestamp associated with when the contact was placed in the queue in the Connect Customer agent workspace.

```typescript
async getQueueTimestamp(contactId: string): Promise<Date | undefined>    
```

 **Contact scope:** 

Requires an instance that is scoped to the contact that you pass in `contactId`, or an instance without a contact scope. For details, see [Connect Customer SDK Contact API](api-reference-3P-apps-contact-client.md).

 **Permissions required:** 

```typescript
Contact.Details.View             
```