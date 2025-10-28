# Convert a license type for Windows

and SQL Server in License Manager

You can use either the License Manager Console or the AWS CLI to convert the license type of
eligible Windows and SQL Server instances.

###### Topics

- [License type conversion limits](#conversion-limits "#conversion-limits")
- [Convert a license type using the License Manager
  console](#conversion-console "#conversion-console")
- [Convert a license type using the AWS CLI](#conversion-cli "#conversion-cli")

## License type conversion limits

###### Important

The use of Microsoft software is subject to the licensing terms of
Microsoft. You are responsible for complying with Microsoft licensing terms.
This documentation is provided for convenience, and you are not entitled to
rely on its description. This documentation does not constitute legal
advice. If you have questions about your licensing rights to Microsoft
software, consult with your legal team, Microsoft, or your Microsoft
reseller.

License Manager restricts the types of license conversions that you can create in
accordance with the Microsoft Service Provider License Agreement (SPLA). Some of
the restrictions that license type conversion is subject to are listed as
follows. This is not a comprehensive list and is subject to change.

- The Amazon EC2 instance must be launched from your own virtual machine (VM)
  image.
- License-included SQL Server cannot be run on a Dedicated Host.
- A license-included SQL Server instance must have at least 4
  vCPUs.

## Convert a license type using the License Manager

console

You can use the License Manager console to convert a license type.

###### Note

Only instances that are in a stopped state and have been associated by
AWS Systems Manager Inventory are displayed.

###### To start a license type conversion in the console

1. Open the License Manager console at [https://console.aws.amazon.com/license-manager/](https://console.aws.amazon.com/license-manager/ "https://console.aws.amazon.com/license-manager/") .
2. From the left navigation pane, choose **License type
   conversion**, then choose **Create license type
   conversion**.
3. For **Source operating system**, choose the platform of the
   instance you want to convert:
   - **RHEL**
   - **RHEL for SAP**
   - **Ubuntu LTS**
   - **Windows BYOL**
   - **Windows license included**

4. (Optional) Filter the available instances by specifying a value for
   **Instance ID** or **Usage operation
   value**.
5. Select the instances whose licenses you want to convert, and then
   choose **Next**.
6. Enter the **Usage operation value** for the license
   type, select the license that you are converting to, and choose
   **Next**.
7. Verify that you are satisfied with your license type conversion
   configuration and choose **Start conversion**.

You can view the status of your license type conversion from the license type
conversion panel. The Conversion status column displays the status of the
conversion as **In progress**, **Completed**,
or **Failed**.

###### Important

If you convert Windows Server from license included to BYOL, you must
activate Windows according to your Microsoft license agreement. See [Convert Windows Server from license included to BYOL](#convert-to-byol "#convert-to-byol") for more
information.

## Convert a license type using the AWS CLI

To start a license type conversion in the AWS CLI:

###### Determine the license type of your instance

1. Verify that you have installed and set up the AWS CLI. For more
   information, see [Installing,
   updating, and uninstalling the AWS CLI](../../../cli/latest/userguide/cli-chap-install.md "../../../cli/latest/userguide/cli-chap-install.md") and [Configuring the
   AWS CLI](../../../cli/latest/userguide/cli-chap-configure.md "../../../cli/latest/userguide/cli-chap-configure.md").

###### Important

You might need to update the AWS CLI to run certain commands and
receive all required output in the following steps. 2. Verify that you have permissions to run the
`create-license-conversion-task-for-resource` AWS CLI
command. For help with this, see [Create IAM policies for License Manager](identity-access-management.md#iam-policy-examples "identity-access-management.md#iam-policy-examples"). 3. To determine the license type currently associated with your instance,
run the following AWS CLI command. Replace the instance ID with the ID of
the instance for which you want to determine the license type.

```
aws ec2 describe-instances --instance-ids `<instance-id>` --query "Reservations[*].Instances[*].{InstanceId: InstanceId, PlatformDetails: PlatformDetails, ProductCode: ProductCode, UsageOperation: UsageOperation, UsageOperationUpdateTime: UsageOperationUpdateTime}"
```

4. The following is an example response to the
   `describe-instances` command. Note that the
   `UsageOperation` value is the billing information code
   associated with the license. The `UsageOperationUpdateTime`
   is the time when the billing code was updated. For more information, see
   [DescribeInstances](../../../AWSEC2/latest/APIReference/API_DescribeInstances.md "../../../AWSEC2/latest/APIReference/API_DescribeInstances.md") in the _Amazon EC2
   API reference_.

```
`"InstanceId": "i-0123456789abcdef",
"Platform details": "Windows with SQL Server Enterprise",
"UsageOperation": "RunInstances:0800",
"UsageOperationUpdateTime: "2021-08-16T21:16:16.000Z"`
```

###### Note

The usage operation for Windows Server with SQL Server Enterprise BYOL is
the same as the usage operation for Windows BYOL because they are
identically billed.

###### Convert Windows Server from license included to

BYOL

When you convert Windows Server from license included to BYOL, License Manager does
not automatically activate Windows. You must switch the KMS server for your
instance from the AWS KMS server to your own KMS server.

###### Important

In order to convert from license included to BYOL, the original Amazon EC2
instance must be launched from your own virtual machine (VM) image. For
more information about converting a VM to Amazon EC2, see [VM Import/Export](../../../vm-import/latest/userguide/vmimport-image-import.md#import-vm-image "../../../vm-import/latest/userguide/vmimport-image-import.md#import-vm-image"). Instances that were originally launched
from an Amazon Machine Image (AMI) are not eligible for license
conversion to BYOL.

Check your Microsoft license agreement to determine what methods you can
use to activate Microsoft Windows Server. For example, if you are using a
KMS server, you must obtain the address of your KMS server from the original
BYOL configuration of the instance.

1. To convert the license type of your instance, run the following
   command, replacing the ARN with the ARN of the instance you want to
   convert:

```
aws license-manager create-license-conversion-task-for-resource \
	--resource-arn `<instance_arn>` \
	--source-license-context UsageOperation=RunInstances:0002 \
	--destination-license-context UsageOperation=RunInstances:0800
```

2. To activate Windows after you convert your license, you must point the
   Windows Server KMS server for your operating system to your own KMS
   servers. Log in to the Windows instance and run the following
   command:

```
slmgr.vbs /skms `<your-kms-address>`
```

###### Convert Windows Server from BYOL to license

included

When you convert Windows Server from BYOL to license included, License Manager
automatically switches the KMS server for your instance to the AWS KMS
server.

To convert the license type of your instance from BYOL to license included,
run the following command, replacing the ARN with the ARN of the instance you
want to convert:

```
aws license-manager create-license-conversion-task-for-resource \
	--resource-arn `<instance_arn>` \
	--source-license-context UsageOperation=RunInstances:0800 \
	--destination-license-context UsageOperation=RunInstances:0002
```

###### Convert both Windows Server and SQL Server from BYOL to

license included

You can switch multiple products at the same time. For example, you can
convert both Windows Server and SQL Server in one license type conversion.

To convert the license type of your Windows Server instance from BYOL to
license included, and SQL Server Standard from BYOL to license included, run the
following command, replacing the ARN with the ARN of the instance you want to
convert:

```
aws license-manager create-license-conversion-task-for-resource \
	--resource-arn `<instance_arn>` \
	--source-license-context UsageOperation=RunInstances:0800 \
	--destination-license-context UsageOperation=RunInstances:0006
```
