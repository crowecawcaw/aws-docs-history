# Flexible cost allocation

By default, transit gateway uses a sender-based cost allocation model where data processing charges are allocated to the account that owns the source attachment. You can create custom metering policies that define which accounts should be charged based on traffic flow properties such as attachment types, specific attachment IDs, or network addresses.

Metering policies consist of ordered rules that are evaluated from lowest to highest rule number. When traffic matches a rule, the specified account is charged according to the rule's configuration. You can specify the account owner for allocating costs from the following options:

- **Source attachment owner** - Charges are allocated to the account that owns the source attachment (default behavior)
- **Destination attachment owner** - Charges are allocated to the account that owns the destination attachment
- **Transit Gateway owner** - Charges are allocated to the account that owns the transit gateway

Flexible Cost Allocation enables better cost management for organizations using centralized network architectures, allowing costs to be allocated to the appropriate business units or application owners regardless of network topology.

###### Note

Flexible Cost Allocation enables flexible allocation of metering usage and in turn costs to account owners of your choice.
However, tax implications for AWS accounts can vary significantly based on geographic location, usage patterns and other factors.
Please review the billing, tax and cost management implications for accounts in your AWS Organization prior to enabling this feature. Reference: [What is AWS Billing and Cost Management?](../../../awsaccountbilling/latest/aboutv2/billing-what-is.md "../../../awsaccountbilling/latest/aboutv2/billing-what-is.md")

## Metering policies

Metering policies allow you to configure cost allocation rules for your transit gateway to control
which accounts are charged for data processing and transfer costs based on traffic flow
properties. This feature enables better cost management and chargeback capabilities for
organizations using centralized network architectures.

A metering policy is composed of the following:

- **Metering policy** - The overall configuration container that contains the Metering Policy Rules. When created, it contains a single default metering policy entry that is configured to charge all traffic to the source attachment owner. Each transit gateway can have only one metering policy.
- **Metering policy entry** - Individual rules within a metering policy that define specific matching criteria and the account to meter usage. Each entry includes a rule number for evaluation order, traffic matching conditions (such as source and destination attachment types, attachment IDs, CIDR blocks, ports, and protocols), and which account owner to charge for matching traffic. A policy can contain up to 50 entries, evaluated in order from lowest to highest rule number.

You can allocate metering usage to any of the following:

    + **Source attachment owner**: Allocates metering usage to the account that owns the attachment where traffic originates (default behavior)
    + **Destination attachment owner**: Allocates metering usage to the account that owns the attachment where traffic terminates, and
    + **transit gateway owner**: Allocates metering usage to the account that owns the transit gateway.

- **Middlebox attachments** - (Optional) Designated transit gateway attachments that route traffic through network appliances for security inspection, load balancing, or other network functions. Data usage for the traffic traversing middlebox attachments is metered to the account owner specified in the metering policy. You can specify a maximum of 10 middlebox attachments. Supported middlebox attachment types are Network Function (AWS Network Firewall), VPC and VPN attachments.

### How metering policies work

By default, transit gateway uses a sender-based cost allocation model where data processing charges are metered to the account that owns the source attachment. With metering policies, you can create custom rules to flexibly meter usage based on the following traffic flow properties:

- Source and destination attachment types (VPC, VPN, Direct Connect Gateway, Peering, Network Function and VPN Concentrator)
- Source and destination attachment IDs
- Source and destination IP addresses, Port ranges and protocols

Metering policies consist of ordered rules that are evaluated from lowest to highest rule number. When traffic matches a rule, the specified account is charged according to the rule's metered account setting. Metering policies address several common organizational scenarios:

- **Hybrid environment cost allocation**: Allocate costs for data entering AWS from on-premises through Direct Connect Gateway to the destination VPC account owner rather than the central IT admin account owner.
- **Centralized inspection architecture**: Allocate costs to individual application or VPC account owners rather than the central security team for traffic traversing via inspection VPCs.
- **Application-based chargeback**: Allocate all data usage costs for a workload to the VPC owner regardless of traffic direction.
- **Client cost allocation**: Allocate data costs to client
  accounts when they create attachments to your transit gateway.

