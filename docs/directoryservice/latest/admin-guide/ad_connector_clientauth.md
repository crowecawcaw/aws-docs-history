# Enabling mTLS authentication in AD Connector for use

with smart cards

You can use certificate-based mutual Transport Layer Security (mTLS) authentication with
smart cards to authenticate users into Amazon WorkSpaces through your self-managed Active Directory (AD)
and AD Connector. When enabled, users select their smart card at the WorkSpaces login screen and
enter a PIN to authenticate, instead of using a username and password. From there, the Windows
or Linux virtual desktop uses the smart card to authenticate into AD from the native desktop OS.

###### Note

Smart card authentication in AD Connector is only available in the following
AWS Regions, and only with WorkSpaces. Other AWS applications are not supported at this
time.

- US East (N. Virginia)
- US West (Oregon)
- Asia Pacific (Sydney)
- Asia Pacific (Tokyo)
- Europe (Ireland)
- AWS GovCloud (US-West)
- AWS GovCloud (US-East)
  You can also deregister and disable the certificates.

###### Topics

- [Prerequisites](#prereqs-clientauth "#prereqs-clientauth")
- [Enabling smart card authentication](#enable-clientauth "#enable-clientauth")
- [Managing smart card authentication settings](manage-clientauth.md "manage-clientauth.md")

## Prerequisites

To enable certificate-based mutual Transport Layer Security (mTLS) authentication using
smart cards for the Amazon WorkSpaces client, you need an operational smart card infrastructure
integrated with your self-managed Active Directory. For more information on how to set up smart card
authentication with Amazon WorkSpaces and Active Directory, see the [Amazon WorkSpaces Administration Guide](../../../workspaces/latest/adminguide/smart-cards.md "../../../workspaces/latest/adminguide/smart-cards.md").

Before you enable smart card authentication for WorkSpaces, please review the following
prerequisites:

- [CA certificate requirements](#ca-cert "#ca-cert")
- [User certificate requirements](#user-cert "#user-cert")
- [Certificate revocation checking process](#ocsp "#ocsp")
- [Considerations](#other "#other")

### CA certificate requirements

AD Connector requires a certificate authority (CA) certificate, which represents the
issuer of your user certificates, for smart card authentication. AD Connector matches CA
certificates with the certificates presented by your users with their smart cards. Note the
following CA certificate requirements:

- Before you can register a CA certificate, it must be more than 90 days away from
  expiration.
- CA certificates must be in Privacy-Enhanced Mail (PEM) format. If you export CA
  certificates from inside Active Directory, choose Base64-encoded X.509 (.CER) as the
  export file format.
- All root and intermediary CA certificates that chain from an issuing CA to user
  certificates must be uploaded for smart card authentication to succeed.
- A maximum of 100 CA certificates can be stored per AD Connector directory
- AD Connector does not support the RSASSA-PSS signature algorithm for CA
  certificates.
- Verify the Certificate Propagation Service is set to Automatic and
  running.

### User certificate requirements

The following are some of the requirements for the user certificate:

- The user's smart card certificate has a Subject Alternative Name (SAN) of
  the user's userPrincipalName (UPN).
- The user's smart card certificate has Enhanced Key Usage as the smart
  card log-on (1.3.6.1.4.1.311.20.2.2) Client Authentication
  (1.3.6.1.5.5.7.3.2).
- The Online Certificate Status Protocol (OCSP) information for the
  user's smart card certificate should be Access Method=On-line
  Certificate Status Protocol (1.3.6.1.5.5.7.48.1) in the Authority
  Information Access.

For more information on AD Connector and smart card authentication
requirements, see [Requirements](../../../workspaces/latest/adminguide/smart-cards.md#smart-cards-requirements "../../../workspaces/latest/adminguide/smart-cards.md#smart-cards-requirements") in _Amazon WorkSpaces Administration Guide_. For help
troubleshooting Amazon WorkSpaces issues, like logging into WorkSpaces, resetting password,
or connecting to WorkSpaces, see [Troubleshoot
WorkSpaces client issues](../../../workspaces/latest/userguide/client_troubleshooting.md "../../../workspaces/latest/userguide/client_troubleshooting.md") in _Amazon WorkSpaces User Guide_.

### Certificate revocation checking process

In order to perform smart card authentication, AD Connector must check the revocation
status of user certificates using Online Certificate Status Protocol (OCSP). To perform
certificate revocation checking, an OCSP responder URL must be internet-accessible. If using
a DNS name, an OCSP responder URL must use a top-level domain found in the [Internet Assigned Numbers Authority (IANA) Root
Zone Database](https://www.iana.org/domains/root/db "https://www.iana.org/domains/root/db").

###### Note

Directories created after October 7, 2025, require that OCSP servers used for SmartCard certificate validation be routable through your VPC's network configuration. If your OCSP server is not accessible via your VPC's routing tables, security groups, and network ACLs, SmartCard authentication will fail during certificate revocation checks. To resolve this issue, please ensure that:

- Network Routing: Your VPC route tables allow traffic to reach your OCSP server from the subnets where your AD Connector directory instances are deployed.
- Security Groups: The security groups associated with your directory's network interfaces permit outbound traffic to your OCSP server on port 80 (HTTP).
- Network ACLs: Your subnet network ACLs allow bidirectional traffic to/from your OCSP server.
- Internet Gateway/NAT: If your OCSP server is internet-facing, ensure your VPC has appropriate internet gateway or NAT gateway configuration for the directory subnets. If your network type is IPv4, you will need to have NAT and internet gateway configured with your VPC.

AD Connector certificate revocation checking uses the following process:

- AD Connector must check the Authority Information Access (AIA) extension in the
  user certificate for an OCSP responder URL, then AD Connector uses the URL to check
  for revocation.
- If AD Connector cannot resolve the URL found in the user certificate AIA
  extension, or find an OCSP responder URL in the user certificate, then AD Connector
  uses the optional OCSP URL provided during root CA certificate registration.

If the URL in the user certificate AIA extension resolves but is unresponsive, then
user authentication fails.

- If the OCSP responder URL provided during root CA certificate registration cannot
  resolve, is unresponsive, or no OCSP responder URL was provided, user authentication
  fails.
- The OCSP server must be compliant with [RFC 6960](https://datatracker.ietf.org/doc/html/rfc6960 "https://datatracker.ietf.org/doc/html/rfc6960"). Additionally,
  the OCSP server must support requests using the GET method for requests that are less
  than or equal to 255 bytes in total.

###### Note

AD Connector requires an **HTTP** URL for the OCSP
responder URL.

### Considerations

Before enabling smart card authentication in AD Connector, consider the following
items:

- AD Connector uses certificate-based mutual Transport Layer Security authentication
  (mutual TLS) to authenticate users to Active Directory using hardware or software-based
  smart card certificates. Only common access cards (CAC) and personal identity
  verification (PIV) cards are supported at this time. Other types of hardware or
  software-based smart cards might work but have not been tested for use with the WorkSpaces
  Streaming Protocol.
- Smart card authentication replaces username and password authentication to
  WorkSpaces.

If you have other AWS applications configured on your AD Connector directory
with smart card authentication enabled, those applications still present the username
and password input screen.

- Enabling smart card authentication limits the user session length to the maximum
  lifetime for Kerberos service tickets. You can configure this setting using a Group
  Policy, and is set to 10 hours by default. For more information on this setting, see
  [Microsoft documentation](https://docs.microsoft.com/en-us/windows/security/threat-protection/security-policy-settings/maximum-lifetime-for-service-ticket "https://docs.microsoft.com/en-us/windows/security/threat-protection/security-policy-settings/maximum-lifetime-for-service-ticket").
- The AD Connector service account's supported Kerberos encryption type should match
  each of the domain controller's supported Kerberos encryption type.

## Enabling smart card authentication

To enable smart card authentication for WorkSpaces on your AD Connector, first you need to
import your certificate authority (CA) certificates into AD Connector. You can import your
CA certificates into AD Connector using AWS Directory Service console, [API](../devguide/welcome.md "../devguide/welcome.md") or [CLI](../../../cli/latest/reference/ds/index.md "../../../cli/latest/reference/ds/index.md"). Use the following
steps to import your CA certificates and subsequently enable smart card authentication.

###### Steps

- [Enabling Kerberos constrained delegation for the
  AD Connector service account](#step1 "#step1")
- [Registering the CA certificate in AD Connector](#step2 "#step2")
- [Enabling smart card authentication for supported AWS
  applications and services](#step3 "#step3")

### Enabling Kerberos constrained delegation for the

AD Connector service account

To use smart card authentication with AD Connector, you must enable **Kerberos Constrained Delegation (KCD)** for the AD Connector
Service account to the LDAP service in the self-managed AD directory.

Kerberos Constrained Delegation is a feature in Windows Server. This feature enables
administrators to specify and enforce application trust boundaries by limiting the scope
where application services can act on a user's behalf. For more information, see [Kerberos
constrained delegation](ms_ad_key_concepts_kerberos.md "ms_ad_key_concepts_kerberos.md").

###### Note

**Kerberos Constrained Delegation (KCD)** requires the username
portion of the AD Connector service account to match the sAMAccountName of the same
user. The sAMAccountName is restricted to 20 characters. sAMAccountName is a Microsoft
Active Directory attribute used as a sign in name for prior versions of Windows clients
and servers.

1. Use the `SetSpn` command to set a Service Principal Name (SPN) for the
   AD Connector service account in the self-managed AD. This enables the service account
   for delegation configuration.

The SPN can be any service or name combination but not a duplicate of an existing
SPN. The `-s` checks for duplicates.

```
**setspn -s my/spn *service\_account***
```

2. In **AD Users and Computers**, open the context (right-click) menu
   and choose the AD Connector service account and choose
   **Properties**.
3. Choose the **Delegation** tab.
4. Choose the **Trust this user for delegation to specified service
   only** and **Use any authentication protocol**
   options.
5. Choose **Add** and then **Users or Computers** to
   locate the domain controller.
6. Choose **OK** to display a list of available services used for
   delegation.
7. Choose the **ldap** service type and choose
   **OK**.
8. Choose **OK** again to save the configuration.
9. Repeat this process for other domain controllers in the Active Directory.
   Alternatively you can automate the process using PowerShell.

### Registering the CA certificate in AD Connector

Use either of the following methods to register a CA certificate for your AD Connector
directory.

###### Method 1: To register your CA certificate in AD Connector (AWS Management Console)

1. In the [AWS Directory Service console](https://console.aws.amazon.com/directoryservicev2/ "https://console.aws.amazon.com/directoryservicev2/") navigation pane, select
   **Directories**.
2. Choose the directory ID link for your directory.
3. On the **Directory details** page, choose the **Networking
   & security** tab.
4. In the **Smart card authentication** section, choose
   **Actions**, and then choose **Register
   certificate**.
5. In the **Register a certificate** dialog box, select
   **Choose file**, and then choose a certificate and choose
   **Open**. You can optionally choose to perform revocation checking
   for this certificate by providing an Online Certificate Status Protocol (OCSP) responder
   URL. For more information about OCSP, see [Certificate revocation checking process](#ocsp "#ocsp").
6. Choose **Register certificate**. When you see the certificate
   status change to **Registered**, the registration process has completed
   successfully.

###### Method 2: To register your CA certificate in AD Connector (AWS CLI)

- Run the following command. For the certificate data, point to the location of your
  CA certificate file. To provide a secondary OCSP responder address, use the optional
  `ClientCertAuthSettings` object.

```
aws ds register-certificate --directory-id `your_directory_id` --certificate-data file://`your_file_path` --type ClientCertAuth --client-cert-auth-settings OCSPUrl=http://`your_OCSP_address`
```

If successful, the response provides a certificate ID. You can also verify your CA
certificate registered successfully by running the following CLI command:

```
aws ds list-certificates --directory-id `your_directory_id`
```

If the status value returns `Registered`, you have successfully
registered your certificate.

### Enabling smart card authentication for supported AWS

applications and services

Use either of the following methods to register a CA certificate for your AD Connector
directory.

###### Method 1: To enable smart card authentication in AD Connector (AWS Management Console)

1. Navigate to the **Smart card authentication** section on the
   **Directory details** page, and choose **Enable**.
   If this option is not available, verify that a valid certificate has been successfully
   registered, and then try again.
2. In the **Enable smart card authentication** dialog box, select
   **Enable**.

###### Method 2: To enable smart card authentication in AD Connector (AWS CLI)

- Run the following command.

```
aws ds enable-client-authentication --directory-id `your_directory_id` --type SmartCard
```

If successful, AD Connector returns an `HTTP 200` response with an
empty HTTP body.

For more information on viewing your certificate, deregistering or
disabling your certificate, see [Managing smart card authentication settings](manage-clientauth.md "manage-clientauth.md").
