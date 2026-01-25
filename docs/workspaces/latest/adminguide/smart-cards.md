# Use smart cards for authentication in WorkSpaces Personal

Windows and Linux WorkSpaces on DCV bundles allow the use of
[Common Access Card (CAC)](https://www.cac.mil/Common-Access-Card "https://www.cac.mil/Common-Access-Card")
and [Personal Identity Verification (PIV)](https://www.idmanagement.gov/university/piv/ "https://www.idmanagement.gov/university/piv/")
smart cards for authentication.

Amazon WorkSpaces supports the use of smart cards for both
_pre-session authentication_ and _in-session authentication_.
Pre-session authentication refers to smart card authentication that's performed while users
are logging in to their WorkSpaces. In-session authentication refers to authentication that's
performed after logging in.

For example, users can use smart cards for in-session authentication while working with
web browsers and applications. They can also use smart cards for actions that require
administrative permissions. For example, if the user has administrative permissions on their
Linux WorkSpace, they can use smart cards to authenticate themselves when running
`sudo` and `sudo -i` commands.

###### Contents

- [Requirements](#smart-cards-requirements "#smart-cards-requirements")
- [Limitations](#smart-cards-limitations "#smart-cards-limitations")
- [Directory configuration](#smart-cards-directory-config "#smart-cards-directory-config")
- [Enable smart cards for Windows WorkSpaces](#smart-cards-windows-workspaces "#smart-cards-windows-workspaces")
- [Enable smart cards for Ubuntu, Rocky Linux, and Red Hat Enterprise Linux WorkSpaces](#smart-cards-linux-workspaces "#smart-cards-linux-workspaces")
- [Enable smart cards for Amazon Linux 2 WorkSpaces](#smart-cards-amazon-linux-workspaces "#smart-cards-amazon-linux-workspaces")

## Requirements

- An Active Directory Connector (AD Connector) directory is required for pre-session authentication.
  AD Connector uses certificate-based mutual Transport Layer Security (mutual TLS) authentication
  to authenticate users to Active Directory using a hardware or software-based smart card certificate.
  For more information about how to configure your AD Connector and your on-premises directory,
  see [Directory configuration](#smart-cards-directory-config "#smart-cards-directory-config").
- To use a smart card with a Windows or Linux WorkSpace, the user must use the Amazon WorkSpaces Windows
  client version 3.1.1 or later, WorkSpaces macOS client version 3.1.5 or later, or WorkSpaces Ubuntu 22.04 client version 2024.1 or later (smart card authentication is not supported with WorkSpaces Ubuntu 20.04 client). For more
  information about using smart cards with the Windows and macOS clients, see
  [Smart Card Support](../userguide/smart_card_support.md "../userguide/smart_card_support.md") in the _Amazon WorkSpaces User Guide_.
- The root CA and smart card certificates must meet certain requirements. For
  more information, see [Enable mTLS authentication in AD Connector for use with smart cards](../../../directoryservice/latest/admin-guide/ad_connector_clientauth.md "../../../directoryservice/latest/admin-guide/ad_connector_clientauth.md")
  in the _AWS Directory Service Administration Guide_ and [Certificate Requirements](https://docs.microsoft.com/en-us/windows/security/identity-protection/smart-cards/smart-card-certificate-requirements-and-enumeration#certificate-requirements "https://docs.microsoft.com/en-us/windows/security/identity-protection/smart-cards/smart-card-certificate-requirements-and-enumeration#certificate-requirements") in the Microsoft documentation.

In addition to those requirements, user certificates employed for smart card authentication to
Amazon WorkSpaces must include the following attributes:

    + The AD user's userPrincipalName (UPN) in the subjectAltName (SAN) field of the certificate. We
     recommend issuing smart card certificates for the user's default UPN.


    ###### Note

    Amazon Linux 2 WorkSpaces rely on UPN for certificate-to-user mapping. Newer Linux WorkSpaces, like Ubuntu, Rocky Linux, and Red Hat Enterprise Linux WorkSpaces, support more secure [mapping methods](https://www.idmanagement.gov/implement/scl-windows/#step-4---account-linking "https://www.idmanagement.gov/implement/scl-windows/#step-4---account-linking").
    + The Client Authentication (1.3.6.1.5.5.7.3.2) Extended Key Usage (EKU) attribute.
    + The Smart Card Logon (1.3.6.1.4.1.311.20.2.2) EKU attribute.

- For pre-session authentication, Online Certificate Status Protocol (OCSP) is required for certificate
  revocation checking. For in-session authentication, OCSP is recommended, but not required.

###### Note

Ubuntu WorkSpaces, Rocky Linux WorkSpaces, and Red Hat Enterprise Linux WorkSpaces require OCSP for in-session authentication by default, and OCSP verification in these systems requires the OCSP responder to have NONCE extension enabled to prevent replay attacks. To disable NONCE extension, in-session OCSP verification must be disabled altogether. To disable OCSP verification in Ubuntu, Rocky Linux, and Red Hat Enterprise Linux WorkSpaces, create a new file `/etc/sssd/conf.d/disable-ocsp.conf`with the following content:

```
[sssd]
certificate_verification = no_ocsp
```

## Limitations

- Only the WorkSpaces Windows client application version 3.1.1 or later, the WorkSpaces macOS client
  application version 3.1.5 or later, and WorkSpaces Ubuntu 22.04 client application version 2024.1 or later are currently supported for smart card authentication. WorkSpaces Ubuntu 20.04 or earlier client application is not supported for smart card authentication.
- The WorkSpaces Windows client application 3.1.1 or later supports smart cards only when the client is
  running on a 64-bit version of Windows.
- Only AD Connector directories are currently supported for smart card authentication.
- In-session authentication is available in all Regions where DCV is
  supported. Pre-session authentication is available in the following
  Regions:
  - Asia Pacific (Sydney) Region
  - Asia Pacific (Tokyo) Region
  - Europe (Ireland) Region
  - AWS GovCloud (US-East) Region
  - AWS GovCloud (US-West) Region
  - US East (N. Virginia) Region
  - US West (Oregon) Region

- For in-session authentication and pre-session authentication on Linux or Windows WorkSpaces,
  only one smart card is currently allowed at a time. Simultaneous use of multiple cards may work, but is not supported.
- For pre-session authentication, enabling both smart card authentication and sign-in
  authentication on the same directory is not currently supported.
- Only CAC and PIV cards are supported at this time. Other types of hardware or software-based smart
  cards might also work, but they haven't been fully tested for use with DCV.

## Directory configuration

To enable smart card authentication, you must configure your AD Connector directory
and your on-premises directory in the following manner.

###### AD Connector directory configuration

Before you begin, make sure your AD Connector directory has been set up as described in
[AD Connector Prerequisites](../../../directoryservice/latest/admin-guide/prereq_connector.md "../../../directoryservice/latest/admin-guide/prereq_connector.md") in the _AWS Directory Service Administration Guide_.
In particular, make sure that you have opened up the necessary ports in your firewall.

To finish configuring your AD Connector directory, follow the instructions in [Enable mTLS authentication in AD Connector for use with smart cards](../../../directoryservice/latest/admin-guide/ad_connector_clientauth.md "../../../directoryservice/latest/admin-guide/ad_connector_clientauth.md") in the _AWS Directory Service Administration Guide_.

###### Note

Smart card authentication requires Kerberos Constrained Delegation (KCD) to function properly. KCD requires the username portion of the AD Connector service account to match
the sAMAccountName of the same user. A sAMAccountName can't exceed 20 characters.

###### On-premises directory configuration

In addition to configuring your AD Connector directory:

- Make sure that the certificates that are issued to the domain controllers for your on-premises
  directory have the "KDC Authentication" extended key usage (EKU) set. To do this,
  use the Active Directory Domain Services (AD DS) default Kerberos Authentication
  certificate template. Do not use a Domain Controller certificate template or a
  Domain Controller Authentication certificate template because those templates don't
  contain the necessary settings for smart card authentication.
- For Linux WorkSpaces, make sure that OCSP responder for the CA issuing smart card certificates has NONCE extension enabled.
  If it cannot be enabled, in-session OCSP verification will have to be disabled in Ubuntu, Rocky Linux, and Red Hat Enterprise Linux WorkSpaces. To disable OCSP verification, create a new file `/etc/sssd/conf.d/disable-ocsp.conf`with the following content:

```
[sssd]
certificate_verification = no_ocsp
```

## Enable smart cards for Windows WorkSpaces

For general guidance on how to enable smart card authentication on Windows, see
[Guidelines for enabling smart card logon with third-party certification authorities](https://docs.microsoft.com/troubleshoot/windows-server/windows-security/enabling-smart-card-logon-third-party-certification-authorities "https://docs.microsoft.com/troubleshoot/windows-server/windows-security/enabling-smart-card-logon-third-party-certification-authorities")
in the Microsoft documentation.

###### To detect the Windows lock screen and disconnect the session

To allow users to unlock Windows WorkSpaces that are enabled for smart card pre-session authentication when
the screen is locked, you can enable Windows lock screen detection in users' sessions. When the Windows lock
screen is detected, the WorkSpace session is disconnected, and the user can reconnect from the WorkSpaces client
by using their smart card.

You can enable disconnecting the session when the Windows lock screen is detected by using Group Policy settings.
For more information, see [Configure disconnect session on
screen lock for DCV](group_policy.md#gp_lock_screen_in_wsp "group_policy.md#gp_lock_screen_in_wsp").

###### To enable in-session or pre-session authentication

By default, Windows WorkSpaces are not enabled to support the use of smart cards for pre-session or
in-session authentication. If needed, you can enable in-session and pre-session authentication
for Windows WorkSpaces by using Group Policy settings. For more information, see
[Configure smart card redirection
for DCV](group_policy.md#gp_smart_cards_in_wsp "group_policy.md#gp_smart_cards_in_wsp").

To use pre-session authentication, in addition to updating the Group Policy settings, you must also
enable pre-session authentication through your AD Connector directory settings. For more information, follow the
instructions in [Enable mTLS authentication in AD Connector for use in smart cards](../../../directoryservice/latest/admin-guide/ad_connector_clientauth.md "../../../directoryservice/latest/admin-guide/ad_connector_clientauth.md") in the _AWS Directory Service Administration Guide_.

###### To enable users to use smart cards in a browser

If your users are using Chrome as their browser, no special configuration is required to use smart cards.

If your users are using Firefox as their browser, you can enable your users to use smart cards in Firefox
through Group Policy. You can use these [Firefox Group Policy templates](https://github.com/mozilla/policy-templates/tree/master/windows "https://github.com/mozilla/policy-templates/tree/master/windows") in GitHub.

For example, you can install the 64-bit version of [OpenSC](https://github.com/OpenSC/OpenSC/wiki "https://github.com/OpenSC/OpenSC/wiki")
for Windows to support PKCS #11, and then use the following Group Policy setting, where
`NAME_OF_DEVICE` is whatever value you want to use to identify PKCS #11,
such as `OpenSC`, and where `PATH_TO_LIBRARY_FOR_DEVICE` is
the path to the PKCS #11 module. This path should point to a library with a .DLL extension, such as
`C:\Program Files\OpenSC Project\OpenSC\pkcs11\onepin-opensc-pkcs11.dll`.

```
Software\Policies\Mozilla\Firefox\SecurityDevices\`NAME_OF_DEVICE` = `PATH_TO_LIBRARY_FOR_DEVICE`
```

###### Tip

If you're using OpenSC, you can also load the OpenSC `pkcs11` module into Firefox by
running the `pkcs11-register.exe` program. To run this program, either double-click the file
at `C:\Program Files\OpenSC Project\OpenSC\tools\pkcs11-register.exe`, or open a
Command Prompt window and run the following command:

```
"C:\Program Files\OpenSC Project\OpenSC\tools\pkcs11-register.exe"
```

To verify that the OpenSC `pkcs11` module has been loaded into Firefox, do the following:

1. If Firefox is already running, close it.
2. Open Firefox. Choose the menu button

![Firefox menu button](images/firefox-menu-button.png)

in the upper-right corner, and then choose **Options**. 3. On the **about:preferences** page, in the left navigation
pane, choose **Privacy & Security**. 4. Under **Certificates**, choose **Security Devices**. 5. In the **Device Manager** dialog box, you should see
**OpenSC smartcard framework (0.21)** in the left navigation, and
it should have the following values when you select it:

**Module**: `OpenSC smartcard framework (0.21)`

**Path**: `C:\Program Files\OpenSC Project\OpenSC\pkcs11\onepin-opensc-pkcs11.dll`

###### Troubleshooting

For information about troubleshooting smart cards, see [Certificate and configuration problems](https://docs.microsoft.com/troubleshoot/windows-server/windows-security/enabling-smart-card-logon-third-party-certification-authorities#certificate-and-configuration-problems "https://docs.microsoft.com/troubleshoot/windows-server/windows-security/enabling-smart-card-logon-third-party-certification-authorities#certificate-and-configuration-problems") in the Microsoft documentation.

Some common issues that can cause problems:

- Incorrect mapping of the slots to the certificates.
- Having multiple certificates on the smart card that can match the user. Certificates are matched using
  the following criteria:
  - The root CA for the certificate.
  - The `<KU>` and `<EKU>` fields of the certificate.
  - The UPN in the certificate subject.

- Having multiple certificates that have `<EKU>msScLogin` in their key usage.

In general, it's best to have only one certificate for smart card authentication that is mapped to the very
first slot in the smart card.

The tools for managing the certificates and keys on the smart card (such as removing or remapping the certificates
and keys) might be manufacturer-specific. For more information, see the documentation provided by the manufacturer
of your smart cards.

## Enable smart cards for Ubuntu, Rocky Linux, and Red Hat Enterprise Linux WorkSpaces

To enable the use of smart cards on Ubuntu, Rocky Linux, and Red Hat Enterprise Linux WorkSpaces, you need to include the root and all intermediate CA certificates in the WorkSpace image
for all CAs issuing smart cards, and for all CAs issuing domain controller certificates.

###### To obtain your CA certificate

You can obtain your CA certificate in several ways:

- You can use a CA certificate bundle of a third-party certification authority.
- You can export your own CA certificate by using the Web Enrollment site, which is either
  `http://`ip_address`/certsrv` or
  `http://`fqdn`/certsrv`, where `ip_address`
  and `fqdn` are the IP address and the fully qualified domain name
  (FQDN) of the CA server. For more information about using the Web Enrollment site, see
  [How to export a Root Certification Authority Certificate](https://docs.microsoft.com/troubleshoot/windows-server/identity/export-root-certification-authority-certificate "https://docs.microsoft.com/troubleshoot/windows-server/identity/export-root-certification-authority-certificate") in the Microsoft documentation.
- You can use the following procedure to export the CA certificate from a CA server
  that is running Active Directory Certificate Services (AD CS). For information about installing AD CS, see
  [Install the Certification Authority](https://docs.microsoft.com/windows-server/networking/core-network-guide/cncg/server-certs/install-the-certification-authority "https://docs.microsoft.com/windows-server/networking/core-network-guide/cncg/server-certs/install-the-certification-authority") in the Microsoft documentation.
  1.  Log into the CA server using an administrator account.
  2.  From the Windows **Start** menu, open a command prompt window (**Start**
      > **Windows System** > **Command Prompt**).
  3.  Use the following command to export the CA certificate to a new file, where
      ``rootca`.cer` is the name of the new file:

  ```
  certutil -ca.cert `rootca`.cer
  ```

  For more information about running certutil, see
  [certutil](https://docs.microsoft.com/windows-server/administration/windows-commands/certutil "https://docs.microsoft.com/windows-server/administration/windows-commands/certutil") in the Microsoft documentation. 4. Use the following OpenSSL command to convert the exported CA certificate from DER format
  to PEM format, where `rootca` is the name of the certificate. For more
  information about OpenSSL, see [www.openssl.org](https://www.openssl.org/ "https://www.openssl.org/").

  ```
  openssl x509 -inform der -in `rootca`.cer -out /tmp/`rootca`.pem
  ```

###### To add your CA certificates to your Linux WorkSpaces

To assist you with enabling smart cards, we've added the `enable_smartcard` script to our
Linux WorkSpaces DCV bundles. This script performs the following actions:

- Imports your CA certificates into a private PEM bundle that defines the trust root for SSSD on Linux WorkSpaces).
- Updates SSSD, PAM, and Kerberos configuration, which includes enabling `PKINIT` (Kerberos authentication using certificate instead of password) during WorkSpace
  provisioning.
  The following procedure explains how to use the
  `enable_smartcard` script to import your CA certificates and to enable smart card authentication for your Linux WorkSpaces.

1. Create a new Linux WorkSpace with the DCV protocol enabled. When launching the WorkSpace in the
   Amazon WorkSpaces console, on the **Select Bundles** page, be sure to select
   **DCV** for the protocol, and then select one of the Linux WorkSpaces public bundles.
2. On the newly created WorkSpace, make sure `/etc/skylight.conf` file has `pam_smartcard = true` line in `[features]` section:

```
[features]
pam_smartcard = true
```

###### Note

If not all your users are yet configured to use strong `altSecurityIdentities` certificate mapping, you can also add `smartcard_weak_mapping = true` line to the same `[features]` section in `/etc/skylight.conf` to support legacy mapping methods, but we recommend migrating those users to use strong mapping methods as soon as possible instead. 3. On the WorkSpace, run the following command as root, where `pem-path1`, `pem-path2`, etc.,
are the paths to files, each containing one of the CA certificates in the trust chain for the smart card and domain controller certificates. All of these files should be in PEM format and contain one certificate per file. Glob patterns can be used (e.g., `*.pem`)

```
/usr/lib/skylight/enable_smartcard --ca-cert `pem-path1` `pem-path2` `pem-path3` `...`
```

###### Note

Make sure additional dependency packages are installed on the WorkSpace before running the above command, using following commands as root.

For Rocky Linux and Red Hat Enterprise Linux WorkSpaces:

```
dnf install sssd-dbus libsss_simpleifp sssd-tools krb5-pkinit opensc
```

For Ubuntu WorkSpaces:

```
apt install krb5-pkinit opensc
```

4. Perform any additional customizations on the WorkSpace. For example, you might want to add a system-wide
   policy to [enable users to use smart cards in Firefox](#smart-cards-firefox-linux "#smart-cards-firefox-linux").
   (Chrome users must enable smart cards on their clients themselves. For more information, see
   [Smart Card Support](../userguide/smart_card_support.md "../userguide/smart_card_support.md") in the _Amazon WorkSpaces User Guide_.)
5. [Create a custom WorkSpace image and bundle](create-custom-bundle.md "create-custom-bundle.md")
   from the WorkSpace.
6. Use the new custom bundle to launch WorkSpaces for your users.

###### To enable users to use smart cards in Firefox

You can enable your users to use smart cards in Firefox by adding a SecurityDevices policy to your
Linux WorkSpace image. For more information about adding system-wide policies to Firefox, see the
[Mozilla policy templates](https://github.com/mozilla/policy-templates/releases "https://github.com/mozilla/policy-templates/releases") on GitHub.

1. On the WorkSpace that you're using to create your WorkSpace image, create a new file named `policies.json`
   in ``PREFIX`/firefox/distribution/`, where ``PREFIX``is`/usr/lib64`on Fedora-based systems (Amazon Linux 2, Red Hat Enterprise Linux, and Rocky Linux WorkSpaces), and`/usr/lib` on Debian-based systems (Ubuntu WorkSpaces).
2. In the JSON file, add the following SecurityDevices policy, where `NAME_OF_DEVICE`
   is whatever value you want to use to identify the `pkcs` module. For example, you might want to
   use a value such as `"OpenSC"`:

```
{
    "policies": {
        "SecurityDevices": {
            "`NAME_OF_DEVICE`": "`PREFIX`/opensc-pkcs11.so"
        }
    }
}
```

###### Troubleshooting

Troubleshooting of smart card authentication is easier when pre-session is set to use password authentication - during session provisioning Linux WorkSpaces automatically switch on-host authentication mode preference to password-based or smartcard-based depending on pre-session authentication method used. If there are any issues with smart card authentication, disconnecting and reconnecting using password pre-session authentication resets the workspace back to password on-host authentication. To manually switch Linux WorkSpaces instance to smart card authentication run `/usr/lib/skylight/resume_smartcard` command as root.

Linux WorkSpaces use OpenSC software for working with smart cards. That software comes with tools like `pkcs11-tool` and `pkcs15-tool` which can be useful in troubleshooting issues with smart cards. These tools can be used for inspecting smart card readers, individual tokens, and PIV slots or certificates on each smart card token.

An `openssl` command-line tool can be helpful in troubleshooting issues with trust chains, OCSP responders, or missing KUs/EKUs (key usage/extended key usage) flags, especially in combination with `pkcs15-tool`'s ability to extract public certificates from a smart card.

Common troubleshooting options:

- Extract first (usually PIV slot 9A) certificate from the smart card and save it as `card-cert.pem`: `pkcs15-tool --read-certificate 1 > `card-cert.pem``
- Validate the extracted certificate against trust database on the WorkSpace: `openssl verify -verbose -CAfile /etc/sssd/pki/sssd_auth_ca_db.pem -cert `card-cert.pem``
- Get OCSP URL from the extracted smart card certificate: `openssl x509 -noout -ocsp_uri -in `card-cert.pem``
- Verify that OCSP response indicates certificate is valid and includes NONCE: `openssl ocsp -issuer /etc/sssd/pki/sssd_auth_ca_db.pem -CAfile /etc/sssd/pki/sssd_auth_ca_db.pem -cert `card-cert.pem`-text -url`OCSP_URI``, where `OCSP_URI` is the OCSP URL from above.
- Check if domain controller certificate is considered trusted: `openssl s_client -connect `DC_HOSTNAME`:636 -showcerts | openssl verify -verbose -CAfile /etc/sssd/pki/sssd_auth_ca_db.pem`, where `DC_HOSTNAME` is the host name of one of the domain controllers in your Active Directory domain.
- Confirm domain controller certificate has KDC Authentication EKU (extended key usage) set: `openssl s_client -connect `DC_HOSTNAME`:636 -showcerts | openssl x509 -noout -text`.
- Attempt manual PKINIT to see if there are any error codes that can be used to narrow down the problem: `KRB5_TRACE=/dev/stdout kinit -X X509_user_identity=PKCS11:opensc-pkcs11.so:certid=`01` -V`, where `01` is the number of one of the four main PIV slots on the card - `01` for `9A`, `02` for `9C`, etc. Most cards will have certificate meant for user authentication in slot 9A.
- Check if system is able to map smart card certificate to an AD user (execute as root): `dbus-send --print-reply --system --dest=org.freedesktop.sssd.infopipe /org/freedesktop/sssd/infopipe/Users org.freedesktop.sssd.infopipe.Users.FindByCertificate string:"$(<`card-cert.pem`)"`. This can be combined with enabling debug logging for SSSD.

The most common known issues:

- Incomplete trust chain for the smart card certificate - when importing certificates using `enable_smartcard` script the full list of all root and intermediate CA certificates must to be provided. The `enable_smartcard` tool will show an error if not all imported certificates are trusted because of missing from the list root CA certificate, but it cannot detect when either an entire trust chain or the innermost intermediate CA certificate in one of the trust chains is missing. In that situation it will import certificates without an error, yet either a smart card certificate or domain controller certificates may still be considered untrusted.
- Missing trust chain for the domain controller certificates - if domain controller certificates are issued by a different CA than smart cards (e.g., in case of [Common Access Card (CAC)](https://www.cac.mil/Common-Access-Card "https://www.cac.mil/Common-Access-Card")), that CA trust chain needs to be imported together with the smart card issuing CA certificates.
- Lack of NONCE extension support in OCSP responder - Linux WorkSpaces require that OCSP responder of the smart card issuer has NONCE extension enabled. If it cannot be enabled, OCSP validation will have to be completely disabled.
- Domain controller certificates are missing `KDC Authentication` EKU (OID 1.3.6.1.5.2.3.1) - for smart card authentication to work domain controller certificates need to be re-issued to include KDC Authentication EKU.
- Domain controller certificates are expired - for smart card authentication to work domain controller certificates must remain up-to-date.
- Smart card certificates are mapped to users in AD using weak mapping methods - traditionally, UPN field in subjectAltName attribute was used to map a certificate to a user in AD, being expected to match userPrincipalName attribute. This is no longer considered a secure mapping method and is disallowed by default. It is possible to re-enable it by passing `--allow-weak-mapping` argument to `enable_smartcard` command and adding `smartcard_weak_mapping = true` line to the `[features]` section in `/etc/skylight.conf` file, but a better solution is to use one of the strong mapping methods. See [Account Linking](https://www.idmanagement.gov/implement/scl-windows/#step-4---account-linking "https://www.idmanagement.gov/implement/scl-windows/#step-4---account-linking") documentation for more details.

The tools for managing the certificates and keys on the smart card (such as removing or remapping the certificates
and keys) might be manufacturer-specific. Additional tools that you can use to work with smart cards are:

- `opensc-explorer`
- `opensc-tool`
- `pkcs11_inspect`
- `pkcs11_listcerts`
- `pkcs15-tool`

###### To enable debug logging

- Add `debug_level = `LEVEL``line in`/etc/sssd/sssd.conf`for each individual section, where`LEVEL`is the desired verbosity level, from 1 to 10. The logs for each corresponding section can then be found in`/var/log/sssd/` directory. See SSSD documentation [here](https://docs.pagure.org/sssd.sssd/users/troubleshooting.html#sssd-debug-logs "https://docs.pagure.org/sssd.sssd/users/troubleshooting.html#sssd-debug-logs") and [here](https://sssd.io/troubleshooting/basics.html#sssd-debug-logs "https://sssd.io/troubleshooting/basics.html#sssd-debug-logs") for more details.

## Enable smart cards for Amazon Linux 2 WorkSpaces

###### Note

Amazon Linux 2 WorkSpaces on DCV currently have the following limitations:

- Clipboard, audio-in, video-in, and time zone redirection aren't supported.
- Multiple monitors aren't supported.

To enable the use of smart cards on Amazon Linux 2 WorkSpaces, you need to include a root CA
certificate file in the PEM format in the WorkSpace image.

###### To obtain your root CA certificate

You can obtain your root CA certificate in several ways:

- You can use a root CA certificate operated by a third-party certification authority.
- You can export your own root CA certificate by using the Web Enrollment site, which is either
  `http://`ip_address`/certsrv` or
  `http://`fqdn`/certsrv`, where `ip_address`
  and `fqdn` are the IP address and the fully qualified domain name
  (FQDN) of the root certification CA server. For more information about using the Web Enrollment site, see
  [How to export a Root Certification Authority Certificate](https://docs.microsoft.com/troubleshoot/windows-server/identity/export-root-certification-authority-certificate "https://docs.microsoft.com/troubleshoot/windows-server/identity/export-root-certification-authority-certificate") in the Microsoft documentation.
- You can use the following procedure to export the root CA certificate from a root CA certification server
  that is running Active Directory Certificate Services (AD CS). For information about installing AD CS, see
  [Install the Certification Authority](https://docs.microsoft.com/windows-server/networking/core-network-guide/cncg/server-certs/install-the-certification-authority "https://docs.microsoft.com/windows-server/networking/core-network-guide/cncg/server-certs/install-the-certification-authority") in the Microsoft documentation.
  1.  Log into the root CA server using an administrator account.
  2.  From the Windows **Start** menu, open a command prompt window (**Start**
      > **Windows System** > **Command Prompt**).
  3.  Use the following command to export the root CA certificate to a new file, where
      ``rootca`.cer` is the name of the new file:

  ```
  certutil -ca.cert `rootca`.cer
  ```

  For more information about running certutil, see
  [certutil](https://docs.microsoft.com/windows-server/administration/windows-commands/certutil "https://docs.microsoft.com/windows-server/administration/windows-commands/certutil") in the Microsoft documentation. 4. Use the following OpenSSL command to convert the exported root CA certificate from DER format
  to PEM format, where `rootca` is the name of the certificate. For more
  information about OpenSSL, see [www.openssl.org](https://www.openssl.org/ "https://www.openssl.org/").

  ```
  openssl x509 -inform der -in `rootca`.cer -out /tmp/`rootca`.pem
  ```

###### To add your root CA certificate to your Amazon Linux 2 WorkSpaces

To assist you with enabling smart cards, we've added the `enable_smartcard` script to our
Amazon Linux DCV bundles. This script performs the following actions:

- Imports your root CA certificate into the
  [Network Security Services (NSS)](https://developer.mozilla.org/docs/Mozilla/Projects/NSS "https://developer.mozilla.org/docs/Mozilla/Projects/NSS") database.
- Installs the `pam_pkcs11` module for Pluggable Authentication Module (PAM) authentication.
- Performs a default configuration, which includes enabling `pkinit` during WorkSpace
  provisioning.
  The following procedure explains how to use the
  `enable_smartcard` script to add your root CA certificate to
  your Amazon Linux 2 WorkSpaces and to enable smart cards for your Amazon Linux 2 WorkSpaces.

1. Create a new Amazon Linux 2 WorkSpace with the DCV protocol enabled. When launching the WorkSpace in the
   Amazon WorkSpaces console, on the **Select Bundles** page, be sure to select
   **DCV** for the protocol, and then select one of the Amazon Linux 2 public bundles.
2. On the new WorkSpace, run the following command as root, where `pem-path`
   is the path to the root CA certificate file in PEM format.

```
/usr/lib/skylight/enable_smartcard --ca-cert `pem-path`
```

###### Note

Amazon Linux 2 WorkSpaces assume that the certificates on the smart cards are issued for the user's
default user principal name (UPN), such as ``sAMAccountName`@`domain``,
where `domain` is a fully qualified domain name (FQDN).

To use alternate UPN suffixes, `run /usr/lib/skylight/enable_smartcard --help` for more
information. The mapping for alternate UPN suffixes is unique to each user. Therefore, that mapping must
be performed individually on each user's WorkSpace. 3. (Optional) By default, all services are enabled to use smart card authentication on Amazon Linux 2 WorkSpaces. To limit smart
card authentication to only specific services, you must edit `/etc/pam.d/system-auth`.
Uncomment the `auth` line for `pam_succeed_if.so` and edit the list of services as
needed.

After the `auth` line is uncommented, to allow a service to use
smart card authentication, you must add it to the list. To make a service use
only password authentication, you must remove it from the list. 4. Perform any additional customizations to the WorkSpace. For example, you might want to add a system-wide
policy to [enable users to use smart cards in Firefox](#smart-cards-firefox-amazon-linux "#smart-cards-firefox-amazon-linux").
(Chrome users must enable smart cards on their clients themselves. For more information, see
[Smart Card Support](../userguide/smart_card_support.md "../userguide/smart_card_support.md") in the _Amazon WorkSpaces User Guide_.) 5. [Create a custom WorkSpace image and bundle](create-custom-bundle.md "create-custom-bundle.md")
from the WorkSpace. 6. Use the new custom bundle to launch WorkSpaces for your users.

###### To enable users to use smart cards in Firefox

You can enable your users to use smart cards in Firefox by adding a SecurityDevices policy to your
Amazon Linux 2 WorkSpace image. For more information about adding system-wide policies to Firefox, see the
[Mozilla policy templates](https://github.com/mozilla/policy-templates/releases "https://github.com/mozilla/policy-templates/releases") on GitHub.

1. On the WorkSpace that you're using to create your WorkSpace image, create a new file named `policies.json`
   in `/usr/lib64/firefox/distribution/`.
2. In the JSON file, add the following SecurityDevices policy, where `NAME_OF_DEVICE`
   is whatever value you want to use to identify the `pkcs` module. For example, you might want to
   use a value such as `"OpenSC"`:

```
{
    "policies": {
        "SecurityDevices": {
            "`NAME_OF_DEVICE`": "/usr/lib64/opensc-pkcs11.so"
        }
    }
}
```

###### Troubleshooting

For troubleshooting, we recommend adding the `pkcs11-tools` utility. This utility allows you to perform
the following actions:

- List each smart card.
- List the slots on each smart card.
- List the certificates on each smart card.

Some common issues that can cause problems:

- Incorrect mapping of the slots to the certificates.
- Having multiple certificates on the smart card that can match the user. Certificates are matched using
  the following criteria:
  - The root CA for the certificate.
  - The `<KU>` and `<EKU>` fields of the certificate.
  - The UPN in the certificate subject.

- Having multiple certificates that have `<EKU>msScLogin` in their key usage.

In general, it's best to have only one certificate for smart card authentication that is mapped to the very
first slot in the smart card.

The tools for managing the certificates and keys on the smart card (such as removing or remapping the certificates
and keys) might be manufacturer-specific. Additional tools that you can use to work with smart cards are:

- `opensc-explorer`
- `opensc-tool`
- `pkcs11_inspect`
- `pkcs11_listcerts`
- `pkcs15-tool`

###### To enable debug logging

To troubleshoot your `pam_pkcs11` and `pam-krb5` configuration, you can enable debug
logging.

1. In the `/etc/pam.d/system-auth-ac` file, edit the `auth` action and
   change the `nodebug` parameter of `pam_pksc11.so` to `debug`.
2. In the `/etc/pam_pkcs11/pam_pkcs11.conf` file, change `debug = false;`
   to `debug = true;`. The `debug` option applies separately to each mapper module,
   so you might need to change it both directly under the `pam_pkcs11` section and also under the
   appropriate mapper section (by default, this is `mapper generic`).
3. In the `/etc/pam.d/system-auth-ac` file, edit the `auth` action and add
   the `debug` or the `debug_sensitive` parameter to `pam_krb5.so`.

After you've enabled debug logging, the system prints out `pam_pkcs11` debug messages directly in
the active terminal. Messages from `pam_krb5` are logged in `/var/log/secure`.

To check which username a smart card certificate maps to, use the following `pklogin_finder` command:

```
sudo pklogin_finder debug config_file=/etc/pam_pkcs11/pam_pkcs11.conf
```

When prompted, enter the smart card PIN. `pklogin_finder` outputs on `stdout` the username on
the smart card certificate in the form ``NETBIOS`\`username``.
This username should match the WorkSpace username.

In Active Directory Domain Services (AD DS), the NetBIOS domain name is the pre-Windows 2000 domain name. Typically
(but not always), the NetBIOS domain name is the subdomain of the Domain Name System (DNS) domain name. For example,
if the DNS domain name is `example.com`, the NetBIOS domain name is usually `EXAMPLE`. If the
DNS domain name is `corp.example.com`, the NetBIOS domain name is usually `CORP`.

For example, for the user `mmajor` in the domain `corp.example.com`, the output from
`pklogin_finder` is `CORP\mmajor`.

###### Note

If you receive the message `"ERROR:pam_pkcs11.c:504: verify_certificate()
 failed"`, this message indicates that `pam_pkcs11` has found a
certificate on the smart card that matches the username criteria but that doesn't
chain up to a root CA certificate that is recognized by the machine. When that
happens, `pam_pkcs11` outputs the above message and then tries the next
certificate. It allows authentication only if it finds a certificate that both
matches the username and chains up to a recognized root CA certificate.

To troubleshoot your `pam_krb5` configuration, you can manually invoke `kinit` in debug mode with the
following command:

```
KRB5_TRACE=/dev/stdout kinit -V
```

This command should successfully obtain a Kerberos Ticket Granting Ticket (TGT). If it fails, try adding the
correct Kerberos principal name explicitly to the command. For example, for the user `mmajor` in the
domain `corp.example.com`, use this command:

```
KRB5_TRACE=/dev/stdout kinit -V mmajor
```

If this command succeeds, the issue is most likely in the mapping from the WorkSpace username to the Kerberos
principal name. Check the `[appdefaults]/pam/mappings` section in the `/etc/krb5.conf`
file.

If this command doesn't succeed, but a password-based `kinit` command does succeed, check the
`pkinit_`-related configurations in the `/etc/krb5.conf` file. For example, if the
smart card contains more than one certificate, you might need to make changes to `pkinit_cert_match`.
