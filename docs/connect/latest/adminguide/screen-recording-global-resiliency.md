

# Screen recording with Connect Customer Global Resiliency
<a name="screen-recording-global-resiliency"></a>

Agent screen recording is supported on instances that have [Set up Connect Customer Global Resiliency](setup-connect-global-resiliency.md). With Global Resiliency, your Connect Customer instance is paired with a replica instance in another AWS Region, and agents can handle contacts in either Region. Screen recording works in both Regions of the pair, including after you shift agents from one Region to the other. However, replicating an instance does not copy every screen recording setting to the replica Region — complete the steps in this topic so that recording works in both Regions.

**Topics**
+ [Set up screen recording for a Global Resiliency instance pair](#set-up-sr-global-resiliency)
+ [How screen recordings work across Regions](#sr-global-resiliency-behavior)

## Set up screen recording for a Global Resiliency instance pair
<a name="set-up-sr-global-resiliency"></a>

1. **Enable screen recording in both Regions.** The [ReplicateInstance](https://docs.aws.amazon.com/connect/latest/APIReference/API_ReplicateInstance.html) API does not copy data storage configuration to the replica instance, so the replica has no screen recording storage until you configure it. Follow the steps in [Step 1: Enable screen recording for your instance](enable-sr.md#install-sr-step1) on your source instance, and then repeat them on the replica instance in the replica Region. Each Region delivers its recordings to the Amazon S3 bucket configured in that Region. If the replica Region has no screen recording storage configured, contacts originating from that Region are not recorded.

1. **Update the Connect Customer Client Application domains allowlist.** With Global Resiliency, agents access the CCP through Region-specific sub-domains in the format `{{region}}.{{your-instance-alias}}.my.connect.aws`. Add the sub-domains for both Regions of your instance pair to the allowlist, for example `us-east-1.{{your-instance-alias}}.my.connect.aws,us-west-2.{{your-instance-alias}}.my.connect.aws`. For Windows, see [Guidelines for specifying your Connect Customer domains allowlist](amazon-connect-client-app.md#domain-allowlist-guidelines). For Chrome OS, add the same sub-domains to the `allowListedDomain` managed configuration. If the allowlist contains only your original single-Region domain, screen recording fails after agents sign in through Global Resiliency domains.

1. **Update your firewall allow list for both Regions.** The screen recording upload endpoints described in [Network requirements](sr-system-req.md#network-requirements) are Regional. Allow the upload endpoints for both Regions of your instance pair.

1. **Confirm your flows.** Flows, including the **Set recording and analytics behavior** block, are mirrored to the replica instance by [ReplicateInstance](https://docs.aws.amazon.com/connect/latest/APIReference/API_ReplicateInstance.html), and changes you make to flows after replication are continuously synchronized between the two instances in both directions. You do not need to configure screen recording separately in your replica Region flows. For more information, see [What resources are mirrored in the replica instance](create-replica-connect-instance.md#mirrored-resources).

1. **If you use Amazon EventBridge to track screen recording status**, set up your Amazon EventBridge rules and targets in both Regions of your instance pair. When the Region an agent is signed in to differs from the Region a contact originated from, the status events for that contact are split between the two Regions: events reported from the agent's workstation, including client-side failure events, are delivered in the agent's Region, while the `PUBLISHED` event is delivered in the contact's originating Region. Some events, such as `INITIATED` and `COMPLETED`, can be delivered in both Regions with different `eventDeduplicationId` values. To receive every event for every contact, create rules in both Regions, and use the contact ARN in the event detail to correlate events for the same contact across Regions. For more information, see [Use Amazon EventBridge events to track screen recording status](track-screen-recording-status.md).

## How screen recordings work across Regions
<a name="sr-global-resiliency-behavior"></a>
+ A contact's screen recording is delivered to the Amazon S3 bucket configured in the Region from which the contact originated, regardless of which Region the agent is signed in to.
+ Shifting agents to the other Region does not change where recordings are delivered. If contacts continue to originate from the first Region, their screen recordings continue to be delivered to that Region's Amazon S3 bucket, even while the agents handling them are active in the other Region.
+ Cross-Region contact search can surface a contact from either Region of your instance pair. For more information about contact search across Regions, see [Contact search and contact details](contact-search-and-contact-details.md).
+ The Connect Customer Client Application on the agent workstation works in both Regions; no reinstallation is required when agents change Regions, provided both Regions' domains are in the allowlist.