# Remove organization policies

###### Warning

We're currently releasing our new experience to a limited number of customers. You might not be able to access this experience yet.

After you've activated advanced features, you can modify the Resource Control Policies
(RCPs) and Service Control Policies (SCPs) to change the governance of your AWS organization.
Certain AWS managed organizational policies are removed when you activate advanced features.
For more information, see [Managed policies for your organization](scps-and-rcps-for-projects.md "scps-and-rcps-for-projects.md"). The following information is only for AWS
organizations that use AWS Builder ID as the identity source. If you use another source,
follow the steps in [Updating a
policy](../../../organizations/latest/userguide/orgs_policies_update.md "../../../organizations/latest/userguide/orgs_policies_update.md").

###### To modify a service control policy (SCP)

1. Open AWS Settings at [https://settings.aws.com](https://settings.aws.com "https://settings.aws.com").
2. In the main navigation pane, choose **Projects**.
3. In **Manage this organization**, choose **Manage
   policies**.

This will open the AWS Organizations console. This is a
task that requires root-level permission. 4. Choose the **Service control policy** page. 5. Choose the name of the policy that you want to update. 6. On the policy's detail page, choose **Edit policy**. 7. Make any or all of the following changes:

    * You can rename the policy by entering a new name in **Policy
     name**.
    * You can change the description by entering new text in **Policy
     description**.
    * You can edit the policy text by editing the policy in JSON format in the left pane.
     Alternatively, you can choose a statement in the editor on the right, and also alter
     its elements by using the controls. For more details about each control, see the
     Creating an SCP procedure earlier in this topic.

8. When you're finished, choose **Save changes**.

###### To modify a resource control policy (RCP)

1. Open AWS Settings at [https://settings.aws.com](https://settings.aws.com "https://settings.aws.com").
2. In the main navigation pane, choose **Projects**.
3. In **Manage this organization**, choose **Manage
   policies**.

This will open the AWS Organizations console. This is a
task that requires root-level permission. 4. Choose the **Resource control policy** page. 5. Choose the name of the policy that you want to update. 6. On the policy's detail page, choose **Edit policy**. 7. Make any or all of the following changes:

    * You can rename the policy by entering a new name in **Policy
     name**.
    * You can change the description by entering new text in **Policy
     description**.
    * You can edit the policy text by editing the policy in JSON format in the left pane.
     Alternatively, you can choose a statement in the editor on the right, and also alter
     its elements by using the controls. For more details about each control, see the
     Creating an RCP procedure earlier in this topic.

8. When you're finished, choose **Save changes**.
These steps show you how to modify organization policies by AWS Settings. However, you
can sign into the AWS Management Console with your management account and access the AWS Organizations
console to modify these policies.
