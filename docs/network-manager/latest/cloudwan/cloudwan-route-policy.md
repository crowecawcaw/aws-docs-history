# Create an AWS Cloud WAN route policy and rule

A routing policy is a set of rules that gives you precise control over route propagations in your core network allowing you better routes management, optimized performance and greater security. A routing policy rule consists of a match condition and an action used to control route propagations. The match condition determines which route propagations the rule applies to, while the action specifies how to process the route propagations in the core network. This granular control enables you to implement complex routing scenarios, such as blocking specific routes, adding BGP community tags, modifying AS paths, or setting route preferences to influence path selection across your network infrastructure. You can associate these routing policies to a) routes propagated on Cloud WAN attachments b) routes propagated across segments or c) routes propagated across core network edges (CNE) or regions (CNE-to-CNE).

## Create a routing policy

Provide policy details to control traffic flow and optimize your network routing. Before you can create a routing policy you must first have completed the following:

- Set up the Network configuration. See [Configure the core network settings](cloudwan-core-network-config.md "cloudwan-core-network-config.md").
- Defined one or more segments. See [Add a segment](cloudwan-policy-segments.md "cloudwan-policy-segments.md")

###### To create a routing policy

1. Access the Network Manager console at [https://console.aws.amazon.com/networkmanager/home/](https://console.aws.amazon.com/networkmanager/home "https://console.aws.amazon.com/networkmanager/home").
2. Under **Connectivity** choose **Cloud WAN**.
3. On the **Global networks** page, choose the global network ID that for the core network you want to create a policy version for, and then choose **Core network**.
4. In the navigation pane, choose **Policy versions**.
5. Choose **Create policy version**.
6. In **Choose policy view mode**, choose **Visual
   editor**.
7. Choose **Routing policies**.
8. Choose **Create**.
9. For **Routing policy number**, enter a priority number. Lower
   numbers take priority over higher numbers when processing the policy.
10. (Optional) Add a **Description** identifying this policy.
    The description can be no longer than 256 characters, using a-z, A-Z, 0-9, and
    hyphens (-). White spaces are not allowed.
11. For the **Routing policy direction** choose one of the
    following:
    - **Inbound** - An inbound routing policy contains rules that control routes propagated inbound on an attachment (e.g. from an external network to Cloud WAN) into the CNE
    - **Outbound** - An outbound policy contains rules that control routes advertised from a CNE outbound over an attachment (e.g. from Cloud WAN to an external network).

12. Choose **Create routing policy**.

Once you've created one or more route policies, you can create route rules to further control route propagation.

## Create a routing policy rule

A routing policy rule consists of a match condition and an action used to control route propagations.

###### To create a routing policy rule

1. Open the at [https://console.aws.amazon.com/networkmanager/](https://console.aws.amazon.com/networkmanager/ "https://console.aws.amazon.com/networkmanager/").
2. In the navigation pane, choose **Cloud WAN**.
3. Choose the global network ID.
4. In the navigation pane, choose **Routing policies**.
5. Choose the routing policy where you want to add a rule.
6. Choose **Create rule**.
7. For **Routing policy rule number**, enter a priority number.
   Lower numbers take priority over higher numbers when processing the
   policy.
8. Set the **Action** for the rule. Available actions
   include:
   - **Drop** - Block specified routes
   - **Allow** - Permit only specified routes
   - **Prepend ASN list** - Add ASNs to make this path
     less preferred
   - **Remove ASN list** - Remove ASNs to make this path
     more preferred
   - **Replace ASN list** - Replace AS-PATH with a new ASN
     list
   - **Add community** - Add a BGP community to
     routes
   - **Remove community** - Remove a BGP community
     from routes
   - **Summarize** - Advertise a summary route
   - **Set local preference** - Set priority for route
     selection (higher value = more preferred path)

9. If adding multiple conditions, choose the logical operator:
   - **AND** - All conditions must be met for the rule to
     apply
   - **OR** - Any condition can be met for the rule to
     apply

10. Configure the match conditions for the rule. You can add multiple conditions and specify whether they should be evaluated with AND or OR logic:
    - **Prefix equals** - Matches routes with an exact
      network prefix specification.
    - **Prefix in CIDR** - Match propagated routes that fall within a specified CIDR range.
    - **Prefix in prefix list** - Matches routes whose
      prefixes are contained in a predefined prefix list.
    - **ASN in as path** - Matches routes that contain a
      specific Autonomous System Number in their AS path.
    - **Community in list** - Matches routes that have BGP
      community attributes present in a specified community list.
    - **MED equals** - Matches routes with a Multi-Exit
      Discriminator (MED) value equal to the specified number.

11. Choose **Add rule**.
