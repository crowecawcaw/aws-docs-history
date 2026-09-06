

# Global routing across ACGR Regions
<a name="global-routing-across-acgr-regions"></a>

**Important**  
Global routing is enabled for new ACGR instances created on or after September 1, 2026, by default. To enable global routing for existing ACGR instances, please reach out to [AWS Support](https://console.aws.amazon.com/support/home).

With Connect Customer Global Resiliency (ACGR), you can link instances across two AWS Regions to create a highly available contact center that meets regulatory requirements mandating redundancy across geographically distant locations, or business continuity requirements that demand the highest level of resiliency. Global routing extends this capability by allowing contacts that originate in one Region to be routed to agents signed in to the linked Region, so both Regions are active at all times. Because your full configuration and integrations are continuously exercised, you gain higher confidence that either Region is ready to handle the full workload whenever you need to shift traffic to one Region.

For information about setting up ACGR, see [Set up Connect Customer Global Resiliency](setup-connect-global-resiliency.md). For requirements and prerequisites, see [Connect Customer Global Resiliency requirements](connect-global-resiliency-requirements.md).

## How global routing works
<a name="how-global-routing-works"></a>

Without global routing, each Connect Customer instance makes routing decisions independently. For example, contacts that originate in the us-east-1 instance can be routed only to agents signed into us-east-1. Global routing changes this behavior for linked ACGR instances. Instead, the routing service evaluates agents from both Regions simultaneously and directs each contact to the appropriate matching agent regardless of which ACGR instance the agent is signed in to.

Global routing works with your existing traffic distribution group configuration. You continue to use the [UpdateTrafficDistribution](https://docs.aws.amazon.com/connect/latest/APIReference/API_UpdateTrafficDistribution.html) API to control how telephony traffic and agents are distributed across Regions. For more information about traffic distribution groups, see [Set up traffic distribution groups](setup-traffic-distribution-groups.md).

**Note**  
Not all Connect Customer features are supported out-of-the-box for cross-region routing. See [Supported features for cross-region routing](#global-routing-supported-features) for details.

## Key concepts
<a name="global-routing-key-concepts"></a>

The following concepts apply when you use global routing:
+ The contact's **active Region** is the AWS Regions where a contact originates. For an inbound voice call, this is determined by the Region that receives the telephony traffic based on your traffic distribution group telephony distribution settings.
+ The agent's **active Region** is the AWS Regions where an agent is currently active and handling contacts. The traffic distribution group agent distribution settings determine what percentage of your agents sign in to each Region.
+ **Cross-region routing** occurs when a contact that originates in one Region is connected to an agent in the other linked Region. The contact itself remains in the origin Region throughout its lifecycle; only the routing decision spans Regions.

## Subdomain-based instance aliases
<a name="subdomain-based-instance-aliases"></a>

To use global routing, you must use the subdomain-based instance aliases, where the source and replica instances share the same alias name differentiated by a regional subdomain prefix. For example, if your primary instance is named `example`, your instances are addressed as follows:
+ Source: `us-east-1.example.my.connect.aws`
+ Replica: `us-west-2.example.my.connect.aws`

**Note**  
`ReplicaAlias` is currently still a required field when invoking the [ReplicateInstance](https://docs.aws.amazon.com/connect/latest/APIReference/API_ReplicateInstance.html) API to create a replica. However, after the `ReplicateInstance` API is called, the replica alias is automatically derived from the source alias and you no longer need to use the custom replica alias going forward.

If you are using a custom CCP built with [Amazon Connect Streams](https://github.com/amazon-connect/amazon-connect-streams), ensure that you update the `connect.core.initCCP` call to include both instance URLs (using the subdomain-based instance aliases):

```
connect.core.initCCP(containerDiv, {
  ccpUrl: "https://us-east-1.example.my.connect.aws/ccp-v2/",
  secondaryCCPUrl: "https://us-west-2.example.my.connect.aws/ccp-v2/",
  enableGlobalResiliency: true,
  loginUrl: "<URL for your SSO provider>",
  // Additional initCCP parameters
});
```

**Note**  
Any previously created source and replica aliases continue to work for their respective instances. However, for agents to accept cross-region contacts, you must add the new subdomain-based URLs to your firewall allowlist. For more details, see [Migrating to global routing](#migrating-to-global-routing).

## Agent experience with cross-region contacts
<a name="agent-experience-cross-region"></a>

As before, agents continue to sign in via the global sign-in endpoint and are distributed across Regions based on their traffic distribution group configuration. The Agent Workspace has been updated to handle cross-region contacts. Global routing is also supported for custom Contact Control Panel (CCP) built with [Amazon Connect Streams](https://github.com/amazon-connect/amazon-connect-streams). When an agent receives a cross-region contact, the experience will be the same as when handling a same-region contact; the agent does not need to take any special action.

However, please note that certain resources such as Chat Quick Responses and Task Templates are not currently automatically replicated across ACGR instances (see [What resources are mirrored in the replica instance](create-replica-connect-instance.md#mirrored-resources)). If you use these resources, please plan to replicate them yourself to provide a consistent agent experience across Regions.

You continue to use the [UpdateTrafficDistribution](https://docs.aws.amazon.com/connect/latest/APIReference/API_UpdateTrafficDistribution.html) API to shift agents across Regions. If an agent is handling a contact when their traffic distribution group configuration is updated, they can complete the contact prior to being switched to the alternate Region. The UpdateTrafficDistribution API only affects new incoming contacts. For example, if you update the traffic distribution group to direct 100% of agents and incoming calls to us-west-2, contacts that were already queued in us-east-1 will remain queued in us-east-1 until they are handled. With global routing enabled, any queued contacts remaining in us-east-1 can still be handled by agents in us-west-2, potentially improving business continuity in case all agents are shifted to the other Region. Alternately, you can temporarily disable and re-enable global routing via the [UpdateCrossRegionRouting](https://docs.aws.amazon.com/connect/latest/APIReference/API_UpdateCrossRegionRouting.html) API.

## Consolidated metrics and search
<a name="consolidated-metrics-search"></a>

With global routing, supervisors and administrators see a consolidated view of contact and agent metrics across both Regions regardless of which Region they are signed in to. For example, if 8 agents are available for a queue, then real-time metrics and dashboards display a total count of 8 Agents Available, regardless of what Region the agents are signed into or what Region the supervisor is viewing the report from. This global view extends to historical metrics and the reporting APIs (`GetMetricDataV2`, `GetCurrentUserData`, `GetCurrentMetricData`).

Contact Search enables supervisors to find and view contacts handled across both paired instances in a single view, including agent details, analytics, call recording, and transcripts. Supervisors must sign in via the global sign-in endpoint to access consolidated contact search.

For more information, see [Metrics, Reports and Search across ACGR Regions](metrics-reports-and-search-across-acgr-regions.md).

## Event streams behavior
<a name="event-streams-global-routing"></a>

The following table summarizes where event streams are available when global routing is enabled.


| Stream type | Behavior | 
| --- | --- | 
| Contact Event Streams (CES) | Emitted in both Regions regardless of where the contact originates. You can filter by the originRegion and activeRegion fields in the globalResiliencyMetadata object. | 
| Agent Event Streams (AES) | Emitted only in the Region where the agent is active. The alternate Region receives only Login and Offline events. | 
| Contact Records (CTR) | Available in the Region where the contact originates. For example, a contact that originates in us-east-1 and is answered by an agent in us-west-2 has its CTR in us-east-1. | 

Since AES and CTR remain regional, update your third-party integration pipelines to consume data from both Regions. While CES provides a consolidated view, we recommend building integration pipelines in both Regions for resiliency.

## Temporarily disabling cross-region routing
<a name="disabling-cross-region-routing"></a>

Use the [UpdateCrossRegionRouting](https://docs.aws.amazon.com/connect/latest/APIReference/API_UpdateCrossRegionRouting.html) API to temporarily disable or re-enable global routing. When global routing is disabled, contacts originating in one Region are no longer routed to agents in the other Region. Contacts that are currently connected to an agent in another Region will not be disconnected when the API is invoked; the agent can complete handling that contact, but will no longer be routed additional contacts from the other Region.

**Important**  
This API only stops cross-region routing. Consolidated reporting, contact search, and resource replication continue to operate globally after you execute the API.

## Additional considerations for custom integrations (StreamsJS, AWS SDK, Connect SDK for Agent Workspace)
<a name="streamsjs-connect-sdk-updates"></a>

While StreamsJS and Connect SDK for Agent Workspace have been updated to support cross-region routing, applications that invoke public APIs in the AWS SDK may need to be updated to fetch the contact's active Region and the agent's active Region, and direct API calls accordingly:
+ Mutation operations on a contact (such as `UpdateContactAttributes` or `TransferContact`) must be performed against the contact's origin Region.
+ Mutation operations on an agent (such as `PutUserStatus`) must be performed against the Region where the agent is active.
+ Read operations (such as `DescribeContact`) can be performed against either Region.

The following table outlines some common use cases for reference.


| Example use case | Notes | 
| --- | --- | 
| Third-party application in Agent Workspace that consumes only native Connect Customer SDK events and requests such as getARN(), listQuickConnects(), accept(), cleared() | The application will not require updates for cross-region invocation. The Connect Customer SDK for Agent Workspace has been updated to support cross-region invocation in the backend. | 
| Custom CCP that calls only StreamsJS APIs such as contact.accept(), agent.mute() | The application will not require updates for cross-region invocation. StreamsJS has been updated to support cross-region invocation in the backend. | 
| Application that calls SearchUsers (AWS SDK) to display a list of all agents who belong to a particular Routing Profile | The application will not require updates for cross-region invocation. Because the User resource is replicated across both Regions (see [What resources are mirrored in the replica instance](create-replica-connect-instance.md#mirrored-resources)), invoking SearchUsers in either of the ACGR instances returns identical results. | 
| Application that calls GetCurrentMetricData (AWS SDK) to display queue metrics such as contacts in queue | The application will not require any updates for cross-region invocation. The GetCurrentMetricData, GetMetricDataV2, and GetCurrentUserData APIs return the same global view regardless of which Region you are invoking the API from. For more detail, see [Metrics, Reports and Search across ACGR Regions](metrics-reports-and-search-across-acgr-regions.md). | 
| Application that calls the DescribeContact API, for example to display contact attributes to the agent working on the contact via a third-party application in Agent Workspace or custom CCP | The application will not require any updates for cross-region invocation. With consolidated contact search, the DescribeContact API returns the same API response regardless of which Region you are calling it from. For more detail, see [Metrics, Reports and Search across ACGR Regions](metrics-reports-and-search-across-acgr-regions.md). | 
| Application that calls the UpdateContactAttributes API (AWS SDK), for example to store a disposition code as a contact attribute | You will need to update your application to check the contact's Region and make the API call to the appropriate Region. Contact mutation operations such as UpdateContactAttributes and TransferContact are available only in the contact's Region. | 
| Custom analytics dashboard where supervisors can monitor contacts via the MonitorContact API and change an agent's status via the PutUserStatus API | You will need to update your application to check the contact's Region and the agent's Region, and make each API call to the appropriate Region. Contact APIs such as MonitorContact and AssociateContactWithUser are available in the contact's Region, while agent APIs such as PutUserStatus are available only in the agent's Region. | 

The contact's active Region and the agent's active Region can be identified in the following interfaces.


| Interface | Contact's active Region | Agent's active Region | 
| --- | --- | --- | 
| Connect SDK for Workspace | To get the contact's Region, use ContactClient.getContactRegion(contactId). | To get the agent's Region, use UserClient.getUserRegion(). | 
| StreamsJS | Use the connect.\_getContactRegion internal helper. | The agent's Region can be fetched from the ARN of any resource in the agent snapshot, using the connect.\_parseRegionFromArn internal helper. | 
| Agent Event Stream | The contact Region is identified in the GlobalResiliencyMetadata object. For more detail, see [Agent event streams data model](agent-event-stream-model.md). | The agent's active Region is identified in the AgentCrossRegionRoutingConfiguration object. For more detail, see [Agent event streams data model](agent-event-stream-model.md). | 
| Contact Event Stream | The contact's Region is indicated in the GlobalResiliencyMetadata object. For more detail, see [Connect contact events (CES)](contact-events.md). | The agent Region is indicated via ActiveRegion on the AgentInfo object. For more detail, see [Connect contact events (CES)](contact-events.md). | 
| DescribeContact API call | The contact's Region is indicated in the GlobalResiliencyMetadata object. For more detail, see [DescribeContact](https://docs.aws.amazon.com/connect/latest/APIReference/API_DescribeContact.html) response syntax. | The agent Region is indicated via ActiveRegion on the AgentInfo object. For more detail, see [DescribeContact](https://docs.aws.amazon.com/connect/latest/APIReference/API_DescribeContact.html) response syntax. | 
| Contact Trace Record | The contact's Region is indicated in the GlobalResiliencyMetadata object. For more detail, see [Data model for contact records](ctr-data-model.md). | The agent Region is indicated via ActiveRegion on the Agent object. For more detail, see [Data model for contact records](ctr-data-model.md). | 

**Important**  
If you have third-party applications in Agent Workspace, please note that you must associate third-party applications with both your primary and replica instances. Third-party applications are not automatically replicated across ACGR instances. If you perform cross-region app invocation, add the application URL as an approved origin in both instances.

## Supported features for cross-region routing
<a name="global-routing-supported-features"></a>

For a consistent agent experience across same-region and cross-region contacts, please ensure all relevant resources are replicated across both instances. For a list of which resources are currently mirrored automatically in Connect Customer Global Resiliency, see [What resources are mirrored in the replica instance](create-replica-connect-instance.md#mirrored-resources).

Connect Customer features that are currently supported for cross-region operation include the following.


| Feature | Notes | 
| --- | --- | 
| Voice calls | Voice calls can be routed cross-region. However, please note that in-app, web, video calling, and screen sharing capabilities are not supported for cross-region routing at this time. | 
| Customer-first callbacks; queued callbacks | Both queued callbacks and customer-first callbacks (where the dialed leg has been accepted by the customer and queued) can be routed cross-region to an agent in the alternate Region. | 
| Chats | Chats can be routed cross-region. Chat quick responses are not natively replicated across Regions. You must replicate these yourself for a consistent agent experience across Regions. Chat quick responses are fetched from the contact's Region. | 
| Tasks | Tasks can be routed cross-region. Task templates are not natively replicated. You must replicate these yourself for a consistent agent experience across Regions. When an agent is not on any contacts, task templates are fetched from the agent's active Region. When the agent is handling a task, task templates are fetched from the contact's Region. | 
| Emails | Emails can be routed cross-region. However, email-specific configuration such as email message templates are not natively replicated. You must replicate these yourself for a consistent agent experience across Regions.<br />For email-heavy workloads, consider keeping email agents in a single Region to avoid limitations with email capabilities. You can use traffic distribution groups to manage email agents differently from voice-only agents. For example:+  Assign all email agents (including any blended agents) to a traffic distribution group with 100% agent distribution to a single Region. <br />+  Assign voice-only agents to a separate traffic distribution group with traffic split across both Regions. <br />+  Route all email traffic to the primary Region.  | 
| Enhanced multi-party call monitoring and barge | Supervisors can monitor or barge cross-region voice calls via enhanced multi-party call monitoring using out-of-the-box dashboards. To monitor cross-region contacts via API, ensure that you invoke the MonitorContact API from the contact's Region. Please note that three-party call monitoring is not supported for cross-region monitoring. | 
| Enhanced contact monitoring for chat contacts | Supervisors can monitor cross-region chat contacts. | 
| Routing to a specific agent via agent queue, preferred agent routing, or Interrupt agent block | Just like contacts in standard queues (including contacts with routing criteria set, such as a preferred agent), contacts in an agent queue can be offered to the specified agent even if that agent is active in the alternate Region. The Interrupt agent flow block will also offer the contact to the agent regardless of Region. However, the Transfer to agent (beta) flow block does not support cross-region routing; instead, use the Set working queue block to specify the agent queue followed by the Transfer to queue block. | 
| Call recordings | Contact recordings are generated for both same-region and cross-region calls. Call recordings are stored in the contact's origin Region. Recordings can be accessed from contact search and the contact detail page from either Region via consolidated contact search. | 
| Live media streaming | Connect Customer streams Kinesis Video Streams (KVS) audio in the contact's origin Region. If a contact originates in us-east-1 and is answered by an agent in us-west-2, the KVS audio is available in us-east-1. If you use KVS for features like voicemail capture or third-party call analytics, build integration pipelines in both Regions since contacts can originate in either Region. | 
| Screen recordings | Screen recordings are currently generated for same-region contacts but not cross-region contacts. Screen recordings can be accessed from contact search and the contact detail page from either Region via consolidated contact search. | 
| Salesforce CTI Adapter | Global routing is supported for Salesforce CTI Adapter v5.33 and Salesforce lambda package v5.27. | 

## Migrating to global routing
<a name="migrating-to-global-routing"></a>

ACGR instances created before September 1, 2026 do not have access to global routing by default. To request access to this feature, contact your AWS account team. Once your instance is enabled for global routing, review the following steps:

1. Update any integrations that consume the Connect Customer instance alias in the replica Region, including your custom CCP, to use the new subdomain-based instance alias.

1. Update your firewall rules to allow the new subdomain-based instance alias if your rules do not use wildcards.

1. Identify changes needed for third-party integrations such as custom reporting, Workforce Management solutions, or systems that rely on event streams and contact records.

1. Identify changes needed for third-party integrations that consume the Connect Customer instance URL. Ensure to update the integration to consume the new subdomain alias.

1. Update Streams JS to include `secondaryCCPUrl` and `enableGlobalResiliency` parameters in your custom agent desktop.

1. Once ready, call the [ReplicateInstance](https://docs.aws.amazon.com/connect/latest/APIReference/API_ReplicateInstance.html) API from the source Region. This enables global routing, consolidated analytics, consolidated contact search, and corresponding changes to event streams and contact records.

1. Monitor replication status using the [DescribeInstance](https://docs.aws.amazon.com/connect/latest/APIReference/API_DescribeInstance.html) API. Wait until the status reflects `INSTANCE_REPLICATION_COMPLETE`.

1. Validate by signing agents into the replica Region and verifying that cross-region routing works as expected.

**Note**  
If agents were already signed in when you enabled global routing, they must sign out and sign back in for cross-region routing to take effect. Otherwise, they will not be able to see and accept cross-region contacts in the CCP. For that reason, we recommend waiting past the default agent session timeout period for Connect Customer (12 hours) before you start distributing contacts and agents across different Regions.

If you are using a custom CCP built with [Amazon Connect Streams](https://github.com/amazon-connect/amazon-connect-streams), then you may want to maintain failover logic in your custom CCP during the migration by defining variables for both the previous replica domain and the new subdomain-based domain. Then, use conditional logic to fall back to the previous domain if the new domain is unreachable during the transition period.