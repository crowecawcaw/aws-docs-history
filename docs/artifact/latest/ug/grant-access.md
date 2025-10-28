# Granting user access to AWS Artifact

Complete the following steps to grant users permissions to AWS Artifact based on the
level of access they need.

###### Tasks

- [Step 1: Create an IAM policy](#create-iam-policy "#create-iam-policy")
- [Step 2: Create an IAM group and attach the policy](#create-iam-group "#create-iam-group")
- [Step 3: Create IAM users and add them to the group](#create-iam-user "#create-iam-user")

## Step 1: Create an IAM policy

As an IAM administrator, you can create a policy that grants permissions
to AWS Artifact actions and resources.

###### To create an IAM policy

Use the following procedure to create an IAM policy that you can use
to grant permissions to your IAM users and groups.

1. Open the IAM console at
   [https://console.aws.amazon.com/iam/](https://console.aws.amazon.com/iam/ "https://console.aws.amazon.com/iam/").
2. In the navigation pane, choose
   **Policies**.
3. Choose
   **Create policy**.
4. Choose the
   **JSON** tab.
5. Enter a policy document. You can create you own policy, or you can
   use one of the policies from
   [Example IAM policies for AWS Artifact in commercial AWS Regions](example-iam-policies.md "example-iam-policies.md").
6. Choose
   **Review Policy**. The policy validator
   reports any syntax errors.
7. On the
   **Review policy** page, enter a unique name
   that helps you remember the purpose of the policy. You can also provide
   a description.
8. Choose
   **Create policy**.

## Step 2: Create an IAM group and attach the policy

As an IAM administrator, you can create a group and attach the policy that you
created to the group. You can add IAM users to the group at any time.

###### To create an IAM group and attach your policy

1. In the navigation pane, choose
   **Groups** and
   then choose
   **Create New Group**.
2. For
   **Group Name**, enter a name for your group and then
   choose
   **Next Step**.
3. In the search field, enter the name of the policy that you created.
   Select the check box for your policy and then choose
   **Next
   Step**.
4. Review the group name and policies. When you are ready, choose

**Create Group**.

## Step 3: Create IAM users and add them to the group

As an IAM administrator, you can add users to a group at any time. This
grants the users the permissions granted to the group.

###### To create an IAM user and add the user to a group

1. In the navigation pane, choose
   **Users** and
   then choose
   **Add user**.
2. For
   **User name**, enter the names for one or more users.
3. Select the check box next to
   **AWS Management Console access**.
   Configure an auto-generated or custom password. You can optionally select

**User must create a new password at next sign-in** to
require a password reset when the user first signs in. 4. Choose
**Next: Permissions**. 5. Choose
**Add user to group** and then select the
group that you created. 6. Choose
**Next: Tags**. You can optionally add tags
to your users. 7. Choose
**Next: Review**. When you are ready, choose

**Create user**.
