# Subscribe to expiration warning cleared event in Amazon Connect Agent Workspace

Subscribes a callback function to be invoked when the agent has acknowledged the
expiration warning and chooses to update their session.

**Signature**

```
onExpirationWarningCleared(handler: ExpirationWarningClearedHandler);
```

**Usage**

```
const handler: ExpirationWarningClearedHandler = () => {
    console.log("My session was extended after I was warned!");
}

sessionExpirationWarningClient.onExpirationWarningCleared(handler);
```
