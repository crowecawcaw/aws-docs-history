

# Subscribe to session extension errors in Connect Customer agent workspace
<a name="3P-apps-activity-onsessionextensionerror"></a>

Subscribes a callback function to be invoked when an attempt to extend the agent's session fails.

 **Signature** 

```
onSessionExtensionError(handler: SessionExtensionErrorHandler);
```

 **Usage** 

```
const handler: SessionExtensionErrorHandler = (details: SessionExtensionErrorData) => {
    console.log("Failed to extend my session!", details);
}

sessionExpirationWarningClient.onSessionExtensionError(handler);

// SessionExtensionErrorData Structure
{
    isWarningActive: boolean;
    errorDetails: Record<string, unknown>;
}
```