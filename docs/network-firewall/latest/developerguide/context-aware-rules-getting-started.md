

# Getting started with context-aware rules

This topic walks you through creating your first context-aware rule in the console and deploying it to your network firewall. To configure context-aware rules with the API instead, use `CreateRuleGroup`. See [Writing context-aware rules](context-aware-rules-writing.md) for the API shapes, and [Listing context stores and their resources](#context-aware-rules-list-apis) for the APIs that list your context stores and their resources.

**Prerequisites**  
Before you begin, make sure that you have the following:
+ A transit gateway-attached network firewall. Context is carried by the transit gateway, so network firewalls deployed with VPC endpoints can't use context-aware rules. To create one, see [Creating a transit gateway-attached firewall from a shared transit gateway](create-tgw-firewall.md).
+ A context store associated with your transit gateway, with read access for Network Firewall. See [Onboarding your transit gateway to a context store](context-aware-rules-setup.md).

**To create your first context-aware rule**

1. Sign in to the AWS Management Console and open the Amazon VPC console at [https://console.aws.amazon.com/vpc/](https://console.aws.amazon.com/vpc/).

   In the navigation pane, under **Network Firewall**, choose **Network Firewall rule groups**, and then choose **Create rule group**.

1. Follow the wizard through the rule group details. On the **Choose rule group type** page, for **Rule group version**, choose **Next Generation** or **Classic**. For the wizard pages that this topic doesn't cover, see [Creating a rule group for a Next Generation policy](rule-groups-v2-creating.md) or [Creating a stateful rule group](rule-group-stateful-creating.md).

1. On the **Rule group variables** page of the wizard, in the **Context sets** section, choose **Create context set**.

   1. For **Variable name**, enter the name that your rules use to reference the set, for example `PROD_RESOURCES`. In rules, you reference it as `$PROD_RESOURCES`.

   1. For **Context store**, choose the store that's associated with your firewall's transit gateway.

   1. (Optional) For **Filter by Region**, choose the Regions whose resources you want to choose from.

   1. For **Resource type**, choose **VPC**, **Subnet**, **Security Group**, or **Transit gateway attachment**, and then for **Resource IDs**, select the resources. The console lists the IDs that the store tracks, so you choose from the resources that your firewall can resolve. To include another resource type in the same set, choose **Add resource type**.

   1. Choose **Create context set**.

1. Before you write rules, use your flow logs to learn which resources talk to each other. Flow logs record each flow's source and destination context with no rules required, so your first rules match real traffic. For the log format, see [Context in your network firewall logs](context-aware-rules-logging.md).

1. On the rules page of the wizard, reference the context IDs in the source or destination of your rules through the set you created. In the rule builder, for **Source** or **Destination**, choose **Context set** and select the set. In a Suricata compatible rule string, reference the set by name, for example `$PROD_RESOURCES`. For the rule forms and examples, see [Writing context-aware rules](context-aware-rules-writing.md).

1. Add the rule group to the firewall policy that's attached to your transit gateway-attached network firewall. For a Next Generation policy, see [Creating a Next Generation policy in AWS Network Firewall](firewall-policy-v2-creating.md); for a Classic policy, see [Updating a firewall policy in AWS Network Firewall](firewall-policy-updating.md).

1. Verify that the rule group shows as in sync for your firewall. Then check the context store sync state separately. On the firewall's details page, the **Context store sync state** section shows the store, with a **Sync state** of **Fully resolved** when every referenced resource resolves. For help, see [How do I check the context store sync state?](troubleshooting-context-aware-rules.md#troubleshoot-context-sync-state).

1. Start with rules that only log, and check your alert logs. For Classic stateful rules and IPS rules, use the `alert` action. A Next Generation firewall rule can't use `alert` as its primary action. Instead, add the `alert` keyword to an `accept:flow` rule. For the valid combinations, see [Firewall engine actions and scopes](firewall-rule-groups-verdicts.md). The alert logs show which context each rule matched. After you create or change a rule or a resource's context, allow a few minutes for matching alerts to appear. When rules match as expected, change the action to `drop` or `reject`.

To change a rule group's context sets later, open the rule group's details page, and in the **Context sets** section, choose **Edit**. The change applies to every firewall policy that references the rule group.

## Listing context stores and their resources
<a name="context-aware-rules-list-apis"></a>

Network Firewall adds 2 APIs for working with context stores:
+ `ListContextStores` returns the context stores associated with your transit gateway-attached network firewalls, with each store's ID and owner account. Use it to find the store ID and to confirm that your firewall discovered a store.
+ `ListResourcesInContextStore` returns the resource IDs that a store tracks: the context IDs that you can reference in rules. Use it to confirm that an ID is tracked before you reference it. A rule that references an untracked ID matches nothing. You can filter the listing by Region and by resource type.

```sh
aws network-firewall list-context-stores

aws network-firewall list-resources-in-context-store \
    --context-store-id context-store-021345abcdef6789a \
    --filters Region=us-east-1,ResourceType=SecurityGroup
```