# Obtain the thumbprint for an

OpenID Connect identity provider

When you [create an OpenID Connect (OIDC)
identity provider](id_roles_providers_create_oidc.md "id_roles_providers_create_oidc.md") in IAM, IAM requires the thumbprint for the top intermediate
certificate authority (CA) that signed the certificate used by the external identity provider
(IdP). The thumbprint is a signature for the CA's certificate that was used to issue the
certificate for the OIDC-compatible IdP. When you create an IAM OIDC identity provider, you
are trusting identities authenticated by that IdP to have access to your AWS account. By using
the CA's certificate thumbprint, you trust any certificate issued by that CA with the same DNS
name as the one registered. This eliminates the need to update trusts in each account when you
renew the IdP's signing certificate.

###### Important

In most cases, the federation server uses two different certificates:

- The first establishes an HTTPS connection between AWS and your IdP. This should be
  issued by a well-known public root CA, such as AWS Certificate Manager. This enables the client to check
  the reliability and status of the certificate.
- The second is used to encrypt tokens, and should be signed by a private or public
  _root_ CA.
  You can create an IAM OIDC identity provider with [the AWS Command Line Interface, the Tools for Windows PowerShell, or the IAM API](id_roles_providers_create_oidc.md#manage-oidc-provider-cli "id_roles_providers_create_oidc.md#manage-oidc-provider-cli"). When you use these methods, you have the
  option to manually provide a thumbprint. If you choose not to include a thumbprint, IAM will
  retrieve the top intermediate CA thumbprint of the OIDC IdP server certificate. If you choose to
  include a thumbprint, you must obtain the thumbprint manually and supply it to AWS.

When you create an OIDC identity provider with [the IAM console](id_roles_providers_create_oidc.md "id_roles_providers_create_oidc.md"), IAM attempts to retrieve
the top intermediate CA thumbprint of the OIDC IdP server certificate for you.

We recommend that you also obtain the thumbprint for your OIDC IdP manually and verify that
IAM retrieved the correct thumbprint. For more information about obtaining certificate
thumbprints, see the following sections.

###### Note

AWS secures communication with OIDC identity providers (IdPs) using our library of
trusted root certificate authorities (CAs) to verify the JSON Web Key Set (JWKS)
endpoint's TLS certificate. If your OIDC IdP relies on a certificate that is not signed
by one of these trusted CAs, only then we secure communication using the thumbprints set in
the IdP's configuration. AWS will fall back to thumbprint verification if we are
unable to retrieve the TLS certificate or if TLS v1.3 is required.

## Obtain certificate thumbprint

You use a web browser and the OpenSSL command line tool to obtain the certificate thumbprint
for an OIDC provider. However, you do not need to manually obtain the certificate thumbprint to
create an IAM OIDC identity provider. You can use the following procedure to obtain the
certificate thumbprint of your OIDC provider.

###### To obtain the thumbprint for an OIDC IdP

1. Before you can obtain the thumbprint for an OIDC IdP, you need to obtain the OpenSSL
   command line tool. You use this tool to download the OIDC IdP certificate chain and produce
   a thumbprint of the final certificate in the certificate chain. If you need to install and
   configure OpenSSL, follow the instructions at [Install OpenSSL](#oidc-install-openssl "#oidc-install-openssl") and [Configure OpenSSL](#oidc-configure-openssl "#oidc-configure-openssl").
2. Start with the OIDC IdP URL (for example, `https://server.example.com`), and
   then add `/.well-known/openid-configuration` to form the URL for the IdP's
   configuration document, such as the following:

`https://`server.example.com`/.well-known/openid-configuration`

Open this URL in a web browser, replacing `server.example.com`
with your IdP server name. 3. In the displayed document, use your web browser **Find** feature to
locate the text `"jwks_uri"`. Immediately following the text
`"jwks_uri"`, there is a colon (:) followed by a URL. Copy the fully qualified
domain name of the URL. Do not include `https://` or any path that comes after
the top-level domain.

```
{
 "issuer": "https://accounts.example.com",
 "authorization_endpoint": "https://accounts.example.com/o/oauth2/v2/auth",
 "device_authorization_endpoint": "https://oauth2.exampleapis.com/device/code",
 "token_endpoint": "https://oauth2.exampleapis.com/token",
 "userinfo_endpoint": "https://openidconnect.exampleapis.com/v1/userinfo",
 "revocation_endpoint": "https://oauth2.exampleapis.com/revoke",
 "jwks_uri": "https://`www.exampleapis.com`/oauth2/v3/certs",
...

```

4. Use the OpenSSL command line tool to run the following command. Replace
   `keys.example.com` with the domain name you obtained in [Step 3](#thumbstep2 "#thumbstep2").

```
openssl s_client -servername `keys.example.com` -showcerts -connect `keys.example.com`:443
```

5. In your command window, scroll up until you see a certificate similar to the following
   example. If you see more than one certificate, find the last certificate displayed (at the
   end of the command output). This contains the certificate of the top intermediate CA in the
   certificate authority chain.

```
-----BEGIN CERTIFICATE-----
 MIICiTCCAfICCQD6m7oRw0uXOjANBgkqhkiG9w0BAQUFADCBiDELMAkGA1UEBhMC
 VVMxCzAJBgNVBAgTAldBMRAwDgYDVQQHEwdTZWF0dGxlMQ8wDQYDVQQKEwZBbWF6
 b24xFDASBgNVBAsTC0lBTSBDb25zb2xlMRIwEAYDVQQDEwlUZXN0Q2lsYWMxHzAd
 BgkqhkiG9w0BCQEWEG5vb25lQGFtYXpvbi5jb20wHhcNMTEwNDI1MjA0NTIxWhcN
 MTIwNDI0MjA0NTIxWjCBiDELMAkGA1UEBhMCVVMxCzAJBgNVBAgTAldBMRAwDgYD
 VQQHEwdTZWF0dGxlMQ8wDQYDVQQKEwZBbWF6b24xFDASBgNVBAsTC0lBTSBDb25z
 b2xlMRIwEAYDVQQDEwlUZXN0Q2lsYWMxHzAdBgkqhkiG9w0BCQEWEG5vb25lQGFt
 YXpvbi5jb20wgZ8wDQYJKoZIhvcNAQEBBQADgY0AMIGJAoGBAMaK0dn+a4GmWIWJ
 21uUSfwfEvySWtC2XADZ4nB+BLYgVIk60CpiwsZ3G93vUEIO3IyNoH/f0wYK8m9T
 rDHudUZg3qX4waLG5M43q7Wgc/MbQITxOUSQv7c7ugFFDzQGBzZswY6786m86gpE
 Ibb3OhjZnzcvQAaRHhdlQWIMm2nrAgMBAAEwDQYJKoZIhvcNAQEFBQADgYEAtCu4
 nUhVVxYUntneD9+h8Mg9q6q+auNKyExzyLwaxlAoo7TJHidbtS4J5iNmZgXL0Fkb
 FFBjvSfpJIlJ00zbhNYS5f6GuoEDmFJl0ZxBHjJnyp378OD8uTs7fLvjx79LjSTb
 NYiytVbZPQUQ5Yaxu2jXnimvw3rrszlaEXAMPLE=
 -----END CERTIFICATE-----
```

Copy the certificate (including the `-----BEGIN CERTIFICATE-----` and
`-----END CERTIFICATE-----` lines) and paste it into a text file. Then save the
file with the file name `certificate.crt`.

###### Note

The OIDC identity provider's certificate chain must start with the domain or issuer
URL, include any intermediate certificates (if present), and end with the root
certificate. If the certificate chain order is different or includes duplicate or
additional certificates, you will receive a signature mismatch error and STS fails to
validate the JSON Web Token (JWT). Correct the order of the certificates in the chain
returned from the server to resolve the error. For more information about certificate
chain standards, see [certificate_list in RFC 5246](https://www.rfc-editor.org/rfc/rfc5246#section-7.4.2 "https://www.rfc-editor.org/rfc/rfc5246#section-7.4.2") on the RFC Series website. 6. Use the OpenSSL command line tool to run the following command.

```
openssl x509 -in certificate.crt -fingerprint -sha1 -noout
```

Your command window displays the certificate thumbprint, which looks similar to the
following example:

```
SHA1 Fingerprint=99:0F:41:93:97:2F:2B:EC:F1:2D:DE:DA:52:37:F9:C9:52:F2:0D:9E
```

Remove the colon characters (:) from this string to produce the final thumbprint, like
this:

```
990F4193972F2BECF12DDEDA5237F9C952F20D9E
```

7. If you are creating the IAM OIDC identity provider with the AWS CLI, Tools for Windows PowerShell, or the IAM
   API, providing a thumbprint is optional. If you choose not to include a thumbprint during
   creation, IAM will retrieve the top intermediate CA thumbprint of the OIDC IdP server
   certificate. After the IAM OIDC identity provider is created, you can compare this
   thumbprint to the thumbprint retrieved by IAM.

If you are creating the IAM OIDC identity provider in the IAM console, the console
attempts to retrieve the top intermediate CA thumbprint of the OIDC IdP server certificate
for you. You can compare this thumbprint to the thumbprint retrieved by IAM. After the
IAM OIDC identity provider is created, you can view the thumbprint for the IAM OIDC
identity provider in the **Endpoint verification** tab on the OIDC provider
**Summary** console page.

###### Important

If the thumbprint you obtained does not match the one you see in the IAM OIDC
identity provider thumbprint details, you should not use the OIDC provider. Instead, you
should delete the created OIDC provider and then try again to create the OIDC provider
after some time has passed. Verify that the thumbprints match before you use the provider.
If the thumbprints still do not match after a second attempt, use the [IAM Forum](https://forums.aws.amazon.com/forum.jspa?forumID=76 "https://forums.aws.amazon.com/forum.jspa?forumID=76") to contact AWS.

## Install OpenSSL

If you don't already have OpenSSL installed, follow the instructions in this
section.

###### To install OpenSSL on Linux or Unix

1. Go to [OpenSSL: Source, Tarballs](https://openssl.org/source/ "https://openssl.org/source/")
   (https://openssl.org/source/).
2. Download the latest source and build the package.

###### To install OpenSSL on Windows

1. Go to [OpenSSL: Binary
   Distributions](https://wiki.openssl.org/index.php/Binaries "https://wiki.openssl.org/index.php/Binaries") (https://wiki.openssl.org/index.php/Binaries) for a list of sites from
   which you can install the Windows version.
2. Follow the instructions on your selected site to start the installation.
3. If you are asked to install the **Microsoft Visual C++ 2008 Redistributables** and it is not already installed on your system, choose the download link appropriate
   for your environment. Follow the instructions provided by the **Microsoft Visual C++
   2008 Redistributable Setup Wizard**.

###### Note

If you are not sure whether the Microsoft Visual C++ 2008 Redistributables is already
installed on your system, you can try installing OpenSSL first. The OpenSSL installer
displays an alert if the Microsoft Visual C++ 2008 Redistributables is not yet
installed. Make sure that you install the architecture (32-bit or 64-bit) that matches the
version of OpenSSL that you install. 4. After you have installed the Microsoft Visual C++ 2008 Redistributables, select the
appropriate version of the OpenSSL binaries for your environment and save the file locally.
Start the **OpenSSL Setup Wizard**. 5. Follow the instructions described in the **OpenSSL Setup Wizard**.

## Configure OpenSSL

Before you use OpenSSL commands, you must configure the operating system so that it has
information about the location where OpenSSL is installed.

###### To configure OpenSSL on Linux or Unix

1. At the command line, set the `OpenSSL_HOME` variable to the location of the
   OpenSSL installation:

```
`$` export OpenSSL_HOME=`path_to_your_OpenSSL_installation`
```

2. Set the path to include the OpenSSL installation:

```
`$` export PATH=$PATH:$OpenSSL_HOME/bin
```

###### Note

Any changes you make to environment variables with the `export` command are
valid only for the current session. You can make persistent changes to the environment variables
by setting them in your shell configuration file. For more information, see the documentation
for your operating system.

###### To configure OpenSSL on Windows

1. Open a **Command Prompt** window.
2. Set the `OpenSSL_HOME` variable to the location of the OpenSSL
   installation:

```
`C:\>` set OpenSSL_HOME=`path_to_your_OpenSSL_installation`
```

3. Set the `OpenSSL_CONF` variable to the location of the configuration file in
   your OpenSSL installation:

```
`C:\>` set OpenSSL_CONF=`path_to_your_OpenSSL_installation`\bin\openssl.cfg
```

4. Set the path to include the OpenSSL installation:

```
`C:\>` set Path=%Path%;%OpenSSL_HOME%\bin
```

###### Note

Any changes you make to Windows environment variables in a **Command
Prompt** window are valid only for the current command line session. You can
make persistent changes to the environment variables by setting them as system properties.
The exact procedures depend on what version of Windows you're using. (For example,
in Windows 7, open **Control Panel**, **System and
Security**, **System**. Then choose **Advanced
system settings**, **Advanced** tab,
**Environment Variables**.) For more information, see the Windows
documentation.
