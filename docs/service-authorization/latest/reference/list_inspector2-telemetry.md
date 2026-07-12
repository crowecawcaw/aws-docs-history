# Actions, resources, and condition keys for Amazon Inspector2 Telemetry Channel

Amazon Inspector2 Telemetry Channel (service prefix: `inspector2-telemetry`) provides the following
service-specific operations, resources, actions, and condition keys for use in IAM permission
policies.

References:

- Learn how to [configure this service](../../../inspector/latest/user/scanning-ec2.md "../../../inspector/latest/user/scanning-ec2.md").
- View a list of the [API operations available for
  this service](../../../inspector/v2/APIReference/Welcome.md "../../../inspector/v2/APIReference/Welcome.md").
- Learn how to secure this service and its resources by
  [using IAM](../../../inspector/latest/user/security-iam.md "../../../inspector/latest/user/security-iam.md") permission policies.
- View the [programmatic service authorization
  reference](https://servicereference.us-east-1.amazonaws.com/v1/inspector2-telemetry/inspector2-telemetry.json "https://servicereference.us-east-1.amazonaws.com/v1/inspector2-telemetry/inspector2-telemetry.json") for this service.

###### Topics

- [Actions defined by Amazon Inspector2 Telemetry Channel](#list_inspector2-telemetry-actions-as-permissions "#list_inspector2-telemetry-actions-as-permissions")
- [Resource types defined by Amazon Inspector2 Telemetry Channel](#list_inspector2-telemetry-resources-for-iam-policies "#list_inspector2-telemetry-resources-for-iam-policies")
- [Condition keys for Amazon Inspector2 Telemetry Channel](#list_inspector2-telemetry-policy-keys "#list_inspector2-telemetry-policy-keys")

## Actions defined by Amazon Inspector2 Telemetry Channel

You can specify the following actions in the `Action` element of an IAM
policy statement. Use policies to grant permissions to perform an operation in AWS. When
you use an action in a policy, you usually allow or deny access to the API operation or CLI
command with the same name. However, in some cases, a single action controls access to more
than one operation. Alternatively, some operations require several different actions.

| Actions                                                                                                                                           | Description                                                           | Resource types (\*required) | Condition keys | Access level |
| ------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------- | --------------------------- | -------------- | ------------ |
| [NotifyHeartbeat](../../../inspector/v2/APIReference/API_NotifyHeartbeat.md "../../../inspector/v2/APIReference/API_NotifyHeartbeat.md")          | Grants permission to notify heartbeat for an active telemetry session |                             |                | Write        |
| [SendTelemetry](../../../inspector/v2/APIReference/API_SendTelemetry.md "../../../inspector/v2/APIReference/API_SendTelemetry.md")                | Grants permission to send telemetry for an active telemetry session   |                             |                | Write        |
| [SendTelemetryEvent](../../../inspector/v2/APIReference/API_SendTelemetryEvent.md "../../../inspector/v2/APIReference/API_SendTelemetryEvent.md") | Grants permission to send telemetry event for a telemetry session     |                             |                | Write        |
| [StartSession](../../../inspector/v2/APIReference/API_StartSession.md "../../../inspector/v2/APIReference/API_StartSession.md")                   | Grants permission to start a telemetry session                        |                             |                | Write        |
| [StopSession](../../../inspector/v2/APIReference/API_StopSession.md "../../../inspector/v2/APIReference/API_StopSession.md")                      | Grants permission to stop a telemetry session                         |                             |                | Write        |

## Resource types defined by Amazon Inspector2 Telemetry Channel

Amazon Inspector2 Telemetry Channel does not support specifying a resource ARN in the
`Resource` element of an IAM policy statement.

## Condition keys for Amazon Inspector2 Telemetry Channel

Amazon Inspector2 Telemetry Channel has no service-specific condition keys that can be used in the
`Condition` element of policy statements.
