# Use Service Control Policies to control account instance creation

The ability for member accounts to create account instances depends on when you enabled IAM Identity Center:

- Before November 2023 – You must [permit account instance creation in member accounts](enable-account-instance-console.md "enable-account-instance-console.md"), which is an action that cannot be reversed.
- After November 15, 2023 – Member accounts can create account instances by default.
  In either case, you can use Service Control Policies (SCPs) to:

- Prevent all member accounts from creating account instances.
- Allow only specific member accounts to create account instances.

## Prevent account instances

Use the following procedure to generate an SCP that prevents member accounts from
creating account instances of IAM Identity Center.

1. Open the [IAM Identity Center
   console](https://console.aws.amazon.com/singlesignon "https://console.aws.amazon.com/singlesignon").
2. On the
   **Dashboard**,
   in the **Central management** section, choose the **Prevent
   account instances** button.
3. In the **Attach SCP to prevent creation of new account instances**
   dialog box, an SCP is provided for you. Copy the SCP and choose the **Go to SCP
   dashboard** button. You'll be directed to the [AWS Organizations console](https://console.aws.amazon.com/organizations/v2 "https://console.aws.amazon.com/organizations/v2") to create the SCP or attach it as a
   statement to an existing SCP. SCPs are a feature of AWS Organizations. For instructions on attaching an SCP, see [Attaching and
   detaching service control policies](../../../organizations/latest/userguide/orgs_manage_policies_scps_attach.md "../../../organizations/latest/userguide/orgs_manage_policies_scps_attach.md") in the _AWS Organizations User
   Guide._

## Limit account instances

Instead of preventing all account instance creation, this policy denies any attempt to
create an account instance of IAM Identity Center for all AWS accounts except those explicitly listed
in the `"<ALLOWED-ACCOUNT-ID>"` placeholder.

###### Example: Deny policy to limit account instance creation

JSON

```
`{

 "Version":"2012-10-17",
 "Statement" : [
 {
 "Sid": "DenyMemberAccountInstances",
 "Effect": "Deny",
 "Action": "sso:CreateInstance",
 "Resource": "*",
 "Condition": {
 "StringNotEquals": {
 "aws:PrincipalAccount": [`"<ALLOWED-ACCOUNT-ID>"`]
 }
 }
 }
 ]
}`

```

- Replace [`"<ALLOWED-ACCOUNT-ID>"`] with the actual
  AWS account ID(s) that you want to allow to create an account instance of
  IAM Identity Center.
- You can list multiple allowed account IDs in the array format: [`"111122223333", "444455556666"`].
- Attach this policy to your organization SCP to enforce centralized control over IAM Identity Center account instance creation.

For instructions on attaching an SCP, see [Attaching and detaching service control policies](../../../organizations/latest/userguide/orgs_manage_policies_scps_attach.md "../../../organizations/latest/userguide/orgs_manage_policies_scps_attach.md") in the _AWS Organizations
User Guide._
