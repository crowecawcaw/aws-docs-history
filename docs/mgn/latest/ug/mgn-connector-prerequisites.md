

NEW - You can now accelerate your migration and modernization with AWS Transform. Read [Getting Started](https://docs.aws.amazon.com/transform/latest/userguide/getting-started.html) in the *AWS Transform User Guide*.

# Prerequisites for installing the MGN connector
<a name="mgn-connector-prerequisites"></a>

To use the MGN connector you must meet these prerequisites.

## General prerequisites
<a name="mgn-connector-prerequisites-general"></a>
+ While the MGN connector can be deployed on the same server that hosts the MGN vCenter Client installer (agentless appliance), we recommend that the MGN connector be installed on a dedicated server.
+ The *openssl* library must be installed on the server.
+ You must have the required [permissions](mgn-connector-permissions.md).

**Note**  
The MGN connector is not supported for IPv6.

## Operating systems that support the MGN connector
<a name="mgn-connector-os"></a>

The MGN connector can be installed on servers running the following Linux versions:
+ Ubuntu 18.x\+ (64 bit) - 22.04 (x86\_64)
+ Amazon Linux 2 (x86\_64)
+ RHEL8.x (x86\_64)

## SSM agent installation requirements
<a name="mgn-connector-ssm"></a>

Installation of the MGN Connector also installs the SSM agent.
+ If the SSM agent is already installed on the server you must uninstall it before installing the MGN connector. See [ Uninstalling SSM Agent from Linux instances ](https://docs.aws.amazon.com/systems-manager/latest/userguide/sysman-uninstall-agent.html) in the *AWS Systems Manager User Guide*.
+ A minimum of 200 MB of free disk space and 200 KB of free disk space in the `/var` directory.

## Security recommendations for MGN connector
<a name="mgn-connector-security"></a>

We recommend that the MGN connector server is only accessed by authorized personnel and has all the required OS patches. We also recommend that the servers to which the MGN connector connects have all the required OS patches.

If you configure [outputting logs to S3](https://docs.aws.amazon.com/systems-manager/latest/userguide/getting-started-create-iam-instance-profile.html#create-iam-instance-profile-ssn-logging), you will first [create an Amazon S3 bucket](https://docs.aws.amazon.com/AmazonS3/latest/userguide/create-bucket-overview.html). We recommend that you apply S3 bucket [S3 security practices](https://docs.aws.amazon.com/AmazonS3/latest/userguide/security-best-practices.html)