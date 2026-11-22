

# Unsubscribe a callback function when an Connect Customer agent workspace contact is missed

Unsubscribes the callback function from the contact missed event.

 **Signature** 

```typescript
offMissed(handler: ContactMissedHandler, contactId?: string)
```

 **Usage** 

```typescript
contactClient.offMissed(handler);
```