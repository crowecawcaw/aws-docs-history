# Update a role trust policy

To change who can assume a role, you must modify the role's trust policy. You cannot
modify the trust policy for a _[service-linked
role](id_roles.md#iam-term-service-linked-role "id_roles.md#iam-term-service-linked-role")_.

###### Notes

- If a user is listed as the principal in a role's trust policy but cannot
  assume the role, check the user's [permissions boundary](access_policies_boundaries.md "access_policies_boundaries.md"). If a permissions boundary is set for the user,
  then it must allow the `sts:AssumeRole` action.
- To allow users to assume the current role again within a role session, specify
  the role ARN or AWS account ARN as a principal in the role trust policy.
  AWS services that provide compute resources such as Amazon EC2, Amazon ECS, Amazon EKS, and
  Lambda provide temporary credentials and automatically update these credentials.
  This ensures that you always have a valid set of credentials. For these
  services, it's not necessary to assume the current role again to obtain
  temporary credentials. However, if you intend to pass [session tags](id_session-tags.md "id_session-tags.md") or a [session policy](access_policies.md#policies_session "access_policies.md#policies_session"), you need to assume the
  current role again.

## Updating a role trust policy

(console)

###### To change a role trust policy in the AWS Management Console

1. Sign in to the AWS Management Console and open the IAM console at [https://console.aws.amazon.com/iam/](https://console.aws.amazon.com/iam/ "https://console.aws.amazon.com/iam/").
2. In the navigation pane of the IAM console, choose
   **Roles**.
3. In the list of roles in your account, choose the name of the role that you
   want to modify.
4. Choose the **Trust relationships** tab, and then choose
   **Edit trust policy**.
5. Edit the trust policy as needed. To add additional principals that can assume
   the role, specify them in the `Principal` element. For example, the
   following policy snippet shows how to reference two AWS accounts in the
   `Principal` element:

```
"Principal": {
  "AWS": [
    "arn:aws:iam::111122223333:root",
    "arn:aws:iam::444455556666:root"
  ]
},
```

If you specify a principal in another account, adding an account to the trust
policy of a role is only half of establishing the cross-account trust
relationship. By default, no users in the trusted accounts can assume the role.
The administrator for the newly trusted account must grant the users the
permission to assume the role. To do that, the administrator must create or edit
a policy that is attached to the user to allow the user access to the
`sts:AssumeRole` action. For more information, see the following
procedure or [Grant a user permissions to switch
roles](id_roles_use_permissions-to-switch.md "id_roles_use_permissions-to-switch.md").

The following policy snippet shows how to reference two AWS services in the
`Principal` element:

```
"Principal": {
  "Service": [
    "opsworks.amazonaws.com",
    "ec2.amazonaws.com"
  ]
},
```

6. When you are finished editing your trust policy, choose **Update
   policy** to save your changes.

For more information about policy structure and syntax, see [Policies and permissions in AWS Identity and Access Management](access_policies.md "access_policies.md") and the [IAM JSON policy element reference](reference_policies_elements.md "reference_policies_elements.md").

###### To allow users in a trusted external account to use the role (console)

For more information and detail about this procedure, see [Grant a user permissions to switch
roles](id_roles_use_permissions-to-switch.md "id_roles_use_permissions-to-switch.md").

1. Sign in to the trusted external AWS account.
2. Decide whether to attach the permissions to a user or to a group. In the
   navigation pane of the IAM console, choose **Users** or
   **User groups** accordingly.
3. Choose the name of the user or group to which you want to grant access, and
   then choose the **Permissions** tab.
4. Do one of the following:
   - To edit a customer managed policy, choose the name of the policy,
     choose **Edit policy**, and then choose the
     **JSON** tab. You cannot edit an AWS managed
     policy. AWS managed policies appear with the AWS icon (
     ![Orange cube icon indicating a policy is managed by AWS.](images/policy_icon.png)
     ). For more information about the difference between
     AWS managed policies and customer managed policies, see [Managed policies and inline policies](access_policies_managed-vs-inline.md "access_policies_managed-vs-inline.md").
   - To edit an inline policy, choose the arrow next to the name of the
     policy and choose **Edit policy**.

5. In the policy editor, add a new `Statement` element that specifies
   the following:

```
{
  "Effect": "Allow",
  "Action": "sts:AssumeRole",
  "Resource": "arn:aws:iam::`ACCOUNT-ID`:role/`ROLE-NAME`"
}
```

Replace the ARN in the statement with the ARN of the role that the user can
assume. 6. Follow the prompts on screen to finish editing the policy.

## Updating a role trust policy

(AWS CLI)

You can use the AWS CLI to change who can assume a role.

###### To modify a role trust policy (AWS CLI)

1. (Optional) If you don't know the name of the role that you want to modify, run
   the following command to list the roles in your account:
   - [aws iam
     list-roles](../../../cli/latest/reference/iam/list-roles.md "../../../cli/latest/reference/iam/list-roles.md")

2. (Optional) To view the current trust policy for a role, run the following
   command:
   - [aws iam
     get-role](../../../cli/latest/reference/iam/get-role.md "../../../cli/latest/reference/iam/get-role.md")

3. To modify the trusted principals that can access the role, create a text file
   with the updated trust policy. You can use any text editor to construct the
   policy.

For example, the following trust policy shows how to reference two
AWS accounts in the `Principal` element. This allows users within
two separate AWS accounts to assume this role.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": {
 "Effect": "Allow",
 "Principal": {"AWS": [
 "arn:aws:iam::111122223333:root",
 "arn:aws:iam::444455556666:root"
 ]},
 "Action": "sts:AssumeRole"
 }
}`

```

If you specify a principal in another account, adding an account to the trust
policy of a role is only half of establishing the cross-account trust
relationship. By default, no users in the trusted accounts can assume the role.
The administrator for the newly trusted account must grant the users the
permission to assume the role. To do that, the administrator must create or edit
a policy that is attached to the user to allow the user access to the
`sts:AssumeRole` action. For more information, see the following
procedure or [Grant a user permissions to switch
roles](id_roles_use_permissions-to-switch.md "id_roles_use_permissions-to-switch.md"). 4. To use the file that you just created to update the trust policy, run the
following command:

    * [aws iam
     update-assume-role-policy](../../../cli/latest/reference/iam/update-assume-role-policy.md "../../../cli/latest/reference/iam/update-assume-role-policy.md")

###### To allow users in a trusted external account to use the role (AWS CLI)

For more information and detail about this procedure, see [Grant a user permissions to switch
roles](id_roles_use_permissions-to-switch.md "id_roles_use_permissions-to-switch.md").

1. Create a JSON file that contains a permissions policy that grants permissions
   to assume the role. For example, the following policy contains the minimum
   necessary permissions:

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": {
 "Effect": "Allow",
 "Action": "sts:AssumeRole",
 "Resource": "arn:aws:iam::`111122223333`:role/`ROLE-NAME`"
 }
}`

```

