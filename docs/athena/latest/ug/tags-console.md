# Work with tags for workgroups

Using the Athena console, you can see which tags are in use by each workgroup in your
account. You can view tags by workgroup only. You can also use the Athena console to
apply, edit, or remove tags from one workgroup at a time.

You can search workgroups using the tags you created.

###### Topics

- [Display tags for individual workgroups](#tags-display "#tags-display")
- [Add and delete tags on an individual workgroup](#tags-add-delete "#tags-add-delete")

## Display tags for individual workgroups

###### To display tags for an individual workgroup in the Athena console

1. Open the Athena console at
   [https://console.aws.amazon.com/athena/](https://console.aws.amazon.com/athena/home "https://console.aws.amazon.com/athena/home").
2. If the console navigation pane is not visible, choose the expansion menu
   on the left.

![Choose the expansion menu.](images/nav-pane-expansion.png) 3. On the navigation menu, choose **Workgroups**, and then
choose the workgroup that you want. 4. Do one of the following:

    * Choose the **Tags** tab. If the list of tags is
     long, use the search box.
    * Choose **Edit**, and then scroll down to the
     **Tags** section.

## Add and delete tags on an individual workgroup

You can manage tags for an individual workgroup directly from the
**Workgroups** tab.

###### Note

If you want users to add tags when they create a workgroup in the console or
pass in tags when they use the **CreateWorkGroup** action, make
sure that you give the users IAM permissions to the
**TagResource** and **CreateWorkGroup**
actions.

###### To add a tag when you create a new workgroup

1. Open the Athena console at
   [https://console.aws.amazon.com/athena/](https://console.aws.amazon.com/athena/home "https://console.aws.amazon.com/athena/home").
2. On the navigation menu, choose **Workgroups**.
3. Choose **Create workgroup** and fill in the values as
   needed. For detailed steps, see [Create a workgroup](creating-workgroups.md "creating-workgroups.md").
4. In the **Tags** section, add one or more tags by
   specifying keys and values. Do not add duplicate tag keys at the same time
   to the same workgroup. If you do, Athena issues an error message. For more
   information, see [Tag restrictions](tags.md#tag-restrictions "tags.md#tag-restrictions").
5. When you are done, choose **Create workgroup**.

###### To add or edit a tag to an existing workgroup

1. Open the Athena console at [https://console.aws.amazon.com/athena/](https://console.aws.amazon.com/athena/home "https://console.aws.amazon.com/athena/home").
2. In the navigation pane, choose **Workgroups**.
3. Choose the workgroup that you want to modify.
4. Do one of the following:
   - Choose the **Tags** tab, and then choose
     **Manage tags**.
   - Choose **Edit**, and then scroll down to the
     **Tags** section.

5. Specify a key and value for each tag. For more information, see [Tag restrictions](tags.md#tag-restrictions "tags.md#tag-restrictions").
6. Choose **Save**.

###### To delete a tag from an individual workgroup

1. Open the Athena console at [https://console.aws.amazon.com/athena/](https://console.aws.amazon.com/athena/home "https://console.aws.amazon.com/athena/home").
2. In the navigation pane, choose **Workgroups**.
3. Choose the workgroup that you want to modify.
4. Do one of the following:
   - Choose the **Tags** tab, and then choose
     **Manage tags**.
   - Choose **Edit**, and then scroll down to the
     **Tags** section.

5. In the list of tags, choose **Remove** for the tag that
   you want to delete, and then choose **Save**.
