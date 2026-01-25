# Install the OpenSSL Dynamic Engine for AWS CloudHSM

Client SDK 5

Use the following sections to install the OpenSSL Dynamic Engine for AWS CloudHSM Client SDK 5.

###### Note

To run a single HSM cluster with Client SDK 5, you must first manage
client key durability settings by setting
`disable_key_availability_check` to `True`.
For more information, see [Key
Synchronization](manage-key-sync.md "manage-key-sync.md") and [Client SDK 5 Configure Tool](configure-sdk-5.md "configure-sdk-5.md").

###### To install and configure the OpenSSL Dynamic Engine

1. Use the following commands to download and install the OpenSSL engine.

Amazon Linux 2023
Install the OpenSSL Dynamic Engine for Amazon Linux 2023 on x86_64 architecture:

```
`$` `wget https://s3.amazonaws.com/cloudhsmv2-software/CloudHsmClient/Amzn2023/cloudhsm-dyn-latest.amzn2023.x86_64.rpm`
```

```
`$` `sudo yum install ./cloudhsm-dyn-latest.amzn2023.x86_64.rpm`
```

Install the OpenSSL Dynamic Engine for Amazon Linux 2023 on ARM64 architecture:

```
`$` `wget https://s3.amazonaws.com/cloudhsmv2-software/CloudHsmClient/Amzn2023/cloudhsm-dyn-latest.amzn2023.aarch64.rpm`
```

```
`$` `sudo yum install ./cloudhsm-dyn-latest.amzn2023.aarch64.rpm`
```

Amazon Linux 2
Install the OpenSSL Dynamic Engine for Amazon Linux 2 on x86_64 architecture:

```
`$` `wget https://s3.amazonaws.com/cloudhsmv2-software/CloudHsmClient/EL7/cloudhsm-dyn-latest.el7.x86_64.rpm`
```

```
`$` `sudo yum install ./cloudhsm-dyn-latest.el7.x86_64.rpm`
```

Install the OpenSSL Dynamic Engine for Amazon Linux 2 on ARM64 architecture:

```
`$` `wget https://s3.amazonaws.com/cloudhsmv2-software/CloudHsmClient/EL7/cloudhsm-dyn-latest.el7.aarch64.rpm`
```

```
`$` `sudo yum install ./cloudhsm-dyn-latest.el7.aarch64.rpm`
```

RHEL 10 (10.0+)
Install the OpenSSL Dynamic Engine for RHEL 10 on x86_64 architecture:

```
`$` `wget https://s3.amazonaws.com/cloudhsmv2-software/CloudHsmClient/EL10/cloudhsm-dyn-latest.el10.x86_64.rpm`
```

```
`$` `sudo yum install ./cloudhsm-dyn-latest.el10.x86_64.rpm`
```

Install the OpenSSL Dynamic Engine for RHEL 10 on ARM64 architecture:

```
`$` `wget https://s3.amazonaws.com/cloudhsmv2-software/CloudHsmClient/EL10/cloudhsm-dyn-latest.el10.aarch64.rpm`
```

```
`$` `sudo yum install ./cloudhsm-dyn-latest.el10.aarch64.rpm`
```

RHEL 9 (9.2+)
Install the OpenSSL Dynamic Engine for RHEL 9 on x86_64 architecture:

```
`$` `wget https://s3.amazonaws.com/cloudhsmv2-software/CloudHsmClient/EL9/cloudhsm-dyn-latest.el9.x86_64.rpm`
```

```
`$` `sudo yum install ./cloudhsm-dyn-latest.el9.x86_64.rpm`
```

Install the OpenSSL Dynamic Engine for RHEL 9 on ARM64 architecture:

```
`$` `wget https://s3.amazonaws.com/cloudhsmv2-software/CloudHsmClient/EL9/cloudhsm-dyn-latest.el9.aarch64.rpm`
```

```
`$` `sudo yum install ./cloudhsm-dyn-latest.el9.aarch64.rpm`
```

RHEL 8 (8.3+)
Install the OpenSSL Dynamic Engine for RHEL 8 on x86_64 architecture:

```
`$` `wget https://s3.amazonaws.com/cloudhsmv2-software/CloudHsmClient/EL8/cloudhsm-dyn-latest.el8.x86_64.rpm`
```

```
`$` `sudo yum install ./cloudhsm-dyn-latest.el8.x86_64.rpm`
```

Install the OpenSSL Dynamic Engine for RHEL 8 on ARM64 architecture:

```
`$` `wget https://s3.amazonaws.com/cloudhsmv2-software/CloudHsmClient/EL8/cloudhsm-dyn-latest.el8.aarch64.rpm`
```

```
`$` `sudo yum install ./cloudhsm-dyn-latest.el8.aarch64.rpm`
```

Ubuntu 24.04 LTS
Install the OpenSSL Dynamic Engine for Ubuntu 24.04 LTS on x86_64 architecture:

```
`$` `wget https://s3.amazonaws.com/cloudhsmv2-software/CloudHsmClient/Noble/cloudhsm-dyn_latest_u24.04_amd64.deb`
```

```
`$` `sudo apt install ./cloudhsm-dyn_latest_u24.04_amd64.deb`
```

Install the OpenSSL Dynamic Engine for Ubuntu 24.04 LTS on ARM64 architecture:

```
`$` `wget https://s3.amazonaws.com/cloudhsmv2-software/CloudHsmClient/Noble/cloudhsm-dyn_latest_u24.04_arm64.deb`
```

```
`$` `sudo apt install ./cloudhsm-dyn_latest_u24.04_arm64.deb`
```

Ubuntu 22.04 LTS
Install the OpenSSL Dynamic Engine for Ubuntu 22.04 LTS on x86_64 architecture:

```
`$` `wget https://s3.amazonaws.com/cloudhsmv2-software/CloudHsmClient/Jammy/cloudhsm-dyn_latest_u22.04_amd64.deb`
```

```
`$` `sudo apt install ./cloudhsm-dyn_latest_u22.04_amd64.deb`
```

Install the OpenSSL Dynamic Engine for Ubuntu 22.04 LTS on ARM64 architecture:

```
`$` `wget https://s3.amazonaws.com/cloudhsmv2-software/CloudHsmClient/Jammy/cloudhsm-dyn_latest_u22.04_arm64.deb`
```

```
`$` `sudo apt install ./cloudhsm-dyn_latest_u22.04_arm64.deb`
```

You have installed the shared
library for the dynamic engine at
`/opt/cloudhsm/lib/libcloudhsm_openssl_engine.so`. 2. Bootstrap Client SDK 5. For more information about bootstrapping, see
[Bootstrap the Client SDK](cluster-connect.md#connect-how-to "cluster-connect.md#connect-how-to"). 3. Set an environment variable with the credentials of a crypto user (CU). For
information about creating CUs, see [Create an AWS CloudHSM user with CloudHSM CLI](cloudhsm_cli-user-create.md "cloudhsm_cli-user-create.md").

```
`$` `export CLOUDHSM_PIN=`<HSM user name>`:`<password>``
```

###### Note

Client SDK 5 introduces the `CLOUDHSM_PIN` environment variable for
storing the credentials of the CU. In Client SDK 3 you store the CU credentials in the
`n3fips_password` environment variable. Client SDK 5 supports both
environment variables, but we recommend using `CLOUDHSM_PIN`.

When setting `CLOUDHSM_PIN` environment variables, you must escape any special characters that may be interpreted by your shell. 4. Connect your installation of OpenSSL Dynamic Engine to the cluster. For more information, see [Connect to the Cluster](cluster-connect.md "cluster-connect.md"). 5. Bootstrap the Client SDK 5. For more information, see [Bootstrap the Client SDK](cluster-connect.md#connect-how-to "cluster-connect.md#connect-how-to").

## Verify the OpenSSL Dynamic Engine for Client SDK 5

Use the following command to verify your installation of OpenSSL Dynamic Engine.

```
`$` `openssl engine -t cloudhsm`
```

The following output verifies your configuration:

```
`(cloudhsm) CloudHSM OpenSSL Engine
 [ available ]`
```
