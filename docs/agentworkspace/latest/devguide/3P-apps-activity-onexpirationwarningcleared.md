

# Subscribe to expiration warning cleared event in Connect Customer agent workspace

Subscribes a callback function to be invoked when the agent has acknowledged the expiration warning and chooses to update their session.

 **Signature** 

```typescript
onExpirationWarningCleared(handler: ExpirationWarningClearedHandler);
```

 **Usage** 

```typescript
const handler: ExpirationWarningClearedHandler = () => {
    console.log("My session was extended after I was warned!");
}

sessionExpirationWarningClient.onExpirationWarningCleared(handler);
```

 **Permissions required:** 

```
*
```