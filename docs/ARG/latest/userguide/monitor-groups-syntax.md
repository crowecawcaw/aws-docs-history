# Structure and syntax of Resource Groups lifecycle

events

###### Topics

- [Structure of the detail
  field](monitor-groups-syntax-detail.md "monitor-groups-syntax-detail.md")
- [Example EventBridge custom event
  patterns for different use cases](monitor-groups-example-eventbridge-filters.md "monitor-groups-example-eventbridge-filters.md")
  The lifecycle events for AWS Resource Groups take the form of [JSON](https://json.org "https://json.org") object strings in the following general format.

```
{
    "version": "0",
    "id": "08f00e24-2e30-ec44-b824-8acddf1ac868",
    "detail-type": "ResourceGroups Group ... Change",
    "source": "aws.resource-groups",
    "account": "123456789012",
    "time": "2020-09-29T09:59:01Z",
    "region": "us-east-1",
    "resources": [
        "arn:aws:resource-groups:us-east-1:123456789012:group/MyGroupName"
    ],
    "detail": {
        ...
    }
}
```

For details about the fields common to all Amazon EventBridge events, see [Amazon EventBridge events](../../../eventbridge/latest/userguide/aws-events.md "../../../eventbridge/latest/userguide/aws-events.md") in the
_Amazon EventBridge User Guide_. Details that are specific to Resource Groups
are explained in the following table.

| Field name    | Type                                     | Description                                                                                                                                                                                                                                                                                                                                          |
| ------------- | ---------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `detail-type` | String                                   | For Resource Groups, the `detail-type` field is always one of the<br>following values:<br>• `ResourceGroups Group State Change`<br>– Represents changes to the overall group state and its<br>properties.<br>• `ResourceGroups Group Membership Change`<br>– Represents changes to the group membership.                                             |
| `source`      | String                                   | For Resource Groups, this value is **always**<br>`"aws.resource-groups"`.                                                                                                                                                                                                                                                                            |
| `resources`   | An array of Amazon Resource Names (ARNs) | This field always includes the [Amazon resource name (ARN)](../../../general/latest/gr/aws-arns-and-namespaces.md "../../../general/latest/gr/aws-arns-and-namespaces.md") of the group with the<br>change that triggered this event.<br>This field can also include the ARNs of any resources added to or<br>removed from the group, if applicable. |
| `detail`      | JSON object string                       | This is the payload of the event. The contents of the `detail`<br>field vary based on the value of the `detail-type`. [See the next section for more<br>information.](monitor-groups-syntax-detail.md "monitor-groups-syntax-detail.md")                                                                                                             |
