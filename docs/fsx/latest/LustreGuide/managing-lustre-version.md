# Managing Lustre versions

FSx for Lustre currently supports multiple long-lerm support (LTS) Lustre versions
released by the Lustre community. Newer LTS versions provide benefits such
as performance enhancements, new features, and support for the latest Linux
kernel versions for your client instances. You can upgrade your file systems
to newer Lustre versions within minutes using the AWS Management Console, AWS CLI, or
AWS SDKs.

FSx for Lustre currently supports Lustre LTS versions 2.10, 2.12, and 2.15.
You can determine the LTS version of your FSx for Lustre file systems using
the AWS Management Console or by using the
[describe-file-systems](../../../cli/latest/reference/fsx/describe-file-systems.md "../../../cli/latest/reference/fsx/describe-file-systems.md") AWS CLI command.

Before you perform a Lustre version upgrade, we recommend that you follow
the steps described in [Best practices for Lustre
version upgrades](#version-upgrade-best-practices "#version-upgrade-best-practices").

###### Topics

- [Best practices for Lustre
  version upgrades](#version-upgrade-best-practices "#version-upgrade-best-practices")
- [Performing the upgrade](#perform-upgrade "#perform-upgrade")

## Best practices for Lustre

version upgrades

We recommend following these best practices before upgrading the Lustre version
of your FSx for Lustre file system:

- **Test in a non-production environment:** Test
  a Lustre version upgrade on a duplicate of your production file system before upgrading your
  production file system. This ensures a smooth upgrade process for your production workload.
- **Ensure client compatibility:** Verify that
  the Linux kernel versions running on your client instances are compatible with the Lustre version
  you plan to upgrade to. See [Lustre file system and client kernel compatibility](lustre-client-matrix.md "lustre-client-matrix.md") for details.
- **Back up your data:**
  - For file systems not linked to S3: We recommend that you create an FSx backup
    before upgrading the Lustre version so that you have a known restore point for your file system.
    If automatic daily backups are enabled on your file system, Amazon FSx will automatically create a
    backup of your file system before upgrading.
  - For file systems linked to S3 We recommend ensuring that all changes have been
    exported to S3 before upgrading. If you have enabled automatic export, check that the
    [AgeOfOldestQueuedMessage](fs-metrics.md#auto-import-export-metrics "fs-metrics.md#auto-import-export-metrics") AutoExport
    metric is zero to confirm that all changes have been successfully exported to S3. If you have not enabled
    automatic export, you can run a manual data repository task (DRT) export to synchronize your
    file system with the S3 bucket before upgrading.

## Performing the upgrade

To upgrade your FSx for Lustre file system to a newer version, follow the
listed steps:

1. **Unmount all clients:** Before initiating
   the upgrade, you must unmount the file system from all client instances accessing
   your file system. You can verify that all clients are successfully unmounted by
   using the `ClientConnections` metric on Amazon CloudWatch - this metric should
   display zero connections. The upgrade process will not proceed if any clients
   remain connected to the file system.

You can view the list of client network identifiers (NIDs) connected to the
file system in the `.fsx/clientConnections` file stored at
the root of your file system. This file is updated every 5 minutes. You can use
the `cat` command to display the contents of the file, as in this example:

```
`cat /test/.fsx/clientConnections`
```

2. **Upgrade the Lustre version:** You can
   upgrade the Lustre version of your FSx for Lustre file system using the Amazon FSx console,
   the AWS CLI, or the Amazon FSx API. We recommend upgrading your file systems to the latest
   Lustre version supported by FSx for Lustre.

**To update the Lustre version of a file system (console)**

    1. Open the Amazon FSx console at [https://console.aws.amazon.com/fsx/](https://console.aws.amazon.com/fsx/ "https://console.aws.amazon.com/fsx/").
    2. In the left navigation pane, choose **File systems**.
     In the **File systems** list, choose the FSx for Lustre file system that you
     want to update the Lustre version for.
    3. For **Actions**, choose **Update file system Lustre version**.
     Or, in the **Summary** panel, choose **Update** next to the file
     system's **Lustre version** field. The **Update file system Lustre version**
     dialog box appears. The **Update file system Lustre version** dialog box appears.
    4. For the **Select a new Lustre version** field, choose a Lustre version.
     The value you choose must be newer than the current Lustre version.
    5. Choose **Update**.**To update the Lustre version of a file system (CLI)**

To update the Lustre version of an FSx for Lustre file system,
use the AWS CLI command [update-file-system](../../../cli/latest/reference/fsx/update-file-system.md "../../../cli/latest/reference/fsx/update-file-system.md"). (The equivalent API action is
[UpdateFileSystem](../APIReference/API_UpdateFileSystem.md "../APIReference/API_UpdateFileSystem.md").) Set the following parameters:

    * Set `--file-system-id` to the ID of the file system that you are updating.
    * Set `--file-system-type-version` to a newer Lustre version for the file system that you are updating.

The following example updates the file system's Lustre version from 2.12 to 2.15:

```
`aws fsx update-file-system \
 --file-system-id `fs-0123456789abcdef0` \
 --file-system-type-version "2.15"`
```

3. **Mount all clients:** You can monitor the progress of
   Lustre version updates by using the **Updates** tab in the Amazon FSx console or
   `describe-file-systems` in the AWS CLI. Once the Lustre version upgrade status shows
   as `Completed`, you can safely remount the file system on your client instances and
   resume your workload.
