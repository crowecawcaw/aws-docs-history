# Inform Connect Customer that the agent is active

Sends a signal to the Connect Customer indicating that the agent is active and should
not be logged out. It takes a provider as a parameter.

**Signature**

```
sendActivity(provider): void
```

**Usage**

```
import { sendActivity } from '@amazon-connect/activity';

const handleActivity = () => {
   sendActivity(sampleProvider);
};

window.addEventListener("click", handleActivity);
```
