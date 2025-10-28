# Add, view, and edit tags for an existing resource

Adding tags to an existing AWS DeepRacer RL model or community races leaderboard can help you identify, organize,
track cost allocation, and manage access to these resources. Add one or more tags (key-value
pairs) to a model or leaderboard. For each resource, each tag key must be unique, and each tag
key can have only one value, but one resource may have up to 50 tags.

Create and apply the tags one resource at a time in the AWS DeepRacer console or use the [Tag Editor](../../../ARG/latest/userguide/tag-editor.md "../../../ARG/latest/userguide/tag-editor.md") to
add, edit, or delete multiple resources at once.

###### Important

Editing tags for an RL model or community races leaderboard can impact access to those resources. Before you edit
the name (key) or value of a tag, make sure to review any IAM policies that might use the key or value for a tag to control
access to those resources.

###### To add, view, and edit tags for an existing RL model

You can use the AWS DeepRacer console to add, view, or edit tags for an existing RL model.

1. In **Your models**, select a model from the list by choosing its name.
2. Select **Actions**.
3. Choose **Manage tags** from the drop down list.
4. In the **Manage tags** pop up box, you can view, add, or remove a tags:
   1. To add a tag, choose **Add new tag**. In **Key**, enter a name for the tag. You can add an optional value for the tag in **Value**. For more information about naming tags, see the Best Practices for Naming Tags and Resources topic in the [Tagging best practices](https://d1.awsstatic.com/whitepapers/aws-tagging-best-practices.pdf "https://d1.awsstatic.com/whitepapers/aws-tagging-best-practices.pdf") whitepaper.
   2. To add another tag, choose **Add new tag** again.
   3. To remove an individual key or value, select the **X** next to it.
   4. To remove a key-value pair, choose **Remove**.

5. When you have finished viewing, adding, and removing tags, choose **Submit**.

###### To add, view, and edit tags for an existing community races leaderboard

1. In **Community races**, choose **Manage races**.
2. On the **Manage races** page, select a race.
3. Select **Actions**.
4. Choose **Manage tags** from the drop down list.
5. In the **Manage tags** pop up box, you can view, add, or remove a tags:
   1. To add a tag, choose **Add new tag**. In **Key**, enter a name for the tag. You can add an optional value for the tag in **Value**. For more information about naming tags, see the Best Practices for Naming Tags and Resources topic in the [Tagging best practices](https://d1.awsstatic.com/whitepapers/aws-tagging-best-practices.pdf "https://d1.awsstatic.com/whitepapers/aws-tagging-best-practices.pdf") whitepaper.
   2. To add another tag, choose **Add new tag** again.
   3. To remove an individual key or value, select the **X** next to it.
   4. To remove a key-value pair, choose **Remove**.

6. When you have finished viewing, adding, and removing tags, choose **Submit**.
