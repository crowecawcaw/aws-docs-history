# Encryption Support for AWS Transit Gateway

Encryption Support on Transit Gateway allows you to enforce encryption-in-transit for all traffic on VPCs
attached to your Transit Gateway. When Encryption support is enabled on the TGW, the transit gateway traffic
will be encrypted between VPCs that are in Enforce mode. Traffic to VPCs that don’t have Encryption Controls
turned on, or are in Monitor mode, TGW is guaranteed to encrypt traffic upto the TGW attachment in the VPC.
Beyond that, it depends on the instance the traffic is being sent to in the VPC.

## Transit Gateway Encryption Support and VPC Encryption Control

Encryption Controls allows you to audit the encryption status of the traffic flows in
their VPC and then enforce encryption-in-transit for all traffic on their VPC. When VPC
EC is enforced, all Elastic Network Interfaces (ENI) in that VPC will be restricted to
attach only to AWS Nitro encryption capable instances; and only AWS services that
encrypt data in transit will be allowed to attach to EC enforced VPC.

To support the end to end encryption of data between VPCs through the TGW, the transit gateway attached
to the VPC should also have Encryption Support enabled. Transit gateway provides you with the option to
enable encryption-in-transit capabilities by using AWS Nitro encryption
capable instances.

You can only add encryption support to an existing transit gateway and not while you're creating one.
As the TGW transitions to Encryption Support Enabled, there will be no downtime on the TGW or the
attachments. The migration is seamless and transparent with no traffic being dropped. For the steps to
modify a transit gateway to add Encryption Support, see [Modify a transit gateway](tgw-modifying.md#tgw-modifying.title "tgw-modifying.md#tgw-modifying.title").

### Requirements

Before enabling encryption support on a transit gateway, ensure that:

- All VPCs attached to the transit gateway must be in monitor mode
- The transit gateway doesn't have Connect attachments
- The transit gateway doesn't have Peering attachments
- The transit gateway doesn't have Network Firewall attachments
- The transit gateway doesn't have VPN Concentrator attachments
- The transit gateway doesn't have security group references enabled
- The transit gateway doesn't have Multicast features enabled

###### Note

You can enable Encryption Support on a Transit Gateway to encrypt traffic between your
VPCs that have encryption controls turned on (in either Monitor mode or enforce mode). To enable encryption on
existing TGWs that have VPCs attached to it, you need to enable VPC Encryption Controls in Monitor Mode in all
associated VPCs before enabling Encryption Support on the TGW. Once TGW Encryption Support is **enabled**, you can
then modify compliant VPCs to Enforce mode. Unconnected VPCs that are in enforce mode can be connected via a
new TGW that has encryption support **enabled**.

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
