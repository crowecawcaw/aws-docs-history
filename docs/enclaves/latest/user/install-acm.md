# Install ACM for Nitro Enclaves

Use the following procedure to install and configure ACM for Nitro Enclaves.

###### Steps

- [Step 1: Create the ACM certificate](#create-cert "#create-cert")
- [Step 2: Prepare the enclaves-enabled parent
  instance](#prepare-instance "#prepare-instance")
- [Step 3: Prepare the IAM role](#create-role "#create-role")
- [Step 4: Associate the role with the ACM
  certificate](#role-cert "#role-cert")
- [Step 5: Grant the role permission to access the
  certificate and encryption key](#add-policy "#add-policy")
- [Step 6: Attach the role to the instance](#instance-role "#instance-role")
- [Step 7: Configure the web server to use ACM
  for Nitro Enclaves](#config-web-server "#config-web-server")
- [Using multiple certificates](#multi-certs "#multi-certs")

###### Prerequisites

The user performing this configuration must have permission to use the
`ec2:AssociateEnclaveCertificateIamRole`,
`ec2:GetAssociatedEnclaveCertificateIamRoles`, and
`ec2:DisassociateEnclaveCertificateIamRole` actions. To grant the
user the required permissions, use the following IAM policy.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Action": [
 "ec2:AssociateEnclaveCertificateIamRole",
 "ec2:GetAssociatedEnclaveCertificateIamRoles",
 "ec2:DisassociateEnclaveCertificateIamRole"
 ],
 "Resource": [
 "arn:aws:acm:`us-east-1`:`111122223333`:certificate/*",
 "arn:aws:iam::`111122223333`:role/*"
 ],
 "Effect": "Allow"
 }
 ]
}`

```

## Step 1: Create the ACM certificate

Create the AWS Certificate Manager (ACM) certificate that you want use with your NGINX or
Apache HTTP server. ACM for Nitro Enclaves supports both private and public
certificates. For more information about creating a certificate, see the following
resources in the _AWS Certificate Manager User Guide_.

- [Requesting a
  Public Certificate](../../../acm/latest/userguide/gs-acm-request-public.md "../../../acm/latest/userguide/gs-acm-request-public.md")
- [Requesting a
  Private Certificate](../../../acm/latest/userguide/gs-acm-request-private.md "../../../acm/latest/userguide/gs-acm-request-private.md")

When you use DNS validation to request an ACM certificate, ACM provides a
CNAME record that you must then add to your DNS configuration. ACM uses the CNAME
record to validate ownership of domains.

## Step 2: Prepare the enclaves-enabled parent

instance

[Launch the enclave enabled instance](create-enclave.md#launch-parent "create-enclave.md#launch-parent") that you
will use as the parent instance. You can use either the ACM for Nitro Enclaves AMI
from AWS Marketplace, or you can install ACM for Nitro Enclaves and the web server
using RPM packages.

###### Tip

After you launch the instance, make a note of the instance ID, as you'll need
it later.

Option 1: Using ACM for Nitro Enclaves AMI

###### To launch an instance using the ACM for Nitro Enclaves AMI from

AWS Marketplace

1. Open the [ACM for
   Nitro Enclaves](https://aws.amazon.com/marketplace/pp/B08S7NZFNF "https://aws.amazon.com/marketplace/pp/B08S7NZFNF") page in the AWS Marketplace.
2. Find the ACM for Nitro Enclaves AMI for your Region, and note
   the AMI ID. You need the AMI ID for the next step.
3. Launch the instance using the AMI from the AWS Marketplace and enable it
   for Nitro Enclaves using the following command.

```
`$` aws ec2 run-instances --image-id `ami_id` --count 1 --instance-type `supported_instance_type` --key-name `your_key_pair` --enclave-options 'Enabled=true'
```

Option 2: Using RPM packages

###### To install ACM for Nitro Enclaves from the Amazon Linux Extras

repository

1. Connect to the instance.
2. Enable the `aws-nitro-enclaves-cli` topic in the
   Amazon Linux Extras library.

```
`$` sudo amazon-linux-extras enable aws-nitro-enclaves-cli
```

3. Install your preferred web server. Do one of the
   following:
   - **NGINX**

   Enable the `nginx1` topic in the Amazon Linux
   Extras library and install NGINX from the Amazon Linux Extras
   library.

   ```
   `$` sudo amazon-linux-extras enable nginx1
   ```

   ```
   `$` sudo amazon-linux-extras install nginx1 -y
   ```

   - **Apache**

   Install and configure the Apache HTTP server with
   SSL/TLS support.

   ```
   `$` sudo yum -y install httpd mod_ssl
   ```

4. Install ACM for Nitro Enclaves from the Amazon Linux Extras
   library.

```
`$` sudo yum install aws-nitro-enclaves-acm -y
```

## Step 3: Prepare the IAM role

To grant the instance permission to use the ACM certificate, you must create an
IAM role with the required permissions. The IAM role is later attached to the
instance and the ACM certificate.

Create a JSON file named `acm-role` and add the following
policy statement.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement":[
 {
 "Effect":"Allow",
 "Principal":{
 "Service":"ec2.amazonaws.com"
 },
 "Action":"sts:AssumeRole"
 }
 ]
}`

```

Use the [create-role](../../../cli/latest/reference/iam/create-role.md "../../../cli/latest/reference/iam/create-role.md") command to
create a role named `acm-role`, and specify the path to the JSON
policy file.

```
`$` aws iam create-role --role-name acm-role --assume-role-policy-document file://acm-role.json
```

After you have created the role, make a note of the role ARN, as you'll need it in
the next step.

## Step 4: Associate the role with the ACM

certificate

Attach the IAM role that you created in the previous step to the ACM
certificate. To do this, use the [associate-enclave-certificate-iam-role](../../../cli/latest/reference/ec2/associate-enclave-certificate-iam-role.md "../../../cli/latest/reference/ec2/associate-enclave-certificate-iam-role.md") command, and specify the ARN of
the role to attach, and the ARN of the certificate to attach it to.

```
`$` aws ec2 --region `region` associate-enclave-certificate-iam-role --certificate-arn `certificate_ARN` --role-arn `role_ARN`
```

For example

```
`$` aws ec2 --region us-east-1 associate-enclave-certificate-iam-role --certificate-arn arn:aws:acm:us-east-1:123456789012:certificate/d4c3b2a1-e5d0-4d51-95d9-1927fEXAMPLE --role-arn arn:aws:iam::123456789012:role/acm-role
```

Example output

```
{

"CertificateS3BucketName": "aws-ec2-enclave-certificate-us-east-1-prod",
"CertificateS3ObjectKey": "arn:aws:iam::123456789012:role/acm-role/arn:aws:acm:us-east-1:123456789012:certificate/d4c3b2a1-e5d0-4d51-95d9-1927fEXAMPLE",
"EncryptionKmsKeyId": "a1b2c3d4-354d-4e51-9190-b12ebEXAMPLE"
}
```

After running the command, make a note of `CertificateS3BucketName` and
`EncryptionKmsKeyId`, as you'll need them for the next step.

## Step 5: Grant the role permission to access the

certificate and encryption key

You must now grant the IAM role (`acm-role`) permission to do
the following:

- Retrieve the ACM certificate from the Amazon S3 bucket returned in the
  previous step
- Perform `kms:Decrypt` using the AWS KMS key returned in the
  previous step
- Retrieve information about itself, including its path, GUID, and
  ARN.

Create a JSON file named `acm-role-policies.json`, add the following
policy statement, and specify the values of `CertificateS3BucketName` and
`EncryptionKmsKeyId` from the previous step.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Action": [
 "s3:GetObject"
 ],
 "Resource": [
 "arn:aws:s3:::`CertificateS3BucketName`/*"
 ]
 },
 {
 "Sid": "VisualEditor0",
 "Effect": "Allow",
 "Action": [
 "kms:Decrypt"
 ],
 "Resource": "arn:aws:kms:`us-east-1`:*:key/`EncryptionKmsKeyId`"
 },
 {
 "Effect": "Allow",
 "Action": "iam:GetRole",
 "Resource": "`arn:aws:iam::123456789012:role/acm-role`"
 }
 ]
}`

```

