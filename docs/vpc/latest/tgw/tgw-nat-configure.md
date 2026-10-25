

# Configure 1:1 NAT in AWS Transit Gateway
<a name="tgw-nat-configure"></a>

You manage NAT for an attachment through a single operation that sets the NAT options and the full rule set together. Every parameter except the attachment ID is optional, so you can update options without changing rules, or replace rules without changing options. Changes are applied asynchronously, and the attachment stays in the `available` state throughout.

Before you begin, review the [Prerequisites](tgw-nat-how-it-works.md#tgw-nat-prerequisites).

## Configure 1:1 NAT using the console
<a name="tgw-nat-configure-console"></a>

**To enable NAT and add rules**

1. Open the Amazon VPC console at [https://console.aws.amazon.com/vpc/](https://console.aws.amazon.com/vpc/).

1. In the navigation pane, choose **Transit gateway attachments**.

1. Select the attachment on which you want to enable NAT.

1. On the attachment's **1:1 NAT** tab, choose **Manage 1:1 NAT**. Alternatively, choose **Actions**, then **Manage 1:1 NAT**.

1. Under **NAT Gateway support**, select **Enable NAT Gateway support**.

1. (Optional) Under **NAT system route support**, choose whether the transit gateway automatically installs routes for this attachment's NAT CIDRs in the route tables that the attachment propagates to.
   + **Direct Connect gateway and BGP Site-to-Site VPN attachments:** You can turn this setting on or off; it's on by default. When it's on, the transit gateway adds a system route for each NAT CIDR, and the routes your network advertises aren't changed. When it's off, you must advertise the NAT CIDRs from your network or add static routes.
   + **VPC attachments:** This setting is always on. When a rule's match source CIDR exactly equals one of the VPC's CIDRs, the propagated route for that CIDR is replaced by a route for the rule's NAT CIDR. For rules that don't exactly match a VPC CIDR, add a static route for the NAT CIDR that targets the VPC attachment.
   + **Connect, VPN Concentrator, static peering, and static-routed Site-to-Site VPN attachments:** This setting is always off. Make the NAT CIDRs reachable with static routes, or by advertising them from your network.

1. Under **NAT rules**, choose **Add rule** and provide the following for each rule.
   + **Rule number** – A unique integer from 1 to 32766.
   + **Match source CIDR** – The source IPv4 CIDR of traffic arriving on this attachment, for example 10.100.10.0/24. It can't overlap multicast (224.0.0.0/4) or link-local (169.254.0.0/16) ranges.
   + **NAT CIDR** – The IPv4 CIDR to which source addresses are translated, for example 100.64.10.0/24. It must be an RFC 1918 or CGNAT (RFC 6598) CIDR with the same prefix length as the match source CIDR.

   No CIDR in a rule can overlap any other CIDR (match source or NAT) on the same attachment.

1. Choose **Add rule** again to add more rules. You can configure up to 50 rules per attachment.

1. Choose **Save changes**.

**Important**  
On a VPC attachment, enabling NAT replaces the propagated route for each VPC CIDR that a rule matches with a route to its NAT CIDR. Other attachments that reach the VPC by its real addresses lose connectivity. Update those peers to use the NAT addresses before you save.

Changes are applied asynchronously, and the attachment stays in the **Available** state. To confirm that NAT is active, select the attachment, choose the **1:1 NAT** tab, and check that **NAT Gateway support** shows **Enabled** and every rule shows **Activated**.

**Important**  
When you save, the rules on the form replace all existing rules on the attachment. Any rule you remove from the form is deleted.

**To modify NAT rules**

1. Open the Amazon VPC console at [https://console.aws.amazon.com/vpc/](https://console.aws.amazon.com/vpc/).

1. In the navigation pane, choose **Transit gateway attachments**.

1. Select the attachment.

1. Choose **Actions**, and then choose **Manage 1:1 NAT**.

1. Add, edit, or remove rules.

1. Choose **Save changes**.

**Important**  
Rules you removed may show **Deleting** until they're removed. You can't save changes while **NAT Gateway support** is **Enabling** or **Disabling**. NAT can't be enabled with zero rules, so to remove every rule, also set **NAT Gateway support** to **Disable** in the same save.

**To view NAT configuration**

1. Open the Amazon VPC console at [https://console.aws.amazon.com/vpc/](https://console.aws.amazon.com/vpc/).

1. In the navigation pane, choose **Transit gateway attachments**.

1. Select the attachment.

1. Choose the **1:1 NAT** tab to view the **NAT Gateway Support** and **NAT System Route Support** settings, and all configured rules.

**Note**  
Only the transit gateway owner can view an attachment's NAT configuration.

**To disable NAT**

1. Open the Amazon VPC console at [https://console.aws.amazon.com/vpc/](https://console.aws.amazon.com/vpc/).

1. In the navigation pane, choose **Transit gateway attachments**.

1. Select the attachment.

1. Choose **Actions**, and then choose **Manage 1:1 NAT**.

1. Under **NAT Gateway support**, clear the **Enable NAT Gateway support** check box.

1. Choose **Save changes**.

**Note**  
When you disable NAT, the transit gateway stops translating traffic on the attachment, and peers that use the NAT addresses lose connectivity. Your rules aren't deleted: they change to **Deactivated** and are reactivated if you enable NAT on the attachment again.

## Configure 1:1 NAT using the AWS CLI
<a name="tgw-nat-configure-cli"></a>

You manage the NAT configuration for a transit gateway attachment with a single command, [modify-transit-gateway-attachment-nat-configuration](https://docs.aws.amazon.com/cli/latest/reference/ec2/modify-transit-gateway-attachment-nat-configuration.html). It sets the NAT options and the full rule set in one operation. Every parameter except `--transit-gateway-attachment-id` is optional, so you can update options without changing rules, or replace rules without changing options.

Changes are applied asynchronously. After each change, run [get-transit-gateway-attachment-nat-configuration](https://docs.aws.amazon.com/cli/latest/reference/ec2/get-transit-gateway-attachment-nat-configuration.html) until:
+ `NatGatewaySupport` is `enabled` or `disabled`,
+ every rule is `activated` or `deactivated`, and
+ rules that you removed, which may show the state `deleting`, no longer appear.

You can't modify the configuration while `NatGatewaySupport` is `enabling` or `disabling`. The attachment stays in the `available` state during all NAT configuration operations.

### Enable NAT and configure rules
<a name="tgw-nat-configure-cli-enable"></a>

**Important**  
On a VPC attachment, enabling NAT replaces the propagated route for each VPC CIDR that a rule matches with a route to its NAT CIDR. Other attachments that reach the VPC by its real addresses lose connectivity.

To enable NAT on a VPC attachment and set the initial rule set:

```
aws ec2 modify-transit-gateway-attachment-nat-configuration \
    --transit-gateway-attachment-id tgw-attach-0123456789abcdef0 \
    --nat-gateway-support enable \
    --nat-gateway-rules '[
        {"RuleNumber":100,"MatchSourceCidr":"10.100.10.0/24","NatCidr":"192.168.10.0/24"},
        {"RuleNumber":200,"MatchSourceCidr":"10.100.20.0/24","NatCidr":"100.64.20.0/24"}
    ]'
```

`--nat-gateway-support` (`enable` \| `disable`)  
Turns 1:1 NAT on or off for the attachment. When enabled, the transit gateway translates traffic that matches the attachment's rules. When disabled, translation stops and the rules are kept in the `deactivated` state. If omitted, the current setting is kept.

`--nat-system-route-support` (`enable` \| `disable`)  
Controls whether the transit gateway automatically installs routes (route type `system`) for the attachment's NAT CIDRs in the route tables the attachment propagates to.  
+ **VPC attachments (always `enable`):** When a rule's `MatchSourceCidr` exactly equals one of the VPC's CIDRs, the transit gateway replaces the propagated route for that CIDR with a route for the rule's `NatCidr`. A rule that doesn't exactly match a VPC CIDR gets no route; add a static route for its `NatCidr` that targets the VPC attachment.
+ **Direct Connect gateway and BGP Site-to-Site VPN attachments (`enable` or `disable`, default `enable`):**
  + When enabled, the transit gateway adds a system route for each rule's `NatCidr`. The routes your network advertises aren't changed or removed. The system route is active while your network advertises a route that overlaps the rule's `MatchSourceCidr`. Otherwise, its state is `blackhole` and traffic to the NAT CIDR is dropped.
  + When disabled, no system routes are added. Advertise the NAT CIDRs from your network, or add static routes.
+ **Static Site-to-Site VPN, static peering, Connect, and VPN Concentrator attachments (always `disable`):** No system routes are added. Add static routes for the NAT CIDRs, or have your peers advertise them.

### Update options without changing rules
<a name="tgw-nat-configure-cli-options"></a>

Omit `--nat-gateway-rules` to change `NatGatewaySupport` or `NatSystemRouteSupport` without changing the rule set. For example, to disable NAT:

```
aws ec2 modify-transit-gateway-attachment-nat-configuration \
    --transit-gateway-attachment-id tgw-attach-0123456789abcdef0 \
    --nat-gateway-support disable
```

When you disable NAT, traffic on the attachment is no longer translated. Your rules are kept and their state changes to `deactivated`. When you re-enable NAT, they change back to `activated`.

### Replace the full rule set
<a name="tgw-nat-configure-cli-replace"></a>

The list you supply replaces all existing rules on the attachment, so include every rule you want to keep in each call. Rules that you leave out may show the state `deleting` until they're removed.

```
aws ec2 modify-transit-gateway-attachment-nat-configuration \
    --transit-gateway-attachment-id tgw-attach-0123456789abcdef0 \
    --nat-gateway-rules '[
        {"RuleNumber":100,"MatchSourceCidr":"10.200.10.0/24","NatCidr":"100.64.10.0/24"}
    ]'
```

### Clear all rules
<a name="tgw-nat-configure-cli-clear"></a>

To remove all rules, use `--reset-nat-gateway-rules`. You can't combine it with a non-empty `--nat-gateway-rules`. NAT can't stay enabled with zero rules, so if NAT is enabled, disable it in the same call:

```
aws ec2 modify-transit-gateway-attachment-nat-configuration \
    --transit-gateway-attachment-id tgw-attach-0123456789abcdef0 \
    --nat-gateway-support disable \
    --reset-nat-gateway-rules
```

### View NAT configuration
<a name="tgw-nat-configure-cli-view"></a>

```
aws ec2 get-transit-gateway-attachment-nat-configuration \
    --transit-gateway-attachment-id tgw-attach-0123456789abcdef0
```

Example output:

```
{
    "TransitGatewayAttachmentId": "tgw-attach-0123456789abcdef0",
    "NatGatewaySupport": "enabled",
    "NatSystemRouteSupport": "enable",
    "NatGatewayRules": [
        {
            "RuleNumber": 100,
            "MatchSourceCidr": "10.100.10.0/24",
            "NatCidr": "192.168.10.0/24",
            "State": "activated"
        },
        {
            "RuleNumber": 200,
            "MatchSourceCidr": "10.100.20.0/24",
            "NatCidr": "100.64.20.0/24",
            "State": "activated"
        }
    ]
}
```

To check only whether a change has finished:

```
aws ec2 get-transit-gateway-attachment-nat-configuration \
    --transit-gateway-attachment-id tgw-attach-0123456789abcdef0 \
    --query '{Support:NatGatewaySupport,Rules:NatGatewayRules[].[RuleNumber,State]}'
```

## Configure 1:1 NAT using CloudFormation
<a name="tgw-nat-configure-cfn"></a>

Use the `AWS::EC2::TransitGatewayAttachmentNatConfiguration` resource. Each resource holds the complete NAT configuration for one attachment: the NAT Gateway support setting, the NAT system route support setting, and the full rule set. NAT configuration isn't available as properties on attachment resources such as `AWS::EC2::TransitGatewayVpcAttachment`.

The stack must be deployed in the account that owns the transit gateway.

```
Resources:
  VpcAttachmentNat:
    Type: AWS::EC2::TransitGatewayAttachmentNatConfiguration
    Properties:
      TransitGatewayAttachmentId: !Ref VpcAttachment
      NatGatewaySupport: enable
      NatGatewayRules:
        - RuleNumber: 100
          MatchSourceCidr: 10.0.0.0/16
          NatCidr: 10.1.0.0/16
```