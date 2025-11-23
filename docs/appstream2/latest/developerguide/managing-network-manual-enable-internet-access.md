# Enable Internet Access for Your

Fleet, Image Builder, or App Block Builder in Amazon WorkSpaces Applications

After your NAT gateway is available on a VPC, you can enable internet
access for your fleet, image builder, and app block builder.

###### Note

When working with IPv6 only subnets, default internet access cannot be enabled. You'll need to set up an Egress-Only Internet Gateway and configure route table to allow outbound internet traffic. For more information check the [steps](../../../vpc/latest/userguide/egress-only-internet-gateway.md "../../../vpc/latest/userguide/egress-only-internet-gateway.md"). You also need to enable auto-assign IPv6 addresses for your subnets. The Egress-Only gateway handles outbound internet traffic only so if you need inbound access, you'll still need a regular internet gateway. You can find more details about this in [egress only internet gateway documentation](../../../vpc/latest/userguide/egress-only-internet-gateway.md "../../../vpc/latest/userguide/egress-only-internet-gateway.md"). Ensure appropriate security and networking controls exist to prevent accidental inbound/outbound access for your subnets.

###### Topics

- [Enable Internet Access for Your Fleet in Amazon WorkSpaces Applications](managing-network-manual-fleet-enable-internet-access-fleet.md "managing-network-manual-fleet-enable-internet-access-fleet.md")
- [Enable Internet
  Access for Your Image Builder in Amazon WorkSpaces Applications](managing-network-manual-enable-internet-access-image-builder.md "managing-network-manual-enable-internet-access-image-builder.md")
- [Enable Internet
  Access for Your App Block Builder in Amazon WorkSpaces Applications](managing-network-enable-internet-access-app-block-builder.md "managing-network-enable-internet-access-app-block-builder.md")
