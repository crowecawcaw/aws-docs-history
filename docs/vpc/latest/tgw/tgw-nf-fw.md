# AWS Transit Gateway network function attachments

You can create a network function attachment to connect your transit gateway directly to
AWS Network Firewall. This eliminates the need to create and manage inspection VPCs.

With a firewall attachment, AWS automatically provisions and manages all the necessary resources behind the scenes. You'll see a new transit gateway attachment rather than individual firewall endpoints. This simplifies the process of implementing centralized network traffic inspection.

Before you can use a firewall attachment, you must first create the attachment in AWS Network Firewall. For the steps to create the attachment, see [Getting Started with
AWS Network Firewall Management](../../../network-firewall/latest/developerguide/getting-started.md "../../../network-firewall/latest/developerguide/getting-started.md") in the _AWS Network Firewall Developer Guide_
After the firewall is created, you can view the attachment in Transit Gateway console under the
**Attachments** section. The attachment will be listed with a type of
**Network function**.

###### Topics

- [Accept or reject a transit gateway network
  function attachment](accept-reject-firewall-attachment.md "accept-reject-firewall-attachment.md")
- [View network function attachments](view-nf-attachment-nm.md "view-nf-attachment-nm.md")
- [Route traffic through a transit
  gateway network function attachment](route-traffic-nf-attachment.md "route-traffic-nf-attachment.md")
