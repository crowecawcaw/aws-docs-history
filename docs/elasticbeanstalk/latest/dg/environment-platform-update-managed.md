

# Managed platform updates
<a name="environment-platform-update-managed"></a>

AWS Elastic Beanstalk regularly releases [platform updates](using-features.platform.upgrade.md) to provide fixes, software updates, and new features. With managed platform updates, you can configure your environment to automatically upgrade to the latest version of a platform during a scheduled [maintenance window](#environment-platform-update-managed-window). Your application remains in service during the update process with no reduction in capacity. Managed updates are available on both single-instance and load-balanced environments. 

You can configure your environment to automatically apply [patch version updates](#environment-platform-update-managed-versioning), or both patch and minor version updates. Managed platform updates don't support updates across platform branches (updates to different major versions of platform components such as operating system, runtime, or Elastic Beanstalk components), because these can introduce changes that are backward incompatible. This is also true after your platform branch is retired. To move to a different platform branch, see [Migrate to a different platform branch](using-features.platform.upgrade.md#using-features.platform.upgrade.different-branch).

You can also configure Elastic Beanstalk to replace all instances in your environment during the maintenance window, even if a platform update isn't available. Replacing all instances in your environment is helpful if your application encounters bugs or memory issues when running for a long period.

When you create an environment using the Elastic Beanstalk console, managed updates are enabled by default. The console sets the **Weekly update window** to a random day of the week at a random time, sets **Update level** to **Minor and patch**, and leaves instance replacement disabled. Managed updates require [enhanced health](health-enhanced.md), which the console also enables by default. You can disable or reconfigure managed updates when you create the environment.

For an existing environment, use the Elastic Beanstalk console anytime to configure managed platform updates.

**Important**  
A *high number* of Beanstalk environments in one AWS account may present a risk of throttling issues during managed updates. *High number* is a relative amount that depends on how closely you schedule the managed updates for your environments. Over 200 environments in one account scheduled closely could cause throttling issues, although a lower number may also be problematic.  
To balance the resource load for managed updates, we advise that you spread out the scheduled maintenance windows for the environments in one account.   
Also, consider a multi‐account strategy. For more information, see [Organizing Your AWS Environment Using Multiple Accounts](https://docs.aws.amazon.com/whitepapers/latest/organizing-your-aws-environment/organizing-your-aws-environment.html) on the *AWS Whitepapers & Guides* website. 

**To configure managed platform updates**

1. Open the [Elastic Beanstalk console](https://console.aws.amazon.com/elasticbeanstalk), and in the **Regions** list, select your AWS Region.

1. In the navigation pane, choose **Environments**, and then choose the name of your environment from the list.

1. On the **Configuration** tab, in the **Monitoring and updates** section, choose **Edit**.

1. Under **Managed updates**, select or clear **Enable managed updates**.

1. If managed updates are enabled, select a **Weekly update window**, and then select an **Update level**.

1. (Optional) Select **Enable instance replacement** to replace all instances during each weekly maintenance window.

1. Choose **Save changes**, review your changes, and then choose **Apply changes**.

Managed platform updates depend on [enhanced health reporting](health-enhanced.md) to determine that your application is healthy enough to consider the platform update successful. You can't enable managed updates when enhanced health is disabled. See [Enabling Elastic Beanstalk enhanced health reporting](health-enhanced-enable.md) for instructions.

**Topics**
+ [Permissions required to perform managed platform updates](#environment-platform-update-managed-perms)
+ [Managed update maintenance window](#environment-platform-update-managed-window)
+ [Minor and patch version updates](#environment-platform-update-managed-versioning)
+ [Immutable environment updates](#environment-platform-update-managed-immutable)
+ [Managing managed updates](#environment-platform-update-managed-managing)
+ [Managed action option namespaces](#environment-platform-update-managed-namespace)

## Permissions required to perform managed platform updates
<a name="environment-platform-update-managed-perms"></a>

Elastic Beanstalk needs permission to initiate a platform update on your behalf. To gain these permissions, Elastic Beanstalk assumes the *managed-updates service role*. When you use the default [service role](iam-servicerole.md) for your environment, the Elastic Beanstalk console uses it as the managed-updates service role too. The console assigns the [`AWSElasticBeanstalkManagedUpdatesCustomerRolePolicy`](iam-servicerole.md#iam-servicerole-update) managed policy to your service role. This policy has all permissions that Elastic Beanstalk needs to perform managed platform updates.

For details about other ways to set the managed-updates service role, see [Managing Elastic Beanstalk service roles](iam-servicerole.md).

**Note**  
If you use [configuration files](ebextensions.md) to extend your environment to include additional resources, you might need to add permissions to your environment's managed-updates service role. Typically you need to add permissions when you reference these resources by name in other sections or files.

If an update fails, you can find the reason for the failure on the [Managed updates](#environment-platform-update-managed-managing) tab.

## Managed update maintenance window
<a name="environment-platform-update-managed-window"></a>

When AWS releases a new version of your environment's platform, Elastic Beanstalk schedules a managed platform update during the next weekly maintenance window. Maintenance windows are two hours long. Elastic Beanstalk starts a scheduled update during the maintenance window. The update might not complete until after the window ends. Elastic Beanstalk runs one managed update per maintenance window. If a platform update is available and instance replacement is enabled, Elastic Beanstalk applies the platform update, which also replaces all instances.

**Note**  
In most cases, Elastic Beanstalk schedules your managed update to occur during your coming weekly maintenance window. The system considers various aspects of update safety and service availability when scheduling managed updates. In rare cases, an update might not be scheduled for the first coming maintenance window. If this happens, the system tries again during the next maintenance window. To manually apply the managed update, choose **Apply now** as explained in [Managing managed updates](#environment-platform-update-managed-managing) on this page.

## Minor and patch version updates
<a name="environment-platform-update-managed-versioning"></a>

You can enable managed platform updates to apply patch version updates only, or for both minor and patch version updates. Patch version updates provide bug fixes and performance improvements, and can include minor configuration changes to the on-instance software, scripts, and configuration options. Minor version updates provide support for new Elastic Beanstalk features. You can't apply major version updates, which might make changes that are backward incompatible, with managed platform updates.

In a platform version number, the second number is the minor update version, and the third number is the patch version. For example, a version 2.0.7 platform version has a minor version of 0 and a patch version of 7.

## Immutable environment updates
<a name="environment-platform-update-managed-immutable"></a>

Managed platform updates perform [immutable environment updates](environmentmgmt-updates-immutable.md) to upgrade your environment to a new platform version. Immutable updates update your environment without taking any instances out of service or modifying your environment, before confirming that instances running the new version pass health checks. 

In an immutable update, Elastic Beanstalk deploys as many instances as are currently running with the new platform version. The new instances begin to take requests alongside those running the old version. If the new set of instances passes all health checks, Elastic Beanstalk terminates the old set of instances, leaving only instances with the new version.

Managed platform updates always perform immutable updates, even when you apply them outside of the maintenance window. If you [change the platform version](using-features.platform.upgrade.md) yourself, Elastic Beanstalk applies the update policy that you've chosen for configuration updates.

**Warning**  
Some policies replace all instances during the deployment or update. This causes all accumulated [Amazon EC2 burst balances](https://docs.aws.amazon.com/AWSEC2/latest/DeveloperGuide/burstable-performance-instances.html) to be lost. It happens in the following cases:  
Managed platform updates with instance replacement enabled
Immutable updates
Deployments with immutable updates or traffic splitting enabled

## Managing managed updates
<a name="environment-platform-update-managed-managing"></a>

The Elastic Beanstalk console shows detailed information about managed updates on the **Managed updates** tab of your environment's page.

**To view information about managed updates (console)**

1. Open the [Elastic Beanstalk console](https://console.aws.amazon.com/elasticbeanstalk), and in the **Regions** list, select your AWS Region.

1. In the navigation pane, choose **Environments**, and then choose the name of your environment from the list.

1. Choose **Managed updates**.

The top of the tab shows the status of the next managed update, if one is scheduled, pending, or running. The **Managed updates history** table lists successful updates and failed attempts, including the reason for each failure.

You can choose to apply a scheduled update immediately, instead of waiting until the maintenance window. 

**To apply a managed platform update immediately (console)**

1. Open the [Elastic Beanstalk console](https://console.aws.amazon.com/elasticbeanstalk), and in the **Regions** list, select your AWS Region.

1. In the navigation pane, choose **Environments**, and then choose the name of your environment from the list.

1. Choose **Managed updates**.

1. Choose **Apply now**.

1. Review the update details, and then choose **Apply**.

When you apply a managed platform update outside of the maintenance window, Elastic Beanstalk performs an immutable update. If you [update the environment's platform](using-features.platform.upgrade.md) yourself, in the console or by using a different client, Elastic Beanstalk uses the update type that you selected for [configuration changes](environments-updating.md).

If you don't have a managed update scheduled, your environment might already be running the latest version. Other reasons for not having an update scheduled include:
+ A [minor version](#environment-platform-update-managed-versioning) update is available, but your environment is configured to automatically apply only patch version updates.
+ Your environment hasn't been scanned since the update was released. Elastic Beanstalk typically checks for updates every hour.
+ An update is pending or already in progress.

A managed update has a status of `Scheduled` until your maintenance window starts or you choose **Apply now**. It's then `Pending` until it starts, and `Running` while it's in progress.

## Managed action option namespaces
<a name="environment-platform-update-managed-namespace"></a>

You can use [configuration options](command-options.md) in the `aws:elasticbeanstalk:managedactions` and `aws:elasticbeanstalk:managedactions:platformupdate` namespaces to enable and configure managed platform updates.

The `ManagedActionsEnabled` option turns on managed platform updates. Set this option to `true` to enable managed platform updates, and use the other options to configure update behavior.

Use `PreferredStartTime` to configure the beginning of the weekly maintenance window in {{day}}:{{hour}}:{{minute}} format.

Set `UpdateLevel` to `minor` or `patch` to apply both minor and patch version updates, or just patch version updates, respectively.

When managed platform updates are enabled, you can enable instance replacement by setting the `InstanceRefreshEnabled` option to `true`. When this setting is enabled, Elastic Beanstalk runs an immutable update on your environment every week, regardless of whether there is a new platform version available.

The following example [configuration file](ebextensions.md) enables managed platform updates for patch version updates with a maintenance window starting at 9:00 AM UTC each Tuesday.

**Example .ebextensions/managed-platform-update.config**  

```
option_settings:
  aws:elasticbeanstalk:managedactions:
    ManagedActionsEnabled: true
    PreferredStartTime: "Tue:09:00"
  aws:elasticbeanstalk:managedactions:platformupdate:
    UpdateLevel: patch
    InstanceRefreshEnabled: true
```