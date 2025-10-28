# Controlling access to

AWS Marketplace Management Portal

AWS Identity and Access Management (IAM) is an AWS service that helps you control access to AWS resources. If
you are an administrator, you control who can be _authenticated_ (signed in) and _authorized_ (have
permissions) to use AWS Marketplace resources. IAM is an AWS service that you can use with no
additional charge.

The recommended way to control who can do what in AWS Marketplace Management Portal is to use IAM to create users
and groups. Then you add the users to the groups, and manage the groups. For example, if John
should be allowed to view your products, create a user for him and add his user to a group you
create for read-only access. You can assign a policy or permissions to the group that provide
read-only permissions. If you have other users that need read-only access, you can add them to
the group you created rather than adding permissions to the user. If John's role changes and he
no longer needs read-only access, you can remove John from the group.

A _policy_ is a document that defines the permissions that apply to a
user, group, or role. In turn, the permissions determine what users can do in AWS. A policy
typically allows access to specific actions, and can optionally grant that the actions are
allowed for specific resources, like Amazon EC2 instances, Amazon S3 buckets, and so on. Policies can also
explicitly deny access. A _permission_ is a statement within a policy that
allows or denies access to a particular resource. You can state any permission like this: "A has
permission to do B to C." For example, Jane (A) has permission to read messages (B) from John's
Amazon Simple Queue Service queue (C). Whenever Jane sends a request to Amazon SQS to use John's queue, the service
checks to see if she has permission. It further checks to see if the request satisfies the
conditions John specified in the permission.

###### Important

All of the users that you create authenticate by using their credentials. However, they
use the same AWS account. Any change that a user makes can impact the whole account.

AWS Marketplace has permissions defined to control the actions that someone with those permissions
can take in AWS Marketplace Management Portal. There are also policies that AWS Marketplace created and manage that combine
several permissions.

The following resources provide more information about getting started and using IAM.

- [Create an administrative
  user](../../../IAM/latest/UserGuide/getting-started_create-admin-group.md "../../../IAM/latest/UserGuide/getting-started_create-admin-group.md")
