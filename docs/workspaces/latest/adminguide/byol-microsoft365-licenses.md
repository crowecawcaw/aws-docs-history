# Microsoft 365 Bring Your Own License

(BYOL) in WorkSpaces Personal

Amazon WorkSpaces allows you to bring your own Microsoft 365 licenses if they meet Microsoft's
licensing requirements. These licenses allow you to install and activate Microsoft 365 Apps
for enterprise software on WorkSpaces that are powered by the following operating systems:

- Windows 10 (Bring Your Own License)
- Windows 11 (Bring Your Own License)
- Windows Server 2016
- Windows Server 2019
- Windows Server 2022
  To use Microsoft 365 Apps for enterprise on WorkSpaces, you must have subscription to Microsoft
  365 E3/E5, Microsoft 365 A3/A5, Microsoft 365 G3/G5, or Microsoft 365 Business
  Premium.

On your Amazon WorkSpaces you can use your Microsoft 365 licenses to install and activate
Microsoft 365 Apps for enterprise, including the following:

- Microsoft Word
- Microsoft Excel
- Microsoft PowerPoint
- Microsoft Outlook
- Microsoft OneDrive
  For more information, see the [full list of Microsoft 365 Apps for enterprise](https://www.microsoft.com/en/microsoft-365/enterprise/microsoft-365-apps-for-enterprise-product?activetab=pivot%3Aoverviewtab&market=af&ranMID=24542&ranEAID=QKfOgZNb5HA&ranSiteID=QKfOgZNb5HA-uvIr8evP5gLQf8n3Z0NLJA&epi=QKfOgZNb5HA-uvIr8evP5gLQf8n3Z0NLJA&irgwc=1&OCID=AIDcmm549zy227_aff_7593_1243925&tduid=%28ir__caugvllhggkfbgesuvvv2g21je2xb3afmz3ilkpl00%29%287593%29%281243925%29%28QKfOgZNb5HA-uvIr8evP5gLQf8n3Z0NLJA%29%28%29&irclickid=_caugvllhggkfbgesuvvv2g21je2xb3afmz3ilkpl00 "https://www.microsoft.com/en/microsoft-365/enterprise/microsoft-365-apps-for-enterprise-product?activetab=pivot%3Aoverviewtab&market=af&ranMID=24542&ranEAID=QKfOgZNb5HA&ranSiteID=QKfOgZNb5HA-uvIr8evP5gLQf8n3Z0NLJA&epi=QKfOgZNb5HA-uvIr8evP5gLQf8n3Z0NLJA&irgwc=1&OCID=AIDcmm549zy227_aff_7593_1243925&tduid=%28ir__caugvllhggkfbgesuvvv2g21je2xb3afmz3ilkpl00%29%287593%29%281243925%29%28QKfOgZNb5HA-uvIr8evP5gLQf8n3Z0NLJA%29%28%29&irclickid=_caugvllhggkfbgesuvvv2g21je2xb3afmz3ilkpl00").

You can also install Microsoft applications not included with Microsoft 365, such as
Microsoft Project, Microsoft Visio, and Microsoft Power Automate on WorkSpaces but you need to bring in your own
additional licenses.

You can install and use Microsoft 365 and other Microsoft applications on primary
WorkSpaces and failover WorkSpaces using [Multi-Region Resilience](multi-region-resilience.md "multi-region-resilience.md").

###### Contents

- [Create WorkSpaces with Microsoft 365 Apps
  for enterprise](#create-workspaces-microsoft365 "#create-workspaces-microsoft365")
- [Migrate your existing WorkSpaces to use
  Microsoft 365 Apps for enterprise](#migrate-workspaces-microsoft365 "#migrate-workspaces-microsoft365")
- [Update your Microsoft 365 Apps for enterprise on
  WorkSpaces](#microsoft365-update "#microsoft365-update")

## Create WorkSpaces with Microsoft 365 Apps

for enterprise

To create WorkSpaces with Microsoft 365 Apps for enterprise, you must create a custom image
with the applications installed, and use it to create a custom bundle. You can use the
bundle to launch new WorkSpaces that have the applications installed. WorkSpaces does not provide
public bundles with Microsoft 365 Apps for enterprise.

###### To create WorkSpaces with Microsoft 365 Apps for enterprise:

1. Open the WorkSpaces console at [https://console.aws.amazon.com/workspaces/v2/home](https://console.aws.amazon.com/workspaces/v2/home "https://console.aws.amazon.com/workspaces/v2/home").
2. Launch a WorkSpace that you want to use as the image for other Microsoft
   application WorkSpaces. This is where you will install your Microsoft applications.
   For more information about launching a WorkSpace, see [Launch a virtual desktop using WorkSpaces](launch-workspaces-tutorials.md "launch-workspaces-tutorials.md").
3. Start the client application at [https://clients.amazonworkspaces.com/](https://clients.amazonworkspaces.com/ "https://clients.amazonworkspaces.com/"), enter the registration code
   from your invitation email, and choose **Register**.
4. When prompted to sign in, enter the user's sign-in credentials, and then
   choose **Sign In**.
5. Install and configure your Microsoft 365 Apps for enterprise.
6. Create a custom image from the WorkSpace, and use it to create a custom
   bundle. For more information about creating custom images and bundles, see
   [Create a custom WorkSpaces image and bundle](create-custom-bundle.md "create-custom-bundle.md").
7. Launch WorkSpaces using the custom bundle that you created. These WorkSpaces have
   Microsoft 365 Apps for enterprise installed.

## Migrate your existing WorkSpaces to use

Microsoft 365 Apps for enterprise

If your WorkSpaces don't have a Microsoft Office license through AWS, you can
install and configure Microsoft 365 Apps for enterprise on your WorkSpaces.

If your WorkSpaces do have a Microsoft Office license through AWS, you must
first deregister your Microsoft Office license before installing Microsoft
365 Apps for enterprise.

###### Important

Uninstalling Microsoft Office applications from your WorkSpaces doesn't deregister the
licenses. To avoid being charged for Microsoft Office licenses, deregister your
WorkSpaces from Microsoft Office applications through AWS by doing either of the
following:

- **Manage applications** (recommended) – You can
  uninstall Microsoft Office version licenses from your WorkSpaces. For more
  information, see [Manage
  applications](manage-applications.md "manage-applications.md"). After you uninstall, you can install Microsoft 365
  Apps for enterprise on your WorkSpaces.
- **Migrate a WorkSpace** – You can migrate a
  WorkSpace from one bundle to another while retaining the data on the user
  volume.
  - Migrate your WorkSpaces to a bundle with an image that doesn’t have a Microsoft Office
    subscription. After the migration is complete, you can install
    Microsoft 365 Apps for enterprise on your WorkSpaces.
  - Or, create a custom WorkSpaces image and bundle that already has Microsoft 365 Apps for enterprise
    installed on the image, and then migrate your WorkSpaces to this new
    custom bundle. After migration is complete, your WorkSpaces users can
    start using Microsoft 365 Apps for enterprise.
  - For more information on how to migrate WorkSpaces, see [Migrate a WorkSpace](migrate-workspaces.md "migrate-workspaces.md").

## Update your Microsoft 365 Apps for enterprise on

WorkSpaces

By default, your WorkSpaces running on the Microsoft Windows Operating System are
configured to receive updates from Windows Update. However, updates for Microsoft 365
Apps for enterprise aren't available using Windows Update. Set up updates to run
automatically from the Office CDN, or use Windows Server Update Services (WSUS) in
conjunction with Microsoft Configuration Manager to update Microsoft 365 Apps for
enterprise. For more information, see [Manage updates to Microsoft 365 Apps with Microsoft Configuration Manager](https://learn.microsoft.com/en-us/deployoffice/updates/manage-microsoft-365-apps-updates-configuration-manager "https://learn.microsoft.com/en-us/deployoffice/updates/manage-microsoft-365-apps-updates-configuration-manager").
To set the frequency of Microsoft 365 application updates, specify an update channel and
set it to Current or Monthly Enterprise to comply with the Microsoft 365 on WorkSpaces
licensing policy.
