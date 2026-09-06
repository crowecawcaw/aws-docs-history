

# DRSFA prerequisites
<a name="failback-failover-drsfa-prereques"></a>

Before using the DRSFA client, verify that you meet the following requirements.

**Note**  
The DRSFA client works only with vCenter source servers. It was tested on vCenter versions 6.7, 7.0, 8.0, and 9.0.

You can fail back all Recovery instances in a single AWS Region simultaneously with the DRSFA client, as long as your vCenter hardware supports the failback load.

## Network and AWS prerequisites
<a name="failback-failover-drsfa-prereqs-network"></a>
+ Meet all [network requirements](preparing-environments.md) for replication.
+ [Initialize AWS Elastic Disaster Recovery](getting-started-initializing.md) in your account.
+ Open inbound TCP port 1500 on the Recovery instance in AWS.
+ The Recovery instance used as a source for failback must have permissions to access AWS Elastic Disaster Recovery through API calls. Attach an instance profile that includes the AWSElasticDisasterRecoveryRecoveryInstancePolicy policy. By default, the launch settings that DRS creates for source servers already include an instance profile with this policy.

## DRSFA client host requirements
<a name="failback-failover-drsfa-prereqs-host"></a>

The DRSFA client host must meet the following requirements:
+ At least 4 GB of RAM
+ Ubuntu 22.04, 24.04, or 26.04 (x86\_64)
+ Python 3.13 with pip installed
+ Network connectivity to your vCenter environment

The following system packages are required. The installer attempts to install them if they are not already present:

```
build-essential curl genisoimage git libbz2-dev libffi-dev
liblzma-dev libncurses5-dev libncursesw5-dev libreadline-dev
libsqlite3-dev libssl-dev llvm make tk-dev unzip wget
xz-utils zlib1g-dev
```

For required Python libraries, see the `requirements.txt` file at `https://drsfa-us-west-2.s3.us-west-2.amazonaws.com/requirements.txt`. These libraries are installed automatically by the DRSFA client.

## vCenter requirements
<a name="failback-failover-drsfa-prereqs-vcenter"></a>
+ Each server being failed back must have at least 4 GB of RAM.
+ Each server being failed back must have the hardware clock set to UTC (not Local Time).
+ Each vCenter source server must have two CD-ROM devices with IDE controllers attached — one for the DRS Failback Client and one for `drs_failback_automation_seed.iso`. If no attached CD-ROM devices are found, the DRSFA client attempts to add them.
+ Upload the DRS Failback Client ISO to your vCenter Datastore. We recommend using the latest version. [Download the latest DRS Failback Client](failback-performing.md#failback-performing-performing) and upload it to your datastore.
+ The vCenter credentials must include the following permissions:    
[See the AWS documentation website for more details](http://docs.aws.amazon.com/drs/latest/userguide/failback-failover-drsfa-prereques.html)
+ Constrain vCenter credentials to only the VMs you plan to fail back.

## Recommendations
<a name="failback-failover-drsfa-prereqs-recommendations"></a>
+ Run SHA-512 checksum verification on the DRS Failback Client ISO before use. Verify the checksum at: `https://aws-elastic-disaster-recovery-hashes-{REGION}.s3.amazonaws.com/latest/failback_livecd/aws-failback-livecd-64bit.iso.sha512`
+ Run SHA-512 checksum verification on `drs_failback_automation_seed.iso` before use. The hash is exported to `drs_failback_automation_seed.iso.sha512` when the seed ISO is created.
+ Run the DRSFA client with low privileges. The client does not require root access.
+ Follow the least privilege principle for the folder where JSON output and ISO files are stored.

## Security best practices
<a name="failback-failover-drsfa-security"></a>

Follow these security best practices when using the DRSFA client:
+ Always use the latest version of the DRSFA client. The client automatically checks for updates at startup.
+ Verify DRSFA client hashes manually when automatic hash verification is not performed. The hash verification hint appears during installation.
+ Do not grant additional permissions to the DRSFA client beyond those listed in the prerequisites.
+ Follow the [AWS recommended password policy](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_credentials_passwords_account-policy.html) when setting the password for the VM that hosts the DRS Failback Client.
+ Restrict access to the vCenter environment to trusted administrators only. The DRSFA client treats the executing user and anyone with datastore access as a single trust entity.