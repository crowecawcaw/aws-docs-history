# Managing users and role assignments

On the **User management** page, you can manage AWS Partner Central users, role
assignments, and AWS Identity and Access Management (IAM) role mapping.

###### Topics

- [Managing role assignments](#assigning-roles "#assigning-roles")
- [Reassigning the alliance lead role](#reassigning-alliance-lead "#reassigning-alliance-lead")
- [Mapping users to IAM roles](#iam-roles-tab "#iam-roles-tab")
- [Removing users](#remove-users "#remove-users")
- [Managing your profile](#manage-profiles "#manage-profiles")

## Managing role assignments

On the **Users** tab of the **User management** page, you
can manage role assignments for up to 10 users at a time. For best practices regarding role
assignments, refer to [AWS Partner Central permissions best practices](permissions-best-practices.md "permissions-best-practices.md").

###### Note

These instructions do not apply to the reassignment of the alliance lead role. To reassign
the alliance lead role, refer to [Reassigning the alliance lead role](#reassigning-alliance-lead "#reassigning-alliance-lead").

###### To assign, reassign, or remove roles

1. Sign in to [AWS Partner Central](https://partnercentral.awspartner.com/APNLogin "https://partnercentral.awspartner.com/APNLogin") as a user with the alliance lead or alliance team role.
2. On the **My Company** menu, choose **User
   Management**.
3. On the **User management** page, choose the **Users**
   tab.
4. In user list, select the check box next to the user name of the user you want to manage.
   You can choose up to 10 users.
5. Choose **Manage roles**.
6. In the **Role assignments** section, each user you selected displays in
   its own row. For each user, the roles they currently have display below the
   **Role** field.
   - **To assign a new role to a user –** To the right of
     the user name, choose a role from the **Role(s)** dropdown list.
   - **To unassign a role –** To the right of the user
     name, below the **Role** field, choose the X icon of the role you want to
     remove.
   - **To configure roles for another user –** Choose
     **Manage another user**.
   - **To remove a user row from the current role-mapping group
     –** Choose **Remove**. This does not remove a user, and
     their role assignments will not change. To remove a user from AWS Partner Central, refer to [Removing users](#remove-users "#remove-users").

7. After completing role assignments, choose **Update**.

###### Note

After you choose **Update**, the number of successful and failed role
assignments display on the **User management** page. AWS Partner Central will not make
prohibited role assignments. For example, you cannot assign the alliance team role to more than
20 users. For more information, refer to [AWS Partner Central roles](role-summaries.md "role-summaries.md").

## Reassigning the alliance lead role

On the **User management** page, the alliance lead can reassign the role to
another user. Only one user can have the alliance lead role at a time.

###### To reassign the alliance lead role

1. Sign in to [AWS Partner Central](https://partnercentral.awspartner.com/APNLogin "https://partnercentral.awspartner.com/APNLogin") as a user with the alliance lead role.
2. On the **My Company** menu, choose **User
   Management**.
3. On the **User management** page, choose the **Users**
   tab.
4. In the first column of the user list, select the checkbox of the user you want to make the
   new alliance lead.
5. Choose **Reassign the alliance lead role**.
6. On the **alliance lead role management** page, choose the new alliance
   lead user.
7. Choose **Reassign**.
8. On the **Reassign alliance lead** dialog box, enter
   `confirm` and choose **Reassign**.

## Mapping users to IAM roles

On the **IAM roles** tab, you can grant single sign-on access to the AWS
Marketplace Management Portal (AMMP) to cloud admin and non-cloud admin partner users by
assigning them an IAM role.

### Prerequisites

You must complete the following before mapping users to IAM roles:

- Link your AWS Partner Central account to an AWS Marketplace account.
- In the IAM console, a cloud admin user creates IAM roles with Marketplace
  permissions.

For more information, refer to [Linking AWS Partner Central and AWS accounts](account-linking.md "account-linking.md").

###### To map users to IAM roles

1. Sign in to [AWS Partner Central](https://partnercentral.awspartner.com/APNLogin "https://partnercentral.awspartner.com/APNLogin") as a user with the alliance lead or alliance team role.
2. On the **My Company** menu, choose **User
   Management**.
3. On the **User management** page, choose the **IAM
   roles** tab.
4. To map cloud admin users:
   1. Choose one or more users from the **Cloud admin users** list. This list
      contains users assigned the cloud admin role that need an IAM role assignment to have AWS
      Marketplace permissions.
   2. Choose **Map to IAM role**.

5. To map non-cloud admin partner users:
   1. Choose one or more users from the **Available partner users** list.
      This list contains users that do not have the cloud admin role but need an IAM role
      assignment to have AWS Marketplace permissions.
   2. Choose **Map to IAM role**.

## Removing users

Removing a user permanently revokes that user's access to AWS Partner Central and cannot be undone. To
restore a removed user, you must reinvite them to register. AWS Partner Central stores data for removed
users.

###### Important

Before removing the user with the alliance lead role, reassign the role to another user.
Refer to [Reassigning the alliance lead role](#reassigning-alliance-lead "#reassigning-alliance-lead").

###### To remove a user

1. Sign in to [AWS Partner Central](https://partnercentral.awspartner.com/APNLogin "https://partnercentral.awspartner.com/APNLogin") as a user with the alliance lead or alliance team role.
2. On the **My Company** menu, choose **User
   Management**.
3. On the **User management** page, choose the **Users**
   tab.
4. In the user list, select the checkboxes next to the users you want to remove. You can
   remove 10 users at a time.
5. Choose **Remove user**.
6. In the **Remove user** dialog box, enter `confirm`
   and choose **Remove**.

## Managing your profile

You can change your profile data, except for your contact type, user role, or email address.

###### To change your profile

1. Sign in to [AWS Partner Central](https://partnercentral.awspartner.com/APNLogin "https://partnercentral.awspartner.com/APNLogin").
2. Navigate to the **My profile** menu and select the **My profile** tab.
3. Choose **Edit**.
4. Update your information and choose **Save**.

###### Note

If you need to update your contact type, submit an [AWS Partner support case](https://partnercentral.awspartner.com/partnercentral2/s/support "https://partnercentral.awspartner.com/partnercentral2/s/support").
