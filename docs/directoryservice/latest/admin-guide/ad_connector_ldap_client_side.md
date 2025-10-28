# Enabling client-side LDAPS using

AD Connector

Client-side LDAPS support in AD Connector encrypts communications between Microsoft Active Directory (AD)
and AWS applications. Examples of such applications include WorkSpaces, AWS IAM Identity Center, Quick Suite, and Amazon Chime.
This encryption helps you to better protect your organization's identity data and meet your
security requirements.

You can also deregister and disable client-side LDAPS.

###### Topics

- [Prerequisites](#prereqs-ldap-client-side "#prereqs-ldap-client-side")
- [Enabling client-side LDAPS](#enable-ldap-client-side "#enable-ldap-client-side")
- [Managing client-side LDAPS](manage-ldap-client-side.md "manage-ldap-client-side.md")

## Prerequisites

Before you enable client-side LDAPS, you need to meet the following requirements.

###### Prerequisites:

- [Deploy server certificates in Active
  Directory](#deploy_server_certs_ldap_client_side "#deploy_server_certs_ldap_client_side")
- [CA certificate requirements](#cert_requirements_ldap_client_side "#cert_requirements_ldap_client_side")
- [Networking requirements](#networking_requirements_ldap_client_side "#networking_requirements_ldap_client_side")

### Deploy server certificates in Active

Directory

In order to enable client-side LDAPS, you need to obtain and install server certificates
for each domain controller in Active Directory. These certificates will be used by the LDAP
service to listen for and automatically accept SSL connections from LDAP clients. You can
use SSL certificates that are either issued by an in-house Active Directory Certificate
Services (ADCS) deployment or purchased from a commercial issuer. For more information on
Active Directory server certificate requirements, see [LDAP over SSL (LDAPS) Certificate](https://social.technet.microsoft.com/wiki/contents/articles/2980.ldap-over-ssl-ldaps-certificate.aspx "https://social.technet.microsoft.com/wiki/contents/articles/2980.ldap-over-ssl-ldaps-certificate.aspx") on the Microsoft website.

### CA certificate requirements

A certificate authority (CA) certificate, which represents the issuer of your server
certificates, is required for client-side LDAPS operation. CA certificates are matched with
the server certificates that are presented by your Active Directory domain controllers to
encrypt LDAP communications. Note the following CA certificate requirements:

- To register a certificate, it must be more than 90 days away from
  expiration.
- Certificates must be in Privacy-Enhanced Mail (PEM) format. If exporting CA
  certificates from inside Active Directory, choose base64 encoded X.509 (.CER) as the
  export file format.
- A maximum of five (5) CA certificates can be stored per AD Connector
  directory.
- Certificates using the RSASSA-PSS signature algorithm are not supported.

### Networking requirements

AWS application LDAP traffic will run exclusively on TCP port 636, with no fallback to
LDAP port 389. However, Windows LDAP communications supporting replication, trusts, and more
will continue using LDAP port 389 with Windows-native security. Configure AWS security
groups and network firewalls to allow TCP communications on port 636 in AD Connector
(outbound) and self-managed Active Directory (inbound).

## Enabling client-side LDAPS

To enable client-side LDAPS, you import your certificate authority (CA) certificate into
AD Connector, and then enable LDAPS on your directory. Upon enabling, all LDAP traffic
between AWS applications and your self-managed Active Directory will flow with Secure
Sockets Layer (SSL) channel encryption.

You can use two different methods to enable client-side LDAPS for your directory. You can
use either the AWS Management Console method or the AWS CLI method.

### Registering certificate in

AWS Directory Service

Use either of the following methods to register a certificate in AWS Directory Service.

###### Method 1: To register your certificate in AWS Directory Service (AWS Management Console)

1. In the [AWS Directory Service console](https://console.aws.amazon.com/directoryservicev2/ "https://console.aws.amazon.com/directoryservicev2/") navigation pane, select
   **Directories**.
2. Choose the directory ID link for your directory.
3. On the **Directory details** page, choose the **Networking
   & security** tab.
4. In the **Client-side LDAPS** section, select the
   **Actions** menu, and then select **Register
   certificate**.
5. In the **Register a CA certificate** dialog box, select
   **Browse**, and then select the certificate and choose
   **Open**.
6. Choose **Register certificate**.

###### Method 2: To register your certificate in AWS Directory Service (AWS CLI)

- Run the following command. For the certificate data, point to the location of your
  CA certificate file. A certificate ID will be provided in the response.

```
aws ds register-certificate --directory-id `your_directory_id` --certificate-data file://`your_file_path`
```

### Checking registration

status

To see the status of a certificate registration or a list of registered certificates,
use either of the following methods.

###### Method 1: To check certificate registration status in AWS Directory Service (AWS Management Console)

1. Go to the **Client-side LDAPS** section on the **Directory
   details** page.
2. Review the current certificate registration state that is displayed under the
   **Registration status** column. When the registration status value
   changes to **Registered**, your certificate has been successfully
   registered.

###### Method 2: To check certificate registration status in AWS Directory Service (AWS CLI)

- Run the following command. If the status value returns `Registered`, your
  certificate has been successfully registered.

```
aws ds list-certificates --directory-id `your_directory_id`
```

### Enabling client-side LDAPS

Use either of the following methods to enable client-side LDAPS in AWS Directory Service.

###### Note

You must have successfully registered at least one certificate before you can enable
client-side LDAPS.

###### Method 1: To enable client-side LDAPS in AWS Directory Service (AWS Management Console)

1. Go to the **Client-side LDAPS** section on the **Directory
   details** page.
2. Choose **Enable**. If this option is not available, verify that a
   valid certificate has been successfully registered, and then try again.
3. In the **Enable client-side LDAPS** dialog box, choose
   **Enable**.

###### Method 2: To enable client-side LDAPS in AWS Directory Service (AWS CLI)

- Run the following command.

```
aws ds enable-ldaps --directory-id `your_directory_id` --type Client
```

### Checking LDAPS status

Use either of the following methods to check the LDAPS status in AWS Directory Service.

###### Method 1: To check LDAPS status in AWS Directory Service (AWS Management Console)

1. Go to the **Client-side LDAPS** section on the **Directory
   details** page.
2. If the status value is displayed as **Enabled**, LDAPS has been
   successfully configured.

###### Method 2: To check LDAPS status in AWS Directory Service (AWS CLI)

- Run the following command. If the status value returns `Enabled`, LDAPS
  has been successfully configured.

```
aws ds describe-ldaps-settings –directory-id `your_directory_id`
```

For more information on viewing your client-side LDAPS certificate, deregistering or
disabling your LDAPS certificate, see [Managing client-side LDAPS](manage-ldap-client-side.md "manage-ldap-client-side.md").
