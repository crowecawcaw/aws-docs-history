# Dynamic thing groups

Dynamic thing groups are created from specific search queries in the registry. Search
query parameters such as device connectivity, device shadow creation, and AWS IoT Device Defender
violations data support this. Dynamic thing groups require fleet indexing enabled to
index, search, and aggregate your devices' data. You can preview the things in a dynamic
thing group using a fleet indexing search query before creating it. For more
information, see [Fleet indexing](iot-indexing.md "iot-indexing.md") and [Query syntax](query-syntax.md "query-syntax.md").

###### Note

Dynamic thing group operations are metered under registry operations. For more
information, see [AWS IoT Core
additional metering details](https://aws.amazon.com/iot-core/pricing/additional-details/ "https://aws.amazon.com/iot-core/pricing/additional-details/").

Dynamic thing groups differ from static thing groups in the following ways:

- Thing membership is not explicitly defined. To create a dynamic thing group,
  define [a search query string](example-queries.md "example-queries.md") to determine
  group membership.
- Dynamic thing groups can't be part of a hierarchy.
- Dynamic thing groups can't have policies applied to them.
- You use a different set of commands to create, update, and delete dynamic
  thing groups. For all other operations, you use the same commands for both types
  of thing groups.
- The number of dynamic groups per AWS account is [limited](../../../general/latest/gr/iot_device_management.md#thing-group-limits "../../../general/latest/gr/iot_device_management.md#thing-group-limits").

- Don't use personally identifiable information in your thing group name. The
  thing group name can appear in unencrypted communications and reports.
  For more information about static thing groups, see [Static thing groups](thing-groups.md "thing-groups.md").

## Use cases of dynamic thing groups

You can use dynamic thing groups for the following use cases:

### Specify a dynamic thing group as a target for a job

Creating a continuous job with a dynamic thing group as target allows you
to automatically target devices when they meet the desired criteria. The
criteria can be the connectivity state or any criteria stored in registry or
shadow such as software version or model. If a thing doesn’t appear in the
dynamic thing group, it won’t receive the job document from the job.

For example, if your device fleet requires a firmware update to minimize
the risk of interruption during the update process, and you only want to
update the firmware on devices with a battery life greater than 80%. You can
create a dynamic thing group called 80PercentBatteryLife that only includes
devices with a battery life above 80% and use it as the target for your job.
Only devices that meet your battery life criteria will receive the firmware
update. As devices reach the 80% battery life criteria, they are
automatically added to the dynamic thing group and will receive the firmware
update.

You may also have multiple device models with different firmware or
operating system, necessitating different versions of new software updates.
This is the most common use case for dynamic groups with continuous jobs,
where you can create a dynamic group for each device model, firmware and OS
combination. You can then set up continuous jobs to each of these dynamic
groups to push software updates as devices automatically become members of
these groups based on the defined criteria.

For more information about specifying thing groups as job targets, see [CreateJob](../apireference/API_CreateJob.md "../apireference/API_CreateJob.md").

### Use dynamic group membership changes to perform

desired actions

Each time a device is added to or removed from a dynamic thing group, a
notification is sent to an MQTT topic as part of [registry
event](registry-events.md "registry-events.md") updates. You can configure [AWS IoT Core rules](iot-rules.md "iot-rules.md")
to interact with AWS services based on the dynamic group membership
updates and take desired actions. Example actions include writing to
Amazon DynamoDB, invoking a Lambda function, or sending a
notification to Amazon SNS.

### Add devices to a dynamic

thing group for automatic violation detection

AWS IoT Device Defender Detect customers can define a [security
profile](device-defender-detect.md "device-defender-detect.md") on a dynamic thing group. Devices of the dynamic thing
group are automatically detected for violations by the security profile
defined on the group.

### Set log levels on

dynamic thing groups to observe devices with fine-grained logging

You can specify a log level on a dynamic thing group. This is useful if
you only want to customize logging level and detail for devices that meet
certain criteria. For example, if you suspect devices with certain firmware
version are causing errors on a specific rule's published topic, you might
want to set detailed logging to debug these issues. In this case, you can
create a dynamic group for all devices that have this firmware version,
which we assume is stored as a registry attribute or in a device shadow. You
can then set a debug level, with logging target defined as this dynamic
thing group. For more information about fine-grained logging, see [Monitor AWS IoT using CloudWatch Logs](cloud-watch-logs.md#fine-grained-logging "cloud-watch-logs.md#fine-grained-logging"). For more information about how
to specify a logging level for a specific thing group, see [Configure resource-specific logging in AWS IoT](configure-logging.md#fine-logging-cli "configure-logging.md#fine-logging-cli").

## Create a dynamic thing group

Use the **CreateDynamicThingGroup** command to create a dynamic
thing group. To create a dynamic thing group for the 80PercentBatteryLife scenario,
use the **create-dynamic-thing-group** CLI command:

```
$ aws iot create-dynamic-thing-group --thing-group-name "80PercentBatteryLife" --query-string "attributes.batterylife80"
```

###### Note

Don't use personally identifiable information in your dynamic thing group
names.

The **CreateDynamicThingGroup** command returns a response. The
response contains the index name, query string, query version, thing group name,
thing group ID, and the Amazon Resource Name (ARN) of your thing group:

```
{
    "indexName": "AWS_Things",
    "queryVersion": "2017-09-30",
    "thingGroupName": "80PercentBatteryLife",
    "thingGroupArn": "arn:aws:iot:us-west-2:123456789012:thinggroup/80PercentBatteryLife",
    "queryString": "attributes.batterylife80\n",
    "thingGroupId": "abcdefgh12345678ijklmnop12345678qrstuvwx"
}
```

The creation of dynamic thing groups doesn't happen at once. The dynamic thing
group backfill takes time to complete. When you create a dynamic thing group, the
status of the group is set to `BUILDING`. When the backfill is complete,
the status changes to `ACTIVE`. To check the status of your dynamic thing
group, use the [DescribeThingGroup](../apireference/API_DescribeThingGroup.md "../apireference/API_DescribeThingGroup.md") command.

## Describe a dynamic thing

group

Use the **DescribeThingGroup** command to get information about a
dynamic thing group:

```
$ aws iot describe-thing-group --thing-group-name "80PercentBatteryLife"
```

The **DescribeThingGroup** command returns information about the
specified group:

```
{
    "status": "ACTIVE",
    "indexName": "AWS_Things",
    "thingGroupName": "80PercentBatteryLife",
    "thingGroupArn": "arn:aws:iot:us-west-2:123456789012:thinggroup/80PercentBatteryLife",
    "queryString": "attributes.batterylife80\n",
    "version": 1,
    "thingGroupMetadata": {
        "creationDate": 1548716921.289
    },
    "thingGroupProperties": {},
    "queryVersion": "2017-09-30",
    "thingGroupId": "84dd9b5b-2b98-4c65-84e4-be0e1ecf4fd8"
}


```

Running **DescribeThingGroup** on a dynamic thing group returns
attributes that are specific to the dynamic thing groups. Example return attributes
are the queryString and the status.

The status of a dynamic thing group can take the following values:

`ACTIVE`

The dynamic thing group is ready for use.

`BUILDING`

The dynamic thing group is being created, and thing membership is
being processed.

`REBUILDING`

The dynamic thing group's membership is being updated, following the
adjustment of the group's search query.

###### Note

After you create a dynamic thing group, use it regardless of its status. Only
dynamic thing groups with an `ACTIVE` status include all of the
things that match the search query for that dynamic thing group. Dynamic thing
groups with `BUILDING` and `REBUILDING` statuses might not
include all of the things that match the search query.

## Update a dynamic thing group

Use the **UpdateDynamicThingGroup** command to update the
attributes of a dynamic thing group, including the group's search query. The
following command updates two attributes. One is the thing group description, and
the other is the query string that changes the membership criteria to battery life

> 85:

```
$ aws iot update-dynamic-thing-group --thing-group-name "80PercentBatteryLife" --thing-group-properties "thingGroupDescription=\"This thing group contains devices with a battery life greater than 85 percent.\"" --query-string "attributes.batterylife85"
```

The **UpdateDynamicThingGroup** command returns a response that
contains the group's version number after the update:

```
{
    "version": 2
}
```

The update of a dynamic thing group doesn't happen at once. The dynamic thing
group backfill takes time to complete. When you update a dynamic thing group, the
status of the group changes to `REBUILDING` while the group updates its
membership. When the backfill is complete, the status changes to
`ACTIVE`. To check the status of your dynamic thing group, use the [DescribeThingGroup](../apireference/API_DescribeThingGroup.md "../apireference/API_DescribeThingGroup.md")
command.

## Delete a dynamic thing group

Use the **DeleteDynamicThingGroup** command to delete a dynamic
thing group:

```
$ aws iot delete-dynamic-thing-group --thing-group-name "80PercentBatteryLife"
```

The **DeleteDynamicThingGroup** command doesn't produce any
output.

Commands that show which groups a thing belongs to (for example,
**ListGroupsForThing**) might continue to show the group while
records in the cloud are being updated.

## Dynamic and Static Thing

Group Limitations

Dynamic thing groups and static thing groups share the following
limitations:

- The number of attributes that a thing group can have is [limited](../../../general/latest/gr/iot_device_management.md#thing-group-limits "../../../general/latest/gr/iot_device_management.md#thing-group-limits").
- The number of groups to which a thing can belong is [limited](../../../general/latest/gr/iot_device_management.md#thing-group-limits "../../../general/latest/gr/iot_device_management.md#thing-group-limits").
- You can't rename thing groups.
- Thing group names can't contain international characters, such as û, é,
  and ñ.

## Dynamic Thing Group

Limitations

Dynamic thing groups have the following limitations:

### Fleet indexing

With the fleet indexing service enabled, you can perform search queries on
your fleet of devices. You can create and manage dynamic thing groups after the
fleet indexing backfill is completed. The completion time for the backfill
process is directly affeted by the size of your device fleet registered with the
AWS Cloud. After you enable the fleet indexing service for dynamic thing
groups, you cannot disable it until you delete all of your dynamic thing
groups.

###### Note

If you have permissions to query the fleet index, you can access the data
of things across the entire fleet.

### The number of dynamic thing

groups is limited

The number of dynamic thing groups is [limited](../../../general/latest/gr/iot_device_management.md#thing-group-limits "../../../general/latest/gr/iot_device_management.md#thing-group-limits").

### Successful commands can log errors

When you create or update a dynamic thing group, it's possible that some
things are eligible for inclusion in a dynamic thing group, but they are not
added to it. That scenario will cause a succeessful create or update command
while logging an error and generating an [AddThingToDynamicThingGroupsFailed metric](metrics_dimensions.md#iot-metrics "metrics_dimensions.md#iot-metrics"). A single
metric can represent multiple log entries.

An [error log
entry](../apireference/cwl-format.md#dynamic-group-logs "../apireference/cwl-format.md#dynamic-group-logs") in the CloudWatch log is created when the following occurs:

- An eligible thing can't be added to a dynamic thing group.
- A thing is removed from a dynamic thing group to add it to another
  group.

When a thing becomes eligible to be added to a dynamic thing group, consider
the following:

- Is the thing already in as many groups as it can be? (See [limits](../../../general/latest/gr/iot_device_management.md#thing-limits "../../../general/latest/gr/iot_device_management.md#thing-limits"))
  - **NO:** The thing is added to the
    dynamic thing group.
  - **YES:** Is the thing a member of
    any dynamic thing groups?
    - **NO:** The thing can't
      be added to the dynamic thing group, an error is logged,
      and an [AddThingToDynamicThingGroupsFailed
      metric](metrics_dimensions.md#iot-metrics "metrics_dimensions.md#iot-metrics") is generated.
    - **YES:** Is the dynamic
      thing group to join older than any dynamic thing group
      that the thing is already a member of?
      - **NO:** The thing
        can't be added to the dynamic thing group, an
        error is logged, and an [AddThingToDynamicThingGroupsFailed
        metric](metrics_dimensions.md#iot-metrics "metrics_dimensions.md#iot-metrics") is generated.
      - **YES:** Remove
        the thing from the most recent dynamic thing
        group, log an error, and add the thing to the
        dynamic thing group. This generates an error and
        an [AddThingToDynamicThingGroupsFailed
        metric](metrics_dimensions.md#iot-metrics "metrics_dimensions.md#iot-metrics") for the dynamic thing group from
        which the thing was removed.

When a thing in a dynamic thing group no longer meets the search query, the
thing is removed from the dynamic thing group. Likewise, when a thing is updated
to meet a dynamic thing group's search query, the thing is then added to the
group as previously described. These additions and removals are normal and don't
produce error log entries.

### With `overrideDynamicGroups`

enabled, static groups take priority over dynamic groups

The number of groups to which a thing can belong is [limited](../../../general/latest/gr/iot_device_management.md#thing-limits "../../../general/latest/gr/iot_device_management.md#thing-limits"). When you use the [AddThingToThingGroup](../apireference/API_AddThingToThingGroup.md "../apireference/API_AddThingToThingGroup.md") or [UpdateThingGroupsForThing](../apireference/API_UpdateThingGroupsForThing.md "../apireference/API_UpdateThingGroupsForThing.md") commands to update thing membership,
adding the `--overrideDynamicGroups` parameter gives static thing
groups priority over dynamic thing groups.

When you add a thing to a static thing group, consider the following:

- Does the thing already belong to the maximum number of groups?
  - **NO:** The thing is added to the
    static thing group.
  - **YES:** Is the thing in any
    dynamic groups?
    - **NO:** The thing can't
      be added to the thing group. The command raises an
      exception.
    - **YES:** Was
      **--overrideDynamicGroups**
      enabled?
      - **NO:** The thing
        can't be added to the thing group. The command
        raises an exception.
      - **YES:** The
        thing is removed from the most recently created
        dynamic thing group, an error is logged, and an
        [AddThingToDynamicThingGroupsFailed
        metric](metrics_dimensions.md#iot-metrics "metrics_dimensions.md#iot-metrics") is generated for the dynamic thing
        group from which the thing was removed. Then, the
        thing is added to the static thing group.

### Older dynamic thing groups take priority over

newer ones

The number of groups to which a thing can belong is [limited](../../../general/latest/gr/iot_device_management.md#thing-limits "../../../general/latest/gr/iot_device_management.md#thing-limits"). When a create or update operation creates additional group
eligibility for a thing and the thing has reached its group limit, removal from
another dynamic thing group can occur to enable this addition. For more
information about how this occurs, see [Successful commands can log errors](#log-errors "#log-errors") and [With overrideDynamicGroups
enabled, static groups take priority over dynamic groups](#membership-limit "#membership-limit") for examples.

When a thing is removed from a dynamic thing group, an error is logged and an
event is raised.

### You can't apply policies to dynamic thing

groups

Attempting to apply a policy to a dynamic thing group generates an exception.

### Dynamic thing group membership is eventually

consistent

Only the final state of a thing is evaluated for the registry. Intermediary
states can be skipped if states are updated rapidly. Avoid associating a rule or
job with a dynamic thing group whose membership depends on an
intermediary state.
