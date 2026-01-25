# AWS CloudHSM SSL/TLS offload on Windows using IIS with KSP

This tutorial provides step-by-step instructions for setting up SSL/TLS offload with AWS CloudHSM
on a Windows web server.

###### Topics

- [Overview](#ssl-offload-windows-overview "#ssl-offload-windows-overview")
- [Step 1: Set up the prerequisites](#ssl-offload-prerequisites-windows "#ssl-offload-prerequisites-windows")
- [Step 2: Create a certificate
  signing request (CSR) and certificate](#ssl-offload-windows-create-csr-and-certificate "#ssl-offload-windows-create-csr-and-certificate")
- [Step 3: Configure the web server](#ssl-offload-configure-web-server-windows "#ssl-offload-configure-web-server-windows")
- [Step 4: Enable HTTPS
  traffic and verify the certificate](#ssl-offload-enable-traffic-and-verify-certificate-windows "#ssl-offload-enable-traffic-and-verify-certificate-windows")

## Overview

On Windows, the [Internet Information Services (IIS) for
Windows Server](https://www.iis.net/ "https://www.iis.net/") web server application natively supports HTTPS. The [AWS CloudHSM key storage provider (KSP) for Microsoft's Cryptography API:
Next Generation (CNG)](ksp-library.md "ksp-library.md") provides the interface that allows IIS to use the HSMs in your
cluster for cryptographic offloading and key storage. The AWS CloudHSM KSP is the bridge that
connects IIS to your AWS CloudHSM cluster.

This tutorial shows you how to do the following:

- Install the web server software on an Amazon EC2 instance.
- Configure the web server software to support HTTPS with a private key stored in your
  AWS CloudHSM cluster.
- (Optional) Use Amazon EC2 to create a second web server instance and Elastic Load Balancing to create a load
  balancer. Using a load balancer can increase performance by distributing the load across
  multiple servers. It can also provide redundancy and higher availability if one or more
  servers fail.

When you're ready to get started, go to [Step 1: Set up the prerequisites](#ssl-offload-prerequisites-windows "#ssl-offload-prerequisites-windows").

## Step 1: Set up the prerequisites

Different platforms require different prerequisites. Use the prerequisites section below
that matches your platform.

###### Topics

- [Prerequisites for Client SDK 5](#ssl-offload-prerequisites-windows-sdk5 "#ssl-offload-prerequisites-windows-sdk5")
- [Prerequisites for Client SDK 3](#ssl-offload-prerequisites-windows-sdk3 "#ssl-offload-prerequisites-windows-sdk3")

### Prerequisites for Client SDK 5

To set up web server SSL/TLS offload with AWS CloudHSM, you need the following:

- An active AWS CloudHSM cluster with at least one HSM.
- An Amazon EC2 instance running a Windows operating system with the following software
  installed:
  - The AWS CloudHSM client software for Windows.
  - Internet Information Services (IIS) for Windows Server.

- A [crypto user](understanding-users.md#crypto-user-chsm-cli "understanding-users.md#crypto-user-chsm-cli") (CU) to own and manage the web server's
  private key on the HSM.

###### Note

This tutorial uses Microsoft Windows Server 2019. Microsoft Windows Server 2016 and 2022 is also
supported.

###### To set up a Windows Server instance and create a CU on the HSM

1. Complete the steps in [Getting started](getting-started.md "getting-started.md"). When you launch the Amazon EC2 client, choose a Windows
   Server 2019 AMI. When you complete these steps, you have an active
   cluster with at least one HSM. You also have an Amazon EC2 client instance running Windows Server
   with the AWS CloudHSM client software for Windows installed.
2. (Optional) Add more HSMs to your cluster. For more information, see [Adding an HSM to an AWS CloudHSM cluster](add-hsm.md "add-hsm.md").
3. Connect to your Windows server. For more information, see [Connect to Your
   Instance](../../../AWSEC2/latest/WindowsGuide/EC2_GetStarted.md#ec2-connect-to-instance-windows "../../../AWSEC2/latest/WindowsGuide/EC2_GetStarted.md#ec2-connect-to-instance-windows") in the _Amazon EC2 User Guide_.
4. Use CloudHSM CLI to create a crypto user (CU). Keep track of the CU user
   name and password. You will need them to complete the next step.

###### Note

For information on creating a user, see [Managing HSM users with CloudHSM CLI](manage-hsm-users-chsm-cli.md "manage-hsm-users-chsm-cli.md"). 5. [Set the login credentials for the HSM](ksp-library-authentication.md "ksp-library-authentication.md"),
using the CU user name and password that you created in the previous step. 6. In step 5, if you used Windows Credentials Manager to set HSM credentials, download [`psexec.exe`](https://live.sysinternals.com/psexec.exe "https://live.sysinternals.com/psexec.exe") from SysInternals to run the following command as _NT Authority\SYSTEM_:

```

psexec.exe -s "C:\Program Files\Amazon\CloudHsm\tools\set_cloudhsm_credentials.exe" --username `<USERNAME>` --password `<PASSWORD>`
```

Replace `<USERNAME>` and `<PASSWORD>` with the HSM credentials.

###### To install IIS on your Windows Server

1. If you haven't already done so, connect to your Windows server. For more information,
   see [Connect to Your Instance](../../../AWSEC2/latest/WindowsGuide/EC2_GetStarted.md#ec2-connect-to-instance-windows "../../../AWSEC2/latest/WindowsGuide/EC2_GetStarted.md#ec2-connect-to-instance-windows") in the _Amazon EC2 User Guide_.
2. On your Windows server, start **Server Manager**.
3. In the **Server Manager** dashboard, choose **Add roles and
   features**.
4. Read the **Before you begin** information, and then choose
   **Next**.
5. For **Installation Type**, choose **Role-based or feature-based
   installation**. Then choose **Next**.
6. For **Server Selection**, choose **Select a server from the
   server pool**. Then choose **Next**.
7. For **Server Roles**, do the following:
   1. Select **Web Server (IIS)**.
   2. For **Add features that are required for Web Server (IIS)**, choose
      **Add Features**.
   3. Choose **Next** to finish selecting server roles.

8. For **Features**, accept the defaults. Then choose
   **Next**.
9. Read the **Web Server Role (IIS)** information. Then choose
   **Next**.
10. For **Select role services**, accept the defaults or change the
    settings as preferred. Then choose **Next**.
11. For **Confirmation**, read the confirmation information. Then choose
    **Install**.
12. After the installation is complete, choose **Close**.

After you complete these steps, go to [Step 2: Create a certificate
signing request (CSR) and certificate](#ssl-offload-windows-create-csr-and-certificate "#ssl-offload-windows-create-csr-and-certificate").

### Prerequisites for Client SDK 3

To set up web server SSL/TLS offload with AWS CloudHSM, you need the following:

- An active AWS CloudHSM cluster with at least one HSM.
- An Amazon EC2 instance running a Windows operating system with the following software
  installed:
  - The AWS CloudHSM client software for Windows.
  - Internet Information Services (IIS) for Windows Server.

- A [crypto user](understanding-users.md#crypto-user-chsm-cli "understanding-users.md#crypto-user-chsm-cli") (CU) to own and manage the web server's
  private key on the HSM.

###### Note

This tutorial uses Microsoft Windows Server 2016. Microsoft Windows Server 2012 is also
supported, but Microsoft Windows Server 2012 R2 is not.

###### To set up a Windows Server instance and create a CU on the HSM

1. Complete the steps in [Getting started](getting-started.md "getting-started.md"). When you launch the Amazon EC2 client, choose a Windows
   Server 2016 or Windows Server 2012 AMI. When you complete these steps, you have an active
   cluster with at least one HSM. You also have an Amazon EC2 client instance running Windows Server
   with the AWS CloudHSM client software for Windows installed.
2. (Optional) Add more HSMs to your cluster. For more information, see [Adding an HSM to an AWS CloudHSM cluster](add-hsm.md "add-hsm.md").
3. Connect to your Windows server. For more information, see [Connect to Your
   Instance](../../../AWSEC2/latest/WindowsGuide/EC2_GetStarted.md#ec2-connect-to-instance-windows "../../../AWSEC2/latest/WindowsGuide/EC2_GetStarted.md#ec2-connect-to-instance-windows") in the _Amazon EC2 User Guide_.
4. Use CloudHSM CLI to create a crypto user (CU). Keep track of the CU user
   name and password. You will need them to complete the next step.

###### Note

For information on creating a user, see [Managing HSM users with CloudHSM CLI](manage-hsm-users-chsm-cli.md "manage-hsm-users-chsm-cli.md"). 5. [Set the login credentials for the HSM](ksp-library-prereq.md "ksp-library-prereq.md"),
using the CU user name and password that you created in the previous step. 6. In step 5, if you used Windows Credentials Manager to set HSM credentials, download [`psexec.exe`](https://live.sysinternals.com/psexec.exe "https://live.sysinternals.com/psexec.exe") from SysInternals to run the following command as _NT Authority\SYSTEM_:

```

psexec.exe -s "C:\Program Files\Amazon\CloudHsm\tools\set_cloudhsm_credentials.exe" --username `<USERNAME>` --password `<PASSWORD>`
```

Replace `<USERNAME>` and `<PASSWORD>` with the HSM credentials.

###### To install IIS on your Windows Server

1. If you haven't already done so, connect to your Windows server. For more information,
   see [Connect to Your Instance](../../../AWSEC2/latest/WindowsGuide/EC2_GetStarted.md#ec2-connect-to-instance-windows "../../../AWSEC2/latest/WindowsGuide/EC2_GetStarted.md#ec2-connect-to-instance-windows") in the _Amazon EC2 User Guide_.
2. On your Windows server, start **Server Manager**.
3. In the **Server Manager** dashboard, choose **Add roles and
   features**.
4. Read the **Before you begin** information, and then choose
   **Next**.
5. For **Installation Type**, choose **Role-based or feature-based
   installation**. Then choose **Next**.
6. For **Server Selection**, choose **Select a server from the
   server pool**. Then choose **Next**.
7. For **Server Roles**, do the following:
   1. Select **Web Server (IIS)**.
   2. For **Add features that are required for Web Server (IIS)**, choose
      **Add Features**.
   3. Choose **Next** to finish selecting server roles.

8. For **Features**, accept the defaults. Then choose
   **Next**.
9. Read the **Web Server Role (IIS)** information. Then choose
   **Next**.
10. For **Select role services**, accept the defaults or change the
    settings as preferred. Then choose **Next**.
11. For **Confirmation**, read the confirmation information. Then choose
    **Install**.
12. After the installation is complete, choose **Close**.

After you complete these steps, go to [Step 2: Create a certificate
signing request (CSR) and certificate](#ssl-offload-windows-create-csr-and-certificate "#ssl-offload-windows-create-csr-and-certificate").

## Step 2: Create a certificate

signing request (CSR) and certificate

To enable HTTPS, your web server needs an SSL/TLS certificate and a corresponding private
key. To use SSL/TLS offload with AWS CloudHSM, you store the private key in the HSM in your AWS CloudHSM
cluster. To do this, you use the [AWS CloudHSM
key storage provider (KSP) for Microsoft's Cryptography API: Next Generation (CNG)](ksp-v3-library.md "ksp-v3-library.md") to
create a certificate signing request (CSR). Then you give the CSR to a certificate authority
(CA), which signs the CSR to produce a certificate.

###### Topics

- [Create a CSR with Client SDK 5](#ssl-offload-windows-create-csr-new-version "#ssl-offload-windows-create-csr-new-version")
- [Create a CSR with Client SDK 3](#ssl-offload-windows-create-csr-old-version "#ssl-offload-windows-create-csr-old-version")
- [Get a signed certificate and import
  it](#ssl-offload-windows-create-certificate "#ssl-offload-windows-create-certificate")

### Create a CSR with Client SDK 5

1. On your Windows Server, use a text editor to create a certificate request file named
   `IISCertRequest.inf`. The following shows the contents of an example
   `IISCertRequest.inf` file. For more information about the sections,
   keys, and values that you can specify in the file, see [Microsoft's documentation](https://docs.microsoft.com/en-us/windows-server/administration/windows-commands/certreq_1#BKMK_New "https://docs.microsoft.com/en-us/windows-server/administration/windows-commands/certreq_1#BKMK_New"). Do not change the `ProviderName`
   value.

```
[Version]
Signature = "$Windows NT$"
[NewRequest]
Subject = "CN=example.com,C=US,ST=Washington,L=Seattle,O=ExampleOrg,OU=WebServer"
HashAlgorithm = SHA256
KeyAlgorithm = RSA
KeyLength = 2048
ProviderName = "CloudHSM Key Storage Provider"
KeyUsage = 0xf0
MachineKeySet = True
[EnhancedKeyUsageExtension]
OID=1.3.6.1.5.5.7.3.1
```

2. Use the [Windows **certreq** command](https://docs.microsoft.com/en-us/windows-server/administration/windows-commands/certreq_1 "https://docs.microsoft.com/en-us/windows-server/administration/windows-commands/certreq_1") to create a CSR from the
   `IISCertRequest.inf` file that you created in the previous step. The
   following example saves the CSR to a file named `IISCertRequest.csr`.
   If you used a different file name for your certificate request file, replace
   `IISCertRequest.inf` with the appropriate file name. You can
   optionally replace `IISCertRequest.csr` with a different file
   name for your CSR file.

````
`C:\>``certreq -new `IISCertRequest.inf` `IISCertRequest.csr```CertReq: Request Created`
````

The `IISCertRequest.csr` file contains your CSR. You need this CSR
to get a signed certificate.

### Create a CSR with Client SDK 3

1. If you haven't already done so, connect to your Windows server. For more information,
   see [Connect to Your Instance](../../../AWSEC2/latest/WindowsGuide/EC2_GetStarted.md#ec2-connect-to-instance-windows "../../../AWSEC2/latest/WindowsGuide/EC2_GetStarted.md#ec2-connect-to-instance-windows") in the
   _Amazon EC2 User Guide_.
2. Use the following command to start the AWS CloudHSM client daemon.

Amazon Linux

```
`$` `sudo start cloudhsm-client`
```

Amazon Linux 2

```
`$` `sudo service cloudhsm-client start`
```

CentOS 7

```
`$` `sudo service cloudhsm-client start`
```

CentOS 8

```
`$` `sudo service cloudhsm-client start`
```

RHEL 7

```
`$` `sudo service cloudhsm-client start`
```

RHEL 8

```
`$` `sudo service cloudhsm-client start`
```

Ubuntu 16.04 LTS

```
`$` `sudo service cloudhsm-client start`
```

Ubuntu 18.04 LTS

```
`$` `sudo service cloudhsm-client start`
```

Windows

    * For Windows client 1.1.2+:



    ```
    `C:\Program Files\Amazon\CloudHSM>``net.exe start AWSCloudHSMClient`
    ```
    * For Windows clients 1.1.1 and older:



    ```
    `C:\Program Files\Amazon\CloudHSM>``start "cloudhsm_client" cloudhsm_client.exe C:\ProgramData\Amazon\CloudHSM\data\cloudhsm_client.cfg`
    ```

3. On your Windows Server, use a text editor to create a certificate request file named
   `IISCertRequest.inf`. The following shows the contents of an example
   `IISCertRequest.inf` file. For more information about the sections,
   keys, and values that you can specify in the file, see [Microsoft's documentation](https://docs.microsoft.com/en-us/windows-server/administration/windows-commands/certreq_1#BKMK_New "https://docs.microsoft.com/en-us/windows-server/administration/windows-commands/certreq_1#BKMK_New"). Do not change the `ProviderName`
   value.

```
[Version]
Signature = "$Windows NT$"
[NewRequest]
Subject = "CN=example.com,C=US,ST=Washington,L=Seattle,O=ExampleOrg,OU=WebServer"
HashAlgorithm = SHA256
KeyAlgorithm = RSA
KeyLength = 2048
ProviderName = "Cavium Key Storage Provider"
KeyUsage = 0xf0
MachineKeySet = True
[EnhancedKeyUsageExtension]
OID=1.3.6.1.5.5.7.3.1
```

4. Use the [Windows **certreq** command](https://docs.microsoft.com/en-us/windows-server/administration/windows-commands/certreq_1 "https://docs.microsoft.com/en-us/windows-server/administration/windows-commands/certreq_1") to create a CSR from the
   `IISCertRequest.inf` file that you created in the previous step. The
   following example saves the CSR to a file named `IISCertRequest.csr`.
   If you used a different file name for your certificate request file, replace
   `IISCertRequest.inf` with the appropriate file name. You can
   optionally replace `IISCertRequest.csr` with a different file
   name for your CSR file.

````
`C:\>``certreq -new `IISCertRequest.inf` `IISCertRequest.csr```SDK Version: 2.03

CertReq: Request Created`
````

The `IISCertRequest.csr` file contains your CSR. You need this CSR
to get a signed certificate.

### Get a signed certificate and import

it

In a production environment, you typically use a certificate authority (CA) to create a
certificate from a CSR. A CA is not necessary for a test environment. If you do use a CA, send
the CSR file (`IISCertRequest.csr`) to it and use the CA to create a signed
SSL/TLS certificate.

As an alternative to using a CA, you can use a tool like [OpenSSL](https://www.openssl.org/ "https://www.openssl.org/") to create a self-signed certificate.

###### Warning

Self-signed certificates are not trusted by browsers and should not be used in
production environments. They can be used in test environments.

The following procedures show how to create a self-signed certificate and use it to sign
your web server's CSR.

###### To create a self-signed certificate

1. Use the following OpenSSL command to create a private key. You can optionally replace
   `SelfSignedCA.key` with the file name to contain your private
   key.

```
`openssl genrsa -aes256 -out `SelfSignedCA.key` 2048``Generating RSA private key, 2048 bit long modulus
......................................................................+++
.........................................+++
e is 65537 (0x10001)
Enter pass phrase for SelfSignedCA.key:
Verifying - Enter pass phrase for SelfSignedCA.key:`
```

2. Use the following OpenSSL command to create a self-signed certificate using the
   private key that you created in the previous step. This is an interactive command. Read
   the on-screen instructions and follow the prompts. Replace
   `SelfSignedCA.key` with the name of the file that contains your
   private key (if different). You can optionally replace
   `SelfSignedCA.crt` with the file name to contain your
   self-signed certificate.

````
`openssl req -new -x509 -days 365 -key `SelfSignedCA.key` -out `SelfSignedCA.crt```Enter pass phrase for SelfSignedCA.key:
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
````

###### To use your self-signed certificate to sign your web server's CSR

- Use the following OpenSSL command to use your private key and self-signed certificate
  to sign the CSR. Replace the following with the names of the files that contain the
  corresponding data (if different).
  - `IISCertRequest.csr` – The name of the file that
    contains your web server's CSR
  - `SelfSignedCA.crt` – The name of the file that
    contains your self-signed certificate
  - `SelfSignedCA.key` – The name of the file that
    contains your private key
  - `IISCert.crt` – The name of the file to contain
    your web server's signed certificate

````
`openssl x509 -req -days 365 -in `IISCertRequest.csr` \
 -CA `SelfSignedCA.crt` \
 -CAkey `SelfSignedCA.key` \
 -CAcreateserial \
 -out `IISCert.crt```Signature ok
subject=/ST=IIS-HSM/L=IIS-HSM/OU=IIS-HSM/O=IIS-HSM/CN=IIS-HSM/C=IIS-HSM
Getting CA Private Key
Enter pass phrase for SelfSignedCA.key:`
````

After you complete the previous step, you have a signed certificate for your web server
(`IISCert.crt`) and a self-signed certificate
(`SelfSignedCA.crt`). When you have these files, go to [Step 3: Configure the web server](#ssl-offload-configure-web-server-windows "#ssl-offload-configure-web-server-windows").

## Step 3: Configure the web server

Update your IIS website's configuration to use the HTTPS certificate that you created at the
end of the [previous step](#ssl-offload-windows-create-csr-and-certificate "#ssl-offload-windows-create-csr-and-certificate").
This will finish setting up your Windows web server software (IIS) for SSL/TLS offload with
AWS CloudHSM.

If you used a self-signed certificate to sign your CSR, you must first import the
self-signed certificate into the Windows Trusted Root Certification Authorities.

###### To import your self-signed certificate into the Windows Trusted Root Certification

Authorities

1. If you haven't already done so, connect to your Windows server. For more information,
   see [Connect to Your Instance](../../../AWSEC2/latest/WindowsGuide/EC2_GetStarted.md#ec2-connect-to-instance-windows "../../../AWSEC2/latest/WindowsGuide/EC2_GetStarted.md#ec2-connect-to-instance-windows") in the _Amazon EC2 User Guide_.
2. Copy your self-signed certificate to your Windows server.
3. On your Windows Server, open the **Control Panel**.
4. For **Search Control Panel**, type `certificates`.
   Then choose **Manage computer certificates**.
5. In the **Certificates ‐ Local Computer** window, double-click
   **Trusted Root Certification Authorities**.
6. Right-click on **Certificates** and then choose **All
   Tasks**, **Import**.
7. In the **Certificate Import Wizard**, choose
   **Next**.
8. Choose **Browse**, then find and select your self-signed certificate.
   If you created your self-signed certificate by following the instructions in the [previous step of this
   tutorial](#ssl-offload-windows-create-csr-and-certificate "#ssl-offload-windows-create-csr-and-certificate"), your self-signed certificate is named
   `SelfSignedCA.crt`. Choose **Open**.
9. Choose **Next**.
10. For **Certificate Store**, choose **Place all certificates in
    the following store**. Then ensure that **Trusted Root Certification
    Authorities** is selected for **Certificate store**.
11. Choose **Next** and then choose **Finish**.

###### To update the IIS website's configuration

1. If you haven't already done so, connect to your Windows server. For more information,
   see [Connect to Your Instance](../../../AWSEC2/latest/WindowsGuide/EC2_GetStarted.md#ec2-connect-to-instance-windows "../../../AWSEC2/latest/WindowsGuide/EC2_GetStarted.md#ec2-connect-to-instance-windows") in the _Amazon EC2 User Guide_.
2. Start the AWS CloudHSM client daemon.
3. Copy your web server's signed certificate—the one that you created at the end of
   [this tutorial's previous
   step](#ssl-offload-windows-create-csr-and-certificate "#ssl-offload-windows-create-csr-and-certificate")—to your Windows server.
4. On your Windows Server, use the [Windows **certreq** command](https://docs.microsoft.com/en-us/windows-server/administration/windows-commands/certreq_1 "https://docs.microsoft.com/en-us/windows-server/administration/windows-commands/certreq_1") to accept the signed certificate, as in the following
   example. Replace `IISCert.crt` with the name of the file that
   contains your web server's signed certificate.

````
`C:\>``certreq -accept `IISCert.crt```SDK Version: 2.03`
````

5. On your Windows server, start **Server Manager**.
6. In the **Server Manager** dashboard, in the top right corner, choose
   **Tools**, **Internet Information Services (IIS)
   Manager**.
7. In the **Internet Information Services (IIS) Manager** window,
   double-click your server name. Then double-click **Sites**. Select your
   website.
8. Select **SSL Settings**. Then, on the right side of the window, choose
   **Bindings**.
9. In the **Site Bindings** window, choose
   **Add**.
10. For **Type**, choose **https**. For **SSL
    certificate**, choose the HTTPS certificate that you created at the end of [this tutorial's previous
    step](#ssl-offload-windows-create-csr-and-certificate "#ssl-offload-windows-create-csr-and-certificate").

###### Note

If you encounter an error during this certificate binding, restart your server and
retry this step. 11. Choose **OK**.

After you update your website's configuration, go to [Step 4: Enable HTTPS
traffic and verify the certificate](#ssl-offload-enable-traffic-and-verify-certificate-windows "#ssl-offload-enable-traffic-and-verify-certificate-windows").

## Step 4: Enable HTTPS

traffic and verify the certificate

After you configure your web server for SSL/TLS offload with AWS CloudHSM, add your web server
instance to a security group that allows inbound HTTPS traffic. This allows clients, such as web
browsers, to establish an HTTPS connection with your web server. Then make an HTTPS connection
to your web server and verify that it's using the certificate that you configured for
SSL/TLS offload with AWS CloudHSM.

###### Topics

- [Enable inbound HTTPS
  connections](#ssl-offload-add-security-group-windows "#ssl-offload-add-security-group-windows")
- [Verify that HTTPS uses the
  certificate that you configured](#ssl-offload-verify-https-connection-windows "#ssl-offload-verify-https-connection-windows")

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
