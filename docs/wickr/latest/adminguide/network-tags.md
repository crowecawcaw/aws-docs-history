

This guide documents the new AWS Wickr administration console, released on March 13, 2025. For documentation on the classic version of the AWS Wickr administration console, see [Classic Administration Guide](https://docs.aws.amazon.com/wickr/latest/adminguide-classic/what-is-wickr.html).

# Network tags for AWS Wickr

You can apply tags to Wickr networks. You can then use those tags to search and filter your Wickr networks or track your AWS costs. You can configure network tags on the **Network home** page of the AWS Management Console for Wickr.

A tag is a [key-value pair](https://docs.aws.amazon.com/general/latest/gr/aws_tagging.html) applied to a resource to hold metadata about that resource. Each tag is a label consisting of a key and a value. For more information on tags, see also [What are tags?](https://docs.aws.amazon.com/whitepapers/latest/tagging-best-practices/what-are-tags.html) and [Tagging use cases](https://docs.aws.amazon.com/whitepapers/latest/tagging-best-practices/tagging-use-cases.html).

You can add up to 50 user-defined tags to each Wickr network. Tag keys must be unique for each network and are case-sensitive. A tag value is optional. You can't use the reserved `aws:` prefix in a tag key.

To manage network tags, your IAM principal needs the permissions required for the operation:
+ `wickr:TagResource` – Add a tag or update the value of an existing tag.
+ `wickr:UntagResource` – Remove a tag.
+ `wickr:ListTagsForResource` – List the tags associated with a network.

You can also use network tags for attribute-based access control (ABAC). For more information, see [ABAC with Wickr](security_iam_service-with-iam-tags.md).

**Topics**
+ [Manage network tags in AWS Wickr](manage-tags.md)
+ [Manage network tags with the](manage-network-tags-cli.md)
+ [Add a network tag in AWS Wickr](add-tag.md)
+ [Edit a network tag in AWS Wickr](edit-tag.md)
+ [Remove a network tag in AWS Wickr](remove-tag.md)