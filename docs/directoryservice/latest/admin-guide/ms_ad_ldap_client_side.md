# Enabling client-side LDAPS using AWS Managed Microsoft AD

Client-side Lightweight Directory Access Protocol Secure Sockets Layer (SSL)/Transport Layer
Security (TLS) (LDAPS) support in AWS Managed Microsoft AD encrypts communications between self-managed
(on-premises) Microsoft Active Directory (AD) and AWS applications. Examples of such
applications include WorkSpaces, AWS IAM Identity Center, Quick Suite, and Amazon Chime. This encryption helps you to better
protect your organization's identity data and meet your security requirements.

## Prerequisites

Before you enable client-side LDAPS, you need to meet the following requirements.

###### Topics

- [Create a trust relationship
  between your AWS Managed Microsoft AD and self-managed Microsoft Active Directory](#trust_relationship_MAD_and_self_managed "#trust_relationship_MAD_and_self_managed")
- [Deploy server certificates in Active
  Directory](#ldap_client_side_deploy_server_certs "#ldap_client_side_deploy_server_certs")
- [Certificate Authority certificate requirements](#ldap_client_side_get_certs_ready "#ldap_client_side_get_certs_ready")
- [Networking requirements](#ldap_client_side_considerations_enabling "#ldap_client_side_considerations_enabling")

### Create a trust relationship

between your AWS Managed Microsoft AD and self-managed Microsoft Active Directory

First, you need to establish a trust relationship between your AWS Managed Microsoft AD and
self-managed Microsoft Active Directory to enable client-side LDAPS. For more information, see [Creating a trust relationship between your AWS Managed Microsoft AD and self-managed AD](ms_ad_setup_trust.md "ms_ad_setup_trust.md").

### Deploy server certificates in Active

Directory

In order to enable client-side LDAPS, you need to obtain and install server certificates
for each domain controller in Active Directory. These certificates will be used by the LDAP
service to listen for and automatically accept SSL connections from LDAP clients. You can
use SSL certificates that are either issued by an in-house Active Directory Certificate
Services (ADCS) deployment or purchased from a commercial issuer. For more information on
Active Directory server certificate requirements, see [LDAP over SSL (LDAPS) Certificate](https://social.technet.microsoft.com/wiki/contents/articles/2980.ldap-over-ssl-ldaps-certificate.aspx "https://social.technet.microsoft.com/wiki/contents/articles/2980.ldap-over-ssl-ldaps-certificate.aspx") on the Microsoft website.

### Certificate Authority certificate requirements

A certificate authority (CA) certificate, which represents the issuer of your server
certificates, is required for client-side LDAPS operation. CA certificates are matched with
the server certificates that are presented by your Active Directory domain controllers to
encrypt LDAP communications. Note the following CA certificate requirements:

- Enterprise Certification Authority (CA) is required to enable client-side LDAPS. You
  can use either Active Directory Certificate Service, a third-party commercial certificate authority,
  or [AWS Certificate Manager](../../../acm/latest/userguide/acm-overview.md "../../../acm/latest/userguide/acm-overview.md"). For more information about Microsoft Enterprise Certificate Authority,
  see [Microsoft documentation](<https://learn.microsoft.com/en-us/previous-versions/tn-archive/cc875810(v=technet.10)?redirectedfrom=MSDN> "https://learn.microsoft.com/en-us/previous-versions/tn-archive/cc875810(v=technet.10)?redirectedfrom=MSDN").
- To register a certificate, it must be more than 90 days away from
  expiration.
- Certificates must be in Privacy-Enhanced Mail (PEM) format. If exporting CA
  certificates from inside Active Directory, choose base64 encoded X.509 (.CER) as the
  export file format.
- A maximum of five (5) CA certificates can be stored per AWS Managed Microsoft AD
  directory.
- Certificates using the RSASSA-PSS signature algorithm are not supported.
- CA certificates that chain to every server certificate in every trusted domain must
  be registered.

### Networking requirements

AWS application LDAP traffic will run exclusively on TCP port 636, with no fallback to
LDAP port 389. However, Windows LDAP communications supporting replication, trusts, and more
will continue using LDAP port 389 with Windows-native security. Configure AWS security
groups and network firewalls to allow TCP communications on port 636 in AWS Managed Microsoft AD
(outbound) and self-managed Active Directory (inbound). Leave open LDAP port 389 between
AWS Managed Microsoft AD and self-managed Active Directory.

## Enable client-side LDAPS

To enable client-side LDAPS, you import your certificate authority (CA) certificate into
AWS Managed Microsoft AD, and then enable LDAPS on your directory. Upon enabling, all LDAP traffic between
AWS applications and your self-managed Active Directory will flow with Secure Sockets Layer
(SSL) channel encryption.

You can use two different methods to enable client-side LDAPS for your directory. You can
use either the AWS Management Console method or the AWS CLI method.

###### Note

Client-Side LDAPS is a Regional feature of AWS Managed Microsoft AD.
If you are using [Multi-Region replication](ms_ad_configure_multi_region_replication.md "ms_ad_configure_multi_region_replication.md"), the
following procedures must be applied separately in each Region. For more information, see
[Global vs Regional features](multi-region-global-region-features.md "multi-region-global-region-features.md").

###### Topics

- [Step 1: Register a certificate in Directory Service](#ms_ad_registercert "#ms_ad_registercert")
- [Step 2: Check registration status](#ms_ad_check-registration-status "#ms_ad_check-registration-status")
- [Step 3: Enable client-side LDAPS](#ms_ad_enableclientsideldapssteps "#ms_ad_enableclientsideldapssteps")
- [Step 4: Check LDAPS status](#ms_ad_check-ldaps-status "#ms_ad_check-ldaps-status")

### Step 1: Register a certificate in Directory Service

Use either of the following methods to register a certificate in Directory Service.

###### Method 1: To register your certificate in Directory Service (AWS Management Console)

1. In the [AWS Directory Service console](https://console.aws.amazon.com/directoryservicev2/ "https://console.aws.amazon.com/directoryservicev2/") navigation pane, select
   **Directories**.
2. Choose the directory ID link for your directory.
3. On the **Directory details** page, do one of the
   following:
   - If you have multiple Regions showing under **Multi-Region
     replication**, select the Region where you want to register your
     certificate, and then choose the **Networking &
     security** tab. For more information, see [Primary vs additional Regions](multi-region-global-primary-additional.md "multi-region-global-primary-additional.md").
   - If you do not have any Regions showing under **Multi-Region
     replication**, choose the **Networking &
     security** tab.

4. In the **Client-side LDAPS** section, select the
   **Actions** menu, and then select **Register
   certificate**.
5. In the **Register a CA certificate** dialog box, select
   **Browse**, and then select the certificate and choose
   **Open**.
6. Choose **Register certificate**.

###### Method 2: To register your certificate in Directory Service (AWS CLI)

- Run the following command. For the certificate data, point to the location of your
  CA certificate file. A certificate ID will be provided in the response.

```
aws ds register-certificate --directory-id `your_directory_id` --certificate-data file://`your_file_path`
```

### Step 2: Check registration status

To see the status of a certificate registration or a list of registered certificates,
use either of the following methods.

###### Method 1: To check certificate registration status in Directory Service (AWS Management Console)

1. Go to the **Client-side LDAPS** section on the **Directory
   details** page.
2. Review the current certificate registration state that is displayed under the
   **Registration status** column. When the registration status value
   changes to **Registered**, your certificate has been successfully
   registered.

###### Method 2: To check certificate registration status in Directory Service (AWS CLI)

- Run the following command. If the status value returns `Registered`, your
  certificate has been successfully registered.

```
aws ds list-certificates --directory-id `your_directory_id`
```

### Step 3: Enable client-side LDAPS

Use either of the following methods to enable client-side LDAPS in Directory Service.

###### Note

You must have successfully registered at least one certificate before you can enable
client-side LDAPS.

###### Method 1: To enable client-side LDAPS in Directory Service (AWS Management Console)

1. Go to the **Client-side LDAPS** section on the **Directory
   details** page.
2. Choose **Enable**. If this option is not available, verify that a
   valid certificate has been successfully registered, and then try again.
3. In the **Enable client-side LDAPS** dialog box, choose
   **Enable**.

###### Method 2: To enable client-side LDAPS in Directory Service (AWS CLI)

- Run the following command.

```
aws ds enable-ldaps --directory-id `your_directory_id` --type Client
```

### Step 4: Check LDAPS status

Use either of the following methods to check the LDAPS status in Directory Service.

###### Method 1: To check LDAPS status in Directory Service (AWS Management Console)

1. Go to the **Client-side LDAPS** section on the **Directory
   details** page.
2. If the status value is displayed as **Enabled**, LDAPS has been
   successfully configured.

###### Method 2: To check LDAPS status in Directory Service (AWS CLI)

- Run the following command. If the status value returns `Enabled`, LDAPS
  has been successfully configured.

```
aws ds describe-ldaps-settings –-directory-id `your_directory_id`
```

## Manage client-side LDAPS

Use these commands to manage your LDAPS configuration.

You can use two different methods to manage client-side LDAPS settings. You can use either
the AWS Management Console method or the AWS CLI method.

### View certificate details

Use either of the following methods to see when a certificate is set to expire.

###### Method 1: To view certificate details in Directory Service (AWS Management Console)

1. In the [AWS Directory Service console](https://console.aws.amazon.com/directoryservicev2/ "https://console.aws.amazon.com/directoryservicev2/") navigation pane, select
   **Directories**.
2. Choose the directory ID link for your directory.
3. On the **Directory details** page, do one of the
   following:
   - If you have multiple Regions showing under **Multi-Region
     replication**, select the Region where you want to view the certificate,
     and then choose the **Networking & security** tab.
     For more information, see [Primary vs additional Regions](multi-region-global-primary-additional.md "multi-region-global-primary-additional.md").
   - If you do not have any Regions showing under **Multi-Region
     replication**, choose the **Networking &
     security** tab.

4. In the **Client-side LDAPS** section, under **CA
   certificates**, information about the certificate will be displayed.

###### Method 2: To view certificate details in Directory Service (AWS CLI)

- Run the following command. For the certificate ID, use the identifier returned by
  `register-certificate` or `list-certificates`.

```
aws ds describe-certificate --directory-id `your_directory_id` --certificate-id `your_cert_id`
```

### Deregister a certificate

Use either of the following methods to deregister a certificate.

###### Note

If only one certificate is registered, you must first disable LDAPS before you can
deregister the certificate.

###### Method 1: To deregister a certificate in Directory Service (AWS Management Console)

1. In the [AWS Directory Service console](https://console.aws.amazon.com/directoryservicev2/ "https://console.aws.amazon.com/directoryservicev2/") navigation pane, select
   **Directories**.
2. Choose the directory ID link for your directory.
3. On the **Directory details** page, do one of the
   following:
   - If you have multiple Regions showing under **Multi-Region
     replication**, select the Region where you want to deregister a
     certificate, and then choose the **Networking &
     security** tab. For more information, see [Primary vs additional Regions](multi-region-global-primary-additional.md "multi-region-global-primary-additional.md").
   - If you do not have any Regions showing under **Multi-Region
     replication**, choose the **Networking &
     security** tab.

4. In the **Client-side LDAPS** section, choose
   **Actions**, and then choose **Deregister
   certificate**.
5. In the **Deregister a CA certificate** dialog box, choose
   **Deregister**.

###### Method 2: To deregister a certificate in Directory Service (AWS CLI)

- Run the following command. For the certificate ID, use the identifier returned by
  `register-certificate` or `list-certificates`.

```
aws ds deregister-certificate --directory-id `your_directory_id` --certificate-id `your_cert_id`
```

### Disable client-side LDAPS

Use either of the following methods to disable client-side LDAPS.

###### Method 1: To disable client-side LDAPS in Directory Service (AWS Management Console)

1. In the [AWS Directory Service console](https://console.aws.amazon.com/directoryservicev2/ "https://console.aws.amazon.com/directoryservicev2/") navigation pane, select
   **Directories**.
2. Choose the directory ID link for your directory.
3. On the **Directory details** page, do one of the
   following:
   - If you have multiple Regions showing under **Multi-Region
     replication**, select the Region where you want to disable client-side
     LDAPS, and then choose the **Networking &
     security** tab. For more information, see [Primary vs additional Regions](multi-region-global-primary-additional.md "multi-region-global-primary-additional.md").
   - If you do not have any Regions showing under **Multi-Region
     replication**, choose the **Networking &
     security** tab.

4. In the **Client-side LDAPS** section, choose
   **Disable**.
5. In the **Disable client-side LDAPS** dialog box, choose
   **Disable**.

###### Method 2: To disable client-side LDAPS in Directory Service (AWS CLI)

- Run the following command.

```
aws ds disable-ldaps --directory-id `your_directory_id` --type Client
```

## Certificate enrollment issues

The process to enroll your AWS Managed Microsoft AD domain controllers with the CA certificates can
take up to 30 minutes. If you experience issues with the certificate enrollment and want to
restart your AWS Managed Microsoft AD domain controllers, you can contact Support. To create a support case,
see [Creating
support cases and case management](../../../awssupport/latest/user/case-management.md "../../../awssupport/latest/user/case-management.md").
