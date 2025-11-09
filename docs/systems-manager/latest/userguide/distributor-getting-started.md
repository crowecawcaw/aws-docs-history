AWS Systems Manager Change Manager is no longer open to new customers. Existing customers can continue to use the service as normal. For more information, see
[AWS Systems Manager Change Manager availability change](change-manager-availability-change.md "change-manager-availability-change.md").

# Setting up Distributor

Before you use Distributor, a tool in AWS Systems Manager, to create, manage, and deploy software
packages, follow these steps.

## Complete Distributor prerequisites

Before you use Distributor, a tool in AWS Systems Manager, be sure your environment meets the
following requirements.

| Distributor prerequisites | Requirement                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        | Description |
| ------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ----------- |
| SSM Agent                 | AWS Systems Manager SSM Agent version 2.3.274.0 or later must be<br>installed on the managed nodes on which you want to deploy or<br>from which you want to remove packages.<br>To install or update SSM Agent, see [Working with SSM Agent](ssm-agent.md "ssm-agent.md").                                                                                                                                                                                                                                                                                         |
| AWS CLI                   | (Optional) To use the AWS Command Line Interface (AWS CLI) instead of the Systems Manager<br>console to create and manage packages, install the newest<br>release of the AWS CLI on your local computer.<br>For more information about how to install or upgrade the CLI,<br>see [Installing the<br>AWS Command Line Interface](../../../cli/latest/userguide/installing.md "../../../cli/latest/userguide/installing.md") in the<br>_AWS Command Line Interface User Guide_.                                                                                      |
| AWS Tools for PowerShell  | (Optional) To use the Tools for PowerShell instead of the Systems Manager console to<br>create and manage packages, install the newest release of<br>Tools for PowerShell on your local computer.<br>For more information about how to install or upgrade the<br>Tools for PowerShell, see [Setting up the<br>AWS Tools for Windows PowerShell or AWS Tools for PowerShell Core](../../../powershell/latest/userguide/pstools-getting-set-up.md "../../../powershell/latest/userguide/pstools-getting-set-up.md") in the<br>_AWS Tools for PowerShell User Guide_. |

###### Note

Systems Manager doesn't support distributing packages to Oracle Linux managed nodes by
using Distributor.

## Verify or create an

IAM instance profile with Distributor permissions

By default, AWS Systems Manager doesn't have permission to perform actions on your
instances. You must grant access by using an AWS Identity and Access Management (IAM) instance profile. An
instance profile is a container that passes IAM role information to an Amazon Elastic Compute Cloud
(Amazon EC2) instance at launch. This requirement applies to permissions for all Systems Manager
tools, not just Distributor.

###### Note

When you configure your edge devices to run AWS IoT Greengrass Core software and
SSM Agent, you specify an IAM service role that enables Systems Manager to peform actions
on it. You don't need to configure managed edge devices with an instance
profile.

If you already use other Systems Manager tools, such as Run Command and State Manager, an instance
profile with the required permissions for Distributor is already attached to your
instances. The simplest way to ensure that you have permissions to perform Distributor
tasks is to attach the **AmazonSSMManagedInstanceCore**
policy to your instance profile. For more information, see [Configure instance permissions required for Systems Manager](setup-instance-permissions.md "setup-instance-permissions.md").

## Control user access to

packages

Using AWS Identity and Access Management (IAM) policies, you can control who can create, deploy, and
manage packages. You also control which Run Command and State Manager API operations they
can perform on managed nodes. Like Distributor, both Run Command and State Manager, are tools
in AWS Systems Manager.

###### ARN Format

User-defined packages are associated with document Amazon Resource Names
(ARNs) and have the following format.

```
arn:aws:ssm:`region`:`account-id`:document/`document-name`
```

The following is an example.

```
arn:aws:ssm:us-west-1:123456789012:document/ExampleDocumentName
```

You can use a pair of AWS supplied default IAM policies, one for end users and
one for administrators, to grant permissions for Distributor activities. Or you can
create custom IAM policies appropriate for your permissions requirements.

For more information about using variables in IAM policies, see [IAM Policy Elements:
Variables](../../../IAM/latest/UserGuide/reference_policies_variables.md "../../../IAM/latest/UserGuide/reference_policies_variables.md").

For information about how to create policies and attach them to users or groups,
see [Creating IAM
Policies](../../../IAM/latest/UserGuide/access_policies_create.md "../../../IAM/latest/UserGuide/access_policies_create.md") and [Adding and
Removing IAM Policies](../../../IAM/latest/UserGuide/access_policies_manage-attach-detach.md "../../../IAM/latest/UserGuide/access_policies_manage-attach-detach.md") in the
_IAM User Guide_.

## Create or choose an Amazon S3 bucket to

store Distributor packages

When you create a package by using the **Simple** workflow in the
AWS Systems Manager console, you choose an existing Amazon Simple Storage Service (Amazon S3) bucket to which Distributor
uploads your software. Distributor is a tool in AWS Systems Manager. In the
**Advanced** workflow, you must upload .zip files of your
software or assets to an Amazon S3 bucket before you begin. Whether you create a package
by using the **Simple** or **Advanced** workflows
in the console, or by using the API, you must have an Amazon S3 bucket before you start
creating your package. As part of the package creation process, Distributor copies your
installable software and assets from this bucket to an internal Systems Manager store. Because
the assets are copied to an internal store, you can delete or repurpose your Amazon S3
bucket when package creation is finished.

For more information about how to create a bucket, see [Create a Bucket](../../../AmazonS3/latest/userguide/CreatingABucket.md "../../../AmazonS3/latest/userguide/CreatingABucket.md") in the
_Amazon Simple Storage Service Getting Started Guide_. For more information about
how to run an AWS CLI command to create a bucket, see [**mb**](../../../cli/latest/reference/s3/mb.md "../../../cli/latest/reference/s3/mb.md") in the
_AWS CLI Command Reference_.
