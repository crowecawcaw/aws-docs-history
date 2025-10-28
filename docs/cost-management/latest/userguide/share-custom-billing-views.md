# Sharing custom billing views

You can share custom billing views with accounts within and outside your organization. Sharing is
not supported for billing views of type “Primary” or “Billing group”.

###### Note

For member accounts within an organization to access a shared custom billing view using
Cost Explorer, the management account must have granted them access to Cost Explorer. Member
account access to discounts, credits, and refunds when accessing a shared custom billing view
is determined by current Cost Explorer preferences, including Linked Account Access, Linked
Account Refunds and Credits, and Linked Account Discounts. For more information, see [Controlling access using Cost Explorer preferences](ce-access.md#ce-controlling-access "ce-access.md#ce-controlling-access").

###### To share a custom billing view

1. Open the Billing and Cost Management console at [https://console.aws.amazon.com/costmanagement/](https://console.aws.amazon.com/costmanagement/ "https://console.aws.amazon.com/costmanagement/").
2. In the navigation pane, choose **Cost Management Preferences**.
3. Choose the **Billing View** tab.
4. To access the sharing page, do one of the following:
   - Select the custom billing view you want to share, and choose **Share
     view**.
   - Choose the name of the custom billing view you want to share and, on the view
     details page, choose the **Sharing** tab.

5. Choose **Share**.
6. You can share custom billing views with accounts within and outside of your
   organization. From **Select**:
   - Choose **Within AWS organization** to share with accounts within your
     organization.
   - Choose **With any account** to manually enter an account ID to
     share with.

7. Select a managed permission for the custom billing view. Managed permissions define how
   recipient accounts can interact with the shared resource. For more information about managed
   permissions, see [Managing permissions in AWS RAM](../../../ram/latest/userguide/security-ram-permissions.md "../../../ram/latest/userguide/security-ram-permissions.md").
8. Select which accounts you want to share the custom billing view.
   - If sharing **Within AWS organization**, select member
     accounts to share with.
   - If sharing **With any account**, manually enter the
     12-digit AWS account ID you want to share with. If sharing with an account outside your
     organization, the recipient must accept the invitation to access the view.

9. Select the member accounts in your organization that you want to share the custom
   billing view with.
10. Choose **Share**.

###### Note

Custom billing views use AWS Resource Access Manager (AWS RAM) for sharing. When you
share a custom billing view, an AWS resource share is automatically created. You can
directly share custom billing view resources with specific accounts in your organization using
AWS RAM. Only the management account needs permissions to share resources with AWS RAM,
with no permissions required for member accounts receiving a shared resource.

For more advanced use cases such as sharing with an entire AWS Organizational Unit or
defining custom managed policies, create a resource share directly through AWS RAM. When a
custom billing view has been shared with IAM principals, other than an AWS account,
directly through AWS RAM, these shares are displayed under **Other principals shared
with** in the **Sharing** tab on the view details page. Resource
shares created directly through AWS RAM can only be managed in AWS RAM.

Once a custom billing view is shared, you can see which accounts have access to it from the
**Sharing** tab on the view details page. Note that if you're using AWS
Billing Conductor, a custom billing view contains cost management data based on your standard
AWS bill, even when being accessed by an account belonging to a billing group. Additionally,
you can view a list of all resource shares you’ve created in AWS RAM. For more information,
see [Viewing resource shares you created in AWS RAM](../../../ram/latest/userguide/working-with-sharing-view-rs.md "../../../ram/latest/userguide/working-with-sharing-view-rs.md").

You have the flexibility to edit the sharing permissions of a custom billing view at any
time, allowing you to maintain control over who has access to your cost management data. For
details, see [Managing shared access to custom billing views](manage-shared-access-custom-billing-views.md "manage-shared-access-custom-billing-views.md").
