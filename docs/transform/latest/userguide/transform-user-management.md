

# Managing users
<a name="transform-user-management"></a>

How you manage user access to AWS Transform depends on the access model you chose during setup. If you configured IAM Identity Center, you add users through IAM Identity Center. If you configured a third-party identity provider, you manage users in that provider. If you chose IAM-only access, user access is managed through IAM policies.

## Adding users in IAM Identity Center
<a name="transform-add-idc-users"></a>

To add users in IAM Identity Center:

1. Navigate to the IAM Identity Center console.

1. In the navigation pane, choose **Users**.

1. Choose **Add user**.

1. Enter the required information:
   + **Username** - A unique identifier for the user (cannot be changed later)
   + **Email address** - The user's email address
   + **First name** and **Last name** - The user's name
   + **Display name** - The name that appears in the user list

1. For **Password**, choose how the user receives their password:
   + **Send an email** - Send setup instructions via email
   + **Generate a one-time password** - Create a password to share manually

1. Choose **Next** to review the user information.

1. Review the details and choose **Add user**.

After the user is added, they'll receive an email invitation to set up their IAM Identity Center account. The invitation link is valid for 7 days.

You can also learn about working with IAM Identity Center and AWS Transform in this video:

[![AWS Videos](http://img.youtube.com/vi/NesMt5cgT0s/0.jpg)](http://www.youtube.com/watch?v=NesMt5cgT0s)


## Adding users to AWS Transform
<a name="transform-add-transform-users"></a>

After adding users to IAM Identity Center, you can grant them access to AWS Transform:

1. Return to the AWS Transform console.

1. In the navigation pane, choose **Users and groups**.

1. Select the **Users** tab or the **Groups** tab.

1. Search for and select the users or groups that you want to add from IAM Identity Center.

1. Choose **Assign users and groups** to grant the selected users or groups access to AWS Transform.

After adding users, they appear in the **Users** list with a status of "Pending" until they accept the invitation and sign in.

## Managing users with IAM-only access
<a name="transform-manage-iam-users"></a>

If you configured AWS Transform with IAM-only access, user access is managed through IAM policies. Any IAM principal with the `transform:AccessTransformProfile` permission on the profile resource can access AWS Transform.

To grant a user or role access to AWS Transform:

1. Navigate to the IAM console.

1. Attach a policy that includes the `transform:AccessTransformProfile` action to the IAM user or role. For an example policy, see [Allow users to access AWS Transform with IAM credentials](security_iam_id-based-policy-examples.md#id-based-policy-examples-access-transform-webapp).

To revoke access, remove the policy from the IAM user or role.