### Middlebox attachments

transit gateway metering policies support Middlebox attachments allowing you to flexibly allocate data processing charges for network traffic routed via middlebox appliances such as network firewalls and load balancers. Examples of middlebox attachments are Network Function attachment to AWS Network Firewall or VPC attachments that route traffic to third-party security appliances in a VPC. Traffic between source and destination transit gateway attachments traverses via these middlebox attachments for typical security inspection use-cases. You can define metering policies to flexibly allocated data processing usage on middlebox attachments to the original source attachment, final destination attachment or transit gateway account owner. For Network Function attachments, the AWS Network Firewall data processing charges are also allocated to the metered account.

### Flexible Cost Allocation - Metering usage types

Flexible cost allocation via metering policies applies to following data usage types:

- Transit gateway Data Processing Usage on VPC, VPN, VPN Concentrator and Direct Connect attachments
- Site-to-site VPN Data Transfer Out usage on VPN attachments
- Direct Connect Data Transfer Out usage on Direct Connect attachments.
- Data transfer usage on TGW peering attachments
- Transit gateway Data processing usage on Network Function attachments
- AWS network firewall (NFW) data processing usage on Network Function attachments.

Flexible cost allocation does not apply to attachments hourly usage and multicast data processing usage. For Transit Gateway Connect attachments, metering policy can be defined for the underlying transport VPC or Direct Connect attachment. For Private IP VPN attachments, metering policy can be defined for the underlying transport Direct Connect attachment.

### Considerations and limitations

Consider the following when implementing metering policies for your transit gateway.

#### Permissions

- Only the transit gateway owner can create, modify, or delete metering policies.
- Cost allocation settings apply at the transit gateway level.
- Attachment owners cannot override cost allocation settings configured by the transit gateway owner.

#### Transit Gateway peering

When traffic traverses transit gateway peering connections:

- Each transit gateway applies its own metering policy independently.
- Data charges are allocated separately by each transit gateway based on its local policy.
- Traffic can be thought of as two separate flows: source attachment to peering, and peering to destination attachment.

#### Cloud WAN integration

When a transit gateway is attached to a Cloud WAN core network:

- Transit gateway data transfer charges on peering connections are allocated according to the transit gateway metering policy.
- Metering policies are not supported on Cloud WAN core networks.

#### Performance impact

- Metering policies do not introduce any additional data-path latency.
- Metering policies have no impact on maximum bandwidth per attachment.
- There are no changes to transit gateway resource sharing capabilities.

#### Billing integration

- Cost allocation tags continue to work with metering policies for organizing costs by business unit.
- Metering policies define which accounts incur costs, while cost allocation tags help categorize those costs.
- Changes to metering policies take effect at the end of the next billing hour.

#### IPv6 support

Metering policies are supported for both IPv4 and IPv6 traffic. CIDR block matching in policy entries works with both address families.

#### Middlebox attachment support

- Middlebox metering policy assumes traffic between the original source and destination attachment is hair-pinned via the specified middle-box attachment (example east-west inspection for VPC-to-VPC traffic). Hence the network 5-tuple (source/destination IPs, source/destination ports and protocol) for flows ingressing and egressing out of middle-box attachments must match. Flows with 5-tuple mis-matches on middle-box attachments (e.g. NAT transformation in inspection VPC) are treated as regular source-destination attachment flows (as opposed to middle-box attachment flows).
- All egress-only flows on the middlebox attachment (for example north-south traffic to internet via IGW in an inspection VPC) are treated as regular source-destination flows (as opposed to middle-box attachment flows).
- For Network Function attachments when AWS Network firewall drops packets, all data processing usage is charged back to the sender account regardless of metering policy configuration.

###### Topics