Use the [put-role-policy](../../../cli/latest/reference/iam/put-role-policy.md "../../../cli/latest/reference/iam/put-role-policy.md")
command to add the additional policies to the `acm-role` role,
and specify the path to the JSON policy file.

```
`$` aws iam put-role-policy --role-name acm-role --policy-name acm-role-policy --policy-document file://acm-role-policies.json
```

## Step 6: Attach the role to the instance

You must attach the IAM role to the instance to give it permission to use the
certificate.

Create a new instance profile named `acm-instance-profile`
using the [create-instance-profile](../../../cli/latest/reference/iam/create-instance-profile.md "../../../cli/latest/reference/iam/create-instance-profile.md") command.

```
`$` aws iam create-instance-profile --instance-profile-name acm-instance-profile
```

Example output

```
{
    "InstanceProfile": {
    "Path": "/",
     "InstanceProfileName": "acm-instance-profile",
    "InstanceProfileId": "ABCDUS6G56GWDIEXAMPLE",
    "Arn": "arn:aws:iam::123456789012:instance-profile/acm-instance-profile",
    "CreateDate": "2020-10-14T03:38:08+00:00",
"Roles": []
}
}
```

Add the `acm-role` that you created earlier to the
`acm-instance-profile` that you just created. Use the [add-role-to-instance-profile](../../../cli/latest/reference/iam/add-role-to-instance-profile.md "../../../cli/latest/reference/iam/add-role-to-instance-profile.md") command.

