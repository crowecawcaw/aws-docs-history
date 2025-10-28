# Configuring IPsec using certificate authentication

The following topics provide instructions for configuring IPsec encryption using certificate authentication on an FSx for ONTAP
file system and a client running Libreswan IPsec. This solution uses AWS Certificate Manager and AWS Private Certificate Authority to create a private certificate authority and for
generating the certificates.

The high-level steps for configuring IPsec encryption using certificate authentication on FSx for ONTAP file systems and connected clients are as follows:

1. Have a certificate authority in place for issuing certificates.
2. Generate and export CA certificates for the file system and client.
3. Install certificate and configure IPsec on the client instance.
4. Install certificate and configure IPsec on your file system.
5. Define the security policy database (SPD).
6. Configure IPsec for multiple client access.

## Creating and installing CA certificates

For certificate authentication, you need to generate and install certificates from a certificate authority on your FSx for ONTAP file system and the clients that will access the
data on your file system. The following example uses AWS Private Certificate Authority to set up a private certificate authority, and generate the certificates to
install on the file system and the client. Using AWS Private Certificate Authority, you can create an entirely AWS hosted hierarchy of root and subordinate certificate
authorities (CAs) for internal use by your organization. This process has five steps:

1. Create a private certificate authority (CA) using AWS Private CA
2. Issue and install the root certificate on the private CA
3. Request a private certificate from AWS Certificate Manager for your file system and clients
4. Export the certificate for the file system and clients.

For more information, see [Private CA administration](../../../privateca/latest/userguide/creating-managing.md "../../../privateca/latest/userguide/creating-managing.md")
in the AWS Private Certificate Authority User Guide.

###### To create the root private CA

1. When you create a CA, you must specify the CA configuration in a file that you supply. The following command uses
   the Nano text editor to create the `ca_config.txt` file, which specifies the following information:
   - The name of the algorithm
   - The signing algorithm that the CA uses to sign
   - X.500 subject information

```
`$ >` `nano ca_config.txt`
```

The text editor appears. 2. Edit the file with the specifications for your CA.

```
`{
 "KeyAlgorithm":"RSA_2048",
 "SigningAlgorithm":"SHA256WITHRSA",
 "Subject":{
 "Country":"US",
 "Organization":"Example Corp",
 "OrganizationalUnit":"Sales",
 "State":"WA",
 "Locality":"Seattle",
 "CommonName":"*.ec2.internal"
 }
}`
```

3. Save and close the file, exiting the text editor. For more information, see
   [Procedure for creating a CA](../../../privateca/latest/userguide/Create-CA-CLI.md "../../../privateca/latest/userguide/Create-CA-CLI.md")
   in the AWS Private Certificate Authority User Guide.
4. Use the [create-certificate-authority](../../../cli/latest/reference/acm-pca/create-certificate-authority.md "../../../cli/latest/reference/acm-pca/create-certificate-authority.md")
   AWS Private CA CLI command to create a private CA.

```
`~/home >` aws acm-pca create-certificate-authority \
     --certificate-authority-configuration file://ca_config.txt \
     --certificate-authority-type "ROOT" \
     --idempotency-token 01234567 --region `aws-region`
```

If successful, this command outputs the Amazon Resource Name (ARN) of the CA.

```
`{
 "CertificateAuthorityArn": "arn:aws:acm-pca:`aws-region`:111122223333:certificate-authority/`12345678-1234-1234-1234-123456789012`"
}`
```

###### To create and install a certificate for your private root CA (AWS CLI)

1. Generate a certificate signing request (CSR) using the
   [`get-certificate-authority-csr`](../../../cli/latest/reference/acm-pca/get-certificate-authority-csr.md "../../../cli/latest/reference/acm-pca/get-certificate-authority-csr.md")
   AWS CLI command.

```
`$` `aws acm-pca get-certificate-authority-csr \
 --certificate-authority-arn arn:aws:acm-pca:`aws-region`:111122223333:certificate-authority/12345678-1234-1234-1234-123456789012 \
 --output text \
 --endpoint https://acm-pca.`aws-region`.amazonaws.com \
 --region eu-west-1 > ca.csr`
```

