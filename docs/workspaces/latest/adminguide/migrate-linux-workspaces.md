

# Migrate a Linux WorkSpace to a different operating system
<a name="migrate-linux-workspaces"></a>

You can migrate an existing Linux WorkSpace to a different Linux operating system bundle while preserving the user's home directory, files, and data. Migration replaces the root volume (operating system) with a new bundle while keeping the user volume (`/home`) intact. This is different from a rebuild, which refreshes the root volume with the same OS bundle.

The Migrate WorkSpace feature handles the entire process automatically, including file ownership correction and desktop environment cleanup when needed.

**Topics**
+ [Supported migration paths](#linux-migration-paths)
+ [Prerequisites](#linux-migration-prerequisites)
+ [How to migrate a WorkSpace](#linux-migration-how-to)
+ [Post-migration verification](#linux-migration-verification)
+ [What happens during migration](#linux-migration-during)
+ [Migrating from Amazon Linux 2](#linux-migration-from-al2)
+ [Migrating between modern distributions](#linux-migration-modern-distros)
+ [What users keep and what changes](#linux-migration-preserved)
+ [Auto-stop and always-on WorkSpaces](#linux-migration-autostop-alwayson)
+ [Known limitations](#linux-migration-limitations)
+ [Troubleshooting](#linux-migration-troubleshooting)

## Supported migration paths
<a name="linux-migration-paths"></a>

The following table shows the supported source and target operating systems for Linux WorkSpace migration.


| Source OS | Ubuntu 22.04 | Ubuntu 22.04 Graphics | Ubuntu 24.04 | RHEL 8 | RHEL 9 | Rocky 8 | Rocky 9 | 
| --- | --- | --- | --- | --- | --- | --- | --- | 
| Amazon Linux 2 (PCoIP) | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | 
| Amazon Linux 2 (WSP) | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | 
| Ubuntu 22.04 | — | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | 
| Ubuntu 22.04 Graphics | ✓ | — | ✓ | ✓ | ✓ | ✓ | ✓ | 
| Ubuntu 24.04 | ✓ | ✓ | — | ✓ | ✓ | ✓ | ✓ | 
| RHEL 8 | ✓ | ✓ | ✓ | — | ✓ | ✓ | ✓ | 
| RHEL 9 | ✓ | ✓ | ✓ | ✓ | — | ✓ | ✓ | 
| Rocky 8 | ✓ | ✓ | ✓ | ✓ | ✓ | — | ✓ | 
| Rocky 9 | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | — | 

**Amazon Linux 2** is a valid migration source but is not a valid migration target. Amazon Linux 2 has reached end-of-life and new WorkSpaces cannot be created with AL2 bundles.

All migration paths between Ubuntu, RHEL, and Rocky Linux are supported in both directions. You can upgrade (for example, RHEL 8 → RHEL 9) or downgrade (for example, Ubuntu 24.04 → Ubuntu 22.04). You can also migrate across distribution families (for example, Rocky 9 → Ubuntu 24.04 or RHEL 9 → Rocky 8). The only restriction is that you cannot migrate a WorkSpace to the same bundle it is already using.

Migrations from Amazon Linux 2 require automatic user ID ownership correction and desktop environment cleanup. Migrations between all other distributions (Ubuntu, RHEL, Rocky) do not require ownership correction because these distributions all use SSSD for Active Directory integration, which assigns stable user IDs.

## Prerequisites
<a name="linux-migration-prerequisites"></a>

Before migrating a Linux WorkSpace, verify the following:
+ **WorkSpace state** — The WorkSpace must be in the `AVAILABLE` state. You cannot migrate a WorkSpace that is starting, stopping, or in an error state.
+ **No Active Directory Forest Trust** — The WorkSpace's directory must not have Forest Trust relationships configured. SSSD, which is used by all modern Linux distributions for Active Directory integration, does not support Forest Trust. If Forest Trust is configured, the migration will fail during provisioning.
+ **Sufficient EBS storage** — The WorkSpace must have sufficient EBS storage for the migration operation.

## How to migrate a WorkSpace
<a name="linux-migration-how-to"></a>

### Using the AWS Management Console
<a name="linux-migration-console"></a>

1. Open the Amazon WorkSpaces console at [https://console.aws.amazon.com/workspaces/](https://console.aws.amazon.com/workspaces/).

1. In the navigation pane, choose **WorkSpaces**.

1. Select the WorkSpace you want to migrate.

1. Choose **Actions**, then choose **Migrate WorkSpace**.

1. Select the target operating system bundle.

1. Choose **Migrate**.

### Using the AWS CLI
<a name="linux-migration-cli"></a>

Use the `migrate-workspace` command to migrate a WorkSpace to a different bundle:

```
aws workspaces migrate-workspace \
    --source-workspace-id ws-1234567890abcdef0 \
    --bundle-id wsb-jttwgmx20 \
    --region us-east-1
```

To find available target bundle IDs:

```
aws workspaces describe-workspace-bundles \
    --query 'Bundles[?contains(Name, `Ubuntu`) || contains(Name, `Rocky`) || contains(Name, `RHEL`)].{Name:Name,BundleId:BundleId}' \
    --output table
```

### Monitoring migration status
<a name="linux-migration-monitoring"></a>

Migration typically takes 20–30 minutes. Monitor the WorkSpace status:

```
aws workspaces describe-workspaces \
    --workspace-ids ws-1234567890abcdef0 \
    --query 'Workspaces[0].State' \
    --output text
```

The WorkSpace transitions through the following states: `AVAILABLE` → `PENDING` → `AVAILABLE` (on success) or `ERROR` (on failure). If migration fails during provisioning, the control plane automatically restores the original WorkSpace.

## Post-migration verification
<a name="linux-migration-verification"></a>

After migration completes, verify the following:

**Check WorkSpace status**

Confirm the WorkSpace is in `AVAILABLE` state in the AWS Console or via the CLI.

**Verify user login**

Have the user log in to the WorkSpace and confirm the desktop loads correctly.

**Check the migration log**

For AL2 migrations, review the migration log for details on what was changed:

```
cat ~/workspace-migration-log-*/user-id-migration.txt
```

This log shows the old and new user IDs, the number of files changed in each phase, and timestamps.

**Check Phase 2 status**

To verify whether the background migration has completed:

```
# Check if the Phase 2 service is still running
systemctl is-active ws-migrate-phase2.service 2>/dev/null

# "inactive" or "not found" means Phase 2 has completed
# "activating" means Phase 2 is still running (Type=simple service)
```

## What happens during migration
<a name="linux-migration-during"></a>

When you initiate a migration, the following steps occur:

1. The user volume (`/home`) is detached from the existing WorkSpace.

1. The existing WorkSpace is disposed.

1. A new WorkSpace is created from the target operating system bundle.

1. The user volume is reattached to the new WorkSpace at `/home`.

1. The new WorkSpace is provisioned: networking is configured, the instance joins Active Directory, and the user's home directory is set up.

1. If migrating from Amazon Linux 2, file ownership is corrected and legacy desktop configuration is cleaned up (see [Migrating from Amazon Linux 2](#linux-migration-from-al2)).

1. The WorkSpace reboots and becomes available for the user to log in.

The user's home directory is stored on a separate EBS volume that is preserved across the migration. All files in `/home/{{username}}` survive the transition, including documents, SSH keys, shell configuration, and application data.

## Migrating from Amazon Linux 2
<a name="linux-migration-from-al2"></a>

Migrations from Amazon Linux 2 involve additional steps that are handled automatically. This section explains what happens and why.

### Why AL2 migrations are different
<a name="linux-migration-al2-why-different"></a>

Amazon Linux 2 uses **Winbind** for Active Directory integration, while all newer Linux distributions (Ubuntu, RHEL, Rocky) use **SSSD**. These two systems assign different POSIX user IDs to the same Active Directory user:
+ **Winbind** (AL2): Assigns user IDs using an unpredictable algorithmic scheme (for example, UID 1000).
+ **SSSD** (modern distributions): Assigns stable user IDs derived from the Active Directory SID (for example, UID 1285401133).

After migration, all files in the user's home directory are owned by the old Winbind UID. The user cannot access their own files until ownership is corrected to match the new SSSD UID.

Additionally, Amazon Linux 2 uses the **MATE** desktop environment (GNOME 2), while newer distributions use **GNOME 3.x**. MATE configuration files conflict with GNOME 3.x and must be cleaned up to ensure a working desktop.

### Two-phase ownership correction
<a name="linux-migration-al2-ownership"></a>

To avoid provisioning timeouts, ownership correction is split into two phases.

**Phase 1 (during provisioning)**

Fixes ownership on desktop-critical files needed for immediate login:
+ Home directory itself
+ SSH keys (`~/.ssh/`)
+ Desktop configuration (`~/.config/`)
+ Shell profiles (`.bashrc`, `.bash_profile`, `.profile`)
+ Any top-level files or directories without world-read permission

Phase 1 completes quickly regardless of the total home directory size, ensuring that provisioning never fails due to large home directories.

**Phase 2 (background, after reboot)**

Fixes ownership on all remaining files:
+ Runs as a systemd service (`ws-migrate-phase2.service`) on boot
+ Retries user resolution for up to 10 minutes if SSSD is not yet ready at boot — if resolution times out, the service stays enabled and retries on next boot
+ Uses idle I/O priority and lowest CPU priority — does not impact user experience
+ The user can log in and work normally while Phase 2 runs
+ Ownership fixes for large directories (10M\+ files) will continue to complete in the background
+ Self-removes the systemd service file after successful completion

### Desktop environment cleanup
<a name="linux-migration-al2-desktop-cleanup"></a>

During migration from AL2, the following MATE desktop configuration files are moved to a backup directory inside the migration log (`~/workspace-migration-log-YYYYMMDD/removed-configuration/`):
+ `~/.config/dconf/user` — MATE-specific dconf database
+ `~/.gconf/` — Legacy GConf directory
+ `~/.config/mate-session/` — MATE session configuration
+ `~/.config/mate-panel/` — MATE panel configuration
+ `~/.local/share/mate-panel/` — MATE panel application data
+ `~/.config/pluma/` — MATE text editor settings
+ `~/.config/caja/` — MATE file manager configuration
+ `~/.config/marco/` — MATE window manager settings
+ `~/.config/gtk-2.0/`, `~/.config/gtk-3.0/` — GTK theme configurations
+ `~/.local/share/recently-used.xbel` — Recent files list

These files are not deleted — they are moved to the backup directory and can be recovered if needed. After cleanup, the desktop loads with the default GNOME 3.x appearance.

### SELinux context restoration
<a name="linux-migration-al2-selinux"></a>

When the migration target is RHEL or Rocky Linux, SELinux security contexts are always restored on the entire user home directory (`/home/{{username}}`), regardless of the source operating system. This applies to all migration paths that target an SELinux-enabled distribution, including:
+ Migrations from non-SELinux sources (Ubuntu, AL2), where files lack SELinux labels entirely.
+ Migrations between SELinux-enabled distributions (for example, RHEL 8 → RHEL 9, Rocky 8 → Rocky 9, or RHEL 9 → Rocky 9). SELinux policy versions and file context definitions can change between major releases.

In all cases, context restoration ensures that files have the correct security labels for the target distribution's SELinux policy.

Context restoration runs in two phases, matching the ownership correction:
+ **Phase 1**: Restores contexts on critical paths (`~/.ssh/`, `~/.config/`) during provisioning.
+ **Phase 2**: Restores contexts on the entire home directory in the background after reboot.

### RFC 2307 home directory auto-correction
<a name="linux-migration-al2-rfc2307"></a>

Active Directory supports RFC 2307 attributes (also known as "Unix Attributes"), which allow administrators to specify POSIX user properties including the home directory path (`unixHomeDirectory`). SSSD respects this attribute, while Winbind on AL2 ignored it and always used `/home/{{username}}`.

When migrating from AL2 to an SSSD-based distribution, the AD user object might have `unixHomeDirectory` set to a different path (for example, `/home/CORP/jsmith`). In that case, SSSD resolves the user's home directory to that AD-specified path. Since the user's actual data lives at `/home/{{username}}` from the AL2 era, the AD-specified path does not exist on the volume.

The migration system detects this situation automatically:

1. After provisioning, SSSD resolves the user's home directory to the AD-specified path.

1. The migration system checks whether this path exists on the user volume.

1. If the AD-specified path does not exist but `/home/{{username}}` does, the system recognizes this as an RFC 2307 path mismatch.

1. The system sets `override_homedir=/home/%u` directly in `/etc/sssd/sssd.conf` (on all domain sections) and restarts SSSD.

1. After SSSD restarts, the user's home directory resolves to `/home/{{username}}`, where the data actually lives.

1. Migration proceeds normally against the existing data.

This correction is permanent — the `override_homedir` setting persists in `sssd.conf` across reboots and future SSSD restarts.

### Enabling RFC 2307 home directory paths after migration
<a name="linux-migration-al2-rfc2307-reverse"></a>

If the migration auto-corrected the RFC 2307 home directory path and you want SSSD to respect the AD `unixHomeDirectory` attribute going forward, you can reverse the override. This is an advanced configuration change that should only be performed if you understand the implications.

**Warning**  
After removing the override, SSSD will use the AD-specified home directory path. You must move the user's data to that path before removing the override, or the user will get an empty home directory.

To restore RFC 2307 home directory paths:

**Step 1: Determine the AD-specified home directory path**

```
# Query the AD unixHomeDirectory attribute
ldapsearch -H ldap://your-dc.example.com -b "dc=example,dc=com" \
    "(sAMAccountName=jsmith)" unixHomeDirectory
```

**Step 2: Move the user's data to the AD-specified path**

```
sudo mkdir -p /home/CORP
sudo mv /home/jsmith /home/CORP/jsmith
```

**Step 3: Remove the override\_homedir setting from /etc/sssd/sssd.conf**

```
sudo sed -i '/^override_homedir/d' /etc/sssd/sssd.conf
```

**Step 4: Restart SSSD**

```
sudo systemctl restart sssd
```

**Step 5: Verify the home directory resolves correctly**

```
getent passwd jsmith
# Should show /home/CORP/jsmith as the home directory
```

**Important**  
After removing the override, future WorkSpace rebuilds and migrations will use the AD-specified path. Ensure the data is at the correct location before the next rebuild or migration.

### User notifications
<a name="linux-migration-al2-notifications"></a>

The migration system uses two notification mechanisms to keep the user informed:

1. **Phase 2 systemd service notifications** — If the user is connected to the desktop when Phase 2 starts or completes, they see notifications directly from the service:
   + **At Phase 2 start:** "Completing file migration in background. You can continue working normally. Some files may remain inaccessible until migration is finished."
   + **At Phase 2 completion:** "File migration completed successfully. All files should now have correct ownership. See \~/workspace-migration-log-\* for details."

1. **XDG autostart login notification** — An autostart entry (`~/.config/autostart/ws-migration-notify.desktop`) runs `/usr/lib/skylight/check-migration-status` on first login after migration. This handles the case where the user connects while Phase 2 is still running or after it has already completed:
   + **If Phase 2 is still running:** "File migration is running in the background. You can continue working normally. Some files may remain inaccessible until migration is finished."
   + **If Phase 2 has completed:** "File migration completed successfully. All files should now have correct ownership. See \~/workspace-migration-log-\* for details."

   The autostart entry is removed after showing the completion notification so it does not run on subsequent logins.

If the user is not connected (for example, an auto-stop WorkSpace that hasn't been accessed), Phase 2 runs silently without error.

## Migrating between modern distributions
<a name="linux-migration-modern-distros"></a>

Migrations between Ubuntu, RHEL, and Rocky Linux distributions do not require user ID ownership correction. All of these distributions use SSSD for Active Directory integration, which assigns stable user IDs derived from the AD SID. The user's files retain correct ownership across the migration.

Common migration paths in this category include:
+ **Cross-family:** Ubuntu 22.04 ↔ RHEL 8/9, Ubuntu 22.04 ↔ Rocky 8/9, RHEL ↔ Rocky
+ **Version upgrades:** Ubuntu 22.04 → Ubuntu 24.04, RHEL 8 → RHEL 9, Rocky 8 → Rocky 9
+ **Graphics bundles:** Any source → Ubuntu 22.04 Graphics. Ubuntu Graphics WorkSpaces can also migrate to any non-Graphics target.

For migrations to RHEL or Rocky Linux targets, SELinux context restoration always runs to ensure files have the correct security labels for the target distribution's SELinux policy. This applies regardless of the source distribution. For files that already have correct labels, the restoration is a no-op.

## What users keep and what changes
<a name="linux-migration-preserved"></a>

### What is preserved
<a name="linux-migration-what-preserved"></a>
+ All files in the home directory (Documents, Downloads, Desktop, and so on)
+ SSH keys and configuration (`~/.ssh/`)
+ Shell configuration (`.bashrc`, `.profile`, `.bash_profile`)
+ Browser bookmarks and profiles (Firefox, Chrome)
+ Application-specific data and configuration (except MATE desktop components on AL2 migrations)

### What changes
<a name="linux-migration-what-changes"></a>
+ The desktop environment resets to the default GNOME 3.x appearance on the target distribution.
+ Legacy MATE desktop preferences are removed and backed up (AL2 migrations only).
+ Desktop icons and panel customizations reset to defaults.
+ Installed applications on the root volume are replaced with the target bundle's default applications. Applications installed by the user in their home directory are preserved.

## Auto-stop and always-on WorkSpaces
<a name="linux-migration-autostop-alwayson"></a>

### Auto-stop WorkSpaces
<a name="linux-migration-autostop"></a>

For WorkSpaces configured with auto-stop (hibernate after idle timeout):

1. Migration completes and the WorkSpace reboots.

1. The Phase 2 background service starts on boot. If SSSD is not yet ready, the service retries user resolution for up to 10 minutes before proceeding.

1. If the user does not connect within the idle timeout (typically 1 hour), Phase 2 runs silently in the background.

1. For typical workloads (fewer than 100,000 files), Phase 2 completes within the idle timeout.

1. The WorkSpace hibernates after Phase 2 completes.

1. When the user next connects, migration is already complete and no notifications are shown.

### Always-on WorkSpaces
<a name="linux-migration-alwayson"></a>

For always-on WorkSpaces:

1. Migration completes and the WorkSpace reboots.

1. The Phase 2 background service starts on boot and runs to completion.

1. The user can connect at any time and work normally — Phase 2 runs at idle priority and does not impact performance.

## Known limitations
<a name="linux-migration-limitations"></a>
+ **Active Directory Forest Trust:** SSSD does not support Forest Trust relationships. WorkSpaces in directories with Forest Trust configured cannot be migrated.
+ **Amazon Linux 2 as target:** AL2 has reached end-of-life and is not a valid migration target. You can only migrate *from* AL2, not *to* AL2.
+ **No rollback:** Completed migrations cannot be rolled back to the previous operating system. If you need to return to the previous OS, you must initiate a new migration (except for AL2, which is not a valid target).
+ **MATE desktop customizations:** When migrating from AL2, MATE desktop preferences are removed. They are backed up in `~/workspace-migration-log-YYYYMMDD/removed-configuration/` but cannot be automatically applied to the GNOME 3.x desktop.
+ **Large home directories:** For home directories with millions of files, Phase 2 background ownership correction may take several hours. The user can work normally during this time, but some files may have incorrect ownership until Phase 2 completes.
+ **File sharing:** If the user has set up file sharing (for example, Samba shares) on their home directory, the ownership change during AL2 migration may affect share permissions. File sharing configurations may need to be re-established after migration.
+ **RFC 2307 override:** If the migration auto-corrected an RFC 2307 home directory path mismatch, the AD `unixHomeDirectory` attribute is overridden via `override_homedir` in `sssd.conf`. See [Enabling RFC 2307 home directory paths after migration](#linux-migration-al2-rfc2307-reverse) if you want SSSD to honor the AD-specified path.

## Troubleshooting
<a name="linux-migration-troubleshooting"></a>

### Migration fails during provisioning
<a name="linux-migration-ts-provisioning"></a>

If the migration fails and the WorkSpace returns to `ERROR` state, the control plane automatically attempts to restore the original WorkSpace. Check the provisioning logs:

```
# Connect to the WorkSpace (if accessible) and check the domain-join log
sudo cat /var/log/skylight/domain-join.log
```

Common causes:
+ **Forest Trust configured:** SSSD cannot join a domain with Forest Trust. Remove Forest Trust before migrating.
+ **AD connectivity issues:** The WorkSpace cannot reach the domain controller. Verify VPC networking and security group rules.
+ **DNS resolution failure:** The WorkSpace cannot resolve the AD domain. Verify DNS configuration.

### User cannot log in after migration
<a name="linux-migration-ts-login"></a>
+ Verify the WorkSpace is in `AVAILABLE` state.
+ Check that the domain join completed successfully: `sudo cat /var/lib/skylight/domain-join-status` should contain `true`.
+ Verify the user can be resolved: `id {{username}}` should return the user's UID and groups.
+ Check SSSD status: `sudo sssctl domain-status {{domain}}` should show `Online status: Online`.

### Desktop appears broken or has wrong theme
<a name="linux-migration-ts-desktop"></a>

This typically occurs when migrating from AL2 and some MATE configuration files were not cleaned up. To reset the desktop to defaults:

```
# Remove remaining desktop configuration
rm -rf ~/.config/dconf/user
rm -rf ~/.gconf

# Log out and log back in
```

### Files have wrong ownership after migration
<a name="linux-migration-ts-ownership"></a>

If files in the home directory are inaccessible after an AL2 migration, Phase 2 may still be running:

```
# Check Phase 2 status
systemctl is-active ws-migrate-phase2.service 2>/dev/null

# Check the migration log for progress
cat ~/workspace-migration-log-*/user-id-migration.txt
```

If Phase 2 has completed but some files still have incorrect ownership, you can manually fix them:

```
# Find files with the old UID and change ownership
sudo find /home/{{username}} -uid {{old-uid}} -exec chown {{username}} {} +
sudo find /home/{{username}} -gid {{old-gid}} -exec chgrp {{username}} {} +
```

### Log file locations
<a name="linux-migration-ts-logs"></a>


| Log | Location | Contents | 
| --- | --- | --- | 
| Domain join log | /var/log/skylight/domain-join.log | Full provisioning workflow including migration Phase 1 | 
| Migration summary | \~/workspace-migration-log-YYYYMMDD/user-id-migration.txt | Old/new UIDs, file counts, timestamps for Phase 1 and Phase 2 | 
| Backed-up MATE configs | \~/workspace-migration-log-YYYYMMDD/removed-configuration/ | MATE desktop files removed during AL2 migration | 
| Phase 1 file list | \~/workspace-migration-log-YYYYMMDD/phase1-processed-files.txt | Files processed during Phase 1 (used by Phase 2 to skip duplicates) | 