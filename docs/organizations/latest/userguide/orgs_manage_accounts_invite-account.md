# Sending account invitations with AWS Organizations

To invite accounts to your organization, you must first verify that you own the email
address associated with the management account. For more information, see [Email address verification with AWS Organizations](about-email-verification.md "about-email-verification.md"). After
you verify your email address, complete the following steps to invite accounts to your
organization.

###### Minimum permissions

To invite an AWS account to join your organization, you must have the following
permissions:

- `organizations:DescribeOrganization` (console only)
- `organizations:InviteAccountToOrganization`

AWS Management Console

###### To invite another account to join your organization

1. Sign in to the [AWS Organizations console](https://console.aws.amazon.com/organizations/v2 "https://console.aws.amazon.com/organizations/v2"). You must sign in as an IAM user, assume an IAM role, or
   sign in as the root user ([not
   recommended](../../../IAM/latest/UserGuide/best-practices.md#lock-away-credentials "../../../IAM/latest/UserGuide/best-practices.md#lock-away-credentials")) in the organization’s management account.
2. If you already verified your email address with AWS, skip this
   step.

If you haven't yet verified your email address, follow the
instructions in the [verification email](about-email-verification.md "about-email-verification.md") within 24 hours after you create the
organization. There might be a delay before you receive the
verification email message. You can't invite an account to join your
organization until you verify your email address. 3. Navigate to the **[AWS accounts](https://console.aws.amazon.com/organizations/v2/home/accounts "https://console.aws.amazon.com/organizations/v2/home/accounts")** page, and choose **Add an AWS
account**. 4. On the **[Add an AWS account](https://console.aws.amazon.com/organizations/v2/home/accounts/add/create "https://console.aws.amazon.com/organizations/v2/home/accounts/add/create")** page, choose **Invite an existing
AWS account**. 5. On the **[Invite an existing AWS](https://console.aws.amazon.com/organizations/v2/home/accounts/add/invite "https://console.aws.amazon.com/organizations/v2/home/accounts/add/invite")** page, for **Email
address or account ID of the AWS account to
invite** enter either the email address associated with
the account to be invited, or its account ID number. 6. (Optional) For **Message to include in the invitation
email message**, enter any text that you want to
include in the email invitation to the invited account owner. 7. (Optional) In the **Add tags** section, specify
one or more tags that are automatically applied to the account after
its administrator accepts the invitation. To do this, choose
**Add tag** and then enter a key and an
optional value. Leaving the value blank sets it to an empty string;
it isn't `null`. You can attach up to 50 tags to an
AWS account. 8. Choose **Send invitation**.

###### Important

If you get a message that you exceeded your account quotas for
the organization or that you can't add an account because your
organization is still initializing, contact [AWS Support](https://console.aws.amazon.com/support/home#/ "https://console.aws.amazon.com/support/home#/"). 9. The console redirects you to the **[Invitations](https://console.aws.amazon.com/organizations/v2/home/accounts/invitations "https://console.aws.amazon.com/organizations/v2/home/accounts/invitations")** page page where you
can view all open and accepted invitations here. The invitation that
you just created appears at the top of the list with its status set
to **OPEN**.

AWS Organizations sends an invitation to the email address of the owner of
the account that you invited to the organization. This email message
includes a link to the AWS Organizations console, where the account owner can
view the details and choose to accept or decline the invitation.
Alternatively, the owner of the invited account can bypass the email
message, go directly to the AWS Organizations console, view the invitation,
and accept or decline it.

The invitation to this account immediately counts against the
maximum number of accounts that you can have in your organization.
AWS Organizations doesn't wait until the account accepts the invitation. If
the invited account declines, the management account cancels the
invitation. If the invited account doesn't respond within the
specified time period, the invitation expires. In either case, the
invitation no longer counts against your quota.

AWS CLI & AWS SDKs

###### To invite another account to join your organization

You can use one of the following commands to invite another account to
join your organization:

- AWS CLI: [invite-account-to-organization](../../../cli/latest/reference/organizations/invite-account-to-organization.md "../../../cli/latest/reference/organizations/invite-account-to-organization.md")

```
`$` **aws organizations invite-account-to-organization \
 --target '{"Type": "EMAIL", "Id": "juan@example.com"}' \
 --notes "This is a request for Juan's account to join Bill's organization."**`{
 "Handshake": {
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
 }
 ],
 "State": "OPEN"
 }
}`
```

- AWS SDKs: [InviteAccountToOrganization](../APIReference/API_InviteAccountToOrganization.md "../APIReference/API_InviteAccountToOrganization.md")
