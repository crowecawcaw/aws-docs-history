

# Troubleshooting context-aware rules in AWS Network Firewall

Use the information here to help you diagnose common issues with context-aware rules. For how context-aware rules work, see [Context-aware rules in AWS Network Firewall](context-aware-rules.md).

Context resolution failures cause context rules to match nothing. They never cause rules to match traffic that they otherwise wouldn't. For example, if a rule that allows traffic references a context ID that can't be resolved, the rule stops matching, and the rest of your policy evaluates that traffic. The failure never widens what your policy permits.

## How do I check the context store sync state?
<a name="troubleshoot-context-sync-state"></a>

The `ContextStoreSyncState` field, in the `FirewallStatus` object of the `DescribeFirewall` response, reports how the network firewall resolved the context store. In the console, the firewall's details page shows the same information in the **Context store sync state** section:
+ `SYNCING` – The firewall is synchronizing with the context store. This state is temporary after discovery.
+ `FULLY_RESOLVED` – Every resource ID that your context sets reference resolves against the store. This is the normal, healthy state.
+ `PARTIALLY_RESOLVED` – Some referenced resource IDs could not be resolved. The status message counts them, for example, "2 of 9 referenced resources could not be resolved." Rules that reference the unresolved IDs match nothing. All other rules work normally.
+ `UNRESOLVED` – None of the referenced resource IDs resolve against the store. The status message asks you to verify that the resources exist in the store. Every context rule on the firewall matches nothing.
+ `SYNC_FAILED` – The firewall can't read the context store. Every context rule on the firewall matches nothing.

A healthy firewall might not show a sync state. To confirm that the firewall discovered its context store, check the `ContextStoreId` field in the `Firewall` object instead.

## My context store sync state is SYNC\_FAILED
<a name="troubleshoot-context-sync-failed"></a>

The firewall can't read the context store, so its context rules match no traffic. The policy's other rule groups work normally. Verify that the `NetworkFirewallContextStoreReadOnly` role exists in the store owner account with the exact name, trust policy, and permissions shown in [Onboarding your transit gateway to a context store](context-aware-rules-setup.md).

## My rule references a context ID that isn't in the context store
<a name="troubleshoot-context-unknown-id"></a>

The firewall can't resolve an ID that the store doesn't recognize, so the rule that references it matches no traffic on that firewall. The firewall's context store sync state shows `PARTIALLY_RESOLVED`, with a message that counts the unresolved references, for example, "2 of 9 referenced resources could not be resolved." The rule group's own sync status stays in sync. To find unresolved IDs, check the firewall's context store sync state, not the rule group status. Other rules in the same rule group work normally. The context store tracks an Amazon VPC security group only after you attach it to a network interface whose traffic passes through the transit gateway. A new, unattached Amazon VPC security group doesn't resolve yet.

## A resource ID doesn't appear in `ListResourcesInContextStore` or in the console drop-down
<a name="troubleshoot-context-resource-not-listed"></a>

The context store tracks only the resources behind a transit gateway that is associated with it. Check that the association for that transit gateway shows **Associated** in the AWS Network Manager console, and that the resource is attached to that transit gateway. A VPC is attached through its transit gateway attachment. An Amazon VPC security group is tracked only after you attach it to a network interface whose traffic passes through the transit gateway. For the association steps, see [Onboarding your transit gateway to a context store](context-aware-rules-setup.md).

## My rules that match on security groups don't fire
<a name="troubleshoot-context-security-groups"></a>

Traffic carries up to 5 Amazon VPC security groups for the sending network interface. Matching on resources with more than 5 Amazon VPC security groups is not supported. If an interface belongs to more than 5 Amazon VPC security groups, which requires a raised Amazon VPC quota for security groups per network interface, match that traffic by VPC, subnet, or attachment instead. Rules that match by VPC, subnet, or attachment are unaffected by the Amazon VPC security group count.

## My destination context rule is rejected on a non-TCP protocol
<a name="troubleshoot-context-destination-protocol"></a>

Rules with a context ID in the destination position require `tcp` or a TCP-based application protocol. The firewall rejects other protocols with a validation error when you create or update the rule group. Change the protocol, or move the context match to the source position. See [Matching on destination context](context-aware-rules-destination.md).

## I don't see context fields in my logs
<a name="troubleshoot-context-no-log-fields"></a>

Only traffic that passes through a transit gateway-attached network firewall carries resource identity. Log entries for traffic from other paths have no `context` object. Also, alert log entries include context fields only for the context IDs the rule matched. An alert from an IP-based rule has no context fields, even for transit gateway traffic. Flow log entries carry resource identity regardless of which rules matched.