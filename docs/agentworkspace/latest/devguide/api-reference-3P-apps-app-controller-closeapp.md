

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
| instanceId Required | string | The instance ID of the application | 

 **Contact scope:** 

The target instance must belong to the AppManager of the calling instance, or to one of that AppManager's ancestors. Otherwise, the request fails. When the calling instance has a scope (contact or idle), it can act only on instances that have the same scope or no scope. An instance without a scope can act on instances of any scope.

 **Permissions required:** 

```
*
```