

# Get the duration of the contact state in Connect Customer agent workspace
<a name="3P-apps-contact-requests-getstateduration"></a>

Returns the duration of the contact state in milliseconds relative to local time, in the Connect Customer agent workspace. This takes into account time skew between the JS client and the Connect Customer backend servers.

```
async getStateDuration(contactId: string): Promise<number>     
```

 **Permissions required:** 

```
Contact.Details.View             
```