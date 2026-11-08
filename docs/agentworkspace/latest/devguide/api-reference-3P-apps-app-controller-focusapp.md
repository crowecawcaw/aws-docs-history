

# Focus an application in Connect Customer agent workspace
<a name="api-reference-3P-apps-app-controller-focusapp"></a>

Brings the application into focus in the Connect Customer agent workspace for the given application instance ID.

 **Signature** 

```
focusApp(instanceId: string): Promise<AppFocusResult>
```

 **Usage** 

```
const applicationFocusResult: AppFocusResult = await appControllerClient.focusApp(appInstanceId);
```

 **Input** 


|  **Parameter**  |  **Type**  |  **Description**  | 
| --- | --- | --- | 
| instanceId Required | string | The instance ID of the application | 

 **Output - AppFocusResult** 


|  **Parameter**  |  **Type**  |  **Description**  | 
| --- | --- | --- | 
| instanceId | string | The instance ID of the application instance that the request focused | 
| result | "queued" \| "completed" \| "failed" | Indicates if the request is queued, completed or failed | 

 **Contact scope:** 

The target instance must belong to the AppManager of the calling instance, or to one of that AppManager's ancestors. Otherwise, the request fails. When the calling instance has a scope (contact or idle), it can act only on instances that have the same scope or no scope. An instance without a scope can act on instances of any scope.

 **Permissions required:** 

```
*
```