# Delete roles or instance profiles

If you no longer need a role, we recommend that you delete the role and its associated
permissions. That way you don't have an unused entity that is not actively monitored or
maintained.

If the role was associated with an EC2 instance, you can also remove the role from the
instance profile and then delete the instance profile.

###### Warning

Make sure that you do not have any Amazon EC2 instances running with the role or instance profile you are about to delete. Deleting a role or instance profile that is associated with a running instance will break any applications that are running on the instance.

If you prefer not to permanently delete a role, you can disable a role. To do this, change
the role policies and then revoke all current sessions. For example, you could add a policy to
the role that denied access to all of AWS. You could also edit the trust policy to deny access
to anyone attempting to assume the role. For more information about revoking sessions, see [Revoke IAM role temporary security
credentials](id_roles_use_revoke-sessions.md "id_roles_use_revoke-sessions.md").

###### Topics

- [Viewing role access](#roles-delete_prerequisites "#roles-delete_prerequisites")
- [Deleting a service-linked role](#id_roles_manage_delete_slr "#id_roles_manage_delete_slr")
- [Deleting an IAM role
  (console)](#roles-managingrole-deleting-console "#roles-managingrole-deleting-console")
- [Deleting an IAM role (AWS CLI)](#roles-managingrole-deleting-cli "#roles-managingrole-deleting-cli")
- [Deleting an IAM role (AWS
  API)](#roles-managingrole-deleting-api "#roles-managingrole-deleting-api")
- [Related information](#roles-managingrole-deleting-related-info "#roles-managingrole-deleting-related-info")

## Viewing role access

Before you delete a role, we recommend that you review when the role was last used. You
can do this using the AWS Management Console, the AWS CLI, or the AWS API. You should view this information
because you don't want to remove access from someone using the role.

The date of the role last activity might not match the last date reported in the
**Last Accessed** tab. The [Last Accessed](access_policies_last-accessed-view-data.md "access_policies_last-accessed-view-data.md")
tab reports activity only for services allowed by the role permissions policies. The date of
the role last activity includes the last attempt to access any service in AWS.

###### Note

The tracking period for a role last activity and Last Accessed data is for the trailing
400 days. This period can be shorter if your Region began supporting these features within
the last year. The role might have been used more than 400 days ago. For more information
about the tracking period, see [Where AWS tracks last accessed
information](access_policies_last-accessed.md#last-accessed_tracking-period "access_policies_last-accessed.md#last-accessed_tracking-period").

###### To view when a role was last used (console)

1. Sign in to the AWS Management Console and open the IAM console at [https://console.aws.amazon.com/iam/](https://console.aws.amazon.com/iam/ "https://console.aws.amazon.com/iam/").
2. In the navigation pane, choose **Roles**.
3. Find the row of the role with the activity you want to view. You can use the search
   field to narrow the results. View the **Last activity** column to see the
   number of days since the role was last used. If the role has not been used within the
   tracking period, then the table displays **None**.
4. Choose the name of the role to view more information. The role **Summary** page also includes **Last activity**, which displays
   the last used date for the role. If the role has not been used within the last 400 days,
   then **Last activity** displays **Not accessed in the tracking
   period**.

###### To view when a role was last used (AWS CLI)

`aws iam get-role` - Run
this command to return information about a role, including the `RoleLastUsed`
object. This object contains the `LastUsedDate` and the `Region` in
which the role was last used. If `RoleLastUsed` is present but does not contain a
value, then the role has not been used within the tracking period.

###### To view when a role was last used (AWS API)

`GetRole` - Call this
operation to return information about a role, including the `RoleLastUsed`
object. This object contains the `LastUsedDate` and the `Region` in
which the role was last used. If `RoleLastUsed` is present but does not contain a
value, then the role has not been used within the tracking period.

## Deleting a service-linked role

The method that you use to delete a service-linked role depends on the service. In some
cases, you don't need to manually delete a service-linked role. For example, when you complete
a specific action (such as removing a resource) in the service, the service might delete the
service-linked role for you. In other cases, the service might support deleting a
service-linked role manually from the service console, API, or AWS CLI.

Review the documentation for the _[service-linked role](id_roles.md#iam-term-service-linked-role "id_roles.md#iam-term-service-linked-role")_ in the
linked service to learn how to delete the role. You can view the service-linked roles in your
account by going to the IAM **Roles** page in the console. Service-linked
roles appear with **(Service-linked role)** in the **Trusted
entities** column of the table. A banner on the role **Summary**
page also indicates that the role is a service-linked role.

If the service does not include documentation for deleting the service-linked role, you
can use the IAM console, AWS CLI, or API to delete the role.

## Deleting an IAM role

(console)

When you use the AWS Management Console to delete a role, IAM automatically detaches managed
policies associated with the role. It also automatically deletes any inline policies
associated with the role, and any Amazon EC2 instance profile that contains the role.

###### Important

In some cases, a role might be associated with an Amazon EC2 instance profile, and the role
and the instance profile might have the same name. In that case you can use the AWS Management Console to
delete the role and the instance profile. This linkage happens automatically for roles and
instance profiles that you create in the console. If you created the role from the AWS CLI,
Tools for Windows PowerShell, or the AWS API, then the role and the instance profile might have different names.
In that case you cannot use the console to delete them. Instead, you must use the AWS CLI,
Tools for Windows PowerShell, or AWS API to first remove the role from the instance profile. You must then take a
separate step to delete the role.

###### To delete a role (console)

1. Sign in to the AWS Management Console and open the IAM console at [https://console.aws.amazon.com/iam/](https://console.aws.amazon.com/iam/ "https://console.aws.amazon.com/iam/").
2. In the navigation pane, choose **Roles**, and then select the check
   box next to the role name that you want to delete.
3. At the top of the page, choose **Delete**.
4. In the confirmation dialog box, review the last accessed information, which shows when
   each of the selected roles last accessed an AWS service. This helps you to confirm if
   the role is currently active. If you want to proceed, enter the name of the role in the
   text input field and choose **Delete**. If you are sure, you can proceed
   with the deletion even if the last accessed information is still loading.

###### Note

You cannot use the console to delete an instance profile unless it has the same name as
the role. The instance profile is deleted as part of the process of deleting a role as
described in the preceding procedure. To delete an instance profile without also deleting
the role, you must use the AWS CLI or AWS API. For more information, see the following
sections.

## Deleting an IAM role (AWS CLI)

When you use the AWS CLI to delete a role, you must first delete inline policies associated
with the role. You must also detach managed policies associated with the role. If you want to
delete the associated instance profile that contains the role, you must delete it
separately.

###### To delete a role (AWS CLI)

1. If you don't know the name of the role that you want to delete, enter the following
   command to list the roles in your account:

```
`aws iam list-roles`
```

The list includes the Amazon Resource Name (ARN) of each role. Use the role name, not
the ARN, to refer to roles with the CLI commands. For example, if a role has the following
ARN: `arn:aws:iam::123456789012:role/myrole`, you refer to the role as
`myrole`. 2. Remove the role from all instance profiles that the role is associated with.

    1. To list all instance profiles that the role is associated with, enter the
     following command:



    ```
    `aws iam list-instance-profiles-for-role --role-name `role-name``
    ```
    2. To remove the role from an instance profile, enter the following command for each
     instance profile:



    ```
    `aws iam remove-role-from-instance-profile --instance-profile-name `instance-profile-name` --role-name `role-name``
    ```

3. Delete all policies that are associated with the role.
   1. To list all inline policies that are in the role, enter the following
      command:

   ```
   `aws iam list-role-policies --role-name `role-name``
   ```

   2. To delete each inline policy from the role, enter the following command for each
      policy:

   ```
   `aws iam delete-role-policy --role-name `role-name` --policy-name `policy-name``
   ```

   3. To list all managed policies that are attached to the role, enter the following
      command:

   ```
   `aws iam list-attached-role-policies --role-name `role-name``
   ```

   4. To detach each managed policy from the role, enter the following command for each
      policy:

   ```
   `aws iam detach-role-policy --role-name `role-name` --policy-arn `policy-arn``
   ```

4. Enter the following command to delete the role:

```
`aws iam delete-role --role-name `role-name``
```

5. If you do not plan to reuse the instance profiles that were associated with the role,
   you can enter the following command to delete them:

```
`aws iam delete-instance-profile --instance-profile-name `instance-profile-name``
```

## Deleting an IAM role (AWS

API)

When you use the IAM API to delete a role, you must first delete inline policies
associated with the role. You must also detach managed policies associated with the role. If
you want to delete the associated instance profile that contains the role, you must delete it
separately.

###### To delete a role (AWS API)

1. To list all instance profiles that a role is associated with, call [ListInstanceProfilesForRole](../APIReference/API_ListInstanceProfilesForRole.md "../APIReference/API_ListInstanceProfilesForRole.md").

To remove the role from an instance profile, call [RemoveRoleFromInstanceProfile](../APIReference/API_RemoveRoleFromInstanceProfile.md "../APIReference/API_RemoveRoleFromInstanceProfile.md"). You must pass the role name and instance profile
name.

If you are not going to reuse an instance profile that was associated with the role,
call [DeleteInstanceProfile](../APIReference/API_DeleteInstanceProfile.md "../APIReference/API_DeleteInstanceProfile.md") to delete it. 2. To list all inline policies for a role, call [ListRolePolicies](../APIReference/API_ListRolePolicies.md "../APIReference/API_ListRolePolicies.md").

To delete inline policies that are associated with the role, call [DeleteRolePolicy](../APIReference/API_DeleteRolePolicy.md "../APIReference/API_DeleteRolePolicy.md"). You must pass the
role name and inline policy name. 3. To list all managed policies that are attached to a role, call [ListAttachedRolePolicies](../APIReference/API_ListAttachedRolePolicies.md "../APIReference/API_ListAttachedRolePolicies.md").

To detach managed policies that are attached to the role, call [DetachRolePolicy](../APIReference/API_DetachRolePolicy.md "../APIReference/API_DetachRolePolicy.md"). You must pass the
role name and managed policy ARN. 4. Call [DeleteRole](../APIReference/API_DeleteRole.md "../APIReference/API_DeleteRole.md") to delete the
role.

## Related information

For general information about instance profiles, see [Use instance profiles](id_roles_use_switch-role-ec2_instance-profiles.md "id_roles_use_switch-role-ec2_instance-profiles.md").

For general information about service-linked roles, see [Create a service-linked role](id_roles_create-service-linked-role.md "id_roles_create-service-linked-role.md").
