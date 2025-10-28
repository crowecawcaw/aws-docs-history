# Operating System

If you plan on using Windows other than via Amazon EC2 for Windows Server, then ensure you have the appropriate licenses in place and the appropriate tenancy type selected. For more details, refer to your licensing terms and conditions, and see [Windows on AWS](https://aws.amazon.com/windows/ "https://aws.amazon.com/windows/").

A base AMI is required to launch an Amazon EC2 instance. For SAP workloads on Windows, you must have a minimum of Windows Server 2012 R2 to be supported as previous versions of Windows Server are now out of support by SAP. If you are using BYOL instead of license-included for Windows Server, you must create your own AMI. For details, see the [Windows on AWS licensing documentation](https://aws.amazon.com/windows/resources/licensing/ "https://aws.amazon.com/windows/resources/licensing/"). Ensure that you have access to the appropriate Windows Server AMIs before proceeding further.

As with any operating system, we recommend you keep the OS up-to-date with the latest patches. You can also refer to [SAP Note 2325651: Required Windows Patches for SAP Operations](https://launchpad.support.sap.com/#/notes/2325651 "https://launchpad.support.sap.com/#/notes/2325651").
