# Tagging Neptune Analytics graph resources

You can use Neptune Analytics graph tags to add metadata to your graph. You can use the tags to add your own notations about graph and
graph snapshots. Doing so can help you to document your Neptune Analytics graph resources.

You can also use these tags with IAM policies. You can use them to manage access to Neptune Analytics graph resources and to control
what actions can be applied to the Neptune Analytics graph resources. You can also use these tags to track costs by grouping expenses
for similarly tagged resources. You can tag the following Neptune Analytics graph resources:

- Neptune Analytics graph
- Neptune Analytics graph snapshots

A Neptune Analytics graph tag is a name-value pair that you define and associate with a Neptune Analytics graph resource. The name is referred to as the
key. Supplying a value for the key is optional. You can use tags to assign arbitrary information to a Neptune Analytics graph resource.
You can use a tag key to define a category, and the tag value might be an item in that category. For example, you might
define a tag key of "env" and a tag value of "preprod". In this case, these indicate that the Neptune Analytics graph resource is
assigned to the preprod environment. It is recommended that you use a consistent set of tag keys to make it easier
to track metadata associated with Neptune Analytics graph resources.

Additionally, you can use conditions in your IAM policies to control access to AWS resources based on the tags
used on that resource. You can do this by using the global `aws:ResourceTag/tag-key` condition key. For
more information, see
[Controlling
access to AWS resources](../../../IAM/latest/UserGuide/access_tags.md#access_tags_control-resources "../../../IAM/latest/UserGuide/access_tags.md#access_tags_control-resources") in the AWS Identity and Access Management user guide.

You can use the AWS management console, the AWS CLI, or the Neptune graph API to add, list, and delete tags
on Neptune Analytics graph resources. When using the CLI or API, make sure to provide the Amazon Resource Name (ARN) for the Neptune Analytics graph
to work with. For more information about constructing an ARN, see [Working with ARNs in Neptune Analytics graph](managing-ARN.md "managing-ARN.md").

###### Note

Tags are cached for authorization purposes. Because of this, additions and updates to tags on Neptune Analytics resources
can take several minutes before they are available.

**Using tags to produce detailed billing reports**

You can also use tags to track costs by grouping expenses for similarly tagged resources. Use tags to organize your
AWS bill to reflect your own cost structure. To do this, sign up to get your AWS account bill with tag key values
included. Then, to see the cost of combined resources, organize your billing information according to resources with
the same tag key values. For example, you can tag several resources with a specific application name, and then organize
your billing information to see the total cost of that application across several services. For more information,
see [Using Cost Allocation Tags](../../../awsaccountbilling/latest/aboutv2/cost-alloc-tags.md "../../../awsaccountbilling/latest/aboutv2/cost-alloc-tags.md") in the AWS Billing user guide.

**Adding, listing, and removing tags**

The process to tag a Neptune Analytics graph resource is similar for all resources. The following procedure shows how to tag a Neptune Analytics graph

AWS Console
**To add a tag to a Neptune Analytics graph**

1. Sign in to the AWS Management Console, and open the Amazon Neptune console at
   [https://console.aws.amazon.com/neptune/](https://console.aws.amazon.com/neptune/ "https://console.aws.amazon.com/neptune/").
2. In the navigation pane, choose **Graphs**.
3. Choose the name of the graph that you want to tag. This will show the graph details.
4. In the details section, scroll down to the **Tags** section.
5. Choose **Manage tags**. The Manage tags window appears.
6. Enter a value for Tag key and value.
7. To add additional tags, choose the **Add another tag** button and enter values
   for its Tag key and value. Repeat this step as many times as necessary.
8. Choose the **Save** button to save the changes.

**To delete a tag from a DB instance**

1. Sign in to the AWS Management Console, and open the Amazon Neptune console at
   [https://console.aws.amazon.com/neptune/](https://console.aws.amazon.com/neptune/ "https://console.aws.amazon.com/neptune/").
2. In the navigation pane, choose **Graphs**.
3. Choose the name of the graph that you want to tag. This will show the graph details.
4. In the details section, scroll down to the **Tags** section.
5. Choose **Manage tags**. The Manage tags window appears.
6. Choose the **Remove** button for the tag you want to delete.
7. Choose the **Save** button to save your changes.

AWS CLI

You can add, list or remove tags for a graph using the AWS CLI.

- To add one or more tags to a Neptune Analytics graph resource, use the AWS CLI command `tag-resource`.

To list the tags on a Neptune Analytics graph resource, use the AWS CLI command `list-tags-for-resource`.

To remove one or more tags from a Neptune Analytics graph resource, use the AWS CLI
`command untag-resource`.

To learn more about how to construct the required ARN, see [Working with ARNs in Neptune Analytics graph](managing-ARN.md "managing-ARN.md").
