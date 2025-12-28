# Launch an

application in Amazon Connect Agent Workspace

Launch the application in the agent workspace for the given application ARN or name. It
supports optional launch options to fine tune the launch behavior.

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

| **Parameter**            | **Type**      | **Description**                                                                                        |
| ------------------------ | ------------- | ------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------- |
| arnOrName _Required_     | string        | The ARN or name of the application                                                                     |
| options.parameters       | AppParameters | Key value pair of parameters passed to the application                                                 |
| options.launchKey        | string        | A unique id to avoid duplicate application being launched with<br>multiple invocation of launchApp API |
| options.openInBackground | boolean       | If set to true, the application won't be set to focus after its<br>launched                            |
| options.scope            | ContactScope  | IdleScope                                                                                              | Indicates if the application is launched with idle i.e when there<br>are no contacts or launched during an active contact |

**Output - AppInfo**

| **Parameter**  | **Type**      | **Description**                                                                                     |
| -------------- | ------------- | --------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------- |
| instanceId     | string        | Unique ID of the application instance                                                               |
| config         | Config        | The configuration of the application                                                                |
| startTime      | Date          | Time when the application is launched                                                               |
| state          | AppState      | Current state of the application                                                                    |
| appCreateOrder | number        | Sequentially incremented counter upon new application launches                                      |
| accessUrl      | string        | Access URL of the application                                                                       |
| parameters     | AppParameters | undefined                                                                                           | Key value pair of parameters passed to the application                                                                 |
| launchKey      | string        | A unique id to avoid duplicate application being launched with multiple invocation of launchApp API |
| scope          | ContactScope  | IdleScope                                                                                           | Indicates if the application is launched with idle i.e when there are no contacts or launched during an active contact |

**Permissions required:**

```

*
```
