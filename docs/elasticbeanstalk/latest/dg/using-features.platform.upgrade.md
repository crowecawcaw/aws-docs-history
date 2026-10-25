

# Updating your Elastic Beanstalk environment's platform version
<a name="using-features.platform.upgrade"></a>

Elastic Beanstalk regularly releases new platform versions to update all Linux-based and Windows Server-based [platforms](concepts.platforms.md). New platform versions provide updates to existing software components and support for new features and configuration options. To learn about platforms and platform versions, see [Elastic Beanstalk platforms glossary](platforms-glossary.md).

How you update depends on where you're updating to:
+ **A newer version in your environment's current platform branch** (same runtime, web server, application server, and operating system). This is the most common and routine platform update. See [Update within your platform branch](#using-features.platform.upgrade.within-branch), or have Elastic Beanstalk apply these updates for you with [Managed platform updates](environment-platform-update-managed.md).
+ **A different platform branch** (different runtime, web server, application server, or operating system), for example to use a new runtime version or to move off of a deprecated or retired platform branch. See [Migrate to a different platform branch](#using-features.platform.upgrade.different-branch).

**Important**  
Every platform version update replaces your environment's instances, even within the same platform branch. To control how Elastic Beanstalk replaces instances, configure [rolling updates](using-features.rollingupdates.md) or [immutable updates](environmentmgmt-updates-immutable.md). Immutable updates launch new instances before removing the old ones.

## Update within your platform branch
<a name="using-features.platform.upgrade.within-branch"></a><a name="using-features.platform.upgrade.config"></a>

Use this procedure to update to the latest version of your environment's platform branch, or to an earlier version in the same branch that's still available to your account.

**To update your environment's platform version**

1. Open the [Elastic Beanstalk console](https://console.aws.amazon.com/elasticbeanstalk), and in the **Regions** list, select your AWS Region.

1. In the navigation pane, choose **Environments**, and then choose the name of your environment from the list.

1. On the environment overview page, under **Platform**, choose **Change version**.

1. In the **Update platform version** dialog, keep the current **Platform branch**, and select a **Platform version**. The recommended version is labeled **(Recommended)**.

1. Choose **Update**.

To update with the EB CLI, use [**eb upgrade**](eb3-upgrade.md). To update with the AWS CLI, use [update-environment](https://docs.aws.amazon.com/cli/latest/reference/elasticbeanstalk/update-environment.html) with the `--platform-arn` or `--solution-stack-name` option.

To further simplify platform updates, Elastic Beanstalk can manage them for you. You can configure your environment to apply minor and patch version updates automatically during a configurable weekly maintenance window. Elastic Beanstalk applies managed updates with no downtime or reduction in capacity, and cancels the update immediately if instances running your application on the new version fail health checks. For details, see [Managed platform updates](environment-platform-update-managed.md).

## Migrate to a different platform branch
<a name="using-features.platform.upgrade.different-branch"></a><a name="using-features.platform.upgrade.bluegreen"></a>

When you migrate to a different platform branch, there's a greater likelihood that your application, or some aspects of it, might not function as expected on the new platform version, and might require changes. For example, a new runtime or operating system version can break application dependencies, [configuration files](ebextensions.md), or [platform hooks](platforms-linux-extend.md).

Before performing the migration, update your local development machine to the newer runtime versions and other components of the platform you plan on migrating to. Verify that your application still works as expected, and make any necessary code fixes and changes. Then use the following best practice procedure, a blue/green deployment, to safely migrate your environment to the new platform branch.

**To migrate your environment to a different platform branch with a blue/green deployment**

1. [Create a new environment](using-features.environments.md), using the new target platform version, and deploy your application code to it. The new environment should be in the Elastic Beanstalk application that contains the environment you're migrating. Don't terminate the existing environment yet.

1. Use the new environment to migrate your application. In particular:
   + Find and fix any application compatibility issues that you couldn't discover during the development phase.
   + Ensure that any customizations that your application makes using [configuration files](ebextensions.md) work correctly in the new environment. These might include option settings, additional installed packages, custom security policies, and script or configuration files installed on environment instances.
   + If your application uses a custom Amazon Machine Image (AMI), create a new custom AMI based on the AMI of the new platform version. To learn more, see [Using a custom Amazon machine image (AMI) in your Elastic Beanstalk environment](using-features.customenv.md).

   Iterate on testing and deploying your fixes until you're satisfied with the application on the new environment.

1. Turn the new environment into your production environment by swapping its CNAME with the existing production environment's CNAME. For details, see [Blue/Green deployments with Elastic Beanstalk](using-features.CNAMESwap.md).

1. When you're satisfied with the state of your new environment in production, terminate the old environment. For details, see [Terminate an Elastic Beanstalk environment](using-features.terminating.md).

Alternatively, you can change an existing environment's platform branch in place. In the **Update platform version** dialog, select a different **Platform branch**, or use the AWS CLI. We recommend this only after you've verified that your application works on the new platform branch, for example in a separate test environment.