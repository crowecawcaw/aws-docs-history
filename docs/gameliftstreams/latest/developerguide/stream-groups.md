# Manage streaming with an Amazon GameLift Streams stream group

After you set up an Amazon GameLift Streams application, you're ready to manage and deploy compute
resources to run and stream your application. An Amazon GameLift Streams _stream
group_ represents a collection of these compute resources. You specify the
maximum number of concurrent streams to support by scaling the stream capacity.

Amazon GameLift Streams allocates compute resources in the AWS Region where you create a stream group.
You can also add remote locations to a stream group and manage capacity per location. It's a
best practice to host stream sessions in locations that are geographically near your end
users. This helps minimize latency and improve stream quality. For more information, refer
to [AWS Regions and remote locations supported by
Amazon GameLift Streams](regions-quotas-rande.md "regions-quotas-rande.md").

In a stream group, you can specify one or more Amazon GameLift Streams applications that the stream group
can stream. A single application can be in multiple stream groups, so you can set up
different configurations or types of compute resources to stream the same application. For
example, to provide two graphics-quality options for streaming an application, you can set
up two stream groups with different stream class configurations and link them to the same
application.

Conversely, a single stream group can have multiple applications: the _default application_, which you can set when you create the
stream group, and additional _linked applications_. For
more information, refer to [Overview of multi-application stream groups](multi-apps.md "multi-apps.md").

How you relate your stream groups and applications together depends on your use case, but
the relationship can be many-to-many.

