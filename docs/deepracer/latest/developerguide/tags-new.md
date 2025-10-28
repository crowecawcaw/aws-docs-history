# Add, view, and edit tags for a new resource

Adding tags to a new car, RL model, or community races leaderboard can help you identify, organize,
track cost allocation, and manage access to these resources. Add one or more tags (key-value
pairs) to a model or leaderboard. For each resource, each tag key must be unique, and each tag
key can have only one value, but one resource may have up to 50 tags.

Create and apply the tags one resource at a time in the AWS DeepRacer console or use the [Tag Editor](../../../ARG/latest/userguide/tag-editor.md "../../../ARG/latest/userguide/tag-editor.md") to
add, edit, or delete multiple resources at once.

###### Important

Editing tags for an RL model or community races leaderboard can impact access to those resources. Before you edit the name (key) or value of a tag, make sure to review any IAM policies that might use the key or value for a tag to control access to those resources.

###### To add, view, and edit tags for a new RL model

Use the AWS DeepRacer console to add, view, and edit tags to a new RL model.

1. In **Your models**, choose **Create model**.
2. On the **Create model** page, after filling out the **Training details**, expand the **Tags** heading.
3. Under the **Tags** heading, choose **Add new tag**.
4. In **Key**, enter a name for the tag. You can add an optional value for the tag in **Value**. For more information about naming tags, see the Best Practices for Naming Tags and Resources topic in the [Tagging best practices](https://d1.awsstatic.com/whitepapers/aws-tagging-best-practices.pdf "https://d1.awsstatic.com/whitepapers/aws-tagging-best-practices.pdf") whitepaper.
5. (Optional) To add another tag, choose **Add new tag** again.
6. (Optional) To remove an individual key or value, select the **X** next to it.
7. (Optional) To remove a key-value pair, choose **Remove**.
8. When you have finished adding tags, choose a track under **Environment simulation** and select **Next**.
   After tagging and submitting a new model for training, you can manage its tags during or after training and evaluation under the **Tags** heading at the bottom of the page.

9. Choose **Manage tags**.
10. In the **Manage tags** pop up box, you can remove a tag you have created by selecting the **Remove** button next to the tag you want to remove or choose **Add a new tag** to add a new tag.
11. If you choose to add a new tag, in **Key**, enter a name for the tag. You can add an optional value for the tag in **Value**. For more information about naming tags, see the Best Practices for Naming Tags and Resources topic in the [Tagging best practices](https://d1.awsstatic.com/whitepapers/aws-tagging-best-practices.pdf "https://d1.awsstatic.com/whitepapers/aws-tagging-best-practices.pdf")
    whitepaper.
12. When you have finished removing and adding tags, choose **Submit**.

###### To add, view, and edit Tags for a new community races leaderboard

Use the AWS DeepRacer console to add, view, and edit tags to a new community races leaderboard.

1. In **Community races**, choose **Create race**.
2. On the **Race details** page, expand the **Tags** heading.
3. Under the **Tags** heading, choose **Add new tag**.
4. In **Key**, enter a name for the tag. You can add an optional value for the tag in
   **Value**. For more information about naming tags, see the Best Practices for Naming Tags and Resources
   topic in the [Tagging best practices](https://d1.awsstatic.com/whitepapers/aws-tagging-best-practices.pdf "https://d1.awsstatic.com/whitepapers/aws-tagging-best-practices.pdf")
   whitepaper.
5. (Optional) To add another tag, choose **Add new tag** again.
6. (Optional) To remove an individual key or value, select the **X** next to it.
7. (Optional) To remove a key-value pair, choose **Remove**.
8. When you have finished adding tags, choose a track under **Environment simulation** and
   select **Next**.
