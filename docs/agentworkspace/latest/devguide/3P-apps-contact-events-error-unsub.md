

# Unsubscribe a callback function when an Connect Customer agent workspace contact turns to Error state

Unsubscribes the callback function from Error event in the Connect Customer agent workspace.

 **Signature** 

```typescript
offError(handler: ContactErrorHandler, contactId?: string)
```

 **Usage** 

```typescript
contactClient.offError(handler);
```