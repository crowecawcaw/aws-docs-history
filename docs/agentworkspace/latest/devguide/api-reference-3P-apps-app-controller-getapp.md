# Get application information in Amazon Connect Agent Workspace

Returns the application information for the given application instance ID in the
Amazon Connect agent workspace.

**Signature**

```

getApp(instanceId: string): Promise<AppInfo>
```

**Usage**

```

const applicationInfo: AppInfo = await appControllerClient.getApp(appInstanceId);
```

**Input**

| **Parameter**            | **Type** | **Description**                    |
| ------------------------ | -------- | ---------------------------------- |
| appInstanceId _Required_ | string   | The instance ID of the application |

**Output - AppInfo**

| **Parameter**  | **Type**      | **Description**                                                                                        |
| -------------- | ------------- | ------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------- |
| instanceId     | string        | Unique ID of the application instance                                                                  |
| config         | Config        | The configuration of the application                                                                   |
| startTime      | Date          | Time when the application is launched                                                                  |
| state          | AppState      | Current state of the application                                                                       |
| appCreateOrder | number        | Sequentially incremented counter upon new application<br>launches                                      |
| accessUrl      | string        | Access URL of the application                                                                          |
| parameters     | AppParameters | undefined                                                                                              | Key value pair of parameters passed to the application                                                                    |
| launchKey      | string        | A unique id to avoid duplicate application being launched with<br>multiple invocation of launchApp API |
| scope          | ContactScope  | IdleScope                                                                                              | Indicates if the application is launched with idle i.e when there<br>are no contacts or launched during an active contact |

**Permissions required:**

```

*
```
