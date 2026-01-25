# AWS CloudHSM SSL/TLS offload on Linux using NGINX or

Apache with OpenSSL

This topic provides step-by-step instructions for setting up SSL/TLS offload with AWS CloudHSM
on a Linux web server.

###### Topics

- [Overview](#ssl-offload-linux-openssl-overview "#ssl-offload-linux-openssl-overview")
- [Step 1: Set up the prerequisites](#ssl-offload-prerequisites "#ssl-offload-prerequisites")
- [Step 2: Generate the
  private key and SSL/TLS certificate](#ssl-offload-import-or-generate-private-key-and-certificate "#ssl-offload-import-or-generate-private-key-and-certificate")
- [Step 3: Configure the web server](#ssl-offload-configure-web-server "#ssl-offload-configure-web-server")
- [Step 4: Enable HTTPS traffic
  and verify the certificate](#ssl-offload-enable-traffic-and-verify-certificate "#ssl-offload-enable-traffic-and-verify-certificate")

## Overview

On Linux, the [NGINX](https://nginx.org/en/ "https://nginx.org/en/") and [Apache HTTP Server](https://httpd.apache.org/ "https://httpd.apache.org/") web server software integrate with
[OpenSSL](https://www.openssl.org/ "https://www.openssl.org/") to support HTTPS. The [AWS CloudHSM dynamic engine for OpenSSL](openssl-library.md "openssl-library.md") provides an interface that
enables the web server software to use the HSMs in your cluster for cryptographic offloading
and key storage. The OpenSSL engine is the bridge that connects the web server to your AWS CloudHSM
cluster.

To complete this tutorial, you must first choose whether to use the NGINX or Apache web
server software on Linux. Then the tutorial shows you how to do the following:

- Install the web server software on an Amazon EC2 instance.
- Configure the web server software to support HTTPS with a private key stored in your
  AWS CloudHSM cluster.
- (Optional) Use Amazon EC2 to create a second web server instance and Elastic Load Balancing to create a load
  balancer. Using a load balancer can increase performance by distributing the load across
  multiple servers. It can also provide redundancy and higher availability if one or more
  servers fail.

When you're ready to get started, go to [Step 1: Set up the prerequisites](#ssl-offload-prerequisites "#ssl-offload-prerequisites").

## Step 1: Set up the prerequisites

Different platforms require different prerequisites. Use the prerequisites section below
that matches your platform.

### Prerequisites for Client SDK 5

To set up web server SSL/TLS offload with Client SDK 5, you need the following:

- An active AWS CloudHSM cluster with at least two hardware security modules (HSM)

###### Note

You can use a single HSM cluster, but you must first disable client key
durability. For more information, see [Manage Client
Key Durability Settings](working-client-sync.md#client-sync-sdk8 "working-client-sync.md#client-sync-sdk8") and [Client SDK 5
Configure Tool](configure-sdk-5.md "configure-sdk-5.md").

- An Amazon EC2 instance running a Linux operating system with the following software
  installed:
  - A web server (either NGINX or Apache)
  - The OpenSSL Dynamic Engine for Client SDK 5

- A [crypto user](understanding-users.md#crypto-user-chsm-cli "understanding-users.md#crypto-user-chsm-cli") (CU) to own and manage the web server's
  private key on the HSM.

###### To set up a Linux web server instance and create a CU on the HSM

1. Install and configure the OpenSSL Dynamic Engine for AWS CloudHSM. For more information about
   installing OpenSSL Dynamic Engine, see [OpenSSL Dynamic Engine for
   Client SDK 5](openssl5-install.md "openssl5-install.md").
2. On an EC2 Linux instance that has access to your cluster, install either NGINX or Apache web
   server:

Amazon Linux

    * NGINX



    ```
    `$` `sudo yum install nginx`
    ```
    * Apache



    ```
    `$` `sudo yum install httpd24 mod24_ssl`
    ```

Amazon Linux 2

    * For information on how to download the latest version of NGINX on Amazon Linux 2, see the
     [NGINX website](https://nginx.org/en/linux_packages.html "https://nginx.org/en/linux_packages.html").


    The latest version of NGINX available for Amazon Linux 2 uses a version of OpenSSL that is newer than the
     system version of OpenSSL. After installing NGINX, you need to create a symbolic link from the AWS CloudHSM OpenSSL Dynamic Engine library to the location that
     this version of OpenSSL expects




    ```
    `$` `sudo ln -sf /opt/cloudhsm/lib/libcloudhsm_openssl_engine.so /usr/lib64/engines-1.1/cloudhsm.so`
    ```
    * Apache



    ```
    `$` `sudo yum install httpd mod_ssl`
    ```

Amazon Linux 2023

    * NGINX



    ```
    `$` `sudo yum install nginx`
    ```
    * Apache



    ```
    `$` `sudo yum install httpd mod_ssl`
    ```

CentOS 7

    * For information on how to download the latest version of NGINX on CentOS 7, see the
     [NGINX website](https://nginx.org/en/linux_packages.html "https://nginx.org/en/linux_packages.html").


    The latest version of NGINX available for CentOS 7 uses a version of OpenSSL that is newer than the
     system version of OpenSSL. After installing NGINX, you need to create a symbolic link from the AWS CloudHSM OpenSSL Dynamic Engine library to the location that
     this version of OpenSSL expects




    ```
    `$` `sudo ln -sf /opt/cloudhsm/lib/libcloudhsm_openssl_engine.so /usr/lib64/engines-1.1/cloudhsm.so`
    ```
    * Apache



    ```
    `$` `sudo yum install httpd mod_ssl`
    ```

Red Hat 7

    * For information on how to download the latest version of NGINX on Red Hat 7, see the
     [NGINX website](https://nginx.org/en/linux_packages.html "https://nginx.org/en/linux_packages.html").


    The latest version of NGINX available for Red Hat 7 uses a version of OpenSSL that is newer than the
     system version of OpenSSL. After installing NGINX, you need to create a symbolic link from the AWS CloudHSM OpenSSL Dynamic Engine library to the location that
     this version of OpenSSL expects




    ```
    `$` `sudo ln -sf /opt/cloudhsm/lib/libcloudhsm_openssl_engine.so /usr/lib64/engines-1.1/cloudhsm.so`
    ```
    * Apache



    ```
    `$` `sudo yum install httpd mod_ssl`
    ```

CentOS 8

    * NGINX



    ```
    `$` `sudo yum install nginx`
    ```
    * Apache



    ```
    `$` `sudo yum install httpd mod_ssl`
    ```

Red Hat 8

    * NGINX



    ```
    `$` `sudo yum install nginx`
    ```
    * Apache



    ```
    `$` `sudo yum install httpd mod_ssl`
    ```

Ubuntu 18.04

    * NGINX



    ```
    `$` `sudo apt install nginx`
    ```
    * Apache



    ```
    `$` `sudo apt install apache2`
    ```

Ubuntu 20.04

    * NGINX



    ```
    `$` `sudo apt install nginx`
    ```
    * Apache



    ```
    `$` `sudo apt install apache2`
    ```

Ubuntu 22.04

    * NGINX



    ```
    `$` `sudo apt install nginx`
    ```
    * Apache



    ```
    `$` `sudo apt install apache2`
    ```

Ubuntu 24.04

    * NGINX



    ```
    `$` `sudo apt install nginx`
    ```
    * Apache



    ```
    `$` `sudo apt install apache2`
    ```

3. Use CloudHSM CLI to create a [crypto user](understanding-users.md#crypto-user-chsm-cli "understanding-users.md#crypto-user-chsm-cli"). For more information about
   managing HSM users, see [Managing HSM users with CloudHSM CLI](manage-hsm-users-chsm-cli.md "manage-hsm-users-chsm-cli.md").

###### Tip

Keep track of the CU user name and password. You will need them later when you
generate or import the HTTPS private key and certificate for your web server.

After you complete these steps, go to [Step 2: Generate the
private key and SSL/TLS certificate](#ssl-offload-import-or-generate-private-key-and-certificate "#ssl-offload-import-or-generate-private-key-and-certificate").

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

## Step 2: Generate the

private key and SSL/TLS certificate

To enable HTTPS, your web server application (NGINX or Apache) needs a private key and a
corresponding SSL/TLS certificate. To use web server SSL/TLS offload with AWS CloudHSM, you must store
the private key in an HSM in your AWS CloudHSM cluster. You will first generate a private key and use
the key to create a certificate signing request (CSR). You then export a _fake PEM
private key_ from the HSM, which is a private key file in PEM format which contains a reference to
the private key stored on the HSM (it's not the actual private key). Your web server uses the fake PEM private key file
to identify the private key on the HSM during SSL/TLS offload.

### Generate a private key and certificate

#### Generate a private key

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
`Command:` `login --username `<user name>` --role crypto-user`
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
 "modulus": "0xb1d27e857a876f4e9fd5de748a763c539b359f937eb4b4260e30d1435485a732c878cdad9c72538e2215351b1d41358c9bf80b599c
73a80fdb457aa7b20cd61e486c326e2cfd5e124a7f6a996437437812b542e3caf85928aa866f0298580f7967ee6aa01440297d7308fdd9b76b70d1b67f12634d
f6e6296d6c116d5744c6d60d14d3bf3cb978fe6b75ac67b7089bafd50d8687213b31abc7dc1bad422780d29c851d5102b56f932551eaf52a9591fd8c43d81ecc
133022653225bd129f8491101725e9ea33e1ded83fb57af35f847e532eb30cd7e726f23910d2671c6364092e834697ec3cef72cc23615a1ba7c5e100156ae0ac
ac3160f0ca9725d38318b7",
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

#### Generate a self-signed certificate

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

After you complete these steps, go to [Step 3: Configure the web server](#ssl-offload-configure-web-server "#ssl-offload-configure-web-server").

## Step 3: Configure the web server

Update your web server software's configuration to use the HTTPS certificate and
corresponding fake PEM private key that you created in the [previous step](#ssl-offload-import-or-generate-private-key-and-certificate "#ssl-offload-import-or-generate-private-key-and-certificate").
Remember to backup your existing certificates and keys before you start. This
will finish setting up your Linux web server software for SSL/TLS offload with AWS CloudHSM.

Complete the steps from one of the following sections.

###### Topics

- [Configure NGINX web server](#ssl-offload-nginx "#ssl-offload-nginx")
- [Configure Apache web server](#ssl-offload-apache "#ssl-offload-apache")

### Configure NGINX web server

Use this section to configure NGINX on supported platforms.

###### To update the web server configuration for NGINX

1. Connect to your client instance.
2. Run the following command to create the required directories for the web server
   certificate and the fake PEM private key.

```
`$` `sudo mkdir -p /etc/pki/nginx/private`
```

3. Run the following command to copy your web server certificate to the required
   location. Replace `<web_server.crt>` with the name of your
   web server certificate.

```
`$` `sudo cp `<web_server.crt>` /etc/pki/nginx/server.crt`
```

4. Run the following command to copy your fake PEM private key to the required location.
   Replace `<web_server_fake_pem.key>` with the name of the
   file that contains your fake PEM private key.

```
`$` `sudo cp `<web_server_example_pem.key>` /etc/pki/nginx/private/server.key`
```

5. Run the following command to change the file ownership so that the user named
   _nginx_ can read them.

```
`$` `sudo chown nginx /etc/pki/nginx/server.crt /etc/pki/nginx/private/server.key`
```

6. Run the following command to back up the `/etc/nginx/nginx.conf`
   file.

```
`$` `sudo cp /etc/nginx/nginx.conf /etc/nginx/nginx.conf.backup`
```

7. Update the NGINX configuration.

###### Note

Each cluster can support a maximum of 1000 NGINX worker processes across
all NGINX web servers.

Amazon Linux
Use a text editor to edit the `/etc/nginx/nginx.conf` file. This requires Linux root permissions. At the
top of the file, add the following lines:

```
ssl_engine cloudhsm;
env CLOUDHSM_PIN;
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
    # It is *strongly* recommended to generate unique DH parameters
    # Generate them with: openssl dhparam -out /etc/pki/nginx/dhparams.pem 2048
    #ssl_dhparam "/etc/pki/nginx/dhparams.pem";
    ssl_session_cache shared:SSL:1m;
    ssl_session_timeout  10m;
    ssl_protocols TLSv1.2;
    ssl_ciphers "ECDHE-RSA-AES128-GCM-SHA256:ECDHE-RSA-AES256-GCM-SHA384:DHE-RSA-AES128-GCM-SHA256:DHE-RSA-AES256-GCM-SHA384:ECDHE-RSA-AES256-SHA384:ECDHE-RSA-AES128-SHA256:ECDHE-RSA-AES256-SHA384:DHE-RSA-AES128-SHA:DHE-RSA-AES256-SHA:DHE-RSA-AES128-SHA256:DHE-RSA-AES256-SHA256:ECDHE-ECDSA-AES256-GCM-SHA384:ECDHE-ECDSA-AES256-SHA384:ECDHE-ECDSA-AES128-GCM-SHA256:ECDHE-ECDSA-AES128-SHA256:ECDHE-ECDSA-AES256-SHA:ECDHE-ECDSA-AES128-SHA";
    ssl_prefer_server_ciphers on;

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

Amazon Linux 2
Use a text editor to edit the `/etc/nginx/nginx.conf` file. This requires Linux root permissions. At the
top of the file, add the following lines:

```
ssl_engine cloudhsm;
env CLOUDHSM_PIN;
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
    # It is *strongly* recommended to generate unique DH parameters
    # Generate them with: openssl dhparam -out /etc/pki/nginx/dhparams.pem 2048
    #ssl_dhparam "/etc/pki/nginx/dhparams.pem";
    ssl_session_cache shared:SSL:1m;
    ssl_session_timeout  10m;
    ssl_protocols TLSv1.2;
    ssl_ciphers "ECDHE-RSA-AES128-GCM-SHA256:ECDHE-RSA-AES256-GCM-SHA384:DHE-RSA-AES128-GCM-SHA256:DHE-RSA-AES256-GCM-SHA384:ECDHE-RSA-AES256-SHA384:ECDHE-RSA-AES128-SHA256:ECDHE-RSA-AES256-SHA384:DHE-RSA-AES128-SHA:DHE-RSA-AES256-SHA:DHE-RSA-AES128-SHA256:DHE-RSA-AES256-SHA256:ECDHE-ECDSA-AES256-GCM-SHA384:ECDHE-ECDSA-AES256-SHA384:ECDHE-ECDSA-AES128-GCM-SHA256:ECDHE-ECDSA-AES128-SHA256:ECDHE-ECDSA-AES256-SHA:ECDHE-ECDSA-AES128-SHA";
    ssl_prefer_server_ciphers on;

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

Amazon Linux 2023
Use a text editor to edit the `/etc/nginx/nginx.conf` file. This requires Linux root permissions. At the
top of the file, add the following lines:

```
ssl_engine cloudhsm;
env CLOUDHSM_PIN;
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
    # It is *strongly* recommended to generate unique DH parameters
    # Generate them with: openssl dhparam -out /etc/pki/nginx/dhparams.pem 2048
    #ssl_dhparam "/etc/pki/nginx/dhparams.pem";
    ssl_session_cache shared:SSL:1m;
    ssl_session_timeout  10m;
    ssl_protocols TLSv1.2;
    ssl_ciphers "ECDHE-RSA-AES128-GCM-SHA256:ECDHE-RSA-AES256-GCM-SHA384:DHE-RSA-AES128-GCM-SHA256:DHE-RSA-AES256-GCM-SHA384:ECDHE-RSA-AES256-SHA384:ECDHE-RSA-AES128-SHA256:ECDHE-RSA-AES256-SHA384:DHE-RSA-AES128-SHA:DHE-RSA-AES256-SHA:DHE-RSA-AES128-SHA256:DHE-RSA-AES256-SHA256:ECDHE-ECDSA-AES256-GCM-SHA384:ECDHE-ECDSA-AES256-SHA384:ECDHE-ECDSA-AES128-GCM-SHA256:ECDHE-ECDSA-AES128-SHA256:ECDHE-ECDSA-AES256-SHA:ECDHE-ECDSA-AES128-SHA";
    ssl_prefer_server_ciphers on;

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

CentOS 7
Use a text editor to edit the `/etc/nginx/nginx.conf` file. This requires Linux root permissions. At the
top of the file, add the following lines:

```
ssl_engine cloudhsm;
env CLOUDHSM_PIN;
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
    # It is *strongly* recommended to generate unique DH parameters
    # Generate them with: openssl dhparam -out /etc/pki/nginx/dhparams.pem 2048
    #ssl_dhparam "/etc/pki/nginx/dhparams.pem";
    ssl_session_cache shared:SSL:1m;
    ssl_session_timeout  10m;
    ssl_protocols TLSv1.2;
    ssl_ciphers "ECDHE-RSA-AES128-GCM-SHA256:ECDHE-RSA-AES256-GCM-SHA384:DHE-RSA-AES128-GCM-SHA256:DHE-RSA-AES256-GCM-SHA384:ECDHE-RSA-AES256-SHA384:ECDHE-RSA-AES128-SHA256:ECDHE-RSA-AES256-SHA384:DHE-RSA-AES128-SHA:DHE-RSA-AES256-SHA:DHE-RSA-AES128-SHA256:DHE-RSA-AES256-SHA256:ECDHE-ECDSA-AES256-GCM-SHA384:ECDHE-ECDSA-AES256-SHA384:ECDHE-ECDSA-AES128-GCM-SHA256:ECDHE-ECDSA-AES128-SHA256:ECDHE-ECDSA-AES256-SHA:ECDHE-ECDSA-AES128-SHA";
    ssl_prefer_server_ciphers on;

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

CentOS 8
Use a text editor to edit the `/etc/nginx/nginx.conf` file. This requires Linux root permissions. At the
top of the file, add the following lines:

```
ssl_engine cloudhsm;
env CLOUDHSM_PIN;
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
    # It is *strongly* recommended to generate unique DH parameters
    # Generate them with: openssl dhparam -out /etc/pki/nginx/dhparams.pem 2048
    #ssl_dhparam "/etc/pki/nginx/dhparams.pem";
    ssl_session_cache shared:SSL:1m;
    ssl_session_timeout  10m;
    ssl_protocols TLSv1.2 TLSv1.3;
    ssl_ciphers "ECDHE-RSA-AES128-GCM-SHA256:ECDHE-RSA-AES256-GCM-SHA384:DHE-RSA-AES128-GCM-SHA256:DHE-RSA-AES256-GCM-SHA384:ECDHE-RSA-AES256-SHA384:ECDHE-RSA-AES128-SHA256:ECDHE-RSA-AES256-SHA384:DHE-RSA-AES128-SHA:DHE-RSA-AES256-SHA:DHE-RSA-AES128-SHA256:DHE-RSA-AES256-SHA256:ECDHE-ECDSA-AES256-GCM-SHA384:ECDHE-ECDSA-AES256-SHA384:ECDHE-ECDSA-AES128-GCM-SHA256:ECDHE-ECDSA-AES128-SHA256:ECDHE-ECDSA-AES256-SHA:ECDHE-ECDSA-AES128-SHA";
    ssl_prefer_server_ciphers on;

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

Red Hat 7
Use a text editor to edit the `/etc/nginx/nginx.conf` file. This requires Linux root permissions. At the
top of the file, add the following lines:

```
ssl_engine cloudhsm;
env CLOUDHSM_PIN;
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
    # It is *strongly* recommended to generate unique DH parameters
    # Generate them with: openssl dhparam -out /etc/pki/nginx/dhparams.pem 2048
    #ssl_dhparam "/etc/pki/nginx/dhparams.pem";
    ssl_session_cache shared:SSL:1m;
    ssl_session_timeout  10m;
    ssl_protocols TLSv1.2;
    ssl_ciphers "ECDHE-RSA-AES128-GCM-SHA256:ECDHE-RSA-AES256-GCM-SHA384:DHE-RSA-AES128-GCM-SHA256:DHE-RSA-AES256-GCM-SHA384:ECDHE-RSA-AES256-SHA384:ECDHE-RSA-AES128-SHA256:ECDHE-RSA-AES256-SHA384:DHE-RSA-AES128-SHA:DHE-RSA-AES256-SHA:DHE-RSA-AES128-SHA256:DHE-RSA-AES256-SHA256:ECDHE-ECDSA-AES256-GCM-SHA384:ECDHE-ECDSA-AES256-SHA384:ECDHE-ECDSA-AES128-GCM-SHA256:ECDHE-ECDSA-AES128-SHA256:ECDHE-ECDSA-AES256-SHA:ECDHE-ECDSA-AES128-SHA";
    ssl_prefer_server_ciphers on;

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

Red Hat 8
Use a text editor to edit the `/etc/nginx/nginx.conf` file. This requires Linux root permissions. At the
top of the file, add the following lines:

```
ssl_engine cloudhsm;
env CLOUDHSM_PIN;
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
    # It is *strongly* recommended to generate unique DH parameters
    # Generate them with: openssl dhparam -out /etc/pki/nginx/dhparams.pem 2048
    #ssl_dhparam "/etc/pki/nginx/dhparams.pem";
    ssl_session_cache shared:SSL:1m;
    ssl_session_timeout  10m;
    ssl_protocols TLSv1.2 TLSv1.3;
    ssl_ciphers "ECDHE-RSA-AES128-GCM-SHA256:ECDHE-RSA-AES256-GCM-SHA384:DHE-RSA-AES128-GCM-SHA256:DHE-RSA-AES256-GCM-SHA384:ECDHE-RSA-AES256-SHA384:ECDHE-RSA-AES128-SHA256:ECDHE-RSA-AES256-SHA384:DHE-RSA-AES128-SHA:DHE-RSA-AES256-SHA:DHE-RSA-AES128-SHA256:DHE-RSA-AES256-SHA256:ECDHE-ECDSA-AES256-GCM-SHA384:ECDHE-ECDSA-AES256-SHA384:ECDHE-ECDSA-AES128-GCM-SHA256:ECDHE-ECDSA-AES128-SHA256:ECDHE-ECDSA-AES256-SHA:ECDHE-ECDSA-AES128-SHA";
    ssl_prefer_server_ciphers on;

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

Ubuntu 16.04 LTS
Use a text editor to edit the `/etc/nginx/nginx.conf` file. This requires Linux root permissions. At the
top of the file, add the following lines:

```
ssl_engine cloudhsm;
    env n3fips_password;
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
        # It is *strongly* recommended to generate unique DH parameters
        # Generate them with: openssl dhparam -out /etc/pki/nginx/dhparams.pem 2048
        #ssl_dhparam "/etc/pki/nginx/dhparams.pem";
        ssl_session_cache shared:SSL:1m;
        ssl_session_timeout  10m;
        ssl_protocols TLSv1.2;
        ssl_ciphers "ECDHE-RSA-AES128-GCM-SHA256:ECDHE-RSA-AES256-GCM-SHA384:DHE-RSA-AES128-GCM-SHA256:DHE-RSA-AES256-GCM-SHA384:ECDHE-RSA-AES256-SHA384:ECDHE-RSA-AES128-SHA256:ECDHE-RSA-AES256-SHA384:DHE-RSA-AES128-SHA:DHE-RSA-AES256-SHA:DHE-RSA-AES128-SHA256:DHE-RSA-AES256-SHA256:ECDHE-ECDSA-AES256-GCM-SHA384:ECDHE-ECDSA-AES256-SHA384:ECDHE-ECDSA-AES128-GCM-SHA256:ECDHE-ECDSA-AES128-SHA256:ECDHE-ECDSA-AES256-SHA:ECDHE-ECDSA-AES128-SHA";
        ssl_prefer_server_ciphers on;

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

Ubuntu 18.04 LTS
Use a text editor to edit the `/etc/nginx/nginx.conf` file. This requires Linux root permissions. At the
top of the file, add the following lines:

```
ssl_engine cloudhsm;
    env CLOUDHSM_PIN;
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
        # It is *strongly* recommended to generate unique DH parameters
        # Generate them with: openssl dhparam -out /etc/pki/nginx/dhparams.pem 2048
        #ssl_dhparam "/etc/pki/nginx/dhparams.pem";
        ssl_session_cache shared:SSL:1m;
        ssl_session_timeout  10m;
        ssl_protocols TLSv1.2 TLSv1.3;
        ssl_ciphers "ECDHE-RSA-AES128-GCM-SHA256:ECDHE-RSA-AES256-GCM-SHA384:DHE-RSA-AES128-GCM-SHA256:DHE-RSA-AES256-GCM-SHA384:ECDHE-RSA-AES256-SHA384:ECDHE-RSA-AES128-SHA256:ECDHE-RSA-AES256-SHA384:DHE-RSA-AES128-SHA:DHE-RSA-AES256-SHA:DHE-RSA-AES128-SHA256:DHE-RSA-AES256-SHA256:ECDHE-ECDSA-AES256-GCM-SHA384:ECDHE-ECDSA-AES256-SHA384:ECDHE-ECDSA-AES128-GCM-SHA256:ECDHE-ECDSA-AES128-SHA256:ECDHE-ECDSA-AES256-SHA:ECDHE-ECDSA-AES128-SHA";
        ssl_prefer_server_ciphers on;

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

Ubuntu 20.04 LTS
Use a text editor to edit the `/etc/nginx/nginx.conf` file. This requires Linux root permissions. At the
top of the file, add the following lines:

```
ssl_engine cloudhsm;
    env CLOUDHSM_PIN;
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
        # It is *strongly* recommended to generate unique DH parameters
        # Generate them with: openssl dhparam -out /etc/pki/nginx/dhparams.pem 2048
        #ssl_dhparam "/etc/pki/nginx/dhparams.pem";
        ssl_session_cache shared:SSL:1m;
        ssl_session_timeout  10m;
        ssl_protocols TLSv1.2 TLSv1.3;
        ssl_ciphers "ECDHE-RSA-AES128-GCM-SHA256:ECDHE-RSA-AES256-GCM-SHA384:DHE-RSA-AES128-GCM-SHA256:DHE-RSA-AES256-GCM-SHA384:ECDHE-RSA-AES256-SHA384:ECDHE-RSA-AES128-SHA256:ECDHE-RSA-AES256-SHA384:DHE-RSA-AES128-SHA:DHE-RSA-AES256-SHA:DHE-RSA-AES128-SHA256:DHE-RSA-AES256-SHA256:ECDHE-ECDSA-AES256-GCM-SHA384:ECDHE-ECDSA-AES256-SHA384:ECDHE-ECDSA-AES128-GCM-SHA256:ECDHE-ECDSA-AES128-SHA256:ECDHE-ECDSA-AES256-SHA:ECDHE-ECDSA-AES128-SHA";
        ssl_prefer_server_ciphers on;

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

Ubuntu 22.04 LTS
Use a text editor to edit the `/etc/nginx/nginx.conf` file. This requires Linux root permissions. At the
top of the file, add the following lines:

```
ssl_engine cloudhsm;
  env CLOUDHSM_PIN;
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
        # It is *strongly* recommended to generate unique DH parameters
        # Generate them with: openssl dhparam -out /etc/pki/nginx/dhparams.pem 2048
        #ssl_dhparam "/etc/pki/nginx/dhparams.pem";
        ssl_session_cache shared:SSL:1m;
        ssl_session_timeout  10m;
        ssl_protocols TLSv1.2 TLSv1.3;
        ssl_ciphers "ECDHE-RSA-AES128-GCM-SHA256:ECDHE-RSA-AES256-GCM-SHA384:DHE-RSA-AES128-GCM-SHA256:DHE-RSA-AES256-GCM-SHA384:ECDHE-RSA-AES256-SHA384:ECDHE-RSA-AES128-SHA256:ECDHE-RSA-AES256-SHA384:DHE-RSA-AES128-SHA:DHE-RSA-AES256-SHA:DHE-RSA-AES128-SHA256:DHE-RSA-AES256-SHA256:ECDHE-ECDSA-AES256-GCM-SHA384:ECDHE-ECDSA-AES256-SHA384:ECDHE-ECDSA-AES128-GCM-SHA256:ECDHE-ECDSA-AES128-SHA256:ECDHE-ECDSA-AES256-SHA:ECDHE-ECDSA-AES128-SHA";
        ssl_prefer_server_ciphers on;

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

Ubuntu 24.04 LTS
Use a text editor to edit the `/etc/nginx/nginx.conf` file. This requires Linux root permissions. At the
top of the file, add the following lines:

```
ssl_engine cloudhsm;
  env CLOUDHSM_PIN;
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
        # It is *strongly* recommended to generate unique DH parameters
        # Generate them with: openssl dhparam -out /etc/pki/nginx/dhparams.pem 2048
        #ssl_dhparam "/etc/pki/nginx/dhparams.pem";
        ssl_session_cache shared:SSL:1m;
        ssl_session_timeout  10m;
        ssl_protocols TLSv1.2 TLSv1.3;
        ssl_ciphers "ECDHE-RSA-AES128-GCM-SHA256:ECDHE-RSA-AES256-GCM-SHA384:DHE-RSA-AES128-GCM-SHA256:DHE-RSA-AES256-GCM-SHA384:ECDHE-RSA-AES256-SHA384:ECDHE-RSA-AES128-SHA256:ECDHE-RSA-AES256-SHA384:DHE-RSA-AES128-SHA:DHE-RSA-AES256-SHA:DHE-RSA-AES128-SHA256:DHE-RSA-AES256-SHA256:ECDHE-ECDSA-AES256-GCM-SHA384:ECDHE-ECDSA-AES256-SHA384:ECDHE-ECDSA-AES128-GCM-SHA256:ECDHE-ECDSA-AES128-SHA256:ECDHE-ECDSA-AES256-SHA:ECDHE-ECDSA-AES128-SHA";
        ssl_prefer_server_ciphers on;

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

Save the file. 8. Back up the `systemd` configuration file, and then set the
`EnvironmentFile` path.

Amazon Linux
No action required.

Amazon Linux 2

    1. Back up the `nginx.service` file.



    ```
    `$` `sudo cp /lib/systemd/system/nginx.service /lib/systemd/system/nginx.service.backup`
    ```
    2. Open the `/lib/systemd/system/nginx.service` file in a
     text editor, and then under the [Service] section, add the following path:



    ```
    EnvironmentFile=/etc/sysconfig/nginx
    ```

Amazon Linux 2023

    1. Back up the `nginx.service` file.



    ```
    `$` `sudo cp /lib/systemd/system/nginx.service /lib/systemd/system/nginx.service.backup`
    ```
    2. Open `/lib/systemd/system/nginx.service` in a text editor. Under the [Service] section, add:



    ```
    EnvironmentFile=/etc/sysconfig/nginx
    ```

CentOS 7
No action required.

CentOS 8

    1. Back up the `nginx.service` file.



    ```
    `$` `sudo cp /lib/systemd/system/nginx.service /lib/systemd/system/nginx.service.backup`
    ```
    2. Open the `/lib/systemd/system/nginx.service` file in a
     text editor, and then under the [Service] section, add the following path:



    ```
    EnvironmentFile=/etc/sysconfig/nginx
    ```

Red Hat 7
No action required.

Red Hat 8

    1. Back up the `nginx.service` file.



    ```
    `$` `sudo cp /lib/systemd/system/nginx.service /lib/systemd/system/nginx.service.backup`
    ```
    2. Open the `/lib/systemd/system/nginx.service` file in a
     text editor, and then under the [Service] section, add the following path:



    ```
    EnvironmentFile=/etc/sysconfig/nginx
    ```

Ubuntu 16.04

    1. Back up the `nginx.service` file.



    ```
    `$` `sudo cp /lib/systemd/system/nginx.service /lib/systemd/system/nginx.service.backup`
    ```
    2. Open the `/lib/systemd/system/nginx.service` file in a
     text editor, and then under the [Service] section, add the following path:



    ```
    EnvironmentFile=/etc/sysconfig/nginx
    ```

Ubuntu 18.04

    1. Back up the `nginx.service` file.



    ```
    `$` `sudo cp /lib/systemd/system/nginx.service /lib/systemd/system/nginx.service.backup`
    ```
    2. Open the `/lib/systemd/system/nginx.service` file in a
     text editor, and then under the [Service] section, add the following path:



    ```
    EnvironmentFile=/etc/sysconfig/nginx
    ```

Ubuntu 20.04 LTS

    1. Back up the `nginx.service` file.



    ```
    `$` `sudo cp /lib/systemd/system/nginx.service /lib/systemd/system/nginx.service.backup`
    ```
    2. Open the `/lib/systemd/system/nginx.service` file in a
     text editor, and then under the [Service] section, add the following path:



    ```
    EnvironmentFile=/etc/sysconfig/nginx
    ```

Ubuntu 22.04 LTS

    1. Back up the `nginx.service` file.



    ```
    `$` `sudo cp /lib/systemd/system/nginx.service /lib/systemd/system/nginx.service.backup`
    ```
    2. Open the `/lib/systemd/system/nginx.service` file in a
     text editor, and then under the [Service] section, add the following path:



    ```
    EnvironmentFile=/etc/sysconfig/nginx
    ```

Ubuntu 24.04 LTS

    1. Back up the `nginx.service` file.



    ```
    `$` `sudo cp /lib/systemd/system/nginx.service /lib/systemd/system/nginx.service.backup`
    ```
    2. Open the `/lib/systemd/system/nginx.service` file in a
     text editor, and then under the [Service] section, add the following path:



    ```
    EnvironmentFile=/etc/sysconfig/nginx
    ```

9. Check if the `/etc/sysconfig/nginx` file exists, and then do one
   of the following:
   - If the file exists, back up the file by running the following command:

   ```
   `$` `sudo cp /etc/sysconfig/nginx /etc/sysconfig/nginx.backup`
   ```

   - If the file doesn't exist, open a text editor, and then create a file named
     `nginx` in the `/etc/sysconfig/` folder.

10. Configure the NGINX environment.

###### Note

Client SDK 5 introduces the `CLOUDHSM_PIN` environment variable for
storing the credentials of the CU.

Amazon Linux
Open the `/etc/sysconfig/nginx` file in a text editor. This requires Linux root permissions. Add
the Cryptography User (CU) credentials:

```
ssl_engine cloudhsm;
env CLOUDHSM_PIN;
```

Replace `<CU user name>` and
`<password>` with the CU credentials.

Save the file.

Amazon Linux 2
Open the `/etc/sysconfig/nginx` file in a text editor. This requires Linux root permissions. Add
the Cryptography User (CU) credentials:

```
ssl_engine cloudhsm;
env CLOUDHSM_PIN;
```

Replace `<CU user name>` and
`<password>` with the CU credentials.

Save the file.

Amazon Linux 2023
As the Linux root user, open `/etc/sysconfig/nginx` file in a
text editor. For example,

```
sudo vi /etc/sysconfig/nginx
```

Add the Cryptography User (CU) credentials:

```
`CLOUDHSM_PIN=`<CU user name>`:`<password>``
```

Replace `<CU user name>` and
`<password>` with the CU credentials.

Save the file.

CentOS 7
Open the `/etc/sysconfig/nginx` file in a text editor. This requires Linux root permissions. Add
the Cryptography User (CU) credentials:

```
ssl_engine cloudhsm;
env CLOUDHSM_PIN;
```

Replace `<CU user name>` and
`<password>` with the CU credentials.

Save the file.

CentOS 8
Open the `/etc/sysconfig/nginx` file in a text editor. This requires Linux root permissions. Add
the Cryptography User (CU) credentials:

```
`CLOUDHSM_PIN=`<CU user name>`:`<password>``
```

Replace `<CU user name>` and
`<password>` with the CU credentials.

Save the file.

Red Hat 7
Open the `/etc/sysconfig/nginx` file in a text editor. This requires Linux root permissions. Add
the Cryptography User (CU) credentials:

```
ssl_engine cloudhsm;
env CLOUDHSM_PIN;
```

Replace `<CU user name>` and
`<password>` with the CU credentials.

Save the file.

Red Hat 8
Open the `/etc/sysconfig/nginx` file in a text editor. This requires Linux root permissions. Add
the Cryptography User (CU) credentials:

```
`CLOUDHSM_PIN=`<CU user name>`:`<password>``
```

Replace `<CU user name>` and
`<password>` with the CU credentials.

Save the file.

Ubuntu 16.04 LTS
Open the `/etc/sysconfig/nginx` file in a text editor. This requires Linux root permissions. Add
the Cryptography User (CU) credentials:

```
`n3fips_password=`<CU user name>`:`<password>``
```

Replace `<CU user name>` and
`<password>` with the CU credentials.

Save the file.

Ubuntu 18.04 LTS
Open the `/etc/sysconfig/nginx` file in a text editor. This requires Linux root permissions. Add
the Cryptography User (CU) credentials:

```
`CLOUDHSM_PIN=`<CU user name>`:`<password>``
```

Replace `<CU user name>` and
`<password>` with the CU credentials.

Save the file.

Ubuntu 20.04 LTS
Open the `/etc/sysconfig/nginx` file in a text editor. This requires Linux root permissions. Add
the Cryptography User (CU) credentials:

```
`CLOUDHSM_PIN=`<CU user name>`:`<password>``
```

Replace `<CU user name>` and
`<password>` with the CU credentials.

Save the file.

Ubuntu 22.04 LTS
Open the `/etc/sysconfig/nginx` file in a text editor. This requires Linux root permissions. Add
the Cryptography User (CU) credentials:

```
`CLOUDHSM_PIN=`<CU user name>`:`<password>``
```

Replace `<CU user name>` and
`<password>` with the CU credentials.

Save the file.

Ubuntu 24.04 LTS
Open the `/etc/sysconfig/nginx` file in a text editor. This requires Linux root permissions. Add
the Cryptography User (CU) credentials:

```
`CLOUDHSM_PIN=`<CU user name>`:`<password>``
```

Replace `<CU user name>` and
`<password>` with the CU credentials.

Save the file. 11. Start the NGINX web server.

Amazon Linux
Open the `/etc/sysconfig/nginx` file in a text editor. This requires Linux root permissions. Add
the Cryptography User (CU) credentials:

```
`$` `sudo service nginx start`
```

Amazon Linux 2
Stop any running NGINX process

```
`$` `sudo systemctl stop nginx`
```

Reload the `systemd` configuration to pick up the latest changes

```
`$` `sudo systemctl daemon-reload`
```

Start the NGINX process

```
`$` `sudo systemctl start nginx`
```

Amazon Linux 2023
Stop all NGINX processes

```
`$` `sudo systemctl stop nginx`
```

Reload the `systemd` configuration to pick up the latest changes

```
`$` `sudo systemctl daemon-reload`
```

Start NGINX

```
`$` `sudo systemctl start nginx`
```

CentOS 7
Stop any running NGINX process

```
`$` `sudo systemctl stop nginx`
```

Reload the `systemd` configuration to pick up the latest changes

```
`$` `sudo systemctl daemon-reload`
```

Start the NGINX process

```
`$` `sudo systemctl start nginx`
```

CentOS 8
Stop any running NGINX process

```
`$` `sudo systemctl stop nginx`
```

Reload the `systemd` configuration to pick up the latest changes

```
`$` `sudo systemctl daemon-reload`
```

Start the NGINX process

```
`$` `sudo systemctl start nginx`
```

Red Hat 7
Stop any running NGINX process

```
`$` `sudo systemctl stop nginx`
```

Reload the `systemd` configuration to pick up the latest changes

```
`$` `sudo systemctl daemon-reload`
```

Start the NGINX process

```
`$` `sudo systemctl start nginx`
```

Red Hat 8
Stop any running NGINX process

```
`$` `sudo systemctl stop nginx`
```

Reload the `systemd` configuration to pick up the latest changes

```
`$` `sudo systemctl daemon-reload`
```

Start the NGINX process

```
`$` `sudo systemctl start nginx`
```

Ubuntu 16.04 LTS
Stop any running NGINX process

```
`$` `sudo systemctl stop nginx`
```

Reload the `systemd` configuration to pick up the latest changes

```
`$` `sudo systemctl daemon-reload`
```

Start the NGINX process

```
`$` `sudo systemctl start nginx`
```

Ubuntu 18.04 LTS
Stop any running NGINX process

```
`$` `sudo systemctl stop nginx`
```

Reload the `systemd` configuration to pick up the latest changes

```
`$` `sudo systemctl daemon-reload`
```

Start the NGINX process

```
`$` `sudo systemctl start nginx`
```

Ubuntu 20.04 LTS
Stop any running NGINX process

```
`$` `sudo systemctl stop nginx`
```

Reload the `systemd` configuration to pick up the latest changes

```
`$` `sudo systemctl daemon-reload`
```

Start the NGINX process

```
`$` `sudo systemctl start nginx`
```

Ubuntu 22.04 LTS
Stop any running NGINX process

```
`$` `sudo systemctl stop nginx`
```

Reload the `systemd` configuration to pick up the latest changes

```
`$` `sudo systemctl daemon-reload`
```

Start the NGINX process

```
`$` `sudo systemctl start nginx`
```

Ubuntu 24.04 LTS
Stop any running NGINX process

```
`$` `sudo systemctl stop nginx`
```

Reload the `systemd` configuration to pick up the latest changes

```
`$` `sudo systemctl daemon-reload`
```

Start the NGINX process

```
`$` `sudo systemctl start nginx`
```

12. (Optional) Configure your platform to start NGINX at start-up.

Amazon Linux

```
`$` `sudo chkconfig nginx on`
```

Amazon Linux 2

```
`$` `sudo systemctl enable nginx`
```

Amazon Linux 2023

```
`$` `sudo systemctl enable nginx`
```

CentOS 7
No action required.

CentOS 8

```
`$` `sudo systemctl enable nginx`
```

Red Hat 7
No action required.

Red Hat 8

```
`$` `sudo systemctl enable nginx`
```

Ubuntu 16.04 LTS

```
`$` `sudo systemctl enable nginx`
```

Ubuntu 18.04 LTS

```
`$` `sudo systemctl enable nginx`
```

Ubuntu 20.04 LTS

```
`$` `sudo systemctl enable nginx`
```

Ubuntu 22.04 LTS

```
`$` `sudo systemctl enable nginx`
```

Ubuntu 24.04 LTS

```
`$` `sudo systemctl enable nginx`
```

After you update your web server configuration, go to [Step 4: Enable HTTPS traffic
and verify the certificate](#ssl-offload-enable-traffic-and-verify-certificate "#ssl-offload-enable-traffic-and-verify-certificate").

### Configure Apache web server

Use this section to configure Apache on supported platforms.

###### To update the web server configuration for Apache

1. Connect to your Amazon EC2 client instance.
2. Define default locations for certificates and private keys for your platform.

Amazon Linux
In the `/etc/httpd/conf.d/ssl.conf` file, ensure these values exist:

```
`SSLCertificateFile `/etc/pki/tls/certs/localhost.crt`
SSLCertificateKeyFile `/etc/pki/tls/private/localhost.key``
```

Amazon Linux 2
In the `/etc/httpd/conf.d/ssl.conf` file, ensure these values exist:

```
`SSLCertificateFile `/etc/pki/tls/certs/localhost.crt`
SSLCertificateKeyFile `/etc/pki/tls/private/localhost.key``
```

Amazon Linux 2023
Open `/etc/httpd/conf.d/ssl.conf` file. Add these values if they don't already exist:

```
`SSLCertificateFile `/etc/pki/tls/certs/localhost.crt`
SSLCertificateKeyFile `/etc/pki/tls/private/localhost.key``
```

CentOS 7
In the `/etc/httpd/conf.d/ssl.conf` file, ensure these values exist:

```
`SSLCertificateFile `/etc/pki/tls/certs/localhost.crt`
SSLCertificateKeyFile `/etc/pki/tls/private/localhost.key``
```

CentOS 8
In the `/etc/httpd/conf.d/ssl.conf` file, ensure these values exist:

```
`SSLCertificateFile `/etc/pki/tls/certs/localhost.crt`
SSLCertificateKeyFile `/etc/pki/tls/private/localhost.key``
```

Red Hat 7
In the `/etc/httpd/conf.d/ssl.conf` file, ensure these values exist:

```
`SSLCertificateFile `/etc/pki/tls/certs/localhost.crt`
SSLCertificateKeyFile `/etc/pki/tls/private/localhost.key``
```

Red Hat 8
In the `/etc/httpd/conf.d/ssl.conf` file, ensure these values exist:

```
`SSLCertificateFile `/etc/pki/tls/certs/localhost.crt`
SSLCertificateKeyFile `/etc/pki/tls/private/localhost.key``
```

Ubuntu 16.04 LTS
In the `/etc/apache2/sites-available/default-ssl.conf` file, ensure these values exist:

```
`SSLCertificateFile `/etc/ssl/certs/localhost.crt`
SSLCertificateKeyFile `/etc/ssl/private/localhost.key``
```

Ubuntu 18.04 LTS
In the `/etc/apache2/sites-available/default-ssl.conf` file, ensure these values exist:

```
`SSLCertificateFile `/etc/ssl/certs/localhost.crt`
SSLCertificateKeyFile `/etc/ssl/private/localhost.key``
```

Ubuntu 20.04 LTS
In the `/etc/apache2/sites-available/default-ssl.conf` file, ensure these values exist:

```
`SSLCertificateFile `/etc/ssl/certs/localhost.crt`
SSLCertificateKeyFile `/etc/ssl/private/localhost.key``
```

Ubuntu 22.04 LTS
In the `/etc/apache2/sites-available/default-ssl.conf` file, ensure these values exist:

```
`SSLCertificateFile `/etc/ssl/certs/localhost.crt`
SSLCertificateKeyFile `/etc/ssl/private/localhost.key``
```

Ubuntu 24.04 LTS
In the `/etc/apache2/sites-available/default-ssl.conf` file, ensure these values exist:

```
`SSLCertificateFile `/etc/ssl/certs/localhost.crt`
SSLCertificateKeyFile `/etc/ssl/private/localhost.key``
```

3. Copy your web server certificate to the required location for your platform.

Amazon Linux

```
`$` `sudo cp `<web_server.crt>` /etc/pki/tls/certs/localhost.crt`
```

Replace `<web_server.crt>` with the name of your web server certificate.

Amazon Linux 2

```
`$` `sudo cp `<web_server.crt>` /etc/pki/tls/certs/localhost.crt`
```

Replace `<web_server.crt>` with the name of your web server certificate.

Amazon Linux 2023

```
`$` `sudo cp `<web_server.crt>` /etc/pki/tls/certs/localhost.crt`
```

Replace `<web_server.crt>` with the name of your web server certificate.

CentOS 7

```
`$` `sudo cp `<web_server.crt>` /etc/pki/tls/certs/localhost.crt`
```

Replace `<web_server.crt>` with the name of your web server certificate.

CentOS 8

```
`$` `sudo cp `<web_server.crt>` /etc/pki/tls/certs/localhost.crt`
```

Replace `<web_server.crt>` with the name of your web server certificate.

Red Hat 7

```
`$` `sudo cp `<web_server.crt>` /etc/pki/tls/certs/localhost.crt`
```

Replace `<web_server.crt>` with the name of your web server certificate.

Red Hat 8

```
`$` `sudo cp `<web_server.crt>` /etc/pki/tls/certs/localhost.crt`
```

Replace `<web_server.crt>` with the name of your web server certificate.

Ubuntu 16.04 LTS

```
`$` `sudo cp `<web_server.crt>` /etc/ssl/certs/localhost.crt`
```

Replace `<web_server.crt>` with the name of your web server certificate.

Ubuntu 18.04 LTS

```
`$` `sudo cp `<web_server.crt>` /etc/ssl/certs/localhost.crt`
```

Replace `<web_server.crt>` with the name of your web server certificate.

Ubuntu 20.04 LTS

```
`$` `sudo cp `<web_server.crt>` /etc/ssl/certs/localhost.crt`
```

Replace `<web_server.crt>` with the name of your web server certificate.

Ubuntu 22.04 LTS

```
`$` `sudo cp `<web_server.crt>` /etc/ssl/certs/localhost.crt`
```

Replace `<web_server.crt>` with the name of your web server certificate.

Ubuntu 24.04 LTS

```
`$` `sudo cp `<web_server.crt>` /etc/ssl/certs/localhost.crt`
```

Replace `<web_server.crt>` with the name of your web server certificate. 4. Copy your fake PEM private key to the required location for your platform.

Amazon Linux

```
`$` `sudo cp `<web_server_example_pem.key>` /etc/pki/tls/private/localhost.key`
```

Replace `<web_server_example_pem.key>` with the name of the file that contains your fake PEM private key.

Amazon Linux 2

```
`$` `sudo cp `<web_server_example_pem.key>` /etc/pki/tls/private/localhost.key`
```

Replace `<web_server_example_pem.key>` with the name of the file that contains your fake PEM private key.

Amazon Linux 2023

```
`$` `sudo cp `<web_server_example_pem.key>` /etc/pki/tls/private/localhost.key`
```

Replace `<web_server_example_pem.key>` with the name of the file that contains your fake PEM private key.

CentOS 7

```
`$` `sudo cp `<web_server_example_pem.key>` /etc/pki/tls/private/localhost.key`
```

Replace `<web_server_example_pem.key>` with the name of the file that contains your fake PEM private key.

CentOS 8

```
`$` `sudo cp `<web_server_example_pem.key>` /etc/pki/tls/private/localhost.key`
```

Replace `<web_server_example_pem.key>` with the name of the file that contains your fake PEM private key.

Red Hat 7

```
`$` `sudo cp `<web_server_example_pem.key>` /etc/pki/tls/private/localhost.key`
```

Replace `<web_server_example_pem.key>` with the name of the file that contains your fake PEM private key.

Red Hat 8

```
`$` `sudo cp `<web_server_example_pem.key>` /etc/pki/tls/private/localhost.key`
```

Replace `<web_server_example_pem.key>` with the name of the file that contains your fake PEM private key.

Ubuntu 16.04 LTS

```
`$` `sudo cp `<web_server_example_pem.key>` /etc/ssl/private/localhost.key`
```

Replace `<web_server_example_pem.key>` with the name of the file that contains your fake PEM private key.

Ubuntu 18.04 LTS

```
`$` `sudo cp `<web_server_example_pem.key>` /etc/ssl/private/localhost.key`
```

Replace `<web_server_example_pem.key>` with the name of the file that contains your fake PEM private key.

Ubuntu 20.04 LTS

```
`$` `sudo cp `<web_server_example_pem.key>` /etc/ssl/private/localhost.key`
```

Replace `<web_server_example_pem.key>` with the name of the file that contains your fake PEM private key.

Ubuntu 22.04 LTS

```
`$` `sudo cp `<web_server_example_pem.key>` /etc/ssl/private/localhost.key`
```

Replace `<web_server_example_pem.key>` with the name of the file that contains your fake PEM private key.

Ubuntu 24.04 LTS

```
`$` `sudo cp `<web_server_example_pem.key>` /etc/ssl/private/localhost.key`
```

Replace `<web_server_example_pem.key>` with the name of the file that contains your fake PEM private key. 5. Change ownership of these files if required by your platform.

Amazon Linux

```
`$` `sudo chown apache /etc/pki/tls/certs/localhost.crt /etc/pki/tls/private/localhost.key`
```

Provides read permission to the user named _apache_.

Amazon Linux 2

```
`$` `sudo chown apache /etc/pki/tls/certs/localhost.crt /etc/pki/tls/private/localhost.key`
```

Provides read permission to the user named _apache_.

Amazon Linux 2023

```
`$` `sudo chown apache /etc/pki/tls/certs/localhost.crt /etc/pki/tls/private/localhost.key`
```

Provides read permission to the user named _apache_.

CentOS 7

```
`$` `sudo chown apache /etc/pki/tls/certs/localhost.crt /etc/pki/tls/private/localhost.key`
```

Provides read permission to the user named _apache_.

CentOS 8

```
`$` `sudo chown apache /etc/pki/tls/certs/localhost.crt /etc/pki/tls/private/localhost.key`
```

Provides read permission to the user named _apache_.

Red Hat 7

```
`$` `sudo chown apache /etc/pki/tls/certs/localhost.crt /etc/pki/tls/private/localhost.key`
```

Provides read permission to the user named _apache_.

Red Hat 8

```
`$` `sudo chown apache /etc/pki/tls/certs/localhost.crt /etc/pki/tls/private/localhost.key`
```

Provides read permission to the user named _apache_.

Ubuntu 16.04 LTS
No action required.

Ubuntu 18.04 LTS
No action required.

Ubuntu 20.04 LTS
No action required.

Ubuntu 22.04 LTS
No action required.

Ubuntu 24.04 LTS
No action required. 6. Configure Apache directives for your platform.

Amazon Linux
Locate the SSL file for this platform:

```
`/etc/httpd/conf.d/ssl.conf`
```

This file contains Apache directives which define how your server should run.
Directives appear on the left, followed by a value. Use a text editor to edit this file. This requires Linux root permissions.

Update or enter the following directives with these values:

```
SSLCryptoDevice `cloudhsm`
SSLCipherSuite `ECDHE-RSA-AES128-GCM-SHA256:ECDHE-RSA-AES256-GCM-SHA384:DHE-RSA-AES128-GCM-SHA256:DHE-RSA-AES256-GCM-SHA384:ECDHE-RSA-AES256-SHA384:ECDHE-RSA-AES128-SHA256:ECDHE-RSA-AES256-SHA384:DHE-RSA-AES128-SHA:DHE-RSA-AES256-SHA:DHE-RSA-AES128-SHA256:DHE-RSA-AES256-SHA256:ECDHE-ECDSA-AES256-GCM-SHA384:ECDHE-ECDSA-AES256-SHA384:ECDHE-ECDSA-AES128-GCM-SHA256:ECDHE-ECDSA-AES128-SHA256:ECDHE-ECDSA-AES256-SHA:ECDHE-ECDSA-AES128-SHA`
```

Save the file.

Amazon Linux 2
Locate the SSL file for this platform:

```
`/etc/httpd/conf.d/ssl.conf`
```

This file contains Apache directives which define how your server should run.
Directives appear on the left, followed by a value. Use a text editor to edit this file. This requires Linux root permissions.

Update or enter the following directives with these values:

```
SSLCryptoDevice `cloudhsm`
SSLCipherSuite `ECDHE-RSA-AES128-GCM-SHA256:ECDHE-RSA-AES256-GCM-SHA384:DHE-RSA-AES128-GCM-SHA256:DHE-RSA-AES256-GCM-SHA384:ECDHE-RSA-AES256-SHA384:ECDHE-RSA-AES128-SHA256:ECDHE-RSA-AES256-SHA384:DHE-RSA-AES128-SHA:DHE-RSA-AES256-SHA:DHE-RSA-AES128-SHA256:DHE-RSA-AES256-SHA256:ECDHE-ECDSA-AES256-GCM-SHA384:ECDHE-ECDSA-AES256-SHA384:ECDHE-ECDSA-AES128-GCM-SHA256:ECDHE-ECDSA-AES128-SHA256:ECDHE-ECDSA-AES256-SHA:ECDHE-ECDSA-AES128-SHA`
```

Save the file.

Amazon Linux 2023
Locate the SSL file for this platform:

```
`/etc/httpd/conf.d/ssl.conf`
```

The Apache configuration file defines server behavior. Edit this file with root permissions.

Update or add the following directives:

```
SSLCryptoDevice `cloudhsm`
SSLCipherSuite `ECDHE-RSA-AES128-GCM-SHA256:ECDHE-RSA-AES256-GCM-SHA384:DHE-RSA-AES128-GCM-SHA256:DHE-RSA-AES256-GCM-SHA384:ECDHE-RSA-AES256-SHA384:ECDHE-RSA-AES128-SHA256:ECDHE-RSA-AES256-SHA384:DHE-RSA-AES128-SHA:DHE-RSA-AES256-SHA:DHE-RSA-AES128-SHA256:DHE-RSA-AES256-SHA256:ECDHE-ECDSA-AES256-GCM-SHA384:ECDHE-ECDSA-AES256-SHA384:ECDHE-ECDSA-AES128-GCM-SHA256:ECDHE-ECDSA-AES128-SHA256:ECDHE-ECDSA-AES256-SHA:ECDHE-ECDSA-AES128-SHA`
```

Save the file.

CentOS 7
Locate the SSL file for this platform:

```
`/etc/httpd/conf.d/ssl.conf`
```

This file contains Apache directives which define how your server should run.
Directives appear on the left, followed by a value. Use a text editor to edit this file. This requires Linux root permissions.

Update or enter the following directives with these values:

```
SSLCryptoDevice `cloudhsm`
SSLCipherSuite `ECDHE-RSA-AES128-GCM-SHA256:ECDHE-RSA-AES256-GCM-SHA384:DHE-RSA-AES128-GCM-SHA256:DHE-RSA-AES256-GCM-SHA384:ECDHE-RSA-AES256-SHA384:ECDHE-RSA-AES128-SHA256:ECDHE-RSA-AES256-SHA384:DHE-RSA-AES128-SHA:DHE-RSA-AES256-SHA:DHE-RSA-AES128-SHA256:DHE-RSA-AES256-SHA256:ECDHE-ECDSA-AES256-GCM-SHA384:ECDHE-ECDSA-AES256-SHA384:ECDHE-ECDSA-AES128-GCM-SHA256:ECDHE-ECDSA-AES128-SHA256:ECDHE-ECDSA-AES256-SHA:ECDHE-ECDSA-AES128-SHA`
```

Save the file.

CentOS 8
Locate the SSL file for this platform:

```
`/etc/httpd/conf.d/ssl.conf`
```

This file contains Apache directives which define how your server should run.
Directives appear on the left, followed by a value. Use a text editor to edit this file. This requires Linux root permissions.

Update or enter the following directives with these values:

```
`SSLCryptoDevice `cloudhsm`SSLProtocol `TLSv1.2 TLSv1.3`
SSLCipherSuite `ECDHE-RSA-AES128-GCM-SHA256:ECDHE-RSA-AES256-GCM-SHA384:DHE-RSA-AES128-GCM-SHA256:DHE-RSA-AES256-GCM-SHA384:ECDHE-RSA-AES256-SHA384:ECDHE-RSA-AES128-SHA256:ECDHE-RSA-AES256-SHA384:DHE-RSA-AES128-SHA:DHE-RSA-AES256-SHA:DHE-RSA-AES128-SHA256:DHE-RSA-AES256-SHA256:ECDHE-ECDSA-AES256-GCM-SHA384:ECDHE-ECDSA-AES256-SHA384:ECDHE-ECDSA-AES128-GCM-SHA256:ECDHE-ECDSA-AES128-SHA256:ECDHE-ECDSA-AES256-SHA:ECDHE-ECDSA-AES128-SHA`
SSLProxyCipherSuite `HIGH:!aNULL``
```

Save the file.

Red Hat 7
Locate the SSL file for this platform:

```
`/etc/httpd/conf.d/ssl.conf`
```

This file contains Apache directives which define how your server should run.
Directives appear on the left, followed by a value. Use a text editor to edit this file. This requires Linux root permissions.

Update or enter the following directives with these values:

```
SSLCryptoDevice `cloudhsm`
SSLCipherSuite `ECDHE-RSA-AES128-GCM-SHA256:ECDHE-RSA-AES256-GCM-SHA384:DHE-RSA-AES128-GCM-SHA256:DHE-RSA-AES256-GCM-SHA384:ECDHE-RSA-AES256-SHA384:ECDHE-RSA-AES128-SHA256:ECDHE-RSA-AES256-SHA384:DHE-RSA-AES128-SHA:DHE-RSA-AES256-SHA:DHE-RSA-AES128-SHA256:DHE-RSA-AES256-SHA256:ECDHE-ECDSA-AES256-GCM-SHA384:ECDHE-ECDSA-AES256-SHA384:ECDHE-ECDSA-AES128-GCM-SHA256:ECDHE-ECDSA-AES128-SHA256:ECDHE-ECDSA-AES256-SHA:ECDHE-ECDSA-AES128-SHA`
```

Save the file.

Red Hat 8
Locate the SSL file for this platform:

```
`/etc/httpd/conf.d/ssl.conf`
```

This file contains Apache directives which define how your server should run.
Directives appear on the left, followed by a value. Use a text editor to edit this file. This requires Linux root permissions.

Update or enter the following directives with these values:

```
`SSLCryptoDevice `cloudhsm`SSLProtocol `TLSv1.2 TLSv1.3`
SSLCipherSuite `ECDHE-RSA-AES128-GCM-SHA256:ECDHE-RSA-AES256-GCM-SHA384:DHE-RSA-AES128-GCM-SHA256:DHE-RSA-AES256-GCM-SHA384:ECDHE-RSA-AES256-SHA384:ECDHE-RSA-AES128-SHA256:ECDHE-RSA-AES256-SHA384:DHE-RSA-AES128-SHA:DHE-RSA-AES256-SHA:DHE-RSA-AES128-SHA256:DHE-RSA-AES256-SHA256:ECDHE-ECDSA-AES256-GCM-SHA384:ECDHE-ECDSA-AES256-SHA384:ECDHE-ECDSA-AES128-GCM-SHA256:ECDHE-ECDSA-AES128-SHA256:ECDHE-ECDSA-AES256-SHA:ECDHE-ECDSA-AES128-SHA`
SSLProxyCipherSuite `HIGH:!aNULL``
```

Save the file.

Ubuntu 16.04 LTS
Locate the SSL file for this platform:

```
`/etc/apache2/mods-available/ssl.conf`
```

This file contains Apache directives which define how your server should run.
Directives appear on the left, followed by a value. Use a text editor to edit this file. This requires Linux root permissions.

Update or enter the following directives with these values:

```
SSLCryptoDevice `cloudhsm`
SSLCipherSuite `ECDHE-RSA-AES128-GCM-SHA256:ECDHE-RSA-AES256-GCM-SHA384:DHE-RSA-AES128-GCM-SHA256:DHE-RSA-AES256-GCM-SHA384:ECDHE-RSA-AES256-SHA384:ECDHE-RSA-AES128-SHA256:ECDHE-RSA-AES256-SHA384:DHE-RSA-AES128-SHA:DHE-RSA-AES256-SHA:DHE-RSA-AES128-SHA256:DHE-RSA-AES256-SHA256:ECDHE-ECDSA-AES256-GCM-SHA384:ECDHE-ECDSA-AES256-SHA384:ECDHE-ECDSA-AES128-GCM-SHA256:ECDHE-ECDSA-AES128-SHA256:ECDHE-ECDSA-AES256-SHA:ECDHE-ECDSA-AES128-SHA`
```

Save the file.

Enable the SSL module and default SSL site configuration:

```
`$` `sudo a2enmod ssl`
`$` `sudo a2ensite default-ssl`
```

Ubuntu 18.04 LTS
Locate the SSL file for this platform:

```
`/etc/apache2/mods-available/ssl.conf`
```

This file contains Apache directives which define how your server should run.
Directives appear on the left, followed by a value. Use a text editor to edit this file. This requires Linux root permissions.

Update or enter the following directives with these values:

```
SSLCryptoDevice `cloudhsm`
SSLCipherSuite `ECDHE-RSA-AES128-GCM-SHA256:ECDHE-RSA-AES256-GCM-SHA384:DHE-RSA-AES128-GCM-SHA256:DHE-RSA-AES256-GCM-SHA384:ECDHE-RSA-AES256-SHA384:ECDHE-RSA-AES128-SHA256:ECDHE-RSA-AES256-SHA384:DHE-RSA-AES128-SHA:DHE-RSA-AES256-SHA:DHE-RSA-AES128-SHA256:DHE-RSA-AES256-SHA256:ECDHE-ECDSA-AES256-GCM-SHA384:ECDHE-ECDSA-AES256-SHA384:ECDHE-ECDSA-AES128-GCM-SHA256:ECDHE-ECDSA-AES128-SHA256:ECDHE-ECDSA-AES256-SHA:ECDHE-ECDSA-AES128-SHA`
SSLProtocol `TLSv1.2 TLSv1.3`
```

Save the file.

Enable the SSL module and default SSL site configuration:

```
`$` `sudo a2enmod ssl`
`$` `sudo a2ensite default-ssl`
```

Ubuntu 20.04 LTS
Locate the SSL file for this platform:

```
`/etc/apache2/mods-available/ssl.conf`
```

This file contains Apache directives which define how your server should run.
Directives appear on the left, followed by a value. Use a text editor to edit this file. This requires Linux root permissions.

Update or enter the following directives with these values:

```
SSLCryptoDevice `cloudhsm`
SSLCipherSuite `ECDHE-RSA-AES128-GCM-SHA256:ECDHE-RSA-AES256-GCM-SHA384:DHE-RSA-AES128-GCM-SHA256:DHE-RSA-AES256-GCM-SHA384:ECDHE-RSA-AES256-SHA384:ECDHE-RSA-AES128-SHA256:ECDHE-RSA-AES256-SHA384:DHE-RSA-AES128-SHA:DHE-RSA-AES256-SHA:DHE-RSA-AES128-SHA256:DHE-RSA-AES256-SHA256:ECDHE-ECDSA-AES256-GCM-SHA384:ECDHE-ECDSA-AES256-SHA384:ECDHE-ECDSA-AES128-GCM-SHA256:ECDHE-ECDSA-AES128-SHA256:ECDHE-ECDSA-AES256-SHA:ECDHE-ECDSA-AES128-SHA`
SSLProtocol `TLSv1.2 TLSv1.3`
```

Save the file.

Enable the SSL module and default SSL site configuration:

```
`$` `sudo a2enmod ssl`
`$` `sudo a2ensite default-ssl`
```

Ubuntu 22.04 LTS
Locate the SSL file for this platform:

```
`/etc/apache2/mods-available/ssl.conf`
```

This file contains Apache directives which define how your server should run.
Directives appear on the left, followed by a value. Use a text editor to edit this file. This requires Linux root permissions.

Update or enter the following directives with these values:

```
SSLCryptoDevice `cloudhsm`
SSLCipherSuite `ECDHE-RSA-AES128-GCM-SHA256:ECDHE-RSA-AES256-GCM-SHA384:DHE-RSA-AES128-GCM-SHA256:DHE-RSA-AES256-GCM-SHA384:ECDHE-RSA-AES256-SHA384:ECDHE-RSA-AES128-SHA256:ECDHE-RSA-AES256-SHA384:DHE-RSA-AES128-SHA:DHE-RSA-AES256-SHA:DHE-RSA-AES128-SHA256:DHE-RSA-AES256-SHA256:ECDHE-ECDSA-AES256-GCM-SHA384:ECDHE-ECDSA-AES256-SHA384:ECDHE-ECDSA-AES128-GCM-SHA256:ECDHE-ECDSA-AES128-SHA256:ECDHE-ECDSA-AES256-SHA:ECDHE-ECDSA-AES128-SHA`
SSLProtocol `TLSv1.2 TLSv1.3`
```

Save the file.

Enable the SSL module and default SSL site configuration:

```
`$` `sudo a2enmod ssl`
`$` `sudo a2ensite default-ssl`
```

Ubuntu 24.04 LTS
Locate the SSL file for this platform:

```
`/etc/apache2/mods-available/ssl.conf`
```

This file contains Apache directives which define how your server should run.
Directives appear on the left, followed by a value. Use a text editor to edit this file. This requires Linux root permissions.

Update or enter the following directives with these values:

```
SSLCryptoDevice `cloudhsm`
SSLCipherSuite `ECDHE-RSA-AES128-GCM-SHA256:ECDHE-RSA-AES256-GCM-SHA384:DHE-RSA-AES128-GCM-SHA256:DHE-RSA-AES256-GCM-SHA384:ECDHE-RSA-AES256-SHA384:ECDHE-RSA-AES128-SHA256:ECDHE-RSA-AES256-SHA384:DHE-RSA-AES128-SHA:DHE-RSA-AES256-SHA:DHE-RSA-AES128-SHA256:DHE-RSA-AES256-SHA256:ECDHE-ECDSA-AES256-GCM-SHA384:ECDHE-ECDSA-AES256-SHA384:ECDHE-ECDSA-AES128-GCM-SHA256:ECDHE-ECDSA-AES128-SHA256:ECDHE-ECDSA-AES256-SHA:ECDHE-ECDSA-AES128-SHA`
SSLProtocol `TLSv1.2 TLSv1.3`
```

Save the file.

Enable the SSL module and default SSL site configuration:

```
`$` `sudo a2enmod ssl`
`$` `sudo a2ensite default-ssl`
```

7. Configure an environment-values file for your platform.

Amazon Linux
No action required. Environment values go in `/etc/sysconfig/httpd`

Amazon Linux 2

Open the httpd service file:

```
`/lib/systemd/system/httpd.service`
```

Under the `[Service]` section, add the following:

```
`EnvironmentFile=/etc/sysconfig/httpd`
```

Amazon Linux 2023
Open `/lib/systemd/system/httpd.service`

Under the [Service] section, add:

```
`EnvironmentFile=/etc/sysconfig/httpd`
```

CentOS 7

Open the httpd service file:

```
`/lib/systemd/system/httpd.service`
```

Under the `[Service]` section, add the following:

```
`EnvironmentFile=/etc/sysconfig/httpd`
```

CentOS 8

Open the httpd service file:

```
`/lib/systemd/system/httpd.service`
```

Under the `[Service]` section, add the following:

```
`EnvironmentFile=/etc/sysconfig/httpd`
```

Red Hat 7

Open the httpd service file:

```
`/lib/systemd/system/httpd.service`
```

Under the `[Service]` section, add the following:

```
`EnvironmentFile=/etc/sysconfig/httpd`
```

Red Hat 8

Open the httpd service file:

```
`/lib/systemd/system/httpd.service`
```

Under the `[Service]` section, add the following:

```
`EnvironmentFile=/etc/sysconfig/httpd`
```

Ubuntu 16.04 LTS
No action required. Environment values go in `/etc/sysconfig/httpd`

Ubuntu 18.04 LTS
No action required. Environment values go in `/etc/sysconfig/httpd`

Ubuntu 20.04 LTS
No action required. Environment values go in `/etc/sysconfig/httpd`

Ubuntu 22.04 LTS
No action required. Environment values go in `/etc/sysconfig/httpd`

Ubuntu 24.04 LTS
No action required. Environment values go in `/etc/sysconfig/httpd` 8. In the file that stores environment variables for your platform, set an environment
variable that contains the credentials of the cryptographic user (CU):

Amazon Linux
Use a text editor to edit the `/etc/sysconfig/httpd`.

```
ssl_engine cloudhsm;
env CLOUDHSM_PIN;
```

Replace `<CU user name>` and
`<password>` with the CU credentials.

Amazon Linux 2
Use a text editor to edit the `/etc/sysconfig/httpd`.

```
ssl_engine cloudhsm;
env CLOUDHSM_PIN;
```

Replace `<CU user name>` and
`<password>` with the CU credentials.

Amazon Linux 2023
Open `/etc/sysconfig/httpd`, add:

```
`CLOUDHSM_PIN=`<CU user name>`:`<password>``
```

Replace `<CU user name>` and
`<password>` with the CU credentials.

CentOS 7
Use a text editor to edit the `/etc/sysconfig/httpd`.

```
ssl_engine cloudhsm;
env CLOUDHSM_PIN;
```

Replace `<CU user name>` and
`<password>` with the CU credentials.

CentOS 8
Use a text editor to edit the `/etc/sysconfig/httpd`.

```
`CLOUDHSM_PIN=`<CU user name>`:`<password>``
```

Replace `<CU user name>` and
`<password>` with the CU credentials.

Red Hat 7
Use a text editor to edit the `/etc/sysconfig/httpd`.

```
ssl_engine cloudhsm;
env CLOUDHSM_PIN;
```

Replace `<CU user name>` and
`<password>` with the CU credentials.

Red Hat 8
Use a text editor to edit the `/etc/sysconfig/httpd`.

```
`CLOUDHSM_PIN=`<CU user name>`:`<password>``
```

Replace `<CU user name>` and
`<password>` with the CU credentials.

###### Note

Client SDK 5 introduces the `CLOUDHSM_PIN` environment variable for
storing the credentials of the CU.

Ubuntu 16.04 LTS
Use a text editor to edit the `/etc/apache2/envvars`.

```
`export n3fips_password=`<CU user name>`:`<password>``
```

Replace `<CU user name>` and
`<password>` with the CU credentials.

Ubuntu 18.04 LTS
Use a text editor to edit the `/etc/apache2/envvars`.

```
`export CLOUDHSM_PIN=`<CU user name>`:`<password>``
```

Replace `<CU user name>` and
`<password>` with the CU credentials.

###### Note

Client SDK 5 introduces the `CLOUDHSM_PIN` environment variable for
storing the credentials of the CU. In Client SDK 3 you stored the CU credentials in the
`n3fips_password` environment variable. Client SDK 5 supports both
environment variables, but we recommend using `CLOUDHSM_PIN`.

Ubuntu 20.04 LTS
Use a text editor to edit the `/etc/apache2/envvars`.

```
`export CLOUDHSM_PIN=`<CU user name>`:`<password>``
```

Replace `<CU user name>` and
`<password>` with the CU credentials.

###### Note

Client SDK 5 introduces the `CLOUDHSM_PIN` environment variable for
storing the credentials of the CU. In Client SDK 3 you stored the CU credentials in the
`n3fips_password` environment variable. Client SDK 5 supports both
environment variables, but we recommend using `CLOUDHSM_PIN`.

Ubuntu 22.04 LTS
Use a text editor to edit the `/etc/apache2/envvars`.

```
`export CLOUDHSM_PIN=`<CU user name>`:`<password>``
```

Replace `<CU user name>` and
`<password>` with the CU credentials.

###### Note

Client SDK 5 introduces the `CLOUDHSM_PIN` environment variable for
storing the credentials of the CU. In Client SDK 3 you stored the CU credentials in the
`n3fips_password` environment variable. Client SDK 5 supports both
environment variables, but we recommend using `CLOUDHSM_PIN`.

Ubuntu 24.04 LTS
Use a text editor to edit the `/etc/apache2/envvars`.

```
`export CLOUDHSM_PIN=`<CU user name>`:`<password>``
```

Replace `<CU user name>` and
`<password>` with the CU credentials.

###### Note

Client SDK 5 introduces the `CLOUDHSM_PIN` environment variable for
storing the credentials of the CU. In Client SDK 3 you stored the CU credentials in the
`n3fips_password` environment variable. Client SDK 5 supports both
environment variables, but we recommend using `CLOUDHSM_PIN`. 9. Start the Apache web server.

Amazon Linux

```
`$` `sudo systemctl daemon-reload`
`$` `sudo service httpd start`
```

Amazon Linux 2

```
`$` `sudo systemctl daemon-reload`
`$` `sudo service httpd start`
```

Amazon Linux 2023

```
`$` `sudo systemctl daemon-reload`
`$` `sudo service httpd start`
```

CentOS 7

```
`$` `sudo systemctl daemon-reload`
`$` `sudo service httpd start`
```

CentOS 8

```
`$` `sudo systemctl daemon-reload`
`$` `sudo service httpd start`
```

Red Hat 7

```
`$` `sudo systemctl daemon-reload`
`$` `sudo service httpd start`
```

Red Hat 8

```
`$` `sudo systemctl daemon-reload`
`$` `sudo service httpd start`
```

Ubuntu 16.04 LTS

```
`$` `sudo service apache2 start`
```

Ubuntu 18.04 LTS

```
`$` `sudo service apache2 start`
```

Ubuntu 20.04 LTS

```
`$` `sudo service apache2 start`
```

Ubuntu 22.04 LTS

```
`$` `sudo service apache2 start`
```

Ubuntu 24.04 LTS

```
`$` `sudo service apache2 start`
```

10. (Optional) Configure your platform to start Apache at start-up.

Amazon Linux

```
`$` `sudo chkconfig httpd on`
```

Amazon Linux 2

```
`$` `sudo chkconfig httpd on`
```

Amazon Linux 2023

```
`$` `sudo chkconfig httpd on`
```

CentOS 7

```
`$` `sudo chkconfig httpd on`
```

CentOS 8

```
`$` `systemctl enable httpd`
```

Red Hat 7

```
`$` `sudo chkconfig httpd on`
```

Red Hat 8

```
`$` `systemctl enable httpd`
```

Ubuntu 16.04 LTS

```
`$` `sudo systemctl enable apache2`
```

Ubuntu 18.04 LTS

```
`$` `sudo systemctl enable apache2`
```

Ubuntu 20.04 LTS

```
`$` `sudo systemctl enable apache2`
```

Ubuntu 22.04 LTS

```
`$` `sudo systemctl enable apache2`
```

Ubuntu 24.04 LTS

```
`$` `sudo systemctl enable apache2`
```

After you update your web server configuration, go to [Step 4: Enable HTTPS traffic
and verify the certificate](#ssl-offload-enable-traffic-and-verify-certificate "#ssl-offload-enable-traffic-and-verify-certificate").

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
  certificate that you configured](#ssl-offload-verify-https-connection-linux-enable "#ssl-offload-verify-https-connection-linux-enable")

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
