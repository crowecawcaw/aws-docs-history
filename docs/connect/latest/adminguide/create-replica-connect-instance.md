# Create a replica of your existing

Amazon Connect instance

###### Note

**New user?** Check out the [Amazon Connect Global Resiliency
Workshop](https://catalog.workshops.aws/amazon-connect-global-resiliency/en-US "https://catalog.workshops.aws/amazon-connect-global-resiliency/en-US"). This online course guides you through the process of onboarding and testing phone number
and agent failover using new APIs through the AWS CLI.

Global Resiliency is available only for Amazon Connect instances created in the following AWS Regions: US East (N. Virginia),
US West (Oregon), Asia Pacific (Osaka), Asia Pacific (Tokyo), Europe (Frankfurt), and Europe (London).

- You can only create a replica in the US East (N. Virginia) Region if your source is US West (Oregon), or the other way around.
- You can only create a replica in the Europe (Frankfurt) Region if your source
  is Europe (London), or the other way around.
- You can only create a replica in Asia Pacific (Osaka) Region if your source is Asia Pacific (Tokyo).
  To obtain access to this feature, contact your Amazon Connect Solutions Architect or Technical Account Manager.

You call the [ReplicateInstance](../APIReference/API_ReplicateInstance.md "../APIReference/API_ReplicateInstance.md") API to create a replica of your Amazon Connect instance in
another AWS Region and to copy configuration information for Amazon Connect
resources across AWS Regions.

###### Contents

- [Important things
  to know](#important-info-automated-config "#important-info-automated-config")
- [Characteristics of the
  replica instance](#replica-characteristics "#replica-characteristics")
- [What resources are mirrored in
  the replica instance](#mirrored-resources "#mirrored-resources")
- [What to do after the
  replica instance is created](#configure-replica-instance "#configure-replica-instance")
- [When to contact AWS
  Support](#replica-cs "#replica-cs")
- [Why a
  ReplicateInstance call fails](#why-replicateinstance-fails "#why-replicateinstance-fails")
- [Find the
  source Region of your instance](#how-to-find-source-region-of-instances "#how-to-find-source-region-of-instances")

## Important things to

know

- Before running [ReplicateInstance](../APIReference/API_ReplicateInstance.md "../APIReference/API_ReplicateInstance.md"):
  - Make sure you have the minimum required IAM permissions to
    create an instance. See [Required permissions for using
    custom IAM policies to manage access to the Amazon Connect console](security-iam-amazon-connect-permissions.md "security-iam-amazon-connect-permissions.md").
  - Update your flows to replace any hardcoded Regions with a
    `$.AwsRegion` or `$['AwsRegion']`
    parameter. At flow runtime, these parameters are replaced with
    the Region where the flow is run.
  - Ensure your Lambda functions across AWS Regions
    have the same name.
  - For Amazon Lex bots, you can do one of the following:
    - Use Amazon Lex Global Resiliency to replicate bots across
      AWS Regions and retain the bot ID.
    - Change your flows to branch based on the AWS Region
      where the flow is running. At flow runtime, these
      parameters are replaced with the Region where the flow
      is run, as shown in the following example.

    ![The properties page of the check contact attributes block.](images/acgr-requirements.png)

  - To allow AWS managed keys in the replica instance, using the
    AWS console, create a temporary Amazon Connect instance in the Region
    where you are planning to create the replica instance. This will
    create the default AWS managed keys for Amazon Connect.

- [ReplicateInstance](../APIReference/API_ReplicateInstance.md "../APIReference/API_ReplicateInstance.md") copies the Amazon Connect configuration across
  AWS Regions as part of the initial replication
  process. After this first step completes, any changes made to either the
  original or [mirrored resources](#mirrored-resources "#mirrored-resources")
  at a later time are continuously synchronized. This happens
  bidirectionally, from source to replica, and from the replica to the
  source.
- All phone numbers on the source instance that aren't already
  associated to number groups are automatically added to the default
  traffic distribution group. This step enables the phone numbers to be
  available in both source and replica Regions, and enables phone
  number-flow associations to be mirrored across AWS Regions.
- For instances in Asia Pacific (Tokyo), only phone numbers that are
  explicitly enabled for Amazon Connect Global Resiliency (ACGR) will support
  complete replication behavior to Asia Pacific (Osaka). When routing
  through Asia Pacific (Osaka), inbound calls may experience delivery
  times of up to 20 seconds.
- Emergency access to log into the replica instance is available only
  after the default routing profile and queue have been mirrored across
  the Regions.
- As the configuration is propagated across AWS Regions,
  you can view the progress in AWS CloudTrail logs. Or, in the Amazon Connect admin website you can
  navigate to **User management**, **View
  historical changes** to view an audit trail of changes to
  the users. Audit trails are also available for other
  configurations.
- You may see the following errors in the CloudTrail log which do not impact
  the configurations mirroring.
  - Http 409 (conflict) errors: These errors occur due to
    mirroring conflicts when processing multiple configuration
    updates made to the same contact center resource in quick
    succession. While these errors might appear in your logs, they
    do not impact the actual mirroring of your contact center
    resources.

- A resource name conflict will occur if resources in the source
  instance and the replica instance have the same name but different
  resource IDs. This might happen, for example, if the resource in the
  replica instance was created manually outside of the replication
  process.

In the case of resource name conflicts, [ReplicateInstance](../APIReference/API_ReplicateInstance.md "../APIReference/API_ReplicateInstance.md") doesn't synchronize the resource across
Regions. Instead it throws a `ResourceConflictException`
error. After you resolve the name conflict (for example, delete the
resource in the replica instance), you can run
`ReplicateInstance` again to synchronize the
resource.

- After running `ReplicateInstance`, you must use the [AssociateTrafficDistributionGroupUser](../APIReference/API_AssociateTrafficDistributionGroupUser.md "../APIReference/API_AssociateTrafficDistributionGroupUser.md") API to associate
  agents to either the default traffic distribution group or a custom
  traffic distribution group.
- Running [ReplicateInstance](../APIReference/API_ReplicateInstance.md "../APIReference/API_ReplicateInstance.md") does not synchronize Lambda functions or
  Amazon Lex bots, or other third-party / integrations you may have.

## Characteristics of the replica

instance

- The replica Amazon Connect instance is created in the same AWS
  account as your existing Amazon Connect instance.
- [ReplicateInstance](../APIReference/API_ReplicateInstance.md "../APIReference/API_ReplicateInstance.md") creates a default traffic distribution group if one doesn't
  already exist. This default traffic distribution group has three types of traffic
  distribution:

      + Sign in
      + Agent
      + Telephony

  Use the [CreateTrafficDistributionGroup](../APIReference/API_CreateTrafficDistributionGroup.md "../APIReference/API_CreateTrafficDistributionGroup.md") API to create more traffic distribution groups,
  however, these additional traffic distribution groups are not default traffic distribution groups and thus only
  support agent and telephony distributions.

- The default traffic distribution group is the only traffic distribution group where you can change the
  `SignInConfig` distribution. See the
  `IsDefault` parameter in the [TrafficDistributionGroup](../APIReference/API_TrafficDistributionGroup.md "../APIReference/API_TrafficDistributionGroup.md") data type.
- You use `SignInConfig` to choose the backend sign-in
  servers to facilitate the agent signing in to their Amazon Connect instance. For
  example, if you call `UpdateTrafficDistribution` with a
  modified `SignInConfig` and a non-default
  `TrafficDistributionGroup`, an
  `InvalidRequestException` is returned.
- The replica instance has the same instance ID as the Amazon Connect instance it
  is replicated from.

## What resources are mirrored in the replica

instance

[ReplicateInstance](../APIReference/API_ReplicateInstance.md "../APIReference/API_ReplicateInstance.md") mirrors the following Amazon Connect
resources across AWS Regions.

###### Important

The service quotas for these resources are automatically matched across
AWS Regions
_before_ the resources are mirrored across Regions. To
increase any other quota in the replica instance, submit a request.

- Agent proficiencies
- Flows
- Flow modules
- Users
- Routing profiles
- Queues
- Security profiles
- Hours of operation
- Quick connects
- Predefined attributes
- Prompts (not including those stored in S3)
- User hierarchies (groups and levels)
- Agent status
- Predefined attributes
- Saved reports

[ReplicateInstance](../APIReference/API_ReplicateInstance.md "../APIReference/API_ReplicateInstance.md") also replicates the following associations across
AWS Regions:

- Phone number to flow
- Queue to routing profile
- User to security profile, routing profile, and user hierarchy
- Routing profiles
- Queue to quick connects
- Queue to hours of operation
- Queue to flow

###### Note

After initial replication, configuration changes are replicated
bidirectionally between replicated instances in near real-time. If this fails,
Amazon Connect Global Resiliency attempts to sync updates within 30 minutes.

## What to do after the replica

instance is created

After your replica Amazon Connect instance is created, you need to configure it:

1. Ensure redundancy for front-end and back-end integrations (for
   example, SSO, Lambda, Lex) across Regions.
2. Make matching manual updates across the linked instances.
3. Use the [AssociateTrafficDistributionGroupUser](../APIReference/API_AssociateTrafficDistributionGroupUser.md "../APIReference/API_AssociateTrafficDistributionGroupUser.md") API to associate
   agents to the default traffic distribution group.

Before you can associate agents to a traffic distribution group, they
must be present on both the source and replica instances. You cannot
associate users to a traffic distribution group when they are newly
added to source instance and not yet in the replica.

## When to contact AWS Support

Contact AWS Support for help with the following activities:

- To understand mirroring status beyond what's available in the CloudTrail
  logs and audit trail in the Amazon Connect admin website.

## Why a ReplicateInstance call

fails

A [ReplicateInstance](../APIReference/API_ReplicateInstance.md "../APIReference/API_ReplicateInstance.md") API call fails with an
`InvalidRequestException` in the following cases:

1. The Region where you are creating the replica is the same Region as
   your existing instance.
2. The instance was already replicated as part of a different [ReplicateInstance](../APIReference/API_ReplicateInstance.md "../APIReference/API_ReplicateInstance.md") API call.
3. The instance does not have an alias.
4. The instance is not in `ACTIVE` status.
5. The instance does not have SAML enabled.
6. There is a resource name conflict.

## How to find the source

Region of your Amazon Connect instances

If you forget which Region is your source Region for your Amazon Connect instances,
perform the following steps to find it:

1. Call the [ListTrafficDistributionGroups](../APIReference/API_ListTrafficDistributionGroups.md "../APIReference/API_ListTrafficDistributionGroups.md") API with your
   `InstanceId`.
2. For any traffic distribution group in the response list, the returned
   `InstanceARN` includes the source Region. For example in
   the following ARN, `source-region` would be the
   Region of your Amazon Connect instance.

`arn:aws:connect:`source-region`:`account-id`:traffic-distribution-group/
 `traffic-distribution-group-id``
