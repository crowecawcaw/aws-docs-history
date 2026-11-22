

# Unsubscribe a callback function from the session extension error event

Unsubscribes a callback function from the session extension error event that is triggered when the agent's session fails to update.

 **Signature** 

```typescript
offSessionExtensionError(handler: SessionExtensionErrorHandler);
```

 **Usage** 

```typescript
sessionExpirationWarningClient.offSessionExtensionError(handler);
```