```
`$` aws iam add-role-to-instance-profile --instance-profile-name acm-instance-profile --role-name acm-role
```

Associate the instance profile with the instance that you launched previously. Use
the [associate-iam-instance-profile](../../../cli/latest/reference/iam/associate-iam-instance-profile.md "../../../cli/latest/reference/iam/associate-iam-instance-profile.md") command and specify the instance profile
to attach and the instance to attach it to.

```
`$` aws ec2 --region `region` associate-iam-instance-profile --instance-id `instance_id` --iam-instance-profile Name=acm-instance-profile
```

Example output

```
{
    "IamInstanceProfileAssociation":
    {
        "AssociationId": "iip-assoc-0a411083b4EXAMPLE",
        "InstanceId": "i-1234567890abcdef0",
        "IamInstanceProfile":
        {
            "Arn": "arn:aws:iam::123456789012:instance-profile/acm-instance-profile",
            "Id": "ABCDUS6G56GWDIEXAMPLE"
        },
        "State": "associating"
    }
}
```

## Step 7: Configure the web server to use ACM

for Nitro Enclaves

Configure the NGINX or Apache HTTP web server to use the ACM certificate. Choose
the correct procedure depending on the web server you're using.

NGINX

###### To configure NGINX

1. SSH into the instance that you launched previously.
2. Nitro Enclaves ships with a sample ACM for Nitro Enclaves
   configuration file that you can use as a starting point for your
   own configuration. To use the sample configuration file, rename
   the configuration file from
   `/etc/nitro_enclaves/acm.example.yaml` to
   `/etc/nitro_enclaves/acm.yaml`.

```
`$` sudo mv /etc/nitro_enclaves/acm.example.yaml /etc/nitro_enclaves/acm.yaml
```

3. Specify the ARN of the certificate that you associated with
   the IAM role that is attached to the parent instance. Using
   your preferred text editor, open
   `/etc/nitro_enclaves/acm.yaml`. In the
   `Acm` section, for `certificate_arn`,
   specify the ARN of the certificate. Save and close the
   file.
4. Open the `/etc/httpd/conf.d/ssl.conf` file and find this
   directive:

```
SSLCryptoDevice builtin
```

Change the directive as follows:

```
SSLCryptoDevice pkcs11
```

5. Configure NGINX to use the pkcs11 SSL engine by setting the
   top-level `ssl_engine` directive.

