# Standard migration process to enable all features with Organizations

This topic describes how to enable all features with the standard migration process.

## Step 1: Request invited accounts to approve the migration (Management account)

When you sign in to your organization's management account, you can begin the process
to enable all features. To do this, complete the following steps.

###### Minimum permissions

To enable all features in your organization, you must have the following
permission:

- `organizations:EnableAllFeatures`
- `organizations:DescribeOrganization` – required only when using the Organizations console

AWS Management Console

###### To ask your invited member accounts to agree to enable all features

in the organization

1. Sign in to the [AWS Organizations console](https://console.aws.amazon.com/organizations/v2 "https://console.aws.amazon.com/organizations/v2"). You must sign in as an IAM user, assume an IAM role, or
   sign in as the root user ([not
   recommended](../../../IAM/latest/UserGuide/best-practices.md#lock-away-credentials "../../../IAM/latest/UserGuide/best-practices.md#lock-away-credentials")) in the organization’s management account.
2. On the **[Settings](https://console.aws.amazon.com/organizations/v2/home/settings "https://console.aws.amazon.com/organizations/v2/home/settings")** page choose **Begin process to enable all
   features**.
3. On the **[Enable all features](https://console.aws.amazon.com/organizations/v2/home/settings/enable-all-features "https://console.aws.amazon.com/organizations/v2/home/settings/enable-all-features")** page, acknowledge your understanding that you
   cannot return to only consolidated billing features after you switch
   by choosing **Begin process to enable all
   features**.

AWS Organizations sends a request to every invited (not created) account in
the organization asking for approval to enable all features in the
organization. If you have any accounts that were created using
AWS Organizations and the member account administrator deleted the
service-linked role named `AWSServiceRoleForOrganizations`, AWS Organizations sends
that account a request to recreate the role.

The console displays the **Request approval
status** list for the invited accounts.

###### Tip

To get back to this page later, open the **[Settings](https://console.aws.amazon.com/organizations/v2/home/settings "https://console.aws.amazon.com/organizations/v2/home/settings")** page and in
the **Request sent _date_** section, choose
**View status**. 4. The **[Enable all features](https://console.aws.amazon.com/organizations/v2/home/settings/enable-all-features "https://console.aws.amazon.com/organizations/v2/home/settings/enable-all-features")** page shows the current request status for each
account in the organization. Accounts that have agreed to the
request show a status of **ACCEPTED**. Accounts
that haven't yet agreed show a status of
**OPEN**.

AWS CLI & AWS SDKs

###### To ask your invited member accounts to agree to enable all features

in the organization

You can use one of the following commands to enable all features in an
organization:

- AWS CLI: [enable-all-features](../../../cli/latest/reference/organizations/enable-all-features.md "../../../cli/latest/reference/organizations/enable-all-features.md")

The following command begins the process to enable all features in
the organization.

```
`$` **aws organizations enable-all-features**`{
 "Handshake": {
 "Id": "h-79d8f6f114ee4304a5e55397eEXAMPLE",
 "Arn": "arn:aws:organizations::123456789012:handshake/o-aa111bb222/enable_all_features/h-79d8f6f114ee4304a5e55397eEXAMPLE",
 "Parties": [
 {
 "Id": "a1b2c3d4e5",
 "Type": "ORGANIZATION"
 }
 ],
 "State": "REQUESTED",
 "RequestedTimestamp": "2020-11-19T16:21:46.995000-08:00",
 "ExpirationTimestamp": "2021-02-17T16:21:46.995000-08:00",
 "Action": "ENABLE_ALL_FEATURES",
 "Resources": [
 {
 "Value": "o-a1b2c3d4e5",
 "Type": "ORGANIZATION"
 }
 ]
 }
}`
```

The output shows the details of the handshake that invited member
accounts must agree to.

- AWS SDKs: [EnableAllFeatures](../APIReference/API_EnableAllFeatures.md "../APIReference/API_EnableAllFeatures.md")

###### Notes

- A countdown of 90 days begins when the request is sent to the member
  accounts. All accounts must approve the request within that time period or
  the request expires. If the request expires, all requests related to this
  attempt are canceled, and you have to start over with step 2.
- Once you make the request to enable all features, any existing unaccepted
  account invitations will be cancelled.
- During the all features migration process, you can still initiate new
  account invitations and create new accounts.

After all invited accounts in the organization approve their requests, you can
finalize the process and enable all features. You can also immediately finalize the
process if your organization doesn't have any _invited_
member accounts. To finalizing the process, continue with [Step 3: Finalize the migration process to enable all
features (Management account)](#finalize-migration "#finalize-migration").

## Step 2: Approve the request to enable all

features or to recreate the service-linked role (Invited account)

When you sign in to one of the organization's invited member accounts, you can approve
a request from the management account. If your account was originally invited to join
the organization, the invitation is to enable all features and implicitly includes
approval for recreating the `AWSServiceRoleForOrganizations` role, if needed. If your account
was instead created using AWS Organizations and you deleted the `AWSServiceRoleForOrganizations`
service-linked role, you receive an invitation only to recreate the role. To do this,
complete the following steps.

###### Important

If you enable all features, the management account in the organization can apply
policy-based controls on your member account. These controls can restrict what users
and even what you as the administrator can do in your account. Such restrictions
might prevent your account from leaving the organization.

###### Minimum permissions

To approve a request to enable all features for your member account, the member account must have
the following permissions:

- `organizations:AcceptHandshake`
- `organizations:DescribeOrganization` – required only when using the Organizations console
- `organizations:ListHandshakesForAccount`– required only when using the Organizations console
- `iam:CreateServiceLinkedRole` – required only if the
  `AWSServiceRoleForOrganizations` role must be recreated in the member
  account

AWS Management Console

###### To agree to the request to enable all features in the

organization

1. Sign in to the AWS Organizations console at [AWS Organizations console](https://console.aws.amazon.com/organizations/v2 "https://console.aws.amazon.com/organizations/v2"). You must sign in as an
   IAM user, assume an IAM role, or sign in as the root user ([not
   recommended](../../../IAM/latest/UserGuide/best-practices.md#lock-away-credentials "../../../IAM/latest/UserGuide/best-practices.md#lock-away-credentials")) in a member account.
2. Read what accepting the request for all features in the
   organization means for your account, and then choose
   **Accept**. The page continues to show the
   process as incomplete until all accounts in the organization accept
   the requests and the administrator of the management account
   finalizes the process.

AWS CLI & AWS SDKs

###### To agree to the request to enable all features in the

organization

To agree to the request, you must accept the handshake with
`"Action": "APPROVE_ALL_FEATURES"`.

- AWS CLI:

      + [accept-handshake](../../../cli/latest/reference/organizations/accept-handshake.md "../../../cli/latest/reference/organizations/accept-handshake.md")
      + [list-handshakes-for-account](../../../cli/latest/reference/organizations/list-handshakes-for-account.md "../../../cli/latest/reference/organizations/list-handshakes-for-account.md")

  The following example shows how to list the handshakes available
  for your account. The value of `"Id"` in the fourth line
  of the output is the value you need for the next command.

```
`$` **aws organizations list-handshakes-for-account**`{
 "Handshakes": [
 {
 "Id": "h-a2d6ecb7dbdc4540bc788200aEXAMPLE",
 "Arn": "arn:aws:organizations::123456789012:handshake/o-aa111bb222/approve_all_features/h-a2d6ecb7dbdc4540bc788200aEXAMPLE",
 "Parties": [
 {
 "Id": "a1b2c3d4e5",
 "Type": "ORGANIZATION"
 },
 {
 "Id": "111122223333",
 "Type": "ACCOUNT"
 }
 ],
 "State": "OPEN",
 "RequestedTimestamp": "2020-11-19T16:35:24.824000-08:00",
 "ExpirationTimestamp": "2021-02-17T16:35:24.035000-08:00",
 "Action": "APPROVE_ALL_FEATURES",
 "Resources": [
 {
 "Value": "c440da758cab44068cdafc812EXAMPLE",
 "Type": "PARENT_HANDSHAKE"
 },
 {
 "Value": "o-aa111bb222",
 "Type": "ORGANIZATION"
 },
 {
 "Value": "111122223333",
 "Type": "ACCOUNT"
 }
 ]
 }
 ]
}`

```

The following example uses the Id of the handshake from the
previous command to accept that handshake.

```
`$` **aws organizations accept-handshake --handshake-id h-a2d6ecb7dbdc4540bc788200aEXAMPLE**`{
 "Handshake": {
 "Id": "h-a2d6ecb7dbdc4540bc788200aEXAMPLE",
 "Arn": "arn:aws:organizations::123456789012:handshake/o-aa111bb222/approve_all_features/h-a2d6ecb7dbdc4540bc788200aEXAMPLE",
 "Parties": [
 {
 "Id": "a1b2c3d4e5",
 "Type": "ORGANIZATION"
 },
 {
 "Id": "111122223333",
 "Type": "ACCOUNT"
 }
 ],
 "State": "ACCEPTED",
 "RequestedTimestamp": "2020-11-19T16:35:24.824000-08:00",
 "ExpirationTimestamp": "2021-02-17T16:35:24.035000-08:00",
 "Action": "APPROVE_ALL_FEATURES",
 "Resources": [
 {
 "Value": "c440da758cab44068cdafc812EXAMPLE",
 "Type": "PARENT_HANDSHAKE"
 },
 {
 "Value": "o-aa111bb222",
 "Type": "ORGANIZATION"
 },
 {
 "Value": "111122223333",
 "Type": "ACCOUNT"
 }
 ]
 }
}`
```

- AWS SDKs:
  - [list-handshakes-for-account](../../../cli/latest/reference/organizations/list-handshakes-for-account.md "../../../cli/latest/reference/organizations/list-handshakes-for-account.md")
  - [AcceptHandshake](../APIReference/API_AcceptHandshake.md "../APIReference/API_AcceptHandshake.md")

## Step 3: Finalize the migration process to enable all

features (Management account)

All invited member accounts must approve the request to enable all features. If there
are no invited member accounts in the organization, the **Enable all features
progress** page indicates with a green banner that you can finalize the
process.

###### Minimum permissions

To finalize the process to enable all features for the organization, you must have
the following permission:

- `organizations:AcceptHandshake`
- `organizations:ListHandshakesForOrganization`
- `organizations:DescribeOrganization` – required only when using the Organizations console

AWS Management Console

###### To finalize the process to enable all features

1. Sign in to the [AWS Organizations console](https://console.aws.amazon.com/organizations/v2 "https://console.aws.amazon.com/organizations/v2"). You must sign in as an IAM user, assume an IAM role, or
   sign in as the root user ([not
   recommended](../../../IAM/latest/UserGuide/best-practices.md#lock-away-credentials "../../../IAM/latest/UserGuide/best-practices.md#lock-away-credentials")) in the organization’s management account.
2. On the **[Settings](https://console.aws.amazon.com/organizations/v2/home/settings "https://console.aws.amazon.com/organizations/v2/home/settings")** page, if all invited accounts accept the request
   to enable all features, a green box appears at the top of the page
   to inform you. In the green box, choose **Go to
   finalize**.
3. On the **[Enable all features](https://console.aws.amazon.com/organizations/v2/home/settings/enable-all-features "https://console.aws.amazon.com/organizations/v2/home/settings/enable-all-features")** page, choose **Finalize**,
   and then in the confirmation dialog box, choose
   **Finalize** again.
4. The organization now has all features enabled.

AWS CLI & AWS SDKs

###### To finalize the process to enable all features

To finalize the process, you must accept the handshake with
`"Action": "ENABLE_ALL_FEATURES"`.

- AWS CLI:
  - [list-handshakes-for-organization](../../../cli/latest/reference/organizations/list-handshakes-for-organization.md "../../../cli/latest/reference/organizations/list-handshakes-for-organization.md")
  - [accept-handshake](../../../cli/latest/reference/organizations/accept-handshake.md "../../../cli/latest/reference/organizations/accept-handshake.md")

```
`$` **aws organizations list-handshakes-for-organization**`{
 "Handshakes": [
 {
 "Id": "h-43a871103e4c4ee399868fbf2EXAMPLE",
 "Arn": "arn:aws:organizations::123456789012:handshake/o-aa111bb222/enable_all_features/h-43a871103e4c4ee399868fbf2EXAMPLE",
 "Parties": [
 {
 "Id": "a1b2c3d4e5",
 "Type": "ORGANIZATION"
 }
 ],
 "State": "OPEN",
 "RequestedTimestamp": "2020-11-20T08:41:48.047000-08:00",
 "ExpirationTimestamp": "2021-02-18T08:41:48.047000-08:00",
 "Action": "ENABLE_ALL_FEATURES",
 "Resources": [
 {
 "Value": "o-aa111bb222",
 "Type": "ORGANIZATION"
 }
 ]
 }
 ]
}`
```

The following example shows how to list the handshakes available
for the organization. The value of `"Id"` in the fourth
line of the output is the value you need for the next
command.

```
`$` **aws organizations accept-handshake \
 --handshake-id h-43a871103e4c4ee399868fbf2EXAMPLE**`{
 "Handshake": {
 "Id": "h-43a871103e4c4ee399868fbf2EXAMPLE",
 "Arn": "arn:aws:organizations::123456789012:handshake/o-aa111bb222/enable_all_features/h-43a871103e4c4ee399868fbf2EXAMPLE",
 "Parties": [
 {
 "Id": "a1b2c3d4e5",
 "Type": "ORGANIZATION"
 }
 ],
 "State": "ACCEPTED",
 "RequestedTimestamp": "2020-11-20T08:41:48.047000-08:00",
 "ExpirationTimestamp": "2021-02-18T08:41:48.047000-08:00",
 "Action": "ENABLE_ALL_FEATURES",
 "Resources": [
 {
 "Value": "o-aa111bb222",
 "Type": "ORGANIZATION"
 }
 ]
 }
}`
```

- AWS SDKs:
  - [ListHandshakesForOrganization](../APIReference/API_ListHandshakesForOrganization.md "../APIReference/API_ListHandshakesForOrganization.md")
  - [AcceptHandshake](../APIReference/API_AcceptHandshake.md "../APIReference/API_AcceptHandshake.md")
