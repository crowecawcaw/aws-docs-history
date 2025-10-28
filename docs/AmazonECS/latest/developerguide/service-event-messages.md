# Viewing Amazon ECS service event messages

When troubleshooting a problem with a service, the first place you should check for the diagnostic information is the service event log. You can view service events using the
`DescribeServices` API, the AWS CLI, or by using the AWS Management Console.

When viewing service event messages using the Amazon ECS API, only the events from the service scheduler are
returned. These include the most recent task placement and instance health events. However, the Amazon ECS
console displays service events from the following sources.

- Task placement and instance health events from the Amazon ECS service scheduler. These events have a
  prefix of **service `(service-name)`**. To ensure that
  this event view is helpful, we only show the `100` most recent events. Duplicate
  event messages are omitted until either the cause is resolved, or six hours passes. If the cause is
  not resolved within six hours, you receive another service event message for that cause.
- Service Auto Scaling events. These events have a prefix of **Message** and occur only when a service is
  configured with an Application Auto Scaling scaling policy.
  Use the following steps to view your current service event messages.

Console

1. Open the console at
   [https://console.aws.amazon.com/ecs/v2](https://console.aws.amazon.com/ecs/v2 "https://console.aws.amazon.com/ecs/v2").
2. In the navigation pane, choose **Clusters**.
3. On the **Clusters** page, choose the cluster.
4. Choose the service to inspect.
5. On the **Events** tab, view the messages.

AWS CLI
Use the [describe-services](../../../cli/latest/reference/ecs/describe-services.md "../../../cli/latest/reference/ecs/describe-services.md") command to view the service event messages for a specified
service.

The following AWS CLI example describes the `service-name` service in
the `default` cluster, which will provide the latest service event
messages.

```
aws ecs describe-services \
    --cluster `default` \
    --services `service-name` \
    --region `us-west-2`
```
