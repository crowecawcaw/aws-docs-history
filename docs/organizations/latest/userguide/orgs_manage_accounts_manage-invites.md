# Managing pending account invitations with AWS Organizations

When you sign in to your management account, you can view all the linked AWS accounts
in your organization and cancel any pending (open) invitations. To do this, complete the
following steps.

###### Minimum permissions

To manage pending invitations for your organization, you must have the following
permissions:

- `organizations:DescribeOrganization` – required only when using the Organizations console
- `organizations:ListHandshakesForOrganization`
- `organizations:CancelHandshake`

AWS Management Console

###### To view or cancel invitations that are sent from your organization to

other accounts

1. Sign in to the [AWS Organizations console](https://console.aws.amazon.com/organizations/v2 "https://console.aws.amazon.com/organizations/v2"). You must sign in as an IAM user, assume an IAM role, or
   sign in as the root user ([not
   recommended](../../../IAM/latest/UserGuide/best-practices.md#lock-away-credentials "../../../IAM/latest/UserGuide/best-practices.md#lock-away-credentials")) in the organization’s management account.
2. Navigate to the **[Invitations](https://console.aws.amazon.com/organizations/v2/home/accounts/invitations "https://console.aws.amazon.com/organizations/v2/home/accounts/invitations")** page.

This page displays all invitations that are sent from your
organization and their current status.

If you can't see an invitation, check if the invited account is the management account of another organization. Only member accounts and standalone accounts are able to receive invitations.
Management accounts cannot receive invitations.

If you want to invite an account that is a management account in another organization, it is recommended that you make that account a standalone account.

###### Note

Accepted, canceled, and declined invitations continue to
appear in the list for 30 days. After that, they're deleted and
no longer appear in the list. 3. Choose the radio button
![Blue circular icon with a white checkmark symbol in the center.](images/radio-button-selected.png)
next to the invitation that you want to cancel,
and then choose **Cancel invitation**. If the radio
button is grayed out, then that invitation can't be canceled.

The status of the invitation changes from **OPEN** to **CANCELED**.

AWS sends an email message to the account owner stating that you
canceled the invitation. The account can no longer join the
organization unless you send a new invitation.

AWS CLI & AWS SDKs

###### To view or cancel invitations that are sent from your organization to

other accounts

You can use the following commands to view or cancel
invitations:

- AWS CLI: [list-handshakes-for-organization](../../../cli/latest/reference/organizations/list-handshakes-for-organization.md "../../../cli/latest/reference/organizations/list-handshakes-for-organization.md"), [cancel-handshake](../../../cli/latest/reference/organizations/cancel-handshake.md "../../../cli/latest/reference/organizations/cancel-handshake.md")
- The following example shows the invitations sent by this
  organization to other accounts.

```
`$` **aws organizations list-handshakes-for-organization**`{
 "Handshakes": [
 {
 "Action": "INVITE",
 "Arn": "arn:aws:organizations::111111111111:handshake/o-exampleorgid/invite/h-examplehandshakeid111",
 "ExpirationTimestamp": 1482952459.257,
 "Id": "h-examplehandshakeid111",
 "Parties": [
 {
 "Id": "o-exampleorgid",
 "Type": "ORGANIZATION"
 },
 {
 "Id": "juan@example.com",
 "Type": "EMAIL"
 }
 ],
 "RequestedTimestamp": 1481656459.257,
 "Resources": [
 {
 "Resources": [
 {
 "Type": "MASTER_EMAIL",
 "Value": "bill@amazon.com"
 },
 {
 "Type": "MASTER_NAME",
 "Value": "Management Account"
 },
 {
 "Type": "ORGANIZATION_FEATURE_SET",
 "Value": "FULL"
 }
 ],
 "Type": "ORGANIZATION",
 "Value": "o-exampleorgid"
 },
 {
 "Type": "EMAIL",
 "Value": "juan@example.com"
 },
 {
 "Type":"NOTES",
 "Value":"This is an invitation to Juan's account to join Bill's organization."
 }
 ],
 "State": "OPEN"
 },
 {
 "Action": "INVITE",
 "State":"ACCEPTED",
 "Arn": "arn:aws:organizations::111111111111:handshake/o-exampleorgid/invite/h-examplehandshakeid111",
 "ExpirationTimestamp": 1.471797437427E9,
 "Id": "h-examplehandshakeid222",
 "Parties": [
 {
 "Id": "o-exampleorgid",
 "Type": "ORGANIZATION"
 },
 {
 "Id": "anika@example.com",
 "Type": "EMAIL"
 }
 ],
 "RequestedTimestamp": 1.469205437427E9,
 "Resources": [
 {
 "Resources": [
 {
 "Type":"MASTER_EMAIL",
 "Value":"bill@example.com"
 },
 {
 "Type":"MASTER_NAME",
 "Value":"Management Account"
 }
 ],
 "Type":"ORGANIZATION",
 "Value":"o-exampleorgid"
 },
 {
 "Type":"EMAIL",
 "Value":"anika@example.com"
 },
 {
 "Type":"NOTES",
 "Value":"This is an invitation to Anika's account to join Bill's organization."
 }
 ]
 }
 ]
}`
```

The following example shows how to cancel an invitation to an
account.

```
`$` **aws organizations cancel-handshake --handshake-id h-examplehandshakeid111**`{
 "Handshake": {
 "Id": "h-examplehandshakeid111",
 "State":"CANCELED",
 "Action": "INVITE",
 "Arn": "arn:aws:organizations::111111111111:handshake/o-exampleorgid/invite/h-examplehandshakeid111",
 "Parties": [
 {
 "Id": "o-exampleorgid",
 "Type": "ORGANIZATION"
 },
 {
 "Id": "susan@example.com",
 "Type": "EMAIL"
 }
 ],
 "Resources": [
 {
 "Type": "ORGANIZATION",
 "Value": "o-exampleorgid",
 "Resources": [
 {
 "Type": "MASTER_EMAIL",
 "Value": "bill@example.com"
 },
 {
 "Type": "MASTER_NAME",
 "Value": "Management Account"
 },
 {
 "Type": "ORGANIZATION_FEATURE_SET",
 "Value": "CONSOLIDATED_BILLING"
 }
 ]
 },
 {
 "Type": "EMAIL",
 "Value": "anika@example.com"
 },
 {
 "Type": "NOTES",
 "Value": "This is a request for Susan's account to join Bob's organization."
 }
 ],
 "RequestedTimestamp": 1.47008383521E9,
 "ExpirationTimestamp": 1.47137983521E9
 }
}`
```

- AWS SDKs: [ListHandshakesForOrganization](../APIReference/API_ListHandshakesForOrganization.md "../APIReference/API_ListHandshakesForOrganization.md"), [CancelHandshake](../APIReference/API_CancelHandshake.md "../APIReference/API_CancelHandshake.md")
