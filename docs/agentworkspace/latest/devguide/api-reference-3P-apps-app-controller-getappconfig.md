# Get the application configuration in Amazon Connect Agent Workspace

Returns the application configuration for the given application ARN in the Amazon Connect
agent workspace.

**Signature**

```

getAppConfig(appArn: string): Promise<AppConfig>
```

**Usage**

```

const applicationConfig: AppConfig = await appControllerClient.getAppConfig(arn);
```

**Input**

| **Parameter**  | **Type** | **Description**            |
| -------------- | -------- | -------------------------- |
| arn _Required_ | string   | The ARN of the application |

**Output - AppConfig**

| **Parameter**         | **Type**    | **Description**                                                          |
| --------------------- | ----------- | ------------------------------------------------------------------------ | --------------------------------------------------------------- |
| arn                   | string      | The AmazonResourceName(ARN) of the application                           |
| namespace             | string      | The immutable application namespace used at the time of<br>registration  |
| id                    | string      | The unique identifier of the application                                 |
| name                  | string      | Name of the application                                                  |
| description           | string      | Description of the application                                           |
| accessUrl             | string      | URL to access the application                                            |
| initializationTimeout | number      | The maximum time allowed to establish a connection with the<br>workspace |
| contactHandling.scope | PER_CONTACT | CROSS_CONTACTS                                                           | Indicates whether the application refreshes for each<br>contact |

**Permissions required:**

```

*
```
