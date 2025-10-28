# Reading a resource with AWS Cloud Control API

Using a resource's primary identifier, you can call the `get-resource` command to retrieve
detailed information about the resource. For information about retrieving a resource's primary identifier, see [Identifying resources with AWS Cloud Control API](resource-identifier.md "resource-identifier.md").

The information returned by `get-resource` includes the resource's schema, which details the
current state of the resource, including property values, supported events, and necessary permissions. For more
information, see [Viewing resource type schemas](resource-types.md#resource-types-schemas "resource-types.md#resource-types-schemas").

The following example returns the current state of an `AWS::Logs::LogGroup`
resource named `LogGroupResourceExample`. For
`AWS::Logs::LogGroup` resources, the name of a log group is its primary
identifier.

```
`$` `aws cloudcontrol get-resource --type-name AWS::Logs::LogGroup --identifier LogGroupResourceExample`
```
