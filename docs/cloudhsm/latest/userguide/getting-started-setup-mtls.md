# Set up mutual TLS between client and AWS CloudHSM

(recommended)

The following topics describe the steps that you must complete to enable the mutual
Transport Layer Security (mTLS) between client and AWS CloudHSM.

###### Considerations

- Currently this feature is exclusively available on hsm2m.medium. For more
  information about HSM type, see [AWS CloudHSM cluster modes](cluster-hsm-types.md "cluster-hsm-types.md").
- mTLS is not supported for AWS CloudHSM key stores used with AWS Key Management Service.

###### Topics

- [Step 1. Create and
  register a trust anchor onto the HSM](#setup-mtls-create-and-register-trust-anchor "#setup-mtls-create-and-register-trust-anchor")
- [Step 2. Enable mTLS for AWS CloudHSM](#getting-start-setup-mtl-sdk "#getting-start-setup-mtl-sdk")
- [Step 3. Set the mTLS enforcement
  for AWS CloudHSM](#getting-start-setup-mtls-enforcement "#getting-start-setup-mtls-enforcement")

## Step 1. Create and

register a trust anchor onto the HSM

A trust anchor must be created and registered onto the HSM before enabling mTLS. This
is a two-step process:

######

- [Create a private key and
  self-signed root certificate](#setup-mtls-create-trust-anchor "#setup-mtls-create-trust-anchor")
- [Register the trust anchor onto
  the HSM](#setup-mtls-register-trust-anchor "#setup-mtls-register-trust-anchor")

### Create a private key and

self-signed root certificate

###### Note

For a production cluster, the key you are about to create should be created in
a secure manner using a trusted source of randomness. We recommend that you use
a secured offsite and offline HSM or the equivalent. Store the key
safely.

For development and testing, you can use any convenient tool (such as OpenSSL)
to create the key and self-sign a root certificate. You will need the key and
root certificate to sign the client certificate in the [enable mTLS for AWS CloudHSM](#getting-start-setup-mtl-sdk "#getting-start-setup-mtl-sdk").

The following examples show how to create a private key and self-signed root
certificate with [OpenSSL](https://www.openssl.org/ "https://www.openssl.org/").

###### Example – Create a private key with OpenSSL

Use the following command to create a 4096-bit RSA key encrypted with the
AES-256 algorithm. To use this example, replace
`<mtls_ca_root_1.key>` with the name of the
file where you want to store the key.

```
`$` `openssl genrsa -out `<mtls_ca_root_1.key>` -aes256 4096``Generating RSA private key, 4096 bit long modulus
.....................................+++
.+++
e is 65537 (0x10001)
Enter pass phrase for mtls_ca_root_1.key:
Verifying - Enter pass phrase for mtls_ca_root_1.key:`
```

###### Example – Create a self-signed root certificate with OpenSSL

Use the following command to create a self-signed root certificate named
`mtls_ca_root_1.crt` from the private key you just
created. The certificate is valid for 25 years (9130 days). Read the on-screen
instructions and follow the prompts.

```
`$` `openssl req -new -x509 -days 9130 -key mtls_ca_root_1.key -out mtls_ca_root_1.crt`
`Enter pass phrase for mtls_ca_root_1.key:
You are about to be asked to enter information that will be incorporated
into your certificate request.
What you are about to enter is what is called a Distinguished Name or a DN.
There are quite a few fields but you can leave some blank
For some fields there will be a default value,
If you enter '.', the field will be left blank.
-----
Country Name (2 letter code) [AU]:
State or Province Name (full name) [Some-State]:
Locality Name (eg, city) []:
Organization Name (eg, company) [Internet Widgits Pty Ltd]:
Organizational Unit Name (eg, section) []:
Common Name (e.g. server FQDN or YOUR name) []:
Email Address []:`
```

### Register the trust anchor onto

the HSM

After creating a self-signed root certificate, the admin must register it as the
trust anchor with the AWS CloudHSM cluster.

###### To register a trust anchor with the HSM

1. Use the following command to start CloudHSM CLI:

Linux

```
`$` `/opt/cloudhsm/bin/cloudhsm-cli interactive`
```

Windows

```
`PS C:\>` `& "C:\Program Files\Amazon\CloudHSM\bin\cloudhsm-cli.exe" interactive`
```

2. Using CloudHSM CLI, log in as an admin.

```
`aws-cloudhsm >` `login --username `<admin>` --role admin``Enter password:
{
 "error_code": 0,
 "data": {
 "username": "`<admin>`",
 "role": "admin"
 }
}`
```

3. Use the **[Register a trust anchor
   with CloudHSM CLI](cloudhsm_cli-cluster-mtls-register-trust-anchor.md "cloudhsm_cli-cluster-mtls-register-trust-anchor.md")** command to register the trust anchor. For more information, see
   the following example or use the **help cluster mtls
   register-trust-anchor** command.

###### Example – Register a trust anchor with AWS CloudHSM cluster

The following example shows how to use the **cluster mtls
register-trust-anchor** command in CloudHSM CLI to register an trust
anchor onto the HSM. To use this command, the admin must be logged in to the
HSM. Replace these values with your own:

```
`aws-cloudhsm >` `cluster mtls register-trust-anchor --path `</path/mtls_ca_root_1.crt>``
`{
 "error_code": 0,
 "data": {
 "trust_anchor": {
 "certificate-reference": "0x01",
 "certificate": "`<PEM Encoded Certificate>`",
 "cluster-coverage": "full"
 }
 }
}`
```

###### Note

AWS CloudHSM supports registering intermediate certificates as trust anchor. In
such cases, the entire PEM-encoded certificate chain file needs to be
registered onto the HSM, with the certificates in hierarchical order.

AWS CloudHSM supports a certificate chain of 6980 bytes.

After successfully registering the trust anchor, you can run the
**cluster mtls list-trust-anchors** command to check the
current registered trust anchors, as shown below:

```
`aws-cloudhsm >` `cluster mtls list-trust-anchors`
`{
 "error_code": 0,
 "data": {
 "trust_anchors": [
 {
 "certificate-reference": "0x01",
 "certificate": "`<PEM Encoded Certificate>`",
 "cluster-coverage": "full"
 }
 ]
 }
}`
```

###### Note

The maximum number of trust anchors can be registered onto hsm2m.medium
is two (2).

## Step 2. Enable mTLS for AWS CloudHSM

To enable the mTLS for AWS CloudHSM, you need to create a private key and a client
certificate signed by the root certificate we generated in [Create and register a trust
anchor onto the HSM](#setup-mtls-create-and-register-trust-anchor "#setup-mtls-create-and-register-trust-anchor"), and then use any of the Client SDK 5 configure tool to
setup the private key path and client certificate chain path.

######

- [Create a private key and client certificate
  chain](#create-client-ssl "#create-client-ssl")
- [Configure mTLS for Client SDK 5](#enable-ssl-5 "#enable-ssl-5")

### Create a private key and client certificate

chain

###### Example – Create a private key with OpenSSL

Use the following command to create a 4096-bit RSA key. To use this example,
replace `<ssl-client.key>` with the name of the
file where you want to store the key.

```
`$` `openssl genrsa -out `<ssl-client.key>` 4096`
`Generating RSA private key, 4096 bit long modulus
.....................................+++
.+++
e is 65537 (0x10001)`
```

###### Example – Generate a certificate signing request (CSR) with OpenSSL

Use the following command to generate a certificate signing request (CSR) from
the private key you just created. Read the on-screen instructions and follow the
prompts.

```
`$` `openssl req -new -key `<ssl-client.key>` -out `<ssl-client.csr>``
`You are about to be asked to enter information that will be incorporated
into your certificate request.
What you are about to enter is what is called a Distinguished Name or a DN.
There are quite a few fields but you can leave some blank
For some fields there will be a default value,
If you enter '.', the field will be left blank.
-----
Country Name (2 letter code) [AU]:
State or Province Name (full name) [Some-State]:
Locality Name (eg, city) []:
Organization Name (eg, company) [Internet Widgits Pty Ltd]:
Organizational Unit Name (eg, section) []:
Common Name (e.g. server FQDN or YOUR name) []:
Email Address []:`
```

###### Example – Sign the CSR with the root certificate

Use the following command to sign the CSR with the root certificate we created
and registered in [Create and register a trust anchor onto the HSM](#setup-mtls-create-and-register-trust-anchor "#setup-mtls-create-and-register-trust-anchor") and create a client
certificate named `ssl-client.crt`. The certificate is valid
for 5 years (1826 days).

```
`$` `openssl x509 -req -days 1826 -in `<ssl-client.csr>` -CA `<mtls_ca_root_1.crt>` -CAkey `<mtls_ca_root_1.key>` -CAcreateserial -out `<ssl-client.crt>``

```

###### Example – Create a client certificate chain

Use the following command to combine the client certificate and root
certificate we created and registered in [Create and register a
trust anchor onto the HSM](#setup-mtls-create-and-register-trust-anchor "#setup-mtls-create-and-register-trust-anchor") and create a client certificate chain named
`ssl-client.pem`, which will be used to configure in next
step.

```
`$` `cat `<ssl-client.crt>` `<mtls_ca_root_1.crt>` > `<ssl-client.pem>``

```

###### Note

If you registered intermediate certificates in [Create and
register a trust anchor onto the HSM](#setup-mtls-create-and-register-trust-anchor "#setup-mtls-create-and-register-trust-anchor") as trust anchor, make sure
to combine the client certificate with the entire certificate chain to
create a client certificate chain.

### Configure mTLS for Client SDK 5

Use any of the Client SDK 5 configure tools to enable the mutual TLS by providing the
right client key path and client certificate chain path. For more information about
configure tool for Client SDK 5, see [AWS CloudHSM Client SDK 5 configure tool](configure-sdk-5.md "configure-sdk-5.md") .

PKCS #11 library

###### To use a custom certificate and key for TLS client-HSM mutual authentication with Client SDK 5 on Linux

1. Copy your key and certificate to the appropriate directory.

```
`$` `sudo cp ssl-client.pem `</opt/cloudhsm/etc>``
`$` `sudo cp ssl-client.key `</opt/cloudhsm/etc>``
```

2. Use the configure tool to specify `ssl-client.pem` and `ssl-client.key`.

```
`$` `sudo /opt/cloudhsm/bin/configure-pkcs11 \
 --client-cert-hsm-tls-file `</opt/cloudhsm/etc/ssl-client.pem>` \
 --client-key-hsm-tls-file `</opt/cloudhsm/etc/ssl-client.key>``
```

###### To use a custom certificate and key for TLS client-HSM mutual authentication with Client SDK 5 on Windows

1. Copy your key and certificate to the appropriate directory.

```
`cp ssl-client.pem `<C:\ProgramData\Amazon\CloudHSM\ssl-client.pem>`
cp ssl-client.key `<C:\ProgramData\Amazon\CloudHSM\ssl-client.key>``
```

2. With a PowerShell interpreter, use the configure tool to specify `ssl-client.pem` and `ssl-client.key`.

```
`PS C:\>` `& "C:\Program Files\Amazon\CloudHSM\bin\configure-pkcs11.exe" `
 --client-cert-hsm-tls-file `<C:\ProgramData\Amazon\CloudHSM\ssl-client.pem>` `
 --client-key-hsm-tls-file `<C:\ProgramData\Amazon\CloudHSM\ssl-client.key>``
```

OpenSSL Dynamic Engine

###### To use a custom certificate and key for TLS client-HSM mutual authentication with Client SDK 5 on Linux

1. Copy your key and certificate to the appropriate directory.

```
`$` `sudo cp ssl-client.pem `</opt/cloudhsm/etc>`
sudo cp ssl-client.key `</opt/cloudhsm/etc>``
```

2. Use the configure tool to specify `ssl-client.pem` and `ssl-client.key`.

```
`$` `sudo /opt/cloudhsm/bin/configure-dyn \
 --client-cert-hsm-tls-file `</opt/cloudhsm/etc/ssl-client.pem>` \
 --client-key-hsm-tls-file `</opt/cloudhsm/etc/ssl-client.key>``
```

Key Storage Provider (KSP)

###### To use a custom certificate and key for TLS client-HSM mutual authentication with Client SDK 5 on Windows

1. Copy your key and certificate to the appropriate directory.

```
`cp ssl-client.pem `<C:\ProgramData\Amazon\CloudHSM\ssl-client.pem>`
cp ssl-client.key `<C:\ProgramData\Amazon\CloudHSM\ssl-client.key>``
```

2. With a PowerShell interpreter, use the configure tool to specify `ssl-client.pem` and `ssl-client.key`.

```
`PS C:\>` `& "C:\Program Files\Amazon\CloudHSM\bin\configure-ksp.exe" `
 --client-cert-hsm-tls-file `<C:\ProgramData\Amazon\CloudHSM\ssl-client.pem>` `
 --client-key-hsm-tls-file `<C:\ProgramData\Amazon\CloudHSM\ssl-client.key>``
```

JCE provider

###### To use a custom certificate and key for TLS client-HSM mutual authentication with Client SDK 5 on Linux

1. Copy your key and certificate to the appropriate directory.

```
`$` `sudo cp ssl-client.pem `</opt/cloudhsm/etc>`
sudo cp ssl-client.key `</opt/cloudhsm/etc>``
```

2. Use the configure tool to specify `ssl-client.pem` and `ssl-client.key`.

```
`$` `sudo /opt/cloudhsm/bin/configure-jce \
 --client-cert-hsm-tls-file `</opt/cloudhsm/etc/ssl-client.pem>` \
 --client-key-hsm-tls-file `</opt/cloudhsm/etc/ssl-client.key>``
```

###### To use a custom certificate and key for TLS client-HSM mutual authentication with Client SDK 5 on Windows

1. Copy your key and certificate to the appropriate directory.

```
`cp ssl-client.pem `<C:\ProgramData\Amazon\CloudHSM\ssl-client.pem>`
cp ssl-client.key `<C:\ProgramData\Amazon\CloudHSM\ssl-client.key>``
```

2. With a PowerShell interpreter, use the configure tool to specify `ssl-client.pem` and `ssl-client.key`.

```
`PS C:\>` `& "C:\Program Files\Amazon\CloudHSM\bin\configure-jce.exe" `
 --client-cert-hsm-tls-file `<C:\ProgramData\Amazon\CloudHSM\ssl-client.pem>` `
 --client-key-hsm-tls-file `<C:\ProgramData\Amazon\CloudHSM\ssl-client.key>``
```

CloudHSM CLI

###### To use a custom certificate and key for TLS client-HSM mutual authentication with Client SDK 5 on Linux

1. Copy your key and certificate to the appropriate directory.

```
`$` `sudo cp ssl-client.pem `</opt/cloudhsm/etc>`
sudo cp ssl-client.key `</opt/cloudhsm/etc>``
```

2. Use the configure tool to specify `ssl-client.pem` and `ssl-client.key`.

```
`$` `sudo /opt/cloudhsm/bin/configure-cli \
 --client-cert-hsm-tls-file `</opt/cloudhsm/etc/ssl-client.pem>` \
 --client-key-hsm-tls-file `</opt/cloudhsm/etc/ssl-client.key>``
```

###### To use a custom certificate and key for TLS client-HSM mutual authentication with Client SDK 5 on Windows

1. Copy your key and certificate to the appropriate directory.

```
`cp ssl-client.pem `<C:\ProgramData\Amazon\CloudHSM\ssl-client.pem>`
cp ssl-client.key `<C:\ProgramData\Amazon\CloudHSM\ssl-client.key>``
```

2. With a PowerShell interpreter, use the configure tool to specify `ssl-client.pem` and `ssl-client.key`.

```
`PS C:\>` `& "C:\Program Files\Amazon\CloudHSM\bin\configure-cli.exe" `
 --client-cert-hsm-tls-file `<C:\ProgramData\Amazon\CloudHSM\ssl-client.pem>` `
 --client-key-hsm-tls-file `<C:\ProgramData\Amazon\CloudHSM\ssl-client.key>``
```

## Step 3. Set the mTLS enforcement

for AWS CloudHSM

After configuring with any of the Client SDK 5 configure tools, connection between client
and AWS CloudHSM will be mutual TLS in the cluster. However, removing the private key path and
client certificate chain path from the config file will turn the connection into regular
TLS again. You can use CloudHSM CLI to set the mtls enforcement in the cluster by
completing the following steps:

1. Use the following command to start CloudHSM CLI:

Linux

```
`$` `/opt/cloudhsm/bin/cloudhsm-cli interactive`
```

Windows

```
`PS C:\>` `& "C:\Program Files\Amazon\CloudHSM\bin\cloudhsm-cli.exe" interactive`
```

2. Using CloudHSM CLI, log in as an admin.

```
`aws-cloudhsm >` `login --username `<admin>` --role admin``Enter password:
{
 "error_code": 0,
 "data": {
 "username": "`<admin>`",
 "role": "admin"
 }
}`
```

###### Note

1.  Make sure you have configured the CloudHSM CLI and start the CloudHSM CLI
    under a mTLS connection.

2.  You must be logged in as the default admin user with username as
    **admin** before set mTLS enforcement.
3.  Use the **[Set the mTLS enforcement level
    with CloudHSM CLI](cloudhsm_cli-cluster-mtls-set-enforcement.md "cloudhsm_cli-cluster-mtls-set-enforcement.md")** command to set the enforcement. For more information, see the
    following example or use the **help cluster mtls
    set-enforcement** command.

###### Example – Set mTLS enforcement with AWS CloudHSM cluster

The following example shows how to use the **cluster mtls
set-enforcement** command in CloudHSM CLI to set the mTLS
enforcement with the HSM. To use this command, the admin with username as
admin must be logged in to the HSM.

```
`aws-cloudhsm >` `cluster mtls set-enforcement --level cluster``{
 "error_code": 0,
 "data": {
 "message": "Mtls enforcement level set to Cluster successfully"
 }
}`
```

###### Warning

After you enforce mTLS usage in the cluster, all existing non-mTLS
connections will be dropped and you can only connect to the cluster with
mTLS certificates.