Replace the ARN in the statement with the ARN of the role that the user can
assume. 2. Run the following command to upload the JSON file that contains the trust
policy to IAM:

    * [aws iam
     create-policy](../../../cli/latest/reference/iam/create-policy.md "../../../cli/latest/reference/iam/create-policy.md")

The output of this command includes the ARN of the policy. Make a note of this
ARN because you will need it in a later step. 3. Decide which user or group to attach the policy to. If you don't know the name
of the intended user or group, use one of the following commands to list the
users or groups in your account:

    * [aws iam
     list-users](../../../cli/latest/reference/iam/list-users.md "../../../cli/latest/reference/iam/list-users.md")
    * [aws iam
     list-groups](../../../cli/latest/reference/iam/list-groups.md "../../../cli/latest/reference/iam/list-groups.md")

4. Use one of the following commands to attach the policy that you created in the
   previous step to the user or group:
   - [aws iam
     attach-user-policy](../../../cli/latest/reference/iam/attach-user-policy.md "../../../cli/latest/reference/iam/attach-user-policy.md")
   - [aws iam
     attach-group-policy](../../../cli/latest/reference/iam/attach-group-policy.md "../../../cli/latest/reference/iam/attach-group-policy.md")

## Updating a role trust policy (AWS

API)

You can use the AWS API to change who can assume a role.