The resulting file `ca.csr`, a PEM file encoded in base64 format, has the following appearance.

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

For more information, see
[Installing a root CA certificate](../../../privateca/latest/userguide/PCACertInstall.md#InstallRoot "../../../privateca/latest/userguide/PCACertInstall.md#InstallRoot")
in the AWS Private Certificate Authority User Guide. 2. Use the [`issue-certificate`](../../../cli/latest/reference/acm-pca/issue-certificate.md "../../../cli/latest/reference/acm-pca/issue-certificate.md")
AWS CLI command to issue and install the root certificate on your private CA.

```
`$` `aws acm-pca issue-certificate \
 --certificate-authority-arn arn:aws:acm-pca:`aws-region`:111122223333:certificate-authority/12345678-1234-1234-1234-123456789012 \
 --csr file://ca.csr \
 --signing-algorithm SHA256WITHRSA \
 --template-arn arn:aws:acm-pca:::template/RootCACertificate/V1 \
 --validity Value=3650,Type=DAYS --region `aws-region``
```

3. Download the root certificate using the
   [`get-certificate`](../../../cli/latest/reference/acm-pca/get-certificate.md "../../../cli/latest/reference/acm-pca/get-certificate.md")
   AWS CLI command.

```
`$` aws acm-pca get-certificate \
    --certificate-authority-arn arn:aws:acm-pca:`aws-region`:111122223333:certificate-authority/12345678-1234-1234-1234-123456789012 \
    --certificate-arn arn:aws:acm-pca:`aws-region`:486768734100:certificate-authority/12345678-1234-1234-1234-123456789012/certificate/abcdef0123456789abcdef0123456789 \
    --output text --region `aws-region` > rootCA.pem
```

4. Install the root certificate on your private CA using the
   [`import-certificate-authority-certificate`](../../../cli/latest/reference/acm-pca/import-certificate-authority-certificate.md "../../../cli/latest/reference/acm-pca/import-certificate-authority-certificate.md")
   AWS CLI command.

```
`$` `aws acm-pca import-certificate-authority-certificate \
 --certificate-authority-arn arn:aws:acm-pca:`aws-region`:111122223333:certificate-authority/12345678-1234-1234-1234-123456789012 \
 --certificate file://rootCA.pem --region `aws-region``
```

###### Generate and export the file system and client certificate

1. Use the
   [`request-certificate`](../../../cli/latest/reference/acm/request-certificate.md "../../../cli/latest/reference/acm/request-certificate.md") AWS CLI command
   to request an AWS Certificate Manager certificate to use on your file system and clients.

```
`$` `aws acm request-certificate \
 --domain-name *.ec2.internal \
 --idempotency-token 12345 \
 --region `aws-region` \
 --certificate-authority-arn arn:aws:acm-pca:`aws-region`:111122223333:certificate-authority/12345678-1234-1234-1234-123456789012`
```

If the request is successful, the ARN of the issued certificate is returned. 2. For security, you must assign a passphrase for the private key when exporting it. Create a passphrase and store it in a file named `passphrase.txt` 3. Use the [`export-certificate`](../../../cli/latest/reference/acm/export-certificate.md "../../../cli/latest/reference/acm/export-certificate.md")
AWS CLI command to export the private certificate issued previously. The exported file contains the certificate, the certificate
chain, and the encrypted private 2048-bit RSA key associated with the public key that is embedded in the certificate. For security, you
must assign a passphrase for the private key when exporting it. The following example is for a Linux EC2 instance.

```
`$` `aws acm export-certificate \
 --certificate-arn arn:aws:acm:`aws-region`:111122223333:certificate/12345678-1234-1234-1234-123456789012 \
 --passphrase $(cat passphrase.txt | base64) --region `aws-region` > exported_cert.json`
```

4. Use the following `jq` commands to extract the private key and the certificate from the JSON response.

```
`$` `passphrase=$(cat passphrase.txt | base64)
cat exported_cert.json | jq -r .PrivateKey > prv.key
cat exported_cert.json | jq -r .Certificate > cert.pem`
```

5. Use the following `openssl` command to decrypt the private key from the JSON response. After entering the
   command, you are prompted for the passphrase.

```
`$` `openssl rsa -in prv.key -passin pass:$passphrase -out decrypted.key`
```

## Installing and configuring Libreswan IPsec on an Amazon Linux 2 client

The following sections provide instructions for installing and configuring Libreswan IPsec on an Amazon EC2 instance running Amazon Linux 2.

###### To install and configure Libreswan

1. Connect to your EC2 instance using SSH. For specific instructions on how to do this, see
   [Connect to your Linux instance using an SSH client](../../../AWSEC2/latest/UserGuide/AccessingInstancesLinux.md#AccessingInstancesLinuxSSHClient "../../../AWSEC2/latest/UserGuide/AccessingInstancesLinux.md#AccessingInstancesLinuxSSHClient")
   in the Amazon Elastic Compute Cloud User Guide for Linux Instances.
2. Run the following command to install `libreswan`:

```
`$` `sudo yum install libreswan`
```

3. (Optional) When verifying IPsec in a later step, these properties might be flagged without these settings. We suggest
   testing your set up first without these settings. If your connection has problems, return to this step and make the following changes.

After the installation completes, use your preferred text editor to add the following entries to the `/etc/sysctl.conf`
file.

```
`net.ipv4.ip_forward=1
net.ipv4.conf.all.accept_redirects = 0
net.ipv4.conf.all.secure_redirects = 0
net.ipv4.conf.all.send_redirects = 0
net.ipv4.conf.default.accept_redirects = 0
net.ipv4.conf.default.send_redirects = 0
net.ipv4.conf.lo.accept_redirects = 0
net.ipv4.conf.lo.send_redirects = 0
net.ipv4.conf.all.rp_filter = 0
net.ipv4.conf.default.rp_filter = 0
net.ipv4.conf.eth0.rp_filter = 0`
```

Save the changes and exit the text editor. 4. Apply the changes.

```
`$` `sudo sysctl -p`
```

5. Verify the IPsec configuration.

```
`$` `sudo ipsec verify`
```

Verify that the version of `Libreswan` you installed is running. 6. Initialize the IPsec NSS database.

```
`$` `sudo ipsec checknss`
```

###### To install the certificate on the client

1. Copy the [certificate you generated](#generate-certificate "#generate-certificate") for the client to the working directory on the EC2 instance. You
2. Export the certificate generated previously into a format compatible with `libreswan`.

```
`$` `openssl pkcs12 -export -in cert.pem -inkey decrypted.key \
 -certfile rootCA.pem -out certkey.p12 -name fsx`
```

3. Import the reformatted key, providing the passphrase when prompted.

```
`$` `sudo ipsec import certkey.p12`
```

4. Create an IPsec configuration file using the preferred text editor.

```
`$` `sudo cat /etc/ipsec.d/nfs.conf`
```

Add the following entries to the config file:

```
`conn fsxn
 authby=rsasig
 left=172.31.77.6
 right=198.19.254.13
 auto=start
 type=transport
 ikev2=insist
 keyexchange=ike
 ike=aes256-sha2_384;dh20
 esp=aes_gcm_c256
 leftcert=fsx
 leftrsasigkey=%cert
 leftid=%fromcert
 rightid=%fromcert
 rightrsasigkey=%cert`
```

You will start IPsec on the client after configuring IPsec on your file system.

## Configuring IPsec on your file system

This section provides instructions on installing the certificate on your FSx for ONTAP file system, and configuring IPsec.

###### To install the certificate on your file system

1. Copy the root certificate (`rootCA.pem)`, the client certificate (`cert.pem`)
   and the decrypted key (`decrypted.key`) files to your file system.
   You will need to know the passphrase for the certificate.
2. To access the ONTAP CLI, establish an SSH session on the management port of the
   Amazon FSx for NetApp ONTAP file system or SVM by running the following command. Replace
   `management_endpoint_ip` with the IP address of the file system's
   management port.

```
`[~]$` `ssh fsxadmin@`management_endpoint_ip``
```

For more information, see [Managing file systems with the ONTAP CLI](managing-resources-ontap-apps.md#fsxadmin-ontap-cli "managing-resources-ontap-apps.md#fsxadmin-ontap-cli"). 3. Use **cat** on a client (not on your file system) to list out the contents of the `rootCA.pem`, `cert.pem` and
`decrypted.key` files so that you can copy the output of each file and paste it when prompted in the following steps.

```
`$ >` `cat cert.pem`
```

Copy the certificate contents. 4. You must install all CA certificates used during the mutual authentication, including both ONTAP-side and client-side CAs, to ONTAP
certificate management unless it is already installed (as is the case of an ONTAP self-signed root-CA).

Use the `security certificate install` NetApp CLI command as follows to install the client certificate:

```
`FSxID123:: >` `security certificate install -vserver `dr` -type client -cert-name ipsec-client-cert`
```

```
`Please enter Certificate: Press <Enter> when done`
```

Paste in the contents of the `cert.pem` file that you copied previously and press Enter.

```
`Please enter Private Key: Press <Enter> when done`
```

Paste in the contents of the `decrypted.key` file, and press enter.

```
`Do you want to continue entering root and/or intermediate certificates {y|n}:`
```

Enter `n` to complete entering the client certificate. 5. Create and install a certificate for use by the SVM. The issuer CA of this certificate must already be installed to ONTAP and
added to IPsec.

Use the following command to install the root certificate.

```
`FSxID123:: >` `security certificate install -vserver `dr` -type server-ca -cert-name ipsec-ca-cert`
```

```
`Please enter Certificate: Press <Enter> when done`
```

Paste in the contents of the `rootCA.pem` file, and press enter. 6. To ensure that the CA installed is within the IPsec CA searching path during authentication, add the ONTAP certificate management CAs to the
IPsec module using the “security ipsec ca-certificate add” command.

Enter the following command to add the root certificate.

```
`FSxID123:: >` `security ipsec ca-certificate add -vserver `dr` -ca-certs ipsec-ca-cert`
```

7. Enter the following command to create the required IPsec policy in the security policy database (SPD).

```
`security ipsec policy create -vserver `dr` -name `policy-name` -local-ip-subnets `198.19.254.13/32` -remote-ip-subnets `172.31.0.0/16` -auth-method PKI -action ESP_TRA -cipher-suite SUITEB_GCM256 -cert-name ipsec-client-cert -local-identity "CN=*.ec2.internal" -remote-identity "CN=*.ec2.internal"`
```

8. Use the following command to show the IPsec policy for the file system to confirm.

```
`FSxID123:: >` `security ipsec policy show -vserver `dr` -instance`
`Vserver: dr
 Policy Name: promise
 Local IP Subnets: 198.19.254.13/32
 Remote IP Subnets: 172.31.0.0/16
 Local Ports: 0-0
 Remote Ports: 0-0
 Protocols: any
 Action: ESP_TRA
 Cipher Suite: SUITEB_GCM256
 IKE Security Association Lifetime: 86400
 IPsec Security Association Lifetime: 28800
IPsec Security Association Lifetime (bytes): 0
 Is Policy Enabled: true
 Local Identity: CN=*.ec2.internal
 Remote Identity: CN=*.ec2.internal
 Authentication Method: PKI
 Certificate for Local Identity: ipsec-client-cert`
