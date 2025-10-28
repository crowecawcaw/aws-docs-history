# Updating a resource with AWS Cloud Control API

Use the `update-resource` command to make updates to an existing resource. This includes
resources that weren't originally provisioned using Cloud Control API.

###### Important

We strongly advise against using Cloud Control API to update resources that are under active management by other
services. Doing so can lead to unexpected results. For example, don't use Cloud Control API to update resources that are
currently part of an AWS CloudFormation stack.

To update an existing resource, you must specify the resource's identifier. For more information about
determining a resource's identifier, see [Using a resource's primary
identifier](resource-identifier.md#resource-identifier-using "resource-identifier.md#resource-identifier-using").

Updating a resource entails changing resource property values. The properties of a resource are defined in
its resource type schema. This includes whether the property is required, valid values, and other property
constraints. For more information about viewing resource property definitions, see [Viewing resource type schemas](resource-types.md#resource-types-schemas "resource-types.md#resource-types-schemas").

## Composing the patch document

To update a resource, you first define the updates as a list of _patch operations_
contained in a JSON patch document. This patch document must adhere to the standard defined in [_RFC 6902 - JavaScript Object Notation (JSON)
Patch_](https://datatracker.ietf.org/doc/html/rfc6902 "https://datatracker.ietf.org/doc/html/rfc6902").

Each patch operation defines a single update to a specific resource property. The
following properties are required:

- `op`: The operation type. Cloud Control API supports all operations defined in RFC 6902:
  `add`, `remove`, `replace`, `move`, `copy`, and
  `test`.
- `path`: The path to the resource property, relative to the
  `properties` section of the resource schema.

Depending on the operation, additional properties may be required. Refer to RFC 6902 for
specifics.

When using the `update-resource` command, you can specify the patch
document inline as a string, or specify a file location.

The following example updates the retention policy of an [`AWS::Logs::LogGroup`](../../../AWSCloudFormation/latest/UserGuide/aws-resource-logs-loggroup.md "../../../AWSCloudFormation/latest/UserGuide/aws-resource-logs-loggroup.md")
resource named `CloudControlApiLogGroup` to 90 days.

```
`$` `aws cloudcontrol update-resource --type-name AWS::Logs::LogGroup \
 --identifier CloudControlApiLogGroup \
 --patch-document '[{"op":"replace","path":"RetentionInDays","value":90}]'`
```

## How Cloud Control API updates resources

To update a resource, Cloud Control API first retrieves the current state of the resource and then updates the resource
in a two-step process:

- Cloud Control API combines the patch operations specified in the update request with the current state of the resource,
  to generate the desired state of the resource after it's updated. Operations are applied sequentially in the order
  that they appear in the patch document. Each operation in the sequence is applied to the resource's current state;
  the resulting resource state becomes the target of the next operation.

At this point, the entire update request fails if:

    + A patch operation included in the request is invalid.
    + A patch operation of `op` type `test` fails.

In such cases, the entire update request fails and Cloud Control API makes no updates to the resource.

- Cloud Control API then calls the update handler of the resource type to update the resource.

If the update handler fails at any point, _Cloud Control API does not roll back the resource to its previous
state._

For example, consider the following patch document that is defined to update an [`AWS::Logs::LogGroup`](../../../AWSCloudFormation/latest/UserGuide/aws-resource-logs-loggroup.md "../../../AWSCloudFormation/latest/UserGuide/aws-resource-logs-loggroup.md")
resource. The document contains two patch operations. The first operation is of type `test` and checks to
see if the resource's retention policy is set to 3653 days. If that is the case, the resource passes the test and
Cloud Control API proceeds to the next operation. This operation replaces the current retention policy value with 180 days. If
the resource's retention policy is set to a value of other than 3653 days, the first `test` operation
fails and Cloud Control API never runs the second `replace` operation.

```
[
  {
    "op": "test",
    "path": "/RetentionInDays",
    "value":3653
  },
  {
    "op": "replace",
    "path": "/RetentionInDays",
    "value":180
  }
]
```

## Tracking the progress of an update resource

request

The `update-resource` command returns a `ProgressEvent` object that you can use to
track the current status of your resource operation request. For more information, see [Tracking the progress of resource operation
requests](resource-operations-manage-requests.md#resource-operations-manage-requests-track "resource-operations-manage-requests.md#resource-operations-manage-requests-track").
