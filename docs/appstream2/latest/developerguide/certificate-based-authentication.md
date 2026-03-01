# Certificate-Based Authentication

You can use certificate-based authentication with WorkSpaces Applications fleets joined to Microsoft
Active Directory. This removes the user prompt for the Active Directory domain password
when a user logs in. By using certificate-based authentication with your Active
Directory domain, you can:

- Rely on your SAML 2.0 identity provider to authenticate the user and provide
  SAML assertions to match the user in Active Directory.
- Create a single sign-on logon experience with fewer user prompts.
- Enable passwordless authentication flows using your SAML 2.0 identity
  provider.
  Certificate-based authentication uses AWS Private Certificate Authority (AWS
  Private CA) resources in your AWS account. With AWS Private CA, you can create
  private certificate authority (CA) hierarchies, including root and subordinate CAs. You
  can also create your own CA hierarchy and issue certificates from it that authenticate
  internal users. For more information, see [What is AWS Private CA](../../../privateca/latest/userguide/PcaWelcome.md "../../../privateca/latest/userguide/PcaWelcome.md").

When you use AWS Private CA for certificate-based authentication, WorkSpaces Applications requests
certificates for your users automatically at session reservation for each WorkSpaces Applications fleet
instance. It authenticates users to Active Directory with a virtual smart card
provisioned with the certificates.

Certificate-based authentication (CBA) is supported on WorkSpaces Applications domain-joined fleets
(both single-session and multi-session fleets) that run Windows instances. To enable CBA
on multi-session fleets, you must use an WorkSpaces Applications image that uses an WorkSpaces Applications agent released
on or after 02-07-2025. Or, your image must use managed WorkSpaces Applications image updates released on
or after 02-11-2025.

###### Contents

- [Prerequisites](certificate-based-authentication-prereq.md "certificate-based-authentication-prereq.md")
- [Enable Certificate-based Authentication](certificate-based-authentication-enable.md "certificate-based-authentication-enable.md")
- [Manage Certificate-based Authentication](certificate-based-authentication-manage.md "certificate-based-authentication-manage.md")
- [Enable Cross-account PCA Sharing](pca-sharing.md "pca-sharing.md")
