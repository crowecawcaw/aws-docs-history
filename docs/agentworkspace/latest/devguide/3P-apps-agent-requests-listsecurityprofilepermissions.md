

# List the contact-handling security profile permissions for the agent in Connect Customer agent workspace
<a name="3P-apps-agent-requests-listsecurityprofilepermissions"></a>

Returns the list of contact-handling security profile permissions granted to the agent currently logged in to the Connect Customer agent workspace. Each permission is returned as a string identifier (for example, `outboundCall`, `outboundEmail`). Apps can use this to gate contact-handling functionality based on what the agent is authorized to do.

```
async listSecurityProfilePermissions(): Promise<string[]>
```

 **Permissions required:** 

```
*
```