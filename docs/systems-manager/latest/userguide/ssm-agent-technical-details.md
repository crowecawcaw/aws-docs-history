# Learn technical details about the

SSM Agent

Use the information in this topic to help you implement AWS Systems Manager Agent (SSM Agent) and
understand how the agent works.

###### Topics

- [SSM Agent version 3.2.x.x credential
  behavior](#credentials-file "#credentials-file")
- [SSM Agent credentials precedence](#credentials-precedence "#credentials-precedence")
- [Configuring SSM Agent for use with
  the Federal Information Processing Standard (FIPS)](#fips-compliant-configurations "#fips-compliant-configurations")
- [About the local ssm-user account](#ssm-user-account "#ssm-user-account")
- [SSM Agent and the Instance Metadata Service
  (IMDS)](#imds "#imds")
- [Keeping SSM Agent up-to-date](#updating "#updating")
- [Ensuring that the SSM Agent installation
  directory is not modified, moved, or deleted](#installation-directory "#installation-directory")
- [SSM Agent rolling updates by AWS Regions](#rolling-updates "#rolling-updates")
- [SSM Agent communications with
  AWS managed S3 buckets](#ssm-agent-minimum-s3-permissions "#ssm-agent-minimum-s3-permissions")
- [SSM Agent on GitHub](#github "#github")
- [Understanding SSM Agent hibernation](#ssm-agent-hibernation "#ssm-agent-hibernation")

## SSM Agent version 3.2.x.x credential

behavior

SSM Agent stores a set of temporary credentials at
`/var/lib/amazon/ssm/credentials` (for Linux and macOS) or
`%PROGRAMFILES%\Amazon\SSM\credentials` (for Windows Server) when
an instance is onboarded using the Default Host Management Configuration in
Quick Setup. The temporary credentials have the permissions you specify for the IAM
role you chose for Default Host Management Configuration. On Linux, only the root
account can access these credentials. On Windows Server, only the SYSTEM account and local
Administrators can access these credentials.

## SSM Agent credentials precedence

This topic describes important information about how SSM Agent is granted
permission to perform actions on your resources.

###### Note

Support for edge devices differs slightly. You must configure your edge
devices to use AWS IoT Greengrass Core software, configure an AWS Identity and Access Management (IAM) service
role, and deploy SSM Agent to your devices by using AWS IoT Greengrass. For more information,
see [Managing edge devices with
Systems Manager](systems-manager-setting-up-edge-devices.md "systems-manager-setting-up-edge-devices.md").

When SSM Agent is installed on a machine, it requires permissions in order to
communicate with the Systems Manager service. On Amazon Elastic Compute Cloud (Amazon EC2) instances, these
permissions are provided in an instance profile that is attached to the instance. On
a non-EC2 machine, SSM Agent normally gets the needed permissions from the shared
credentials file, located at `/root/.aws/credentials` (Linux and
macOS) or `%USERPROFILE%\.aws\credentials` (Windows Server). The needed
permissions are added to this file during the [hybrid
activation](activations.md "activations.md") process. If a hybrid-activated node is deregistered, the agent
may enter hibernation mode. For more information, see [Understanding SSM Agent hibernation](#ssm-agent-hibernation "#ssm-agent-hibernation").

In rare cases, however, a machine might end up with permissions added to more than
one of the locations where SSM Agent checks for permissions to run its tasks.

For example, say that you have configured an EC2 instance to be managed by Systems Manager.
That configuration includes attaching an instance profile. But then you decide to
also use that instance for developer or end-user tasks and install the AWS Command Line Interface
(AWS CLI) on it. This installation results in additional permissions being added to a
credentials file on the instance.

When you run a Systems Manager command on the instance, SSM Agent might try to use
credentials different from the ones you expect it to use, such as from a credentials
file instead of an instance profile. This is because SSM Agent looks for credentials
in the order prescribed for the _default credential provider
chain_.

###### Note

On Linux and macOS, SSM Agent runs as the root user. Therefore, the environment
variables and credentials file that SSM Agent looks for in this process are those
of the root user only (`/root/.aws/credentials`). SSM Agent
doesn't look at the environment variables or credentials file of any other users
on the instance during the search for credentials.

The default provider chain looks for credentials in the following order:

1. Environment variables, if configured (`AWS_ACCESS_KEY_ID` and
   `AWS_SECRET_ACCESS_KEY`).
2. Shared credentials file (`$HOME/.aws/credentials` for Linux and
   macOS or `%USERPROFILE%\.aws\credentials` for Windows Server) with
   permissions provided by, for example, a hybrid activation or an AWS CLI
   installation.
3. An AWS Identity and Access Management (IAM) role for tasks if an application is present that uses
   an Amazon Elastic Container Service (Amazon ECS) task definition or **RunTask** API
   operation.
4. An instance profile attached to an Amazon EC2 instance.
5. The IAM role chosen for Default Host Management Configuration.

For related information, see the following topics:

- Instance profiles for EC2 instances – [Configure instance permissions required for Systems Manager](setup-instance-permissions.md "setup-instance-permissions.md")
- Hybrid activations – [Create a hybrid activation to register nodes with Systems Manager](hybrid-activation-managed-nodes.md "hybrid-activation-managed-nodes.md")
- AWS CLI credentials – [Configuration and
  credential file settings](../../../cli/latest/userguide/cli-configure-files.md "../../../cli/latest/userguide/cli-configure-files.md") in the
  _AWS Command Line Interface User Guide_
- Default credential provider chain – [Specifying Credentials](../../../sdk-for-go/latest/developer-guide/configuring-sdk.md#specifying-credentials "../../../sdk-for-go/latest/developer-guide/configuring-sdk.md#specifying-credentials") in the
  _AWS SDK for Go Developer Guide_

###### Note

This topic in the _AWS SDK for Go Developer Guide_ describes the
default provider chain in terms of the SDK for Go; however, the same
principles apply to evaluating credentials for SSM Agent.

## Configuring SSM Agent for use with

the Federal Information Processing Standard (FIPS)

If you need to use Systems Manager with Federal Information Processing Standard (FIPS) 140-3
validated cryptographic modules, you can configure AWS Systems Manager Agent (SSM Agent) to use
the FIPS endpoints in supported Regions.

###### To configure SSM Agent to connect to FIPS 140-3 endpoints

1. Connect to your managed node.
2. Navigate to the directory that contains the
   `amazon-ssm-agent.json` file:
   - Linux: `/etc/amazon/ssm/`
   - macOS: `/opt/aws/ssm/`
   - Windows Server: `C:\Program Files\Amazon\SSM\`

3. Open the file named `amazon-ssm-agent.json` for editing.

###### Tip

If no `amazon-ssm-agent.json` file exists yet, copy the
contents of `amazon-ssm-agent.json.template` to a new file
named `amazon-ssm-agent.json`. Save
`amazon-ssm-agent.json` in the same directory where
`amazon-ssm-agent.json.template` is located. 4. Add the following content to the file. Replace the
`region` placeholder values with the
appropriate Region code for your partition:

```
{
    *---Existing file content, if any---*
    "Mds": {
        "Endpoint": "ec2messages-fips.`region`.amazonaws.com",
    },
    "Ssm": {
        "Endpoint": "ssm-fips.`region`.amazonaws.com",
    },
    "Mgs": {
        "Endpoint": "ssmmessages-fips.`region`.amazonaws.com",
        "Region": "`region`"
    },
    "S3": {
        "Endpoint": "s3-fips.dualstack.`region`.amazonaws.com",
        "Region": `region`"
    },
    "Kms": {
        "Endpoint": "kms-fips.`region`.amazonaws.com"
    }
}
```

Supported Regions include the following:

    * `us-east-1` for the US East (N. Virginia) Region
    * `us-east-2` for the US East (Ohio) Region
    * `us-west-1` for the US West (N. California) Region
    * `us-west-2` for the US West (Oregon) Region
    * `ca-west-1` for the Canada West (Calgary) Region

5. Save the file and restart SSM Agent.

Every time you change the configuration, restart SSM Agent.

You can customize other features of SSM Agent using the same procedure. For an
up-to-date list of the available configuration properties and their default values,
see [Config Property Definitions](https://github.com/aws/amazon-ssm-agent#config-property-definitions "https://github.com/aws/amazon-ssm-agent#config-property-definitions") in the
`amazon-ssm-agent` repository in GitHub.

For more information about AWS support for FIPS, see [Federal Information Processing Standard (FIPS)
140-3](https://aws.amazon.com/compliance/fips/ "https://aws.amazon.com/compliance/fips/").

## About the local ssm-user account

Starting with version 2.3.50.0 of SSM Agent, the agent creates a local user account
called `ssm-user` and adds it to the `/etc/sudoers.d`
directory (Linux and macOS) or to the Administrators group (Windows Server). On agent
versions before 2.3.612.0, the account is created the first time SSM Agent starts or
restarts after installation. On version 2.3.612.0 and later, the
`ssm-user` account is created the first time a session is started on
an instance. This `ssm-user` is the default OS user when a session starts
in Session Manager, a tool in AWS Systems Manager. You can change the permissions by moving
`ssm-user` to a less-privileged group or by changing the
`sudoers` file. The `ssm-user` account isn't
removed from the system when SSM Agent is uninstalled.

On Windows Server, SSM Agent handles setting a new password for the `ssm-user`
account when each session starts. No passwords are set for `ssm-user` on
Linux managed instances.

Starting with SSM Agent version 2.3.612.0, the `ssm-user` account isn't
created automatically on Windows Server machines that are being used as domain
controllers. To use Session Manager on a Windows Server domain controller, create the
`ssm-user` account manually if it isn't already present, and assign
Domain Administrator permissions to the user.

###### Important

In order for the `ssm-user` account to be created, the instance
profile attached to the instance must provide the necessary permissions. For
information, see [Step 2: Verify or add instance permissions for Session Manager](session-manager-getting-started-instance-profile.md "session-manager-getting-started-instance-profile.md").

## SSM Agent and the Instance Metadata Service

(IMDS)

Systems Manager relies on EC2 instance metadata to function correctly. Systems Manager can access
instance metadata using either version 1 or version 2 of the Instance
Metadata Service (IMDSv1 and IMDSv2). Your
instance must be able to access IPv4 address of the instance metadata service:
169.254.169.254. For more information, see [Instance metadata and
user data](../../../AWSEC2/latest/UserGuide/ec2-instance-metadata.md "../../../AWSEC2/latest/UserGuide/ec2-instance-metadata.md") in the _Amazon EC2 User Guide_.

## Keeping SSM Agent up-to-date

An updated version of SSM Agent is released whenever new tools are added to Systems Manager or
updates are made to existing tools. Failing to use the latest version of the agent can
prevent your managed node from using various Systems Manager tools and features. For that reason, we
recommend that you automate the process of keeping SSM Agent up to date on your machines. For
information, see [Automating updates to SSM Agent](ssm-agent-automatic-updates.md "ssm-agent-automatic-updates.md"). Subscribe to the [SSM Agent
Release Notes](https://github.com/aws/amazon-ssm-agent/blob/mainline/RELEASENOTES.md "https://github.com/aws/amazon-ssm-agent/blob/mainline/RELEASENOTES.md") page on GitHub to get notifications about SSM Agent
updates.

###### Note

An updated version of SSM Agent is released whenever new tools are added to Systems Manager or
updates are made to existing tools. Failing to use the latest version of the agent can
prevent your managed node from using various Systems Manager tools and features. For that reason, we
recommend that you automate the process of keeping SSM Agent up to date on your machines. For
information, see [Automating updates to SSM Agent](ssm-agent-automatic-updates.md "ssm-agent-automatic-updates.md"). Subscribe to the [SSM Agent
Release Notes](https://github.com/aws/amazon-ssm-agent/blob/mainline/RELEASENOTES.md "https://github.com/aws/amazon-ssm-agent/blob/mainline/RELEASENOTES.md") page on GitHub to get notifications about SSM Agent
updates.

Amazon Machine Images (AMIs) that include SSM Agent by default can take up to two
weeks to be updated with the newest version of SSM Agent. We recommend that you
configure even more frequent automated updates to SSM Agent.

## Ensuring that the SSM Agent installation

directory is not modified, moved, or deleted

SSM Agent is installed at `/var/lib/amazon/ssm/` (Linux and
macOS) and `%PROGRAMFILES%\Amazon\SSM\` (Windows Server). These
installation directories contain critical files and folders used by SSM Agent, such
as a credentials file, resources for inter-process communication (IPC), and
orchestration folders. Nothing within the installation directory should be modified,
moved, or deleted. Otherwise, SSM Agent might cease to function properly.

## SSM Agent rolling updates by AWS Regions

After an SSM Agent update is made available in its GitHub
repository, it can take up to two weeks until the updated version is rolled out to
all AWS Regions at different times. For this reason, you might receive the
"Unsupported on current platform" or "updating amazon-ssm-agent to an older version,
please turn on allow downgrade to proceed" error when trying to deploy a new version
of SSM Agent in a Region.

To determine the version of SSM Agent available to you, you can run a
`curl` command.

To view the version of the agent available in the global download bucket, run the
following command.

```
curl https://s3.amazonaws.com/ec2-downloads-windows/SSMAgent/latest/VERSION
```

To view the version of the agent available in a specific Region, run the following
command, substituting `region` with the Region you're
working in, such as `us-east-2` for the US East (Ohio) Region.

```
curl https://s3.`region`.amazonaws.com/amazon-ssm-`region`/latest/VERSION
```

You can also open the `VERSION` file directly in your browser
without a `curl` command.

## SSM Agent communications with

AWS managed S3 buckets

In the course of performing various Systems Manager operations, AWS Systems Manager Agent (SSM Agent)
accesses a number of Amazon Simple Storage Service (Amazon S3) buckets. These S3 buckets are publicly
accessible, and by default, SSM Agent connects to them using `HTTP` calls.

However, if you're using a virtual private cloud (VPC) endpoint in your Systems Manager
operations, you must provide explicit permission in an Amazon Elastic Compute Cloud (Amazon EC2) instance
profile for Systems Manager, or in a service role for non-EC2 machines in a [hybrid and multicloud](operating-systems-and-machine-types.md#supported-machine-types "operating-systems-and-machine-types.md#supported-machine-types")
environment. Otherwise, your resources can't access these public buckets.

To grant your managed nodes access to these buckets when you are using a VPC
endpoint, you create a custom Amazon S3 permissions policy, and then attach it to your
instance profile (for EC2 instances) or your service role (for non-EC2 managed
nodes).

For information about using a virtual private cloud (VPC) endpoint in your Systems Manager
operations, see [Improve the security of EC2 instances by using VPC endpoints for Systems Manager](setup-create-vpc.md "setup-create-vpc.md").

###### Note

These permissions only provide access to the AWS managed buckets required by
SSM Agent. They don't provide the permissions that are necessary for other Amazon S3
operations. They also don't provide permission to your own S3 buckets.

For more information, see the following topics:

- [Configure instance permissions required for Systems Manager](setup-instance-permissions.md "setup-instance-permissions.md")
- [Create the IAM service role required for Systems Manager in hybrid and multicloud environments](hybrid-multicloud-service-role.md "hybrid-multicloud-service-role.md")
- [Reference: Amazon S3 buckets for patching
  operations](patch-operations-s3-buckets.md "patch-operations-s3-buckets.md")

###### Contents

- [Required bucket
  permissions](#ssm-agent-minimum-s3-permissions-required "#ssm-agent-minimum-s3-permissions-required")
- [Example](#ssm-agent-minimum-s3-permissions-example "#ssm-agent-minimum-s3-permissions-example")
- [Validating hybrid-activated machines
  using a hardware fingerprint](#fingerprint-validation "#fingerprint-validation")

### Required bucket

permissions

The following table describes each of the S3 buckets that SSM Agent might need
to access for Systems Manager operations.

###### Note

`region` represents the identifier for an AWS Region supported
by AWS Systems Manager, such as `us-east-2` for the US East (Ohio) Region. For a list of supported
`region` values, see the **Region** column in [Systems Manager service endpoints](../../../general/latest/gr/ssm.md#ssm_region "../../../general/latest/gr/ssm.md#ssm_region") in the
_Amazon Web Services General Reference_.

Amazon S3 permissions required by SSM Agent

| S3 bucket ARN                                                                                                                                                                                                | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `arn:aws:s3:::aws-windows-downloads-`region`/*`                                                                                                                                                              | Required for some SSM documents that support only Windows Server operating systems, plus some for cross-platform support, such as `AWSEC2-ConfigureSTIG`.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| `arn:aws:s3:::amazon-ssm-`region`/*`                                                                                                                                                                         | Required for updating SSM Agent installations. These buckets contain the SSM Agent installation packages, and the installation manifests that are referenced by the `AWS-UpdateSSMAgent` document and plugin. If these permissions aren't provided, the SSM Agent makes an HTTP call to download the update.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| `arn:aws:s3:::aws-ssm-`region`/*`                                                                                                                                                                            | Provides access to the S3 bucket containing modules required for use with Systems Manager documents (SSM Command documents), including both non-patching and patching operations. For example: `arn:aws:s3:::aws-ssm-us-east-2/*`. The following are some commonly used SSM documents that use modules from these buckets. <br>• `AWS-RunPatchBaseline` <br>• `AWS-RunPatchBaselineAssociation` <br>• `AWS-RunPatchBaselineWithHooks` <br>• `AWS-ApplyPatchBaseline` (a legacy SSM document) <br>• `AWS-ConfigureWindowsUpdate` <br>• `AWS-FindWindowsUpdates` <br>• `AWS-UpdateSSMAgent` <br>• `AWS-UpdateEC2Config`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| `arn:aws:s3:::patch-baseline-snapshot-`region`/*` -or-`arn:aws:s3:::patch-baseline-snapshot-`region`-`unique-suffix`/*`                                                                                      | Provides access to the S3 bucket containing patch baseline snapshots. This is required if you use any of the following SSM Command documents: <br>• `AWS-RunPatchBaseline` <br>• `AWS-RunPatchBaselineAssociation` <br>• `AWS-RunPatchBaselineWithHooks` <br>• `AWS-ApplyPatchBaseline` (a legacy SSM document) The buckets for most supported AWS Regions use the following format: `arn:aws:s3:::patch-baseline-snapshot-`region``For some Regions, an additional unique suffix is included in the bucket name. For example, the bucket name for the Middle East (Bahrain) Region (me-south-1) is as follows: <br>•`patch-baseline-snapshot-me-south-1-uduvl7q8` For a complete list of patch baseline snapshot bucket names, see [Buckets containing AWS managed patch baseline snapshots](patch-operations-s3-buckets.md#aws-patch-manager-buckets-baseline-snapshots "patch-operations-s3-buckets.md#aws-patch-manager-buckets-baseline-snapshots"). NoteIf you use an on-premises firewall and plan to use Patch Manager, that firewall must also allow access to the appropriate patch baseline endpoint.                                                                                                                                                                   |
| For Linux and Windows Server managed nodes: `arn:aws:s3:::aws-patch-manager-`region`-`unique-suffix`/*` For Amazon EC2 instances for macOS: `arn:aws:s3:::aws-patchmanager-macos-`region`-`unique-suffix`/*` | Provides access to the S3 bucket containing modules used by SSM Command documents for patching operations in Patch Manager. Each bucket name includes a unique suffix, such as `552881074` for buckets in the US East (Ohio) (us-east-2) Region: <br>• `arn:aws:s3:::aws-patch-managerer-us-east-2-552881074/*` <br>• `arn:aws:s3:::``aws-patchmanager-macos-us-east-2-552881074/*` SSM documents The following are some commonly used SSM documents that use modules from these buckets. <br>• `AWS-RunPatchBaseline` <br>• `AWS-RunPatchBaselineAssociation` <br>• `AWS-RunPatchBaselineWithHooks` <br>• `AWS-InstanceRebootWithHooks` <br>• `AWS-PatchAsgInstance` <br>• `AWS-PatchInstanceWithRollback` For complete lists of AWS managed S3 buckets for patching operations, see the following topics: <br>• [Buckets containing SSM Command documents for patching operations (Linux and Windows Server)](patch-operations-s3-buckets.md#aws-patch-manager-buckets-linux-windows "patch-operations-s3-buckets.md#aws-patch-manager-buckets-linux-windows") <br>• [Buckets containing SSM Command documents for patching operations (macOS)](patch-operations-s3-buckets.md#aws-patch-manager-buckets-macos "patch-operations-s3-buckets.md#aws-patch-manager-buckets-macos") | ### Example The following example illustrates how to provide access to the S3 buckets required for Systems Manager operations in the US East (Ohio) Region (us-east-2). In most cases, you need to provide these permissions explicitly in an instance profile or service role only when using a VPC endpoint. ###### Important We recommend that you avoid using wildcard characters (\*) in place of specific Regions in this policy. For example, use `arn:aws:s3:::aws-ssm-us-east-2/*` and don't use `arn:aws:s3:::aws-ssm-*/*`. Using wildcards could provide access to S3 buckets that you don’t intend to grant access to. If you want to use the instance profile for more than one Region, we recommend repeating the first `Statement` block for each Region. JSON `` `{ "Version":"2012-10-17", "Statement": [ { "Effect": "Allow", "Action": "s3:GetObject", "Resource": [ "arn:aws:s3:::aws-windows-downloads-us-east-2/*", "arn:aws:s3:::amazon-ssm-us-east-2/*", "arn:aws:s3:::aws-ssm-us-east-2/*", "arn:aws:s3:::patch-baseline-snapshot-us-east-2/*", "arn:aws:s3:::aws-patch-manager-us-east-2-552881074/*", "arn:aws:s3:::aws-patchmanager-macos-us-east-2-552881074/*" ] } ] }` `` ### Validating hybrid-activated machines using a hardware fingerprint When non-EC2 machines in a [hybrid and multicloud](operating-systems-and-machine-types.md#supported-machine-types "operating-systems-and-machine-types.md#supported-machine-types") environment, SSM Agent gathers a number of system attributes (referred to as the _hardware hash_) and uses these attributes to compute a _fingerprint_. The fingerprint is an opaque string that the agent passes to certain Systems Manager APIs. This unique fingerprint associates the caller with a particular hybrid-activated managed node. The agent stores the fingerprint and hardware hash on the local disk in a location called the _Vault_. The agent computes the hardware hash and fingerprint when the machine is registered for use with Systems Manager. Then, the fingerprint is passed back to the Systems Manager service when the agent sends a `RegisterManagedInstance` command. Later, when sending a `RequestManagedInstanceRoleToken` command, the agent checks the fingerprint and hardware hash in the Vault to make sure that the current machine attributes match with the stored hardware hash. If the current machine attributes do match the hardware hash stored in the Vault, the agent passes in the fingerprint from the Vault to `RegisterManagedInstance`, resulting in a successful call. If the current machine attributes don't match the stored hardware hash, SSM Agent computes a new fingerprint, stores the new hardware hash and fingerprint in the Vault, and passes the new fingerprint to `RequestManagedInstanceRoleToken`. _This causes `RequestManagedInstanceRoleToken` to fail, and the agent won't be able to obtain a role token to connect to the Systems Manager service._ This failure is by design and is used as a verification step to prevent multiple managed nodes from communicating with the Systems Manager service as the same managed node. When comparing the current machine attributes to the hardware hash stored in the Vault, the agent uses the following logic to determine whether the old and new hashes match: <br>• If the SID (system/machine ID) is different, then no match. <br>• Otherwise, if the IP address is the same, then match. <br>• Otherwise, the percentage of machine attributes that match is computed and compared with the user-configured similarity threshold to determine whether there is a match. The similarity threshold is stored in the Vault, as part of the hardware hash. The similarity threshold can be set after an instance is registered using a command like the following. On Linux machines: `sudo amazon-ssm-agent -fingerprint -similarityThreshold 1` On Windows Server machines using PowerShell: ``cd "C:\Program Files\Amazon\SSM\" ` .\amazon-ssm-agent.exe -fingerprint -similarityThreshold 1`` ###### Important If one of the components used to calculate the fingerprint changes, this can cause the agent to hibernate. To help avoid this hibernation, set the similarity threshold to a low value, such as `1`. For more information about hibernation, see [Understanding SSM Agent hibernation](#ssm-agent-hibernation "#ssm-agent-hibernation"). ## SSM Agent on GitHub The source code for SSM Agent is available on [GitHub](https://github.com/aws/amazon-ssm-agent "https://github.com/aws/amazon-ssm-agent") so that you can adapt the agent to meet your needs. We encourage you to submit [pull requests](https://github.com/aws/amazon-ssm-agent/blob/mainline/CONTRIBUTING.md "https://github.com/aws/amazon-ssm-agent/blob/mainline/CONTRIBUTING.md") for changes that you would like to have included. However, Amazon Web Services doesn't provide support for running modified copies of this software. ## Understanding SSM Agent hibernation AWS Systems Manager Agent (SSM Agent) hibernation is an operational mode that occurs when the agent can't maintain proper communication with the Systems Manager service. During hibernation, the agent reduces its communication frequency and enters a standby state. ###### When SSM Agent hibernation occurs SSM Agent hibernation can occur in the following scenarios: Deregistered hybrid nodes When you deregister a [hybrid-activated node](hybrid-activation-managed-nodes.md "hybrid-activation-managed-nodes.md") from Systems Manager, the SSM Agent on that node can't refresh its authorization token. This causes the agent to enter hibernation mode because it can't authenticate with the service. Hardware fingerprint changes SSM Agent uses a hardware fingerprint to validate hybrid-activated machines. If one of the components used to calculate this fingerprint changes significantly, the agent might hibernate as a security measure. This is by design to prevent multiple managed nodes from communicating with Systems Manager as the same node. For more information, see [Validating hybrid-activated machines using a hardware fingerprint](#fingerprint-validation "#fingerprint-validation"). SSM Agent hibernation on Amazon EC2 instances Hibernation can also occur on Amazon EC2 instances under certain conditions, such as when there are connectivity issues or authentication problems with the Systems Manager service. ###### Hibernation communication behavior When SSM Agent enters hibernation mode, its communication pattern with the Systems Manager service changes: <br>• **Normal operation**: The agent regularly communicates with Systems Manager (typically every few minutes) to check for new commands and report status. <br>• **Hibernation mode**: The ping frequency starts at 5 minutes and gradually increases to once per hour by default (configurable up to 24 hours). This reduced communication frequency helps minimize unnecessary network traffic while still allowing the agent to potentially recover if conditions change. During hibernation, the agent continues to retry authentication and connection attempts at the reduced frequency, but it can't process new commands or report detailed status information until hibernation is resolved. ###### Configuration options to prevent hibernation in hybrid instances The primary configuration option to help prevent hibernation caused by hardware fingerprint changes is adjusting the similarity threshold: On Linux machines: `sudo amazon-ssm-agent -fingerprint -similarityThreshold 1` On Windows Server machines using PowerShell: ``cd "C:\Program Files\Amazon\SSM\" ` .\amazon-ssm-agent.exe -fingerprint -similarityThreshold 1`` The similarity threshold determines how strictly the agent compares current machine attributes with the stored hardware hash: <br>• Higher values require more matching attributes <br>• Lower values (such as `1`) are more lenient and can help avoid hibernation caused by minor hardware changes ###### Hibernation logging and monitoring When SSM Agent enters hibernation mode, it creates log entries that can help you identify and troubleshoot the hibernation state: <br>• **Agent log files**: Hibernation events are logged in the standard SSM Agent log files. For more information about log file locations, see [Troubleshoot issues using SSM Agent log files](troubleshooting-ssm-agent.md#systems-manager-ssm-agent-log-files "troubleshooting-ssm-agent.md#systems-manager-ssm-agent-log-files"). <br>• **Amazon EC2 console logging**: For EC2 instances, hibernation messages are now logged to the Amazon EC2 console system logs, providing additional visibility into agent status. To access the logs, select the instance in the EC2 console, and then choose **Actions**, **Monitor and troubleshoot**, **Get system log**. <br>• **Specific log files**: When hibernation starts, particular log files are created that contain detailed information about the hibernation trigger and status. Monitor these log sources to detect hibernation events early and take corrective action to restore normal agent operation. ###### Recovering from hibernation To recover from hibernation, address the underlying cause: <br>• **For deregistered hybrid nodes**: Reregister the node with Systems Manager using a new activation code and ID, as described in [Deregister and reregister a managed node (Linux)](hybrid-multicloud-ssm-agent-install-linux.md#systems-manager-install-managed-linux-deregister-reregister "hybrid-multicloud-ssm-agent-install-linux.md#systems-manager-install-managed-linux-deregister-reregister") and [Deregister and reregister a managed node (Windows Server)](hybrid-multicloud-ssm-agent-install-windows.md#systems-manager-install-managed-win-deregister-reregister "hybrid-multicloud-ssm-agent-install-windows.md#systems-manager-install-managed-win-deregister-reregister"). <br>• **For hardware fingerprint issues**: Adjust the similarity threshold as described above under **Configuration options to prevent hibernation in hybrid instances**, or re-register the node if hardware changes are significant. <br>• **For connectivity issues**: Verify network connectivity and make sure that the required endpoints are accessible. For more information, see [Troubleshooting managed node availability using ssm-cli](troubleshooting-managed-nodes-using-ssm-cli.md "troubleshooting-managed-nodes-using-ssm-cli.md"). After you resolve the underlying issue, the agent should automatically exit hibernation mode and resume normal operation at the next communication attempt. |