Using your preferred text editor, open
`/etc/nginx/nginx.conf`. Add the following line
below `pid /run/nginx.pid;`.

```
ssl_engine pkcs11;
```

Example

```
# For more information on configuration, see:
#   * Official English Documentation: http://nginx.org/en/docs/

user nginx;
worker_processes auto;
error_log /var/log/nginx/error.log;
pid /run/nginx.pid;

**ssl\_engine pkcs11;**
```

6. Enable the TLS server and configure the server to use your
   certificate.

In `/etc/nginx/nginx.conf`, scroll to the bottom of
the file and do the following:

    * Uncomment all of the lines below `Settings for a
     TLS enabled server`.
    * In the first block, for `server_name`,
     specify the host name, or the common name (CN), that you
     specified when you created the certificate.
    * In the second block, remove the following
     lines.



    ```
    ssl_certificate "/etc/pki/nginx/server.crt";
    ssl_certificate_key "/etc/pki/nginx/private/server.key";
    ssl_ciphers PROFILE=SYSTEM;
    ```

    And add the following line.



    ```
    ssl_protocols TLSv1.2;
    ```
    * Add the following as a new block below the second
     block.



    ```
    # Set this to the stanza path configured in /etc/nitro_enclaves/acm.yaml
    include "/etc/pki/nginx/nginx-acm.conf";
    ```

The completed section should appear as follows.

```
# Settings for a TLS enabled server.
#
    server {
        listen       443 ssl http2;
        listen       [::]:443 ssl http2;
        server_name  `example.com`;
        root         /usr/share/nginx/html;

        ssl_protocols TLSv1.2;
        ssl_session_cache shared:SSL:1m;
        ssl_session_timeout  10m;
        ssl_prefer_server_ciphers on;

        # Set this to the stanza path configured in /etc/nitro_enclaves/acm.yaml
        include "/etc/pki/nginx/nginx-acm.conf";

        # Load configuration files for the default server block.
        include /etc/nginx/default.d/*.conf;

        error_page 404 /404.html;
            location = /40x.html {
        }
        error_page 500 502 503 504 /50x.html;
            location = /50x.html {
        }
    }
```

    * (Amazon Linux 2023) Edit the OpenSSL configuration file
     `/etc/pki/tls/openssl.cnf` as
     follows.



    ```
    [openssl_init]
    ...
    engines = engine_section

    [engine_section]
    pkcs11 = pkcs11_section

    [ pkcs11_section ]
    engine_id = pkcs11
    init = 1
    ...
    ```

7. Start the ACM for Nitro Enclaves service and ensure that it
   starts automatically at instance boot.

```
`$` sudo systemctl start nitro-enclaves-acm.service
```

```
`$` sudo systemctl enable nitro-enclaves-acm
```

8. Test that the ACM for Nitro Enclaves is working as
   expected.

If you used a public certificate, use the following
command.

```
`$` curl https://`host_name_or_IP`
```

If you used a private certificate, you must add the host name
to `/etc/hosts` in the following format:
`127.0.0.1 `host_name``,
 for example `127.0.0.1 example.com`. And you must
