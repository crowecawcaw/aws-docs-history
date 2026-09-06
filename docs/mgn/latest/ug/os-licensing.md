

NEW - You can now accelerate your migration and modernization with AWS Transform. Read [Getting Started](https://docs.aws.amazon.com/transform/latest/userguide/getting-started.html) in the *AWS Transform User Guide*.

# Operating system licensing
<a name="os-licensing"></a>

Choose whether you want to Bring Your Own Licenses (BYOL) from the source server into the test or cutover instance. 

Choose the **BYOL** option if you are migrating a Linux server. All Linux licenses are BYOL by default. Any RHEL, SUSE or Debian licenses are transferred in their current form to the migrated instance. Make sure to ensure that the terms of your licenses allow this license transfer.

Choose the **BYOL** option if you want to BYOL your Windows licenses. This sets up a dedicated host. All the licenses from the source Windows server are automatically transferred to the Test or Cutover instance. [Learn more about dedicated hosts.](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/dedicated-hosts-overview.html)

**Important**  
If you activate BYOL licensing for Windows, you have to change the **Placement.tenancy** type in the EC2 launch template to **Host**. Otherwise, instance launch fails. 

**Note**  
Windows Desktop Editions require BYOL – [note the specific restrictions for AWS Provided Licenses](https://aws.amazon.com/windows/faq/#buy-win-cl).
If you are using Windows Server Datacenter: Azure Edition, [note the specified restrictions for BYOL](https://www.microsoft.com/licensing/terms/productoffering/WindowsServerStandardDatacenterEssentials/EAEAS#UseRights).