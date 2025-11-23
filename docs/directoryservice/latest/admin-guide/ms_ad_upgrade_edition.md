# Upgrading your AWS Managed Microsoft AD

You can upgrade your Standard edition AWS Managed Microsoft AD to Enterprise edition. The following
outlines the differences between Standard and Enterprise editions:

- **Standard Edition:** AWS Managed Microsoft AD (Standard Edition)
  is optimized to be a primary directory for small and midsize businesses with up to
  5,000 employees. It provides you enough storage capacity to support up to 30,000\*
  directory objects, such as users, groups, and computers.
- **Enterprise Edition:** AWS Managed Microsoft AD (Enterprise
  Edition) is designed to support enterprise organizations with up to 500,000\*
  directory objects. \* Upper limits are approximations. Your directory may support more or less directory
  objects depending on the size of your objects and the behavior and performance needs of your
  applications.

To upgrade your Standard edition AWS Managed Microsoft AD to Enterprise edition, use [UpdateDirectorySetup](../devguide/API_UpdateDirectorySetup.md "../devguide/API_UpdateDirectorySetup.md") from the API, [update-directory-setup](../../../cli/latest/reference/ds/update-directory-setup.md "../../../cli/latest/reference/ds/update-directory-setup.md")
from the AWS CLI, or [Update-DSDirectorySetup](../../../powershell/v5/reference.md "../../../powershell/v5/reference.md") from AWS Tools for PowerShell.

API
To upgrade your Standard edition AWS Managed Microsoft AD to Enterprise
edition:

```
{
   "DirectoryId": "d-1234567890",
   "UpdateType": "SIZE",
   "DirectorySizeUpdateSettings": {
      "DirectorySize": "Large"
   }
}
```

AWS CLI
To upgrade your Standard edition AWS Managed Microsoft AD to Enterprise
edition:

```
aws ds update-directory-setup \
    --directory-id d-1234567890 \
    --update-type SIZE \
    --directory-size-update-settings DirectorySize=Large
```

PowerShell
To upgrade your Standard edition AWS Managed Microsoft AD to Enterprise
edition:

```
Update-DSDirectorySetup `
    -DirectoryId d-9a676e4148 `
    -UpdateType SIZE `
    -DirectorySizeUpdateSettings_DirectorySize Large
```

###### Note

Multi-region replication is only available in AWS Managed Microsoft AD Enterprise edition for
the following regions:

- US East (Ohio)
- US East (N. Virginia)
- US West (N. California)
- US West (Oregon)
- Asia Pacific (Mumbai)
- Asia Pacific (Osaka)
- Asia Pacific (Seoul)
- Asia Pacific (Singapore)
- Asia Pacific (Sydney)
- Asia Pacific (Thailand)
- Asia Pacific (Tokyo)
- Canada (Central)
- China (Beijing)
- China (Ningxia)
- Mexico (Central)
- Europe (Frankfurt)
- Europe (Ireland)
- Europe (London)
- Europe (Paris)
- Europe (Stockholm)
- South America (São Paulo)
- AWS GovCloud (US-West)
- AWS GovCloud (US-East)

[Show moreShow less](# "#")There are a few limitations to be aware of when upgrading your AWS Managed Microsoft AD. They
are:

- The upgrade will incur additional cost. See [Directory Service Pricing](https://aws.amazon.com/directoryservice/pricing/ "https://aws.amazon.com/directoryservice/pricing/") for more
  information.
- Once your Active Directory is upgraded, it can't be reverted back to its previous
  edition.
- Previous snapshots can't be used to restore the Active Directory after it has been
  upgraded.
- Upgrades occur at a scheduled date and time agreed upon with Support. Upgrades occur
  between Monday through Friday, 9 AM - 5 PM Pacific Standard Time.
- The upgrade process requires four to five hours.
- During the upgrade process, the domain controllers of your AWS Managed Microsoft AD are
  upgraded one at a time. This can negatively impact your performance and can cause
  downtime during your maintenance window.
- The upgrade process will change the hostname of each domain controller instance,
  but their IP addresses will remain the same.
- If you are using LDAPS (Lightweight Directory Access Protocol over SSL), the
  domain controllers will need new certificates.
