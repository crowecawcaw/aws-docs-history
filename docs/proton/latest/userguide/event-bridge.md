End of support notice: On October 7, 2026, AWS will end support for AWS Proton. After October
7, 2026, you will no longer be able to access the AWS Proton console or AWS Proton resources. Your deployed infrastructure
will remain intact. For more information, see [AWS Proton Service Deprecation and Migration
Guide](proton-end-of-support.md "proton-end-of-support.md").

# Automate AWS Proton with EventBridge

You can monitor AWS Proton events in Amazon EventBridge. EventBridge delivers a stream of real-time data from your own applications, software-as-a-service (SaaS)
applications, and AWS services. You can configure events to respond to AWS resource state changes. EventBridge routes this data then to
_target_ services such as AWS Lambda and Amazon Simple Notification Service. These events are the same as those that appear in Amazon CloudWatch Events. CloudWatch Events delivers a near
real-time stream of system events that describe changes in AWS resources. For more information, see [What Is Amazon EventBridge?](../../../eventbridge/latest/userguide.md "../../../eventbridge/latest/userguide.md") in the _Amazon EventBridge User Guide_.

Use EventBridge to be notified of state changes in the AWS Proton provisioning workflows.

## Event types

Events are composed of rules that include an event pattern and targets. You configure a rule by choosing event pattern and target objects:

Event pattern

Each rule is expressed as an event pattern with the source and type of events to monitor and the event targets. To monitor events, you create
a rule with the service that you're monitoring as the event source. For example, you can create a rule with an event pattern that uses AWS Proton
as an event source to trigger a rule when there are changes in a deployment state.

Targets

The rule receives a selected service as the event target. You can set up a target service to send notifications, capture state information,
take corrective action, initiate events, or take other actions.

Event objects contain standard fields of ID, account, AWS Region, detail-type, source, version, resource, time (optional). The detail field is a
nested object containing custom fields for the event.

AWS Proton events are emitted on a best effort basis. Best effort delivery means that the service attempts to send all events to EventBridge, but in some
rare cases an event might not be delivered.

For each AWS Proton resource that can emit events, the following table lists the detail-type value, detail fields, and (where available) a reference
to a list of values for the `status` and `previousStatus` detail fields. When a resource is deleted, the `status`
detail field value is `DELETED`.

| Resource                       | Detail-type value                                       | Detail fields                                                                                                                                                                                                                                                                                       |
| ------------------------------ | ------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `EnvironmentTemplate`          | AWS Proton Environment Template Status Change           | `name`<br>`status`<br>`previousStatus`                                                                                                                                                                                                                                                              |
| `EnvironmentTemplateVersion`   | AWS Proton Environment Template Version Status Change   | `name`<br>`majorVersion`<br>`minorVersion`<br>`status`<br>`previousStatus`<br>[status<br>values](../APIReference/API_EnvironmentTemplateVersion.md#proton-Type-EnvironmentTemplateVersion-status "../APIReference/API_EnvironmentTemplateVersion.md#proton-Type-EnvironmentTemplateVersion-status") |
| `ServiceTemplate`              | AWS Proton Service Template Status Change               | `name`<br>`status`<br>`previousStatus`                                                                                                                                                                                                                                                              |
| `ServiceTemplateVersion`       | AWS Proton Service Template Version Status Change       | `name`<br>`majorVersion`<br>`minorVersion`<br>`status`<br>`previousStatus`<br>[status values](../APIReference/API_ServiceTemplateVersion.md#proton-Type-ServiceTemplateVersion-status "../APIReference/API_ServiceTemplateVersion.md#proton-Type-ServiceTemplateVersion-status")                    |
| `Environment`                  | AWS Proton Environment Status Change                    | `name`<br>`status`<br>`previousStatus`                                                                                                                                                                                                                                                              |
| `Service`                      | AWS Proton Service Status Change                        | `name`<br>`status`<br>`previousStatus`<br>[status values](../APIReference/API_Service.md#proton-Type-Service-status "../APIReference/API_Service.md#proton-Type-Service-status")                                                                                                                    |
| `ServiceInstance`              | AWS Proton Service Instance Status Change               | `name`<br>`serviceName`<br>`status`<br>`previousStatus`                                                                                                                                                                                                                                             |
| `ServicePipeline`              | AWS Proton Service Pipeline Status Change               | `serviceName`<br>`status`<br>`previousStatus`                                                                                                                                                                                                                                                       |
| `EnvironmentAccountConnection` | AWS Proton Environment Account Connection Status Change | `id`<br>`status`<br>`previousStatus`<br>[status<br>values](../APIReference/API_EnvironmentAccountConnection.md#proton-Type-EnvironmentAccountConnection-status "../APIReference/API_EnvironmentAccountConnection.md#proton-Type-EnvironmentAccountConnection-status")                               |
| `Component`                    | AWS Proton Component Status Change                      | `name`<br>`status`<br>`previousStatus`                                                                                                                                                                                                                                                              |

## AWS Proton event examples

The following examples show the ways that AWS Proton can send events to EventBridge.

Service template

```
{
    "source": "aws.proton",
    "detail-type": ["AWS Proton Service Template Status Change"],
    "time": "2021-03-22T23:21:40.734Z",
    "resources": ["arn:aws:proton:region_id:123456789012:service-template/sample-service-template-name"],
    "detail": {
        "name": "sample-service-template-name",
        "status": "PUBLISHED",
        "previousStatus": "DRAFT"
    }
}
```

Service template version

```
{
    "source": "aws.proton",
    "detail-type": ["AWS Proton Service Template Version Status Change"],
    "time": "2021-03-22T23:21:40.734Z",
    "resources": ["arn:aws:proton:region_id:123456789012:service-template/sample-service-template-name:1.0"],
    "detail": {
        "name": "sample-service-template-name",
        "majorVersion": "1",
        "minorVersion": "0",
        "status": "REGISTRATION_FAILED",
        "previousStatus": "REGISTRATION_IN_PROGRESS"
    }
}
```

Environment

```
{
    "source": "aws.proton",
    "detail-type": ["AWS Proton Environment Status Change"],
    "time": "2021-03-22T23:21:40.734Z",
    "resources": ["arn:aws:proton:region_id:123456789012:environment/sample-environment"],
    "detail": {
        "name": "sample-environment",
        "status": "DELETE_FAILED",
        "previousStatus": "DELETE_IN_PROGRESS"
    }
}
```
