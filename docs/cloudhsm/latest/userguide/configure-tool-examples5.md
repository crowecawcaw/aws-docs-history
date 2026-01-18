# AWS CloudHSM Client SDK 5 configuration examples

These examples show how to use the configure tool for AWS CloudHSM Client SDK 5.

This example uses the `-a` parameter to update the HSM data for
Client SDK 5. To use the `-a` parameter, you must have the IP address
for one of the HSMs in your cluster.

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

For more information about the `-a` parameter, see [AWS CloudHSM Client SDK 5 configuration parameters](configure-tool-params5.md "configure-tool-params5.md").

This example uses the `cluster-id` parameter to bootstrap Client SDK 5 by making
a `DescribeClusters` call.

PKCS #11 library

###### To bootstrap a Linux EC2 instance for Client SDK 5 with `cluster-id`

- Use the cluster ID `cluster-1234567` to specify the IP address of an HSM in your
  cluster.

```
``$` sudo /opt/cloudhsm/bin/configure-pkcs11 --cluster-id `<cluster-1234567>``
```

###### To bootstrap a Windows EC2 instance for Client SDK 5 with `cluster-id`

- Use the cluster ID `cluster-1234567` to specify the IP address of an HSM in your
  cluster.

```
`PS C:\>` `& "C:\Program Files\Amazon\CloudHSM\bin\configure-pkcs11.exe" --cluster-id `<cluster-1234567>``
```

OpenSSL Dynamic Engine

###### To bootstrap a Linux EC2 instance for Client SDK 5 with `cluster-id`

- Use the cluster ID `cluster-1234567` to specify the IP address of an HSM in your
  cluster.

```
``$` sudo /opt/cloudhsm/bin/configure-dyn --cluster-id `<cluster-1234567>``
```

Key Storage Provider (KSP)

###### To bootstrap a Windows EC2 instance for Client SDK 5 with `cluster-id`

- Use the cluster ID `cluster-1234567` to specify the IP address of an HSM in your
  cluster.

```
`PS C:\>` `& "C:\Program Files\Amazon\CloudHSM\bin\configure-ksp.exe" --cluster-id `<cluster-1234567>``
```

JCE provider

###### To bootstrap a Linux EC2 instance for Client SDK 5 with `cluster-id`

- Use the cluster ID `cluster-1234567` to specify the IP address of an HSM in your
  cluster.

```
``$` sudo /opt/cloudhsm/bin/configure-jce --cluster-id `<cluster-1234567>``
```

###### To bootstrap a Windows EC2 instance for Client SDK 5 with `cluster-id`

- Use the cluster ID `cluster-1234567` to specify the IP address of an HSM in your
  cluster.

```
`PS C:\>` `& "C:\Program Files\Amazon\CloudHSM\bin\configure-jce.exe" --cluster-id `<cluster-1234567>``
```

CloudHSM CLI

###### To bootstrap a Linux EC2 instance for Client SDK 5 with `cluster-id`

- Use the cluster ID `cluster-1234567` to specify the IP address of an HSM in your
  cluster.

```
``$` sudo /opt/cloudhsm/bin/configure-cli --cluster-id `<cluster-1234567>``
```

###### To bootstrap a Windows EC2 instance for Client SDK 5 with `cluster-id`

- Use the cluster ID `cluster-1234567` to specify the IP address of an HSM in your
  cluster.

```
`PS C:\>` `& "C:\Program Files\Amazon\CloudHSM\bin\configure-cli.exe" --cluster-id `<cluster-1234567>``
```

You can use the `--region` and `--endpoint` parameters in combination with
the `cluster-id` parameter to specify how the system makes the
`DescribeClusters` call. For instance, if the region of the cluster is different than
the one configured as your AWS CLI default, you should use the `--region` parameter to
use that region. Additionally, you have the ability to specify the AWS CloudHSM API endpoint to use for
the call, which might be necessary for various network setups, such as using VPC interface
endpoints that don’t use the default DNS hostname for AWS CloudHSM.

PKCS #11 library

###### To bootstrap a Linux EC2 instance with a custom endpoint and region

