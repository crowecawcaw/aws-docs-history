# Tagging Amazon Managed Blockchain (AMB) resources

A _tag_ is a custom attribute label that you assign or that AWS
assigns to an AWS resource. Each tag has two parts:

- A _tag key_, such as `CostCenter`,
  `Environment`, or `Project`. Tag keys are
  case-sensitive.
- An optional field known as a _tag value_, such as
  `111122223333` or `Production`. Omitting the tag
  value is the same as using an empty string. Like tag keys, tag values are
  case-sensitive.
  Tags help you do the following:

- Identify and organize your AWS resources. Many AWS services support tagging, so
  you can assign the same tag to resources from different services to indicate that
  the resources are related. For example, you could assign the same tag to an Amazon Managed Blockchain (AMB) node and an EC2 instance that you use as a client for the AMB Access framework.
- Track your AWS costs. You activate these tags on the AWS Billing and Cost Management dashboard. AWS uses
  the tags to categorize your costs and deliver a monthly cost allocation report to
  you. For more information, see [Using cost allocation tags](../../../awsaccountbilling/latest/aboutv2/cost-alloc-tags.md "../../../awsaccountbilling/latest/aboutv2/cost-alloc-tags.md") in the [AWS Billing User Guide](../../../awsaccountbilling/latest/aboutv2.md "../../../awsaccountbilling/latest/aboutv2.md").
- Control access to your AWS resources with AWS Identity and Access Management (IAM). For information,
  see [Controlling access using tags](security_iam_id-based-policy-examples.md#security_iam_id-based-policy-examples-tags "security_iam_id-based-policy-examples.md#security_iam_id-based-policy-examples-tags") in this developer guide and
  [Control access using IAM
  tags](../../../IAM/latest/UserGuide/access_iam-tags.md "../../../IAM/latest/UserGuide/access_iam-tags.md") in the _IAM User Guide_.
  For more information about tags, see the [Tagging Best Practices](https://aws.amazon.com/answers/account-management/aws-tagging-strategies/ "https://aws.amazon.com/answers/account-management/aws-tagging-strategies/") guide.

The following sections provide more information about tags for AMB Access.

## Create and add tags for AMB Access Ethereum resources

You can tag the following resources:

- Networks
- Nodes

Tags that you create for Ethereum public networks
are scoped only to the account in
which you create them. Other AWSaccounts participating on the network cannot access
the tags.

## Tag naming and usage conventions

The following basic naming and usage conventions apply to tags used with AMB Access
resources:

- Each resource can have a maximum of 50 tags.
- For each resource, each tag key must be unique, and each tag key can have only
  one value.
- The maximum tag key length is 128 Unicode characters in UTF-8.
- The maximum tag value length is 256 Unicode characters in UTF-8.
- Allowed characters are letters, numbers, spaces representable in UTF-8, and
  the following characters: `. : + =
@ _ / -` (hyphen).
- Tag keys and values are case-sensitive. As a best practice, decide on a strategy
  for capitalizing tags, and consistently implement that strategy across all resource
  types. For example, decide whether to use `Costcenter`,
  `costcenter`, or `CostCenter`, and use the same convention
  for all tags. Avoid using similar tags with inconsistent case treatment.
- The `aws:` prefix is reserved for AWS use. You can't edit or
  delete a tag's key or value when the tag has a tag key with the
  `aws:` prefix. Tags with this prefix do not count against your limit of tags per resource.

## Working with tags

You can use the AMB Access console, the AWS CLI, or the AMB Access API to add, edit, or delete tag keys and tag values. You can assign tags when you create a resource, or you can apply tags after the resource is created.

For more information about AMB Access API actions for tagging, see the following topics in the _Amazon Managed Blockchain (AMB) API Reference_:

- [ListTagsForResource](../APIReference/API_ListTagsForResource.md "../APIReference/API_ListTagsForResource.md")
- [TagResource](../APIReference/API_TagResource.md "../APIReference/API_TagResource.md")
- [UntagResource](../APIReference/API_TagResource.md "../APIReference/API_TagResource.md")

Using the AMB Access console, you can add a tag to an Ethereum node when you create it or when viewing node details. You can remove a tag when viewing node details. For more information, see [Working with Ethereum nodes using AMB Access](ethereum-nodes.md "ethereum-nodes.md").

AMB Access allows you to tag public Ethereum networks after you create a node on the network using AMB Access.

###### To add or remove a tag for an Ethereum network using the AWS Management Console

1. Open the AMB Access console at [https://console.aws.amazon.com/managedblockchain/](https://console.aws.amazon.com/managedblockchain/ "https://console.aws.amazon.com/managedblockchain/").
2. If the console doesn't open to the **Networks** list, choose **Networks** from the navigation pane.
3. Choose the network from the list.
4. Under **Tags**, choose **Edit tags**, and then do one of the following:
   - To add a tag, choose **Add new tag**, enter a **Key** and optional **Value**, and then choose **Save**.
   - To remove a tag, choose **Remove** next to the **Tag** you want to remove, and then choose **Save**.

###### To add or remove a tag for a node

1. Open the AMB Access console at [https://console.aws.amazon.com/managedblockchain/](https://console.aws.amazon.com/managedblockchain/ "https://console.aws.amazon.com/managedblockchain/").
2. Choose **Networks** and then choose an Ethereum network from the list.
3. Under **Nodes**, choose a **Node ID** from the list.
4. Choose **Tags**, choose **Edit tags**, and then do one of the following:
   - To add a tag, choose **Add new tag**, enter a **Key** and optional **Value**, and then choose **Save**.
   - To remove a tag, choose **Remove** next to the **Tag** you want to remove, and then choose **Save**.
