

# Close an application in Connect Customer agent workspace
<a name="api-reference-3P-apps-app-controller-closeapp"></a>

Closes the application for the given application instance ID in the Connect Customer agent workspace.

 **Signature** 

```
closeApp(instanceId: string): Promise<void>
```

 **Usage** 

```
await appControllerClient.closeApp(appInstanceId);
```

 **Input** 


|  **Parameter**  |  **Type**  |  **Description**  | 
| --- | --- | --- | 
| appInstanceId Required | string | The instance ID of the application | 

 **Permissions required:** 

```
*
```