- Use the configure tool to specify the IP address of an HSM in your
  cluster with a custom region and endpoint.

```
`$` `sudo /opt/cloudhsm/bin/configure-pkcs11 --cluster-id `<cluster-1234567>` --region `<us-east-1>` --endpoint `<https://cloudhsmv2.us-east-1.amazonaws.com>``
```

###### To bootstrap a Windows EC2 instance with a endpoint and region

- Use the configure tool to specify the IP address of an HSM in your
  cluster with a custom region and endpoint.

```
`PS C:\>` `& "C:\Program Files\Amazon\CloudHSM\bin\configure-pkcs11.exe" --cluster-id `<cluster-1234567>`--region `<us-east-1>` --endpoint `<https://cloudhsmv2.us-east-1.amazonaws.com>``
```

OpenSSL Dynamic Engine

###### To bootstrap a Linux EC2 instance with a custom endpoint and region

- Use the configure tool to specify the IP address of an HSM in your
  cluster with a custom region and endpoint.

```
`$` `sudo /opt/cloudhsm/bin/configure-dyn --cluster-id `<cluster-1234567>` --region `<us-east-1>` --endpoint `<https://cloudhsmv2.us-east-1.amazonaws.com>``
```

Key Storage Provider (KSP)

###### To bootstrap a Windows EC2 instance with a endpoint and region

- Use the configure tool to specify the IP address of an HSM in your
  cluster with a custom region and endpoint.

```
`PS C:\>` `& "C:\Program Files\Amazon\CloudHSM\bin\configure-ksp.exe" --cluster-id `<cluster-1234567>` --region `<us-east-1>` --endpoint `<https://cloudhsmv2.us-east-1.amazonaws.com>``
```

JCE provider

###### To bootstrap a Linux EC2 instance with a custom endpoint and region

- Use the configure tool to specify the IP address of an HSM in your
  cluster with a custom region and endpoint.

```
`$` `sudo /opt/cloudhsm/bin/configure-jce --cluster-id `<cluster-1234567>` --region `<us-east-1>` --endpoint `<https://cloudhsmv2.us-east-1.amazonaws.com>``
```

###### To bootstrap a Windows EC2 instance with a endpoint and region

- Use the configure tool to specify the IP address of an HSM in your
  cluster with a custom region and endpoint.

```
`PS C:\>` `& "C:\Program Files\Amazon\CloudHSM\bin\configure-jce.exe" --cluster-id `<cluster-1234567>` --region `<us-east-1>` --endpoint `<https://cloudhsmv2.us-east-1.amazonaws.com>``
```

CloudHSM CLI

###### To bootstrap a Linux EC2 instance with a custom endpoint and region

- Use the configure tool to specify the IP address of an HSM in your
  cluster with a custom region and endpoint.

```
`$` `sudo /opt/cloudhsm/bin/configure-cli --cluster-id `<cluster-1234567>` --region `<us-east-1>` --endpoint `<https://cloudhsmv2.us-east-1.amazonaws.com>``
```

###### To bootstrap a Windows EC2 instance with a endpoint and region

- Use the configure tool to specify the IP address of an HSM in your
  cluster with a custom region and endpoint.

```
`PS C:\>` `& "C:\Program Files\Amazon\CloudHSM\bin\configure-cli.exe" --cluster-id `<cluster-1234567>` --region `<us-east-1>` --endpoint `<https://cloudhsmv2.us-east-1.amazonaws.com>``
```

For more information about the `--cluster-id`, `--region`,
and `--endpoint` parameters, see [AWS CloudHSM Client SDK 5 configuration parameters](configure-tool-params5.md "configure-tool-params5.md").

This examples shows how to use the `--client-cert-hsm-tls-file` and `--client-key-hsm-tls-file` parameters to reconfigure
SSL by specifying a custom key and SSL certificate for AWS CloudHSM

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

For more information about the `--client-cert-hsm-tls-file` and
`--client-key-hsm-tls-file` parameters, see [AWS CloudHSM Client SDK 5 configuration parameters](configure-tool-params5.md "configure-tool-params5.md").

