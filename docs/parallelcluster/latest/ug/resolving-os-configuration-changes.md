# Resolving OS configuration changes that cause errors or failures

When making OS configuration changes to AWS ParallelCluster nodes, various issues can arise that may cause cluster creation, update, or operation failures. This section provides guidance on identifying and resolving common OS configuration-related issues.

## Common OS configuration issues

### Locale configuration issues

One of the most common OS configuration issues is related to locale settings. If you see errors like:

```
cannot change locale (en_US.utf-8) because it has an invalid name
```

This typically occurs when:

- A `yum` installation process was unsuccessful and left locale settings in an inconsistent state
- A user terminated an installation process prematurely
- Locale packages are missing or corrupted

#### How to diagnose

1. Check if you can switch to the pcluster-admin user:

```
`$` `su - pcluster-admin`
```

If you see an error like `cannot change locale...no such file or directory`, this confirms the issue. 2. Check available locales:

```
`$` `localedef --list`
```

If this returns an empty list or doesn't contain the default locale, your locale configuration is broken. 3. Check the last `yum` command:

```
`$` `yum history`
`$` `yum history info #ID`
```

If the last ID doesn't have `Return-Code: Success`, the post-install scripts might not have run successfully.

#### How to resolve

Rebuild the locale by reinstalling the language packs:

```
`$` `sudo yum reinstall glibc-all-langpacks`
```

After the rebuild, verify the issue is fixed by running:

```
`$` `su - pcluster-admin`
```

If no error or warning appears, the issue has been resolved.

### OS package conflicts

When installing custom packages or modifying system packages, conflicts can arise that prevent proper cluster operation.

#### How to diagnose

1. Check the chef-client log for package-related errors:

```
`$` `less /var/log/chef-client.log`
```

2. Look for package dependency conflicts in the cfn-init log:

```
`$` `less /var/log/cfn-init.log`
```

#### How to resolve

1. If a specific package is causing issues, try reinstalling it:

```
`$` `sudo yum reinstall package-name`
```

2. For dependency conflicts, you may need to remove conflicting packages:

```
`$` `sudo yum remove conflicting-package`
```

3. If the issue persists, consider creating a custom AMI with your required packages pre-installed using the `pcluster build-image` command. For more information, see [AWS ParallelCluster AMI customization](custom-ami-v3.md "custom-ami-v3.md").

### System configuration file modifications

Modifying critical system configuration files can cause cluster failures, especially if these files are managed by AWS ParallelCluster.

#### How to diagnose

1. Check for errors in the chef-client log that mention specific configuration files:

```
`$` `grep -i "config" /var/log/chef-client.log`
```

2. Look for permission or syntax errors in configuration files:

```
`$` `less /var/log/cfn-init.log`
```

#### How to resolve

1. Restore modified configuration files to their original state:

```
`$` `sudo cp /etc/file.conf.bak /etc/file.conf`
```

2. If you need to make persistent changes to system configuration files, use custom bootstrap actions instead of directly modifying files:

```
HeadNode:
  CustomActions:
    OnNodeConfigured:
      Script: s3://bucket-name/config-script.sh
```

For more information, see [Custom bootstrap actions](custom-bootstrap-actions-v3.md "custom-bootstrap-actions-v3.md"). 3. For configuration changes that must be made directly to system files, consider creating a custom AMI. For more information, see [AWS ParallelCluster AMI customization](custom-ami-v3.md "custom-ami-v3.md").

### Kernel updates and compatibility issues

Kernel updates can cause compatibility issues with certain AWS services, particularly with Amazon FSx for Lustre.

#### How to diagnose

1. Check if kernel updates have been applied:

```
`$` `uname -r`
```

2. Look for Amazon FSx mount failures in the logs:

```
`$` `grep -i "fsx" /var/log/chef-client.log`
```

#### How to resolve

1. For Ubuntu 22.04, avoid updating to the latest kernel as there is no Amazon FSx client for that kernel. For more information, see [Operating system considerations](operating-systems-v3.md#OS-Consideration-v3 "operating-systems-v3.md#OS-Consideration-v3").
2. If you've already updated the kernel and are experiencing issues, consider downgrading to a compatible kernel version:

```
`$` `sudo apt install linux-image-previous-version`
```

3. For persistent kernel customizations, create a custom AMI with the specific kernel version you need. For more information, see [AWS ParallelCluster AMI customization](custom-ami-v3.md "custom-ami-v3.md").

## Best practices for OS configuration changes

To minimize issues when making OS configuration changes:

1. **Use Custom Bootstrap Actions**: Instead of directly modifying system files, use `OnNodeStart` or `OnNodeConfigured` scripts to make changes in a controlled manner. For more information, see [Custom bootstrap actions](custom-bootstrap-actions-v3.md "custom-bootstrap-actions-v3.md").
2. **Create Custom AMIs**: For significant OS modifications, create a custom AMI using `pcluster build-image` rather than making changes to running instances. For more information, see [AWS ParallelCluster AMI customization](custom-ami-v3.md "custom-ami-v3.md").
3. **Test Changes First**: Before applying changes to a production cluster, test them on a small test cluster to ensure compatibility.
4. **Document Changes**: Keep track of all OS configuration changes made to facilitate troubleshooting.
5. **Backup Configuration Files**: Before modifying any system configuration file, create a backup:

```
`$` `sudo cp /etc/file.conf /etc/file.conf.bak`
```

6. **Check Logs After Changes**: After making OS configuration changes, check the logs for any errors:

```
`$` `less /var/log/cfn-init.log`
`$` `less /var/log/chef-client.log`
```

By following these guidelines, you can minimize the risk of OS configuration changes causing cluster failures and more effectively troubleshoot any issues that do arise.
