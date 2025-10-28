# Tags for your VPC Lattice target group

Tags help you to categorize your target groups in different ways, for example, by
purpose, owner, or environment.

You can add multiple tags to each target group. Tag keys must be unique for each
target group. If you add a tag with a key that is already associated with the target
group, it updates the value of that tag.

When you are finished with a tag, you can remove it.

###### Restrictions

- Maximum number of tags per resource—50
- Maximum key length—127 Unicode characters
- Maximum value length—255 Unicode characters
- Tag keys and values are case sensitive. Allowed characters are letters,
  spaces, and numbers representable in UTF-8, plus the following special
  characters: + - = . \_ : / @. Do not use leading or trailing spaces.
- Do not use the `aws:` prefix in your tag names or values because it
  is reserved for AWS use. You can't edit or delete tag names or values with
  this prefix. Tags with this prefix do not count against your tags per resource
  limit.

###### To update the tags for a target group using the console

1. Open the Amazon VPC console at
   [https://console.aws.amazon.com/vpc/](https://console.aws.amazon.com/vpc/ "https://console.aws.amazon.com/vpc/").
2. In the navigation pane, under **VPC Lattice**, choose
   **Target groups**.
3. Select the name of the target group to open its details page.
4. Choose the **Tags** tab.
5. To add a tag, choose **Add tags** and enter the tag
   key and tag value. To add another tag, choose **Add new
   tag**. When you are finished adding tags, choose
   **Save changes**.
6. To delete a tag, select the check box for the tag and choose
   **Delete**. When prompted for confirmation, enter
   `confirm` and then choose **Delete**.

###### To update the tags for a target group using the AWS CLI

Use the [tag-resource](../../../cli/latest/reference/vpc-lattice/tag-resource.md "../../../cli/latest/reference/vpc-lattice/tag-resource.md")
and [untag-resource](../../../cli/latest/reference/vpc-lattice/untag-resource.md "../../../cli/latest/reference/vpc-lattice/untag-resource.md") commands.
