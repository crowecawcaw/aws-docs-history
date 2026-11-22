

# Get the duration of the contact state in Connect Customer agent workspace

Returns the duration of the contact state in milliseconds relative to local time, in the Connect Customer agent workspace. This takes into account time skew between the JS client and the Connect Customer backend servers.

```typescript
async getStateDuration(contactId: string): Promise<number>     
```

 **Contact scope:** 

Requires an instance that is scoped to the contact that you pass in `contactId`, or an instance without a contact scope. For details, see [Connect Customer SDK Contact API](api-reference-3P-apps-contact-client.md).

 **Permissions required:** 

```typescript
Contact.Details.View             
```