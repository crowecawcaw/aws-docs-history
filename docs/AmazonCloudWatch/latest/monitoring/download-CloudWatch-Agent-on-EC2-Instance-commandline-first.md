# Download the

CloudWatch agent package

###### Note

To download the CloudWatch agent, your connection must use TLS 1.2 or later.

The CloudWatch agent is available as a package in Amazon Linux 2023 and Amazon Linux 2. If
you are using this operating system, you can install the package by entering the following
command. You must also make sure that the IAM role attached to the instance has the
**CloudWatchAgentServerPolicy** attached.

```
sudo yum install amazon-cloudwatch-agent
```

On all supported operating systems, you can download and install the CloudWatch
agent using the command line.

For each download link, there is
a general link as well as links for each AWS Region.

If you use the Region-specific links, replace the default
Region (`us-east-1`) with the appropriate Region for
your account. For example, for Amazon Linux 2023 and Amazon Linux 2 and the x86-64 architecture, three of the
valid download links are:

- `https://amazoncloudwatch-agent.s3.amazonaws.com/amazon_linux/amd64/latest/amazon-cloudwatch-agent.rpm`
- `https://amazoncloudwatch-agent-us-east-1.s3.us-east-1.amazonaws.com/amazon_linux/amd64/latest/amazon-cloudwatch-agent.rpm`
- `https://amazoncloudwatch-agent-eu-central-1.s3.eu-central-1.amazonaws.com/amazon_linux/amd64/latest/amazon-cloudwatch-agent.rpm`
  You can also download a README file about the latest changes to the
  agent, and a file that indicates the version number that is available for download. These
  files are in the following locations:

###### Note

If you use the Region-specific links, replace the default
Region (`us-east-1`) with the appropriate Region for
your account.

- `https://amazoncloudwatch-agent.s3.amazonaws.com/info/latest/RELEASE_NOTES`
  or
  `https://amazoncloudwatch-agent-`us-east-1`.s3.`us-east-1`.amazonaws.com/info/latest/RELEASE_NOTES`
- `https://amazoncloudwatch-agent.s3.amazonaws.com/info/latest/CWAGENT_VERSION`
  or
  `https://amazoncloudwatch-agent-`us-east-1`.s3.`us-east-1`.amazonaws.com/info/latest/CWAGENT_VERSION`

