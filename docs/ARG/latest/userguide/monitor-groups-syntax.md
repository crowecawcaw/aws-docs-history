

# Structure and syntax of Resource Groups lifecycle events
<a name="monitor-groups-syntax"></a>

**Note**  
AWS Group Lifecycle Events (GLE) feature of AWS Resource Groups is no longer open to new customers. For capabilities similar to Group Lifecycle Events (GLE), see the recommended EventBridge-based alternative. For more information, see [Group Lifecycle Events feature of AWS Resource Groups availability change](resource-groups-gle-availability-change.md).

**Topics**
+ [Structure of the `detail` field](monitor-groups-syntax-detail.md)
+ [Example EventBridge custom event patterns for different use cases](monitor-groups-example-eventbridge-filters.md)

The lifecycle events for AWS Resource Groups take the form of [JSON](https://json.org) object strings in the following general format.

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

For details about the fields common to all Amazon EventBridge events, see [Amazon EventBridge events](https://docs.aws.amazon.com/eventbridge/latest/userguide/aws-events.html) in the *Amazon EventBridge User Guide*. Details that are specific to Resource Groups are explained in the following table.


| Field name | Type | Description | 
| --- | --- | --- | 
| detail-type | String | For Resource Groups, the `detail-type` field is always one of the following values:+  `ResourceGroups Group State Change` – Represents changes to the overall group state and its properties. <br />+  `ResourceGroups Group Membership Change` – Represents changes to the group membership.   | 
| source | String | For Resource Groups, this value is always "aws.resource-groups". | 
| resources | An array of Amazon Resource Names (ARNs) | This field always includes the [Amazon resource name (ARN)](https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html) of the group with the change that triggered this event.<br />This field can also include the ARNs of any resources added to or removed from the group, if applicable. | 
| `detail` | JSON object string | This is the payload of the event. The contents of the detail field vary based on the value of the detail-type. [See the next section for more information.](monitor-groups-syntax-detail.md) | 