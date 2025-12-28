# Unsubscribe a callback

function when an Amazon Connect Agent Workspace contact starts ACW

Unsubscribes the callback function from the contact StartingAcw event in the Amazon Connect
agent workspace.

**Signature**

```

offStartingAcw(handler: ContactStartingAcwHandler, contactId?: string)

```

**Usage**

```

contactClient.offStartingAcw(handler);

```
