# AWS CloudHSM SSL/TLS offload on Linux using Tomcat with JSSE

This topic provides step-by-step instructions for setting up SSL/TLS offload using Java Secure Socket Extension (JSSE) with the AWS CloudHSM JCE SDK.

###### Topics

- [Overview](#third-offload-linux-jsse-overview "#third-offload-linux-jsse-overview")
- [Step 1: Set up the prerequisites](#third-offload-linux-jsse-prereqs "#third-offload-linux-jsse-prereqs")
- [Step 2: Generate or
  import a private key and SSL/TLS certificate](#third-offload-linux-jsse-gen "#third-offload-linux-jsse-gen")
- [Step 3: Configure the Tomcat web server](#third-offload-linux-jsse-config "#third-offload-linux-jsse-config")
- [Step 4: Enable HTTPS traffic
  and verify the certificate](#third-offload-linux-jsse-verify "#third-offload-linux-jsse-verify")

## Overview

In AWS CloudHSM, Tomcat web servers work on Linux to support HTTPS. The AWS CloudHSM JCE SDK provides an interface that can be used with JSSE (Java Secure Socket Extension) to enable use of HSMs for such web servers.
AWS CloudHSM JCE is the bridge that connects JSSE to your AWS CloudHSM cluster. JSSE is a Java API for Secure Sockets Layer (SSL) and Transport Layer Security (TLS) protocols.

## Step 1: Set up the prerequisites

Follow these prerequisites to use a Tomcat web server with AWS CloudHSM for SSL/TLS offload on Linux. These prerequisites must be met to set up web server SSL/TLS offload with Client SDK 5 and a Tomcat web server.

###### Note

Different platforms require different prerequisites. Always follow the correct installation steps for your platform.

### Prerequisites

- An Amazon EC2 instance running a Linux operating system with A tomcat web server
  installed.
- A [crypto user](understanding-users.md#crypto-user-chsm-cli "understanding-users.md#crypto-user-chsm-cli") (CU) to own and manage the web server's
  private key on the HSM.
- An active AWS CloudHSM cluster with at least two hardware security modules (HSMs) that have [JCE for
  Client SDK 5](java-library-install_5.md "java-library-install_5.md") installed and configured.

###### Note

You can use a single HSM cluster, but you must first disable client key
durability. For more information, see [Manage Client
Key Durability Settings](working-client-sync.md#client-sync-sdk8 "working-client-sync.md#client-sync-sdk8") and [Client SDK 5
Configure Tool](configure-sdk-5.md "configure-sdk-5.md").

#### How to meet the prerequisites

1. Install and configure the JCE for AWS CloudHSM on an active AWS CloudHSM cluster with at least two hardware security modules (HSMs). For more information about
   installation, see [JCE for
   Client SDK 5](java-library-install_5.md "java-library-install_5.md").
2. On an EC2 Linux instance that has access to your AWS CloudHSM cluster, follow the [Apache Tomcat instructions](https://tomcat.apache.org/download-90.cgi "https://tomcat.apache.org/download-90.cgi ") to download and install the Tomcat web server.
3. Use [CloudHSM CLI](cloudhsm_cli.md "cloudhsm_cli.md") to create a crypto user (CU). For more information about
   managing HSM users, see [Managing HSM users with CloudHSM CLI](manage-hsm-users-chsm-cli.md "manage-hsm-users-chsm-cli.md").

###### Tip

Keep track of the CU user name and password. You will need them later when you
generate or import the HTTPS private key and certificate for your web server. 4. To setup JCE with Java Keytool, follow the instructions in [Use Client SDK 5 to integrate AWS CloudHSM with Java
Keytool and Jarsigner](keystore-third-party-tools_5.md "keystore-third-party-tools_5.md").

After you complete these steps, go to [Step 2: Generate or
import a private key and SSL/TLS certificate](#third-offload-linux-jsse-gen "#third-offload-linux-jsse-gen").

#### Notes

- To use Security-Enhanced Linux (SELinux) and web servers, you must allow
  outbound TCP connections on port 2223, which is the port Client SDK 5 uses to
  communicate with the HSM.
- To create and activate a cluster and give an EC2 instance access to the cluster,
  complete the steps in [Getting Started with
  AWS CloudHSM](getting-started.md "getting-started.md"). This section offers step-by-step instructions for creating an
  active cluster with one HSM and an Amazon EC2 client instance. You can use this client instance as your web server.
- To avoid disabling client key durability, add more than one HSM to your cluster.
  For more information, see [Adding an HSM to an AWS CloudHSM cluster](add-hsm.md "add-hsm.md").
- To connect to your client instance, you can use SSH or PuTTY. For more
  information, see [Connecting
  to Your Linux Instance Using SSH](../../../AWSEC2/latest/UserGuide/AccessingInstancesLinux.md "../../../AWSEC2/latest/UserGuide/AccessingInstancesLinux.md") or [Connecting to Your Linux Instance from Windows Using PuTTY](../../../AWSEC2/latest/UserGuide/putty.md "../../../AWSEC2/latest/UserGuide/putty.md") in the Amazon EC2
  documentation.

## Step 2: Generate or

import a private key and SSL/TLS certificate

To enable HTTPS, your Tomcat web server application needs a private key and a corresponding SSL/TLS certificate.
To use web server SSL/TLS offload with AWS CloudHSM, you must store the private key in an HSM in your AWS CloudHSM cluster.

###### Note

If you don't yet have a private key and a corresponding certificate, generate a private key in an HSM.
You use the private key to create a certificate signing request (CSR), which you use to create the SSL/TLS certificate.

You create a local AWS CloudHSM KeyStore file that contains a reference to your private key on the HSM and the associated certificate.
Your web server uses the AWS CloudHSM KeyStore file to identify the private key on the HSM during SSL/TLS offload.

###### Topics

- [Generate a private key](#jsse-ssl-offload-generate-private-key "#jsse-ssl-offload-generate-private-key")
- [Generate a self-signed certificate](#jsse-ssl-offload-generate-certificate "#jsse-ssl-offload-generate-certificate")

### Generate a private key

This section shows you how to generate a key pair using the KeyTool from JDK. Once you
have a key pair generated inside the HSM, you can export it as a KeyStore file, and generate the corresponding certificate.

Depending on your use case, you can either generate an RSA or an EC key pair. The following steps show how to generate an RSA key pair.

###### Use the `genkeypair` command in KeyTool to generate an RSA key pair

1. After replacing the `<VARIABLES>` below with your specific data, use the following command to generate a keystore file
   named `jsse_keystore.keystore`, which will have a reference of your private key on the HSM.

```
`$` `keytool -genkeypair -alias `<UNIQUE ALIAS FOR KEYS>` -keyalg `<KEY ALGORITHM>` -keysize `<KEY SIZE>` -sigalg `<SIGN ALGORITHM>` \
 -keystore `<PATH>`/`<JSSE KEYSTORE NAME>`.keystore -storetype CLOUDHSM \
 -dname CERT_DOMAIN_NAME \
 -J-classpath '-J'$JAVA_LIB'/*:/opt/cloudhsm/java/*:./*' \
 -provider "com.amazonaws.cloudhsm.jce.provider.CloudHsmProvider" \
 -providerpath "$CLOUDHSM_JCE_LOCATION" \
 -keypass `<KEY PASSWORD>` -storepass `<KEYSTORE PASSWORD>``
```

    * **`<PATH>`**: The path that you want to generate your keystore file.
    * **`<UNIQUE ALIAS FOR KEYS>`**: This is used to uniquely identify your key on the HSM. This alias will be set as the LABEL attribute for the key.
    * **`<KEY PASSWORD>`**: We store reference to your key in the local keystore file, and this password protects that local reference.
    * **`<KEYSTORE PASSWORD>`**: This is the password for your local keystore file.
    * **`<JSSE KEYSTORE NAME>`**: Name of the Keystore file.
    * **`<CERT DOMAIN NAME>`**: X.500 Distinguished name.
    * **`<KEY ALGORITHM>`**: Key algorithm to generate key pair (For example, RSA and EC).
    * **`<KEY SIZE>`**: Key size to generate key pair (for example, 2048, 3072, and 4096).
    * **`<SIGN ALGORITHM>`**: Key size to generate key pair (for example, SHA1withRSA, SHA224withRSA, SHA256withRSA, SHA384withRSA, and SHA512withRSA).

2. To confirm the command was successful, enter the following command and verify you have successfully generated an RSA key pair.

```
`$` `ls `<PATH>`/`<JSSE KEYSTORE NAME>`.keystore`
```

### Generate a self-signed certificate

Once you have generated a private key along with the keystore file, you can use this file to generate a certificate signing request (CSR) and certificate.

In a production environment, you typically use a certificate authority (CA) to create a certificate from a CSR. A CA is not necessary for a test environment.
If you do use a CA, send the CSR file to them and use signed SSL/TLS certificate that they provide you in your web server for HTTPS.

As an alternative to using a CA, you can use the KeyTool to create a self-signed certificate. Self-signed certificates are not trusted by browsers and should not be used in production environments. They can be used in test environments.

###### Warning

Self-signed certificates should be used in a test environment only. For a production environment, use a more secure method, such as a certificate authority to create a certificate.

###### Topics

###### Generate a certificate

1. Obtain a copy of your keystore file generated in an earlier step.
2. Run the following command to use the KeyTool to create a certificate signing request (CSR).

```
`$` `keytool -certreq -keyalg RSA -alias unique_alias_for_key -file certreq.csr \
 -keystore `<JSSE KEYSTORE NAME>`.keystore -storetype CLOUDHSM \
 -J-classpath '-J$JAVA_LIB/*:/opt/cloudhsm/java/*:./*' \
 -keypass `<KEY PASSWORD>` -storepass `<KEYSTORE PASSWORD>``
```

###### Note

The output file of the certificate signing request is `certreq.csr`.

###### Sign a certificate

- After replacing the `<VARIABLES>` below with your specific data, run the following command to sign your CSR with your private key on your HSM. This creates a self-signed certificate.

```
`$` `keytool -gencert -infile certreq.csr -outfile certificate.crt \
 -alias `<UNIQUE ALIAS FOR KEYS>` -keypass `<KEY_PASSWORD>` -storepass `<KEYSTORE_PASSWORD>` -sigalg SIG_ALG \
 -storetype CLOUDHSM -J-classpath '-J$JAVA_LIB/*:/opt/cloudhsm/java/*:./*' \
 -keystore jsse_keystore.keystore`
```

###### Note

`certificate.crt` is the signed certificate that uses the alias’s private key.

###### Import a certificate in Keystore

- After replacing the `<VARIABLES>` below with your specific data, run the following command to import a signed certificate as a trusted certificate. This step will store the certificate in the keystore entry identified by alias.

```
`$` `keytool -import -alias `<UNIQUE ALIAS FOR KEYS>` -keystore jsse_keystore.keystore \
 -file certificate.crt -storetype CLOUDHSM \
 -v -J-classpath '-J$JAVA_LIB/*:/opt/cloudhsm/java/*:./*' \
 -keypass `<KEY PASSWORD>` -storepass `<KEYSTORE_PASSWORD>``
```

###### Convert a certificate to a PEM

- Run following command to convert the signed certificate file (`.crt`) to a PEM. The PEM file will be used to send the request from the http client.

```
`$` `openssl x509 -inform der -in certificate.crt -out certificate.pem`
```

After you complete these steps, go to [Step 3: Configure the web server](#third-offload-linux-jsse-config "#third-offload-linux-jsse-config").

## Step 3: Configure the Tomcat web server

Update your web server software's configuration to use the HTTPS certificate and corresponding PEM file that you created in the previous step.
Remember to backup your existing certificates and keys before you start. This will finish setting up your Linux web server software for SSL/TLS offload with AWS CloudHSM. For more information, refer to the
[Apache Tomcat 9 Configuration Reference](https://tomcat.apache.org/tomcat-9.0-doc/config/http.html "https://tomcat.apache.org/tomcat-9.0-doc/config/http.html").

###### Stop the server

- After replacing the `<VARIABLES>` below with your specific data, run following command to stop Tomcat Server before updating configuration

```
`$` `/`<TOMCAT DIRECTORY>`/bin/shutdown.sh`
```

    + **`<TOMCAT DIRECTORY>`**: Your Tomcat installation directory.

###### Update the Tomcat classpath

1. Connect to your client instance.
2. Locate the Tomcat installation folder.
3. After replacing the `<VARIABLES>` below with your specific data, use the following command to add Java library and AWS CloudHSM Java path in Tomcat **classpath**, located in Tomcat/bin/catalina.sh file.

```
`$` `sed -i 's@CLASSPATH="$CLASSPATH""$CATALINA_HOME"\/bin\/bootstrap.jar@CLASSPATH="$CLASSPATH""$CATALINA_HOME"\/bin\/bootstrap.jar:'"
 `<JAVA LIBRARY>`"'\/*:\/opt\/cloudhsm\/java\/*:.\/*@' `<TOMCAT PATH>` /bin/catalina.sh`
```

    * **`<JAVA LIBRARY>`**: Java JRE Library location.
    * **`<TOMCAT PATH>`**: Tomcat installation folder.

###### Add an HTTPS connector in the server configuration.

1. Go to the Tomcat installation folder.
2. After replacing the `<VARIABLES>` below with your specific data, use the following command to add an HTTPS connector to use certificates generated in prerequisites:

```
`$` `sed -i '/<Connector port="8080"/i <Connector port=\"443\" maxThreads=\"200\" scheme=\"https\" secure=\"true\" SSLEnabled=\"true\" keystoreType=\"CLOUDHSM\" keystoreFile=\"
 `<CUSTOM DIRECTORY>`/`<JSSE KEYSTORE NAME>`.keystore\" keystorePass=\"`<KEYSTORE PASSWORD>`\" keyPass=\"`<KEY PASSWORD>`
 \" keyAlias=\"`<UNIQUE ALIAS FOR KEYS>`" clientAuth=\"false\" sslProtocol=\"TLS\"/>' `<TOMCAT PATH>`/conf/server.xml`
```

    * **`<CUSTOM DIRECTORY>`**: Directory where keystore file is located.
    * **`<JSSE KEYSTORE NAME>`**: Name of the Keystore file.
    * **`<KEYSTORE PASSWORD>`**: This is the password for your local keystore file.
    * **`<KEY PASSWORD>`**: We store reference to your key in the local keystore file, and this password protects that local reference.
    * **`<UNIQUE ALIAS FOR KEYS>`**: This is used to uniquely identify your key on the HSM. This alias will be set as the LABEL attribute for the key.
    * **`<TOMCAT PATH>`**: The path to your Tomcat folder.

###### Start Server

- After replacing the `<VARIABLES>` below with your specific data, use the following command to start Tomcat Server:

```
`$` `/`<TOMCAT DIRECTORY>`/bin/startup.sh`
```

###### Note

**`<TOMCAT DIRECTORY>`** is the name of your Tomcat installation directory.

After you update your web server configuration, go to [Step 4: Enable HTTPS traffic
and verify the certificate](#third-offload-linux-jsse-verify "#third-offload-linux-jsse-verify").

## Step 4: Enable HTTPS traffic

and verify the certificate

After you configure your web server for SSL/TLS offload with AWS CloudHSM, add your web server
instance to a security group that allows inbound HTTPS traffic. This allows clients, such as web
browsers, to establish an HTTPS connection with your web server. Then make an HTTPS connection
to your web server and verify that it's using the certificate that you configured for
SSL/TLS offload with AWS CloudHSM.

###### Topics

- [Enable inbound HTTPS
  connections](#jsse-linux-add-security-group "#jsse-linux-add-security-group")
- [Verify that HTTPS uses the
  certificate that you configured](#jsse-linux-verify-https-connection "#jsse-linux-verify-https-connection")

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

To add a load balancer, see [Add a load balancer with ELB for AWS CloudHSM(optional)](third-offload-add-lb.md "third-offload-add-lb.md").
