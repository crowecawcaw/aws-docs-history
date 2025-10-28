# Working with channel groups in AWS Elemental MediaPackage

A channel group is the top-level resource that consists of channels and origin endpoints associated with it.
After you create a channel group, MediaPackage provides a fixed egress domain for its lifetime, regardless
of any failures or upgrades that might occur. All channels and origin endpoints belonging to this
channel group use the same egress domain. Direct your CDNs to this domain for stream delivery from MediaPackage.

For each channel group, you add channels that define the entry point for a content stream into MediaPackage.
You then add origin endpoints to the channels that define the packaging options for the output stream.

###### Topics

- [Creating a channel group](channel-group-create.md "channel-group-create.md")
- [Viewing channel group details](channel-group-view.md "channel-group-view.md")
- [Editing a channel group](channel-group-edit.md "channel-group-edit.md")
- [Deleting a channel group](channel-group-delete.md "channel-group-delete.md")
