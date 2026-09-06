

# Gets the outbound call permission configured for the agent in Connect Customer agent workspace
<a name="3P-apps-voice-requests-getoutboundcallpermission"></a>

Gets true if the agent has the security profile permission for making outbound calls, false otherwise.

 **Signature** 

```
getOutboundCallPermission(): Promise<boolean>
```

 **Usage** 

```
const outboundCallPermission: boolean = await voiceClient.getOutboundCallPermission();
```

 **Permissions required:** 

```
User.Configuration.View      
```