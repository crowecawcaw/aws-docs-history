# Username in sign-in CloudTrail

events

IAM Identity Center emits the `UserName` field under the
`additionalEventData` element once per successful sign-in of an IAM Identity Center user.
The following list describes the two sign-in events in scope, and the conditions under
which these events happen. Only one of the conditions can be true when a user is signing
in.

- `CredentialChallenge`
  - When `CredentialType` is "`PASSWORD`" – applies
    to password authentication with Directory Service or IAM Identity Center directory.
  - When `CredentialType` is "`EMAIL_OTP`" –
    applies only to the IAM Identity Center directory when a user created with a `CreateUser`
    API call attempts to sign in for the first time, and the user receives a
    one-time password to sign in with that password once.

- `UserAuthentication`

      + When `CredentialType` is "`EXTERNAL_IDP`" –
       applies to authentication with an external IdP.

  The value of `UserName` for successful authentications is as follows
  :

- When the identity source is an external IdP, the value is equal to the
  `nameID` value in the incoming SAML assertion. This value is equal to
  the `UserName` field in the IAM Identity Center directory.
- When the identity source is an IAM Identity Center directory, the value emitted is equal to the
  `UserName` field in this directory.
- When the identity source is the Directory Service, the value emitted is equal to the
  username that the user enters during authentication. For example, a user who has the
  username `anyuser@company.com`, can authenticate with
  `anyuser`, `anyuser@company.com`, or
  `company.com/anyuser`, and in each case the entered value is emitted in
  CloudTrail respectively.
  **Security masking of incorrect username attempts**

The `UserName` field contains the string `HIDDEN_DUE_TO_SECURITY_REASONS` when the recorded event is a console sign-in failure
caused by incorrect user name input. CloudTrail doesn't record the contents in this case because the text could contain sensitive information,
as described in the following examples:

- A user accidentally types a password in the user name field.
- A user accidentally types the account name of a personal email account, a bank sign-in identifier, or some other private ID.

###### Tip

We recommend you use `userId` and `identityStoreArn` for
identifying the user behind IAM Identity Center CloudTrail events. If you need to use the
`userName` field, you can use the `userName` under the
`additionalEventData` element that's emitted once per successful
sign-in.

For additional information on how you can use the `UserName` field, refer
to [Correlating user events within the same user session](sso-cloudtrail-use-cases.md#correlating-users "sso-cloudtrail-use-cases.md#correlating-users").
