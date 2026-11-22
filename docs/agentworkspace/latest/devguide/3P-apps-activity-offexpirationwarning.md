

# Unsubscribe a callback function from the expiration warning event

Unsubscribes a callback function from the expiration warning event that is triggered when the agent is nearing expiration due to inactivity.

 **Signature** 

```typescript
offExpirationWarning(handler: ExpirationWarningHandler);
```

 **Usage** 

```typescript
sessionExpirationWarningClient.offExpirationWarning(handler);
```