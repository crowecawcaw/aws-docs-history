# Manually configure trust stores for HTTPS proxy support in AWS IoT SiteWise Edge

When configuring AWS IoT SiteWise Edge components to connect through an HTTPS proxy, add the
proxy server's certificate to the appropriate trust stores. SiteWise Edge uses multiple
trust stores to secure communications. There are three trust stores and your use of
them depends upon the SiteWise Edge component type in your gateway implementation.

Trust stores are automatically updated during the installation process when proxy
settings are provided.

- [Configure
  an AWS IoT Greengrass Core component trust store](#manage-trust-stores-proxy_greengrass-core-components "#manage-trust-stores-proxy_greengrass-core-components")
  – The AWS IoT Greengrass root CA certificate is included in the trust stores to
  verify the authenticity of AWS services.

This trust store helps AWS IoT Greengrass components securely communicate with AWS
services through the proxy while verifying the authenticity of those
services.

- [Configure a
  Java-based component trust store](#manage-trust-stores-proxy_java-based-components "#manage-trust-stores-proxy_java-based-components")
  – The Java KeyStore (JKS) is the main trust store used by Java-based
  components for SSL/TLS connections.

Java applications rely on the JKS to establish secure connections. For
example, if you're using the IoT SiteWise publisher or IoT SiteWise OPC UA collector,
which are Java-based, you'll need to configure this trust store. This
ensures these components can securely communicate through the HTTPS proxy
when sending data to the cloud or collecting data from OPC UA
servers.

- [System-level
  component trust store configuration](#manage-trust-stores-proxy_system-level-components "#manage-trust-stores-proxy_system-level-components")
  – When using HTTPS proxies, their certificates must be added to the
  appropriate trust stores to enable secure connections.

When using HTTPS proxies, their certificates must be added to the
appropriate trust stores to enable secure connections. This is necessary
because system-level components, often written in languages like Rust or Go,
rely on the system's trust store rather than Java's JKS. For example, if
you're using system utilities that need to communicate through the proxy
(like for software updates or time synchronization), you'll need to
configure the system-level trust store. This ensures these components and
utilities can establish secure connections through the proxy.

## Configure

an AWS IoT Greengrass Core component trust store

For AWS IoT Greengrass Core functions that use Amazon's root CA:

1. Locate the certificate file at
   `/greengrass/v2/AmazonRootCA1.pem`
2. Append the HTTPS proxy root certificate (self-signed) to this
   file.

```

-----BEGIN CERTIFICATE-----
MIIEFTCCAv2gAwIQWgIVAMHSAzWG/5YVRYtRQOxXUTEpHuEmApzGCSqGSIb3DQEK
\nCwUAhuL9MQswCQwJVUzEPMAVUzEYMBYGA1UECgwP1hem9uLmNvbSBJbmMuMRww
... `content of proxy CA certificate` ...
+vHIRlt0e5JAm5\noTIZGoFbK82A0/nO7f/t5PSIDAim9V3Gc3pSXxCCAQoFYnui
GaPUlGk1gCE84a0X\n7Rp/lND/PuMZ/s8YjlkY2NmYmNjMCAXDTE5MTEyN2cM216
gJMIADggEPADf2/m45hzEXAMPLE=
-----END CERTIFICATE-----

-----BEGIN CERTIFICATE-----
MIIDQTCCAimgF6AwIBAgITBmyfz/5mjAo54vB4ikPmljZKyjANJmApzyMZFo6qBg
ADA5MQswCQYDVQQGEwJVUzEPMA0tMVT8QtPHRh8jrdkGA1UEChMGDV3QQDExBBKW
... `content of root CA certificate` ...
o/ufQJQWUCyziar1hem9uMRkwFwYVPSHCb2XV4cdFyQzR1KldZwgJcIQ6XUDgHaa
5MsI+yMRQ+hDaXJiobldXgjUka642M4UwtBV8oK2xJNDd2ZhwLnoQdeXeGADKkpy
rqXRfKoQnoZsG4q5WTP46EXAMPLE
-----END CERTIFICATE-----

```

### Configure

HTTPS proxy on an established gateway

You can add proxy support to an established gateway by connecting to port
443 instead of port 8883. For more information on using a proxy server, see
[Connect on port 443 or through a network proxy](../../../greengrass/v2/developerguide/configure-greengrass-core-v2.md#configure-alpn-network-proxy "../../../greengrass/v2/developerguide/configure-greengrass-core-v2.md#configure-alpn-network-proxy") in the
_AWS IoT Greengrass Version 2 Developer Guide_. If you create a new gateway, you
can set the proxy configuration during gateway installation. For more
information, see [Configure proxy settings during
AWS IoT SiteWise Edge gateway installation](manage-trust-stores-proxy_config.md "manage-trust-stores-proxy_config.md").

When you use an HTTPS proxy with AWS IoT Greengrass on SiteWise Edge, the software
automatically chooses between HTTP and HTTPS for proxy connections based on
the provided URL.

###### Important

Update all required trust stores before attempting to connect through
an HTTPS proxy.

## Configure a

Java-based component trust store

For IoT SiteWise publisher, IoT SiteWise OPC UA collector, and Java services in the data
processing pack, the default Java trust store location is
`$JAVA_HOME/jre/lib/security/cacerts`

###### To add a certificate

1. Create a file to store the proxy server's certificate, such as
   `proxy.crt`.

###### Note

Create the file ahead of time using the proxy server's
certificate. 2. Add the file to Java's trust store using the following command:

```
sudo keytool -import -alias proxyCert -keystore /usr/lib/jvm/java-11-openjdk-amd64/lib/security/cacerts -file proxy.crt
```

3. When prompted, use the default password: `changeit`

## System-level

component trust store configuration

For components written in Rust, Go, and other languages that use the system
trust store:

Linux
Linux systems: Add certificates to
`/etc/ssl/certs/ca-certificates.crt`

Windows
Microsoft Windows systems: To configure the trust
store, follow the [Certificate Store](https://learn.microsoft.com/en-us/windows-hardware/drivers/install/certificate-stores "https://learn.microsoft.com/en-us/windows-hardware/drivers/install/certificate-stores") procedure in the _Microsoft
Ignite_ documentation.

Windows offers multiple certificate stores, including separate
stores for User and Computer scopes, each with several sub-stores.
For most SiteWise Edge setups, we recommend adding certificates to the
`COMPUTER | Trusted Root Certification Authorities`
store. However, depending on your specific configuration and
security requirements, you might need to use a different
store.

## Troubleshooting trust store issues

For more information on resolving trust store issues related to a SiteWise Edge
gateway, see [Trust store issues](troubleshooting-gateway.md#troubleshoot-trust-stores "troubleshooting-gateway.md#troubleshoot-trust-stores").
