

# Upgrading your AWS Managed Microsoft AD
<a name="ms_ad_upgrade_edition"></a>

You can upgrade your Standard edition AWS Managed Microsoft AD to Enterprise edition. The following outlines the differences between Standard and Enterprise editions:
+ **Standard Edition: **AWS Managed Microsoft AD (Standard Edition) is optimized to be a primary directory for small and midsize businesses with up to 5,000 employees. It provides you enough storage capacity to support up to 30,000\* directory objects, such as users, groups, and computers.
+ **Enterprise Edition: **AWS Managed Microsoft AD (Enterprise Edition) is designed to support enterprise organizations with up to 500,000\* directory objects.

\* Upper limits are approximations. Your directory may support more or less directory objects depending on the size of your objects and the behavior and performance needs of your applications.

To upgrade your Standard edition AWS Managed Microsoft AD to Enterprise edition, use the AWS Management Console, the [UpdateDirectorySetup](https://docs.aws.amazon.com/directoryservice/latest/devguide/API_UpdateDirectorySetup.html) API, the [update-directory-setup](https://docs.aws.amazon.com/cli/latest/reference/ds/update-directory-setup.html) AWS CLI command, or [Update-DSDirectorySetup](https://docs.aws.amazon.com/powershell/v5/reference/?page=Update-DSDirectorySetup.html) from AWS Tools for PowerShell.

------
#### [ AWS Management Console ]

To upgrade your Standard edition AWS Managed Microsoft AD to Enterprise edition using the AWS Management Console:

1. Sign in to the AWS Management Console and open the Directory Service console at [https://console.aws.amazon.com/directoryservicev2/](https://console.aws.amazon.com/directoryservicev2/).

1. In the navigation pane, choose **Directories**.

1. Choose the directory ID link for the AWS Managed Microsoft AD directory you want to upgrade to open its **Directory details** page.

1. Choose **Actions**, and then choose **Upgrade edition**.

1. Select **Enterprise edition**, and review the limitations that occur with an upgrade.

1. Type `confirm` in the field to acknowledge the limitations, and then choose **Upgrade**.

------
#### [ API ]

To upgrade your Standard edition AWS Managed Microsoft AD to Enterprise edition:

```
{
   "DirectoryId": "d-1234567890",
   "UpdateType": "SIZE",
   "DirectorySizeUpdateSettings": {
      "DirectorySize": "Large"
   }
}
```

------
#### [ AWS CLI ]

To upgrade your Standard edition AWS Managed Microsoft AD to Enterprise edition:

```
aws ds update-directory-setup \
    --directory-id d-1234567890 \
    --update-type SIZE \
    --directory-size-update-settings DirectorySize=Large
```

------
#### [ PowerShell ]

To upgrade your Standard edition AWS Managed Microsoft AD to Enterprise edition:

```
Update-DSDirectorySetup `
    -DirectoryId d-9a676e4148 `
    -UpdateType SIZE `
    -DirectorySizeUpdateSettings_DirectorySize Large
```

------

There are a few limitations to be aware of when upgrading your AWS Managed Microsoft AD. They are:
+ The upgrade will incur additional cost. See [Directory Service Pricing](https://aws.amazon.com/directoryservice/pricing/) for more information.
+ Once your Active Directory is upgraded, it can't be reverted back to its previous edition.
+ Previous snapshots can't be used to restore the Active Directory after it has been upgraded.
+ The upgrade process requires four to five hours.
+ During the upgrade process, the domain controllers of your AWS Managed Microsoft AD are upgraded one at a time. This can negatively impact your performance and can cause downtime during your maintenance window.
+ The upgrade process will change the hostname of each domain controller instance, but their IP addresses will remain the same.
+ If you are using LDAPS (Lightweight Directory Access Protocol over SSL), the domain controllers will need new certificates.