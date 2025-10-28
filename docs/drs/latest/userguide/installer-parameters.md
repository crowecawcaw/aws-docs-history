# AWS Replication Agent Installer

parameters

The AWS Replication Agent Installer supports the following command line parameters.

**--region**

The region into which the installer registers the source server.

**--aws-access-key-id**

The AWS IAM Access Key used for authenticating the installing user. If this
parameter is not provided, the installer prompts for it.

**--aws-secret-access-key**

The AWS IAM Secret Access Key tied to the AWS IAM Access Key used for
authenticating the installing user. If this parameter is not provided, the
installer prompts for it.

**--aws-session-token**

The session token is generated when using [temporary credentials](credentials.md#credentials-agent-temporary "credentials.md#credentials-agent-temporary") generated using AWS STS.

**--account-id**

Use this parameter to install the DRS agent on an EC2 instance to replicate to another AWS account without any additional access key or temporary credentials.
Specify the 12 digit ID of the account into which you want to replicate your source server.
This action requires an EC2 instance profile with the [AWSElasticDisasterRecoveryEc2InstancePolicy](security-iam-awsmanpol-AWSElasticDisasterRecoveryEc2InstancePolicy.md "security-iam-awsmanpol-AWSElasticDisasterRecoveryEc2InstancePolicy.md") policy,
to define the account to replicate into as a [Trusted Account](trusted-accounts.md#trusted-accounts-page "trusted-accounts.md#trusted-accounts-page") and select the roles in **Failback and in-AWS right-sizing roles**.

**--no-prompt**

Run the installation without prompting the user.

**--devices**

Specify exactly which disks to replicate.

**--force-volumes**

This parameter must be used with the _--no-prompt_
parameter. This parameter cancels the automatic detection of physical disks to
replicate. You need to specify the exact disks to replicate using the
_--devices_ parameter (including the root disk, failure to
specify the root disk causes replication to fail). This parameter should only be
used as a troubleshooting tool if the _--devices_ parameter
fails to identify the disks correctly.

**--tags**

Use this parameter to add resource tags to the source server. Use a space to
separate each tag.

```
--tags {"Key1"="Value1" "Key2"="Value2"}
```

###### Note

This flag may only be used when adding new source servers to AWS DRS. You
cannot use the --tags flag to modify tags of source servers that have already
been added to AWS DRS.

**--s3-endpoint**

Use this parameter to specify a VPC endpoint you created for S3 if you do not wish to
open your firewall ports to access the default S3 endpoint. [Learn more about installing the Agent on a blocked
network.](installing-agent-blocked.md "installing-agent-blocked.md")

**--endpoint**

Use this parameter to specify the Private Link endpoint you created for Elastic
Disaster Recovery if you do not wish to open your firewall ports to access the default
AWS Elastic Disaster Recovery endpoint. [Learn more
about installing the agent on a blocked network.](installing-agent-blocked.md "installing-agent-blocked.md")

###### Note

We do not recommend using this flag when installing the AWS Elastic Disaster Recovery Agent on an EC2 Instance, as it can prevent successful failback from occuring.
We recommend ensuring DNS automatically resolves the `{region}.drs.amazonaws.com`
entry to the Private Link endpoint rather than leveraging this parameter.

**--install-as-recovery-instance**

Use this parameter to add an existing AWS instance to AWS Elastic Disaster Recovery as a recovery
instance. You may opt to add recovery instances if you have added additional EC2
instances to AWS and now want to recover them into source servers. You are asked
to pair the newly added recovery instance with a source server during AWS
Replication Agent installation.

**--proxy-address**

_Linux Installer only._

Use this parameter to configure the agent to use a specific proxy server:
`--proxy-address https://PROXY:PORT/`. Ensure the proxy configuration
has the trailing forward slash (/).

**--exclude-instance-store-volumes**

_Linux Installer only._

Use this parameter to exclude instance store volumes from replication.
