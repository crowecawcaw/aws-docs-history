NEW - You can now accelerate your migration and modernization with AWS Transform. Read [Getting Started](../../../transform/latest/userguide/getting-started.md "../../../transform/latest/userguide/getting-started.md") in the _AWS Transform User Guide_.

# Transfer server tags

Choose whether you want AWS Application Migration Service to transfer any user-configured custom tags from your
source servers onto your test or cutover instance.

If you choose **Yes**, server tags are transferred. These
tags are attached to all source servers, all launched test and cutover instances, and all of
the ephemeral resources that are created on your AWS Account during the normal operation of
AWS Application Migration Service. These resources include:

- EC2 instances
- Conversion groups
- Security groups
- EBS volumes
- Snapshots

###### Note

AWS Application Migration Service automatically adds system tags to all resources.

###### Note

Transfer server tags only copies tags associated with the source servers in the
AWS Application Migration Service console, and does not copy the EC2 source server tags (in case of AWS to AWS migration)

If you choose the **No** option, server tags are not
transferred. You can always add tags from the Amazon EC2 console as described in [this EC2 article.](../../../AWSEC2/latest/UserGuide/Using_Tags.md#tag-resources)%5C "../../../AWSEC2/latest/UserGuide/Using_Tags.md#tag-resources)%5C")

###### Note

Tags that are added on the EC2 launch template take precedence over tags that are
transferred directly from the source server.