Stream groups should be recreated every 3-4 weeks to pick up important service updates and
fixes. For more information, refer to [Stream group lifecycle](#stream-groups-lifecycle "#stream-groups-lifecycle").

## About stream capacity

You manage the number of streams you can deliver concurrently to end-users by setting
the stream group's capacity, or _stream capacity_.
Stream capacity represents the number of concurrent stream sessions a stream group can
support. It is configured at each location. There are two types of capacity: always-on
capacity and on-demand capacity.

- **Always-on capacity:**

The streaming capacity that is pre-allocated and ready to handle stream requests without delay. You pay for this capacity whether it's in use or not.
Best for quickest time from streaming request to streaming session.

- **On-demand capacity:**

The streaming capacity that Amazon GameLift Streams can allocate in response to stream requests, and then de-allocate when the session has terminated.
This offers a cost control measure at the expense of a greater stream start time (typically under 5 minutes).

If you have a stream group with an always-on capacity set to 100 at a location, this
means the stream group has enough resources to stream to 100 end-users concurrently at
that location. You can increase or decrease the stream capacity at any time, at each
location (up to your current quota amount) to meet changes in user demand.

When specifying the stream capacity in stream groups with multi-tenant stream classes
(which can stream more than 1 session per compute resource), the capacity must be a
multiple of the tenancy. For example, the `gen5n_high` stream class has a
multi-tenancy of 2. That means each compute resource that gets allocated in your stream
group can stream to 2 clients. Therefore, the capacity you request must be in multiples
of 2.

Amazon GameLift Streams uses always-on capacity first to fulfill stream requests. When always-on
capacity is fully utilized, it automatically allocates on-demand capacity (if
configured) to handle additional requests. As stream sessions end, on-demand capacity is
automatically deallocated to reduce costs. Note that deallocating unused on-demand
capacity can take a few minutes.

Scaling the capacity reflects in your total cost for the stream group. Ensure that you
set up billing alerts to manage your Amazon GameLift Streams costs. Refer to [Create billing alerts to monitor usage](pricing.md#pricing-billing-alerts "pricing.md#pricing-billing-alerts").

To change stream group capacity, edit your stream group settings and enter new values
for always-on and/or on-demand capacity. When you change always-on capacity, Amazon GameLift Streams
adjusts allocated resources to match the new value by provisioning new resources or
shutting down existing ones. Increasing always-on capacity can take more than a few
minutes if resources aren't immediately available. Decreasing always-on capacity takes a
few minutes to deprovision allocated resources.

## Capacity and service quotas

Usage of Amazon GameLift Streams is subject to service quotas that limit the total number of GPUs
(compute resources) you can configure for streaming in your account. The default quotas
and the utilization of the quotas can be viewed in the Service Quota Console for
GameLift Streams. Understanding how these quotas interact with stream capacity helps you
plan your streaming infrastructure and avoid capacity limitations.

More specifically, the GPU service quotas specify the maximum number of GPUs of a
particular stream class family you can request per location across all stream groups in
your account. For example, if your account has a limit of 5 `gen5n` GPUs in
`us-west-2`, the sum of `gen5n` GPUs needed to provide the
total stream capacity in `us-west-2` for all of your stream groups must be
less than or equal to 5. This includes GPUs for both always-on and on-demand
capacity.

When calculating the total stream capacity provided by these GPUs, it's important to
remember that multi-tenant stream classes support streaming more than one session per
GPU. Therefore if you're using multi-tenant stream classes in your stream groups, such
as `gen5n_high`, you will need to take this into account when determining how
the capacity will count against your quota. Single-tenant stream classes, such as
`gen5n_ultra` and `gen5n_win2022`, dedicate one GPU per stream
session.

### Example: How quotas affect capacity

The following example demonstrates how service quotas interact with stream
capacity across multiple stream groups and locations. In this example, assume your
account has a quota of 10 `gen5n` GPUs per location.

1. **Create a single-tenant stream group:** You
   create a stream group using the `gen5n_ultra` stream class with 5
   total capacity (always-on plus on-demand) in `us-east-2`. Because
   this stream class has 1:1 tenancy (1 stream per GPU), you need 5 GPUs for 5
   total capacity. This leaves you with 5 remaining GPUs in
   `us-east-2`.
2. **Create a multi-tenant stream group:** You
   create another stream group using the `gen5n_high` stream class
   with 6 total capacity in `us-east-2`. Because this stream class
   has 1:2 tenancy (2 streams per GPU), you only need 3 GPUs for 6 total
   capacity. This leaves you with 2 remaining GPUs in
   `us-east-2`.
3. **Add capacity in other locations:** After
   creating these stream groups, you have 2 remaining GPUs in
   `us-east-2`, but you still have 10 GPUs available in other
   locations such as `us-west-2` or `eu-west-1`. You can
   add these locations to either of the stream groups you created earlier or
   create new stream groups that have these locations.

This example shows that quotas are enforced per location and across all of your
stream groups, allowing you to distribute your streaming capacity across multiple
geographic regions while staying within service limits.

###### Note

You can view your Applied account level or default quota, including the
utilization of those quotas, in the Service Quotas console by selecting GameLift Streams
as the AWS service. For more information, see [Amazon GameLift Streams service quotas](quotas.md "quotas.md").

## About locations

The location is where Amazon GameLift Streams allocates compute resources to host your application
and stream to users. For lower latency and better quality, you should choose locations
closer to your users. By default, you can stream from the AWS Region where you created
your stream group, known as the _primary location_. Additionally, a
stream group can extend its coverage to stream from other supported locations, known as
_remote locations_.

For a complete list of supported locations, refer to [AWS Regions and remote
locations](regions-quotas-rande.md "regions-quotas-rande.md").

**Multi-location stream group**

A stream group that's configured to host applications and stream sessions from multiple locations, in addition to the primary location (the AWS Region where you created the stream group).
You manage capacity for each location.

## Create a stream group

Console

###### To create a stream group in the Amazon GameLift Streams console

1. Sign in to the AWS Management Console and open the [Amazon GameLift Streams console](https://console.aws.amazon.com/gameliftstreams/ "https://console.aws.amazon.com/gameliftstreams/"). Choose the AWS Region where you want to create your stream group. This Region must be the same as that of the application that you want to stream with the stream group. For more information, refer to [Choosing a Region](../../../awsconsolehelpdocs/latest/gsg/select-region.md "../../../awsconsolehelpdocs/latest/gsg/select-region.md") in the _AWS Management Console Getting Started Guide_.
2. To open the creation workflow, in the navigation pane, choose **Stream groups**, and then choose **Create stream group**.
3. In **Define stream group**, enter the following:
   1. **Description**

   A human-readable label for your stream group. This value doesn't have to be unique. As a best practice, use a meaningful description, name, or label for the stream group.
   You can edit this field at any time. 2. **Tags**

   Tags are labels that can help you organize your AWS resources. For more information, refer to [Tagging your AWS resources](../../../tag-editor/latest/userguide/tagging.md "../../../tag-editor/latest/userguide/tagging.md").

4. In **Select stream class**, choose a stream class for the stream group.
   1. **Stream class options**

   The
   type of compute resources to run and stream applications with. This choice impacts the quality of the streaming experience and the cost. You can specify only one stream class per stream group.
   Choose the class that best fits your application.

   | Stream class    | Description                                                                                                                                                                                                                                                                                                                                                                                                                              |
   | --------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------- |
   | `gen5n_win2022` | (NVIDIA, ultra) Supports applications with extremely high 3D scene complexity.<br>Runs applications on Microsoft Windows Server 2022 Base and supports DirectX 12 and DirectX 11.<br>Supports Unreal Engine up through version 5.5, 64-bit applications, and anti-cheat technology.<br>Uses NVIDIA A10G Tensor GPU.<br>Resources per application: vCPUs: 8. RAM: 32 GB. VRAM: 24 GB.<br>Tenancy: Supports one concurrent stream session. |
   | `gen5n_high`    | (NVIDIA, high) Supports applications with moderate-to-high 3D scene complexity.<br>Uses NVIDIA A10G Tensor GPU.<br>Resources per application: vCPUs: 4. RAM: 16 GB. VRAM: 12 GB.<br>Tenancy: Supports up to two concurrent stream sessions.                                                                                                                                                                                              |
   | `gen5n_ultra`   | (NVIDIA, ultra) Supports applications with extremely high 3D scene complexity.<br>Uses NVIDIA A10G Tensor GPU.<br>Resources per application: vCPUs: 8. RAM: 32 GB. VRAM: 24 GB.<br>Tenancy: Supports one concurrent stream session.                                                                                                                                                                                                      |
   | `gen4n_win2022` | (NVIDIA, ultra) Supports applications with high 3D scene complexity.<br>Runs applications on Microsoft Windows Server 2022 Base and supports DirectX 12 and DirectX 11.<br>Supports Unreal Engine up through version 5.5, 64-bit applications, and anti-cheat technology.<br>Uses NVIDIA T4 Tensor GPU.<br>Resources per application: vCPUs: 8. RAM: 32 GB. VRAM: 16 GB.<br>Tenancy: Supports one concurrent stream session.             |
   | `gen4n_high`    | (NVIDIA, high) Supports applications with moderate-to-high 3D scene complexity.<br>Uses NVIDIA T4 Tensor GPU.<br>Resources per application: vCPUs: 4. RAM: 16 GB. VRAM: 8 GB.<br>Tenancy: Supports up to two concurrent stream sessions.                                                                                                                                                                                                 |
   | `gen4n_ultra`   | (NVIDIA, ultra) Supports applications with high 3D scene complexity.<br>Uses NVIDIA T4 Tensor GPU.<br>Resources per application: vCPUs: 8. RAM: 32 GB. VRAM: 16 GB.<br>Tenancy: Supports one concurrent stream session.                                                                                                                                                                                                                  | To continue, choose **Next**. |

5. In **Link application**, choose an application that you want to stream, or select "**No application**" to choose one at a later time.
   You can edit the stream group after it has been created to add or remove applications.
   You can only link an application that's in `Ready` status and has a runtime that's compatible with the stream class you've chosen.
   By default, these are the only applications that are shown in the table. To see all applications in `Ready` status, choose `All runtimes` in the drop down list.

###### Note

If you don't see your application listed, then check the current AWS Region
setting. You can only link an application to a stream group that's in the same Region.

To continue, choose **Next**. 6. In **Configure stream settings**, under **Locations and capacity**, choose one or more locations where your stream group will have capacity to stream your application.
By default, the region where you create the stream group, known as the _primary location_, has already been added to your stream group and cannot be removed.
You can add additional locations by checking the box next to each location that you want to add. For lower latency and better quality streaming, you should choose locations closer to your users.

For each location, you can specify its _streaming capacity_. Stream capacity represents the number of concurrent streams that can be active at a time.
You set stream capacity per location in each stream group. At each location, there are two types of capacity: always-on capacity and on-demand capacity.

    * **Always-on capacity:**
     The streaming capacity that is pre-allocated and ready to handle stream requests without delay. You pay for this capacity whether it's in use or not.
     Best for quickest time from streaming request to streaming session.
    * **On-demand capacity:**
     The streaming capacity that Amazon GameLift Streams can allocate in response to stream requests, and then de-allocate when the session has terminated.
     This offers a cost control measure at the expense of a greater stream start time (typically under 5 minutes).

You can increase or decrease your total stream capacity at any time to meet changes in user demand for a location by adjusting
either capacity. Amazon GameLift Streams fulfills streaming requests using the idle, pre-allocated resources in the always-on capacity pool if any are
available. If all always-on capacity is in use, Amazon GameLift Streams will provision additional compute resources up to the maximum number specified
in on-demand capacity. As allocated capacity scales, the change is reflected in your total cost for the stream group.

Linked applications will be automatically replicated to each enabled location. An application must finish replicating in a remote location before the remote location can host a stream.
To check on the replication status, open the stream group after it has been created and refer to the **Replication status** column in the table of linked applications.
Click on the current status to see the replication status for each added location.

###### Note

Application data will be stored in all enabled locations including the primary location for this stream group.
Stream session data will be stored in both the primary location and the location where the streaming occurred. 7. In **Review and create stream group**, verify your stream group configuration and make changes as needed. When everything is correct, choose **Create stream group**.

CLI
**Prerequisite**

You must configure the AWS CLI with your user credentials and your chosen AWS Region. For setup instructions, refer to [Download the AWS CLI](setting-up.md#setting-up-prereqs "setting-up.md#setting-up-prereqs").

**To create a stream group using the
AWS CLI**

In your AWS CLI use the [CreateStreamGroup](../apireference/API_CreateStreamGroup.md "../apireference/API_CreateStreamGroup.md") command, customized for your content.

```
aws gameliftstreams create-stream-group \
    --description "`Test_gen4_high`" \
    --default-application-identifier `arn:aws:gameliftstreams:us-west-2:111122223333:application/a-9ZY8X7Wv6` \
    --stream-class `gen4n_high` \
    --location-configurations '[{"LocationName": "`us-east-1`", "AlwaysOnCapacity": `2`, "OnDemandCapacity": `4`}]'
```

where

`description`:

A human-readable label for your stream group. This value doesn't have to be unique. As a best practice, use a meaningful description, name, or label for the stream group.
You can edit this field at any time.

`default-application-identifier`

The [Amazon Resource Name (ARN)](../../../IAM/latest/UserGuide/reference-arns.md "../../../IAM/latest/UserGuide/reference-arns.md") value or ID assigned to an Amazon GameLift Streams application resource. The application must be in `READY` status.

ARN example: `arn:aws:gameliftstreams:us-west-2:111122223333:application/a-9ZY8X7Wv6`

ID example: `a-9ZY8X7Wv6`

`stream-class`

**Stream class options**

The
type of compute resources to run and stream applications with. This choice impacts the quality of the streaming experience and the cost. You can specify only one stream class per stream group.
Choose the class that best
fits your application.

| Stream class    | Description                                                                                                                                                                                                                                                                                                                                                                                                                              |
| --------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `gen5n_win2022` | (NVIDIA, ultra) Supports applications with extremely high 3D scene complexity.<br>Runs applications on Microsoft Windows Server 2022 Base and supports DirectX 12 and DirectX 11.<br>Supports Unreal Engine up through version 5.5, 64-bit applications, and anti-cheat technology.<br>Uses NVIDIA A10G Tensor GPU.<br>Resources per application: vCPUs: 8. RAM: 32 GB. VRAM: 24 GB.<br>Tenancy: Supports one concurrent stream session. |
| `gen5n_high`    | (NVIDIA, high) Supports applications with moderate-to-high 3D scene complexity.<br>Uses NVIDIA A10G Tensor GPU.<br>Resources per application: vCPUs: 4. RAM: 16 GB. VRAM: 12 GB.<br>Tenancy: Supports up to two concurrent stream sessions.                                                                                                                                                                                              |
| `gen5n_ultra`   | (NVIDIA, ultra) Supports applications with extremely high 3D scene complexity.<br>Uses NVIDIA A10G Tensor GPU.<br>Resources per application: vCPUs: 8. RAM: 32 GB. VRAM: 24 GB.<br>Tenancy: Supports one concurrent stream session.                                                                                                                                                                                                      |
| `gen4n_win2022` | (NVIDIA, ultra) Supports applications with high 3D scene complexity.<br>Runs applications on Microsoft Windows Server 2022 Base and supports DirectX 12 and DirectX 11.<br>Supports Unreal Engine up through version 5.5, 64-bit applications, and anti-cheat technology.<br>Uses NVIDIA T4 Tensor GPU.<br>Resources per application: vCPUs: 8. RAM: 32 GB. VRAM: 16 GB.<br>Tenancy: Supports one concurrent stream session.             |
| `gen4n_high`    | (NVIDIA, high) Supports applications with moderate-to-high 3D scene complexity.<br>Uses NVIDIA T4 Tensor GPU.<br>Resources per application: vCPUs: 4. RAM: 16 GB. VRAM: 8 GB.<br>Tenancy: Supports up to two concurrent stream sessions.                                                                                                                                                                                                 |
| `gen4n_ultra`   | (NVIDIA, ultra) Supports applications with high 3D scene complexity.<br>Uses NVIDIA T4 Tensor GPU.<br>Resources per application: vCPUs: 8. RAM: 32 GB. VRAM: 16 GB.<br>Tenancy: Supports one concurrent stream session.                                                                                                                                                                                                                  |

`location-configurations`

A set of locations to add to this stream group, and their
capacities. By default, if no capacities are specified, Amazon GameLift Streams
will only allocate enough always-on stream capacity to start one
stream in the location where the stream group is created. For a
complete list of locations that Amazon GameLift Streams supports, refer to [AWS Regions and remote locations supported by
Amazon GameLift Streams](regions-quotas-rande.md "regions-quotas-rande.md").

Values for capacity must be whole number multiples of the
tenancy value of the stream group's stream class.

If the request is successful, then Amazon GameLift Streams returns a response similar to
the following:

```
{
    "Arn": "arn:aws:gameliftstreams:us-west-2:111122223333:streamgroup/sg-1AB2C3De4",
    "Description": "Test_gen4_high",
    "DefaultApplication": {
        "Id": "a-9ZY8X7Wv6"
    },
    "StreamClass": "gen4n_high",
    "Id": "sg-1AB2C3De4",
    "Status": "ACTIVATING",
    "LastUpdatedAt": "2024-11-18T15:49:01.482000-08:00",
    "CreatedAt": "2024-11-18T15:49:01.482000-08:00"
}
```

Amazon GameLift Streams begins searching for unallocated computing resources and provisioning them
for the new stream group, which can take several minutes. During this time,
the new stream group is in **Activating** status.

You can adjust the stream group's capacity when its status is **Active**. For
more information, refer to [Edit capacity](#stream-groups-edit-capacity "#stream-groups-edit-capacity").

When the stream group is in **Active** status, it's ready to deploy resources
for streaming. To start streaming, refer to [Start stream sessions with Amazon GameLift Streams](stream-sessions.md "stream-sessions.md").

## Edit general settings

Amazon GameLift Streams groups the following settings together in the console under **Stream
group settings**: **Status**, **Stream group
ID**, **Description**, **Stream group
ARN**, and **Stream class**. Of these, the only one that
you can update without creating a new stream group is **Description**.

Console

1. Sign in to the AWS Management Console and open the [Amazon GameLift Streams console](https://console.aws.amazon.com/gameliftstreams/ "https://console.aws.amazon.com/gameliftstreams/").
2. In the navigation bar, choose **Stream groups**
   to view a list of your existing stream groups. Choose the stream
   group you want to edit.
3. In the stream group detail page, choose **Edit
   settings**.
4. To update the description, enter a new value.

CLI
**Prerequisite**

You must configure the AWS CLI with your user credentials and your chosen AWS Region. For setup instructions, refer to [Download the AWS CLI](setting-up.md#setting-up-prereqs "setting-up.md#setting-up-prereqs").

**To edit a stream group's description using the
AWS CLI**

In your AWS CLI use the [UpdateStreamGroup](../apireference/API_UpdateStreamGroup.md "../apireference/API_UpdateStreamGroup.md") command, customized for your content.

```
aws gameliftstreams update-stream-group \
    --identifier `arn:aws:gameliftstreams:us-west-2:111122223333:streamgroup/sg-1AB2C3De4` \
    --description "`MyGame - Ultra`"
```

where

`identifier`

An
[Amazon Resource Name (ARN)](../../../IAM/latest/UserGuide/reference-arns.md "../../../IAM/latest/UserGuide/reference-arns.md") or ID that uniquely identifies the stream group resource.

ARN example: `arn:aws:gameliftstreams:us-west-2:111122223333:streamgroup/sg-1AB2C3De4`

ID example: `sg-1AB2C3De4`

`description`

A human-readable label for your stream group. This value doesn't have to be unique. As a best practice, use a meaningful description, name, or label for the stream group.
You can edit this field at any time.

## Edit capacity

Scale your stream groups by adjusting the capacity for each location.

Refer to [Amazon GameLift Streams service quotas](quotas.md "quotas.md") to learn more about stream
group capacity quotas per AWS account, per location, and how to increase these quotas.

Console

1. Sign in to the AWS Management Console and open the [Amazon GameLift Streams console](https://console.aws.amazon.com/gameliftstreams/ "https://console.aws.amazon.com/gameliftstreams/").
2. In the navigation bar, choose **Stream groups**
   to view a list of your existing stream groups. Choose the stream
   group you want to edit.
3. In the stream group detail page, choose **Edit
   configuration**.
4. For each location, enter new always-on and on-demand stream
   capacity values in the relevant cells in the table. You can request
   an increase or decrease in capacity. Values for capacity must be
   whole number multiples of the tenancy value of the stream group's
   stream class.

If you set the always-on capacity value to zero, the stream group
won't allocate any hosts to stream.

CLI
**Prerequisite**

You must configure the AWS CLI with your user credentials and your chosen AWS Region. For setup instructions, refer to [Download the AWS CLI](setting-up.md#setting-up-prereqs "setting-up.md#setting-up-prereqs").

**To edit stream capacity using the
AWS CLI**

In your AWS CLI use the [UpdateStreamGroup](../apireference/API_UpdateStreamGroup.md "../apireference/API_UpdateStreamGroup.md") command, customized for your content.

```
aws gameliftstreams update-stream-group \
    --identifier `arn:aws:gameliftstreams:us-west-2:111122223333:streamgroup/sg-1AB2C3De4` \
    --location-configurations '[{"LocationName": "`us-east-1`", "AlwaysOnCapacity": `4`}, \
        {"LocationName": "`ap-northeast-1`", "AlwaysOnCapacity": `0`, "OnDemandCapacity": `2`}]'
```

where

`identifier`

An
[Amazon Resource Name (ARN)](../../../IAM/latest/UserGuide/reference-arns.md "../../../IAM/latest/UserGuide/reference-arns.md") or ID that uniquely identifies the stream group resource.

ARN example: `arn:aws:gameliftstreams:us-west-2:111122223333:streamgroup/sg-1AB2C3De4`

ID example: `sg-1AB2C3De4`

`location-configurations`

A set of locations to update in this stream group with their
new capacities. Values for capacity must be whole number
multiples of the tenancy value of the stream group's stream
class.

When you update a stream group location's capacity, Amazon GameLift Streams will begin processing
your request, which can take a some time. During this time, Amazon GameLift Streams works to allocate or
release resources in the stream group as needed to meet the desired always-on stream
capacity you set. You can view the provisioning status of your stream capacity by
viewing the **Stream group details** page in the Amazon GameLift Streams console, or by calling the
[GetStreamGroup](../apireference/API_GetStreamGroup.md "../apireference/API_GetStreamGroup.md") API.

When your stream group is in **Active** status, has available stream capacity,
and the application has finished replicating to the location where you want to stream,
you can start streaming. For more information, refer to [Start stream sessions with Amazon GameLift Streams](stream-sessions.md "stream-sessions.md").

## Capacity scale-down behavior

When you scale down capacity, Amazon GameLift Streams waits until the host is idle before releasing
it. Since a host can support 1 or 2 sessions, the host is idle only when all active
sessions on the host end. A stream session ends when the user ends their session or the
session times out. Therefore, in extreme situations when existing sessions are allowed
to reach the maximum possible duration, it may take up to 24 hours to reach the desired
capacity. If you want to force all active stream sessions in a stream group to end, you
can delete the stream group in the console or by using the [DeleteStreamGroup](../apireference/API_DeleteStreamGroup.md "../apireference/API_DeleteStreamGroup.md") API, or
you can use the [TerminateStreamSession](../apireference/API_TerminateStreamSession.md "../apireference/API_TerminateStreamSession.md")
API to end active sessions one at a time.

## Add locations in a stream group

Console

###### To add locations to a stream group using the Amazon GameLift Streams console

1. In the navigation bar, choose **Stream groups**
   to view a list of your existing stream groups. Choose the stream
   group you want to add new locations to.
2. In the **Stream group details** page, choose **Edit
   configuration**.
3. Select the checkbox next to the location(s) you want to add to
   this stream group, and then set their capacities.
4. Review the summary of your selected locations, including the cost
   for stream capacity. Choose **Save** to confirm
   your selection.

CLI
**Prerequisite**

You must configure the AWS CLI with your user credentials and your chosen AWS Region. For setup instructions, refer to [Download the AWS CLI](setting-up.md#setting-up-prereqs "setting-up.md#setting-up-prereqs").

**To add locations to a stream group using the
AWS CLI**

In your AWS CLI use the [AddStreamGroupLocations](../apireference/API_AddStreamGroupLocations.md "../apireference/API_AddStreamGroupLocations.md") command, customized for your content.

```
aws gameliftstreams add-stream-group-locations \
    --identifier `arn:aws:gameliftstreams:us-west-2:111122223333:streamgroup/sg-1AB2C3De4`
    --location-configurations '[{"LocationName": "`us-east-1`", "AlwaysOnCapacity": `2`, "OnDemandCapacity": `2`}]'
```

where

`identifier`

An
[Amazon Resource Name (ARN)](../../../IAM/latest/UserGuide/reference-arns.md "../../../IAM/latest/UserGuide/reference-arns.md") or ID that uniquely identifies the stream group resource.

ARN example: `arn:aws:gameliftstreams:us-west-2:111122223333:streamgroup/sg-1AB2C3De4`

ID example: `sg-1AB2C3De4`

`location-configurations`

A set of locations to add to this stream group, and their
capacities. For a complete list of locations that Amazon GameLift Streams
supports, refer to [AWS Regions and remote locations supported by
Amazon GameLift Streams](regions-quotas-rande.md "regions-quotas-rande.md").

Values for capacity must be whole number multiples of the
tenancy value of the stream group's stream class.

When your application has completed replicating to the new location(s) and your
stream group has available stream capacity, you can start streaming from the new
location(s). For more information on streaming, refer to [Start stream sessions with Amazon GameLift Streams](stream-sessions.md "stream-sessions.md"). Amazon GameLift Streams will begin processing your request.
During this time, Amazon GameLift Streams works to replicate your application and allocate compute
resources in the new locations. You can view the status of the replication from the
**Linked applications** section of the
**Stream group details** page by clicking on the status in the
**Replication status** column.

## Remove locations in a stream

group

To stop using compute resources from specific locations, you can remove the locations
from your stream group. You cannot remove the primary location of a stream group.
However, if you don't want compute resources in that location, then you can set the
stream capacities to zero.

###### Warning

When you remove a location in a stream group, Amazon GameLift Streams disconnects active streams
in that location, which stops the stream of any connected end users.

Console

###### To remove locations from a stream group using the

Amazon GameLift Streams console

1. In the navigation pane, choose **Stream groups**
   to view a list of your existing stream groups.
2. Choose the name of the stream group that you want to remove
   locations from.
3. In the **Stream group details** page, choose **Edit
   configuration**.
4. Uncheck the checkbox next to the name of the location that you
   want to remove.
5. Choose **Save**.

CLI
**Prerequisite**

You must configure the AWS CLI with your user credentials and your chosen AWS Region. For setup instructions, refer to [Download the AWS CLI](setting-up.md#setting-up-prereqs "setting-up.md#setting-up-prereqs").

**To remove locations from a stream group using the
AWS CLI**

In your AWS CLI use the [RemoveStreamGroupLocations](../apireference/API_RemoveStreamGroupLocations.md "../apireference/API_RemoveStreamGroupLocations.md") command, customized for your
content.

```
aws gameliftstreams remove-stream-group-locations \
    --identifier `arn:aws:gameliftstreams:us-west-2:111122223333:streamgroup/sg-1AB2C3De4`
    --locations `us-east-1 eu-central-1`
```

where

`identifier`

An
[Amazon Resource Name (ARN)](../../../IAM/latest/UserGuide/reference-arns.md "../../../IAM/latest/UserGuide/reference-arns.md") or ID that uniquely identifies the stream group resource.

ARN example: `arn:aws:gameliftstreams:us-west-2:111122223333:streamgroup/sg-1AB2C3De4`

ID example: `sg-1AB2C3De4`

`locations`

A set of locations to remove from this stream group. For a
complete list of locations that Amazon GameLift Streams supports, refer to [AWS Regions and remote locations supported by
Amazon GameLift Streams](regions-quotas-rande.md "regions-quotas-rande.md").

## Delete a stream group

You can delete a stream group that's in any status. This action permanently deletes
the stream group and releases its compute resources. If there are streams in process,
then this action stops them and your end users can no longer view the stream.

As a best practice, before you delete a stream group, check for streams in process and
take steps to stop them.

Console

###### To delete a stream group using the Amazon GameLift Streams console

1. Sign in to the AWS Management Console and open the [Amazon GameLift Streams console](https://console.aws.amazon.com/gameliftstreams/ "https://console.aws.amazon.com/gameliftstreams/").
2. To view a list of your existing stream groups, in the navigation pane, choose **Stream groups**.
3. Choose the name of the stream group that you want to delete.
4. On the stream group detail page, choose **Delete**.
5. In the **Delete** dialog box, confirm the delete action.

CLI
**Prerequisite**

You must configure the AWS CLI with your user credentials and your chosen AWS Region. For setup instructions, refer to [Download the AWS CLI](setting-up.md#setting-up-prereqs "setting-up.md#setting-up-prereqs").

**To delete your stream group using the AWS CLI**

In your AWS CLI use the [DeleteStreamGroup](../apireference/API_DeleteStreamGroup.md "../apireference/API_DeleteStreamGroup.md") command, customized for your content.

```
aws gameliftstreams delete-stream-group \
    --identifier `arn:aws:gameliftstreams:us-west-2:111122223333:streamgroup/sg-1AB2C3De4`
```

where

`identifier`

An
[Amazon Resource Name (ARN)](../../../IAM/latest/UserGuide/reference-arns.md "../../../IAM/latest/UserGuide/reference-arns.md") or ID that uniquely identifies the stream group resource.

ARN example: `arn:aws:gameliftstreams:us-west-2:111122223333:streamgroup/sg-1AB2C3De4`

ID example: `sg-1AB2C3De4`

Amazon GameLift Streams begins releasing compute resources and deleting the stream group. During this
time, the stream group is in **Deleting** status. After Amazon GameLift Streams deletes the stream
group, you can no longer retrieve it.

## Linked applications

If you want to stream multiple application using the same pool of compute resources,
then you can link multiple applications to the same stream group. Similarly, if you want
to stream an application using different sets of compute resources, then you can link an
application to multiple stream groups.

For more information about linking applications to stream groups, refer to [Overview of multi-application stream groups](multi-apps.md "multi-apps.md").

## Stream group lifecycle

Stream groups have a maximum lifespan of 365 days. As a best practice, we recommend
that you recreate stream groups every 3-4 weeks to receive important service updates and
fixes and ensure optimal performance. Recreating a stream group does not affect your
uploaded applications.

As stream groups age, the following restrictions apply:

- **At 180 days**: You can no longer update the
  stream group with new application associations
- **At 365 days**: The stream group expires and can
  no longer stream sessions

The account associated with the stream group will receive two reminder notifications
from AWS Health: one on the 45-day and a second reminder on the 150-day. These
notifications will remind you that application association functionality will be lost on
the 180-day. There will also be one final notification on 335-day reminding you that
stream groups will expire on 365-day. Maintenance warnings also appear on the
AWS Health dashboard and on stream group pages in the Amazon GameLift Streams console.

To find the expiration date of a stream group, view the
**Stream group details** page on the console, or use the `ExpiresAt`
field in the [GetStreamGroup](../apireference/API_GetStreamGroup.md "../apireference/API_GetStreamGroup.md") API response.

An expired stream group has a status of `EXPIRED` and becomes read-only.
You cannot update it or start new stream sessions. To regain functionality, recreate the
stream group.

## Stream group maintenance

Whenever a feature is released that requires a new stream group to use it, you will
see a "Maintenance required" message at the top of the stream group's detail page to
inform you that it is outdated. Recreating a stream group is a manual process, but to
help you do it, use the **Create Stream Group** button in
the message to start the process. Some of the fields will be filled in for you.

Stream group maintenance is also required when the stream group is over 180 days old.
You will no longer be able to link new applications to these older stream groups until
they are recreated. At 365 days, streaming from the stream group will not be possible,
and no changes to the stream group will be permitted.
