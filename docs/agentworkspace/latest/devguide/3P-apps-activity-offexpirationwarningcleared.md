# Unsubscribe a callback function from the expiration warning cleared event

Unsubscribes a callback function from the expiration warning cleared event that is
triggered when the expiration warning is dismissed due to the agent choosing to stay
logged in.

**Signature**

```
offExpirationWarningCleared(handler: ExpirationWarningClearedHandler);
```

**Usage**

```
sessionExpirationWarningClient.offExpirationWarningCleared(handler);
```
