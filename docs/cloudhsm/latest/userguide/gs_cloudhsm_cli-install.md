# Install and configure CloudHSM CLI

To interact with the HSM in your AWS CloudHSM cluster, you need the CloudHSM CLI.

Connect to your client instance and run the following commands to download and install
the AWS CloudHSM command line tools. For more information,
see [Launch an Amazon EC2 client instance for interacting with
AWS CloudHSM](launch-client-instance.md "launch-client-instance.md").

Amazon Linux 2023
Amazon Linux 2023 on x86_64 architecture:

```
`$` `wget https://s3.amazonaws.com/cloudhsmv2-software/CloudHsmClient/Amzn2023/cloudhsm-cli-latest.amzn2023.x86_64.rpm`
```

```
`$` `sudo yum install ./cloudhsm-cli-latest.amzn2023.x86_64.rpm`
```

Amazon Linux 2023 on ARM64 architecture:

```
`$` `wget https://s3.amazonaws.com/cloudhsmv2-software/CloudHsmClient/Amzn2023/cloudhsm-cli-latest.amzn2023.aarch64.rpm`
```

```
`$` `sudo yum install ./cloudhsm-cli-latest.amzn2023.aarch64.rpm`
```

Amazon Linux 2
Amazon Linux 2 on x86_64 architecture:

```
`$` `wget https://s3.amazonaws.com/cloudhsmv2-software/CloudHsmClient/EL7/cloudhsm-cli-latest.el7.x86_64.rpm`
```

```
`$` `sudo yum install ./cloudhsm-cli-latest.el7.x86_64.rpm`
```

Amazon Linux 2 on ARM64 architecture:

```
`$` `wget https://s3.amazonaws.com/cloudhsmv2-software/CloudHsmClient/EL7/cloudhsm-cli-latest.el7.aarch64.rpm`
```

```
`$` `sudo yum install ./cloudhsm-cli-latest.el7.aarch64.rpm`
```

RHEL 9 (9.2+)
RHEL 9 on x86_64 architecture:

```
`$` `wget https://s3.amazonaws.com/cloudhsmv2-software/CloudHsmClient/EL9/cloudhsm-cli-latest.el9.x86_64.rpm`
```

```
`$` `sudo yum install ./cloudhsm-cli-latest.el9.x86_64.rpm`
```

RHEL 9 on ARM64 architecture:

```
`$` `wget https://s3.amazonaws.com/cloudhsmv2-software/CloudHsmClient/EL9/cloudhsm-cli-latest.el9.aarch64.rpm`
```

```
`$` `sudo yum install ./cloudhsm-cli-latest.el9.aarch64.rpm`
```

RHEL 8 (8.3+)
RHEL 8 on x86_64 architecture:

```
`$` `wget https://s3.amazonaws.com/cloudhsmv2-software/CloudHsmClient/EL8/cloudhsm-cli-latest.el8.x86_64.rpm`
```

```
`$` `sudo yum install ./cloudhsm-cli-latest.el8.x86_64.rpm`
```

Ubuntu 24.04 LTS
Ubuntu 24.04 LTS on x86_64 architecture:

```
`$` `wget https://s3.amazonaws.com/cloudhsmv2-software/CloudHsmClient/Noble/cloudhsm-cli_latest_u24.04_amd64.deb`
```

```
`$` `sudo apt install ./cloudhsm-cli_latest_u24.04_amd64.deb`
```

Ubuntu 24.04 LTS on ARM64 architecture:

```
`$` `wget https://s3.amazonaws.com/cloudhsmv2-software/CloudHsmClient/Noble/cloudhsm-cli_latest_u24.04_arm64.deb`
```

```
`$` `sudo apt install ./cloudhsm-cli_latest_u24.04_arm64.deb`
```

Ubuntu 22.04 LTS
Ubuntu 22.04 LTS on x86_64 architecture:

```
`$` `wget https://s3.amazonaws.com/cloudhsmv2-software/CloudHsmClient/Jammy/cloudhsm-cli_latest_u22.04_amd64.deb`
```

```
`$` `sudo apt install ./cloudhsm-cli_latest_u22.04_amd64.deb`
```

Ubuntu 22.04 LTS on ARM64 architecture:

```
`$` `wget https://s3.amazonaws.com/cloudhsmv2-software/CloudHsmClient/Jammy/cloudhsm-cli_latest_u22.04_arm64.deb`
```

```
`$` `sudo apt install ./cloudhsm-cli_latest_u22.04_arm64.deb`
```

Ubuntu 20.04 LTS
Ubuntu 20.04 LTS on x86_64 architecture:

```
`$` `wget https://s3.amazonaws.com/cloudhsmv2-software/CloudHsmClient/Focal/cloudhsm-cli_latest_u20.04_amd64.deb`
```

```
`$` `sudo apt install ./cloudhsm-cli_latest_u20.04_amd64.deb`
```

Windows Server 2022
For Windows Server 2022 on x86_64 architecture, open PowerShell as an administrator and run the following command:

```
`PS C:\>` `wget https://s3.amazonaws.com/cloudhsmv2-software/CloudHsmClient/Windows/AWSCloudHSMCLI-latest.msi -Outfile C:\AWSCloudHSMCLI-latest.msi`
```

```
`PS C:\>` `Start-Process msiexec.exe -ArgumentList '/i C:\AWSCloudHSMCLI-latest.msi /quiet /norestart /log C:\client-install.txt' -Wait`
```

Windows Server 2019
For Windows Server 2019 on x86_64 architecture, open PowerShell as an administrator and run the following command:

```
`PS C:\>` `wget https://s3.amazonaws.com/cloudhsmv2-software/CloudHsmClient/Windows/AWSCloudHSMCLI-latest.msi -Outfile C:\AWSCloudHSMCLI-latest.msi`
```

```
`PS C:\>` `Start-Process msiexec.exe -ArgumentList '/i C:\AWSCloudHSMCLI-latest.msi /quiet /norestart /log C:\client-install.txt' -Wait`
```

Windows Server 2016
For Windows Server 2016 on x86_64 architecture, open PowerShell as an administrator and run the following command:

```
`PS C:\>` `wget https://s3.amazonaws.com/cloudhsmv2-software/CloudHsmClient/Windows/AWSCloudHSMCLI-latest.msi -Outfile C:\AWSCloudHSMCLI-latest.msi`
```

```
`PS C:\>` `Start-Process msiexec.exe -ArgumentList '/i C:\AWSCloudHSMCLI-latest.msi /quiet /norestart /log C:\client-install.txt' -Wait`
```

Use the following commands to configure CloudHSM CLI.

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