```

## Start IPsec on the client

Now IPsec is configured on both the FSx for ONTAP file system and the client, you can start IPsec on the client.

1. Connect to your client system using SSH.
2. Start IPsec.

```
`$` `sudo ipsec start`
```

3. Check the status of IPsec.

```
`$` `sudo ipsec status`
```

4. Mount a volume on your file system.

```
`$` `sudo mount -t nfs `198.19.254.13:/benchmark` `/home/ec2-user/acm/dr``
```

5. Verify the IPsec setup by showing the encrypted connection on your FSx for ONTAP file system.

```
`FSxID123:: >` `security ipsec show-ikesa -node FsxId`123``
`FsxId08ac16c7ec2781a58::> security ipsec show-ikesa -node FsxId08ac16c7ec2781a58-01
 Policy Local Remote
Vserver Name Address Address Initator-SPI State
----------- ------ --------------- --------------- ---------------- -----------
dr `policy-name`
 198.19.254.13 172.31.77.6 551c55de57fe8976 ESTABLISHED
fsx `policy-name`
 198.19.254.38 172.31.65.193 4fd3f22c993e60c5 ESTABLISHED
2 entries were displayed.`
```

## Setting up IPsec for multiple clients

When a small number of clients need to leverage IPsec, using a single SPD entry for each client is
sufficient. However, when hundreds or even thousands of clients need to leverage IPsec, we recommend that you
use IPsec multiple client configuration.

FSx for ONTAP supports connecting multiple clients across many networks to a single SVM IP address with IPsec enabled.
You can accomplish this using either the `subnet` configuration or the `Allow all clients` configuration, which are
explained in the following procedures:

###### To configure IPsec for multiple clients using a subnet configuration

To allow all clients on a particular subnet (192.168.134.0/24
for example) to connect to a single SVM IP address using a single SPD policy entry, you must specify the `remote-ip-subnets`
in subnet form. Additionally, you must specify the `remote-identity` field with the correct client side identity.

###### Important

When using certificate authentication, each client can use
either their own unique certificate or a shared certificate to authenticate. FSx for ONTAP IPsec checks the validity of the certificate
based on the CAs installed on its local trust store. FSx for ONTAP also supports certificate revocation list (CRL) checking.

1. To access the ONTAP CLI, establish an SSH session on the management port of the
   Amazon FSx for NetApp ONTAP file system or SVM by running the following command. Replace
   `management_endpoint_ip` with the IP address of the file system's
   management port.

```
`[~]$` `ssh fsxadmin@`management_endpoint_ip``
```

For more information, see [Managing file systems with the ONTAP CLI](managing-resources-ontap-apps.md#fsxadmin-ontap-cli "managing-resources-ontap-apps.md#fsxadmin-ontap-cli"). 2. Use the `security ipsec policy create` NetApp ONTAP CLI command as follows, replacing the `sample` values
with your specific values.

```
`FsxId123456::>` `security ipsec policy create -vserver `svm_name` -name `policy_name` \
 -local-ip-subnets `192.168.134.34/32` -remote-ip-subnets `192.168.134.0/24` \
 -local-ports `2049` -protocols `tcp` -auth-method PSK \
 -cert-name `my_nfs_server_cert` -local-identity `ontap_side_identity` \
 -remote-identity `client_side_identity``
