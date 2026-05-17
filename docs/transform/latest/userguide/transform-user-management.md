# Managing users

How you manage user access to AWS Transform depends on the access model you chose during setup.
If you configured IAM Identity Center, you add users through IAM Identity Center. If you configured a third-party identity
provider, you manage users in that provider. If you chose IAM-only access, user access is managed
through IAM policies.

## Adding users in IAM Identity Center

To add users in IAM Identity Center:

1. Navigate to the IAM Identity Center console.
2. In the navigation pane, choose **Users**.
3. Choose **Add user**.
4. Enter the required information:
   - **Username** - A unique identifier for the user (cannot be changed later)
   - **Email address** - The user's email address
   - **First name** and **Last name** - The user's name
   - **Display name** - The name that appears in the user list

5. For **Password**, choose how the user receives their password:
   - **Send an email** - Send setup instructions via email
   - **Generate a one-time password** - Create a password to share manually

6. Choose **Next** to review the user information.
7. Review the details and choose **Add user**.

After the user is added, they'll receive an email invitation to set up their IAM Identity Center account. The invitation link is valid for 7 days.

You can also learn about working with IAM Identity Center and AWS Transform in this video:

## Adding users to AWS Transform

After adding users to IAM Identity Center, you can grant them access to AWS Transform:

1. Return to the AWS Transform console.
2. In the navigation pane, choose **Users and groups**.
3. Select the **Users** tab or the **Groups** tab.
4. Search for and select the users or groups that you want to add from IAM Identity Center.
5. Choose **Assign users and groups** to grant the selected users or groups access to AWS Transform.

After adding users, they appear in the **Users** list with a status of "Pending" until they accept the invitation and sign in.

## Managing users with IAM-only access

If you configured AWS Transform with IAM-only access, user access is managed through IAM
policies. Any IAM principal with the `transform:AccessTransformProfile` permission
on the profile resource can access AWS Transform.

To grant a user or role access to AWS Transform:

1. Navigate to the IAM console.
2. Attach a policy that includes the `transform:AccessTransformProfile` action
   to the IAM user or role. For an example policy, see [Allow users to access AWS Transform
   with IAM credentials](security_iam_id-based-policy-examples.md#id-based-policy-examples-access-transform-webapp "security_iam_id-based-policy-examples.md#id-based-policy-examples-access-transform-webapp").

To revoke access, remove the policy from the IAM user or role.
