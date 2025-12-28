# Subscribe to session expiration

warning event in Amazon Connect Agent Workspace

Subscribes a callback function to be invoked whenever the agent's session is about to
expire due to inactivity.

**Signature**

```
onExpirationWarning(handler: ExpirationWarningHandler);
```

**Usage**

```
const handler: ExpirationWarningHandler = (data: SessionExpirationInformation) => {
    console.log("Agent's session expiring at:", data);
}

sessionExpirationWarningClient.onExpirationWarning(handler);

// SessionExpirationInformation Structure
{
   expiration: number;
}
```
