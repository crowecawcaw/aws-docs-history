# Handling App Runner events in EventBridge

Using Amazon EventBridge, you can set up event-driven rules that monitor a stream of real-time data from your AWS App Runner service for certain patterns. When a
pattern for a rule is matched, EventBridge initiates an action in a target such as AWS Lambda, Amazon ECS, AWS Batch, and Amazon SNS. For example, you can set a rule for
sending out email notifications by signaling an Amazon SNS topic whenever a deployment to your service fails. Or, you can set a Lambda function to notify a Slack
channel whenever a service update fails. For more information about EventBridge, see [Amazon EventBridge User Guide](../../../eventbridge/latest/userguide.md "../../../eventbridge/latest/userguide.md").

App Runner sends the following event types to EventBridge

- _Service status change_ – A change in the status of an App Runner service. For example, a service status changed to
  `DELETE_FAILED`.
- _Service operation status change_ – A change in the status of a long, asynchronous operation on an App Runner service. For
  example, a service started to create, a service update successfully completed, or a service deployment completed with errors.

## Creating an EventBridge rule to act on App Runner events

An EventBridge _event_ is an object that defines some standard EventBridge fields, such as the source AWS service and the detail (event) type,
and an event-specific set of fields with the event details. To create an EventBridge rule, you use the EventBridge console to define an _event
pattern_ (which events should bet tracked) and specify a _target action_ (what should be done on a match). An event pattern
is similar to the events that it matches. You specify a subset of fields to match, and for each field, you specify a list of possible values. This topic
provides examples of App Runner events and event patterns.

For more information about creating EventBridge rules, see [Creating a rule for an AWS
service](../../../eventbridge/latest/userguide/create-eventbridge-rule.md "../../../eventbridge/latest/userguide/create-eventbridge-rule.md") in the _Amazon EventBridge User Guide_.

###### Note

Some services support _pre-defined patterns_ in EventBridge. This simplifies how an event pattern is created. You select field values on
a form, and EventBridge generates the pattern for you. At this time, App Runner doesn't support pre-defined patterns. You have to enter the pattern as a JSON object.
You can use the examples in this topic as a starting point.

## App Runner event examples

These are some examples to events that App Runner sends to EventBridge.

- A service status change event. Specifically, a service that changed from the `OPERATION_IN_PROGRESS` to the `RUNNING`
  status.

```
{
  "version": "0",
  "id": "6a7e8feb-b491-4cf7-a9f1-bf3703467718",
  "detail-type": "AppRunner Service Status Change",
  "source": "aws.apprunner",
  "account": "111122223333",
  "time": "2021-04-29T11:54:23Z",
  "region": "us-east-2",
  "resources": [
    "arn:aws:apprunner:us-east-2:123456789012:service/my-app/8fe1e10304f84fd2b0df550fe98a71fa"
  ],
  "detail": {
    "previousServiceStatus": "OPERATION_IN_PROGRESS",
    "currentServiceStatus": "RUNNING",
    "serviceName": "my-app",
    "serviceId": "8fe1e10304f84fd2b0df550fe98a71fa",
    "message": "Service status is set to RUNNING.",
    "severity": "INFO"
  }
}
```

- An operation status change event. Specifically, an `UpdateService` operation that completed successfully.

```
{
  "version": "0",
  "id": "6a7e8feb-b491-4cf7-a9f1-bf3703467718",
  "detail-type": "AppRunner Service Operation Status Change",
  "source": "aws.apprunner",
  "account": "111122223333",
  "time": "2021-04-29T18:43:48Z",
  "region": "us-east-2",
  "resources": [
    "arn:aws:apprunner:us-east-2:123456789012:service/my-app/8fe1e10304f84fd2b0df550fe98a71fa"
  ],
  "detail": {
    "operationStatus": "UpdateServiceCompletedSuccessfully",
    "serviceName": "my-app",
    "serviceId": "8fe1e10304f84fd2b0df550fe98a71fa",
    "message": "Service update completed successfully. New application and configuration is deployed.",
    "severity": "INFO"
  }
}
```

## App Runner event pattern examples

The following examples demonstrate event patterns that you can use in EventBridge rules to match one or more App Runner events. An event pattern is similar to an
event. Include only the fields that you want to match, and provide a list instead of a scalar to each one.

- Match all service status change events for services of a specific account, where the service is no longer in `RUNNING` status.

```
{
  "detail-type": [ "AppRunner Service Status Change" ],
  "source": [ "aws.apprunner" ],
  "account": [ "111122223333" ],
  "detail": {
    "previousServiceStatus": [ "RUNNING" ]
  }
}
```

- Match all operation status change events for services of a specific account, where the operation failed.

```
{
  "detail-type": [ "AppRunner Service Operation Status Change" ],
  "source": [ "aws.apprunner" ],
  "account": [ "111122223333" ],
  "detail": {
    "operationStatus": [
      "CreateServiceFailed",
      "DeleteServiceFailed",
      "UpdateServiceFailed",
      "DeploymentFailed",
      "PauseServiceFailed",
      "ResumeServiceFailed"
    ]
  }
}
```

## App Runner event reference

### Service status change

A service status change event has `detail-type` set to `AppRunner Service Status Change`. It has the following detail
fields and values:

```
"serviceId": "`your service ID`",
"serviceName": "`your service name`",
"message": "Service status is set to `CurrentStatus`.",
"previousServiceStatus": "`any valid service status`",
"currentServiceStatus": "`any valid service status`",
"severity": "`varies`"
```

### Operation status change

An operation status change event has `detail-type` set to `AppRunner Service Operation Status Change`. It has the
following detail fields and values:

```
"operationStatus": "`see following table`",
"serviceName": "`your service name`",
"serviceId": "`your service ID`",
"message": "`see following table`",
"severity": "`varies`"
```

The following table lists all possible status codes and related messages.

| Status                                                                | Message                                                                               |
| --------------------------------------------------------------------- | ------------------------------------------------------------------------------------- |
| `CreateServiceStarted`                                                | Service creation started.                                                             |
| `CreateServiceCompletedSuccessfully`                                  | Service creation completed successfully.                                              |
| `CreateServiceFailed`                                                 | Service creation failed. For details, see service logs.                               |
| `DeleteServiceStarted`                                                | Service deletion started.                                                             |
| `DeleteServiceCompletedSuccessfully`                                  | Service deletion completed successfully.                                              |
| `DeleteServiceFailed`                                                 | Service deletion failed.                                                              |
| `UpdateServiceStarted`                                                |                                                                                       |
| `UpdateServiceCompletedSuccessfully`                                  | Service update completed successfully. New application and configuration is deployed. |
| Service update completed successfully. New configuration is deployed. |
| `UpdateServiceFailed`                                                 | Service update failed. For details, see service logs.                                 |
| `DeploymentStarted`                                                   | Deployment started.                                                                   |
| `DeploymentCompletedSuccessfully`                                     | Deployment completed successfully.                                                    |
| `DeploymentFailed`                                                    | Deployment failed. For details, see service logs.                                     |
| `PauseServiceStarted`                                                 | Service pause started.                                                                |
| `PauseServiceCompletedSuccessfully`                                   | Service pause completed successfully.                                                 |
| `PauseServiceFailed`                                                  | Service pause failed.                                                                 |
| `ResumeServiceStarted`                                                | Service resume started.                                                               |
| `ResumeServiceCompletedSuccessfully`                                  | Service resume completed successfully.                                                |
| `ResumeServiceFailed`                                                 | Service resume failed.                                                                |
