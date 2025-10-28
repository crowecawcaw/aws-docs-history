NEW - You can now accelerate your migration and modernization with AWS Transform. Read [Getting Started](../../../transform/latest/userguide/getting-started.md "../../../transform/latest/userguide/getting-started.md") in the _AWS Transform User Guide_.

# Operating system licensing

Choose whether you want to Bring Your Own Licenses (BYOL) from the source server into the
test or cutover instance.

Choose the **BYOL** option if you are migrating a Linux
server. All Linux licenses are BYOL by default. Any RHEL, SUSE or Debian licenses are
transferred in their current form to the migrated instance. Make sure to ensure that the terms
of your licenses allow this license transfer.

Choose the **BYOL** option if you want to BYOL your Windows
licenses. This sets up a dedicated host. All the licenses from the source Windows source server
are automatically transferred to the Test or Cutover instance. [Learn
more about dedicated hosts.](../../../AWSEC2/latest/UserGuide/dedicated-hosts-overview.md "../../../AWSEC2/latest/UserGuide/dedicated-hosts-overview.md")

###### Important

If you activate BYOL licensing for Windows, you have to change the **Placement.tenancy** type in the EC2 launch template to **Host**. Otherwise, instance launch fails.

###### Note

- Windows Desktop Editions require BYOL – [note the specific restrictions for
  AWS Provided Licenses](https://aws.amazon.com/windows/faq/#buy-win-cl "https://aws.amazon.com/windows/faq/#buy-win-cl").
- If you are using Windows Servers datacenter: Azure addition, [note the specified restrictions for BYOL](https://www.microsoft.com/licensing/terms/productoffering/WindowsServerStandardDatacenterEssentials/EAEAS#UseRights "https://www.microsoft.com/licensing/terms/productoffering/WindowsServerStandardDatacenterEssentials/EAEAS#UseRights").
