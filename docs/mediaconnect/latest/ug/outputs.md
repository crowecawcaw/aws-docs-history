# Managing outputs in MediaConnect

Outputs are the different destinations where you want MediaConnect to send the content of your
flow. You can add, remove, and disable outputs at any time, even when the flow is active. A
disabled output will stop steaming content to its destination and won't incur data transfer
costs. These outputs are sent to the IP address that you specify. This option is useful if
you intend to send your content to an on-premises encoder.

For transport stream flows, you can [grant an
entitlement](entitlements-grant.md "entitlements-grant.md") to share your content with another AWS account (subscriber
account). When the subscriber creates a flow using your content as the source,
AWS Elemental MediaConnect generates an output on your flow.

###### Note

If you [disable](entitlements-disable.md "entitlements-disable.md") an entitlement after the
subscriber creates a flow based on that entitlement, the associated output remains on
your flow. This output continues to counts toward your maximum number of outputs. To
delete an output that's associated with an entitlement, [revoke](entitlements-revoke.md "entitlements-revoke.md") the entitlement.

###### Topics

- [Using NDI® outputs in a MediaConnect
  flow](outputs-using-ndi.md "outputs-using-ndi.md")
- [Adding outputs to a MediaConnect flow](outputs-add.md "outputs-add.md")
- [Viewing the list of outputs for a MediaConnect
  flow](outputs-view-list.md "outputs-view-list.md")
- [Updating outputs on a MediaConnect flow](outputs-update.md "outputs-update.md")
- [Managing tags on a MediaConnect output](outputs-manage-tags.md "outputs-manage-tags.md")
- [Disabling or removing outputs from a MediaConnect
  flow](outputs-remove.md "outputs-remove.md")
- [Output destinations](destinations.md "destinations.md")
- [Determining an output's IP address](output-ip-address.md "output-ip-address.md")
