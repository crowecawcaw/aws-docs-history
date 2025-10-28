# Managing and searching for user accounts

Users pools can contains millions of users. Working with a dataset of this size is a
challenge for administrators. Amazon Cognito has tools for finding and modifying user profiles. The top
methods for finding users are the **Users** menu of the Amazon Cognito console, and with
[ListUsers](../../../cognito-user-identity-pools/latest/APIReference/API_ListUsers.md "../../../cognito-user-identity-pools/latest/APIReference/API_ListUsers.md"). Of
the methods that retrieve information about users, these are the options that don't have a cost
impact unlike, for example, [AdminGetUser](../../../cognito-user-identity-pools/latest/APIReference/API_AdminGetUser.md "../../../cognito-user-identity-pools/latest/APIReference/API_AdminGetUser.md").

This section of the guide has information about finding and updating user profiles in a user
pool.

## Viewing user attributes

Use the following procedure to view user attributes in the Amazon Cognito console.

###### To view user attributes

1. Go to the [Amazon Cognito console](https://console.aws.amazon.com/cognito/home "https://console.aws.amazon.com/cognito/home"). If
   prompted, enter your AWS credentials.
2. Choose **User Pools**.
3. Choose an existing user pool from the list.
4. Choose the **Users** menu and select a user in the list.
5. On the user details page, under **User attributes**, you can view
   which attributes are associated with the user.

## Resetting a user's password

Use the following procedure to reset a user's password in the Amazon Cognito console.

###### To reset a user's password

1. Go to the [Amazon Cognito console](https://console.aws.amazon.com/cognito/home "https://console.aws.amazon.com/cognito/home"). If
   prompted, enter your AWS credentials.
2. Choose **User Pools**.
3. Choose an existing user pool from the list.
4. Choose the **Users** menu and select a user in the list.
5. On the user details page, choose **Actions**, **Reset
   password**.
6. In the **Reset password** dialog, review the information and when
   ready, choose **Reset**.

This action immediately results in a confirmation code being sent to the user and
disables the user’s current password by changing the user state to
`RESET_REQUIRED`. The **Reset password** code is valid for 1
hour.

## Enable, disable, and delete user

accounts

You can delete unused user profiles or, if you want to temporarily prevent access, disable
them. Users can delete their own accounts, but only user pool administrators can enable and
disable user accounts.

###### Effect of deletion

Users can't sign in with deleted user accounts and to regain access, must sign up or be
created again.

###### Effect of disabling accounts

When you disable a user account, Amazon Cognito automatically invalidates all authenticated
sessions, deactivates the user account for sign-in, and [revokes their access and refresh tokens](token-revocation.md "token-revocation.md"). Amazon Cognito returns an
`invalid_request` error with the message `User is not enabled` when
a user tries to sign in to an account that you disabled. This behavior doesn't change with
your [user existence disclosure
settings](cognito-user-pool-managing-errors.md "cognito-user-pool-managing-errors.md") for the app client. You can disable local user accounts and the local
profiles of federated user accounts. When users sign in with managed login or the classic
hosted UI, then you disable their account, and then they try to sign in again with the the
browser cookie that maintains their authenticated session, Amazon Cognito redirects them to the login
page.

###### Effect of enabling accounts

Users can immediately sign in to accounts after you enable them. User accounts are
enabled by default. Users' attributes and passwords remain the same as before their account
was disabled. Tokens that your application revoked, whether you disabled the user account or
separately revoked the refresh token, remain non-valid after you enable the user account
that owned the token.

Delete a user account (console)

###### To delete a user account

1. Go to the [Amazon Cognito console](https://console.aws.amazon.com/cognito/home "https://console.aws.amazon.com/cognito/home").
   If prompted, enter your AWS credentials.
2. Choose **User Pools**.
3. Choose an existing user pool from the list.
4. Choose the **Users** menu and select the radio button next to
   the username of a user in the list.
5. Choose **Delete**.
6. Choose **Disable user access**.
7. Choose **Delete**.

Delete a user account (API)
Users can delete their accounts with the self-service access-token-authorized [DeleteUser](../../../cognito-user-identity-pools/latest/APIReference/API_DeleteUser.md "../../../cognito-user-identity-pools/latest/APIReference/API_DeleteUser.md") API operation. The following is an example `DeleteUser`
request body.

```
{
   "AccessToken": "`eyJra456defEXAMPLE`"
}
```

Administrators can delete user accounts with the IAM-authorized [AdminDeleteUser](../../../cognito-user-identity-pools/latest/APIReference/API_AdminDeleteUser.md "../../../cognito-user-identity-pools/latest/APIReference/API_AdminDeleteUser.md") API operation. The following is an example
`AdminDeleteUser` request body.

```
{
   "Username": "`testuser`",
   "UserPoolId": "`us-west-2_EXAMPLE`"
}
```

Disable a user account (console)

###### To disable a user account

1. Go to the [Amazon Cognito console](https://console.aws.amazon.com/cognito/home "https://console.aws.amazon.com/cognito/home").
   If prompted, enter your AWS credentials.
2. Choose **User Pools**.
3. Choose an existing user pool from the list.
4. Choose the **Users** menu and select the username of a user in
   the list.
5. On the user details page, choose **Actions**, **Disable
   user access**.
6. In the dialog that this creates, choose **Disable**.

Disable a user account (API)
Administrators can disable user accounts with the IAM-authorized [AdminDisableUser](../../../cognito-user-identity-pools/latest/APIReference/API_AdminDisableUser.md "../../../cognito-user-identity-pools/latest/APIReference/API_AdminDisableUser.md") API operation. The following is an example
`AdminDisableUser` request body.

```
{
   "Username": "`testuser`",
   "UserPoolId": "`us-west-2_EXAMPLE`"
}
```

Enable a user account (console)

###### To enable a user account

1. Go to the [Amazon Cognito console](https://console.aws.amazon.com/cognito/home "https://console.aws.amazon.com/cognito/home").
   If prompted, enter your AWS credentials.
2. Choose **User Pools**.
3. Choose an existing user pool from the list.
4. Choose the **Users** menu and select the username of a user in
   the list.
5. On the user details page, choose **Actions**, **Enable
   user access**.
6. In the dialog that this creates, choose **Enable**.

Enable a user account (API)
Administrators can enable user accounts with the IAM-authorized [AdminEnableUser](../../../cognito-user-identity-pools/latest/APIReference/API_AdminEnableUser.md "../../../cognito-user-identity-pools/latest/APIReference/API_AdminEnableUser.md") API operation. The following is an example
`AdminEnableUser` request body.

```
{
   "Username": "`testuser`",
   "UserPoolId": "`us-west-2_EXAMPLE`"
}
```

## Searching user

attributes

If you have already created a user pool, you can search from the
**Users** panel in the AWS Management Console. You can also use the Amazon Cognito [ListUsers API](../../../cognito-user-identity-pools/latest/APIReference/API_ListUsers.md "../../../cognito-user-identity-pools/latest/APIReference/API_ListUsers.md"), which accepts a **Filter** parameter.

You can search for any of the following standard attributes. Custom attributes are not
searchable.

- username (case-sensitive)
- email
- phone_number
- name
- given_name
- family_name
- preferred_username
- cognito:user_status (called **Status** in the Console)
  (case-insensitive)
- status (called **Enabled** in the Console) (case-sensitive)
- sub

###### Note

You can also list users with a client-side filter. The server-side filter matches no
more than 1 attribute. For advanced search, use a client-side filter with the
`--query` parameter of the `list-users` action in the AWS Command Line Interface.
When you use a client-side filter, ListUsers returns a paginated list of zero or more users.
You can receive multiple pages in a row with zero results. Repeat the query with each
pagination token that is returned until you receive a null pagination token value, then
review the combined result.

For more information about server-side and client-side filtering, see [Filtering AWS CLI
output](../../../cli/latest/userguide/cli-usage-filter.md "../../../cli/latest/userguide/cli-usage-filter.md") in the AWS Command Line Interface User Guide.

## Searching for users with the AWS Management Console

If you have already created a user pool, you can search from the
**Users** panel in the AWS Management Console.

AWS Management Console searches are always prefix ("starts with") searches.

###### To search for a user in the Amazon Cognito console

1. Go to the [Amazon Cognito console](https://console.aws.amazon.com/cognito/home "https://console.aws.amazon.com/cognito/home"). You
   might be prompted for your AWS credentials.
2. Choose **User Pools**.
3. Choose an existing user pool from the list.
4. Choose the **Users** menu and enter the username in the search field.
   Note that some attribute values are case-sensitive (for example,
   **Username**).

You can also find users by adjusting the search filter to narrow the scope down to
other user properties, such as **Email**, **Phone
number**, or **Last name**.

## Searching for

users with the `ListUsers` API

To search for users from your app, use the Amazon Cognito [ListUsers API](../../../cognito-user-identity-pools/latest/APIReference/API_ListUsers.md "../../../cognito-user-identity-pools/latest/APIReference/API_ListUsers.md"). This API uses the following parameters:

- `AttributesToGet`: An array of strings, where each string is the name of a user
  attribute to be returned for each user in the search results. To retrieve all attributes,
  don't include an `AttributesToGet` parameter or request
  `AttributesToGet` with a value of the literal string
  `null`.
- `Filter`: A filter string of the form "`AttributeName`
  `Filter-Type` "`AttributeValue`"". Quotation marks within the filter
  string must be escaped using the backslash (`\`) character. For example,
  `"family_name = \"Reddy\""`. If the filter string is empty,
  `ListUsers` returns all users in the user pool.

      + `AttributeName`: The name of the attribute to search for. You can only
       search for one attribute at a time.


      ###### Note

      You can only search for standard attributes. Custom attributes are not
       searchable. This is because only indexed attributes are searchable, and custom
       attributes cannot be indexed.
      + `Filter-Type`: For an exact match, use `=`, for example,
       `given_name = "Jon"`. For a prefix ("starts with") match, use
       `^=`, for example, `given_name ^= "Jon"`.
      + `AttributeValue`: The attribute value that must be matched for each
       user.

- `Limit`: Maximum number of users to be returned.
- `PaginationToken`: A token to get more results from a previous search. Amazon Cognito
  expires the pagination token after one hour.
- `UserPoolId`: The user pool ID for the user pool on which the search should be
  performed.

All searches are case-insensitive. Search results are sorted by the attribute named by the
`AttributeName` string, in ascending order.

## Examples of

using the `ListUsers` API

The following example returns all users and includes all attributes.

```

{
    "AttributesToGet": null,
    "Filter": "",
    "Limit": 10,
    "UserPoolId": "us-east-1_samplepool"
}

```

The following example returns all users whose phone numbers start with "+1312" and
includes all attributes.

```

{
    "AttributesToGet": null,
    "Filter": "phone_number ^= \"+1312\"",
    "Limit": 10,
    "UserPoolId": "us-east-1_samplepool"
}

```

The following example returns the first 10 users whose family name is "Reddy". For each
user, the search results include the user's given name, phone number, and email address. If
there are more than 10 matching users in the user pool, the response includes a pagination
token.

```
{
    "AttributesToGet": [
        "given_name",
        "phone_number",
        "email"
    ],
    "Filter": "family_name = \"Reddy\"",
    "Limit": 10,
    "UserPoolId": "us-east-1_samplepool"
}
```

If the previous example returns a pagination token, the following example returns the next
10 users that match the same filter string.

```
{
    "AttributesToGet": [
        "given_name",
        "phone_number",
        "email"
    ],
    "Filter": "family_name = \"Reddy\"",
    "Limit": 10,
    "PaginationToken": "pagination_token_from_previous_search",
    "UserPoolId": "us-east-1_samplepool"
}
```
