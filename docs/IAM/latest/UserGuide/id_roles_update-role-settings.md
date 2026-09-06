

# Update settings for a role
<a name="id_roles_update-role-settings"></a>

Use the following procedures to update a role's description or change the maximum session duration for a role.

## Update a role description
<a name="id_roles_update-description"></a>

To change the description of the role, modify the description text.

### Updating a role description (console)
<a name="id_roles_update-description-console"></a>

**To change the description of a role (console)**

1. Sign in to the AWS Management Console and open the IAM console at [https://console.aws.amazon.com/iam/](https://console.aws.amazon.com/iam/).

1. In the navigation pane of the IAM console, choose **Roles**.

1. Choose the name of the role to modify.

1. In the **Summary** section, choose **Edit**.

1. Enter a new description in the box and choose **Save changes**.

### Updating a role description (AWS CLI)
<a name="id_roles_update-description-cli"></a>

**To change the description of a role (AWS CLI)**

1. (Optional) To view the current description for a role, run the following command:
   + [aws iam get-role](https://docs.aws.amazon.com/cli/latest/reference/iam/get-role.html)

1. To update a role's description, run the following command with the description parameter:
   + [aws iam update-role](https://docs.aws.amazon.com/cli/latest/reference/iam/update-role.html)

### Updating a role description (AWS API)
<a name="id_roles_update-description-api"></a>

**To change the description of a role (AWS API)**

1. (Optional) To view the current description for a role, call the following operation:
   + [GetRole](https://docs.aws.amazon.com/IAM/latest/APIReference/API_GetRole.html) 

1. To update a role's description, call the following operation with the description parameter:
   + [UpdateRole](https://docs.aws.amazon.com/IAM/latest/APIReference/API_UpdateRole.html)

## Update the maximum session duration for a role
<a name="id_roles_update-session-duration"></a>

To specify the maximum session duration setting for roles that are assumed using the console, the AWS CLI, or AWS API, modify the maximum session duration setting value. This setting can have a value from 1 hour to 12 hours. If you do not specify a value, the default maximum of 1 hour is applied. This setting does not limit sessions assumed by AWS services.

### Updating the maximum role session duration (console)
<a name="id_roles_update-session-duration-console"></a><a name="id_roles_modify_max-session"></a>

**To change the maximum session duration setting for roles that are assumed using the console, AWS CLI, or AWS API (console)**

1. Sign in to the AWS Management Console and open the IAM console at [https://console.aws.amazon.com/iam/](https://console.aws.amazon.com/iam/).

1. In the navigation pane of the IAM console, choose **Roles**.

1. Choose the name of the role to modify.

1. In the **Summary** section, choose **Edit**.

1. For **Maximum session duration**, choose a value. Alternatively, choose **Custom duration** and enter a value (in seconds).

1. Choose **Save changes**.

   Your changes don't take effect until the next time someone assumes this role. To learn how to revoke existing sessions for this role, see [Revoke IAM role temporary security credentials](id_roles_use_revoke-sessions.md).

In the AWS Management Console, IAM user sessions are 12 hours by default. IAM users who switch roles in the console are granted the role maximum session duration, or the remaining time in the user's session, whichever is less.

Anyone who assumes the role from the AWS CLI or AWS API can request a longer session, up to this maximum. The `MaxSessionDuration` setting determines the maximum duration of the role session that can be requested.
+ To specify a session duration using the AWS CLI use the `duration-seconds` parameter. To learn more, see [Switch to an IAM role (AWS CLI)](id_roles_use_switch-role-cli.md).
+ To specify a session duration using the AWS API, use the `DurationSeconds` parameter. To learn more, see [Switch to an IAM role (AWS API)](id_roles_use_switch-role-api.md). 

### Updating the maximum role session duration (AWS CLI)
<a name="id_roles_update-session-duration-cli"></a>

**Note**  
Anyone who assumes the role from the AWS CLI or API can use the `duration-seconds` CLI parameter or the `DurationSeconds` API parameter to request a longer session. The `MaxSessionDuration` setting determines the maximum duration of the role session that can be requested using the `DurationSeconds` parameter. If users don't specify a value for the `DurationSeconds` parameter, their security credentials are valid for one hour.

**To change the maximum session duration setting for roles that are assumed using the AWS CLI (AWS CLI)**

1. (Optional) To view the current maximum session duration setting for a role, run the following command:
   + [aws iam get-role](https://docs.aws.amazon.com/cli/latest/reference/iam/get-role.html)

1. To update a role's maximum session duration setting, run the following command with the `max-session-duration` CLI parameter or the `MaxSessionDuration` API parameter:
   + [aws iam update-role](https://docs.aws.amazon.com/cli/latest/reference/iam/update-role.html)

   Your changes don't take effect until the next time someone assumes this role. To learn how to revoke existing sessions for this role, see [Revoke IAM role temporary security credentials](id_roles_use_revoke-sessions.md).

### Updating the maximum role session duration (AWS API)
<a name="id_roles_update-session-duration-api"></a>

**Note**  
Anyone who assumes the role from the AWS CLI or API can use the `duration-seconds` CLI parameter or the `DurationSeconds` API parameter to request a longer session. The `MaxSessionDuration` setting determines the maximum duration of the role session that can be requested using the `DurationSeconds` parameter. If users don't specify a value for the `DurationSeconds` parameter, their security credentials are valid for one hour.

**To change the maximum session duration setting for roles that are assumed using the API (AWS API)**

1. (Optional) To view the current maximum session duration setting for a role, call the following operation:
   + [GetRole](https://docs.aws.amazon.com/IAM/latest/APIReference/API_GetRole.html) 

1. To update a role's maximum session duration setting, call the following operation with the `max-session-duration` CLI parameter or the `MaxSessionDuration` API parameter:
   + [UpdateRole](https://docs.aws.amazon.com/IAM/latest/APIReference/API_UpdateRole.html)

   Your changes don't take effect until the next time someone assumes this role. To learn how to revoke existing sessions for this role, see [Revoke IAM role temporary security credentials](id_roles_use_revoke-sessions.md).