This example uses the `--disable-key-availability-check` parameter to
disable client key durability settings. To run a cluster with a single HSM, you must
disable client key durability settings.

PKCS #11 library

###### To disable client key durability for Client SDK 5 on Linux

- Use the configure tool to disable client key durability settings.

```
`$` `sudo /opt/cloudhsm/bin/configure-pkcs11 --disable-key-availability-check`
```

###### To disable client key durability for Client SDK 5 on Windows

- Use the configure tool to disable client key durability settings.

```
`PS C:\>` `& "C:\Program Files\Amazon\CloudHSM\bin\configure-pkcs11.exe" --disable-key-availability-check`
```

OpenSSL Dynamic Engine

###### To disable client key durability for Client SDK 5 on Linux

- Use the configure tool to disable client key durability settings.

```
`$` `sudo /opt/cloudhsm/bin/configure-dyn --disable-key-availability-check`
```

OpenSSL Dynamic Engine Provider

###### To disable client key durability for Client SDK 5 on Linux

- Use the configure tool to disable client key durability settings.

```
`$` `sudo /opt/cloudhsm/bin/configure-openssl-provider --disable-key-availability-check`
```

Key Storage Provider (KSP)

###### To disable client key durability for Client SDK 5 on Windows

- Use the configure tool to disable client key durability settings.

```
`PS C:\>` `& "C:\Program Files\Amazon\CloudHSM\bin\configure-ksp.exe" --disable-key-availability-check`
```

JCE provider

###### To disable client key durability for Client SDK 5 on Linux

- Use the configure tool to disable client key durability settings.

```
`$` `sudo /opt/cloudhsm/bin/configure-jce --disable-key-availability-check`
```

###### To disable client key durability for Client SDK 5 on Windows

- Use the configure tool to disable client key durability settings.

```
`PS C:\>` `& "C:\Program Files\Amazon\CloudHSM\bin\configure-jce.exe" --disable-key-availability-check`
```

CloudHSM CLI

###### To disable client key durability for Client SDK 5 on Linux

- Use the configure tool to disable client key durability settings.

```
`$` `sudo /opt/cloudhsm/bin/configure-cli --disable-key-availability-check`
```

###### To disable client key durability for Client SDK 5 on Windows

- Use the configure tool to disable client key durability settings.

```
`PS C:\>` `& "C:\Program Files\Amazon\CloudHSM\bin\configure-cli.exe" --disable-key-availability-check`
```

For more information about the `--disable-key-availability-check`
parameter, see [AWS CloudHSM Client SDK 5 configuration parameters](configure-tool-params5.md "configure-tool-params5.md").

Client SDK 5 uses the `log-file`, `log-level`,
`log-rotation`, and `log-type` parameters to manage logging.

###### Note

To configure your SDK for serverless environments such as AWS Fargate or AWS Lambda, we recommend you configure your AWS CloudHSM log type to `term`.
The client logs will be output to `stderr` and captured in the CloudWatch Logs log group configured for that environment.

PKCS #11 library

###### Default logging location

- If you do not specify a location for the file, the system writes logs to the following default location:

Linux

```
/opt/cloudhsm/run/cloudhsm-pkcs11.log
```

Windows

```
C:\Program Files\Amazon\CloudHSM\cloudhsm-pkcs11.log
```

###### To configure the logging level and leave other logging options set to default

- ```
  `$` `sudo /opt/cloudhsm/bin/configure-pkcs11 --log-level info`
  ```

````

###### To configure file logging options

* ```
`$` `sudo /opt/cloudhsm/bin/configure-pkcs11 --log-type file --log-file `<file name with path>` --log-rotation daily --log-level info`
````

###### To configure terminal logging options

- ```
  `$` `sudo /opt/cloudhsm/bin/configure-pkcs11 --log-type term --log-level info`
  ```

```


OpenSSL Dynamic Engine
###### Default logging location

* If you do not specify a location for the file, the system writes logs to the following default location:


Linux



