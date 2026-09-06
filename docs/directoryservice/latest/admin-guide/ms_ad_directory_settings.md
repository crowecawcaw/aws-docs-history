

# Editing AWS Managed Microsoft AD directory security settings
<a name="ms_ad_directory_settings"></a>

You can configure fine-grained directory settings for your AWS Managed Microsoft AD to meet your compliance and security requirements without any increase in operational workload. In directory settings, you can update secure channel configuration for protocols and ciphers used in your directory. For example, you have the flexibility to disable individual legacy ciphers, such as RC4 or DES, and protocols, such as SSL 2.0/3.0 and TLS 1.0/1.1. AWS Managed Microsoft AD then deploys the configuration to all domain controllers in your directory, manages domain controller reboots, and maintains this configuration as you scale out or deploy additional AWS Regions. For all available settings, see [List of directory security settings](#list-ds-settings).

## Edit directory security settings
<a name="edit-ds-settings"></a>

You can configure and edit settings for any of your directories.

**To edit directory settings**

1. Sign in to the AWS Management Console and open the Directory Service console at [https://console.aws.amazon.com/directoryservicev2/](https://console.aws.amazon.com/directoryservicev2/).

1. On the **Directories** page, choose your directory ID.

1. Under **Networking & security**, find **Directory settings**, and then choose **Edit settings**.

1. In **Edit settings**, change the **Value** for the settings that you want to edit. When you edit a setting, its status changes from **Default** to **Ready to Update**. If you have edited the setting previously, its status changes from **Updated** to **Ready to Update**. Then, choose **Review**.

1. In **Review and update settings**, see **Directory settings** and make sure that the new values are all correct. If you want to make any other changes to your settings, choose **Edit settings**. When you're satisfied with your changes and ready to implement the new values, choose **Update settings**. Then, you're taken back to the directory ID page.
**Note**  
Under **Directory settings**, you can view the **Status** of your updated settings. While settings are implemented, the **Status** displays **Updating**. You cannot edit other settings while a setting displays **Updating** under **Status**. The **Status** displays **Updated** if the setting successfully updates with your edit. The **Status** displays **Failed** if the setting fails to update with your edit. 

## Failed directory security settings
<a name="failed-ds-settings"></a>

If an error occurs during a settings update, the **Status** displays as **Failed**. In a failed status, the settings do not update to the new values, and the original values remain implemented. You can retry updating these settings or revert them to their previous values. 

**To resolve failed updated settings**
+ Under **Directory settings**, choose **Resolve failed settings**. Then, do one of the following:
  + To revert your settings back to their original value before the failure state, choose **Revert failed settings**. Then, choose **Revert** in the pop-up modal.
  + To retry updating your directory settings, choose **Retry failed settings**. If you want to make additional changes to your directory settings before retrying the failed updates, choose **Continue editing**. On **Review and retry failed updates**, choose **Update settings**.

## List of directory security settings
<a name="list-ds-settings"></a>

The following list shows the type, setting name, API name, potential values, and setting description for all available directory security settings.

TLS 1.2 and AES 256/256 are the default directory security settings if all other security settings are disabled. They cannot be disabled.




- **Authentication Protocol**
  - **Setting name:** NTLM V1 / **API name:** NTLM\_V1 / **Potential values:** Enable, Disable / **Setting description:** Enable or Disable NTLM V1 authentication for clients of your Active Directory domain controllers.
  - **Setting name:** NTLM Security Support Provider (SSP) Session Security / **API name:** NTLM\_SSP\_SESSION\_SECURITY / **Potential values:** Enable, Disable / **Setting description:** Enable or disable NTLM SSP session security to enforce encryption and signing for NTLM authentication sessions in your Active Directory domain controllers.

- **Encryption**
  - **Setting name:** FIPS Algorithm Policy
  - **API name:** FIPS\_ALGORITHM\_POLICY
  - **Potential values:** Enable, Disable
  - **Setting description:** Enable or disable the FIPS algorithm policy to enforce FIPS-compliant cryptographic algorithms for data protection in your Active directory.

- **Network Hardened Path**
  - **Setting name:** UNC Hardened Paths: Netlogon / **API name:** UNC\_HARDENED\_PATHS\_NETLOGON / **Potential values:** Maximum Security, Identity Verification Only, Tamper Protection Only, Encryption Only, Authentication with Integrity, Authentication with Encryption, Secure Data, No Protection / **Setting description:** Configure security requirements for UNC connections to the NETLOGON share.+ **Maximum Security**: Highest security with authentication, encryption, and signing.<br />+ **Identity Verification Only**: Both client and server authentication required.<br />+ **Tamper Protection Only**: Data integrity verification during transmission.<br />+ **Encryption Only**: Data encryption during transmission.<br />+ **Authentication with Integrity**: Authentication with data integrity checks.<br />+ **Authentication with Encryption**: Authentication with encryption.<br />+ **Secure Data**: Data integrity and encryption combined.<br />+ **No Protection**: No additional security requirements.
  - **Setting name:** UNC Hardened Paths: SYSVOL / **API name:** UNC\_HARDENED\_PATHS\_SYSVOL / **Potential values:** Maximum Security, Identity Verification Only, Tamper Protection Only, Encryption Only, Authentication with Integrity, Authentication with Encryption, Secure Data, No Protection / **Setting description:** Configure security requirements for UNC connections to the SYSVOL share.+ **Maximum Security**: Highest security with authentication, encryption, and signing.<br />+ **Identity Verification Only**: Both client and server authentication required.<br />+ **Tamper Protection Only**: Data integrity verification during transmission.<br />+ **Encryption Only**: Data encryption during transmission.<br />+ **Authentication with Integrity**: Authentication with data integrity checks.<br />+ **Authentication with Encryption**: Authentication with encryption.<br />+ **Secure Data**: Data integrity and encryption combined.<br />+ **No Protection**: No additional security requirements.

- **Certificate Based Authentication**
  - **Setting name:** Certificate Backdating Compensation / **API name:** CERTIFICATE\_BACKDATING\_COMPENSATION / **Potential values:** Years: 0 to 50<br />Months: 0 to 11<br />Days: 0 to 30<br />Hours: 0 to 23<br />Minutes: 0 to 59<br />Seconds: 0 to 59 / **Setting description:** Specify a value to indicate the length of time that a certificate can predate a user in Active Directory and still be used for authentication in Active Directory. The default value is 10 minutes. You can set this value from 1 second to 50 years.<br />To configure this setting, you must select the **Compatibility **type for **Strong Certificate Binding Enforcement**.<br />For more information, see [KB5014754—Certificate-based authentication changes on Windows domain controllers](https://support.microsoft.com/en-us/topic/kb5014754-certificate-based-authentication-changes-on-windows-domain-controllers-ad2c23b0-15d8-4340-a468-4d4f3b188f16) in the Microsoft Support documentation.
  - **Setting name:** Certificate Strong Enforcement / **API name:** CERTIFICATE\_STRONG\_ENFORCEMENT / **Potential values:** Compatibility, Full Enforcement / **Setting description:** Specify either of the following enforcement types:+ **Compatibility **: Authentication is allowed if a certificate can't be strongly mapped to a user. If the certificate predates the user account in Active Directory, you must also set **Certificate Backdating Compensation**, or authentication will fail.<br />+ **Full Enforcement**(default): Authentication isn't allowed if a certificate can't be strongly mapped to a user. If you choose this enforcement type, **Certificate Backdating Compensation** can't be configured.<br />For more information, see [KB5014754—Certificate-based authentication changes on Windows domain controllers](https://support.microsoft.com/en-us/topic/kb5014754-certificate-based-authentication-changes-on-windows-domain-controllers-ad2c23b0-15d8-4340-a468-4d4f3b188f16) in the Microsoft Support documentation.

- **Secure Channel: Cipher**
  - **Setting name:** AES 128/128 / **API name:** AES\_128\_128 / **Potential values:** Enable, Disable / **Setting description:** Enable or disable the AES 128/128 encryption cipher for secure channel communications between domain controllers in your directory.
  - **Setting name:** DES 56/56 / **API name:** DES\_56\_56 / **Potential values:** Enable, Disable / **Setting description:** Enable or disable the DES 56/56 encryption cipher for secure channel communications between domain controllers in your directory.
  - **Setting name:** RC2 40/128 / **API name:** RC2\_40\_128 / **Potential values:** Enable, Disable / **Setting description:** Enable or disable the RC2 40/128 encryption cipher for secure channel communications between domain controllers in your directory.
  - **Setting name:** RC2 56/128 / **API name:** RC2\_56\_128 / **Potential values:** Enable, Disable / **Setting description:** Enable or disable the RC2 56/128 encryption cipher for secure channel communications between domain controllers in your directory.
  - **Setting name:** RC2 128/128 / **API name:** RC2\_128\_128 / **Potential values:** Enable, Disable / **Setting description:** Enable or disable the RC2 128/128 encryption cipher for secure channel communications between domain controllers in your directory.
  - **Setting name:** RC4 40/128 / **API name:** RC4\_40\_128 / **Potential values:** Enable, Disable / **Setting description:** Enable or disable the RC4 40/128 encryption cipher for secure channel communications between domain controllers in your directory.
  - **Setting name:** RC4 56/128 / **API name:** RC4\_56\_128 / **Potential values:** Enable, Disable / **Setting description:** Enable or disable the RC4 56/128 encryption cipher for secure channel communications between domain controllers in your directory.
  - **Setting name:** RC4 64/128 / **API name:** RC4\_64\_128 / **Potential values:** Enable, Disable / **Setting description:** Enable or disable the RC4 64/128 encryption cipher for secure channel communications between domain controllers in your directory.
  - **Setting name:** RC4 128/128 / **API name:** RC4\_128\_128 / **Potential values:** Enable, Disable / **Setting description:** Enable or disable the RC4 128/128 encryption cipher for secure channel communications between domain controllers in your directory.
  - **Setting name:** Triple DES 168/168 / **API name:** 3DES\_168\_168 / **Potential values:** Enable, Disable / **Setting description:** Enable or disable the Triple DES 168/168 encryption cipher for secure channel communications between domain controllers in your directory.

- **Secure Channel: Protocol**
  - **Setting name:** PCT 1.0 / **API name:** PCT\_1\_0 / **Potential values:** Enable, Disable / **Setting description:** Enable or disable the PCT 1.0 protocol for secure channel communications (Server and Client) on the domain controllers in your directory.
  - **Setting name:** SSL 2.0 / **API name:** SSL\_2\_0 / **Potential values:** Enable, Disable / **Setting description:** Enable or disable the SSL 2.0 protocol for secure channel communications (Server and Client) on the domain controllers in your directory.
  - **Setting name:** SSL 3.0 / **API name:** SSL\_3\_0 / **Potential values:** Enable, Disable / **Setting description:** Enable or disable the SSL 3.0 protocol for secure channel communications (Server and Client) on the domain controllers in your directory.
  - **Setting name:** TLS 1.0 / **API name:** TLS\_1\_0 / **Potential values:** Enable, Disable / **Setting description:** Enable or disable the TLS 1.0 protocol for secure channel communications (Server and Client) on the domain controllers in your directory.
  - **Setting name:** TLS 1.1 / **API name:** TLS\_1\_1 / **Potential values:** Enable, Disable / **Setting description:** Enable or disable the TLS 1.1 protocol for secure channel communications (Server and Client) on the domain controllers in your directory.

