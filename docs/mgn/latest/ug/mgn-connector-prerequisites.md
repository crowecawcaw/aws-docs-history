NEW - You can now accelerate your migration and modernization with AWS Transform. Read [Getting Started](../../../transform/latest/userguide/getting-started.md "../../../transform/latest/userguide/getting-started.md") in the _AWS Transform User Guide_.

# Prerequisites for installing the MGN connector

To use the Application Migration Service connector you must meet these prerequisites.

## General prerequisites

- While the MGN connector can be deployed on the same server that hosts the MGN vCenter Client installer (agentless appliance),
  we recommend that the MGN connector be installed on a dedicated server.
- The _openssl_ library must be installed on the server.
- You must have the required [permissions](mgn-connector-permissions.md "mgn-connector-permissions.md").

## Operating systems that support the MGN

connector

The MGN connector can be installed on servers running the following Linux
versions:

- Ubuntu 18.x+ (64 bit) - 22.04 (x86_64)
- Amazon Linux 2 (x86_64)
- RHEL8.x (x86_64)

## SSM agent installation requirements

Installation of the MGN Connector also installs the SSM agent.

- If the SSM agent is already installed on the server you must uninstall it before installing the MGN connector. See
  [Uninstalling SSM Agent from Linux instances](../../../systems-manager/latest/userguide/sysman-uninstall-agent.md "../../../systems-manager/latest/userguide/sysman-uninstall-agent.md")
  in the _AWS Systems Manager User Guide_.
- A minimum of 200 MB of free disk space and 200 KB of free disk space in the `/var` directory.
- Installation is not supported on these operating systems:
  - CentOS 5.x
  - CentOS 6.x
  - RHEL 6.x
  - Oracle 6.x
  - Amazon Linux 1

## Security recommendations for MGN connector

We recommend that the MGN connector server is only accessed by authorized
personnel and has the required OS patches. We also recommend that the servers to
which the MGN connector connects have all the required OS patches.

If you configure [outputting logs to S3](../../../systems-manager/latest/userguide/getting-started-create-iam-instance-profile.md#create-iam-instance-profile-ssn-logging "../../../systems-manager/latest/userguide/getting-started-create-iam-instance-profile.md#create-iam-instance-profile-ssn-logging"), you will first [create an Amazon S3 bucket](../../../AmazonS3/latest/userguide/create-bucket-overview.md "../../../AmazonS3/latest/userguide/create-bucket-overview.md"). We recommend that you apply S3 bucket
[S3 security practices](../../../AmazonS3/latest/userguide/security-best-practices.md "../../../AmazonS3/latest/userguide/security-best-practices.md")