```

stderr

````

###### To configure the logging level and leave other logging options set to default

* ```
`$` `sudo /opt/cloudhsm/bin/configure-dyn --log-level info`
````

###### To configure file logging options

- ```
  `$` `sudo /opt/cloudhsm/bin/configure-dyn --log-type file --log-file `<file name with path>` --log-rotation daily --log-level info`
  ```

````

###### To configure terminal logging options

* ```
`$` `sudo /opt/cloudhsm/bin/configure-dyn --log-type term --log-level info`
````

OpenSSL Dynamic Engine Provider

###### Default logging location

- If you do not specify a location for the file, the system writes logs to the following default location:

Linux

```
stderr
```

###### To configure the logging level and leave other logging options set to default

- ```
  `$` `sudo /opt/cloudhsm/bin/configure-openssl-provider --log-level info`
  ```

````

###### To configure file logging options

* ```
`$` `sudo /opt/cloudhsm/bin/configure-openssl-provider --log-type file --log-file `<file name with path>` --log-rotation daily --log-level info`
````

###### To configure terminal logging options

- ```
  `$` `sudo /opt/cloudhsm/bin/configure-openssl-provider --log-type term --log-level info`
  ```

```


Key Storage Provider (KSP)
###### Default logging location

* If you do not specify a location for the file, the system writes logs to the following default location:


Windows



```

C:\Program Files\Amazon\CloudHSM\cloudhsm-ksp.log

````

###### To configure the logging level and leave other logging options set to default

* ```
`PS C:\>` `& "C:\Program Files\Amazon\CloudHSM\bin\configure-ksp.exe" --log-level info`
````

###### To configure file logging options

- ```
  `PS C:\>` `& "C:\Program Files\Amazon\CloudHSM\bin\configure-ksp.exe" --log-type file --log-file `<file name with path>` --log-rotation daily --log-level info`
  ```

````

###### To configure terminal logging options

* ```
`PS C:\>` `& "C:\Program Files\Amazon\CloudHSM\bin\configure-ksp.exe" --log-type term --log-level info`
````

JCE provider

###### Default logging location

- If you do not specify a location for the file, the system writes logs to the following default location:

Linux

```
/opt/cloudhsm/run/cloudhsm-jce.log
```

Windows

```
C:\Program Files\Amazon\CloudHSM\cloudhsm-jce.log
```

###### To configure the logging level and leave other logging options set to default

- ```
  `$` `sudo /opt/cloudhsm/bin/configure-jce --log-level info`
  ```

````

###### To configure file logging options

* ```
`$` `sudo /opt/cloudhsm/bin/configure-jce --log-type file --log-file `<file name with path>` --log-rotation daily --log-level info`
````

###### To configure terminal logging options

- ```
  `$` `sudo /opt/cloudhsm/bin/configure-jce --log-type term --log-level info`
  ```

```


CloudHSM CLI
###### Default logging location

* If you do not specify a location for the file, the system writes logs to the following default location:


Linux



```

/opt/cloudhsm/run/cloudhsm-cli.log

```

Windows



```

C:\Program Files\Amazon\CloudHSM\cloudhsm-cli.log

````

###### To configure the logging level and leave other logging options set to default

* ```
`$` `sudo /opt/cloudhsm/bin/configure-cli --log-level info`
````

###### To configure file logging options

- ```
  `$` `sudo /opt/cloudhsm/bin/configure-cli --log-type file --log-file `<file name with path>` --log-rotation daily --log-level info`
  ```

````

###### To configure terminal logging options

* ```
`$` `sudo /opt/cloudhsm/bin/configure-cli --log-type term --log-level info`
````

For more information about the `log-file`, `log-level`,
`log-rotation`,and `log-type` parameters, see [AWS CloudHSM Client SDK 5 configuration parameters](configure-tool-params5.md "configure-tool-params5.md").

This example uses the `--hsm-ca-cert` parameter to update the location of the
issuing certificate for Client SDK 5.

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

For more information about the `--hsm-ca-cert` parameter, see [AWS CloudHSM Client SDK 5 configuration parameters](configure-tool-params5.md "configure-tool-params5.md").
