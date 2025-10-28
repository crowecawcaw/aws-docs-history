# Long ASN support in AWS Direct Connect

Support for long ASNs (4-byte) allows you to configure long Autonomous System Numbers
(ASNs) as part of the parameters of the BGP session established between the AWS
network device and your network device. This feature is enabled or disabled on a
per-account basis.

You can set the an ASN or Long ASN range on either the console or through the
APIs.

- When using the console, the **ASN** field supports both ASNs
  and long ASNs. You can add any range from 1 to 4294967294.
- When using the APIs to create a virtual interface, you can specify either an
  ASN (`asn`) or the Long ASN (`asnLong`) but not both. For
  more information on using ASN or Long ASN, see the following APIs in the [_AWS Direct Connect API Reference_](../APIReference/Welcome.md "../APIReference/Welcome.md"):
  - `BGPPeer`
  - `DeleteBGPPeerRequest`
  - `NewBGPPeer`
  - `NewPrivateVirtualInterface`
  - `NewPrivateVirtualInterfaceAllocation`
  - `NewPublicVirtualInterface`
  - `NewPublicVirtualInterfaceAllocation`
  - `NewTransitVirtualInterface`
  - `NewTransitVirtualInterfaceAllocation`
  - `VirtualInterface`

## Considerations

When choosing to use either an ASN or a long ASN, note the following:

- **Backward compatibility**: Direct Connect automatically
  handles BGP sessions with both ASN and long ASN-capable routers. If your
  router doesn't support long ASNs, the BGP session will operate in ASN
  mode.
- **ASN format**: You can specify 4-byte ASNs in either
  asplain format —for example, `4200000000` or asdot format —
  for example, `64086.59904`. Direct Connect accepts both
  formats but displays ASNs in asplain format
- **Private ASN ranges:** When using private long ASNs
  (`4200000000-4294967294`), the same replacement
  behavior applies as with private ASNs. Direct Connect will replace your
  private ASN with `7224` when advertising to other
  networks.
- **BGP community tags**: All existing BGP community tags
  (`7224:xxxx`) work with long ASNs. The community tag
  format remains unchanged.
- **Monitoring and troubleshooting**: CloudWatch metrics,
  BGP session logs, and troubleshooting tools display long ASNs in asplain
  format for consistency.

## Availability and Pricing

Note the following for long ASN support with AWS Direct Connect:

- **Availability**: Long ASN is available in all AWS Regions where AWS Direct Connect
  is supported.
- **Pricing**: There are no additional charges for long ASN support beyond
  standard AWS Direct Connect pricing.

###### Note

Long ASN enablement applies to your entire AWS account. You cannot enable long ASN support for individual virtual interfaces or BGP peers.
