

# Launch an application in Connect Customer agent workspace
<a name="api-reference-3P-apps-app-controller-launchapp"></a>

Launch the application in the agent workspace for the given application ARN or name. It supports optional launch options to fine tune the launch behavior.

For details on how the `options.scope` value controls an application's relationship to contacts, see [Application scoping for Connect Customer applications](getting-started-application-contact-scope.md).

 **Signature** 

```
launchApp(arnOrName: string, options?: AppLaunchOptions): Promise<AppInfo>
```

 **Usage** 

```
const applicationsConfig: AppConfig[] = await appControllerClient.getAppCatalog();
const appInfo: AppInfo = await appControllerClient.launchApp(applicationsConfig[0].arn);
```

 **Input** 


|  **Parameter**  |  **Type**  |  **Description**  | 
| --- | --- | --- | 
| arnOrName Required | string | The ARN or name of the application | 
| options.parameters | AppParameters | Key value pair of parameters passed to the application | 
| options.launchKey | string | A unique id to avoid duplicate application being launched with multiple invocation of launchApp API | 
| options.openInBackground | boolean | If set to true, the application is not set to focus after its launched | 
| options.appManagerData | AppManagerData | Key value pair of data passed to the AppManager that launches the application. Values must be strings, numbers, booleans, or nested objects of the same types. | 
| options.scope | ContactScope \| IdleScope | Indicates if the application is launched with idle i.e when there are no contacts or launched during an active contact | 

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

When the calling application instance has a scope (contact or idle), the launched instance receives the scope of the calling instance, whatever scope the target application was registered with. If the calling instance passes a different scope in `options.scope`, the request fails authorization. Pass the scope of the calling instance, or omit `options.scope`. An instance without a scope can pass any scope.

 **Permissions required:** 

```
*
```