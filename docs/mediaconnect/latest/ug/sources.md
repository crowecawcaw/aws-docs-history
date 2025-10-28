# Sources in AWS Elemental MediaConnect

A source in MediaConnect can be anything that provides a live video feed, such as the
following:

- An on-premises encoder
- Another AWS Elemental MediaConnect flow
- An AWS Elemental MediaLive output
- A playout system (cloud-based or on-premises)
  For a list of supported protocols that you can use for your source, see [Protocols](protocols.md "protocols.md").

From the MediaConnect console, you can view Amazon CloudWatch metrics to [monitor the source health](monitor-source-health.md "monitor-source-health.md") of an active
flow.

###### Topics

- [Adding a source to an existing MediaConnect flow](source-adding.md "source-adding.md")
- [Updating the source of a MediaConnect flow](source-update.md "source-update.md")
- [Source failover on a MediaConnect flow](source-failover.md "source-failover.md")
- [Managing tags on a MediaConnect source](sources-manage-tags.md "sources-manage-tags.md")
- [Removing a source from a MediaConnect flow](source-remove.md "source-remove.md")
- [Source ports on MediaConnect flows](source-ports.md "source-ports.md")
- [Determining a source's peer IP address](source-ip-address.md "source-ip-address.md")
