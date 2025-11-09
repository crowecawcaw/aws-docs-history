# Logging and monitoring in AWS CloudShell

This topic describes how you can log and monitor AWS CloudShell activity and performance with
CloudTrail.

## Monitoring activity with CloudTrail

AWS CloudShell is integrated with AWS CloudTrail, a service that provides a record of actions taken by
a user, role, or AWS service in AWS CloudShell. CloudTrail captures all API calls for AWS CloudShell as
events. The calls captured include calls from the AWS CloudShell console and code calls to the
AWS CloudShell API.

If you create a trail, you can enable the continuous delivery of CloudTrail events to an
Amazon Simple Storage Service (Amazon S3) bucket. This includes events for AWS CloudShell.

If you don't configure a trail, you can still view the most recent events in the CloudTrail
console in **Event history**. Using the information collected by CloudTrail, you
can discover a variety of information about a request. For example, you can determine the
request that was made to AWS CloudShell, you can learn the IP address that the request was
made from, who made the request, and when it was made.

## AWS CloudShell in CloudTrail

The following table lists the AWS CloudShell events that are saved in the CloudTrail log file.

###### Note

AWS CloudShell event that includes:

- `*` indicates that it is a non-mutating (read-only) API call.
- The word `Environment` relates to the lifecycle of the compute
  environment that hosts the shell experience.
- The word `Layout` restores all the browser tabs in the CloudShell
  terminal.

| CloudShell Events in CloudTrail   | Event name                                                                                                                                                                                        | Description |
| --------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------- |
| `createEnvironment`               | Occurs when a CloudShell environment is created.                                                                                                                                                  |
| `createSession`                   | Occurs when a CloudShell environment is connected from the AWS Management Console.                                                                                                                |
| `deleteEnvironment`               | Occurs when a CloudShell environment is deleted.                                                                                                                                                  |
| `deleteSession`                   | Occurs when the session in the CloudShell tab that is running in the current<br>browser tab is deleted.                                                                                           |
| `getEnvironmentStatus*`           | Occurs when the status of a CloudShell environment is retrieved.                                                                                                                                  |
| `getFileDownloadUrls*`            | Occurs when pre-signed Amazon S3 URLs that are used to download files through<br>CloudShell using the CloudShell web interface are generated.                                                     |
| `getFileUploadUrls*`              | Occurs when pre-signed Amazon S3 URLs that are used to upload files through<br>CloudShell using the CloudShell web interface are generated.                                                       |
| `cloudshell:DescribeEnvironments` | Describes the environments.                                                                                                                                                                       |
| `getLayout*`                      | Occurs when the CloudShell layout at the start of the session is<br>retrieved.                                                                                                                    |
| `putCredentials`                  | Occurs when the credentials used to log in to the AWS Management Console to CloudShell are<br>forwarded.                                                                                          |
| `redeemCode*`                     | Occurs when the workflow to retrieve refresh token in the CloudShell<br>environment begins. You can later use this token in the `putCredentials`<br>command to access the CloudShell environment. |
| `sendHeartBeat`                   | Occurs to confirm that the CloudShell session is active.                                                                                                                                          |
| `startEnvironment`                | Occurs when a CloudShell environment is started.                                                                                                                                                  |
| `stopEnvironment`                 | Occurs when a running CloudShell environment is stopped.                                                                                                                                          |
| `updateLayout`                    | Occurs when the current layout from the web application in the backend is<br>saved.                                                                                                               |

Events that include the word "Layout" restore all the browser tabs in the CloudShell
terminal.

**EventBridge rules for AWS CloudShell actions**

With EventBridge rules, you specify a target action to take when EventBridge receives an event that
matches the rule. You can define a rule that specifies a target action to take based on an
AWS CloudShell action that's recorded as an event in a CloudTrail log file.

For example, you can [create EventBridge rules with
AWS CLI](../../../cli/latest/reference/events/put-rule.md "../../../cli/latest/reference/events/put-rule.md") using the `put-rule` command. A `put-rule` call must
contain at least an EventPattern or ScheduleExpression. Rules with EventPatterns are triggered
when a matching event is observed. The EventPattern for AWS CloudShell events:

```
{ "source": [ "aws.cloudshell" ], "detail-type": [ "AWS API Call via CloudTrail" ], "detail": { "eventSource": [ "cloudshell.amazonaws.com" ] } }
```

For more information, see [Events and Event Patterns in EventBridge](../../../eventbridge/latest/userguide/eb-event-patterns.md "../../../eventbridge/latest/userguide/eb-event-patterns.md") in the
_Amazon EventBridge User Guide_.
