# Assigning custom permissions profiles

After you create a custom permissions profile, you can assign it to users, roles, or
accounts. Users with sufficient permissions can also use the [`AWS::QuickSight::CustomPermissions`](../../../AWSCloudFormation/latest/UserGuide/aws-resource-quicksight-custompermissions.md "../../../AWSCloudFormation/latest/UserGuide/aws-resource-quicksight-custompermissions.md") CloudFormation resource to manage
Amazon Quick custom permissions profiles.

## Assigning a custom permissions profile (Quick console)

You can assign a custom permissions profile to specific users, roles, or to the
entire account. Assigning a profile replaces any existing assignment at that level.
A user, role, or account can only have one active custom permissions profile
at a time.

###### Note

If a user or role already has a custom permissions profile assigned, the new
assignment replaces the previous one. The original profile is no longer active
for that user or role. Similarly, if an account-level profile is already active,
Quick displays a warning before you replace it.

###### To assign a custom permissions profile

1. Open the [Quick console](https://aws.amazon.com/quicksight/ "https://aws.amazon.com/quicksight/").
2. Choose **Manage Quick**.
3. In the left navigation, choose **Permissions**, and
   then choose **Custom permissions**.
4. On the **Custom permissions** page, locate the profile
   you want to assign. Choose the actions menu next to the
   profile, and then choose **Assign**.

###### Tip

You can also assign a profile immediately after creating one.
After you choose **Create** on the profile
creation page, Quick takes you directly to the
assignment page. 5. On the assignment page, configure who receives this profile:

    * **Users** – Enter the
     usernames of the users you want to assign this profile to. You
     can add multiple users.
    * **Roles** – Select the
     Quick roles (Admin, Author, Reader) that you want
     to assign this profile to.
    * **Set as account default**
     – Select this option to apply the profile as the
     account-level default. If an account-level profile is already
     active, Quick displays a warning indicating that
     the existing assignment will be replaced.

6. When you are ready, choose **Assign**.
You are returned to the custom permissions list page.

## Assigning custom permissions profiles (AWS CLI)

Before you begin, you need to set up and configure the AWS CLI. For more
information about installing the AWS CLI, see [Install or update the latest
version of the AWS CLI](../../../cli/latest/userguide/getting-started-install.md "../../../cli/latest/userguide/getting-started-install.md") and [Configure the AWS CLI](../../../cli/latest/userguide/cli-chap-configure.md "../../../cli/latest/userguide/cli-chap-configure.md")
in the AWS Command Line Interface User guide. You also need permissions to use the Quick
API.

### Updating custom permissions assignments

The following example updates the custom permissions that are assigned to a
role.

```
aws quicksight update-role-custom-permission \
--role `ROLE` \
--aws-account-id `AWSACCOUNTID` \
--namespace default \
--custom-permissions-name `PERMISSIONNAME`
```

The following example applies a custom permissions profile to a user.

```
aws quicksight update-user-custom-permission \
--aws-account-id `AWSACCOUNTID` \
--namespace default \
--user-name `USER_NAME` \
--custom-permissions-name `PERMISSIONNAME`
```

The following example updates the custom permissions that are assigned to an
account.

```
aws quicksight update-account-custom-permission \
--aws-account-id `AWSACCOUNTID` \
--custom-permissions-name `PERMISSIONNAME`
```

### Removing custom permissions assignments

The following example deletes a custom permissions profile from a role.

```
aws quicksight delete-role-custom-permission \
--role `ROLE` \
--aws-account-id `AWSACCOUNTID` \
--namespace default
```

The following example deletes a custom permissions profile from a user.

```
aws quicksight delete-user-custom-permission \
--user-name `USER_NAME` \
--aws-account-id `AWSACCOUNTID` \
--namespace default
```

The following example removes a custom permissions profile from an
account.

```
aws quicksight delete-account-custom-permission \
--aws-account-id `AWSACCOUNTID`
```

### Describing custom permissions assignments

The following example returns the custom permissions profile that is assigned to a
role.

```
aws quicksight describe-role-custom-permission \
--role `ROLE` \
--aws-account-id `AWSACCOUNTID` \
--namespace default
```

The following example returns the custom permissions profile that is assigned to
an account.

```
aws quicksight describe-account-custom-permission \
--aws-account-id `AWSACCOUNTID`
```

To test the custom permissions that are applied to a role or user, log in to the
user's account. When a user logs into Quick, they are granted the highest
privilege role that they have access to. The highest privileged role a user can be granted is
Admin. The lowest privileged role that a user can be granted is Reader. For more information
about roles in Quick, see [Managing user access inside Quick](../../../quicksight/latest/user/managing-users.md "../../../quicksight/latest/user/managing-users.md").

## Verifying permissions for a user

After you assign a custom permissions profile, you can verify which profile is active for
any user and at which level it applies.

###### To verify a user's active permissions profile

1. Open the [Quick console](https://aws.amazon.com/quicksight/ "https://aws.amazon.com/quicksight/").
2. Choose **Manage Quick**.
3. In the left navigation, choose **Permissions**, and
   then choose **Custom permissions**.
4. Choose **Check permissions**.
5. Enter the username of the user you want to verify.
6. Quick displays the active profile name and the level at which it applies (user, role,
   or account).

Use this feature to confirm that Deny by Default profiles are correctly applied and that
precedence is working as expected.
