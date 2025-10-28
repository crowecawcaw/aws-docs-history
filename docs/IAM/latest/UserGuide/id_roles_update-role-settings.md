# Update settings for a role

Use the following procedures to update a role's description or change the maximum session
duration for a role.

## Update a role description

To change the description of the role, modify the description text.

###### To change the description of a role (console)

1. Sign in to the AWS Management Console and open the IAM console at [https://console.aws.amazon.com/iam/](https://console.aws.amazon.com/iam/ "https://console.aws.amazon.com/iam/").
2. In the navigation pane of the IAM console, choose
   **Roles**.
3. Choose the name of the role to modify.
4. In the **Summary** section, choose
   **Edit**.
5. Enter a new description in the box and choose **Save
   changes**.

###### To change the description of a role (AWS CLI)

1. (Optional) To view the current description for a role, run the
   following command:
   - [aws iam
     get-role](../../../cli/latest/reference/iam/get-role.md "../../../cli/latest/reference/iam/get-role.md")

2. To update a role's description, run the following command with the
   description parameter:
   - [aws iam
     update-role](../../../cli/latest/reference/iam/update-role.md "../../../cli/latest/reference/iam/update-role.md")

###### To change the description of a role (AWS API)

1. (Optional) To view the current description for a role, call the
   following operation:
   - [GetRole](../APIReference/API_GetRole.md "../APIReference/API_GetRole.md")

2. To update a role's description, call the following operation with the
   description parameter:
   - [UpdateRole](../APIReference/API_UpdateRole.md "../APIReference/API_UpdateRole.md")

## Update the maximum session duration

for a role

To specify the maximum session duration setting for roles that are assumed using the
console, the AWS CLI, or AWS API, modify the maximum session duration setting value.
This setting can have a value from 1 hour to 12 hours. If you do not specify a value,
the default maximum of 1 hour is applied. This setting does not limit sessions assumed
by AWS services.

###### To change the maximum session

duration setting for roles that are assumed using the console, AWS CLI, or
AWS API (console)

1. Sign in to the AWS Management Console and open the IAM console at [https://console.aws.amazon.com/iam/](https://console.aws.amazon.com/iam/ "https://console.aws.amazon.com/iam/").
2. In the navigation pane of the IAM console, choose
   **Roles**.
3. Choose the name of the role to modify.
4. In the **Summary** section, choose
   **Edit**.
5. For **Maximum session duration**, choose a value.
   Alternatively, choose **Custom duration** and enter a
   value (in seconds).
6. Choose **Save changes**.

Your changes don't take effect until the next time someone assumes
this role. To learn how to revoke existing sessions for this role, see
[Revoke IAM role temporary security
credentials](id_roles_use_revoke-sessions.md "id_roles_use_revoke-sessions.md").
In the AWS Management Console, IAM user sessions are 12 hours by default. IAM users who
switch roles in the console are granted the role maximum session duration, or
the remaining time in the user's session, whichever is less.

Anyone who assumes the role from the AWS CLI or AWS API can request a longer
session, up to this maximum. The `MaxSessionDuration` setting
determines the maximum duration of the role session that can be
requested.

- To specify a session duration using the AWS CLI use the
  `duration-seconds` parameter. To learn more, see [Switch to an IAM role (AWS CLI)](id_roles_use_switch-role-cli.md "id_roles_use_switch-role-cli.md").
- To specify a session duration using the AWS API, use the
  `DurationSeconds` parameter. To learn more, see [Switch to an IAM role (AWS API)](id_roles_use_switch-role-api.md "id_roles_use_switch-role-api.md").

###### Note

Anyone who assumes the role from the AWS CLI or API can use the
`duration-seconds` CLI parameter or the
`DurationSeconds` API parameter to request a longer session.
The `MaxSessionDuration` setting determines the maximum duration
of the role session that can be requested using the
`DurationSeconds` parameter. If users don't specify a value
for the `DurationSeconds` parameter, their security credentials
are valid for one hour.

###### To change the maximum session duration setting for roles that are assumed

using the AWS CLI (AWS CLI)

1.  (Optional) To view the current maximum session duration setting for a
    role, run the following command:
    - [aws iam
      get-role](../../../cli/latest/reference/iam/get-role.md "../../../cli/latest/reference/iam/get-role.md")

2.  To update a role's maximum session duration setting, run the following
    command with the `max-session-duration` CLI parameter or the
    `MaxSessionDuration` API parameter:

        * [aws iam
         update-role](../../../cli/latest/reference/iam/update-role.md "../../../cli/latest/reference/iam/update-role.md")

    Your changes don't take effect until the next time someone assumes
    this role. To learn how to revoke existing sessions for this role, see
    [Revoke IAM role temporary security
    credentials](id_roles_use_revoke-sessions.md "id_roles_use_revoke-sessions.md").

###### Note

Anyone who assumes the role from the AWS CLI or API can use the
`duration-seconds` CLI parameter or the
`DurationSeconds` API parameter to request a longer session.
The `MaxSessionDuration` setting determines the maximum duration
of the role session that can be requested using the
`DurationSeconds` parameter. If users don't specify a value
for the `DurationSeconds` parameter, their security credentials
are valid for one hour.

###### To change the maximum session duration setting for roles that are assumed

using the API (AWS API)

1.  (Optional) To view the current maximum session duration setting for a
    role, call the following operation:
    - [GetRole](../APIReference/API_GetRole.md "../APIReference/API_GetRole.md")

2.  To update a role's maximum session duration setting, call the
    following operation with the `max-sessionduration` CLI
    parameter or the `MaxSessionDuration` API parameter:

        * [UpdateRole](../APIReference/API_UpdateRole.md "../APIReference/API_UpdateRole.md")

    Your changes don't take effect until the next time someone assumes
    this role. To learn how to revoke existing sessions for this role, see
    [Revoke IAM role temporary security
    credentials](id_roles_use_revoke-sessions.md "id_roles_use_revoke-sessions.md").
