# Manage applications in WorkSpaces Personal

After you launch a WorkSpace, you can see the list of all of the application bundles
that are associated with your WorkSpace on the WorkSpaces console.

###### To see the list of all the application bundles associated to your WorkSpace

1. Open the WorkSpaces console at [https://console.aws.amazon.com/workspaces/v2/home](https://console.aws.amazon.com/workspaces/v2/home "https://console.aws.amazon.com/workspaces/v2/home").
2. From the left navigation pane, choose **WorkSpaces**.
3. Select the WorkSpace and choose **View Details**.
4. Under **Applications**, find the list of applications that are associated
   with this WorkSpace, along with their installation status.

###### You can update the application bundles on your WorkSpace in the following ways:

- Install application bundles on your WorkSpace
- Uninstall application bundles from your WorkSpace
- Install application bundles and uninstall a different set of application bundles on your
  WorkSpace

###### Note

- To update application bundles, the WorkSpace must have a status of `AVAILABLE` or
  `STOPPED`.
- Manage applications is only available for Windows WorkSpaces.
- Manage applications is only available for application bundles that are subscribed through
  AWS.

## Supported bundles for Manage applications

Manage applications allows you install and uninstall the following applications on
your WorkSpaces. For Microsoft Office 2016 bundle and Microsoft Office 2019, you can only
uninstall.

- Microsoft Office LTSC Professional Plus 2021
- Microsoft Visio LTSC Professional 2021
- Microsoft Project Professional 2021
- Microsoft Office LTSC Standard 2021
- Microsoft Visio LTSC Standard 2021
- Microsoft Project Standard 2021
- Microsoft Visual Studio Professional 2022
- Microsoft Visual Studio Enterprise 2022

The following table shows the list of supported and unsupported application and operating system combinations:

|                     | Microsoft Office Professional Plus 2016 (32-bit) | Microsoft Office Professional Plus 2019 (64-bit) | Microsoft LTSC Office Professional Plus / Standard 2021 (64-bit) | Microsoft Project Professional / Standard 2021 (64-bit) | Microsoft LTSC Visio Professional / Standard 2021 (64-bit) | Microsoft Visual Studio Professional / Enterprise 2022 |
| ------------------- | ------------------------------------------------ | ------------------------------------------------ | ---------------------------------------------------------------- | ------------------------------------------------------- | ---------------------------------------------------------- | ------------------------------------------------------ |
| Windows Server 2016 | Uninstall                                        | Not supported                                    | Not supported                                                    | Not supported                                           | Not supported                                              | Not supported                                          |
| Windows Server 2019 | Not supported                                    | Uninstall                                        | Install/uninstall                                                | Install/uninstall                                       | Install/uninstall                                          | Not supported                                          |
| Windows Server 2022 | Not supported                                    | Uninstall                                        | Install/uninstall                                                | Install/uninstall                                       | Install/uninstall                                          | Install/uninstall                                      |
| Windows 10          | Uninstall                                        | Uninstall                                        | Install/uninstall                                                | Install/uninstall                                       | Install/uninstall                                          | Install/uninstall                                      |
| Windows 11          | Uninstall                                        | Uninstall                                        | Install/uninstall                                                | Install/uninstall                                       | Install/uninstall                                          | Install/uninstall                                      |

###### Important

- Microsoft Office/Visio/Project must follow the same editions. For example, you cannot mix
  Standard applications with Professional applications.
- Microsoft Office/Visio/Project must follow the same versions. For example, you cannot mix 2019
  applications with 2021 applications.
- Microsoft Office/Visio/Project 2021 Standard/Professional are not supported for
  Value, Graphics, and GraphicsPro WorkSpaces bundles.
- Value, Standard, Graphics, and GraphicsPro WorkSpaces bundles are not supported
  for Microsoft Visual Studio 2022 Enterprise/Professional. Performance bundles
  can be used for Visual Studio workloads that are less resource intensive.
  However, for best results, we recommended using Visual Studio with quad-core or
  higher bundle types. The bundle types Power, PowerPro, General Purpose.4xlarge, General Purpose.8xlarge, Graphics.g4dn, and
  GraphicsPro.g4dn meet this requirement. For more information, see [Visual Studio 2022 Product Family System Requirements](https://learn.microsoft.com/en-us/visualstudio/releases/2022/system-requirements "https://learn.microsoft.com/en-us/visualstudio/releases/2022/system-requirements").
- When you uninstall **Plus applications bundle for Microsoft Office 2016** from your WorkSpaces,
  you will lose access to any Trend Micro solutions that were included as part of that Amazon WorkSpaces bundle. If you want
  to continue using Trend Micro solutions with your Amazon WorkSpaces, you can purchase them separately on the
  [AWS marketplace](https://aws.amazon.com/marketplace/pp/prodview-u2in6sa3igl7c "https://aws.amazon.com/marketplace/pp/prodview-u2in6sa3igl7c").
- In order to install/uninstall Microsoft 365 apps, you need to bring in your own
  tools and installers, Manage application workflow cannot install/uninstall Microsoft 365 apps.
- You can create a custom image of WorkSpaces with applications installed/uninstalled through Manage applications.
- For opt-in Regions, such as Africa (Cape Town), WorkSpaces internet connection must be enabled at the
  directory level.
- Plus applications bundles with Office 2016 or Office 2019 will no longer be supported after October 14, 2025. We recommend migrating your WorkSpaces bundles with those Office version to use Office 2021. For more information, see, [Manage applications in WorkSpaces Personal](manage-applications.md "manage-applications.md").

## Update application bundles on a WorkSpace

1. Open the WorkSpaces console at [https://console.aws.amazon.com/workspaces/v2/home](https://console.aws.amazon.com/workspaces/v2/home "https://console.aws.amazon.com/workspaces/v2/home").
2. In the navigation pane, choose **WorkSpaces**.
3. Select the WorkSpace and choose **Actions**, **Manage applications**.
4. Under **Current applications** you will see a list of application bundles that are already installed on this WorkSpace
   and under **Choose applications** you have a list of application bundles that are available to install on this WorkSpace.
5. To install application bundles on this WorkSpace:
   1. Select an application bundle that you want to install on this WorkSpace, and choose **Associate**.
   2. Repeat the previous step to install other application bundles.
   3. While the application bundles are installing, you will see them under **Current applications**
      with the `Pending install deployment` status.

6. To uninstall application bundles from this WorkSpace:
   1. Under **Choose applications**, select an application bundle that you want to uninstall and
      choose **Disassociate**.
   2. Repeat the previous step to uninstall other application bundles.
   3. While the application bundles are uninstalling, you will see them under **Current applications**
      with the `Pending uninstall deployment` status.

7. To revert the bundles installation or installation state, do one of the following.
   - If you want to revert the bundles from the `Pending uninstall deployment` state, select the application you want to
     revert, then choose **Associate**.
   - If you want to revert the bundles from the `Pending install deployment` state, select the application you want to
     revert, then choose **Disassociate**.

8. After the application bundles you chose to install or uninstall are in pending states, choose **Deploy applications**.

###### Important

After you select **Deploy applications**, the end user session will terminate and WorkSpaces
will not be accessible while the applications are being installed or uninstalled. 9. To confirm your actions, type **confirm**. Choose **force** to install or uninstall applications
bundles that are in an **Error** state. 10. To monitor the progress of your application bundles:

    1. Open the WorkSpaces console at [https://console.aws.amazon.com/workspaces/v2/home](https://console.aws.amazon.com/workspaces/v2/home "https://console.aws.amazon.com/workspaces/v2/home").
    2. In the navigation pane, choose **WorkSpaces**. You can see the status under **Status** including the following.




    	* **UPDATING** - The application bundle update is still ongoing.
    	* **AVAILABLE / STOPPED** - The application bundle update is complete and the WorkSpace is back to its original state.
    3. To monitor the installation or uninstallation status of your application bundles, select the WorkSpace and choose **View Details**.
     Under **Applications**, you can see the status under **Status**, including `Pending install`, `Pending uninstall`,
     and `Installed`.###### Note

If your users observe that their newly installed application bundles through Managed Applications are not license activated, you
can perform a manual WorkSpace reboot. Your users can begin using those applications following a reboot. For additional support,
contact [AWS Support](https://console.aws.amazon.com/support/home#/ "https://console.aws.amazon.com/support/home#/").

## Update Microsoft Visual Studio 2022 workloads on a WorkSpace

By default Microsoft Visual Studio 2022 is installed with the following workloads
and requires 18 GB of hard disk space:

- Visual Studio core editor
- Azure development
- Data storage and processing
- .NET desktop development
- NET Multi-platform App UI development
- ASP.NET and web development
- Node.js development

Users have the flexibility to add or remove workloads and individual components,
allowing them to tailor the application to their specific requirements. It's
important to note that installing additional workloads requires more disk space. To
learn more about workload configurations, see [Modify Visual Studio workloads, components, and language packs](https://learn.microsoft.com/en-us/visualstudio/install/modify-visual-studio?view=vs-2022 "https://learn.microsoft.com/en-us/visualstudio/install/modify-visual-studio?view=vs-2022").

## Managing WorkSpaces modified using Manage applications

After installing or uninstalling application bundles on your WorkSpaces, the following actions can impact existing configurations.

- **Restore a WorkSpace** - Restoring a WorkSpace recreates both the root volume and user volume,
  based on the most recent snapshots of these volumes that were created when the WorkSpace was healthy. Full WorkSpace snapshots are
  taken every 12 hours. For more information, see [Restore a WorkSpace](restore-workspace.md "restore-workspace.md"). Ensure you wait for at least 12 hours before restoring your WorkSpaces that were modified using Manage applications.
  Restoring your WorkSpaces before the next full snapshot, which were modified using Manage applications, will result in the following:
  - The application bundles that were installed on your WorkSpaces using the Manage applications workflow will be
    removed from your WorkSpaces but the license will still be activated and your WorkSpaces will be billed for those applications.
    To get those application bundles back on your WorkSpaces you need to run the Manage application workflow again,
    uninstall the application to start fresh, and then install again.
  - The application bundles that were removed from your WorkSpaces using the Manage applications workflow will be back
    on your WorkSpaces. However, those application bundles won’t work properly because the license activation will be missing.
    In order to get rid of those application bundles, run a manual uninstall of those application bundles from your WorkSpaces.

- **Rebuild a WorkSpace** - Rebuilding a WorkSpace recreates the root volume. For more information, see
  [Rebuild a WorkSpace](rebuild-workspace.md "rebuild-workspace.md").
  Rebuilding your WorkSpaces that were modified using Manage applications will result in the following:
  - The application bundles that were installed on your WorkSpaces using the Manage applications workflow will be removed and
    deactivated from your WorkSpaces. In order to get those applications back on your WorkSpaces you need to run the Manage applications workflow again.
  - The application bundles that were removed from your WorkSpaces via Manage applications workflow will be installed and activated on your WorkSpaces.
    In order to remove those application bundles from your WorkSpaces, you need to run the Manage applications workflow again.

- **Migrate a WorkSpace** - The migration process recreates the WorkSpace by using a new root volume
  from the target bundle image and the user volume from the last available snapshot of the original WorkSpace.
  A new WorkSpace with a new WorkSpace ID is created. For more information, see
  [Migrate a WorkSpace](migrate-workspaces.md "migrate-workspaces.md")
  Migrating your WorkSpaces that were modified using Manage applications will result in the following:
  - All the application bundle from the source WorkSpaces will be removed and deactivated. The new destination WorkSpaces will inherit
    applications from the destination WorkSpaces bundle. Source WorkSpaces application bundles will be billed for the full month but application
    bundles on destination bundle will have a pro-rated bill.
