# Connect the client SDK to the AWS CloudHSM cluster

To connect to the cluster with either Client SDK 5 or Client SDK 3, you must first do two
things:

- Have an issuing certificate in place on the EC2 instance
- Bootstrap the Client SDK to the cluster

## Place the issuing certificate on each EC2 instance

You create the issuing certificate when you initialize the cluster. Copy the issuing
certificate to the default location for the platform on each EC2 instance that connects to
the cluster.

Linux

```
/opt/cloudhsm/etc/`customerCA.crt`
```

Windows

```
C:\ProgramData\Amazon\CloudHSM\`customerCA.crt`
```

## Specify the location of the issuing certificate

With Client SDK 5, you use the configure tool to specify the location of the issuing
certificate.

PKCS #11 library

###### To place the issuing certificate on Linux for Client SDK 5

- Use the configure tool to specify a location for the issuing certificate.

```
``$` sudo /opt/cloudhsm/bin/configure-pkcs11 --hsm-ca-cert `<customerCA certificate file>``
```

###### To place the issuing certificate on Windows for Client SDK 5

- Use the configure tool to specify a location for the issuing certificate.

```
`PS C:\>` `& "C:\Program Files\Amazon\CloudHSM\bin\configure-pkcs11.exe" --hsm-ca-cert `<customerCA certificate file>``
```

OpenSSL Dynamic Engine

###### To place the issuing certificate on Linux for Client SDK 5

- Use the configure tool to specify a location for the issuing certificate.

```
``$` sudo /opt/cloudhsm/bin/configure-dyn --hsm-ca-cert `<customerCA certificate file>``
```

OpenSSL Dynamic Engine Provider

###### To place the issuing certificate on Linux for Client SDK 5

- Use the configure tool to specify a location for the issuing certificate.

```
``$` sudo /opt/cloudhsm/bin/configure-openssl-provider --hsm-ca-cert `<customerCA certificate file>``
```

Key Storage Provider (KSP)

###### To place the issuing certificate on Windows for Client SDK 5

- Use the configure tool to specify a location for the issuing certificate.

```
`PS C:\>` `& "C:\Program Files\Amazon\CloudHSM\bin\configure-ksp.exe" --hsm-ca-cert `<customerCA certificate file>``
```

JCE provider

###### To place the issuing certificate on Linux for Client SDK 5

- Use the configure tool to specify a location for the issuing certificate.

```
``$` sudo /opt/cloudhsm/bin/configure-jce --hsm-ca-cert `<customerCA certificate file>``
```

###### To place the issuing certificate on Windows for Client SDK 5

- Use the configure tool to specify a location for the issuing certificate.

```
`PS C:\>` `& "C:\Program Files\Amazon\CloudHSM\bin\configure-jce.exe" --hsm-ca-cert `<customerCA certificate file>``
```

CloudHSM CLI

###### To place the issuing certificate on Linux for Client SDK 5

- Use the configure tool to specify a location for the issuing certificate.

```
``$` sudo /opt/cloudhsm/bin/configure-cli --hsm-ca-cert `<customerCA certificate file>``
```

###### To place the issuing certificate on Windows for Client SDK 5

- Use the configure tool to specify a location for the issuing certificate.

```
`PS C:\>` `& "C:\Program Files\Amazon\CloudHSM\bin\configure-cli.exe" --hsm-ca-cert `<customerCA certificate file>``
```

For more information, see [Configure Tool](configure-sdk-5.md "configure-sdk-5.md").

For more information about initializing the cluster or creating and signing the
certificate, see [Initialize the Cluster](initialize-cluster.md#initialize "initialize-cluster.md#initialize").

## Bootstrap the Client SDK

The bootstrap process is different depending on the version of the Client SDK you're
using, but you must have the IP address of one of the hardware security modules (HSM) in the
cluster. You can use the IP address of any HSM attached to your cluster. After the Client
SDK connects, it retrieves the IP addresses of any additional HSMs and performs load
balancing and client-side key synchronization operations.

###### To get an IP address for an HSM (console)

1. Open the AWS CloudHSM console at
   [https://console.aws.amazon.com/cloudhsm/home](https://console.aws.amazon.com/cloudhsm/home "https://console.aws.amazon.com/cloudhsm/home").
2. To change the AWS Region, use the Region selector in the upper-right corner of the
   page.
3. To open the cluster detail page, in the cluster table, choose the cluster ID.
4. To get the IP address, go to the HSMs tab. For IPv4 clusters, choose an address listed under **ENI IPv4 address**. For dual-stack clusters use either the ENI IPv4 or the **ENI IPv6 address**.

###### To get an IP address for an HSM (AWS CLI)

- Get the IP address of an HSM by using the **[describe-clusters](../../../cli/latest/reference/cloudhsmv2/describe-clusters.md "../../../cli/latest/reference/cloudhsmv2/describe-clusters.md")** command from the AWS CLI. In the output from the command,
  the IP address of the HSMs are the values of `EniIp` and `EniIpV6` (if it is a dual-stack cluster).

```
`$` `aws cloudhsmv2 describe-clusters`
`{
 "Clusters": [
 { ... }
 "Hsms": [
 {
...
 "EniIp": "10.0.0.9",
...
 },
 {
...
 "EniIp": "10.0.1.6",
 "EniIpV6": "2600:113f:404:be09:310e:ed34:3412:f733",
...`
```

For more information about bootstrapping, see [Configure
Tool](configure-tool.md "configure-tool.md").

PKCS #11 library

###### To bootstrap a Linux EC2 instance for Client SDK 5

- Use the configure tool to specify the IP address of an HSM in your
  cluster.

```
`$` `sudo /opt/cloudhsm/bin/configure-pkcs11 -a `<HSM IP addresses>``
```

###### To bootstrap a Windows EC2 instance for Client SDK 5

- Use the configure tool to specify the IP address of an HSM in your
  cluster.

```
`PS C:\>` `& "C:\Program Files\Amazon\CloudHSM\bin\configure-pkcs11.exe" -a `<HSM IP addresses>``
```

OpenSSL Dynamic Engine

###### To bootstrap a Linux EC2 instance for Client SDK 5

- Use the configure tool to specify the IP address of an HSM in your
  cluster.

```
`$` `sudo /opt/cloudhsm/bin/configure-dyn -a `<HSM IP addresses>``
```

OpenSSL Dynamic Engine Provider

###### To bootstrap a Linux EC2 instance for Client SDK 5

- Use the configure tool to specify the IP address of an HSM in your
  cluster.

```
`$` `sudo /opt/cloudhsm/bin/configure-openssl-provider -a `<HSM IP addresses>``
```

Key Storage Provider (KSP)

###### To bootstrap a Windows EC2 instance for Client SDK 5

- Use the configure tool to specify the IP address of an HSM in your
  cluster.

```
`PS C:\>` `& "C:\Program Files\Amazon\CloudHSM\bin\configure-ksp.exe" -a `<HSM IP addresses>``
```

JCE provider

###### To bootstrap a Linux EC2 instance for Client SDK 5

- Use the configure tool to specify the IP address of an HSM in your
  cluster.

```
`$` `sudo /opt/cloudhsm/bin/configure-jce -a `<HSM IP addresses>``
```

###### To bootstrap a Windows EC2 instance for Client SDK 5

- Use the configure tool to specify the IP address of an HSM in your
  cluster.

```
`PS C:\>` `& "C:\Program Files\Amazon\CloudHSM\bin\configure-jce.exe" -a `<HSM IP addresses>``
```

CloudHSM CLI

###### To bootstrap a Linux EC2 instance for Client SDK 5

- Use the configure tool to specify the IP address of the HSM(s) in your
  cluster.

```
`$` `sudo /opt/cloudhsm/bin/configure-cli -a `<The ENI IPv4 / IPv6 addresses of the HSMs>``
```

###### To bootstrap a Windows EC2 instance for Client SDK 5

- Use the configure tool to specify the IP address of the HSM(s) in your
  cluster.

```
`PS C:\>` `& "C:\Program Files\Amazon\CloudHSM\bin\configure-cli.exe" -a `<The ENI IPv4 / IPv6 addresses of the HSMs>``
```

###### Note

you can use the `–-cluster-id` parameter in place of `-a <HSM_IP_ADDRESSES>`. To see requirements for using `–-cluster-id`, see [AWS CloudHSM Client SDK 5 configure tool](configure-sdk-5.md "configure-sdk-5.md").

###### To bootstrap a Linux EC2 instance for Client SDK 3

- Use **configure** to specify the IP address of an HSM in your
  cluster.

```
`sudo /opt/cloudhsm/bin/configure -a `<IP address>``
```

###### To bootstrap a Windows EC2 instance for Client SDK 3

- Use **configure** to specify the IP address of an HSM in your
  cluster.

```
`PS C:\>` `& "C:\Program Files\Amazon\CloudHSM\configure.exe" -a `<HSM IP address>``
```

For more information about configure, see [AWS CloudHSM configure tool](configure-tool.md "configure-tool.md").
