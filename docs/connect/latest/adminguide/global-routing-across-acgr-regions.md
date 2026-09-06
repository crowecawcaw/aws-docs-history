# Global routing across ACGR Regions

###### Important

Global routing is enabled for new ACGR instances created on or after September 1,
2026, by default. To enable global routing for existing ACGR instances, please reach
out to [AWS
Support](https://console.aws.amazon.com/support/home "https://console.aws.amazon.com/support/home").

With Connect Customer Global Resiliency (ACGR), you can link instances across two AWS Regions to create a highly available contact center that meets regulatory
requirements mandating redundancy across geographically distant locations, or business
continuity requirements that demand the highest level of resiliency. Global routing extends
this capability by allowing contacts that originate in one Region to be routed to agents
signed in to the linked Region, so both Regions are active at all times. Because your full
configuration and integrations are continuously exercised, you gain higher confidence that
either Region is ready to handle the full workload whenever you need to shift traffic to one
Region.

For information about setting up ACGR, see [Set up Connect Customer Global Resiliency](setup-connect-global-resiliency.md "setup-connect-global-resiliency.md"). For
requirements and prerequisites, see [Connect Customer Global Resiliency
requirements](connect-global-resiliency-requirements.md "connect-global-resiliency-requirements.md").

## How global routing works

Without global routing, each Connect Customer instance makes routing decisions independently.
For example, contacts that originate in the us-east-1 instance can be routed only to
agents signed into us-east-1. Global routing changes this behavior for linked ACGR
instances. Instead, the routing service evaluates agents from both Regions
simultaneously and directs each contact to the appropriate matching agent regardless of
which ACGR instance the agent is signed in to.

Global routing works with your existing traffic distribution group configuration. You continue to use the
[UpdateTrafficDistribution](../APIReference/API_UpdateTrafficDistribution.md "../APIReference/API_UpdateTrafficDistribution.md") API to control how telephony traffic and agents
are distributed across Regions. For more information about traffic distribution groups, see [Set up traffic distribution groups](setup-traffic-distribution-groups.md "setup-traffic-distribution-groups.md").

###### Note

Not all Connect Customer features are supported out-of-the-box for cross-region routing.
See [Supported features for
cross-region routing](#global-routing-supported-features "#global-routing-supported-features") for details.

## Key concepts

The following concepts apply when you use global routing:

- The contact's **active Region** is the AWS Regions where a contact originates. For
  an inbound voice call, this is determined by the Region that receives the
  telephony traffic based on your traffic distribution group telephony distribution settings.
- The agent's **active Region** is the AWS Regions where an agent is currently active
  and handling contacts. The traffic distribution group agent distribution settings determine what
  percentage of your agents sign in to each Region.
- **Cross-region routing** occurs when a contact
  that originates in one Region is connected to an agent in the other linked
  Region. The contact itself remains in the origin Region throughout its lifecycle;
  only the routing decision spans Regions.

## Subdomain-based instance aliases

To use global routing, you must use the subdomain-based instance aliases, where the
source and replica instances share the same alias name differentiated by a regional
subdomain prefix. For example, if your primary instance is named
`example`, your instances are addressed as follows:

- Source: `us-east-1.example.my.connect.aws`
- Replica: `us-west-2.example.my.connect.aws`

###### Note

`ReplicaAlias` is currently still a required field when invoking the
[ReplicateInstance](../APIReference/API_ReplicateInstance.md "../APIReference/API_ReplicateInstance.md") API to create a replica. However, after the
`ReplicateInstance` API is called, the replica alias is automatically
derived from the source alias and you no longer need to use the custom replica alias
going forward.

If you are using a custom CCP built with [Amazon Connect
Streams](https://github.com/amazon-connect/amazon-connect-streams "https://github.com/amazon-connect/amazon-connect-streams"), ensure that you update the
`connect.core.initCCP` call to include both instance URLs (using the
subdomain-based instance aliases):

```
connect.core.initCCP(containerDiv, {
  ccpUrl: "https://us-east-1.example.my.connect.aws/ccp-v2/",
  secondaryCCPUrl: "https://us-west-2.example.my.connect.aws/ccp-v2/",
  enableGlobalResiliency: true,
  loginUrl: "<URL for your SSO provider>",
  // Additional initCCP parameters
});
```

###### Note

Any previously created source and replica aliases continue to work for their
respective instances. However, for agents to accept cross-region contacts, you must
add the new subdomain-based URLs to your firewall allowlist. For more details, see
[Migrating to global
routing](#migrating-to-global-routing "#migrating-to-global-routing").

## Agent experience with cross-region contacts

As before, agents continue to sign in via the global sign-in endpoint and are
distributed across Regions based on their traffic distribution group configuration. The Agent Workspace has
been updated to handle cross-region contacts. Global routing is also supported for
custom Contact Control Panel (CCP) built with [Amazon Connect
Streams](https://github.com/amazon-connect/amazon-connect-streams "https://github.com/amazon-connect/amazon-connect-streams"). When an agent receives a cross-region contact, the experience will
be the same as when handling a same-region contact; the agent does not need to take any
special action.

However, please note that certain resources such as Chat Quick Responses and Task
Templates are not currently automatically replicated across ACGR instances (see [What resources are mirrored in the replica
instance](create-replica-connect-instance.md#mirrored-resources "create-replica-connect-instance.md#mirrored-resources")). If you use these resources, please plan to replicate them yourself
to provide a consistent agent experience across Regions.

You continue to use the [UpdateTrafficDistribution](../APIReference/API_UpdateTrafficDistribution.md "../APIReference/API_UpdateTrafficDistribution.md") API to shift agents across Regions. If an agent
is handling a contact when their traffic distribution group configuration is updated, they can complete the
contact prior to being switched to the alternate Region. The UpdateTrafficDistribution
API only affects new incoming contacts. For example, if you update the traffic distribution group to direct
100% of agents and incoming calls to us-west-2, contacts that were already queued in
us-east-1 will remain queued in us-east-1 until they are handled. With global routing
enabled, any queued contacts remaining in us-east-1 can still be handled by agents in
us-west-2, potentially improving business continuity in case all agents are shifted to
the other Region. Alternately, you can temporarily disable and re-enable global routing
via the [UpdateCrossRegionRouting](../APIReference/API_UpdateCrossRegionRouting.md "../APIReference/API_UpdateCrossRegionRouting.md") API.

## Consolidated metrics and search

With global routing, supervisors and administrators see a consolidated view of
contact and agent metrics across both Regions regardless of which Region they are signed
in to. For example, if 8 agents are available for a queue, then real-time metrics and
dashboards display a total count of 8 Agents Available, regardless of what Region the
agents are signed into or what Region the supervisor is viewing the report from. This
global view extends to historical metrics and the reporting APIs
(`GetMetricDataV2`, `GetCurrentUserData`,
`GetCurrentMetricData`).

Contact Search enables supervisors to find and view contacts handled across both
paired instances in a single view, including agent details, analytics, call recording,
and transcripts. Supervisors must sign in via the global sign-in endpoint to access
consolidated contact search.

For more information, see [Metrics, Reports and
Search across ACGR Regions](metrics-reports-and-search-across-acgr-regions.md "metrics-reports-and-search-across-acgr-regions.md").

## Event streams behavior

The following table summarizes where event streams are available when global routing
is enabled.

| Stream type                 | Behavior                                                                                                                                                                              |
| --------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Contact Event Streams (CES) | Emitted in both Regions regardless of where the contact originates.<br>You can filter by the `originRegion` and<br>`activeRegion` fields in the<br>`globalResiliencyMetadata` object. |
| Agent Event Streams (AES)   | Emitted only in the Region where the agent is active. The<br>alternate Region receives only Login and Offline events.                                                                 |
| Contact Records (CTR)       | Available in the Region where the contact originates. For example, a<br>contact that originates in us-east-1 and is answered by an agent in<br>us-west-2 has its CTR in us-east-1.    |

Since AES and CTR remain regional, update your third-party integration pipelines to
consume data from both Regions. While CES provides a consolidated view, we recommend
building integration pipelines in both Regions for resiliency.

## Temporarily disabling cross-region routing

Use the [UpdateCrossRegionRouting](../APIReference/API_UpdateCrossRegionRouting.md "../APIReference/API_UpdateCrossRegionRouting.md") API to temporarily disable or re-enable global
routing. When global routing is disabled, contacts originating in one Region are no
longer routed to agents in the other Region. Contacts that are currently connected to an
agent in another Region will not be disconnected when the API is invoked; the agent can
complete handling that contact, but will no longer be routed additional contacts from
the other Region.

###### Important

This API only stops cross-region routing. Consolidated reporting, contact search,
and resource replication continue to operate globally after you execute the
API.

## Additional considerations for custom integrations (StreamsJS, AWS SDK, Connect SDK for Agent Workspace)

While StreamsJS and Connect SDK for Agent Workspace have been updated to support
cross-region routing, applications that invoke public APIs in the AWS SDK may need to be
updated to fetch the contact's active Region and the agent's active Region, and direct
API calls accordingly:

- Mutation operations on a contact (such as
  `UpdateContactAttributes` or `TransferContact`) must
  be performed against the contact's origin Region.
- Mutation operations on an agent (such as `PutUserStatus`) must be
  performed against the Region where the agent is active.
- Read operations (such as `DescribeContact`) can be performed
  against either Region.

The following table outlines some common use cases for reference.

| Example use case                                                                                                                                                                                        | Notes                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| Third-party application in Agent Workspace that consumes only native<br>Connect Customer SDK events and requests such as `getARN()`,<br>`listQuickConnects()`, `accept()`,<br>`cleared()`               | The application will not require updates for cross-region invocation.<br>The Connect Customer SDK for Agent Workspace has been updated to support<br>cross-region invocation in the backend.                                                                                                                                                                                                                                               |
| Custom CCP that calls only StreamsJS APIs such as<br>`contact.accept()`, `agent.mute()`                                                                                                                 | The application will not require updates for cross-region invocation.<br>StreamsJS has been updated to support cross-region invocation in the<br>backend.                                                                                                                                                                                                                                                                                  |
| Application that calls `SearchUsers` (AWS SDK) to display a<br>list of all agents who belong to a particular Routing Profile                                                                            | The application will not require updates for cross-region invocation.<br>Because the User resource is replicated across both Regions (see [What resources are mirrored in the<br>replica instance](create-replica-connect-instance.md#mirrored-resources "create-replica-connect-instance.md#mirrored-resources")), invoking `SearchUsers` in either<br>of the ACGR instances returns identical results.                                   |
| Application that calls `GetCurrentMetricData` (AWS SDK) to<br>display queue metrics such as contacts in queue                                                                                           | The application will not require any updates for cross-region<br>invocation. The `GetCurrentMetricData`,<br>`GetMetricDataV2`, and `GetCurrentUserData`<br>APIs return the same global view regardless of which Region you are<br>invoking the API from. For more detail, see [Metrics,<br>Reports and Search across ACGR Regions](metrics-reports-and-search-across-acgr-regions.md "metrics-reports-and-search-across-acgr-regions.md"). |
| Application that calls the `DescribeContact` API, for<br>example to display contact attributes to the agent working on the<br>contact via a third-party application in Agent Workspace or custom<br>CCP | The application will not require any updates for cross-region<br>invocation. With consolidated contact search, the<br>`DescribeContact` API returns the same API response<br>regardless of which Region you are calling it from. For more detail, see<br>[Metrics, Reports and Search across ACGR Regions](metrics-reports-and-search-across-acgr-regions.md "metrics-reports-and-search-across-acgr-regions.md").                         |
| Application that calls the `UpdateContactAttributes` API<br>(AWS SDK), for example to store a disposition code as a contact<br>attribute                                                                | You will need to update your application to check the contact's Region<br>and make the API call to the appropriate Region. Contact mutation<br>operations such as `UpdateContactAttributes` and<br>`TransferContact` are available only in the contact's<br>Region.                                                                                                                                                                        |
| Custom analytics dashboard where supervisors can monitor contacts via<br>the `MonitorContact` API and change an agent's status via the<br>`PutUserStatus` API                                           | You will need to update your application to check the contact's Region<br>and the agent's Region, and make each API call to the appropriate Region.<br>Contact APIs such as `MonitorContact` and<br>`AssociateContactWithUser` are available in the contact's<br>Region, while agent APIs such as `PutUserStatus` are available<br>only in the agent's Region.                                                                             |

The contact's active Region and the agent's active Region can be identified in the
following interfaces.

| Interface                 | Contact's active Region                                                                                                                                                                                                    | Agent's active Region                                                                                                                                                                                                    |
| ------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| Connect SDK for Workspace | To get the contact's Region, use<br>`ContactClient.getContactRegion(contactId)`.                                                                                                                                           | To get the agent's Region, use<br>`UserClient.getUserRegion()`.                                                                                                                                                          |
| StreamsJS                 | Use the `connect._getContactRegion` internal<br>helper.                                                                                                                                                                    | The agent's Region can be fetched from the ARN of any resource in the<br>agent snapshot, using the `connect._parseRegionFromArn`<br>internal helper.                                                                     |
| Agent Event Stream        | The contact Region is identified in the<br>`GlobalResiliencyMetadata` object. For more detail, see<br>[Agent event streams<br>data model](agent-event-stream-model.md "agent-event-stream-model.md").                      | The agent's active Region is identified in the<br>`AgentCrossRegionRoutingConfiguration` object. For more<br>detail, see [Agent event<br>streams data model](agent-event-stream-model.md "agent-event-stream-model.md"). |
| Contact Event Stream      | The contact's Region is indicated in the<br>`GlobalResiliencyMetadata` object. For more detail, see<br>[Connect contact events<br>(CES)](contact-events.md "contact-events.md").                                           | The agent Region is indicated via `ActiveRegion` on the<br>`AgentInfo` object. For more detail, see [Connect contact events (CES)](contact-events.md "contact-events.md").                                               |
| DescribeContact API call  | The contact's Region is indicated in the<br>`GlobalResiliencyMetadata` object. For more detail, see<br>[DescribeContact](../APIReference/API_DescribeContact.md "../APIReference/API_DescribeContact.md") response syntax. | The agent Region is indicated via `ActiveRegion` on the<br>`AgentInfo` object. For more detail, see [DescribeContact](../APIReference/API_DescribeContact.md "../APIReference/API_DescribeContact.md") response syntax.  |
| Contact Trace Record      | The contact's Region is indicated in the<br>`GlobalResiliencyMetadata` object. For more detail, see<br>[Data model for contact<br>records](ctr-data-model.md "ctr-data-model.md").                                         | The agent Region is indicated via `ActiveRegion` on the<br>`Agent` object. For more detail, see [Data model for contact records](ctr-data-model.md "ctr-data-model.md").                                                 |

###### Important

If you have third-party applications in Agent Workspace, please note that you must
associate third-party applications with both your primary and replica instances.
Third-party applications are not automatically replicated across ACGR instances. If
you perform cross-region app invocation, add the application URL as an approved
origin in both instances.

## Supported features for cross-region routing

For a consistent agent experience across same-region and cross-region contacts, please
ensure all relevant resources are replicated across both instances. For a list of which
resources are currently mirrored automatically in Connect Customer Global Resiliency, see [What resources are mirrored in the replica
instance](create-replica-connect-instance.md#mirrored-resources "create-replica-connect-instance.md#mirrored-resources").

Connect Customer features that are currently supported for cross-region operation include the
following.

| Feature                                                                                           | Notes                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| ------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Voice calls                                                                                       | Voice calls can be routed cross-region. However, please note that<br>in-app, web, video calling, and screen sharing capabilities are not<br>supported for cross-region routing at this time.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| Customer-first callbacks; queued callbacks                                                        | Both queued callbacks and customer-first callbacks (where the dialed<br>leg has been accepted by the customer and queued) can be routed<br>cross-region to an agent in the alternate Region.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| Chats                                                                                             | Chats can be routed cross-region. Chat quick responses are not<br>natively replicated across Regions. You must replicate these yourself<br>for a consistent agent experience across Regions. Chat quick responses<br>are fetched from the contact's Region.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| Tasks                                                                                             | Tasks can be routed cross-region. Task templates are not natively<br>replicated. You must replicate these yourself for a consistent agent<br>experience across Regions. When an agent is not on any contacts, task<br>templates are fetched from the agent's active Region. When the agent is<br>handling a task, task templates are fetched from the contact's<br>Region.                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| Emails                                                                                            | Emails can be routed cross-region. However, email-specific<br>configuration such as email message templates are not natively<br>replicated. You must replicate these yourself for a consistent agent<br>experience across Regions.<br>For email-heavy workloads, consider keeping email agents in a<br>single Region to avoid limitations with email capabilities. You can<br>use traffic distribution groups to manage email agents differently from voice-only agents.<br>For example:<br>• Assign all email agents (including any blended agents) to a<br>traffic distribution group with 100% agent distribution to a single Region.<br>• Assign voice-only agents to a separate traffic distribution group with traffic<br>split across both Regions.<br>• Route all email traffic to the primary Region. |
| Enhanced multi-party call monitoring and barge                                                    | Supervisors can monitor or barge cross-region voice calls via enhanced<br>multi-party call monitoring using out-of-the-box dashboards. To monitor<br>cross-region contacts via API, ensure that you invoke the<br>`MonitorContact` API from the contact's Region. Please<br>note that three-party call monitoring is not supported for cross-region<br>monitoring.                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| Enhanced contact monitoring for chat contacts                                                     | Supervisors can monitor cross-region chat contacts.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| Routing to a specific agent via agent queue, preferred agent routing,<br>or Interrupt agent block | Just like contacts in standard queues (including contacts with routing<br>criteria set, such as a preferred agent), contacts in an agent queue can<br>be offered to the specified agent even if that agent is active in the<br>alternate Region. The Interrupt agent flow block will also offer the<br>contact to the agent regardless of Region. However, the Transfer to agent<br>(beta) flow block does not support cross-region routing; instead, use the<br>Set working queue block to specify the agent queue followed by the<br>Transfer to queue block.                                                                                                                                                                                                                                                |
| Call recordings                                                                                   | Contact recordings are generated for both same-region and<br>cross-region calls. Call recordings are stored in the contact's origin<br>Region. Recordings can be accessed from contact search and the contact<br>detail page from either Region via consolidated contact search.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| Live media streaming                                                                              | Connect Customer streams Kinesis Video Streams (KVS) audio in the contact's<br>origin Region. If a contact originates in us-east-1 and is answered by an<br>agent in us-west-2, the KVS audio is available in us-east-1. If you use<br>KVS for features like voicemail capture or third-party call analytics,<br>build integration pipelines in both Regions since contacts can originate<br>in either Region.                                                                                                                                                                                                                                                                                                                                                                                                 |
| Screen recordings                                                                                 | Screen recordings are currently generated for same-region contacts but<br>not cross-region contacts. Screen recordings can be accessed from contact<br>search and the contact detail page from either Region via consolidated<br>contact search.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| Salesforce CTI Adapter                                                                            | Global routing is supported for Salesforce CTI Adapter v5.33 and<br>Salesforce lambda package v5.27.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |

## Migrating to global routing

ACGR instances created before September 1, 2026 do not have access to global routing
by default. To request access to this feature, contact your AWS account team. Once
your instance is enabled for global routing, review the following steps:

1. Update any integrations that consume the Connect Customer instance alias in the replica
   Region, including your custom CCP, to use the new subdomain-based instance
   alias.
2. Update your firewall rules to allow the new subdomain-based instance alias if
   your rules do not use wildcards.
3. Identify changes needed for third-party integrations such as custom
   reporting, Workforce Management solutions, or systems that rely on event streams
   and contact records.
4. Identify changes needed for third-party integrations that consume the Connect Customer
   instance URL. Ensure to update the integration to consume the new subdomain
   alias.
5. Update Streams JS to include `secondaryCCPUrl` and
   `enableGlobalResiliency` parameters in your custom agent
   desktop.
6. Once ready, call the [ReplicateInstance](../APIReference/API_ReplicateInstance.md "../APIReference/API_ReplicateInstance.md") API from the source Region. This enables global
   routing, consolidated analytics, consolidated contact search, and corresponding
   changes to event streams and contact records.
7. Monitor replication status using the [DescribeInstance](../APIReference/API_DescribeInstance.md "../APIReference/API_DescribeInstance.md") API. Wait until the status reflects
   `INSTANCE_REPLICATION_COMPLETE`.
8. Validate by signing agents into the replica Region and verifying that
   cross-region routing works as expected.

###### Note

If agents were already signed in when you enabled global routing, they must sign
out and sign back in for cross-region routing to take effect. Otherwise, they will
not be able to see and accept cross-region contacts in the CCP. For that reason, we
recommend waiting past the default agent session timeout period for Connect Customer (12 hours)
before you start distributing contacts and agents across different Regions.

If you are using a custom CCP built with [Amazon Connect
Streams](https://github.com/amazon-connect/amazon-connect-streams "https://github.com/amazon-connect/amazon-connect-streams"), then you may want to maintain failover logic in your custom CCP
during the migration by defining variables for both the previous replica domain and the
new subdomain-based domain. Then, use conditional logic to fall back to the previous
domain if the new domain is unreachable during the transition period.
