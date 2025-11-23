# Manage your CA certificates

This section describes common tasks for managing your own certificate
authority (CA) certificates.

You can register your certificate authority (CA) with AWS IoT if you are
using client certificates signed by a CA that AWS IoT doesn't
recognize.

If you want clients to automatically register their client certificates
with AWS IoT when they first connect, the CA that signed the client
certificates must be registered with AWS IoT. Otherwise, you don't need to
register the CA certificate that signed the client certificates.

###### Note

A CA certificate can be registered in `DEFAULT` mode by
only one account in a Region. A CA certificate can be registered in
`SNI_ONLY` mode by multiple accounts in a Region.

###### Topics:

- [Create a CA certificate](#create-your-CA-cert "#create-your-CA-cert")
- [Register your CA certificate](#register-CA-cert "#register-CA-cert")
- [Deactivate a CA certificate](#deactivate-ca-cert "#deactivate-ca-cert")

## Create a CA certificate

If you do not have a CA certificate, you can use [OpenSSL v1.1.1i](https://www.openssl.org/ "https://www.openssl.org/") tools to
create one.

###### Note

You can't perform this procedure in the AWS IoT console.

###### To create a CA certificate using [OpenSSL v1.1.1i](https://www.openssl.org/ "https://www.openssl.org/")

tools

1. Generate a key pair.

```
`openssl genrsa -out `root_CA_key_filename.key` 2048`
```

2. Use the private key from the key pair to generate a CA
   certificate.

```
`openssl req -x509 -new -nodes \
 -key `root_CA_key_filename.key` \
 -sha256 -days 1024 \
 -out `root_CA_cert_filename.pem``
```

## Register your CA certificate

These procedures describe how to register a certificate from a
certificate authority (CA) that's not Amazon's CA. AWS IoT Core uses CA
certificates to verify the ownership of certificates. To use device
certificates signed by a CA that's not Amazon's CA, you must register
the CA certificate with AWS IoT Core so that it can verify the device
certificate's ownership.

### Register a CA

certificate (console)

###### Note

To register a CA certificate in the console, start in the
console at [Register CA
certificate](https://console.aws.amazon.com//iot/home#/create/cacertificate "https://console.aws.amazon.com//iot/home#/create/cacertificate"). You can register your CA in
Multi-account mode and without the need to provide a
verification certificate or access to the private key. A CA can
be registered in Multi-account mode by multiple AWS accounts
in the same AWS Region. You can register your CA in
Single-account mode by providing a verification certificate and
proof of ownership of CA’s private key.

### Register a CA certificate

(CLI)

You can register a CA certificate in `DEFAULT` mode
or `SNI_ONLY` mode. A CA can be registered in
`DEFAULT` mode by one AWS account in one
AWS Region. A CA can be registered in `SNI_ONLY`
mode by multiple AWS accounts in the same AWS Region. For
more information about CA certificate mode, see [certificateMode](../apireference/API_CACertificateDescription.md#iot-Type-CACertificateDescription-certificateMode "../apireference/API_CACertificateDescription.md#iot-Type-CACertificateDescription-certificateMode").

###### Note

We recommend that you register a CA in
`SNI_ONLY` mode. You don't need to provide a
verification certificate or access to the private key, and
you can register the CA by multiple AWS accounts in the
same AWS Region.

#### Register a CA

certificate in SNI_ONLY mode (CLI) - Recommended

**Prerequisites**

Make sure you have the following available on your
computer before you continue:

- The root CA's certificate file (referenced in the
  following example as
  `root_CA_cert_filename.pem`)
- [OpenSSL
  v1.1.1i](https://www.openssl.org/ "https://www.openssl.org/") or later

###### To register a CA certificate in `SNI_ONLY`

mode using the AWS CLI

1. Register the CA certificate with AWS IoT. Using the
   **register-ca-certificate**
   command, enter the CA certificate file name. For
   more information, see [register-ca-certificate](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iot/register-ca-certificate.html "https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iot/register-ca-certificate.html") in the
   _AWS CLI Command Reference_.

```
`aws iot register-ca-certificate \
 --ca-certificate file://`root_CA_cert_filename.pem` \
 --certificate-mode `SNI_ONLY``
```

If successful, this command returns the
`certificateId`. 2. At this point, the CA certificate has been
registered with AWS IoT but is inactive. The CA
certificate must be active before you can register
any client certificates that it has signed.

This step activates the CA certificate.

To activate the CA certificate, use the
**update-certificate** command as
follows. For more information, see [update-certificate](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iot/update-certificate.html "https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iot/update-certificate.html") in the
_AWS CLI Command Reference_.

```
`aws iot update-ca-certificate \
 --certificate-id `certificateId` \
 --new-status ACTIVE`
```

To see the status of the CA certificate, use the
**describe-ca-certificate** command. For
more information, see [describe-ca-certificate](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iot/describe-ca-certificate.html "https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iot/describe-ca-certificate.html") in the
_AWS CLI Command Reference_.

#### Register a CA

certificate in `DEFAULT` mode (CLI)

**Prerequisites**

Make sure you have the following available on your
computer before you continue:

- The root CA's certificate file (referenced in the
  following example as
  `root_CA_cert_filename.pem`)
- The root CA certificate's private key file
  (referenced in the following example as
  `root_CA_key_filename.key`)
- [OpenSSL
  v1.1.1i](https://www.openssl.org/ "https://www.openssl.org/") or later

###### To register a CA certificate in `DEFAULT`

mode using the AWS CLI

1. To get a registration code from AWS IoT, use
   **get-registration-code**. Save the
   returned `registrationCode` to use as the
   `Common Name` of the private key
   verification certificate. For more information, see
   [get-registration-code](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iot/get-registration-code.html "https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iot/get-registration-code.html") in the
   _AWS CLI Command Reference_.

```
`aws iot get-registration-code`
```

2. Generate a key pair for the private key
   verification certificate:

```
`openssl genrsa -out `verification_cert_key_filename.key` 2048`
```

3. Create a certificate signing request (CSR) for the
   private key verification certificate. Set the
   `Common Name` field of the certificate
   to the `registrationCode` returned by
   **get-registration-code**.

```
`openssl req -new \
 -key `verification_cert_key_filename.key` \
 -out `verification_cert_csr_filename.csr``
```

You are prompted for some information, including
the `Common Name` for the
certificate.

```
You are about to be asked to enter information that will be incorporated
into your certificate request.
What you are about to enter is what is called a Distinguished Name or a DN.
There are quite a few fields but you can leave some blank
For some fields there will be a default value,
If you enter '.', the field will be left blank.
-----
Country Name (2 letter code) [AU]:
    State or Province Name (full name) []:
    Locality Name (for example, city) []:
    Organization Name (for example, company) []:
    Organizational Unit Name (for example, section) []:
    Common Name (e.g. server FQDN or YOUR name) []:`your_registration_code`
    Email Address []:

    Please enter the following 'extra' attributes
    to be sent with your certificate request
    A challenge password []:
    An optional company name []:
```

4. Use the CSR to create a private key verification
   certificate:

```
`openssl x509 -req \
 -in `verification_cert_csr_filename.csr` \
 -CA `root_CA_cert_filename.pem` \
 -CAkey `root_CA_key_filename.key` \
 -CAcreateserial \
 -out `verification_cert_filename.pem` \
 -days 500 -sha256`
```

5. Register the CA certificate with AWS IoT. Pass in
   the CA certificate file name and the private key
   verification certificate file name to the
   **register-ca-certificate**
   command, as follows. For more information, see
   [register-ca-certificate](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iot/register-ca-certificate.html "https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iot/register-ca-certificate.html") in the
   _AWS CLI Command Reference_.

```
`aws iot register-ca-certificate \
 --ca-certificate file://`root_CA_cert_filename.pem` \
 --verification-cert file://`verification_cert_filename.pem``
```

This command returns the
`certificateId`, if
successful. 6. At this point, the CA certificate has been
registered with AWS IoT but is not active. The CA
certificate must be active before you can register
any client certificates it has signed.

This step activates the CA certificate.

To activate the CA certificate, use the
**update-certificate** command as
follows. For more information, see [update-certificate](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iot/update-certificate.html "https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iot/update-certificate.html") in the
_AWS CLI Command Reference_.

```
`aws iot update-ca-certificate \
 --certificate-id `certificateId` \
 --new-status ACTIVE`
```

To see the status of the CA certificate, use the
**describe-ca-certificate** command. For
more information, see [describe-ca-certificate](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iot/describe-ca-certificate.html "https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iot/describe-ca-certificate.html") in the
_AWS CLI Command Reference_.

### Create a CA

verification certificate to register the CA certificate in the
console

###### Note

This procedure is only for use if you are registering a CA
certificate from the AWS IoT console.

If you did not come to this procedure from the AWS IoT console,
start the CA certificate registration process in the console at
[Register CA certificate](https://console.aws.amazon.com//iot/home#/create/cacertificate "https://console.aws.amazon.com//iot/home#/create/cacertificate").

Make sure you have the following available on the same computer
before you continue:

- The root CA's certificate file (referenced in the
  following example as
  `root_CA_cert_filename.pem`)
- The root CA certificate's private key file (referenced in
  the following example as
  `root_CA_key_filename.key`)
- [OpenSSL
  v1.1.1i](https://www.openssl.org/ "https://www.openssl.org/") or later

###### To use the command line interface to create a CA verification

certificate to register your CA certificate in the
console

1. Replace
   `verification_cert_key_filename.key`
   with the name of the verification certificate key file that
   you want to create (for example,
   `verification_cert.key`). Then run
   this command to generate a key pair for the private key
   verification certificate:

```
`openssl genrsa -out `verification_cert_key_filename.key` 2048`
```

2. Replace
   `verification_cert_key_filename.key`
   with the name of the key file that you created in step
1.

Replace
`verification_cert_csr_filename.csr`
with the name of the certificate signing request (CSR) file
that you want to create. For example,
`verification_cert.csr`.

Run this command to create the CSR file.

```
`openssl req -new \
 -key `verification_cert_key_filename.key` \
 -out `verification_cert_csr_filename.csr``
```

The command prompts you for additional information that's
explained later. 3. In the AWS IoT console, in the **Verification
certificate** container, copy the registration
code. 4. The information that the **openssl**
command prompts you for is shown in the following example.
Except for the `Common Name` field, you can enter
your own values or keep them blank.

In the `Common Name` field, paste the
registration code that you copied in the previous
step.

```
You are about to be asked to enter information that will be incorporated
into your certificate request.
What you are about to enter is what is called a Distinguished Name or a DN.
There are quite a few fields but you can leave some blank
For some fields there will be a default value,
If you enter '.', the field will be left blank.
-----
Country Name (2 letter code) [AU]:
    State or Province Name (full name) []:
    Locality Name (for example, city) []:
    Organization Name (for example, company) []:
    Organizational Unit Name (for example, section) []:
    Common Name (e.g. server FQDN or YOUR name) []:`your_registration_code`
    Email Address []:

    Please enter the following 'extra' attributes
    to be sent with your certificate request
    A challenge password []:
    An optional company name []:
```

After you finish, the command creates the CSR file. 5. Replace
`verification_cert_csr_filename.csr`
with the
`verification_cert_csr_filename.csr`
you used in the previous step.

Replace
`root_CA_cert_filename.pem`
with the file name of the CA certificate that you want to
register.

Replace
`root_CA_key_filename.key`
with the file name of the CA certificate's private key
file.

Replace
`verification_cert_filename.pem`
with the file name of the verification certificate that you
want to create. For example,
`verification_cert.pem`.

```
`openssl x509 -req \
 -in `verification_cert_csr_filename.csr` \
 -CA `root_CA_cert_filename.pem` \
 -CAkey `root_CA_key_filename.key` \
 -CAcreateserial \
 -out `verification_cert_filename.pem` \
 -days 500 -sha256`
```

6. After the OpenSSL command completes, you should have these
   files ready to use for when you return to the
   console.
   - Your CA certificate file
     (`root_CA_cert_filename.pem`
     used in the previous command)
   - The verification certificate that you created in
     the previous step
     (`verification_cert_filename.pem`
     used in the previous command)

## Deactivate a CA certificate

When a certificate authority (CA) certificate is enabled for automatic
client certificate registration, AWS IoT checks the CA certificate to make
sure the CA is `ACTIVE`. If the CA certificate is
`INACTIVE`, AWS IoT doesn't allow the client certificate to
be registered.

By setting the CA certificate to `INACTIVE`, you prevent
any new client certificates issued by the CA from being registered
automatically.

###### Note

Any registered client certificates that were signed by the
compromised CA certificate continue to work until you explicitly
revoke each one of them.

### Deactivate a CA

certificate (console)

###### To deactivate a CA certificate using the AWS IoT

console

1. Sign in to the AWS Management Console and open the [AWS IoT
   console](https://console.aws.amazon.com/iot/home "https://console.aws.amazon.com/iot/home").
2. In the left navigation pane, choose
   **Secure**, choose
   **CAs**.
3. In the list of certificate authorities, find the one that
   you want to deactivate, and choose the ellipsis icon to open
   the option menu.
4. On the option menu, choose
   **Deactivate**.

The certificate authority should show as
**Inactive** in the list.

###### Note

The AWS IoT console does not provide a way to list the
certificates that were signed by the CA you deactivated. For an
AWS CLI option to list those certificates, see [Deactivate a CA certificate
(CLI)](#deactivate-ca-cert-cli "#deactivate-ca-cert-cli").

### Deactivate a CA certificate

(CLI)

The AWS CLI provides the [**update-ca-certificate**](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iot/update-ca-certificate.html "https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iot/update-ca-certificate.html") command to
deactivate a CA certificate.

```
`aws iot update-ca-certificate \
 --certificate-id `certificateId` \
 --new-status INACTIVE`
```

Use the [**list-certificates-by-ca**](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iot/list-certificates-by-ca.html "https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iot/list-certificates-by-ca.html") command
to get a list of all registered client certificates that were signed
by the specified CA. For each client certificate signed by the
specified CA certificate, use the [**update-certificate**](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iot/update-certificate.html "https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iot/update-certificate.html") command to
revoke the client certificate to prevent it from being used.

Use the [**describe-ca-certificate**](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iot/describe-ca-certificate.html "https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iot/describe-ca-certificate.html") command
to see the status of the CA certificate.
