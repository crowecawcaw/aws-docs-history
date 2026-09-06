

# Set the visual mode of a user in Connect Customer agent workspace
<a name="3P-apps-user-requests-setvisualmode"></a>

Sets the visual mode (light, dark, or auto) for the user that's currently logged in to the Connect Customer agent workspace. The promise resolves once the visual mode change has been persisted.

 **Signature** 

```
setVisualMode(visualMode: VisualMode): Promise<void>
```

 **Usage** 

```
await settingsClient.setVisualMode("dark");
```

 **Input** 


| **Parameter** | **Type** | **Description** | 
| --- | --- | --- | 
| visualMode Required | VisualMode | The visual mode to set. One of "light", "dark", or "auto". | 

 **Permissions required:** 

```
*
```