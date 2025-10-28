# Import and export virtual machine images with Image Builder

When you export a VM from its virtualization environment, that process
creates a set of one or more disk container files that act as snapshots of
your VM’s environment, settings, and data. You can use these files to import
your VM, and use it as the base image for your image recipes. To export, you can
create VM disk files as output from your custom image build, and distribute
the files.

Image Builder supports the following file formats for your VM disk containers:

- Open Virtualization Archive (OVA)
- Virtual Machine Disk (VMDK)
- Virtual Hard Disk (VHD/VHDX)
- Raw
  The import uses the disks to create an Amazon Machine Image (AMI) and an Image Builder image
  resource, either of which can serve as the base image for your custom image recipe.
  The VM disks must be stored in S3 buckets for the import. Alternatively, you can import
  from an existing EBS snapshot.

In the Image Builder console, you can import the image directly, and then use the output image
or AMI in your recipes, or you can specify import parameters when you are creating your
recipe or recipe version. For more information about importing as part of your image recipe,
see [VM import configuration](create-image-recipes.md#import-vm-recipe-console-config "create-image-recipes.md#import-vm-recipe-console-config").

## Import a VM into Image Builder

Image Builder integrates with the Amazon EC2 VM Import/Export API to enable the import process to run
asynchronously in the background. Image Builder references the task ID from the VM import to track its progress, and
creates an Image Builder image resource as output. This allows you to reference the
Image Builder image resource in your recipes before the VM import finishes.

Console
To import a VM with the Image Builder console, follow these steps:

1. Open the EC2 Image Builder console at
   [https://console.aws.amazon.com/imagebuilder/](https://console.aws.amazon.com/imagebuilder/ "https://console.aws.amazon.com/imagebuilder/").
2. Choose **Images** from the
   navigation pane.
3. To open the import dialog, choose **Import image**.
4. Enter the following **General** information:
   - Specify a unique **Name** for your image.
   - Specify a **Version** for the base image. Use the
     following format: `*major*.*minor*.*patch*`.

5. Choose the import type: **VM import**.
6. Provide details for each of the following sections on the **Import image**
   page. Then choose **Import image** when you're done.

###### Base image operating system

1. Select the **Image Operating System (OS)** option that
   matches your VM OS platform.
2. Select the **OS version** that matches the version for
   your VM from the list.

###### VM import configuration

1. When you export your VM from its virtualization environment, that process creates a
   set of one or more disk container files. These act as snapshots of your VM’s
   environment, settings, and data. You can use these files to import your VM as
   the base image for your image recipe. For more information about importing VMs
   in Image Builder, see [Import and export VM images](vm-import-export.md "vm-import-export.md").

To specify the location of your import source, follow these steps:

 

###### Import source

Specify the source for the first VM image disk container or snapshot to import in
the **Disk container 1** section.

    1. **Source** – This can be either an
     S3 bucket, or an EBS snapshot.
    2. **Select S3 location of disk** – Enter
     the location in Amazon S3 where your disk images are stored. To browse for the location,
     choose **Browse S3**.
    3. To add a disk container, choose **Add disk container**.

2. ###### IAM role

To associate an IAM role with your VM import configuration, select the role from the
**IAM role** dropdown list, or choose **Create new role**
to create a new one. If you create a new role, the IAM Roles console page opens in a
separate tab. 3. ###### Advanced settings – _optional_

The following settings are optional. With these settings, you can configure
encryption, licensing, tags, and more for the base image that the import
creates.

###### Base image architecture

To specify the architecture of your VM import source, select a value
from the **Architecture** list.

###### Encryption

If your VM disk images are encrypted, you must provide a key to use for the import
process. To specify a KMS key for the import, select a value from the
**Encryption (KMS key)** list. The list contains
KMS keys that your account has access to in the current Region.

###### License management

When you import a VM, the import process automatically detects the VM OS and
applies the appropriate license to the base image. Depending on your OS
platform, the license types are as follows:

    * **License included** – An appropriate AWS
     license for your platform is applied to your base image.
    * **Bring your own license (BYOL)** – Retains
     the license from your VM, if applicable.

To attach license configurations created with AWS License Manager to your base image, select from
the **License configuration name** list. For more information about License Manager,
see Working with AWS License Manager

###### Note

    * License configurations contain licensing rules based on the terms of your
     enterprise agreements.
    * Linux only supports BYOL licenses.

###### Tags (base image)

Tags use key-value pairs to assign searchable text to your Image Builder resource. To specify
tags for the imported base image, enter key-value pairs using the **Key**
and **Value** boxes.

To add a tag, choose **Add tag**. To remove a tag, choose
**Remove tag**.

AWS CLI
To import a VM from disks into an AMI and create an Image Builder image resource that
you can reference right away, follow these steps from the AWS CLI:

1. Initiate a VM import, with the Amazon EC2 VM Import/Export **import-image**
   command in the AWS CLI. Make note of the task ID that is returned in the command
   response. You'll need it for the next step. For more information, see
   [Importing a VM as an
   image using VM Import/Export](../../../vm-import/latest/userguide/vmimport-image-import.md "../../../vm-import/latest/userguide/vmimport-image-import.md") in the _VM Import/Export User Guide_.
2. ###### Create a CLI input JSON file

To streamline the Image Builder **import-vm-image**
command that is used in the AWS CLI, we create a JSON file that contains
all of the import configuration that we want to pass into the command.

###### Note

The naming convention for the data values in the JSON file follows the
pattern that is specified for the Image Builder API operation request parameters. To review the API operation request
parameters, see the
[ImportVmImage](../APIReference/API_ImportVmImage.md "../APIReference/API_ImportVmImage.md")
operation in the _EC2 Image Builder API Reference_.

To provide the data values as command line parameters, refer to the
parameter names specified in the _AWS CLI Command Reference_. to the Image Builder **import-vm-image**
command as options.

Here is a summary of the parameters that we specify in this example:

    * name (string, required) –
     The name for the Image Builder image resource to create as output from the import.
    * semanticVersion (string, required) –
     The semantic version for the output image that specifies the version
     in the following format, with numeric values in each position to indicate
     a specific version: <major>.<minor>.<patch>. For example,
     `1.0.0`. To learn more about semantic versioning for Image Builder resources, see
     [Semantic versioning in Image Builder](ibhow-semantic-versioning.md "ibhow-semantic-versioning.md").
    * description (string) –
     The description of the image recipe.
    * platform (string, required) –
     The operating system platform for the imported VM.
    * vmImportTaskId (string, required) –
     The `ImportTaskId` (AWS CLI) from the Amazon EC2 VM import process. Image Builder
     monitors the import process to pull in the AMI that it creates and build an
     Image Builder image resource that can be used in recipes right away.
    * tags (string map) –
     Tags are key-value pairs that are attached to the import resources. Up
     to 50 key-value pairs are allowed.

Save the file as `import-vm-image.json`, to use in the
Image Builder **import-vm-image** command.

```
{
    "name": "example-request",
    "semanticVersion": "1.0.0",
    "description": "vm-import-test",
    "platform": "Linux",
    "vmImportTaskId": "import-ami-01ab234567890cd1e",
    "tags": {
    	"Usage": "VMIE"
    }
}
```

3. ###### Import the image

Run the **[import-vm-image](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/imagebuilder/import-vm-image.html "https://awscli.amazonaws.com/v2/documentation/api/latest/reference/imagebuilder/import-vm-image.html")**
command, with the file that you created as input:

```
aws imagebuilder import-vm-image --cli-input-json file://`import-vm-image.json`
```

###### Note

    * You must include the `file://` notation
     at the beginning of the JSON file path.
    * The path for the JSON file should follow the appropriate
     convention for the base operating system where you are running
     the command. For example, Windows uses the backslash (\) to
     refer to the directory path, while Linux and macOS use the forward slash (/).

## Distribute VM disks from your image build from the AWS CLI

You can set up distribution of supported VM disk format files to S3 buckets in target
Regions as part of your regular image build process, using Image Builder distribution
configurations in the AWS CLI. For more information, see [Example: Create
distribution settings for output VM disks from the AWS CLI](cr-upd-ami-distribution-settings.md#cli-create-vm-dist-config "cr-upd-ami-distribution-settings.md#cli-create-vm-dist-config").
