

# Inform Connect Customer that the agent is active

Sends a signal to the Connect Customer indicating that the agent is active and should not be logged out. It takes a provider as a parameter.

 **Signature** 

```typescript
sendActivity(provider: AmazonConnectProvider): void
```

 **Usage** 

```typescript
import { sendActivity } from '@amazon-connect/activity'; 

const handleActivity = () => {
   sendActivity(sampleProvider);
};

window.addEventListener("click", handleActivity);
```

 **Permissions required:** 

```
*
```