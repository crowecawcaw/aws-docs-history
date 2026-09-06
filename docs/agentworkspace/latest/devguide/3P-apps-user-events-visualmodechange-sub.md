

# Subscribe a callback function when an Connect Customer agent workspace user's visual mode changes
<a name="3P-apps-user-events-visualmodechange-sub"></a>

Subscribes a callback function to-be-invoked whenever the user's visual mode changes in the Connect Customer agent workspace.

 **Signature** 

```
onVisualModeChange(handler: VisualModeChangedHandler)
```

 **Usage** 

```
const handler: VisualModeChangedHandler = async (data: VisualModeChanged) => {
    console.log("Visual mode changed! " + data.visualMode);
};

settingsClient.onVisualModeChange(handler);

// VisualModeChanged Structure
{
  visualMode: VisualMode;
  previous: {
    visualMode: VisualMode | null;
  };
}
```

 **Permissions required:** 

```
*
```