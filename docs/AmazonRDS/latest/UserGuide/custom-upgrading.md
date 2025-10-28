# Upgrading a DB instance for Amazon RDS Custom for Oracle

You can upgrade an Amazon RDS Custom DB instance by modifying it to use a new custom engine version (CEV). For general information about upgrades,
see [Upgrading
a DB instance engine version](USER_UpgradeDBInstance.md "USER_UpgradeDBInstance.md").

###### Topics

- [Overview of upgrades in RDS Custom for Oracle](#custom-upgrading.overview "#custom-upgrading.overview")
- [Requirements for RDS Custom for Oracle upgrades](#custom-upgrading-reqs "#custom-upgrading-reqs")
- [Considerations for RDS Custom for Oracle database
  upgrades](custom-upgrading-considerations.md "custom-upgrading-considerations.md")
- [Considerations for RDS Custom for Oracle OS
  upgrades](custom-upgrading-considerations-os.md "custom-upgrading-considerations-os.md")
- [Viewing valid CEV upgrade targets for RDS Custom for Oracle
  DB instances](custom-upgrading-target.md "custom-upgrading-target.md")
- [Upgrading an RDS Custom for Oracle DB instance](custom-upgrading-modify.md "custom-upgrading-modify.md")
- [Viewing pending database upgrades for RDS Custom DB
  instances](custom-upgrading-pending.md "custom-upgrading-pending.md")
- [Troubleshooting an upgrade failure for an RDS Custom for Oracle DB instance](custom-upgrading-failure.md "custom-upgrading-failure.md")

## Overview of upgrades in RDS Custom for Oracle

With RDS Custom for Oracle, you can patch either your Oracle database or your DB instance operating
system (OS) by creating new CEVs and then modifying your instance to use the new
CEV.

###### Topics

- [CEV upgrade options](#custom-upgrading.overview.cev-options "#custom-upgrading.overview.cev-options")
- [Patching without CEVs](#custom-upgrading.overview.no-cevs "#custom-upgrading.overview.no-cevs")
- [General steps for patching
  your DB instance with a CEV](#custom-upgrading.overview.general-steps "#custom-upgrading.overview.general-steps")

### CEV upgrade options

When you create a CEV for an upgrade, you have the following mutually exclusive options:

**Database only**

Reuse the Amazon Machine Image (AMI) currently in use by your DB instance,
but specify different database binaries. RDS Custom allocates a new binary
volume and then attaches it to the existing Amazon EC2 instance. RDS Custom
replaces the entire database volume with a new volume that uses your
target database version.

**OS only**

Reuse the database binaries currently in use by your DB instance, but
specify a different AMI. RDS Custom allocates a new Amazon EC2 instance, and then
attaches the existing binary volume to the new instance. The existing
database volume is retained.

If you want to upgrade both the OS and database, you must upgrade the CEV twice.
You can either upgrade the OS and then the database or upgrade the database and then
the OS.

###### Warning

When you patch your OS, you lose your root volume data and any existing OS
customization. Thus, we strongly recommend that you don't use the root volume
for installations or for storing permanent data or files. We also recommend that
you back up your data before the upgrade.

### Patching without CEVs

We strongly recommend that you upgrade your RDS Custom for Oracle DB instance using CEVs. RDS Custom for Oracle
automation synchronizes the patch metadata with the database binary on your
DB instance.

In special circumstances, RDS Custom supports applying a "one-off" database patch
directly to the underlying Amazon EC2 instance directly using the OPatch utility. A valid
use case might be a database patch that you want to apply immediately, but the
RDS Custom team is upgrading the CEV feature, causing a delay. To apply a database patch
manually, perform the following steps:

1. Pause RDS Custom automation.
2. Apply your patch to the database binaries on the Amazon EC2 instance.
3. Resume RDS Custom automation.

A disadvantage of the preceding technique is that you must apply the database
patch manually to every instance that you want to upgrade. In contrast, when you
create a new CEV, you can create or upgrade multiple DB instances using the same
CEV.

### General steps for patching

your DB instance with a CEV

Whether you patch the OS or your database, perform the following basic
steps:

1.  Create a CEV that contains either of the following, depending on whether
    you're patching the database or OS:

        * The Oracle Database RU that you want to apply to your DB instance
        * A different AMI–either the latest available or one that you
         specify–and an existing CEV to use as a source

    Follow the steps in [Creating a CEV](custom-cev.md "custom-cev.md").

2.  (Optional for database patching) Check available engine version upgrades
    by running `describe-db-engine-versions`.
3.  Start the patching process by running
    `modify-db-instance`.

The status of the instance being patched differs as follows:

    * While RDS is patching the database, the status of the DB instance
     changes to **Upgrading**.
    * While RDS is patching the OS, the status of the DB instance changes to
     **Modifying**.

When the DB instance has the status **Available**, patching is
complete. 4. Confirm that your DB instance uses the new CEV by running
`describe-db-instances`.

## Requirements for RDS Custom for Oracle upgrades

When upgrading your RDS Custom for Oracle DB instance to a target CEV, make sure you meet the following
requirements:

- The target CEV to which you are upgrading must exist.
- You must upgrade either the OS or the database in a single operation. Upgrading
  both the OS and the database in a single API call isn't supported.
- The target CEV must use the installation parameter settings that are in the
  manifest of the current CEV. For example, you can't upgrade a database that uses the
  default Oracle home to a CEV that uses a nondefault Oracle home.
- For database upgrades, the target CEV must use a new minor database version, not a
  new major version. For example, you can't upgrade from an Oracle Database 12c
  CEV to an Oracle Database 19c CEV. But you can upgrade from version
  21.0.0.0.ru-2023-04.rur-2023-04.r1 to version
  21.0.0.0.ru-2023-07.rur-2023-07.r1.
- For OS upgrades, the target CEV must use a different AMI but have the same major
  version.
