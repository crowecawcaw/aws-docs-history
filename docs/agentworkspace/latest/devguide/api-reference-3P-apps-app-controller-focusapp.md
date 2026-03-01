# Focus an application in Amazon Connect Agent Workspace

Brings the application into focus in the Amazon Connect agent workspace for the given
application instance ID.

**Signature**

```

focusApp(instanceId: string): Promise<AppFocusResult>
```

**Usage**

```

const applicationFocusResult: AppFocusResult = await appControllerClient.focusApp(appInstanceId);
```

**Input**

| **Parameter**            | **Type** | **Description**                    |
| ------------------------ | -------- | ---------------------------------- |
| appInstanceId _Required_ | string   | The instance ID of the application |

**Output - AppFocusResult**

| **Parameter** | **Type** | **Description**                                |
| ------------- | -------- | ---------------------------------------------- | -------- | ------------------------------------------------------- |
| instanceId    | string   | The AmazonResourceName(ARN) of the application |
| result        | "queued" | "completed"                                    | "failed" | Indicates if the request is queued, completed or failed |

**Permissions required:**

```

*
```
