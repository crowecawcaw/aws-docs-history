# Manage tags for a VPC Lattice service

network

Tags help you to categorize your service network in different ways, for example, by
purpose, owner, or environment.

You can add multiple tags to each service network. Tag keys must be unique for each
service network. If you add a tag with a key that is already associated with the service
network, it updates the value of that tag. You can use characters such as letters,
spaces, numbers (in UTF-8), and the following special characters: + - = . \_ : / @. Do
not use leading or trailing spaces. Tag values are case sensitive.

###### To add or delete tags using the console

1. Open the Amazon VPC console at
   [https://console.aws.amazon.com/vpc/](https://console.aws.amazon.com/vpc/ "https://console.aws.amazon.com/vpc/").
2. In the navigation pane, under **VPC Lattice**, choose
   **Service networks**.
3. Select the name of the service network to open its details page.
4. Choose the **Tags** tab.
5. To add a tag, choose **Add tags** and enter the tag key and
   tag value. To add another tag, choose **Add new tag**. When you
   are finished adding tags, choose **Save changes**.
6. To delete a tag, select the check box for the tag and choose
   **Delete**. When prompted for confirmation, enter
   `confirm` and then choose
   **Delete**.

###### To add or delete tags using the AWS CLI

Use the [tag-resource](../../../cli/latest/reference/vpc-lattice/tag-resource.md "../../../cli/latest/reference/vpc-lattice/tag-resource.md") and [untag-resource](../../../cli/latest/reference/vpc-lattice/untag-resource.md "../../../cli/latest/reference/vpc-lattice/untag-resource.md")
commands.
