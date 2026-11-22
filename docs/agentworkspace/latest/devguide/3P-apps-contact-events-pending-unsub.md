

# Unsubscribe a callback function when an Connect Customer agent workspace contact turns to Pending state

Unsubscribes the callback function from Pending event in the Connect Customer agent workspace.

 **Signature** 

```typescript
offPending(handler: ContactPendingHandler, contactId?: string)
```

 **Usage** 

```typescript
contactClient.offPending(handler);
```