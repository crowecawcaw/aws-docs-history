# MediaConnect Gateway bridges

A _bridge_ is a connection between your data center's
instances and the AWS Cloud. Depending on the selected bridge type, a bridge can be
used to send content from the AWS Cloud to your data center or from your data center
to the AWS Cloud.

###### Contents

- [Key points](#gateway-components-bridges-key-points "#gateway-components-bridges-key-points")
  - [Bridge types](#gateway-components-bridges-types "#gateway-components-bridges-types")
  - [Bridge sources](#gateway-components-bridges-sources "#gateway-components-bridges-sources")
  - [Bridge outputs](#gateway-components-bridges-outputs "#gateway-components-bridges-outputs")

- [Next
  steps](#gateway-components-bridges-next-steps "#gateway-components-bridges-next-steps")

## Key points

### Bridge types

AWS Elemental MediaConnect Gateway supports two types of bridges. Each bridge type serves a different
purpose and determines if you will be contributing content to the AWS Cloud or
distributing content to a physical location. The following are the two types of
bridges and their different functions:

- **Ingress bridge**: A ground-to-cloud
  bridge. On an ingress bridge, the content originates at your premises
  and is delivered to the AWS Cloud
- **Egress bridge**: A cloud-to-ground
  bridge. On an egress bridge, the content comes from an existing
  MediaConnect flow and is delivered to your premises.

### Bridge sources

Each bridge requires you to create a minimum of one source. The source is the
content that will be ingested by the MediaConnect Gateway. The origin of the source content
will be different depending on the bridge type you select. If you create
multiple bridge sources, you can enhance the resiliency of your bridge by
activating failover during the creation process. The following are the two types
of sources:

- **Ingress bridge source**: For an ingress
  bridge, the content originates at your premises and is delivered to the
  cloud. When creating an ingress bridge source, you will need to select
  the protocol (RTP, RTP-FEC, or UDP) and enter the multicast IP address
  and port of the content originating in your premises. You can also use
  source-specific multicast (SSM) for ingress bridges, which allows you to
  optionally provide a source IP address in addition to the multicast IP
  when creating or updating an ingress bridge. This gives you more precise
  control over the multicast traffic.
- **Egress bridge source**: For an egress
  bridge, the content originates as an existing MediaConnect flow and is
  delivered to your premises. When creating an egress bridge source, you
  will need to select the MediaConnect flow that you would like to send to your
  premises. You don't need to select the protocol. The source will use the
  same protocol as the existing flow.

#### Bridge source

failover

If you create multiple bridge sources, you can enhance the resiliency of
your bridge by activating failover during the creation process. The failover
configuration determines how AWS Elemental MediaConnect Gateway behaves in the event of source input
loss. The bridge type will determine which of the two failover modes are
available. The following are the two failover modes:

- **Failover**: This mode allows
  switching between a primary and a backup source. You can specify a
  source as the primary source. The second source serves as the
  backup. The service switches to the backup source if the primary
  source fails, and switches back to the primary source as soon as it
  is reliable.
- **Merge**: This mode combines the
  sources into a single stream, allowing a graceful recovery from any
  single-source loss. In merge mode, if a source is missing a packet
  the service pulls the missing packet from the other source.

### Bridge outputs

Each bridge requires you to create a minimum of one output. The following are
the two types of outputs:

- **Ingress bridge output**: For an ingress
  bridge, the content originates at your premises and is delivered to the
  cloud. You do not need to configure outputs for ingress bridge types.
  When you create a MediaConnect flow using the ingress bridge as a source, the
  output is automatically created when the flow is started.
- **Egress bridge output**: For an egress
  bridge, the content originates as an existing MediaConnect flow and is
  delivered to your premises. When you create an egress bridge output, you
  will need to configure the IP and protocol information that will be
  delivered to your premises. Egress bridge outputs support RTP, RTP-FEC,
  and UDP protocols.

## Next

steps

- To create a bridge, see [Creating a MediaConnect Gateway bridge](gateway-components-bridges-create.md "gateway-components-bridges-create.md").
