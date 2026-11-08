

# Get all active application information in Connect Customer agent workspace
<a name="api-reference-3P-apps-app-controller-getapps"></a>

Returns the application information for the active application instances that share the AppManager of the calling instance in the Connect Customer agent workspace. When the calling instance has a scope (contact or idle), the result includes only the instances that have the same scope and the instances that have no scope.

 **Signature** 

```
getApps(): Promise<AppInfo[]>
```

 **Usage** 

```
const applicationInfo: AppInfo[] = await appControllerClient.getApps();
```

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

 **Permissions required:** 

```
*
```