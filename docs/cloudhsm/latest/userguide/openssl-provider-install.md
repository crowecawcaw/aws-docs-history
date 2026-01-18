# Install the OpenSSL Provider for AWS CloudHSM

Client SDK 5

Use the following sections to install the OpenSSL Provider for AWS CloudHSM Client SDK 5.

###### Note

To run a single HSM cluster with Client SDK 5, you must first manage client key durability settings by setting `disable_key_availability_check` to `True`. For more information, see [Key Synchronization](working-client-sync.md#client-sync-sdk8 "working-client-sync.md#client-sync-sdk8") and [Client SDK 5 Configure Tool](configure-sdk-5.md "configure-sdk-5.md").

## Requirements

The OpenSSL Provider requires **hsm2m.medium** cluster types and minimum CloudHSM Client SDK version 5.17.0 or later.

## Install the OpenSSL Provider

###### To install the OpenSSL Provider

1. Use the following commands to download and install the OpenSSL Provider.

Amazon Linux 2023
Install the OpenSSL Provider for Amazon Linux 2023 on x86_64 architecture:

```
`$` `wget https://s3.amazonaws.com/cloudhsmv2-software/CloudHsmClient/Amzn2023/cloudhsm-openssl-provider-latest.amzn2023.x86_64.rpm`
```

```
`$` `sudo yum install ./cloudhsm-openssl-provider-latest.amzn2023.x86_64.rpm`
```

Install the OpenSSL Provider for Amazon Linux 2023 on ARM64 architecture:

```
`$` `wget https://s3.amazonaws.com/cloudhsmv2-software/CloudHsmClient/Amzn2023/cloudhsm-openssl-provider-latest.amzn2023.aarch64.rpm`
```

```
`$` `sudo yum install ./cloudhsm-openssl-provider-latest.amzn2023.aarch64.rpm`
```

RHEL 9 (9.2+)
Install the OpenSSL Provider for RHEL 9 on x86_64 architecture:

```
`$` `wget https://s3.amazonaws.com/cloudhsmv2-software/CloudHsmClient/EL9/cloudhsm-openssl-provider-latest.el9.x86_64.rpm`
```

```
`$` `sudo yum install ./cloudhsm-openssl-provider-latest.el9.x86_64.rpm`
```

Install the OpenSSL Provider for RHEL 9 on ARM64 architecture:

```
`$` `wget https://s3.amazonaws.com/cloudhsmv2-software/CloudHsmClient/EL9/cloudhsm-openssl-provider-latest.el9.aarch64.rpm`
```

```
`$` `sudo yum install ./cloudhsm-openssl-provider-latest.el9.aarch64.rpm`
```

RHEL 10 (10.0+)
Install the OpenSSL Provider for RHEL 10 on x86_64 architecture:

```
`$` `wget https://s3.amazonaws.com/cloudhsmv2-software/CloudHsmClient/EL10/cloudhsm-openssl-provider-latest.el10.x86_64.rpm`
```

```
`$` `sudo yum install ./cloudhsm-openssl-provider-latest.el10.x86_64.rpm`
```

Install the OpenSSL Provider for RHEL 10 on ARM64 architecture:

```
`$` `wget https://s3.amazonaws.com/cloudhsmv2-software/CloudHsmClient/EL10/cloudhsm-openssl-provider-latest.el10.aarch64.rpm`
```

```
`$` `sudo yum install ./cloudhsm-openssl-provider-latest.el10.aarch64.rpm`
```

Ubuntu 24.04
Install the OpenSSL Provider for Ubuntu 24.04 on x86_64 architecture:

```
`$` `wget https://s3.amazonaws.com/cloudhsmv2-software/CloudHsmClient/Noble/cloudhsm-openssl-provider_latest_amd64.deb`
```

```
`$` `sudo dpkg -i ./cloudhsm-openssl-provider_latest_amd64.deb`
```

Install the OpenSSL Provider for Ubuntu 24.04 on ARM64 architecture:

```
`$` `wget https://s3.amazonaws.com/cloudhsmv2-software/CloudHsmClient/Noble/cloudhsm-openssl-provider_latest_arm64.deb`
```

```
`$` `sudo dpkg -i ./cloudhsm-openssl-provider_latest_arm64.deb`
```

You have installed the shared library for the OpenSSL Provider at
`/opt/cloudhsm/lib/licloudhsm_openssl_provider.so`. 2. Bootstrap Client SDK 5. For more information about bootstrapping, see [Bootstrap the Client SDK](cluster-connect.md#connect-how-to "cluster-connect.md#connect-how-to"). 3. Set the `CLOUDHSM_PIN` environment variable with your crypto user (CU) credentials:

```
`$` `export CLOUDHSM_PIN=`<username>`:`<password>``
```

4. Connect your installation of OpenSSL Provider to the cluster. For more information, see [Connect to the Cluster](cluster-connect.md "cluster-connect.md").

## Verify the installation

Verify that the OpenSSL Provider is installed correctly:

```
`$` `CLOUDHSM_PIN=`<username>`:`<password>` openssl list -providers -provider cloudhsm`
```

You should see output similar to:

```
Providers:
  cloudhsm
    name: AWS CloudHSM OpenSSL Provider
    version: 5.17.0
    status: active
  default
    name: OpenSSL Default Provider
    version: 3.2.2
    status: active
```
