

# Get application information in Connect Customer agent workspace
<a name="api-reference-3P-apps-app-controller-getapp"></a>

Returns the application information for the given application instance ID in the Connect Customer agent workspace.

 **Signature** 

```
getApp(instanceId: string): Promise<AppInfo>
```

 **Usage** 

```
const applicationInfo: AppInfo = await appControllerClient.getApp(appInstanceId);
```

 **Input** 


|  **Parameter**  |  **Type**  |  **Description**  | 
| --- | --- | --- | 
| instanceId Required | string | The instance ID of the application | 

 **Output - AppInfo** 


|  **Parameter**  |  **Type**  |  **Description**  | 
| --- | --- | --- | 
| instanceId | string | Unique ID of the application instance | 
| config | Config | The configuration of the application | 
| startTime | Date | Time when the application is launched | 
| state | AppState | Current state of the application | 
| appCreateOrder | number | Sequentially incremented counter upon new application launches | 
| appManagerId | string | The ID of the AppManager that manages the application instance | 
| parameters | AppParameters \| undefined | Key value pair of parameters passed to the application | 
| launchKey Optional | string | A unique id to avoid duplicate application being launched with multiple invocation of launchApp API | 
| launchedBy Optional | LaunchSource | The source that launched the application instance. LaunchSource is { name: string \| undefined } combined with either { type: "external"; connectionId: string } or { type: "internal" }. | 
| scope Optional | ContactScope \| IdleScope | Indicates if the application is launched with idle i.e when there are no contacts or launched during an active contact | 

 **Contact scope:** 

The target instance must belong to the AppManager of the calling instance, or to one of that AppManager's ancestors. Otherwise, the request fails. When the calling instance has a scope (contact or idle), it can act only on instances that have the same scope or no scope. An instance without a scope can act on instances of any scope.

 **Permissions required:** 

```
*
```