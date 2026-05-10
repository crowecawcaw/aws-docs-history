# Close an application in Connect Customer Customer agent workspace

Closes the application for the given application instance ID in the Connect Customer
Customer agent workspace.

**Signature**

```

closeApp(instanceId: string): Promise<void>
```

**Usage**

```

await appControllerClient.closeApp(appInstanceId);
```

**Input**

| **Parameter**            | **Type** | **Description**                    |
| ------------------------ | -------- | ---------------------------------- |
| appInstanceId _Required_ | string   | The instance ID of the application |

**Permissions required:**

```

*
```
