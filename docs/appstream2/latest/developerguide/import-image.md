# Import Image

You can create WorkSpaces Applications images by importing your customized EC2 AMIs. Here's how it works:

1. Customize your EC2 AMI using any preferred method including [EC2 Image Builder](../../../imagebuilder.md "../../../imagebuilder.md").
2. Import your customized AMI into WorkSpaces Applications to create a WorkSpaces Applications image
3. Optionally, use Image Builder for additional image customization
   Images created through AMI import are of `type = "custom"`, while WorkSpaces Applications provided images are of `type = "native"`.

You can use stream.\* instance types for images with `type = "native"`. To use any of the following instance type you must import your AMI and create an image with `type = "custom"`.

- GeneralPurpose.\*
- MemoryOptimized.\*
- ComputeOptimized.\*
- Accelerated.\*

## Prerequisites for image import

All these prerequisites are important for a successful workflow execution. Supported AMI configurations and other mandatory requirements are listed below.

### Required AMI Properties

EBS

- Less or equal to 500GB size
  - You can import an AMI with < 200 GB, however, the imported image will use minimum 200GB.

- GP2
  - You can import an AMI with gp2 or gp3 EBS volume type, however, the imported image will use gp2.

- One volume per image
- `/dev/sda1` Root Device Name

- Image Type: Machine
- Architecture: x86_64
- Virtualization Type: HVM
- Boot Mode: UEFI
- TPM Support: v2.0. This is required, Refer to [https://docs.aws.amazon.com/ec2/latest/windows-ami-reference/ami-windows-tpm.html#ami-windows-tpm-find](../../../ec2/latest/windows-ami-reference/ami-windows-tpm.md#ami-windows-tpm-find "../../../ec2/latest/windows-ami-reference/ami-windows-tpm.md#ami-windows-tpm-find") to find a TPM enabled AMI.
- ENA Support: true
- Platform: Windows
- Platform Details: Windows

### Operating System Properties

Windows Server 2022/2025 **Full Base**

- Windows Server **Core** is not supported
- Windows with SQL Server is not supported

Agents

- EC2 Launch V2 Version >= 2.1.1
- SSM Agent required

Drivers

- EC2 ENA Driver Version >= 2.9.0
- EC2 NVMe Driver Version >= 1.6.0

Library Support

- .NET Framework 4.8 or greater
  - Installed by default in Windows Server 2022/2025

- PowerShell 5.1 or greater
  - Installed by default in Windows Server 2022/2025

- Windows Features: Remote Desktop Services Licensing and Remote Desktop Services Session Host must not be installed
- Ports: Ports 8000, 8300, and 8443 must be unblocked and unoccupied
- Boot Mode: UEFI

If you want to use image with graphics instances such as Accelerated.g4dn, Accelerated.g5, Accelerated.G6, or Accelerated.G6e you much install proper GRID driver on your AMI. For more details please refer to [https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/nvidia-GRID-driver.html](../../../AWSEC2/latest/UserGuide/nvidia-GRID-driver.md "../../../AWSEC2/latest/UserGuide/nvidia-GRID-driver.md"). If the drivers are not setup correctly the streaming will work, however, graphics card may not available.

###### Important

"Owner Account Id" of the AMI must be your AWS account id. You cannot import a public EC2 AMI.

Perform any Windows updates and disable automatic Windows updates before importing the image.

Import of encrypted EC2 AMIs is currently not supported

### IAM Role Requirements

###### Important

"Create an IAM role with the following permissions to use for image import:

```
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Sid": "AllowModifyImageAttributeWithTagCondition",
            "Effect": "Allow",
            "Action": "ec2:ModifyImageAttribute",
            "Resource": "*"
        },
        {
            "Sid": "AllowDescribeImages",
            "Effect": "Allow",
            "Action": "ec2:DescribeImages",
            "Resource": "*"
        }
    ]
}
```

Add the following trust relationship for this IAM role

```
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Effect": "Allow",
            "Principal": {
                "Service": "appstream.amazonaws.com"
            },
            "Action": "sts:AssumeRole"
        }
    ]
}
```

## To import an image

1.  Open the WorkSpaces Applications console at [https://console.aws.amazon.com/appstream2](https://console.aws.amazon.com/appstream2 "https://console.aws.amazon.com/appstream2").
2.  In the left navigation pane, choose **Images** and then choose **Image registry**.
3.  Choose **Import Image**.
4.  **AMI ID** - Enter an AMI ID for AMI that you would like to import to WorkSpaces Applications. You can also search for your AMI using this field.
5.  **Image name** - Enter a unique name for the image that will be created because of import operation.
6.  **Display name** _(Optional)_ - Enter a to display for the image.
7.  **Description** _(Optional)_ – Enter a description for the image.
8.  **IAM Role** - Select the IAM role that you have created for image import. For more details refer to [IAM Role Requirements](#iam-role-requirements "#iam-role-requirements").
9.  **Manage WorkSpaces Applications agent** – Select this option if you want to always use the latest WorkSpaces Applications agent version, your streaming instances are automatically updated with the latest features, performance improvements, and security updates that are available from AWS when a new agent version is released.
10. **Runtime validation** _(Optional)_: Select this option and service will provision an instance with the image being imported and run streaming tests.
    - ###### Note

    These streaming tests will be executed in the background, you cannot connect to this instance via WorkSpaces Applications client.
    - We recommend using this option to get higher confidence that your image is suitable for WorkSpaces Applications.
    - You will be billed for the hourly price of that instance.
    - You can avoid running runtime validation if you are re-importing your AMI after making minor changes that may not affect the streaming test, and if runtime validation passed the last time, you imported this AMI.

    - **Choose instance type** _(Optional)_: Select the right instance family, type, and size for running the streaming test. It is recommended that you use the same instance which you are planning to use for fleet creation.

11. **Applications catalog and launch performance manifest** _(Optional)_: Provide details to create applications catalog for your end users and improve the launch performance of your applications.

        * **Application catalog**: To create an application catalog specify details about the applications installed your image. For each application that you plan to stream, you can specify the name, display name, executable file to launch, and icon to display.
        * **Launch performance**: Adding files to the application optimization manifest reduces the time that it takes for the application to launch for the first time on a new fleet instance. The optimization manifest is a line-delimited text file that is per application.

    To learn more refer to [Applications Details](applications-details.md "applications-details.md").

12. **Tags** _(Optional)_ - Choose **Add Tag** and type the key and value for the tag. To add more tags, repeat this step. For more information, see [Tagging Your Amazon WorkSpaces Applications Resources](tagging-basic.md "tagging-basic.md").
13. **Import Image** – Review all the information you have entered and choose **Import Image**. Service will run compatibility checks to make sure AMI is compatible with WorkSpaces Applications.
    - If the static checks fail, you will receive an error straight away.
    - If the static checks pass, your import request will be submitted and depending upon the options you have selected it could take 30-60 min to create a new WorkSpaces Applications image with `type = "custom"`
