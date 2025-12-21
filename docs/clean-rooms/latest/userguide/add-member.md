# Adding members to a collaboration

**Prerequisites**

- An AWS account with permissions to manage collaborations
- The AWS account IDs of members you want to add

###### To add a member to a collaboration

1. Sign in to the AWS Management Console and open the [AWS Clean Rooms console](https://console.aws.amazon.com/cleanrooms/home "https://console.aws.amazon.com/cleanrooms/home").
2. In the left navigation pane, choose **Collaborations**.
3. Select the collaboration you want to add members to.
4. Choose the **Members** tab.
5. Choose **Edit members**.
6. Choose **Add another member** and enter the following
   information:
   - **Member display name**
   - **Member AWS account ID**
   - Specify whether they **can receive results**

7. Choose **Save changes**.
8. In the confirmation modal, verify that the information is correct, and choose
   **Submit change request**.
   - If the change request requires other members' approval, all existing members
     must approve the change request before the new member is added. For more
     information on change requests, see [Change requests in AWS Clean Rooms](change-requests.md "change-requests.md").
   - If auto-approval change types are supported for new members with the
     specified abilities, then this change will take effect immediately. For more
     information, see [Edit collaboration auto-approval settings](change-requests.md#edit-auto-approval-settings "change-requests.md#edit-auto-approval-settings").

9. On the collaboration detail page, under the **Members** tab,
   verify that the **Member status** of the added member(s) displays
   as **Invited**.
   After completing these steps, the invited members can join the collaboration. For more
   information about joining a collaboration, see [Creating a membership and joining a
   collaboration](create-membership.md "create-membership.md")