```

###### To configure IPsec for multiple clients using an allow all clients configuration

To allow any client, regardless of their source IP address, to connect to the SVM IPsec-enabled IP address, use
the `0.0.0.0/0` wild card when specifying the `remote-ip-subnets` field.

Additionally, you must specify the `remote-identity` field with the correct client side identity. For certificate authentication,
you can enter `ANYTHING`.

Also, when the 0.0.0.0/0 wild card is used, you must configure a specific local or remote port number to use.
For example, NFS port 2049.

1. To access the ONTAP CLI, establish an SSH session on the management port of the
   Amazon FSx for NetApp ONTAP file system or SVM by running the following command. Replace
   `management_endpoint_ip` with the IP address of the file system's
   management port.

```
`[~]$` `ssh fsxadmin@`management_endpoint_ip``
```

For more information, see [Managing file systems with the ONTAP CLI](managing-resources-ontap-apps.md#fsxadmin-ontap-cli "managing-resources-ontap-apps.md#fsxadmin-ontap-cli"). 2. Use the `security ipsec policy create` NetApp ONTAP CLI command as follows, replacing the `sample` values
with your specific values.

```
`FsxId123456::>` `security ipsec policy create -vserver `svm_name` -name `policy_name` \
 -local-ip-subnets `192.168.134.34/32` -remote-ip-subnets 0.0.0.0/0 \
 -local-ports `2049` -protocols `tcp` -auth-method PSK \
 -cert-name `my_nfs_server_cert` -local-identity `ontap_side_identity` \
 -local-ports `2049` -remote-identity `client_side_identity``
```
