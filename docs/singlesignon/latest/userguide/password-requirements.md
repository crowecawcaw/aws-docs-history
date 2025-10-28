# Password requirements when managing identities

in IAM Identity Center

###### Note

These requirements apply only to users created in the Identity Center directory. If you
have configured an identity source other than IAM Identity Center for authentication, such as [Active Directory](https://learn.microsoft.com/en-us/windows-server/identity/ad-ds/get-started/adac/introduction-to-active-directory-administrative-center-enhancements--level-100-#fine_grained_pswd_policy_mgmt "https://learn.microsoft.com/en-us/windows-server/identity/ad-ds/get-started/adac/introduction-to-active-directory-administrative-center-enhancements--level-100-#fine_grained_pswd_policy_mgmt") or an [external identity provider](confirm-identity-source.md "confirm-identity-source.md"), the
password policies for your users are defined and enforced in those systems, not in
IAM Identity Center. If your identity source is AWS Managed Microsoft AD, see [Manage
password policies for AWS Managed Microsoft AD](../../../directoryservice/latest/admin-guide/ms_ad_password_policies.md "../../../directoryservice/latest/admin-guide/ms_ad_password_policies.md") for more information.

When you use IAM Identity Center as your identity source, users must adhere to the following
password requirements to set or change their password:

- Passwords are case-sensitive.
- Passwords must be between 8 and 64 characters in length.
- Passwords must contain at least one character from each of the following four
  categories:
  - Lowercase letters (a-z)
  - Uppercase letters (A-Z)
  - Numbers (0-9)
  - Non-alphanumeric characters
    (~!@#$%^&\*\_-+=`|\(){}[]:;"'<>,.?/)

- The last three passwords cannot be reused.
- Passwords that are publicly known through a data set leaked from a third party
  cannot be used.
