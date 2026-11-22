

# Unsubscribe a callback function when an Connect Customer agent workspace contact starts ACW

Unsubscribes the callback function from the contact StartingAcw event in the Connect Customer agent workspace.

 **Signature** 

```typescript
offStartingAcw(handler: ContactStartingAcwHandler, contactId?: string)
```

 **Usage** 

```typescript
contactClient.offStartingAcw(handler);              
```