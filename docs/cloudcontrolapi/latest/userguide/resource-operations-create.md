# Creating a resource with AWS Cloud Control API

Use the `create-resource` command to create a resource.

## Composing the desired state of the

resource

For Cloud Control API to create a resource, you must specify the _desired state_ of the resource
you want to create. The desired state consists of a listing of the resource properties that you want to specify, and
their desired values.

The properties of a resource are defined in its resource type schema. This includes whether the property
is required, valid values, and other property constraints. For more information about viewing resource property
definitions, see [Viewing resource type schemas](resource-types.md#resource-types-schemas "resource-types.md#resource-types-schemas").

The desired state that you specify must be valid against the resource type schema.

As an example, suppose you wanted to create an [`AWS::Logs::LogGroup`](../../../AWSCloudFormation/latest/UserGuide/aws-resource-logs-loggroup.md "../../../AWSCloudFormation/latest/UserGuide/aws-resource-logs-loggroup.md")
resource with a specific name and a retention policy of 90 days. As a first step, you must compose the desired state
of the resource, formatted as JSON text.

```
{
  "LogGroupName": "CloudApiLogGroup",
  "RetentionInDays": 90
}
```

When you call the `create-resource` command, you can pass the desired state directly inline as
a string, or, for more complicated desired state definitions, specify a file location.

The following AWS Command Line Interface (AWS CLI) command creates the resource and specifies in the
`desired-state` parameter that the `RetentionInDays` property of the resource is set to
`90`, in addition to specifying the log group name.

```
`$` `aws cloudcontrol create-resource --type-name AWS::Logs::LogGroup \
 --desired-state '{"LogGroupName": "CloudApiLogGroup", "RetentionInDays":90}'`
```

## Tracking the progress of a create resource

request

The `create-resource` command returns a `ProgressEvent` object that you can use
to monitor the current status of your resource create request. For more information, see [Tracking the progress of resource operation
requests](resource-operations-manage-requests.md#resource-operations-manage-requests-track "resource-operations-manage-requests.md#resource-operations-manage-requests-track").
