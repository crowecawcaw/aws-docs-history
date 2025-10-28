# Optimize AWS infrastructure management with prefix lists

You can reference a prefix list in the following AWS resources.

###### Resources

- [VPC security groups](#prefix-list-vpc-security-group "#prefix-list-vpc-security-group")
- [Subnet route tables](#prefix-list-subnet-route-table "#prefix-list-subnet-route-table")
- [Transit gateway route tables](#prefix-list-tgw-route-table "#prefix-list-tgw-route-table")
- [AWS Network Firewall rule groups](#prefix-list-nfw-rule-groups "#prefix-list-nfw-rule-groups")
- [Amazon Managed Grafana network access control](#prefix-list-grafana "#prefix-list-grafana")
- [AWS Outposts rack local gateways](#prefix-list-outpost-racks-lgw "#prefix-list-outpost-racks-lgw")

## VPC security groups

You can specify a prefix list as the source for an inbound rule, or as the destination
for an outbound rule. For more information, see [Security groups](vpc-security-groups.md "vpc-security-groups.md").

###### Important

You can't modify an existing rule to use a prefix list. You have to create a new rule to use a
prefix list.

###### To reference a prefix list in a security group rule using the console

1. Open the Amazon VPC console at
   [https://console.aws.amazon.com/vpc/](https://console.aws.amazon.com/vpc/ "https://console.aws.amazon.com/vpc/").
2. In the navigation pane, choose **Security
   Groups**.
3. Select the security group to update.
4. Choose **Actions**, **Edit inbound
   rules** or **Actions**, **Edit
   outbound rules**.
5. Choose **Add rule**. For **Type**,
   select the traffic type. For **Source** (inbound rules) or
   **Destination** (outbound rules), choose
   **Custom**. Then, in the next field, under
   **Prefix lists**, choose the ID of the prefix list.
6. Choose **Save rules**.

###### To reference a prefix list in a security group rule using the AWS CLI

Use the [authorize-security-group-ingress](../../../cli/latest/reference/ec2/authorize-security-group-ingress.md "../../../cli/latest/reference/ec2/authorize-security-group-ingress.md") and [authorize-security-group-egress](../../../cli/latest/reference/ec2/authorize-security-group-egress.md "../../../cli/latest/reference/ec2/authorize-security-group-egress.md") commands. For the
`--ip-permissions` parameter, specify the ID of the prefix list
using `PrefixListIds`.

## Subnet route tables

You can specify a prefix list as the destination for route table
entry. You cannot reference a prefix list in a gateway route table. For
more information about route tables, see [Configure route tables](VPC_Route_Tables.md "VPC_Route_Tables.md").

###### To reference a prefix list in a route table using the console

1. Open the Amazon VPC console at
   [https://console.aws.amazon.com/vpc/](https://console.aws.amazon.com/vpc/ "https://console.aws.amazon.com/vpc/").
2. In the navigation pane, choose **Route Tables**, and select the
   route table.
3. Choose **Actions**, **Edit routes**.
4. To add a route, choose **Add route**.
5. For **Destination** enter the ID of a prefix list.
6. For **Target**, choose a target.
7. Choose **Save changes**.

###### To reference a prefix list in a route table using the AWS CLI

Use the [create-route](../../../cli/latest/reference/ec2/create-route.md "../../../cli/latest/reference/ec2/create-route.md")
(AWS CLI) command. Use the `--destination-prefix-list-id` parameter to
specify the ID of a prefix list.

## Transit gateway route tables

You can specify a prefix list as the destination for a route. For more
information, see [Prefix
list references](../tgw/create-prefix-list-reference.md "../tgw/create-prefix-list-reference.md") in _Amazon VPC Transit Gateways_.

## AWS Network Firewall rule groups

An AWS Network Firewall rule group is a reusable set of criteria for inspecting and
handling network traffic. If you create Suricata-compatible stateful rule groups
in AWS Network Firewall, you can reference a prefix list from the rule group. For more
information, see [Referencing Amazon VPC prefix lists](../../../network-firewall/latest/developerguide/rule-groups-ip-set-references.md#rule-groups-referencing-prefix-lists "../../../network-firewall/latest/developerguide/rule-groups-ip-set-references.md#rule-groups-referencing-prefix-lists") and [Creating a stateful
rule group](../../../network-firewall/latest/developerguide/rule-group-stateful-creating.md "../../../network-firewall/latest/developerguide/rule-group-stateful-creating.md") in the _AWS Network Firewall Developer
Guide_.

## Amazon Managed Grafana network access control

You can specify one or more prefix lists as an inbound rule for requests to
Amazon Managed Grafana workspaces. For more information about Grafana workspace network access
control, including how to reference prefix lists, see [Managing network
access](../../../grafana/latest/userguide/AMG-configure-nac.md "../../../grafana/latest/userguide/AMG-configure-nac.md") in the _Amazon Managed Grafana User Guide_.

## AWS Outposts rack local gateways

Each AWS Outposts rack provides a local gateway that allows you to connect your Outpost resources with your on-premises networks. You can group CIDRs that you frequently use in a prefix list and reference this list as a route target in your local gateway route table. For more information, see [Manage local gateway route table routes](../../../outposts/latest/userguide/routing.md#manage-lgw-routes "../../../outposts/latest/userguide/routing.md#manage-lgw-routes") in the _AWS Outposts User Guide for racks_.
