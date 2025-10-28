# Create the Amazon EMR security configuration for

LDAP integration

Before you can launch an EMR cluster with LDAP integration, use the steps in
[Create a security
configuration with the Amazon EMR console or with the AWS CLI](emr-create-security-configuration.md "emr-create-security-configuration.md") to create an Amazon EMR security
configuration for the cluster. Complete the following configurations in the
`LDAPConfiguration` block under
`AuthenticationConfiguration`, or the in corresponding fields in the
Amazon EMR console **Security Configurations** section:

**`EnableLDAPAuthentication`**

Console option: **Authentication protocol:
LDAP**

To use the LDAP integration, set this option to `true` or
select it as your authentication protocol when you create a cluster in
the console. By default, `EnableLDAPAuthentication` is
`true` when you create a security configuration in the
Amazon EMR console.

**`LDAPServerURL`**

Console option: **LDAP server location**

The location of the LDAP server including the prefix:
`ldaps://`location_of_server``.

**`BindCertificateARN`**

Console option: **LDAP SSL certificate**

The AWS Secrets Manager ARN that contains the certificate to sign the SSL
certificate that the LDAP server uses. If your LDAP server is signed by
a public Certificate Authority (CA), you can provide an AWS Secrets Manager ARN
with a blank file. For more information on how to store your certificate
in Secrets Manager, see [Store TLS certificates in
AWS Secrets Manager](emr-ranger-tls-certificates.md "emr-ranger-tls-certificates.md").

**`BindCredentialsARN`**

Console option: **LDAP server bind
credentials**

An AWS Secrets Manager ARN that contains the LDAP admin user bind credentials.
The credentials are stored as a JSON object. There is only one key-value
pair in this secret; the key in the pair is the username, and the value
is the password. For example,
`{"uid=admin,cn=People,dc=example,dc=com":
 "AdminPassword1"}`. This is an optional field unless you
enable SSH login for your EMR cluster. In many configurations, Active
Directory instances require bind credentials to allow SSSD to sync
users.

**`LDAPAccessFilter`**

Console option: **LDAP access filter**

Specifies the subset of objects within your LDAP server that can
authenticate. For example, if all you want to grant access to all users
with the `posixAccount` object class in your LDAP server,
define the access filter as
`(objectClass=posixAccount)`.

**`LDAPUserSearchBase`**

Console option: **LDAP user search base**

The search base that your users belong under within your LDAP server.
For example, `cn=People,dc=example,dc=com`.

**`LDAPGroupSearchBase`**

Console option: **LDAP group search base**

The search base that your groups belong under within your LDAP server.
For example, `cn=Groups,dc=example,dc=com`.

**`EnableSSHLogin`**

Console option: **SSH login**

Specifies whether or not to allow password authentication with LDAP
credentials. We don't recommend that you enable this option. Key pairs
are a more secure route to allow access into EMR clusters. This field
is optional and defaults to `false`.

**`LDAPServerType`**

Console option: **LDAP server type**

Specifies the type of LDAP server that Amazon EMR connects to. Supported
options are Active Directory and OpenLDAP. Other LDAP server types might
work, but Amazon EMR doesn't officially support other server types. For more
information, see [LDAP components for Amazon EMR](ldap-components.md "ldap-components.md").

**`ActiveDirectoryConfigurations`**

A required sub-block for security configurations that use the Active
Directory server type.

**`ADDomain`**

Console option: **Active Directory domain**

The domain name used to create the User Principal Name (UPN) for user
authentication with security configurations that use the Active
Directory server type.

## Considerations for security

configurations with LDAP and Amazon EMR

- To create a security configuration with Amazon EMR LDAP integration, you
  must use in-transit encryption. For information about in-transit
  encryption, see [Encrypt data at rest and in transit with Amazon EMR](emr-data-encryption.md "emr-data-encryption.md").
- You can't define Kerberos configuration in the same security
  configuration. Amazon EMR provisions a KDC thar is dedicated to the
  automatically, and manages the admin password for this KDC. Users can't
  access this admin password.
- You can't define IAM runtime roles and AWS Lake Formation in the same security
  configuration.
- The `LDAPServerURL` must have the `ldaps://`
  protocol in its value.
- The `LDAPAccessFilter` can't be empty.

## Use LDAP with the Apache Ranger integration

for Amazon EMR

With the LDAP integration for Amazon EMR, you can further integrate with Apache
Ranger. When you pull .your LDAP users into Ranger, you can then associate those
users with an Apache Ranger policy server to integrate with Amazon EMR and other
applications. To do this, define the `RangerConfiguration` field
within `AuthorizationConfiguration` in the security configuration
that you use with your LDAP cluster. For more information on how to set up the
security configuration, see [Create the EMR security
configuration](emr-ranger-security-config.md "emr-ranger-security-config.md").

When you use LDAP with Amazon EMR, you don't need to provide a
`KerberosConfiguration` with the Amazon EMR integration for Apache
Ranger.
