# Structure of the `detail`

field

The `detail` field includes all of the Resource Groups service-specific details about
a specific change. The `detail` field can take one of two forms, a group
state change or membership change, based on the value of the `detail-type`
field described in the previous section.

###### Important

Resource groups in these events are identified by a combination of the group's ARN
and a `"unique-id"` field that contains a [UUID](https://wikipedia.org/wiki/Universally_unique_identifier "https://wikipedia.org/wiki/Universally_unique_identifier"). By
including a UUID as part of the identity of a resource group, you can distinguish
between a group that is deleted and a different group that is later created with the
same name. We recommend that you treat a concatenation of the ARN and unique id as
the key for the group in your programs that interact with these events.

## Group state

change

`"detail-type": "ResourceGroups Group State Change"`

This `detail-type` value indicates that the state of the group itself,
including its metadata, has changed. This change occurs when a group is created,
updated, or deleted, as indicated by the `"change"` field within the
`detail`.

The information included in the `details` section when this
`detail-type` is specified include the fields described in the
following table.

| Field name       | Type                                                                                                         | Description                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| ---------------- | ------------------------------------------------------------------------------------------------------------ | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `event-sequence` | Double                                                                                                       | A monotonically increasing number that specifies the sequence of<br>events for a specific group. The number resets when you delete the<br>group and create another group with the same name.                                                                                                                                                                                                                                                  |
| `group`          | [Group](#monitor-groups-syntax-detail-group-object "#monitor-groups-syntax-detail-group-object") JSON object | The group object associated with the event by its ARN, name, and<br>unique ID.                                                                                                                                                                                                                                                                                                                                                                |
| `state-change`   | String                                                                                                       | The type of state change that occurred. Can be any of the<br>following values:<br>• [create](#monitor-groups-syntax-detail-state-change-create "#monitor-groups-syntax-detail-state-change-create")<br>• [update](#monitor-groups-syntax-detail-state-change-update "#monitor-groups-syntax-detail-state-change-update")<br>• [delete](#monitor-groups-syntax-detail-state-change-delete "#monitor-groups-syntax-detail-state-change-delete") |
| `old-state`      | `GroupState` JSON object                                                                                     | The state of the group before the change. The object includes<br>only the values of properties that changed.                                                                                                                                                                                                                                                                                                                                  |
| `new-state`      | `GroupState` JSON object                                                                                     | The state of the group after the change. The object includes only<br>the values of properties that changed.                                                                                                                                                                                                                                                                                                                                   |

The `group`
JSON object contains the elements described in the following table.

| Field name  | Type   | Description                                                                                                                                                                                                                                                                   |
| ----------- | ------ | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `arn`       | String | The ARN of the group.                                                                                                                                                                                                                                                         |
| `name`      | String | The friendly name of the group.                                                                                                                                                                                                                                               |
| `unique-id` | GUID   | A unique GUID value that distinguishes between a group that was<br>deleted and a different group that was later created with the same<br>name and ARN. Use the concatenation of ARN and this value as a<br>unique key for the group when consuming these events in your code. |

The
`GroupState` JSON objects contain the elements described in the
following table.

| Field name            | Type                        | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| --------------------- | --------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| `description`         | String                      | The customer-provided description of the resource group.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| `resource-query`      | `ResourceQuery` JSON object | A JSON representation of the query that defines the group's<br>members. This field is present only for groups based on a query. The<br>syntax of this field is defined by the [ResourceQuery API<br>data type](../../../organizations/latest/APIReference/API_ResourceQuery.md "../../../organizations/latest/APIReference/API_ResourceQuery.md"). Example of this are included in the [Create](#monitor-groups-syntax-detail-state-change-create "#monitor-groups-syntax-detail-state-change-create") and [Update](#monitor-groups-syntax-detail-state-change-update "#monitor-groups-syntax-detail-state-change-update") event examples. |
| `group-configuration` | `Configuration` JSON object | A JSON representation of configuration parameters associated with<br>a service-linked group. For more information, see [Service<br>configurations for resource groups](../APIReference/about-slg.md "../APIReference/about-slg.md") in the<br>_AWS Resource Groups API Reference_.                                                                                                                                                                                                                                                                                                                                                         |

Each of the following code examples illustrates the contents of the
`detail` field for each `state-change` type.

### Create

`"state-change": "create"`

The event indicates that a new group was created. The event carries all the
group metadata properties set during the group's creation. This event is
typically followed by one of more group membership events unless the group is
empty. Properties that have a null value are not displayed in the event body.

The following example event indicates a newly created resource group named
`my-service-group`. In this example, the group uses a tag-based
query that matches only Amazon Elastic Compute Cloud (Amazon EC2) instances that have the tag
`"project"="my-service"`.

```
{
    "version": "0",
    "id": "08f00e24-2e30-ec44-b824-8acddf1ac868",
    "detail-type": "ResourceGroups Group State Change",
    "source": "aws.resource-groups",
    "account": "123456789012",
    "time": "2020-09-29T09:59:01Z",
    "region": "us-east-1",
    "resources": [
        "arn:aws:resource-groups:us-east-1:123456789012:group/my-service-group"
    ],
    "detail": {
        "event-sequence": 1.0,
        "state-change": "create",
        "group": {
            "arn": "arn:aws:resource-groups:us-east-1:123456789012:group/my-service-group",
            "name": "my-service-group",
            "unique-id": "3dd07ab7-3228-4410-8cdc-6c4a10fcceea"
        },
        "new-state": {
            "resource-query": {
                "type": "TAG_FILTERS_1_0",
                "query": "{
                    \"ResourceTypeFilters\": [\"AWS::EC2::Instance\"],
                    \"TagFilters\": [{\"Key\":\"project\", \"Values\":[\"my-service\"}]
                }"
            }
        }
    }
}
```

### Update

`"state-change": "update"`

The event indicates that an existing group was modified in some way. The event
carries only the properties that changed from the previous state. Properties
that have not changed are not displayed in the event body.

The following example event indicates that the tag-based query in the previous
example's resource group was modified to also include Amazon EC2 volume resources in
the group.

```
{
    "version": "0",
    "id": "08f00e24-2e30-ec44-b824-8acddf1ac868",
    "detail-type": "ResourceGroups Group State Change",
    "source": "aws.resource-groups",
    "account": "123456789012",
    "time": "2020-09-29T09:59:01Z",
    "region": "us-east-1",
    "resources": [
        "arn:aws:resource-groups:us-east-1:123456789012:group/my-service-group"
    ],
    "detail": {
        "event-sequence": 3.0,
        "state-change": "update",
        "group": {
            "arn": "arn:aws:resource-groups:us-east-1:123456789012:group/my-service-group",
            "name": "my-service",
            "unique-id": "3dd07ab7-3228-4410-8cdc-6c4a10fcceea"
        },
        "new-state": {
            "resource-query": {
                "type": "TAG_FILTERS_1_0",
                "query": "{
                    \"ResourceTypeFilters\": [\"AWS::EC2::Instance\", \"AWS::EC2::Volume\"],
                    \"TagFilters\": [{\"Key\":\"project\", \"Values\":[\"my-service\"}]
                }"
            }
        },
        "old-state": {
            "resource-query": {
                "type": "TAG_FILTERS_1_0",
                "query": "{
                    \"ResourceTypeFilters\": [\"AWS::EC2::Instance\"],
                    \"TagFilters\": [{\"Key\":\"Project\", \"Values\":[\"my-service\"}]
                }"
            }
        }
    }
}

```

### Delete

`"state-change": "delete"`

The event indicates that an existing group was deleted. The detail field
includes no metadata about the group other than its identification. The
`event-sequence` field is reset after this event as it is, by
definition, the last event for this `arn` and
`unique-id`.

```
{
    "version": "0",
    "id": "08f00e24-2e30-ec44-b824-8acddf1ac868",
    "detail-type": "ResourceGroups Group State Change",
    "source": "aws.resource-groups",
    "account": "123456789012",
    "time": "2020-09-29T09:59:01Z",
    "region": "us-east-1",
    "resources": [
        "arn:aws:resource-groups:us-east-1:123456789012:group/my-service"
    ],
    "detail": {
        "event-sequence": 4.0,
        "state-change": "delete",
        "group": {
            "arn": "arn:aws:resource-groups:us-east-1:123456789012:group/my-service",
            "name": "my-service",
            "unique-id": "3dd07ab7-3228-4410-8cdc-6c4a10fcceea"
        }
    }
}
```

## Group membership

change

`"detail-type": "ResourceGroups Group Membership Change"`

This `detail-type` value indicates that the group's membership was
changed by a resource being added to or removed from the group. When this
`detail-type` is specified, the top-level `resources`
field includes the ARN of the group whose membership was changed and the ARNs of any
resources that were added to or removed from the group.

The information included in the `details` section when this
`detail-type` is specified include the fields described in the
following table.

| Field name       | Type                                   | Description                                                                                                                                                                                                                                                                                                                                             |
| ---------------- | -------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `event-sequence` | Double                                 | A monotonically increasing number that indicates the sequence of<br>events for a specific group. The number resets when the group is<br>deleted and its unique ID changes.                                                                                                                                                                              |
| `group`          | `Group` JSON object                    | Identifies the group object associated with the event by its ARN,<br>name, and unique ID.                                                                                                                                                                                                                                                               |
| `resources`      | Array of `ResourceChange` JSON objects | An array of resources whose group membership has<br>changed.<br>This `ResourceChange` object contains the following<br>fields for each resource:<br>• `membership-change` – The value is<br>either `"add"` or<br>`"remove"`.<br>• `arn` – The ARN of the resource<br>added or removed.<br>• `resource-type` – The type of<br>resource added or removed. |

The following code example illustrates the contents of the event for a typical
membership change type. This example shows one resource being added to the group,
and one resource being removed from the group.

```
{
    "version": "0",
    "id": "08f00e24-2e30-ec44-b824-8acddf1ac868",
    "detail-type": "ResourceGroups Group Membership Change",
    "source": "aws.resource-groups",
    "account": "123456789012",
    "time": "2020-09-29T09:59:01Z",
    "region": "us-east-1",
    "resources": [
        "arn:aws:resource-groups:us-east-1:123456789012:group/my-service",
        "arn:aws:ec2:us-east-1:123456789012:instance/i-abcd1111",
        "arn:aws:ec2:us-east-1:123456789012:instance/i-efef2222"
    ],
    "detail": {
        "event-sequence": 2.0,
        "group": {
            "arn": "arn:aws:resource-groups:us-east-1:123456789012:group/my-service",
            "name": "my-service",
            "unique-id": "3dd07ab7-3228-4410-8cdc-6c4a10fcceea"
        },
        "resources": [
            {
                "membership-change": "add",
                "arn": "arn:aws:ec2:us-east-1:123456789012:instance/i-abcd1111",
                "resource-type": "AWS::EC2::Instance"
            },
            {
                "membership-change": "remove",
                "arn": "arn:aws:ec2:us-east-1:123456789012:instance/i-efef2222",
                "resource-type": "AWS::EC2::Instance"
            }
        ]
    }
}
```
