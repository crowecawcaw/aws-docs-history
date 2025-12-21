# Change requests in AWS Clean Rooms

Change requests allow you to propose changes to existing collaboration settings for approval by other collaboration members. With change requests, you can submit a request to add new members, update existing member abilities, and modify collaboration auto-approval settings. All collaboration members must approve change requests for the proposed changes to take effect.

Change requests are collaboration-specific and can be submitted by the collaboration creator.

You can submit a change request in the following ways:

- Add a new member to a collaboration
- Update existing member abilities
- Edit collaboration auto-approval settings

###### Note

You must be the collaboration creator to submit a change request.

## Add a new member to a collaboration

To add a new member to a collaboration, you must be the collaboration creator. Adding a new member to a collaboration requires manual approval from existing collaboration members, and will submit a change request.

You can add new members to a collaboration by following these steps:

###### To add a new member to a collaboration

1. Sign in to the AWS Management Console and open the [AWS Clean Rooms console](https://console.aws.amazon.com/cleanrooms/home "https://console.aws.amazon.com/cleanrooms/home") with your member AWS account.
2. In the left navigation pane, choose **Collaborations**.
3. Select your collaboration to navigate to your collaboration details.
4. On the collaboration page, navigate to the **Members** tab.
5. In the Members table, select **Edit members**.
6. Choose **Add another member**.
7. Input the new member information:
   - Member display name
   - Member AWS account ID
   - Specify whether the member can receive results. Check the box to grant this member ability.

8. Choose **Save changes**.
9. Confirm your change request submission. In the confirmation modal, confirm the changes and select **Submit change request**.

###### Note

If auto-approved change types are supported in your collaboration, manual approval of change requests may not be required. You can review which change types do not require a change request in the "Overview" section of the collaboration. For more information, see [Edit collaboration auto-approval settings](#edit-auto-approval-settings "#edit-auto-approval-settings").

## Update existing member abilities

To update existing collaboration member abilities, you must be the collaboration creator. Updating abilities for existing collaboration members requires manual approval from existing members, and will submit a change request.

The member abilities that can be updated are:

- Can receive results

You can update the member abilities for existing collaboration members by following these steps:

###### To update existing member abilities

1. Sign in to the AWS Management Console and open the [AWS Clean Rooms console](https://console.aws.amazon.com/cleanrooms/home "https://console.aws.amazon.com/cleanrooms/home") with your member AWS account.
2. In the left navigation pane, choose **Collaborations**.
3. Select your collaboration to navigate to your collaboration details.
4. On the collaboration page, navigate to the **Members** tab.
5. In the Members table, select **Edit members**.
6. Specify the member ability to change.
7. Choose **Save changes**.
8. Confirm your change request submission. In the confirmation modal, confirm the changes and select **Submit change request**.

###### Note

If auto-approved change types are supported in your collaboration, manual approval of change requests may not be required. You can review which change types do not require a change request in the "Overview" section of the collaboration. For more information, see [Edit collaboration auto-approval settings](#edit-auto-approval-settings "#edit-auto-approval-settings").

## Edit collaboration auto-approval settings

To edit the collaboration settings for auto-approvals, you must be the collaboration creator and submit a change request for approval by other collaboration members.

You can edit the auto-approval settings for a collaboration by following these steps:

###### To edit collaboration auto-approval settings

1. Sign in to the AWS Management Console and open the [AWS Clean Rooms console](https://console.aws.amazon.com/cleanrooms/home "https://console.aws.amazon.com/cleanrooms/home") with your member AWS account.
2. In the left navigation pane, choose **Collaborations**.
3. Select your collaboration to navigate to your collaboration details.
4. On the collaboration page, choose the **Actions** button and select **Edit auto approvals**.
5. **To grant member abilities to existing members without manually approving a change request:**
   1. Navigate to the **Grant member abilities** section.
   2. Specify which member abilities can be automatically granted.

   ###### Note

   By default, all collaboration members can "Contribute data". 3. (Optional) To allow new members to instantly join a collaboration with the specified abilities without manually approving change requests, select **Auto-approve new members with these abilities**.

6. **To allow removal of abilities from existing members without a change request:**
   1. Navigate to the **Abilities that can be automatically revoked** section.
   2. Specify which member abilities can be automatically removed.

7. Choose **Save changes**.
8. Confirm your change request submission. In the confirmation modal, confirm the changes and select **Submit change request**.
