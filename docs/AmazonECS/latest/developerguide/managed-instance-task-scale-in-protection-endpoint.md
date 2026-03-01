# Amazon ECS task scale-in protection endpoint

The Amazon ECS container agent automatically injects the `ECS_AGENT_URI`
environment variable into the containers of Amazon ECS tasks to provide a method to
interact with the container agent API endpoint.

We recommend using the Amazon ECS container agent endpoint for tasks that can
self-determine the need to be protected.

When a container starts processing work, you can set the
`protectionEnabled` attribute using the task scale-in protection
endpoint path `$ECS_AGENT_URI/task-protection/v1/state` from within the
container.

Use a PUT request to this URI from within a container to set task scale-in
protection. A GET request to this URI returns the current protection status of a
task.

## Task scale-in protection request parameters

You can set task scale-in protection using the
`${ECS_AGENT_URI}/task-protection/v1/state` endpoint with the
following request parameters.

`ProtectionEnabled`

Specify `true` to mark a task for protection. Specify
`false` to remove protection and make the task eligible
for termination.

Type: Boolean

Required: Yes

`ExpiresInMinutes`

The number of minutes the task is protected. You can specify a
minimum of 1 minute to up to 2,880 minutes (48 hours). During this time
period, your task will not be terminated by scale-in events from service
Auto Scaling or deployments. After this time period lapses, the
`protectionEnabled` parameter is set to
`false`.

If you don't specify the time, then the task is automatically
protected for 120 minutes (2 hours).

Type: Integer

Required: No

The following examples show how to set task protection with different
durations.

**Example of how to protect a task with the default time
period**

This example shows how to protect a task with the default time period of 2
hours.

```
curl --request PUT --header 'Content-Type: application/json' ${ECS_AGENT_URI}/task-protection/v1/state --data '{"ProtectionEnabled":true}'
```

**Example of how to protect a task for 60
minutes**

This example shows how to protect a task for 60 minutes using the
`expiresInMinutes` parameter.

```
curl --request PUT --header 'Content-Type: application/json' ${ECS_AGENT_URI}/task-protection/v1/state --data '{"ProtectionEnabled":true,"ExpiresInMinutes":60}'
```

**Example of how to protect a task for 24
hours**

This example shows how to protect a task for 24 hours using the
`expiresInMinutes` parameter.

```
curl --request PUT --header 'Content-Type: application/json' ${ECS_AGENT_URI}/task-protection/v1/state --data '{"ProtectionEnabled":true,"ExpiresInMinutes":1440}'
```

The PUT request returns the following response.

```
{
  "protection": {
    "ExpirationDate": "2023-12-20T21:57:44.837Z",
    "ProtectionEnabled": true,
    "TaskArn": "arn:aws:ecs:us-west-2:111122223333:task/1234567890abcdef0"
  }
}
```

## Task scale-in protection response parameters

The following information is returned from the task scale-in protection endpoint
`${ECS_AGENT_URI}/task-protection/v1/state` in the JSON
response.

`ExpirationDate`

The epoch time when protection for the task will expire. If the
task is not protected, this value is null.

`ProtectionEnabled`

The protection status of the task. If scale-in protection is
enabled for a task, the value is `true`. Otherwise, it is
`false`.

`TaskArn`

The full Amazon Resource Name (ARN) of the task that the container belongs
to.

The following example shows the details returned for a protected task.

```
curl --request GET ${ECS_AGENT_URI}/task-protection/v1/state
```

```
{
    "protection":{
        "ExpirationDate":"2023-12-20T21:57:44Z",
        "ProtectionEnabled":true,
        "TaskArn":"arn:aws:ecs:us-west-2:111122223333:task/1234567890abcdef0"
    }
}
```

The following information is returned when a failure occurs.

`Arn`

The full Amazon Resource Name (ARN) of the task.

`Detail`

The details related to the failure.

`Reason`

The reason for the failure.

The following example shows the details returned for a task that is not
protected.

```
{
    "failure":{
        "Arn":"arn:aws:ecs:us-west-2:111122223333:task/1234567890abcdef0",
        "Detail":null,
        "Reason":"TASK_NOT_VALID"
    }
}
```

The following information is returned when an exception occurs.

`requestID`

The AWS request ID for the Amazon ECS API call that results in an
exception.

`Arn`

The full Amazon Resource Name (ARN) of the task or service.

`Code`

The error code.

`Message`

The error message.

###### Note

If a `RequestError` or `RequestTimeout`
error appears, it is likely that it's a networking issue. Try
using VPC endpoints for Amazon ECS.

The following example shows the details returned when an error occurs.

```
{
    "requestID":"12345-abc-6789-0123-abc",
    "error":{
        "Arn":"arn:aws:ecs:us-west-2:555555555555:task/my-cluster-name/1234567890abcdef0",
        "Code":"AccessDeniedException",
        "Message":"User: arn:aws:sts::444455556666:assumed-role/my-ecs-task-role/1234567890abcdef0 is not authorized to perform: ecs:GetTaskProtection on resource: arn:aws:ecs:us-west-2:555555555555:task/test/1234567890abcdef0 because no identity-based policy allows the ecs:GetTaskProtection action"
    }
}
```

The following error appears if the Amazon ECS agent is unable to get a response
from the Amazon ECS endpoint for reasons such as network issues or the Amazon ECS control
plane is down.

```
{
  "error": {
    "Arn": "arn:aws:ecs:us-west-2:555555555555:task/my-cluster-name/1234567890abcdef0",
    "Code": "RequestCanceled",
    "Message": "Timed out calling Amazon ECS Task Protection API"
  }
}
```

The following error appears when the Amazon ECS agent gets a throttling exception
from Amazon ECS.

```
{
  "requestID": "12345-abc-6789-0123-abc",
  "error": {
    "Arn": "arn:aws:ecs:us-west-2:555555555555:task/my-cluster-name/1234567890abcdef0",
    "Code": "ThrottlingException",
    "Message": "Rate exceeded"
  }
}
```
