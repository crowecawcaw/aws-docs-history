# Secure your AD Connector directory

You can use features like multi-factor authentication (MFA), client-side Lightweight
Directory Access Protocol over Secure Sockets Layer (SSL)/Transport Layer Security (TLS)
(LDAPS), and AWS Private Certificate Authority to secure your AD Connector. Ways you can secure your AD Connector
include:

- Enable MFA which increases your AD Connector security.
- Enable client-side Lightweight Directory Access Protocol over Secure Socket Layer
  (SSL)/Transport Layer Security (TLS) (LDAPS) so that communications over LDAP are encrypted
  and improves security.
- Enable certificate-based mutual Transport Layer Security (mTLS) authentication with smart
  cards which allows users to authenticate in to Amazon Web Services through your Active Directory and
  AD Connector.
- Update your AD Connector service account credentials.
- Set up AWS Private CA Connector for AD so you can issue and manage certificates for your
  AD Connector.

###### Tasks to secure your AD Connector

- [Enabling multi-factor authentication for AD Connector](ad_connector_mfa.md "ad_connector_mfa.md")
- [Enabling client-side LDAPS using
  AD Connector](ad_connector_ldap_client_side.md "ad_connector_ldap_client_side.md")
- [Enabling mTLS authentication in AD Connector for use
  with smart cards](ad_connector_clientauth.md "ad_connector_clientauth.md")
- [Updating your AD Connector service account credentials
  in AWS Management Console](ad_connector_update_creds.md "ad_connector_update_creds.md")
- [Set up AWS Private CA Connector for AD](ad_connector_pca_connector.md "ad_connector_pca_connector.md")
