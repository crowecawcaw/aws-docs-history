

# Deleting a resource with AWS Cloud Control API
<a name="resource-operations-delete"></a>

Use the `delete-resource` command to delete an existing resource. You can delete the resource whether or not the resource was originally provisioned using Cloud Control API.

**Important**  
We strongly advise against using Cloud Control API to delete resources that are under active management by other services. Doing so can lead to unexpected results. For example, don't use Cloud Control API to delete resources that are currently part of an CloudFormation stack.

To update an existing resource, you must specify the resource's identifier. For more information about finding a resource's identifier, see [Using a resource's primary identifier](resource-identifier.md#resource-identifier-using).

The follow example deletes an [`AWS::Logs::LogGroup`](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-logs-loggroup.html) resource with the name of `CloudControlApiLogGroup`.

```
$ aws cloudcontrol delete-resource \
    --type-name AWS::Logs::LogGroup --identifier CloudControlApiLogGroup
```

## Tracking the progress of a delete resource request
<a name="resource-operations-delete-progress"></a>

The `delete-resource` command returns a `ProgressEvent` object that you can use to track the current status of your resource operation request. For more information, see [Tracking the progress of resource operation requests](resource-operations-manage-requests.md#resource-operations-manage-requests-track).