specify the certificate chain to use to validate the
certificate. For more information about generating the
certificate chain for your certificate, see [Exporting a Private Certificate](../../../acm/latest/userguide/export-private.md#export-console "../../../acm/latest/userguide/export-private.md#export-console") in the
_AWS Certificate Manager User Guide_.

```
`$` curl --cacert `path_to_pem_file` https://`host_name_or_IP`
```

A successful test displays the NGINX index.htm. The ACM for
Nitro Enclaves service continuously polls and fetches the
ACMcertificate data and updates NGINX accordingly. It does
this by generating an NGINX config snippet and including it in
the main `nginx.conf`.

If you renew the ACM certificate by running [acm
renew-certificate](../../../cli/latest/reference/acm/renew-certificate.md "../../../cli/latest/reference/acm/renew-certificate.md"), the ACM for Nitro Enclaves
automatically reconfigures the enclave and the NGINX web server.
You can use the following command to check the log for update
announcements and to diagnose possible issues.

```
`$` journalctl -u nitro-enclaves-acm.service
```

If you encounter any unexpected errors, you can also check the
NGINX service log for more details.

```
`$` journalctl -u nginx.service
```

Apache

###### To configure Apache HTTP server

1. SSH into the instance that you launched previously.
2. Nitro Enclaves ships with a sample ACM for Nitro Enclaves
   configuration file that you can use as a starting point for your
   own configuration. Rename the sample ACM for Nitro Enclaves
   configuration file from
   `/etc/nitro_enclaves/acm-httpd.example.yaml` to
   `/etc/nitro_enclaves/acm.yaml`.

```
`$` sudo mv /etc/nitro_enclaves/acm-httpd.example.yaml /etc/nitro_enclaves/acm.yaml
```

3. Specify the ARN of the certificate that you associated with
   the IAM role that is attached to the parent instance. Using
   your preferred text editor, open
   `/etc/nitro_enclaves/acm.yaml`. In the
   `Acm` section, for `certificate_arn`,
   specify the ARN of the certificate. Save and close the
   file.
4. Using your preferred text editor, open
   `/etc/httpd/conf.d/httpd-acm.conf`. For
   `ServerName`, specify the host name, or the
   common name (CN), that you specified when you created the
   certificate, and configure the remaining settings as needed. The
   following is an example of a minimal SSL/TLS
   configuration:

```
<VirtualHost *:443>
ServerName `www.example.com`
SSLEngine on
SSLProtocol -all +TLSv1.2
SSLCertificateKeyFile "/etc/pki/tls/private/localhost.key"
SSLCertificateFile "/etc/pki/tls/certs/localhost.crt"
</VirtualHost>
```

###### Note

The `SSLCertificateFile` and
`SSLCertificateKeyFile` entries must be
present in the configuration file. These entries will be
automatically updated with the URIs after starting the ACM
for Nitro Enclaves service. 5. Apache HTTP server ships with a configuration file that you
can use. To use the configuration file, rename it from
`/etc/httpd/conf.d/ssl.conf` to
`/etc/httpd/conf.d/httpd-acm.conf`.

```
`$` sudo mv /etc/httpd/conf.d/ssl.conf /etc/httpd/conf.d/httpd-acm.conf
```

6. Start the ACM for Nitro Enclaves service and ensure that it
   starts automatically at instance boot.

```
`$` sudo systemctl start nitro-enclaves-acm.service
```

```
`$` sudo systemctl enable nitro-enclaves-acm
```

7. Test that the ACM for Nitro Enclaves is working as
   expected.
   - If you used a public certificate, use the following
     command.

   ```
   `$` curl https://`host_name_or_IPM`
   ```

   - If you used a private certificate, you must add the
     host name to `/etc/hosts` in the following
     format: 127.0.0.1 `host_name`,
     for example `127.0.0.1 example.com`. And you
     must specify the certificate chain to use to validate
     the certificate. For more information about generating
     the certificate chain for your certificate, see [Exporting a Private Certificate](../../../acm/latest/userguide/export-private.md#export-console "../../../acm/latest/userguide/export-private.md#export-console") in the
     _AWS Certificate Manager User Guide_.

```
`$` curl --cacert `path_to_pem_file` https://`host_name_or_IP`
```

A successful test displays the Apache HTTP index.htm. The
ACM for Nitro Enclaves service continuously polls and fetches the
ACM certificate data and updates Apache accordingly.

If you renew the ACM certificate by running [acm
renew-certificate](../../../cli/latest/reference/acm/renew-certificate.md "../../../cli/latest/reference/acm/renew-certificate.md"), the ACM for Nitro Enclaves
automatically reconfigures the enclave and the Apache web
server. You can use the following command to check the log for
update announcements and to diagnose possible issues.

```
`$` $ journalctl -u nitro-enclaves-acm.service
```

If you encounter any unexpected errors, you can also check the
Apache HTTP service log for more details.

```
`$` journalctl -u httpd.service
```

## Using multiple certificates

You can also add multiple ACM certificates; one for each PKCS#11 token. For each
additional certificate that you need to add, repeat [Step 4: Associate the role with the ACM
certificate](#role-cert "#role-cert") in order to associate your IAM role with the
additional ACM certificates.

Then to add more PKCS#11 tokens, open `/etc/nitro_enclaves/acm.yaml`
with your preferred text editor, and under the `token` section, add
another `label` block and specify a label name, the ARN of the additional
certificate, and a path for the NGINX stanza or Apache HTTP configuration file
respectively. For example, the following snippet shows the format to be used for two
ACM certificates (the initial certificate and two additional certificates):

NGINX

```
tokens:
    # A label for this PKCS#11 token
  - label: nginx-acm-token
    # Configure a managed token, sourced from an ACM certificate.
    source:
      Acm:
        # The certificate ARN
        # Note: this certificate must have been associated with the IAM role assigned to the instance on
        # which ACM for Nitro Enclaves is run.
        certificate_arn: "arn:aws:acm:us-east-1:123456789012:certificate/d4c3b2a1-e5d0-4d51-95d9-1927fEXAMPLE"
    target:
      NginxStanza:
        # Path to the nginx stanza to be written by the ACM service whenever # the certificate configuration
        # changes (e.g. after a certificate renewal). # This file must be included from the main nginx config
        # `server` section, as it will contain the TLS nginx configuration directives.
        path: /etc/pki/nginx/nginx-acm.conf
        # Stanza file owner (i.e. the user nginx is configured to run as).
        user: nginx
    # PKCS#11 token 2
  - label: `token_2_name`
    source:
      Acm:
        certificate_arn: "`certificate_2_ARN`"
    target:
      NginxStanza:
        path: `/etc/pki/nginx/nginx-acm-2.conf`
        user: nginx

```

Apache

```
tokens:
  # A label for this PKCS#11 token
  - label: `token_1_name`
    # Configure a managed token, sourced from an ACM certificate.
    source:
      Acm:
        # The certificate ARN
        # Note: this certificate must have been associated with the IAM role assigned to the instance
        # on which ACM for Nitro Enclaves is run.
        certificate_arn: "`certificate_1_ARN`"
    target:
      Conf:
        # Path to the server configuration file to be written by # the ACM service whenever the
        # certificate configuration changes (e.g. after a certificate renewal). The SSLCertificateKeyFile
        # and optionally the SSLCertificateFile directives shall be populated.
        path: `/etc/httpd/conf.d/httpd-acm.conf`
        # Configuration file owner (i.e. the user httpd is configured to run as).
        user: apache
    # Attestation period (seconds)
    refresh_interval_secs: 43200

  - label: `token_2_name`
    # Configure a managed token, sourced from an ACM certificate.
    source:
      Acm:
        # The certificate ARN
        # Note: this certificate must have been associated with the IAM role assigned to the instance
        # on which ACM for Nitro Enclaves is run.
        certificate_arn: "`certificate_2_ARN`"
    target:
      Conf:
        # Path to the server configuration file to be written by the ACM service whenever the certificate
        # configuration changes (e.g. after a certificate renewal). The SSLCertificateKeyFile and optionally
        # the SSLCertificateFile directives shall be populated.
        path: `/etc/httpd/conf.d/httpd-acm-2.conf`
        # Configuration file owner (i.e. the user httpd is configured to run as).
        user: apache
    # Attestation repeat period (seconds)
    refresh_interval_secs: 43200
```

###### Note

You also need to update the `/etc/nginx/nginx.conf` configuration
(NGINX) or the `/etc/httpd/conf.d/httpd-acm.conf` configuration file
(Apache) to include the additional ACM certificates. For more information
about configuring NGINX for multiple domains and about different use cases,
refer to the [NGINX documentation](https://nginx.org/en/docs/ "https://nginx.org/en/docs/")
or [Apache HTTP server
documentation](https://httpd.apache.org/docs/ "https://httpd.apache.org/docs/").

After you have completed the necessary configuration, run the following command to
restart the Start the ACM for Nitro Enclaves service.

```
`$` sudo systemctl restart nitro-enclaves-acm.service
```
