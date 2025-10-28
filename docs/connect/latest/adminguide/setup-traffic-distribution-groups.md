# Create traffic distribution groups for your Amazon Connect

instance

You can create a traffic distribution group for your existing Amazon Connect instance by using the [CreateTrafficDistributionGroup](../APIReference/API_CreateTrafficDistributionGroup.md "../APIReference/API_CreateTrafficDistributionGroup.md") API.

A _traffic distribution group_ is an Amazon Connect resource that enables you to link Amazon Connect
instances that are in different AWS Regions. Phone numbers can be
attached to the traffic distribution group. Traffic to these numbers can be distributed between the
instances in the traffic distribution group.

## Important things to know

- When creating a traffic distribution group, it must be created in the source AWS Region. A _source Region_ is the
  Region where you set up your existing Amazon Connect instance.
- When associating phone numbers to a traffic distribution group:
  - You can associate only phone numbers that are claimed in the
    source Region.
  - The phone number must be in the same Region as where the traffic distribution group
    was created.

- You can claim numbers to a traffic distribution group, or get or
  update traffic distribution for a traffic distribution group only when its
  `Status` is `ACTIVE`. Use the [DescribeTrafficDistributionGroup](../APIReference/API_DescribeTrafficDistributionGroup.md "../APIReference/API_DescribeTrafficDistributionGroup.md") API to determine whether
  it has been created successfully (`Status` must be
  `ACTIVE`).
- When you create a replica Amazon Connect instance, a default traffic distribution group is created
  for it. The default traffic distribution group is the only traffic distribution group where you can change the
  `SignInConfig` distribution. See the
  `IsDefault` parameter in the [TrafficDistributionGroup](../APIReference/API_TrafficDistributionGroup.md "../APIReference/API_TrafficDistributionGroup.md") data type. You use
  `SignInConfig` to choose which backend sign-in servers
  are used to facilitate the agent signing in to their Amazon Connect instance. For
  example, if you call `UpdateTrafficDistribution` with a
  modified `SignInConfig` and a non-default
  `TrafficDistributionGroup`, an
  `InvalidRequestException` is returned.

## Traffic distribution group statuses

Following is a description of the traffic distribution group statuses:

- `CREATION_IN_PROGRESS`: Traffic distribution group creation
  is in progress.
- `ACTIVE`: Traffic distribution group has been
  created.
- `CREATION_FAILED`: Traffic distribution group creation
  failed.
- `PENDING_DELETION`: Traffic distribution group deletion is
  in progress.
- `DELETION_FAILED`: Traffic distribution group deletion
  failed.
- `UPDATE_IN_PROGRESS`: Traffic distribution group update is
  in progress.

## Why a

CreateTrafficDistributionGroup call fails

A [CreateTrafficDistributionGroup](../APIReference/API_CreateTrafficDistributionGroup.md "../APIReference/API_CreateTrafficDistributionGroup.md") API call fails with an
`InvalidRequestException` in the following cases:

- The [ReplicateInstance](../APIReference/API_ReplicateInstance.md "../APIReference/API_ReplicateInstance.md") API was not called before creating a
  traffic distribution group for the linked instances.
- The [CreateTrafficDistributionGroup](../APIReference/API_CreateTrafficDistributionGroup.md "../APIReference/API_CreateTrafficDistributionGroup.md") API was not called in the
  same Region where the [ReplicateInstance](../APIReference/API_ReplicateInstance.md "../APIReference/API_ReplicateInstance.md") API was called. The Region where this API
  is called must match the Region of the instance that was used to create
  a replica.
