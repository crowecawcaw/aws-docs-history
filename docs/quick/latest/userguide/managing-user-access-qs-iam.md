

# Managing access for AWS Quick and IAM users

AWS Quick account administrators can use this topic to learn more about managing accounts that use IAM or Quick for identity federation.

To manage Quick users, you must have administrative privileges in Quick and also the appropriate AWS permissions. For more information about the necessary AWS permissions, see [IAM policy examples for Quick](https://docs.aws.amazon.com/quicksight/latest/user/iam-policy-examples.html).

Each Quick Enterprise edition account can have an unlimited number of users. User names that contain a semicolon (`;` ) aren't supported.

Use the topics below to learn more about managing access for Quick and IAM users.

**Topics**
+ [Inviting users to access AWS Quick](#inviting-users)
+ [Viewing AWS Quick account details](#view-user-accounts)
+ [Deleting a AWS Quick user account](#delete-a-user-account)

## Inviting users to access AWS Quick
<a name="inviting-users"></a>


|  | 
| --- |
|    Applies to: Enterprise Edition and Standard Edition  | 


|  | 
| --- |
|    Intended audience:  AWS Quick administrators  | 

Use the following procedure to invite a user to access Quick.

1. Choose your user name on the application bar and then choose **Manage Quick**.

1. Choose **Manage Users**. On this screen, you can manage users who already exist in your account.

1. Choose **Invite users**.

1. In the **Invite users to this account** table, enter a new user name for a person to whom you want to grant access to Quick. If the user is an IAM user, enter their IAM username. Then press **\+**. A user's IAM username can be the same as their email address.

   Repeat this step until you have entered everyone who you want to invite. Then go to the next step to enter details.

1. For **Email**, enter an email address for the account. 
**Note**  
Currently, email addresses are case-sensitive. Email distribution lists are not supported for inviting users. Instead, send individual invitations to each user. To share assets like dashboards, datasets, and agents with multiple users, create user groups in Quick.

1. For **Role**, choose the role to assign to each person you're inviting. A *role *determines the permission level to grant to that account.
   + **ADMIN roles**:
     + **ADMIN** – The user is able to both use AWS Quick for authoring and for performing administrative tasks like managing users or purchasing [SPICE](https://docs.aws.amazon.com/quicksight/latest/user/spice.html) capacity.
     + **ADMIN PRO** – The user is able to perform all actions of a AWS Quick Admin and utilize applicable AWS Quick Generative BI capabilities. For more information about Pro roles in AWS Quick, see [Get started with Generative BI](https://docs.aws.amazon.com/quicksight/latest/user/generative-bi-get-started.html).

     There are some differences in the administrative tasks that IAM users and AWS Quick administrators can perform. These differences occur because some administrative tasks require permissions in AWS, which AWS Quick–only users lack. The differences are these:
     + AWS Quick administrators can manage users, SPICE capacity, and subscriptions. 
     + IAM users with administrative permissions can also manage users, SPICE capacity, and subscriptions. In addition, they can manage AWS Quick permissions to AWS resources, upgrade to Enterprise edition, and unsubscribe from AWS Quick.

     If you want to create a user with administrator permissions with IAM access, check with your AWS administrator. Make sure that the IAM user has the all necessary statements in their IAM permissions policy to work with AWS Quick resources. For more information about what statements are required, see [IAM policy examples for AWS Quick](https://docs.aws.amazon.com/quicksight/latest/user/iam-policy-examples.html).
   + **AUTHOR roles**:
     + **AUTHOR**– The user is able to author analyses and dashboards in AWS Quick but not perform any administrative tasks in AWS Quick.
     + **AUTHOR PRO**– The user is able to perform all actions of a AWS Quick Author and utilize applicable AWS Quick Generative BI capabilities. For more information about Pro roles in AWS Quick, see [Get started with Generative BI](https://docs.aws.amazon.com/quicksight/latest/user/generative-bi-get-started.html).
   + **READER roles (Enterprise only)**:
     + **READER**– Users are able to interact with shared dashboards, but not author analyses or dashboards or perform any administrative tasks.
     + **READER PRO**– The user is able to perform all actions of a AWS Quick Reader and utilize applicable AWS Quick Generative BI capabilities. For more information about Pro roles in AWS Quick, see [Get started with Generative BI](https://docs.aws.amazon.com/quicksight/latest/user/generative-bi-get-started.html).

1. For **IAM User**, verify that it says **Yes** for accounts that are associated with IAM users, and **No** for those that are AWS Quick-only.

1. (Optional) To delete a user, choose the delete icon at the end of the relevant row.

1. Choose **Invite**.

## Viewing AWS Quick account details
<a name="view-user-accounts"></a>


|  | 
| --- |
|    Intended audience:  AWS Quick administrators  | 

You can view AWS Quick accounts on the **Manage Users** page. To view a AWS Quick user account, use the following procedure. 

1. Choose your user name on the application bar and then choose **Manage Quick**.

1. Choose **Manage Users** to view details about people who are AWS Quick users. The information that displays includes:
   + Username – The person's user name.
   + Email – The email associated with this user name.
   + Role – The security cohort that the person's user name belongs to: **ADMIN**, **ADMIN PRO**, **AUTHOR**, **AUTHOR PRO**, **READER**, or **READER PRO**.
   + Last active – The last date and time that this person accessed the AWS Quick console. Anyone who isn't an active user has a **Last active** status of `User has no activity`.

   You can also see deleted or inactive users in this screen.

1. To find a user name, enter a part or all of a user's name or email the search box. Search is case-insensitive and wildcards aren't supported. To clear the search results and view all user names, delete your search entry.

## Deleting a AWS Quick user account
<a name="delete-a-user-account"></a>


|  | 
| --- |
|    Intended audience:  AWS Quick administrators  | 

**Warning**  
**Deleting user accounts has permanent, organization-wide consequences.** When you delete a user account:  
Assets owned solely by the user are permanently removed unless you transfer them to another user before deletion.
Assets that have other owners remain available to those owners; the deleted user is removed from their permissions.
**This action cannot be undone – deleted resources cannot be recovered.**
Always transfer critical resources to another user before deleting an account. Review all user-owned assets using the asset management console before proceeding with any account deletion.

For the full model of how user removal affects assets and data, see [User lifecycle and data handling in AWS Quick](user-lifecycle-data-handling.md).

Accounts can be deleted by either an AWS administrator or an AWS Quick administrator. Deleting a AWS Quick user account works the same in both the Standard and Enterprise editions of AWS Quick. 

Deleting a AWS Quick user account removes or transfers their resources. In Enterprise edition, the network administrator can temporarily deactivate a AWS Quick user account by removing it from the network group that has access to AWS Quick. If a user is deleted, but not deactivated, that user can still access AWS Quick as a new user. For more information about deactivating an Enterprise account, see [Deactivating user accounts](https://docs.aws.amazon.com/quicksight/latest/user/deactivate-user-groups-enterprise.html).

Use the following procedure to delete a AWS Quick user account. 

1. Choose your user name on the application bar and then choose **Manage Quick**.

1. Choose **Manage Users**.

1. Locate the account you want to delete and then choose the delete icon at the end of that row.

1. Choose to either delete or transfer any resources owned by the user and then choose **OK**.

1. Do one of the following:
   + If you chose to transfer user resources, enter the user name of the account to transfer them to and then choose **Delete and transfer resources**.
   + If you chose to delete user resources, choose **Delete**. You can't undo this action.