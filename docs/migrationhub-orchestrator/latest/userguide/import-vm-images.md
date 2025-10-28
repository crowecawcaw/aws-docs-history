AWS Migration Hub will no longer be open to new customers starting November 7, 2025. To continue using the service, sign up prior to November 7, 2025. For capabilities similar to AWS Migration Hub, explore [AWS Transform](https://aws.amazon.com/transform "https://aws.amazon.com/transform").

# Import virtual machine images to AWS template

You can use the _Import virtual machine images to AWS_
template to convert existing images to Amazon Machine Images (AMI) for Amazon EC2.

## Prerequisites

You must meet the following requirements to create a VM import workflow using this
template.

###### AWS Identity and Access Management (IAM) requirements

You need to create resources in IAM for both Migration Hub Orchestrator and VM Import/Export:

- Create an IAM user and attach the required policies to use Migration Hub Orchestrator. For more
  information, see [Create an IAM user](setting-up.md#setting-up-create-iam-user "setting-up.md#setting-up-create-iam-user")
- Create an IAM user and a service role, and attach required policies to use VM Import/Export.
  For more information, see [Required
  permissions](../../../vm-import/latest/userguide/required-permissions.md "../../../vm-import/latest/userguide/required-permissions.md").

###### VM Import/Export requirements

You might need to perform additional tasks to prepare your AWS environment before
importing your image. For more information, see [VM Import/Export Requirements](../../../vm-import/latest/userguide/vmie_prereqs.md "../../../vm-import/latest/userguide/vmie_prereqs.md").

###### Upload images to Amazon S3

Create an Amazon S3 bucket, and add the image files you want to import into the bucket. For more
information about creating an Amazon S3 bucket, see [Creating a bucket](../../../AmazonS3/latest/userguide/create-bucket-overview.md "../../../AmazonS3/latest/userguide/create-bucket-overview.md").

The following considerations and limitations apply:

- The Amazon S3 bucket must be in the same Region as the AWS account in which you are using
  Migration Hub Orchestrator.
- You must have separate folders for each image file format you want to upload in your S3
  bucket.
- Migration Hub Orchestrator supports importing the following image file formats:
  - OVA
  - RAW
  - VHD
  - VHDX
  - VMDK

Each image file type has additional requirements for the S3 bucket, file name, and workflow.

OVA files
The following considerations apply when you import OVA files:

- The folder must be named with the prefix
  `migrationhub-orchestrator-vmie-`folder-name`` and
  must only contain one OVA file.
- The S3 object must end with `.ova`.
- Only one OVA file can be added in one import task.
- You can add up to five import tasks in the workflow.

RAW files
The following considerations apply when you import RAW files:

- The folder must be named with the prefix
  `migrationhub-orchestrator-vmie-`folder-name`` and
  must only contain one RAW file.
- The S3 object must end with `.raw`.
- Only one RAW file can be added in one import task.
- You can add up to five import tasks in the workflow.

VMDK files
The following considerations apply when you import VMDK files:

- The folder must be named with the prefix
  `migrationhub-orchestrator-vmie-`folder-name``.
- The S3 object must end with `.vmdk`.
- The folder must only contain VMDK files.
- The folder can contain up to 21 VMDK files.

VHD files
The following considerations apply when you import VHD files:

- The folder must be named with the prefix
  `migrationhub-orchestrator-vmie-`folder-name``.
- The S3 object must end with `.vhd`.
- The folder must only contain VHD files.
- The folder can contain up to 21 VHD files.

VHDX files
The following considerations apply when you import VHDX files:

- The folder must be named with the prefix
  `migrationhub-orchestrator-vmie-`folder-name``.
- The S3 object must end with `.vhdx`.
- The folder must only contain VHDX files.
- The folder can contain up to 21 VHDX files.

## Create a workflow

1. Go to [https://console.aws.amazon.com/migrationhub/orchestrator/](https://console.aws.amazon.com/migrationhub/orchestrator/ "https://console.aws.amazon.com/migrationhub/orchestrator/"), select **Create
   migration workflow**.
2. On Choose a workflow template page, select **Import virtual images to
   AWS** template.
3. Configure and submit your workflow to begin the VM import.
   - [Details](#details-import-vm-images "#details-import-vm-images")
   - [Source environment configuration](#source-env-config-import-vm-images "#source-env-config-import-vm-images")
   - [Target environment configuration](#target-env-config-import-vm-images "#target-env-config-import-vm-images")

###### Note

You can customize the migration workflow once it has been created. For more information, see
[Migration workflows for Migration Hub Orchestrator](migration-workflows.md "migration-workflows.md").

## Details

Enter a name for your workflow. Optionally, you can enter a description and add tags. If you
intend to import multiple VM images, we recommend adding tags to enhance searchability. For more
information, see [Tagging AWS resources](../../../general/latest/gr/aws_tagging.md "../../../general/latest/gr/aws_tagging.md").

## Source environment configuration

You need to specify the following parameters to configure your workflow.

- **Server IP** – This is an optional parameter where you can provide the
  IP address of the on-premises server that needs to be migrated. You must setup the Migration Hub Orchestrator
  plugin on providing the IP address. This enables Migration Hub Orchestrator to run a validation and detect any
  failure scenarios before import.
- **Disk container** – You must specify the Amazon S3 path to your images
  that you set up in [Prerequisites](#prerequisites-import-vm-images "#prerequisites-import-vm-images"). See the following examples
  for more details.

OVA files
You can use either of the following path style examples for the disk container parameter.

s3://`bucket-name`/migrationhub-orchestrator-vmie-`folder-name`

s3://`bucket-name`/migrationhub-orchestrator-vmie-`folder-name`/`file-name`.ova

RAW files
You can use either of the following path style examples for the disk container parameter.

s3://`bucket-name`/migrationhub-orchestrator-vmie-`folder-name`

s3://`bucket-name`/migrationhub-orchestrator-vmie-`folder-name`/`file-name`.raw

VMDK files
You can use either of the following path style examples for the disk container parameter.

s3://`bucket-name`/migrationhub-orchestrator-vmie-`folder-name`

s3://`bucket-name`/migrationhub-orchestrator-vmie-`folder-name`/`file-name`.vmdk

VHD files
You can use either of the following path style examples for the disk container parameter.

s3://`bucket-name`/migrationhub-orchestrator-vmie-`folder-name`

s3://`bucket-name`/migrationhub-orchestrator-vmie-`folder-name`/`file-name`.vhd

VHDX files
You can use either of the following path style examples for the disk container parameter.

s3://`bucket-name`/migrationhub-orchestrator-vmie-`folder-name`

s3://`bucket-name`/migrationhub-orchestrator-vmie-`folder-name`/`file-name`.vhdx

When more than one disk container is added, Migration Hub Orchestrator runs the workflow sequentially. If
the first disk container fails, you must recover the failed container or create a new
workflow.

- **Add new item** – You can add up to five image tasks for the
  workflow.

## Target environment configuration

This section of the Import virtual machine images to AWS template workflow has optional
parameters for licensing. For more information, refer to the following documentation.

- [Licensing
  options](../../../vm-import/latest/userguide/licensing.md "../../../vm-import/latest/userguide/licensing.md")
- [Boot
  modes](../../../AWSEC2/latest/UserGuide/ami-boot.md "../../../AWSEC2/latest/UserGuide/ami-boot.md")