- [Security best practices in IAM](../../../IAM/latest/UserGuide/best-practices.md "../../../IAM/latest/UserGuide/best-practices.md")
- [Managing IAM policies](../../../IAM/latest/UserGuide/access_policies_managed-using.md#create-managed-policy-console "../../../IAM/latest/UserGuide/access_policies_managed-using.md#create-managed-policy-console")
- [Attaching a policy to an
  IAM user group](../../../IAM/latest/UserGuide/id_groups_manage_attach-policy.md "../../../IAM/latest/UserGuide/id_groups_manage_attach-policy.md")
- [IAM Identities (users, groups, and roles)](../../../IAM/latest/UserGuide/id.md "../../../IAM/latest/UserGuide/id.md")
- [Controlling access to AWS resources
  using policies](../../../IAM/latest/UserGuide/access_permissions.md "../../../IAM/latest/UserGuide/access_permissions.md")
  The following topics provide some high-level guidance for creating users and groups, and
  signing in as an user.

###### Topics

- [Creating users](#creating-iam-users "#creating-iam-users")
- [Creating or using groups](#creating-iam-groups "#creating-iam-groups")
- [Signing in as a user](#signing-in-using-iam-user "#signing-in-using-iam-user")

## Creating users

To allow people in your company to sign in to the AWS Marketplace Management Portal, create a user for each person
who needs access.

###### To create users

1. Sign in to the AWS Management Console and open the IAM console at [https://console.aws.amazon.com/iam/](https://console.aws.amazon.com/iam/ "https://console.aws.amazon.com/iam/").
2. In the navigation pane, under **Access management**, choose **Users**, then choose
   **Create user**.
3. In the numbered text boxes, enter a name for each user that you want to create.
4. Clear the **Generate an access key for each user** check box and
   then choose **Create**.

###### To assign a password to each user that you just created

1. In the list of users, choose the name of a new user.
2. Choose the **Security Credentials** tab and then choose
   **Manage Password**.
3. Choose an option for either an auto-generated password or a custom password.
   Optionally, to require the user to choose a new password at the next sign-in, select
   the box for **Require user to create a new password at next sign-in**.
   Choose **Apply**.
4. Choose **Download Credentials** to save the sign-in credentials and
   account-specific sign-in URL to a comma-separated values (CSV) file on your computer.
   Then choose **Close**.

###### Note

To sign in with the sign-in credentials that you just created, users must
navigate to your account-specific sign-in URL. This URL is in the credentials file that you
just downloaded and is also available on the IAM console. For more information, see
[How IAM users sign in to
your AWS account](../../../IAM/latest/UserGuide/id_users_sign-in.md "../../../IAM/latest/UserGuide/id_users_sign-in.md") in the _IAM User Guide_.

###### Tip

Create sign-in credentials for yourself as well, even though you're the AWS account
owner. It's a recommended best practice for everyone to work in AWS Marketplace
as a user, even the account owner. For instructions on how to create a user for
yourself that has administrative permissions, see
[Create an
administrative user](../../../IAM/latest/UserGuide/getting-started_create-admin-group.md "../../../IAM/latest/UserGuide/getting-started_create-admin-group.md") in the _IAM User Guide_.

## Creating or using groups

After you create users, create groups, create permissions to access the pages in the
AWS Marketplace Management Portal, add those permissions to the groups, and then add users to the groups.

When you assign permissions to a group, you allow any member of that group to perform
specific actions. When you add a new user to the group, that user automatically gains the
permissions that are assigned to the group. A group can have permissions for more than one
action. We recommend using an [AWS Marketplace managed
policy](security-iam-awsmanpol.md "security-iam-awsmanpol.md") rather than creating your own policy.

###### To assign a managed policy for AWS Marketplace to a group

1. Open the IAM console at
   [https://console.aws.amazon.com/iam/](https://console.aws.amazon.com/iam/ "https://console.aws.amazon.com/iam/").
2. In the navigation pane, choose **Groups**, and then choose the group
   that you want to attach a policy to.
3. On the summary page for the group, under the **Permissions** tab,
   choose **Attach Policy**.
4. On the **Attach Policy** page, next to **Filter:**
   enter **awsmarketplace**.
5. Choose the policy or policies that you want to attach, and then choose
   **Attach Policy**.

###### To create a policy with AWS Marketplace Management Portal permissions

1. Open the IAM console at
   [https://console.aws.amazon.com/iam/](https://console.aws.amazon.com/iam/ "https://console.aws.amazon.com/iam/").
2. In the navigation pane, choose **Policies** and then choose
   **Create Policy**.
3. Next to **Policy Generator**, choose **Select**.
4. On the **Edit Permissions** page, do the following:
   1. For **Effect**, choose **Allow**.
   2. For **AWS Service**, choose
      **AWS Marketplace Management Portal**.
   3. For **Actions**, select the permission or permissions to
      allow.
   4. Choose **Add Statement**.
   5. Choose **Next Step**.

5. On the **Review Policy** page, do the following:
   1. For **Policy Name**, enter a name for this policy. Take note of
      the policy name because you need it for a later step.
   2. (Optional) For **Description**, enter a description for this
      policy.
   3. Choose **Create Policy**.

###### To create an IAM group with appropriate permissions and add users to the

group

1. Open the IAM console at
   [https://console.aws.amazon.com/iam/](https://console.aws.amazon.com/iam/ "https://console.aws.amazon.com/iam/").
2. In the navigation pane, choose **Groups** and then choose
   **Create New Group**.
3. For **Group Name:**, type a name for the group. Then choose
   **Next Step**.
4. On the **Attach Policy** page, do the following:
   1. For **Filter:**, choose **Customer Managed
      Policies**.
   2. Select the check box next to the name of the policy that you want to attach to
      this group. This is typically the policy that you just created.
   3. Choose **Next Step**.

5. Choose **Create Group**.
6. Find your new group in the **Groups** list and then select the check
   box next to it. Choose **Group Actions** and then **Add Users to
   Group**.
7. Select the check box next to each user to add to the group and then choose
   **Add Users**.

## Signing in as a user

After you have created users in IAM, users can sign in with their own sign-in
credentials. To do so, they need to use the unique URL that is associated with your
AWS account. You can get and distribute the sign-in URL to your users.

###### To get your account's unique sign-in URL

1. Open the IAM console at
   [https://console.aws.amazon.com/iam/](https://console.aws.amazon.com/iam/ "https://console.aws.amazon.com/iam/").
2. In the navigation pane, choose **Dashboard**.
3. Near the top of the content pane, find **IAM users sign-in link:** and take note of the sign-in link, which has a format like this:

```
 https://AWS_account_ID.signin.aws.amazon.com/console/
```

###### Note

If you want the URL for your sign-in page to contain your company name (or other
friendly identifier) instead of your AWS account ID, you can create an alias for your
account by choosing **Customize**. For more information, see
[Your AWS Account ID and Its
Alias](../../../IAM/latest/UserGuide/console_account-alias.md "../../../IAM/latest/UserGuide/console_account-alias.md") in the _IAM User Guide_. 4. Distribute this URL to the people at your company who can work with AWS Marketplace,
along with the sign-in credentials that you created for each. Instruct them to use your
account's unique sign-in URL to sign in before they access AWS Marketplace.
