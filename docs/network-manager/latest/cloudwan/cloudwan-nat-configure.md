

# Configure 1:1 NAT in AWS Cloud WAN
<a name="cloudwan-nat-configure"></a>

You manage NAT for an attachment through a single operation that sets the NAT options and the full rule set together. Every parameter except the attachment ID is optional. Changes are applied asynchronously: the attachment transitions to **Updating** while the workflow runs and returns to **Available** on completion. The operation is complete when the attachment is back to **Available**.

**Important**  
Currently, only the core network owner can configure NAT on Cloud WAN attachments. Shared attachment owners can't configure NAT.
On a VPC attachment, enabling NAT replaces the route for each VPC CIDR that a rule exactly matches with a route to its NAT CIDR. Other attachments that reach the VPC by its real addresses lose connectivity. Update those networks to use the NAT addresses before you enable NAT.
1:1 NAT is a paid feature. Enabling NAT on an attachment adds an hourly charge and a data processing charge. For more information, see [Cloud WAN pricing](what-is-cloudwan.md#cloudwan-available-pricing).

## Configure 1:1 NAT using the console
<a name="cloudwan-nat-configure-console"></a>

The **NAT system route support** setting controls whether Cloud WAN automatically installs routes for an attachment's NAT CIDRs in the attachment's segment. It works as follows for each attachment type:
+ **Direct Connect gateway and BGP Site-to-Site VPN attachments** – You can turn this setting on or off; it's on by default. When it's on, Cloud WAN adds a system route for each NAT CIDR, and the routes your network advertises aren't changed. When it's off, you must advertise the NAT CIDRs from your network or add static routes in your core network policy.
+ **VPC attachments** – This setting is always on. When a rule's match source CIDR exactly equals one of the VPC's CIDRs, the VPC CIDR's route is replaced by a route for the rule's NAT CIDR. For rules that don't exactly match a VPC CIDR, add a static route for the NAT CIDR in your core network policy.
+ **Connect attachments** – This setting is always off. Your peers must advertise the NAT CIDRs.

Each NAT rule has the following fields:
+ **Rule number** – A unique integer from 1 to 32766.
+ **Match source CIDR** – The source IPv4 CIDR of traffic arriving on this attachment, for example `10.100.10.0/24`. It can't overlap multicast (`224.0.0.0/4`) or link-local (`169.254.0.0/16`) ranges.
+ **NAT CIDR** – The IPv4 CIDR that source addresses are translated to, for example `100.64.10.0/24`. It must be within RFC 1918 or CGNAT (RFC 6598) space, with the same prefix length as the match source CIDR.

No CIDR in a rule can overlap any other CIDR (match source or NAT) on the same attachment. You can add up to 50 rules per attachment.

**To configure NAT during attachment creation**

1. Access the Network Manager console at [https://console.aws.amazon.com/networkmanager/home/](https://console.aws.amazon.com/networkmanager/home).

1. Under **Connectivity**, choose **Global networks**.

1. On the **Global networks** page, choose the global network ID.

1. Under **Core network** in the navigation pane, choose **Attachments**.

1. Choose **Create attachment**.

1. Under **1:1 NAT Gateway settings**, for **NAT Gateway support**, select **Enable NAT Gateway support**.

1. (Optional) For **NAT system route support**, choose whether Cloud WAN automatically installs routes for this attachment's NAT CIDRs in the attachment's segment.

1. Under **1:1 NAT Gateway rules**, choose **Add rule**, and then enter the **Rule number**, **Match source CIDR**, and **NAT CIDR**.

1. To add more rules, choose **Add rule** again.

1. Complete the remaining attachment settings, then choose **Create attachment**.

**To enable NAT and add rules**

1. Access the Network Manager console at [https://console.aws.amazon.com/networkmanager/home/](https://console.aws.amazon.com/networkmanager/home).

1. Under **Connectivity**, choose **Global networks**.

1. On the **Global networks** page, choose the global network ID.

1. Under **Core network** in the navigation pane, choose **Attachments**.

1. Select the attachment on which you want to enable NAT.

1. Choose **Actions**, and then choose **Manage 1:1 NAT**.

1. Under **NAT Gateway support**, select **Enable NAT Gateway support**.

1. (Optional) Under **NAT system route support**, choose whether Cloud WAN automatically installs routes for this attachment's NAT CIDRs in the attachment's segment.

1. Under **1:1 NAT Gateway rules**, choose **Add rule**, and then enter the **Rule number**, **Match source CIDR**, and **NAT CIDR**.

1. To add more rules, choose **Add rule** again.

1. Choose **Save changes**.

While the configuration is applied, the attachment is in the **Updating** state. It returns to **Available** when the change is complete. For attachments that span multiple Regions, such as Direct Connect gateway attachments, the rules apply in every Region where the attachment is present.

If the attachment is pending acceptance, the configuration is applied after the attachment is accepted. Until then, **NAT Gateway support** and the rules show **Pending attachment acceptance**. For more information, see [Attachment states](cloudwan-nat-how-it-works.md#cloudwan-nat-attachment-states).

When you modify NAT rules, the rules on the form replace all existing rules on the attachment when you save. Any rule you remove from the form is deleted.

**To modify NAT rules**

1. Access the Network Manager console at [https://console.aws.amazon.com/networkmanager/home/](https://console.aws.amazon.com/networkmanager/home).

1. Under **Connectivity**, choose **Global networks**.

1. On the **Global networks** page, choose the global network ID.

1. Under **Core network** in the navigation pane, choose **Attachments**.

1. Select the attachment, and then choose **Actions**, **Manage 1:1 NAT**.

1. Add, edit, or remove rules.

1. Choose **Save changes**.

You can't save changes while the attachment is **Updating**. NAT can't be enabled with zero rules, so to remove every rule, also turn off **NAT Gateway support** in the same save.

**To view NAT configuration for an attachment**

1. Access the Network Manager console at [https://console.aws.amazon.com/networkmanager/home/](https://console.aws.amazon.com/networkmanager/home).

1. Under **Connectivity**, choose **Global networks**.

1. On the **Global networks** page, choose the global network ID.

1. Under **Core network** in the navigation pane, choose **Attachments**.

1. Choose the name of the attachment you want to inspect.

1. Choose the **1:1 NAT** tab to view the `natGatewaySupport`, the `natSystemRouteSupport` setting, and all configured rules.

**To disable NAT**

1. Access the Network Manager console at [https://console.aws.amazon.com/networkmanager/home/](https://console.aws.amazon.com/networkmanager/home).

1. Under **Connectivity**, choose **Global networks**.

1. On the **Global networks** page, choose the global network ID.

1. Under **Core network** in the navigation pane, choose **Attachments**.

1. Select the attachment.

1. Choose **Actions**, and then choose **Manage 1:1 NAT**.

1. Under **NAT Gateway support**, clear **Enable NAT Gateway support**.

1. Choose **Save changes**.

The attachment transitions to **Updating** while the change is applied and returns to **Available** on completion.

## Configure 1:1 NAT using the AWS CLI
<a name="cloudwan-nat-configure-cli"></a>

You manage the NAT configuration for a core network attachment with a single command, **update-attachment-nat-configuration**. With this command, you set the NAT options and the full rule set in one operation. Every parameter except `--attachment-id` is optional, so you can update options without changing rules, or replace rules without changing options.

Changes are applied asynchronously. While a change is in progress, the attachment is in the `UPDATING` state; traffic keeps flowing, but you can't make further NAT changes. When the attachment returns to `AVAILABLE`, the change is complete. For attachments that span multiple Regions, such as Direct Connect gateway attachments, the NAT rules apply in every Region where the attachment is present.

In the following examples, replace the attachment ID, core network ID, and CIDRs with your own values.

### Enable NAT and configure rules
<a name="cloudwan-nat-cli-enable"></a>

The following command enables NAT on an attachment and configures two rules:

```
aws networkmanager update-attachment-nat-configuration \
    --attachment-id {{attachment-0123456789abcdef0}} \
    --nat-gateway-support ENABLE \
    --nat-gateway-rules '[
        {"RuleNumber":100,"MatchSourceCidr":"{{10.100.10.0/24}}","NatCidr":"{{192.168.10.0/24}}"},
        {"RuleNumber":200,"MatchSourceCidr":"{{10.100.20.0/24}}","NatCidr":"{{100.64.20.0/24}}"}
    ]'
```

Each rule needs a unique rule number from 1 to 32766. You can specify up to 50 rules.

`--nat-gateway-support` (`ENABLE` \| `DISABLE`): Turns 1:1 NAT on or off for the attachment. When enabled, Cloud WAN translates traffic that matches the attachment's rules. NAT can't be enabled with zero rules, so you must include rules in the request, or rules must already be configured. When disabled, translation stops, and Cloud WAN keeps the rules in the deactivated state. If you omit this parameter, Cloud WAN keeps the current setting.

`--nat-system-route-support` (`true` \| `false`) controls whether Cloud WAN automatically installs routes for the attachment's NAT CIDRs in the attachment's segment:
+ **Direct Connect gateway and BGP Site-to-Site VPN attachments** – You can set to `true` or `false`. If you omit it, Cloud WAN keeps the current value; for a new configuration, it defaults to `true`. When NAT system route support is set to true, Cloud WAN adds a system route for each NAT CIDR specified in a NAT gateway rule, and the routes your network advertises aren't changed. When it's disabled, advertise the NAT CIDRs from your network, or add static routes in your core network policy.
+ **VPC attachments** – Always `true`; setting it to `false` is rejected. When a rule's `MatchSourceCidr` exactly equals one of the VPC's CIDRs, the VPC CIDR's route is replaced by a route for the rule's `NatCidr`. For rules that don't exactly match, add a static route for the `NatCidr` in your core network policy.
+ **Connect attachments** – Always `false`; setting it to `true` is rejected. Your peers must advertise the NAT CIDRs.

### Replace the full rule set
<a name="cloudwan-nat-cli-replace"></a>

The list you supply replaces all existing rules on the attachment, so include every rule you want to keep in each call. If you omit `--nat-gateway-rules`, the rules stay unchanged.

The following command replaces the existing rules with a single rule:

```
aws networkmanager update-attachment-nat-configuration \
    --attachment-id {{attachment-0123456789abcdef0}} \
    --nat-gateway-rules '[
        {"RuleNumber":100,"MatchSourceCidr":"{{10.200.10.0/24}}","NatCidr":"{{100.64.10.0/24}}"}
    ]'
```

### Disable NAT
<a name="cloudwan-nat-cli-disable"></a>

The following command disables NAT on an attachment:

```
aws networkmanager update-attachment-nat-configuration \
    --attachment-id {{attachment-0123456789abcdef0}} \
    --nat-gateway-support DISABLE
```

When you disable NAT, traffic on the attachment is no longer translated. Your rules are kept and their state changes to deactivated. They're reactivated when you enable NAT again.

### Clear all rules
<a name="cloudwan-nat-cli-clear"></a>

To remove all rules, pass an empty list. NAT can't stay enabled with zero rules, so if NAT is enabled, disable it in the same call:

```
aws networkmanager update-attachment-nat-configuration \
    --attachment-id {{attachment-0123456789abcdef0}} \
    --nat-gateway-support DISABLE \
    --nat-gateway-rules '[]'
```

### View NAT configurations
<a name="cloudwan-nat-cli-view"></a>

You can view the NAT configuration for one attachment, or for all attachments in a core network. Results are paginated.

The following command lists the NAT configuration for one attachment:

```
aws networkmanager list-attachment-nat-configurations \
    --attachment-id {{attachment-0123456789abcdef0}}
```

The following command lists the NAT configurations for all attachments in a core network:

```
aws networkmanager list-attachment-nat-configurations \
    --core-network-id {{core-network-0123456789abcdef0}}
```