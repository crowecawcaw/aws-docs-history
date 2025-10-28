# Managing shared access to custom

billing views in your organization

###### Note

Custom billing views use AWS Resource Access Manager (AWS RAM) for sharing. When you
share a custom billing view, an AWS resource share is automatically created. You can also
directly modify the resource share from the AWS RAM console. For more information about
modifying the resource share in AWS RAM, see [Update a
resource share in AWS RAM](../../../ram/latest/userguide/working-with-sharing-update.md "../../../ram/latest/userguide/working-with-sharing-update.md").

###### To edit who can access a custom billing view in your organization

1. Open the Billing and Cost Management console at [https://console.aws.amazon.com/costmanagement/](https://console.aws.amazon.com/costmanagement/ "https://console.aws.amazon.com/costmanagement/").
2. In the navigation pane, choose **Cost Management
   Preferences**.
3. Choose the **Billing View** tab.
4. To access the sharing page, do one of the following:
   - Select the custom billing view whose sharing you want to update, choose
     **Actions**, and then choose **Edit shared
     accounts** from the dropdown list.
   - Choose the name of the custom billing view whose sharing you want to update and,
     on the view details page, choose the **Sharing** tab.

5. In the **Sharing** tab, choose **Edit**.
6. Choose which member accounts in your organization should have access to the custom
   billing view.
7. Choose **Share**.

###### Note

AWS RAM also supports a single resource belonging to multiple resource shares. If a
custom billing view belongs to multiple resource shares, you will see a drop-down within the
Edit sharing page labeled Select a share listing all resource shares the currently selected
custom billing view belongs to. By selecting a resource share, you will be able to modify
which accounts should be included or excluded from the selected resource share.
