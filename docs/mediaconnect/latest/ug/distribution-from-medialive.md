# Distributing content from an AWS Elemental MediaLive

Multiplex

An AWS Elemental MediaLive [multiplex](../../../medialive/latest/ug/eml-multiplex.md "../../../medialive/latest/ug/eml-multiplex.md") creates a UDP transport stream (TS) that carries multiple programs,
also known as a multi-program transport stream (MPTS). When you create a multiplex, MediaLive automatically grants an entitlement in MediaConnect for your
account. Create a flow based on that entitlement and distribute the content from that flow.

###### To distribute content from a MediaLive multiplex (console)

1. In MediaLive, [create a multiplex](../../../medialive/latest/ug/multiplex-create.md "../../../medialive/latest/ug/multiplex-create.md").

MediaLive creates a MediaConnect entitlement that uses the multiplex as the source. The name of the entitlement includes `multiplex` and
the name you chose for the multiplex. 2. In MediaConnect, [create a flow based on the
new entitlement](entitlements-subscriber.md "entitlements-subscriber.md"). 3. [Add outputs](outputs-add.md "outputs-add.md") to distribute the
content.
