# Encryption Support for AWS Transit Gateway

Encryption Controls allows you to audit the encryption status of the traffic flows in your VPC and then
enforce encryption-in-transit for all traffic within the VPC. When VPC Encryption Control is in enforce mode,
all Elastic Network Interfaces (ENI) in that VPC will be restricted to attach only to AWS Nitro encryption
capable instances; and only AWS services that encrypt data in transit will be allowed to attach to Encryption
Controls enforced VPC. For more information on VPC Encryption Controls, please refer to this
[documentation](../userguide/vpc-encryption-controls.md "../userguide/vpc-encryption-controls.md").

## Transit Gateway Encryption Support and VPC Encryption Control

Encryption Support on Transit Gateway allows you to enforce encryption-in-transit for traffic between VPCs
attached to a Transit Gateway. You will need to manually activate Encryption Support on the Transit Gateway
using the [modify-transit-gateway](../../../cli/latest/reference/ec2/modify-transit-gateway.md "../../../cli/latest/reference/ec2/modify-transit-gateway.md")
command to encrypt traffic between the VPCs. Once enabled, all traffic will traverse 100% encrypted links
between VPCs that are in Enforce mode (without exclusions) through the Transit Gateway. You can also connect
VPCs that don’t have Encryption Controls turned on, or are in Monitor mode through a Transit Gateway that
has Encryption Support enabled. In this scenario Transit Gateway is guaranteed to encrypt traffic up to
the Transit Gateway attachment in the VPC not running in enforce mode. Beyond that, it depends on the
instance the traffic is being sent to in the VPC not running in enforce mode.

You can only add encryption support to an existing transit gateway and not while you're creating one.
As the Transit Gateway transitions to Encryption Support Enabled state,
there will be no downtime on the Transit Gateway or the attachments.
The migration is seamless and transparent with no traffic being dropped.
For the steps to modify a transit gateway to add Encryption Support,
see [Modify a transit gateway](tgw-modifying.md#tgw-modifying.title "tgw-modifying.md#tgw-modifying.title").

### Requirements

Before enabling encryption support on a transit gateway, ensure that:

- The transit gateway doesn't have Connect attachments
- The transit gateway doesn't have Peering attachments
- The transit gateway doesn't have Network Firewall attachments
- The transit gateway doesn't have VPN Concentrator attachments
- The transit gateway doesn't have security group references enabled
- The transit gateway doesn't have Multicast features enabled

### Encryption Support states

A transit gateway can have one of the following encryption states:

- **enabling** - The transit gateway is in the process of enabling
  encryption support. This process can take up to 14 days to complete.
- **enabled** - Encryption support is enabled on the transit gateway. You
  can create VPC attachments with Encryption Control enforced.
- **disabling** - The transit gateway is in the
  process of disabling Encryption support.
- **disabled** - Encryption support is disabled on
  the transit gateway.

### Transit Gateway attachment rules

When a transit gateway has Encryption support enabled, the following attachment rules
apply:

- When the transit gateway encryption state is **enabling** or **disabling**,
  you can create Direct Connect attachments, VPN attachments, and VPC attachment not in Encryption
  Control enforced or enforcing mode.
- When the transit gateway encryption state is **enabled**, you can create VPC,
  Direct Connect attachments, VPN attachments, and VPC attachments in any Encryption Control mode.
- When the transit gateway encryption state is **disabling**,
  you cannot create new VPC attachments with Encryption control
  enforced.
- Connect attachments, peering attachments, security group references, and multicast features are
  not supported with Encryption Support.

Attempting to create incompatible attachments will fail with an API error.
