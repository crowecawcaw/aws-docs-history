# Unsubscribe a callback

function from the session extension error event

Unsubscribes a callback function from the session extension error event that is
triggered when the agent's session fails to update.

**Signature**

```
offSessionExtensionError(handler: SessionExtensionErrorHandler);
```

**Usage**

```
sessionExpirationWarningClient.offSessionExtensionError(handler);
```