###### To modify a role trust policy (AWS API)

1. (Optional) If you don't know the name of the role that you want to modify,
   call the following operation to list the roles in your account:
   - [ListRoles](../APIReference/API_ListRoles.md "../APIReference/API_ListRoles.md")

2. (Optional) To view the current trust policy for a role, call the following
   operation:
   - [GetRole](../APIReference/API_GetRole.md "../APIReference/API_GetRole.md")

3. To modify the trusted principals that can access the role, create a text file
   with the updated trust policy. You can use any text editor to construct the
   policy.

For example, the following trust policy shows how to reference two
AWS accounts in the `Principal` element. This allows users within
two separate AWS accounts to assume this role.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": {
 "Effect": "Allow",
 "Principal": {"AWS": [
 "arn:aws:iam::111122223333:root",
 "arn:aws:iam::444455556666:root"
 ]},
 "Action": "sts:AssumeRole"
 }
}`

```

If you specify a principal in another account, adding an account to the trust
policy of a role is only half of establishing the cross-account trust
relationship. By default, no users in the trusted accounts can assume the role.
The administrator for the newly trusted account must grant the users the
permission to assume the role. To do that, the administrator must create or edit
a policy that is attached to the user to allow the user access to the
`sts:AssumeRole` action. For more information, see the following
procedure or [Grant a user permissions to switch
roles](id_roles_use_permissions-to-switch.md "id_roles_use_permissions-to-switch.md"). 4. To use the file that you just created to update the trust policy, call the
following operation:

    * [UpdateAssumeRolePolicy](../APIReference/API_UpdateAssumeRolePolicy.md "../APIReference/API_UpdateAssumeRolePolicy.md")

###### To allow users in a trusted external account to use the role (AWS API)

For more information and detail about this procedure, see [Grant a user permissions to switch
roles](id_roles_use_permissions-to-switch.md "id_roles_use_permissions-to-switch.md").

1. Create a JSON file that contains a permissions policy that grants permissions
   to assume the role. For example, the following policy contains the minimum
   necessary permissions:

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": {
 "Effect": "Allow",
 "Action": "sts:AssumeRole",
 "Resource": "arn:aws:iam::`111122223333`:role/`ROLE-NAME`"
 }
}`

```

Replace the ARN in the statement with the ARN of the role that the user can
assume. 2. Call the following operation to upload the JSON file that contains the trust
policy to IAM:

    * [CreatePolicy](../APIReference/API_CreatePolicy.md "../APIReference/API_CreatePolicy.md")

The output of this operation includes the ARN of the policy. Make a note of
this ARN because you will need it in a later step. 3. Decide which user or group to attach the policy to. If you don't know the name
of the intended user or group, call one of the following operations to list the
users or groups in your account:

    * [ListUsers](../APIReference/API_ListUsers.md "../APIReference/API_ListUsers.md")
    * [ListGroups](../APIReference/API_ListGroups.md "../APIReference/API_ListGroups.md")

4. Call one of the following operations to attach the policy that you created in
   the previous step to the user or group:
   - API: [AttachUserPolicy](../APIReference/API_AttachUserPolicy.md "../APIReference/API_AttachUserPolicy.md")
   - [AttachGroupPolicy](../APIReference/API_AttachGroupPolicy.md "../APIReference/API_AttachGroupPolicy.md")