| Architecture | Platform                             | Download link                                                                                                                                                                                                                        | Signature file link                                                                                                                                                                                                                          |
| ------------ | ------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| x86-64       | Amazon Linux 2023 and Amazon Linux 2 | https://amazoncloudwatch-agent.s3.amazonaws.com/amazon\_linux/amd64/latest/amazon-cloudwatch-agent.rpm https://amazoncloudwatch-agent-`us-east-1`.s3.`us-east-1`.amazonaws.com/amazon_linux/amd64/latest/amazon-cloudwatch-agent.rpm | https://amazoncloudwatch-agent.s3.amazonaws.com/amazon\_linux/amd64/latest/amazon-cloudwatch-agent.rpm.sig https://amazoncloudwatch-agent-`us-east-1`.s3.`us-east-1`.amazonaws.com/amazon_linux/amd64/latest/amazon-cloudwatch-agent.rpm.sig |
| x86-64       | Centos                               | https://amazoncloudwatch-agent.s3.amazonaws.com/centos/amd64/latest/amazon-cloudwatch-agent.rpm https://amazoncloudwatch-agent-`us-east-1`.s3.`us-east-1`.amazonaws.com/centos/amd64/latest/amazon-cloudwatch-agent.rpm              | https://amazoncloudwatch-agent.s3.amazonaws.com/centos/amd64/latest/amazon-cloudwatch-agent.rpm.sig https://amazoncloudwatch-agent-`us-east-1`.s3.`us-east-1`.amazonaws.com/centos/amd64/latest/amazon-cloudwatch-agent.rpm.sig              |
| x86-64       | Redhat                               | https://amazoncloudwatch-agent.s3.amazonaws.com/redhat/amd64/latest/amazon-cloudwatch-agent.rpm https://amazoncloudwatch-agent-`us-east-1`.s3.`us-east-1`.amazonaws.com/redhat/amd64/latest/amazon-cloudwatch-agent.rpm              | https://amazoncloudwatch-agent.s3.amazonaws.com/redhat/amd64/latest/amazon-cloudwatch-agent.rpm.sig https://amazoncloudwatch-agent-`us-east-1`.s3.`us-east-1`.amazonaws.com/redhat/amd64/latest/amazon-cloudwatch-agent.rpm.sig              |
| x86-64       | SUSE                                 | https://amazoncloudwatch-agent.s3.amazonaws.com/suse/amd64/latest/amazon-cloudwatch-agent.rpm https://amazoncloudwatch-agent-`us-east-1`.s3.`us-east-1`.amazonaws.com/suse/amd64/latest/amazon-cloudwatch-agent.rpm                  | https://amazoncloudwatch-agent.s3.amazonaws.com/suse/amd64/latest/amazon-cloudwatch-agent.rpm.sig https://amazoncloudwatch-agent-`us-east-1`.s3.`us-east-1`.amazonaws.com/suse/amd64/latest/amazon-cloudwatch-agent.rpm.sig                  |
| x86-64       | Debian                               | https://amazoncloudwatch-agent.s3.amazonaws.com/debian/amd64/latest/amazon-cloudwatch-agent.deb https://amazoncloudwatch-agent-`us-east-1`.s3.`us-east-1`.amazonaws.com/debian/amd64/latest/amazon-cloudwatch-agent.deb              | https://amazoncloudwatch-agent.s3.amazonaws.com/debian/amd64/latest/amazon-cloudwatch-agent.deb.sig https://amazoncloudwatch-agent-`us-east-1`.s3.`us-east-1`.amazonaws.com/debian/amd64/latest/amazon-cloudwatch-agent.deb.sig              |
| x86-64       | Ubuntu                               | https://amazoncloudwatch-agent.s3.amazonaws.com/ubuntu/amd64/latest/amazon-cloudwatch-agent.deb https://amazoncloudwatch-agent-`us-east-1`.s3.`us-east-1`.amazonaws.com/ubuntu/amd64/latest/amazon-cloudwatch-agent.deb              | https://amazoncloudwatch-agent.s3.amazonaws.com/ubuntu/amd64/latest/amazon-cloudwatch-agent.deb.sig https://amazoncloudwatch-agent-`us-east-1`.s3.`us-east-1`.amazonaws.com/ubuntu/amd64/latest/amazon-cloudwatch-agent.deb.sig              |
| x86-64       | Oracle                               | https://amazoncloudwatch-agent.s3.amazonaws.com/oracle\_linux/amd64/latest/amazon-cloudwatch-agent.rpm https://amazoncloudwatch-agent-`us-east-1`.s3.`us-east-1`.amazonaws.com/oracle_linux/amd64/latest/amazon-cloudwatch-agent.rpm | https://amazoncloudwatch-agent.s3.amazonaws.com/oracle\_linux/amd64/latest/amazon-cloudwatch-agent.rpm.sig https://amazoncloudwatch-agent-`us-east-1`.s3.`us-east-1`.amazonaws.com/oracle_linux/amd64/latest/amazon-cloudwatch-agent.rpm.sig |
| x86-64       | macOS                                | https://amazoncloudwatch-agent.s3.amazonaws.com/darwin/amd64/latest/amazon-cloudwatch-agent.pkg https://amazoncloudwatch-agent-`us-east-1`.s3.`us-east-1`.amazonaws.com/darwin/amd64/latest/amazon-cloudwatch-agent.pkg              | https://amazoncloudwatch-agent.s3.amazonaws.com/darwin/amd64/latest/amazon-cloudwatch-agent.pkg.sig https://amazoncloudwatch-agent-`us-east-1`.s3.`us-east-1`.amazonaws.com/darwin/amd64/latest/amazon-cloudwatch-agent.pkg.sig              |
| x86-64       | Windows                              | https://amazoncloudwatch-agent.s3.amazonaws.com/windows/amd64/latest/amazon-cloudwatch-agent.msi https://amazoncloudwatch-agent-`us-east-1`.s3.`us-east-1`.amazonaws.com/windows/amd64/latest/amazon-cloudwatch-agent.msi            | https://amazoncloudwatch-agent.s3.amazonaws.com/windows/amd64/latest/amazon-cloudwatch-agent.msi.sig https://amazoncloudwatch-agent-`us-east-1`.s3.`us-east-1`.amazonaws.com/windows/amd64/latest/amazon-cloudwatch-agent.msi.sig            |
| ARM64        | Amazon Linux 2023 and Amazon Linux 2 | https://amazoncloudwatch-agent.s3.amazonaws.com/amazon\_linux/arm64/latest/amazon-cloudwatch-agent.rpm https://amazoncloudwatch-agent-`us-east-1`.s3.`us-east-1`.amazonaws.com/amazon_linux/arm64/latest/amazon-cloudwatch-agent.rpm | https://amazoncloudwatch-agent.s3.amazonaws.com/amazon\_linux/arm64/latest/amazon-cloudwatch-agent.rpm.sig https://amazoncloudwatch-agent-`us-east-1`.s3.`us-east-1`.amazonaws.com/amazon_linux/arm64/latest/amazon-cloudwatch-agent.rpm.sig |
| ARM64        | Redhat                               | https://amazoncloudwatch-agent.s3.amazonaws.com/redhat/arm64/latest/amazon-cloudwatch-agent.rpm https://amazoncloudwatch-agent-`us-east-1`.s3.`us-east-1`.amazonaws.com/redhat/arm64/latest/amazon-cloudwatch-agent.rpm              | https://amazoncloudwatch-agent.s3.amazonaws.com/redhat/arm64/latest/amazon-cloudwatch-agent.rpm.sig https://amazoncloudwatch-agent-`us-east-1`.s3.`us-east-1`.amazonaws.com/redhat/arm64/latest/amazon-cloudwatch-agent.rpm.sig              |
| ARM64        | Ubuntu                               | https://amazoncloudwatch-agent.s3.amazonaws.com/ubuntu/arm64/latest/amazon-cloudwatch-agent.deb https://amazoncloudwatch-agent-`us-east-1`.s3.`us-east-1`.amazonaws.com/ubuntu/arm64/latest/amazon-cloudwatch-agent.deb              | https://amazoncloudwatch-agent.s3.amazonaws.com/ubuntu/arm64/latest/amazon-cloudwatch-agent.deb.sig https://amazoncloudwatch-agent-`us-east-1`.s3.`us-east-1`.amazonaws.com/ubuntu/arm64/latest/amazon-cloudwatch-agent.deb.sig              |
| ARM64        | Debian                               | https://amazoncloudwatch-agent.s3.amazonaws.com/debian/arm64/latest/amazon-cloudwatch-agent.deb https://amazoncloudwatch-agent-`us-east-1`.s3.`us-east-1`.amazonaws.com/debian/arm64/latest/amazon-cloudwatch-agent.deb              | https://amazoncloudwatch-agent.s3.amazonaws.com/debian/arm64/latest/amazon-cloudwatch-agent.deb.sig https://amazoncloudwatch-agent-`us-east-1`.s3.`us-east-1`.amazonaws.com/debian/arm64/latest/amazon-cloudwatch-agent.deb.sig              |
| ARM64        | SUSE                                 | https://amazoncloudwatch-agent.s3.amazonaws.com/suse/arm64/latest/amazon-cloudwatch-agent.rpm https://amazoncloudwatch-agent-`us-east-1`.s3.`us-east-1`.amazonaws.com/suse/arm64/latest/amazon-cloudwatch-agent.rpm                  | https://amazoncloudwatch-agent.s3.amazonaws.com/suse/arm64/latest/amazon-cloudwatch-agent.rpm.sig https://amazoncloudwatch-agent-`us-east-1`.s3.`us-east-1`.amazonaws.com/suse/arm64/latest/amazon-cloudwatch-agent.rpm.sig                  |
| ARM64        | MacOS                                | https://amazoncloudwatch-agent.s3.amazonaws.com/darwin/arm64/latest/amazon-cloudwatch-agent.pkg https://amazoncloudwatch-agent-`us-east-1`.s3.`us-east-1`.amazonaws.com/darwin/arm64/latest/amazon-cloudwatch-agent.pkg              | https://amazoncloudwatch-agent.s3.amazonaws.com/darwin/arm64/latest/amazon-cloudwatch-agent.pkg.sig https://amazoncloudwatch-agent-`us-east-1`.s3.`us-east-1`.amazonaws.com/darwin/arm64/latest/amazon-cloudwatch-agent.pkg.sig              |
