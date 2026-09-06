

# Release: Elastic Beanstalk console enables managed updates by default on November 25, 2019
<a name="release-2019-11-25-managed-updates"></a>

Managed platform updates are now enabled by default for new environments created in the Elastic Beanstalk console.

**Release date:** November 25, 2019

## Changes
<a name="release-2019-11-25-managed-updates.changes"></a>

Starting today, when you create an AWS Elastic Beanstalk environment using the Elastic Beanstalk console, managed platform updates are enabled by default whenever possible (on supported platform versions, and with [enhanced health](https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/health-enhanced.html) enabled), with a weekly update time window that Elastic Beanstalk sets at random. This ensures that your application always runs on a platform with the latest security updates, bug fixes, and minor software stack releases.

### About managed updates
<a name="release-2019-11-25-managed-updates.changes.about"></a>

With managed platform updates, you can configure your environment to automatically upgrade to the latest version of a platform during a scheduled maintenance window. Your application remains in service during the update process with no reduction in capacity.

For more information about managed platform updates, see [Managed Platform Updates](https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/environment-platform-update-managed.html) in the *AWS Elastic Beanstalk Developer Guide*.