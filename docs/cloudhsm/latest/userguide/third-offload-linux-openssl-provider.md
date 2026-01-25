# AWS CloudHSM SSL/TLS offload on Linux using NGINX or HAProxy with OpenSSL Provider

This topic provides step-by-step instructions for setting up SSL/TLS server identity offload with AWS CloudHSM on a Linux web server using NGINX or HAProxy with the OpenSSL Provider.

###### Topics

- [Overview](#ssl-offload-linux-openssl-provider-overview "#ssl-offload-linux-openssl-provider-overview")
- [Step 1: Set up the prerequisites](#ssl-offload-provider-prerequisites "#ssl-offload-provider-prerequisites")
- [Step 2: Generate or import a private key and get a certificate](#ssl-offload-provider-generate-key-and-certificate "#ssl-offload-provider-generate-key-and-certificate")
- [Step 3: Configure the web server](#ssl-offload-provider-configure-web-server "#ssl-offload-provider-configure-web-server")
- [Step 4: Enable HTTPS traffic
  and verify the certificate](#ssl-offload-enable-traffic-and-verify-certificate-provider "#ssl-offload-enable-traffic-and-verify-certificate-provider")

## Overview

On Linux, the [NGINX](https://nginx.org/en/ "https://nginx.org/en/") and [HAProxy](https://www.haproxy.org/ "https://www.haproxy.org/") web server software integrate with [OpenSSL](https://www.openssl.org/ "https://www.openssl.org/") to support HTTPS. The [AWS CloudHSM OpenSSL Provider](openssl-provider-library.md "openssl-provider-library.md") provides an interface that enables the web server software to use the HSMs in your cluster for cryptographic offloading and key storage. The OpenSSL Provider is the bridge that connects the web server to your AWS CloudHSM cluster.

To complete this tutorial, you will configure NGINX or HAProxy to use the AWS CloudHSM OpenSSL Provider. The tutorial shows you how to do the following:

- Install the web server software on an Amazon EC2 instance.
- Configure the web server software to support HTTPS with a private key stored in your
  AWS CloudHSM cluster.
- (Optional) Use Amazon EC2 to create a second web server instance and Elastic Load Balancing to create a load
  balancer. Using a load balancer can increase performance by distributing the load across
  multiple servers. It can also provide redundancy and higher availability if one or more
  servers fail.

When you're ready to get started, go to [Step 1: Set up the prerequisites](#ssl-offload-provider-prerequisites "#ssl-offload-provider-prerequisites").

## Step 1: Set up the prerequisites

Different platforms require different prerequisites. Use the prerequisites section below that matches your platform.

### Prerequisites for AWS CloudHSM OpenSSL Provider

To set up web server SSL/TLS server identity offload with AWS CloudHSM OpenSSL Provider for Client SDK 5, you need the following:

- An active AWS CloudHSM cluster with at least two hardware security modules (HSM)

###### Note

You can use a single HSM cluster, but you must first disable client key
durability. For more information, see [Manage Client
Key Durability Settings](working-client-sync.md#client-sync-sdk8 "working-client-sync.md#client-sync-sdk8") and [Client SDK 5
Configure Tool](configure-sdk-5.md "configure-sdk-5.md").

- An Amazon EC2 instance running a Linux operating system with the following software
  installed:
  - A web server (either NGINX or HAProxy)
  - The AWS CloudHSM OpenSSL Provider for Client SDK 5

- A [crypto user](understanding-users.md#crypto-user-chsm-cli "understanding-users.md#crypto-user-chsm-cli") (CU) to own and manage the web server's
  private key on the HSM.

###### To set up a Linux web server instance and create a CU on the HSM

###### Note

Many of the commands in this procedure require elevated privileges. You may need to run commands with `sudo` or as the root user depending on your system configuration.

1. Install and configure the AWS CloudHSM OpenSSL Provider for Client SDK 5. For more information about
   installing the OpenSSL Provider, see [AWS CloudHSM OpenSSL Provider for Client SDK 5](openssl-provider-install.md "openssl-provider-install.md").
2. On an EC2 Linux instance that has access to your cluster, install either NGINX or HAProxy web
   server:

Amazon Linux 2023

    * NGINX



    ```
    `$` `yum install nginx`
    ```
    * HAProxy



    ```
    `$` `yum install haproxy`
    ```

RHEL 9 (9.2+)

    * NGINX



    ```
    `$` `yum install nginx`
    ```
    * HAProxy



    ```
    `$` `yum install haproxy`
    ```

RHEL 10 (10.0+)

    * NGINX



    ```
    `$` `yum install nginx`
    ```
    * HAProxy



    ```
    `$` `yum install haproxy`
    ```

Ubuntu 24.04

    * NGINX



    ```
    `$` `apt install nginx`
    ```
    * HAProxy



    ```
    `$` `apt install haproxy`
    ```

3. Use CloudHSM CLI to create a [crypto user](understanding-users.md#crypto-user-chsm-cli "understanding-users.md#crypto-user-chsm-cli"). For more information about
   managing HSM users, see [Managing HSM users with CloudHSM CLI](manage-hsm-users-chsm-cli.md "manage-hsm-users-chsm-cli.md").

###### Tip

Keep track of the CU user name and password. You will need them later when you
generate or import the HTTPS private key and certificate for your web server.

After you complete these steps, go to [Step 2: Generate or import a private key and get a certificate](#ssl-offload-provider-generate-key-and-certificate "#ssl-offload-provider-generate-key-and-certificate").

#### Notes

- To use Security-Enhanced Linux (SELinux) and web servers, you must allow
  outbound TCP connections on port 2223, which is the port Client SDK 5 uses to
  communicate with the HSM.
- To create and activate a cluster and give an EC2 instance access to the cluster,
  complete the steps in [Getting Started with
  AWS CloudHSM](getting-started.md "getting-started.md"). The getting started offers step-by-step instruction for creating an
  active cluster with one HSM and an Amazon EC2 client instance. You can use this client instance as your web server.
- To avoid disabling client key durability, add more than one HSM to your cluster.
  For more information, see [Adding an HSM to an AWS CloudHSM cluster](add-hsm.md "add-hsm.md").
- To connect to your client instance, you can use SSH or PuTTY. For more
  information, see [Connecting
  to Your Linux Instance Using SSH](../../../AWSEC2/latest/UserGuide/AccessingInstancesLinux.md "../../../AWSEC2/latest/UserGuide/AccessingInstancesLinux.md") or [Connecting to Your Linux Instance from Windows Using PuTTY](../../../AWSEC2/latest/UserGuide/putty.md "../../../AWSEC2/latest/UserGuide/putty.md") in the Amazon EC2
  documentation.

## Step 2: Generate or import a private key and get a certificate

To enable HTTPS, your web server application (NGINX or HAProxy) needs a private key and a
corresponding SSL/TLS certificate. To use web server SSL/TLS server identity offload with AWS CloudHSM, you must store
the private key in an HSM in your AWS CloudHSM cluster. You will first generate a private key and use
the key to create a certificate signing request (CSR). You then export a _fake PEM
private key_ from the HSM, which is a private key file in PEM format which contains a reference to
the private key stored on the HSM (it's not the actual private key). Your web server uses the fake PEM private key file
to identify the private key on the HSM during SSL/TLS server identity offload.

### Generate a private key

This section shows you how to generate a keypair using the [CloudHSM CLI](cloudhsm_cli.md "cloudhsm_cli.md"). Once you
have a key pair generated inside the HSM, you can export it as a fake PEM file and generate the corresponding certificate.

###### Install and configure the CloudHSM CLI

1. [Install and Configure](cloudhsm_cli-getting-started.md "cloudhsm_cli-getting-started.md") the CloudHSM CLI.
2. Use the following command to start the CloudHSM CLI.

```
`$` `/opt/cloudhsm/bin/cloudhsm-cli interactive`
```

3. Run the following command to log in to the HSM. Replace `<user name>`
   with the user name of your crypto-user

```
`aws-cloudhsm>``login --username `<user name>` --role crypto-user`
```

**Generate a Private Key**

Depending on your use case, you can either generate an RSA or an EC key pair. Do one of the following:

- To generate an RSA private key on an HSM

Use the [key generate-asymmetric-pair rsa](cloudhsm_cli-key-generate-asymmetric-pair-rsa.md "cloudhsm_cli-key-generate-asymmetric-pair-rsa.md") command to generate an RSA key pair. This example generates an RSA key pair with a modulus of 2048,
a public exponent of 65537, public key label of `tls_rsa_pub`, and private key label of `tls_rsa_private`.

```
`aws-cloudhsm >` `key generate-asymmetric-pair rsa \
--public-exponent 65537 \
--modulus-size-bits 2048 \
--public-label tls_rsa_pub \
--private-label tls_rsa_private \
--private-attributes sign=true``{
 "error_code": 0,
 "data": {
 "public_key": {
 "key-reference": "0x0000000000280cc8",
 "key-info": {
 "key-owners": [
 {
 "username": "cu1",
 "key-coverage": "full"
 }
 ],
 "shared-users": [],
 "cluster-coverage": "full"
 },
 "attributes": {
 "key-type": "rsa",
 "label": "tls_rsa_pub",
 "id": "",
 "check-value": "0x01fe6e",
 "class": "public-key",
 "encrypt": true,
 "decrypt": false,
 "token": true,
 "always-sensitive": false,
 "derive": false,
 "destroyable": true,
 "extractable": true,
 "local": true,
 "modifiable": true,
 "never-extractable": false,
 "private": true,
 "sensitive": false,
 "sign": false,
 "trusted": false,
 "unwrap": false,
 "verify": false,
 "wrap": false,
 "wrap-with-trusted": false,
 "key-length-bytes": 512,
 "public-exponent": "0x010001",
 "modulus": "0xb1d27e857a876f4e9fd5de748a763c539b359f937eb4b4260e30d1435485a732c878cdad9c72538e2215351b1d41358c9bf80b599c73a80fdb457aa7b20cd61e486c326e2cfd5e124a7f6a996437437812b542e3caf85928aa866f0298580f7967ee6aa01440297d7308fdd9b76b70d1b67f12634df6e6296d6c116d5744c6d60d14d3bf3cb978fe6b75ac67b7089bafd50d8687213b31abc7dc1bad422780d29c851d5102b56f932551eaf52a9591fd8c43d81ecc133022653225bd129f8491101725e9ea33e1ded83fb57af35f847e532eb30cd7e726f23910d2671c6364092e834697ec3cef72cc23615a1ba7c5e100156ae0acac3160f0ca9725d38318b7",
 "modulus-size-bits": 2048
 }
 },
 "private_key": {
 "key-reference": "0x0000000000280cc7",
 "key-info": {
 "key-owners": [
 {
 "username": "cu1",
 "key-coverage": "full"
 }
 ],
 "shared-users": [],
 "cluster-coverage": "full"
 },
 "attributes": {
 "key-type": "rsa",
 "label": "tls_rsa_private",
 "id": "",
 "check-value": "0x01fe6e",
 "class": "private-key",
 "encrypt": false,
 "decrypt": true,
 "token": true,
 "always-sensitive": true,
 "derive": false,
 "destroyable": true,
 "extractable": true,
 "local": true,
 "modifiable": true,
 "never-extractable": false,
 "private": true,
 "sensitive": true,
 "sign": true,
 "trusted": false,
 "unwrap": false,
 "verify": false,
 "wrap": false,
 "wrap-with-trusted": false,
 "key-length-bytes": 1217,
 "public-exponent": "0x010001",
 "modulus": "0xb1d27e857a876f4e9fd5de748a763c539b359f937eb4b4260e30d1435485a732c878cdad9c72538e2215351b1d41358c9bf80b599c73a80fdb457aa7b20cd61e486c326e2cfd5e124a7f6a996437437812b542e3caf85928aa866f0298580f7967ee6aa01440297d7308fdd9b76b70d1b67f12634df6e6296d6c116d5744c6d60d14d3bf3cb978fe6b75ac67b7089bafd50d8687213b31abc7dc1bad422780d29c851d5102b56f932551eaf52a9591fd8c43d81ecc133022653225bd129f8491101725e9ea33e1ded83fb57af35f847e532eb30cd7e726f23910d2671c6364092e834697ec3cef72cc23615a1ba7c5e100156ae0acac3160f0ca9725d38318b7",
 "modulus-size-bits": 2048
 }
 }
 }
}`
```

- To generate an EC private key on an HSM

Use the [key generate-asymmetric-pair ec](cloudhsm_cli-key-generate-asymmetric-pair-ec.md "cloudhsm_cli-key-generate-asymmetric-pair-ec.md") command to generate an EC key pair. This example generates an EC key pair
with the `prime256v1` curve (corresponding to the `NID_X9_62_prime256v1` curve), a public key label of `tls_ec_pub`,
and a private key label of `tls_ec_private`.

```
`aws-cloudhsm >` `key generate-asymmetric-pair ec \
 --curve prime256v1 \
 --public-label tls_ec_pub \
 --private-label tls_ec_private \
 --private-attributes sign=true``{
 "error_code": 0,
 "data": {
 "public_key": {
 "key-reference": "0x000000000012000b",
 "key-info": {
 "key-owners": [
 {
 "username": "cu1",
 "key-coverage": "full"
 }
 ],
 "shared-users": [],
 "cluster-coverage": "session"
 },
 "attributes": {
 "key-type": "ec",
 "label": "tls_ec_pub",
 "id": "",
 "check-value": "0xd7c1a7",
 "class": "public-key",
 "encrypt": false,
 "decrypt": false,
 "token": false,
 "always-sensitive": false,
 "derive": false,
 "destroyable": true,
 "extractable": true,
 "local": true,
 "modifiable": true,
 "never-extractable": false,
 "private": true,
 "sensitive": false,
 "sign": false,
 "trusted": false,
 "unwrap": false,
 "verify": false,
 "wrap": false,
 "wrap-with-trusted": false,
 "key-length-bytes": 57,
 "ec-point": "0x047096513df542250a6b228fd9cb67fd0c903abc93488467681974d6f371083fce1d79da8ad1e9ede745fb9f38ac8622a1b3ebe9270556000c",
 "curve": "secp224r1"
 }
 },
"private_key": {
 "key-reference": "0x000000000012000c",
 "key-info": {
 "key-owners": [
 {
 "username": "cu1",
 "key-coverage": "full"
 }
 ],
 "shared-users": [],
 "cluster-coverage": "session"
 },
 "attributes": {
 "key-type": "ec",
 "label": "tls_ec_private",
 "id": "",
 "check-value": "0xd7c1a7",
 "class": "private-key",
 "encrypt": false,
 "decrypt": false,
 "token": false,
 "always-sensitive": true,
 "derive": false,
 "destroyable": true,
 "extractable": true,
 "local": true,
 "modifiable": true,
 "never-extractable": false,
 "private": true,
 "sensitive": true,
 "sign": true,
 "trusted": false,
 "unwrap": false,
 "verify": false,
 "wrap": false,
 "wrap-with-trusted": false,
 "key-length-bytes": 122,
 "ec-point": "0x047096513df542250a6b228fd9cb67fd0c903abc93488467681974d6f371083fce1d79da8ad1e9ede745fb9f38ac8622a1b3ebe9270556000c",
 "curve": "secp224r1"
 }
 }
 }
}`
```

**Export a fake PEM private key file**

Once you have a private key on the HSM, you must export a fake PEM private key file. This file does not contain the actual key data, but it allows
the OpenSSL Dynamic Engine to identify the private key on the HSM. You can then you use the private key to create a
certificate signing request (CSR) and sign the CSR to create the certificate.

Use the [key generate-file](cloudhsm_cli-key-generate-file.md "cloudhsm_cli-key-generate-file.md") command to export the private key in fake PEM format and save it to a file.
Replace the following values with your own.

- `<private_key_label>` – Label of the private key you generated in the previous step.
- `<web_server_fake_pem.key>` – Name of the file that your fake PEM key will be written to.

````
`aws-cloudhsm >` `key generate-file --encoding reference-pem --path `<web_server_fake_pem.key>` --filter attr.label=`<private_key_label>```{
 "error_code": 0,
 "data": {
 "message": "Successfully generated key file"
 }
}`
````

**Exit the CloudHSM CLI**

Run the following command to stop the CloudHSM CLI.

```
`aws-cloudhsm >` `quit`
```

You should now have a new file on your system, located at the path specified by `<web_server_fake_pem.key>` in the preceding command.
This file is the fake PEM private key file.

### Generate a self-signed certificate

Once you have generated a fake PEM private key, you can use this file to generate a certificate signing request (CSR) and certificate.

In a production environment, you typically use a certificate authority (CA) to create a certificate from a CSR.
A CA is not necessary for a test environment. If you do use a CA, send the CSR file
to them and use signed SSL/TLS certificate that they provide you in your web server for HTTPS.

As an alternative to using a CA, you can use the AWS CloudHSM OpenSSL Dynamic Engine to
create a self-signed certificate. Self-signed certificates are not trusted by browsers and
should not be used in production environments. They can be used in test environments.

###### Warning

Self-signed certificates should be used in a test environment only. For a production
environment, use a more secure method such as a certificate authority to create a
certificate.

###### Install and configure the OpenSSL Dynamic Engine

1. Connect to your client instance.
2. [Install the OpenSSL Dynamic Engine for AWS CloudHSM
   Client SDK 5](openssl5-install.md "openssl5-install.md")

###### Generate a certificate

1. Obtain a copy of your fake PEM file generated in an earlier step.
2. Create a CSR

Run the following command to use the AWS CloudHSM OpenSSL Dynamic Engine to create a
certificate signing request (CSR). Replace
`<web_server_fake_pem.key>` with the name of the file that
contains your fake PEM private key. Replace `<web_server.csr>`
with the name of the file that contains your CSR.

The `req` command is interactive. Respond to each field. The field information is copied into your
SSL/TLS certificate.

###### Note

CSR creation is not currently supported with the OpenSSL Provider. You must use the OpenSSL Engine for this step, but TLS cipher operations will work with the Provider.

```
`$` `openssl req -engine cloudhsm -new -key `<web_server_fake_pem.key>` -out `<web_server.csr>``
```

3. Create a self-signed certificate

Run the following command to use the AWS CloudHSM OpenSSL Dynamic Engine to sign your CSR with
your private key on your HSM. This creates a self-signed certificate. Replace the following
values in the command with your own.

    * `<web_server.csr>` – Name of the file that contains the CSR.
    * `<web_server_fake_pem.key>` – Name of the file that contains the
     fake PEM private key.
    * `<web_server.crt>` – Name of the file that will
     contain your web server certificate.

```
`$` `openssl x509 -engine cloudhsm -req -days 365 -in `<web_server.csr>` -signkey `<web_server_fake_pem.key>` -out `<web_server.crt>``
```

After you have a private key and certificate, go to [Step 3: Configure the web server](#ssl-offload-provider-configure-web-server "#ssl-offload-provider-configure-web-server").

## Step 3: Configure the web server

Update your web server software's configuration to use the HTTPS certificate and
corresponding fake PEM private key that you created in the [previous step](#ssl-offload-provider-generate-key-and-certificate "#ssl-offload-provider-generate-key-and-certificate").
Remember to backup your existing certificates and keys before you start. This
will finish setting up your Linux web server software for SSL/TLS server identity offload with AWS CloudHSM.

Complete the steps from one of the following sections.

###### Topics

- [Configure NGINX web server](#ssl-offload-provider-configure-nginx "#ssl-offload-provider-configure-nginx")
- [Configure HAProxy web server](#ssl-offload-provider-configure-haproxy "#ssl-offload-provider-configure-haproxy")

### Configure NGINX web server

Use this section to configure NGINX with the OpenSSL Provider.

###### To configure NGINX for OpenSSL Provider

1. Connect to your client instance.
2. Run the following command to create the required directories for the web server
   certificate and the fake PEM private key.

```
`$` `mkdir -p /etc/pki/nginx/private`
```

3. Run the following command to copy your web server certificate to the required
   location. Replace `<web_server.crt>` with the name of your
   web server certificate.

```
`$` `cp `<web_server.crt>` /etc/pki/nginx/server.crt`
```

4. Run the following command to copy your fake PEM private key to the required location.
   Replace `<web_server_fake_pem.key>` with the name of the
   file that contains your fake PEM private key.

```
`$` `cp `<web_server_fake_pem.key>` /etc/pki/nginx/private/server.key`
```

5. Run the following command to change the file ownership so that the user named
   _nginx_ can read them.

```
`$` `chown nginx /etc/pki/nginx/server.crt /etc/pki/nginx/private/server.key`
```

6. Configure OpenSSL to use the AWS CloudHSM provider. For more information about configuring the OpenSSL Provider, see [AWS CloudHSM OpenSSL Provider for Client SDK 5](openssl-provider-install.md "openssl-provider-install.md").
   1. Locate your OpenSSL configuration file:

   ```
   `$` `openssl version -d`
   ```

   You should see output similar to:

   ```
   OPENSSLDIR: "/etc/pki/tls"
   ```

   The configuration file is `openssl.cnf` in this directory. 2. ###### Note

   Do not modify your system's default openssl.cnf file directly. This prevents system-wide OpenSSL operations (SSH, TLS connections, and other services) from unintentionally routing through the CloudHSM provider.

   Using a separate configuration file allows you to scope CloudHSM Provider usage to only specific applications that require HSM-backed cryptographic operations.

   Create a new OpenSSL configuration file with the following contents:

   ```
   `$` `cat > `<example-cloudhsm-openssl.cnf>` << 'EOF'`
   ## NOTE: This should point to the system default openssl config file.
   # Replace /etc/pki/tls with the path to your OpenSSL configuration directory
   .include `</etc/pki/tls>`/openssl.cnf

   # Override the existing provider_section to include AWS CloudHSM OpenSSL Provider as a 3rd party OpenSSL provider
   [provider_sect]
   default = default_sect
   # Include AWS CloudHSM CloudHSM OpenSSL provider
   cloudhsm = cloudhsm_sect

   [default_sect]
   activate = 1

   [cloudhsm_sect]
   activate = 1
   `EOF`
   ```

   3. Ensure that the `CLOUDHSM_PIN` environment variable is set with your crypto user (CU) credentials:

   ```
   `$` `export CLOUDHSM_PIN=`<username>`:`<password>``
   ```

   4. Set the `OPENSSL_CONF` environment variable to point to your updated configuration file and verify the provider is loaded:

   ```
   `$` `OPENSSL_CONF=/path/to/example-cloudhsm-openssl.cnf openssl list -providers`
   ```

   You should see both the default provider and the CloudHSM provider listed:

   ```
   OPENSSL_CONF=/path/to/example-cloudhsm-openssl.cnf openssl list -providers
   Providers:
     default
       name: OpenSSL Default Provider
       version: 3.2.2
       status: active
     cloudhsm
       name: AWS CloudHSM OpenSSL Provider
       version: 5.17.0
       status: active
   ```

7. Run the following command to back up the `/etc/nginx/nginx.conf`
   file.

```
`$` `cp /etc/nginx/nginx.conf /etc/nginx/nginx.conf.backup`
```

8. Update the NGINX configuration.

###### Note

Each cluster can support a maximum of 1000 NGINX worker processes across
all NGINX web servers.

Amazon Linux 2023
Use a text editor to edit the `/etc/nginx/nginx.conf` file. This may require Linux root permissions. At the
top of the file, add the following lines:

```
env CLOUDHSM_PIN;
env OPENSSL_CONF;
```

Then add the following to the TLS section of the file:

```
# Settings for a TLS enabled server.
server {
    listen       443 ssl http2 default_server;
    listen       [::]:443 ssl http2 default_server;
    server_name  _;
    root         /usr/share/nginx/html;

    ssl_certificate "/etc/pki/nginx/server.crt";
    ssl_certificate_key "/etc/pki/nginx/private/server.key";
    # It is *strongly* recommended to generate unique DH parameters for DHE ciphers
    # Generate them with: openssl dhparam -out /etc/pki/nginx/dhparams.pem 2048
    # ssl_dhparam "/etc/pki/nginx/dhparams.pem";
    ssl_session_cache shared:SSL:1m;
    ssl_session_timeout  10m;
    ssl_protocols TLSv1.2 TLSv1.3;
    ssl_ciphers "ECDHE-RSA-AES128-GCM-SHA256:ECDHE-RSA-AES256-GCM-SHA384:DHE-RSA-AES128-GCM-SHA256:DHE-RSA-AES256-GCM-SHA384:ECDHE-RSA-AES256-SHA384:ECDHE-RSA-AES128-SHA256:DHE-RSA-AES128-SHA256:DHE-RSA-AES256-SHA256:ECDHE-RSA-CHACHA20-POLY1305:DHE-RSA-CHACHA20-POLY1305:ECDHE-ECDSA-AES256-GCM-SHA384:ECDHE-ECDSA-AES256-SHA384:ECDHE-ECDSA-AES128-GCM-SHA256:ECDHE-ECDSA-AES128-SHA256:ECDHE-ECDSA-CHACHA20-POLY1305:TLS_AES_128_GCM_SHA256:TLS_AES_256_GCM_SHA384:TLS_CHACHA20_POLY1305_SHA256";
    ssl_prefer_server_ciphers off;

    # Load configuration files for the default server block.
    include /etc/nginx/default.d/*.conf;

    location / {
    }

    error_page 404 /404.html;
    location = /40x.html {
    }

    error_page 500 502 503 504 /50x.html;
    location = /50x.html {
    }
}

```

RHEL 9 (9.2+)
Use a text editor to edit the `/etc/nginx/nginx.conf` file. This may require Linux root permissions. At the
top of the file, add the following lines:

```
env CLOUDHSM_PIN;
env OPENSSL_CONF;
```

Then add the following to the TLS section of the file:

```
# Settings for a TLS enabled server.
server {
    listen       443 ssl http2 default_server;
    listen       [::]:443 ssl http2 default_server;
    server_name  _;
    root         /usr/share/nginx/html;

    ssl_certificate "/etc/pki/nginx/server.crt";
    ssl_certificate_key "/etc/pki/nginx/private/server.key";
    # It is *strongly* recommended to generate unique DH parameters for DHE ciphers
    # Generate them with: openssl dhparam -out /etc/pki/nginx/dhparams.pem 2048
    # ssl_dhparam "/etc/pki/nginx/dhparams.pem";
    ssl_session_cache shared:SSL:1m;
    ssl_session_timeout  10m;
    ssl_protocols TLSv1.2 TLSv1.3;
    ssl_ciphers "ECDHE-RSA-AES128-GCM-SHA256:ECDHE-RSA-AES256-GCM-SHA384:DHE-RSA-AES128-GCM-SHA256:DHE-RSA-AES256-GCM-SHA384:ECDHE-RSA-AES256-SHA384:ECDHE-RSA-AES128-SHA256:DHE-RSA-AES128-SHA256:DHE-RSA-AES256-SHA256:ECDHE-RSA-CHACHA20-POLY1305:DHE-RSA-CHACHA20-POLY1305:ECDHE-ECDSA-AES256-GCM-SHA384:ECDHE-ECDSA-AES256-SHA384:ECDHE-ECDSA-AES128-GCM-SHA256:ECDHE-ECDSA-AES128-SHA256:ECDHE-ECDSA-CHACHA20-POLY1305:TLS_AES_128_GCM_SHA256:TLS_AES_256_GCM_SHA384:TLS_CHACHA20_POLY1305_SHA256";
    ssl_prefer_server_ciphers off;

    # Load configuration files for the default server block.
    include /etc/nginx/default.d/*.conf;

    location / {
    }

    error_page 404 /404.html;
    location = /40x.html {
    }

    error_page 500 502 503 504 /50x.html;
    location = /50x.html {
    }
}

```

RHEL 10 (10.0+)
Use a text editor to edit the `/etc/nginx/nginx.conf` file. This may require Linux root permissions. At the
top of the file, add the following lines:

```
env CLOUDHSM_PIN;
env OPENSSL_CONF;
```

Then add the following to the TLS section of the file:

```
# Settings for a TLS enabled server.
server {
    listen       443 ssl http2 default_server;
    listen       [::]:443 ssl http2 default_server;
    server_name  _;
    root         /usr/share/nginx/html;

    ssl_certificate "/etc/pki/nginx/server.crt";
    ssl_certificate_key "/etc/pki/nginx/private/server.key";
    # It is *strongly* recommended to generate unique DH parameters for DHE ciphers
    # Generate them with: openssl dhparam -out /etc/pki/nginx/dhparams.pem 2048
    # ssl_dhparam "/etc/pki/nginx/dhparams.pem";
    ssl_session_cache shared:SSL:1m;
    ssl_session_timeout  10m;
    ssl_protocols TLSv1.2 TLSv1.3;
    ssl_ciphers "ECDHE-RSA-AES128-GCM-SHA256:ECDHE-RSA-AES256-GCM-SHA384:DHE-RSA-AES128-GCM-SHA256:DHE-RSA-AES256-GCM-SHA384:ECDHE-RSA-AES256-SHA384:ECDHE-RSA-AES128-SHA256:DHE-RSA-AES128-SHA256:DHE-RSA-AES256-SHA256:ECDHE-RSA-CHACHA20-POLY1305:DHE-RSA-CHACHA20-POLY1305:ECDHE-ECDSA-AES256-GCM-SHA384:ECDHE-ECDSA-AES256-SHA384:ECDHE-ECDSA-AES128-GCM-SHA256:ECDHE-ECDSA-AES128-SHA256:ECDHE-ECDSA-CHACHA20-POLY1305:TLS_AES_128_GCM_SHA256:TLS_AES_256_GCM_SHA384:TLS_CHACHA20_POLY1305_SHA256";
    ssl_prefer_server_ciphers off;

    # Load configuration files for the default server block.
    include /etc/nginx/default.d/*.conf;

    location / {
    }

    error_page 404 /404.html;
    location = /40x.html {
    }

    error_page 500 502 503 504 /50x.html;
    location = /50x.html {
    }
}

```

Ubuntu 24.04
Use a text editor to edit the `/etc/nginx/nginx.conf` file. This may require Linux root permissions. At the
top of the file, add the following lines:

```
env CLOUDHSM_PIN;
env OPENSSL_CONF;
```

Then add the following to the TLS section of the file:

```
# Settings for a TLS enabled server.
server {
    listen       443 ssl http2 default_server;
    listen       [::]:443 ssl http2 default_server;
    server_name  _;
    root         /var/www/html;

    ssl_certificate "/etc/ssl/certs/server.crt";
    ssl_certificate_key "/etc/ssl/private/server.key";
    # It is *strongly* recommended to generate unique DH parameters for DHE ciphers
    # Generate them with: openssl dhparam -out /etc/ssl/certs/dhparams.pem 2048
    # ssl_dhparam "/etc/ssl/certs/dhparams.pem";
    ssl_session_cache shared:SSL:1m;
    ssl_session_timeout  10m;
    ssl_protocols TLSv1.2 TLSv1.3;
    ssl_ciphers "ECDHE-RSA-AES128-GCM-SHA256:ECDHE-RSA-AES256-GCM-SHA384:DHE-RSA-AES128-GCM-SHA256:DHE-RSA-AES256-GCM-SHA384:ECDHE-RSA-AES256-SHA384:ECDHE-RSA-AES128-SHA256:DHE-RSA-AES128-SHA256:DHE-RSA-AES256-SHA256:ECDHE-RSA-CHACHA20-POLY1305:DHE-RSA-CHACHA20-POLY1305:ECDHE-ECDSA-AES256-GCM-SHA384:ECDHE-ECDSA-AES256-SHA384:ECDHE-ECDSA-AES128-GCM-SHA256:ECDHE-ECDSA-AES128-SHA256:ECDHE-ECDSA-CHACHA20-POLY1305:TLS_AES_128_GCM_SHA256:TLS_AES_256_GCM_SHA384:TLS_CHACHA20_POLY1305_SHA256";
    ssl_prefer_server_ciphers off;

    # Load configuration files for the default server block.
    include /etc/nginx/default.d/*.conf;

    location / {
    }

    error_page 404 /404.html;
    location = /40x.html {
    }

    error_page 500 502 503 504 /50x.html;
    location = /50x.html {
    }
}

```

Save the file. 9. Back up the `systemd` configuration file, and then set the
`EnvironmentFile` path.

Amazon Linux 2023

    1. Back up the `nginx.service` file:



    ```
    `$` `cp /lib/systemd/system/nginx.service /lib/systemd/system/nginx.service.backup`
    ```
    2. Open `/lib/systemd/system/nginx.service` in a text editor. Under the [Service] section, add:



    ```
    EnvironmentFile=/etc/sysconfig/nginx
    ```

RHEL 9 (9.2+)

    1. Back up the `nginx.service` file:



    ```
    `$` `cp /lib/systemd/system/nginx.service /lib/systemd/system/nginx.service.backup`
    ```
    2. Open `/lib/systemd/system/nginx.service` in a text editor. Under the [Service] section, add:



    ```
    EnvironmentFile=/etc/sysconfig/nginx
    ```

RHEL 10 (10.0+)

    1. Back up the `nginx.service` file:



    ```
    `$` `cp /lib/systemd/system/nginx.service /lib/systemd/system/nginx.service.backup`
    ```
    2. Open `/lib/systemd/system/nginx.service` in a text editor. Under the [Service] section, add:



    ```
    EnvironmentFile=/etc/sysconfig/nginx
    ```

Ubuntu 24.04

    1. Back up the `nginx.service` file:



    ```
    `$` `cp /lib/systemd/system/nginx.service /lib/systemd/system/nginx.service.backup`
    ```
    2. Open `/lib/systemd/system/nginx.service` in a text editor. Under the [Service] section, add:



    ```
    EnvironmentFile=/etc/sysconfig/nginx
    ```

10. Check if the `/etc/sysconfig/nginx` file exists, and then do one
    of the following:
    - If the file exists, back up the file by running the following command:

    ```
    `$` `cp /etc/sysconfig/nginx /etc/sysconfig/nginx.backup`
    ```

    - If the file doesn't exist, open a text editor, and then create a file named
      `nginx` in the `/etc/sysconfig/` folder.

11. Configure the NGINX environment.

Amazon Linux 2023
As the Linux root user, open `/etc/sysconfig/nginx` file in a
text editor. For example,

```
vi /etc/sysconfig/nginx
```

Add the Cryptography User (CU) credentials and the path to your OpenSSL configuration file:

```
`CLOUDHSM_PIN=`<CU user name>`:`<password>`
OPENSSL_CONF=`<path to example-cloudhsm-openssl.cnf>``
```

Replace `<CU user name>` and
`<password>` with the CU credentials. Replace `<path to example-cloudhsm-openssl.cnf>` with the full path to the configuration file you created in [To configure NGINX for OpenSSL Provider](#configure-nginx-provider "#configure-nginx-provider").

Save the file.

RHEL 9 (9.2+)
Open the `/etc/sysconfig/nginx` file in a text editor. This may require Linux root permissions. Add
the Cryptography User (CU) credentials and the path to your OpenSSL configuration file:

```
`CLOUDHSM_PIN=`<CU user name>`:`<password>`
OPENSSL_CONF=`<path to example-cloudhsm-openssl.cnf>``
```

Replace `<CU user name>` and
`<password>` with the CU credentials. Replace `<path to example-cloudhsm-openssl.cnf>` with the full path to the configuration file you created in [To configure NGINX for OpenSSL Provider](#configure-nginx-provider "#configure-nginx-provider").

Save the file.

RHEL 10 (10.0+)
Open the `/etc/sysconfig/nginx` file in a text editor. This may require Linux root permissions. Add
the Cryptography User (CU) credentials and the path to your OpenSSL configuration file:

```
`CLOUDHSM_PIN=`<CU user name>`:`<password>`
OPENSSL_CONF=`<path to example-cloudhsm-openssl.cnf>``
```

Replace `<CU user name>` and
`<password>` with the CU credentials. Replace `<path to example-cloudhsm-openssl.cnf>` with the full path to the configuration file you created in [To configure NGINX for OpenSSL Provider](#configure-nginx-provider "#configure-nginx-provider").

Save the file.

Ubuntu 24.04
Open the `/etc/sysconfig/nginx` file in a text editor. This may require Linux root permissions. Add
the Cryptography User (CU) credentials and the path to your OpenSSL configuration file:

```
`CLOUDHSM_PIN=`<CU user name>`:`<password>`
OPENSSL_CONF=`<path to example-cloudhsm-openssl.cnf>``
```

Replace `<CU user name>` and
`<password>` with the CU credentials. Replace `<path to example-cloudhsm-openssl.cnf>` with the full path to the configuration file you created in [To configure NGINX for OpenSSL Provider](#configure-nginx-provider "#configure-nginx-provider").

Save the file. 12. Start the NGINX web server.

Amazon Linux 2023
Stop all NGINX processes

```
`$` `systemctl stop nginx`
```

Reload the `systemd` configuration to pick up the latest changes

```
`$` `systemctl daemon-reload`
```

Start NGINX

```
`$` `systemctl start nginx`
```

RHEL 9 (9.2+)
Stop any running NGINX process

```
`$` `systemctl stop nginx`
```

Reload the `systemd` configuration to pick up the latest changes

```
`$` `systemctl daemon-reload`
```

Start the NGINX process

```
`$` `systemctl start nginx`
```

RHEL 10 (10.0+)
Stop any running NGINX process

```
`$` `systemctl stop nginx`
```

Reload the `systemd` configuration to pick up the latest changes

```
`$` `systemctl daemon-reload`
```

Start the NGINX process

```
`$` `systemctl start nginx`
```

Ubuntu 24.04
Stop any running NGINX process

```
`$` `systemctl stop nginx`
```

Reload the `systemd` configuration to pick up the latest changes

```
`$` `systemctl daemon-reload`
```

Start the NGINX process

```
`$` `systemctl start nginx`
```

After you configure NGINX, go to [Verify that HTTPS uses the
certificate that you configured](#ssl-offload-verify-https-connection-linux "#ssl-offload-verify-https-connection-linux").

### Configure HAProxy web server

Use this section to configure HAProxy with the OpenSSL Provider. The following examples show how to set up HAProxy with your CloudHSM certificates and keys.

###### To configure HAProxy for OpenSSL Provider

1. Back up the existing combined certificate file if it exists:

```
`$` `cp server-combined.pem server-combined.pem.backup`
```

2. Create a combined certificate file for HAProxy using your certificate and CloudHSM fake PEM key:

```
`$` `cat server.crt server.key > server-combined.pem`
```

3. Back up the existing HAProxy configuration:

```
`$` `cp /etc/haproxy/haproxy.cfg /etc/haproxy/haproxy.cfg.backup`
```

4. Create a new CloudHSM TLS offload configuration at `/etc/haproxy/haproxy.cfg`:

```
global
    daemon
    ssl-provider cloudhsm
    # It is *strongly* recommended to generate unique DH parameters
    # Generate them with: openssl dhparam -out /etc/haproxy/dhparams.pem 2048
    # ssl-dh-param-file /etc/haproxy/dhparams.pem
    ssl-default-bind-ciphers ECDHE-RSA-AES128-GCM-SHA256:ECDHE-RSA-AES256-GCM-SHA384:DHE-RSA-AES128-GCM-SHA256:DHE-RSA-AES256-GCM-SHA384:ECDHE-RSA-AES256-SHA384:ECDHE-RSA-AES128-SHA256:DHE-RSA-AES128-SHA256:DHE-RSA-AES256-SHA256:ECDHE-RSA-CHACHA20-POLY1305:DHE-RSA-CHACHA20-POLY1305:ECDHE-ECDSA-AES256-GCM-SHA384:ECDHE-ECDSA-AES256-SHA384:ECDHE-ECDSA-AES128-GCM-SHA256:ECDHE-ECDSA-AES128-SHA256:ECDHE-ECDSA-CHACHA20-POLY1305
    ssl-default-bind-ciphersuites TLS_AES_128_GCM_SHA256:TLS_AES_256_GCM_SHA384:TLS_CHACHA20_POLY1305_SHA256
    ssl-default-bind-options ssl-min-ver TLSv1.2 no-tls-tickets

defaults
    mode http
    timeout connect 5000ms
    timeout client 50000ms
    timeout server 50000ms

frontend haproxy_frontend
    bind *:443 ssl crt /path/to/server-combined.pem
    default_backend web_servers

backend web_servers
    server web1 127.0.0.1:8080 check
```

Update the certificate path to match your file location. 5. Configure systemd to use an environment file for HAProxy. The location depends on your Linux distribution.

Amazon Linux and RHEL
Back up and modify the HAProxy service file:

```
`$` `cp /lib/systemd/system/haproxy.service /lib/systemd/system/haproxy.service.backup`
```

Edit `/lib/systemd/system/haproxy.service` and add the following line under the [Service] section:

```
EnvironmentFile=/etc/sysconfig/haproxy
```

Ubuntu
Back up and modify the HAProxy service file:

```
`$` `cp /lib/systemd/system/haproxy.service /lib/systemd/system/haproxy.service.backup`
```

Edit `/lib/systemd/system/haproxy.service` and add the following line under the [Service] section:

```
EnvironmentFile=/etc/default/haproxy
```

6. Create the environment file in the appropriate location for your system.

Amazon Linux and RHEL
Back up the HAProxy environment file if it exists:

```
`$` `cp /etc/sysconfig/haproxy /etc/sysconfig/haproxy.backup`
```

Create the HAProxy environment file `/etc/sysconfig/haproxy` with the following contents:

```
CLOUDHSM_PIN=`<CU user name>`:`<password>`
```

Ubuntu
Back up the HAProxy environment file if it exists:

```
`$` `cp /etc/default/haproxy /etc/default/haproxy.backup`
```

Create the HAProxy environment file `/etc/default/haproxy` with the following contents:

```
CLOUDHSM_PIN=`<CU user name>`:`<password>`
```

Replace `<CU user name>` and `<password>` with your CU credentials. 7. Reload systemd configuration:

```
`$` `systemctl daemon-reload`
```

8. Start HAProxy with the CloudHSM TLS offload configuration:

```
`$` `systemctl start haproxy`
```

You can also run HAProxy directly with a custom configuration file:

```
`$` `haproxy -f /path/to/haproxy-cloudhsm.cfg`
```

After you configure HAProxy, go to [Verify that HTTPS uses the
certificate that you configured](#ssl-offload-verify-https-connection-linux "#ssl-offload-verify-https-connection-linux").

## Step 4: Enable HTTPS traffic

and verify the certificate

After you configure your web server for SSL/TLS offload with AWS CloudHSM, add your web server
instance to a security group that allows inbound HTTPS traffic. This allows clients, such as web
browsers, to establish an HTTPS connection with your web server. Then make an HTTPS connection
to your web server and verify that it's using the certificate that you configured for
SSL/TLS offload with AWS CloudHSM.

###### Topics

- [Enable inbound HTTPS
  connections](#ssl-offload-add-security-group-linux "#ssl-offload-add-security-group-linux")
- [Verify that HTTPS uses the
  certificate that you configured](#ssl-offload-verify-https-connection-linux "#ssl-offload-verify-https-connection-linux")

### Enable inbound HTTPS

connections

To connect to your web server from a client (such as a web browser), create a security
group that allows inbound HTTPS connections. Specifically, it should allow inbound TCP
connections on port 443. Assign this security group to your web server.

###### To create a security group for HTTPS and assign it to your web server

1. Open the Amazon EC2 console at [https://console.aws.amazon.com/ec2/](https://console.aws.amazon.com/ec2/ "https://console.aws.amazon.com/ec2/").
2. Choose **Security groups** in the navigation pane.
3. Choose **Create security group**.
4. For **Create Security Group**, do the following:
   1. For **Security group name**, type a name for the security group
      that you are creating.
   2. (Optional) Type a description of the security group that you are creating.
   3. For **VPC**, choose the VPC that contains your web server Amazon EC2
      instance.
   4. Select **Add Rule**.
   5. For **Type**, select **HTTPS** from the drop-down window.
   6. For **Source**, enter a source location.
   7. Choose **Create security group**.

5. In the navigation pane, choose **Instances**.
6. Select the check box next to your web server instance.
7. Select the **Actions** drop-down menu at the top of the page. Select **Security** and then **Change Security Groups**.
8. For **Associated security groups**, select the search box and choose the security group that you created for HTTPS. Then choose **Add Security Groups**.
9. Select **Save**.

### Verify that HTTPS uses the

certificate that you configured

After you add the web server to a security group, you can verify that SSL/TLS offload is using your self-signed certificate.
You can do this with a web browser or with a tool such as [OpenSSL s_client](https://www.openssl.org/docs/manmaster/man1/s_client.html "https://www.openssl.org/docs/manmaster/man1/s_client.html").

###### To verify SSL/TLS offload with a web browser

1. Use a web browser to connect to your web server using the public DNS name or IP
   address of the server. Ensure that the URL in the address bar begins with https://. For
   example, `https://ec2-52-14-212-67.us-east-2.compute.amazonaws.com/`.

###### Tip

You can use a DNS service such as Amazon Route 53 to route your website's domain name
(for example, https://www.example.com/) to your web server. For more information, see
[Routing Traffic to an Amazon EC2
Instance](../../../Route53/latest/DeveloperGuide/routing-to-ec2-instance.md "../../../Route53/latest/DeveloperGuide/routing-to-ec2-instance.md") in the _Amazon Route 53 Developer Guide_ or in the documentation for
your DNS service. 2. Use your web browser to view the web server certificate. For more information, see the
following:

    * For Mozilla Firefox, see [View a Certificate](https://support.mozilla.org/en-US/kb/secure-website-certificate#w_view-a-certificate "https://support.mozilla.org/en-US/kb/secure-website-certificate#w_view-a-certificate") on the Mozilla Support website.
    * For Google Chrome, see [Understand
     Security Issues](https://developers.google.com/web/tools/chrome-devtools/security "https://developers.google.com/web/tools/chrome-devtools/security") on the Google Tools for Web Developers website.

Other web browsers might have similar features that you can use to view the web server
certificate. 3. Ensure that the SSL/TLS certificate is the one that you configured your web server to
use.

###### To verify SSL/TLS offload with OpenSSL s_client

1. Run the following OpenSSL command to connect to your web server using HTTPS. Replace
   `<server name>` with the public DNS name or IP address of
   your web server.

```
`openssl s_client -connect `<server name>`:443`
```

###### Tip

You can use a DNS service such as Amazon Route 53 to route your website's domain name
(for example, https://www.example.com/) to your web server. For more information, see
[Routing Traffic to an Amazon EC2
Instance](../../../Route53/latest/DeveloperGuide/routing-to-ec2-instance.md "../../../Route53/latest/DeveloperGuide/routing-to-ec2-instance.md") in the _Amazon Route 53 Developer Guide_ or in the documentation for
your DNS service. 2. Ensure that the SSL/TLS certificate is the one that you configured your web server to
use.

You now have a website that is secured with HTTPS. The private key for the web server is
stored in an HSM in your AWS CloudHSM cluster.

To add a load balancer, see [Add a load balancer with Elastic Load Balancing for AWS CloudHSM(optional)](third-offload-add-lb.md "third-offload-add-lb.md").
