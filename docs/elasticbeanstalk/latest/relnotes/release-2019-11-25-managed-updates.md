# Release: Elastic Beanstalk console enables managed updates by default on November 25, 2019

Managed platform updates are now enabled by default for new environments created in the Elastic Beanstalk console.

**Release date:** November 25, 2019

## Changes

Starting today, when you create an AWS Elastic Beanstalk environment using the Elastic Beanstalk console, managed platform updates are enabled by default whenever possible (on
supported platform versions, and with [enhanced health](../dg/health-enhanced.md "../dg/health-enhanced.md") enabled), with a weekly update time window
that Elastic Beanstalk sets at random. This ensures that your application always runs on a platform with the latest security updates, bug fixes, and minor software
stack releases.

### About managed updates

With managed platform updates, you can configure your environment to automatically upgrade to the latest version of a platform during a scheduled
maintenance window. Your application remains in service during the update process with no reduction in capacity.

For more information about managed platform updates, see [Managed Platform
Updates](../dg/environment-platform-update-managed.md "../dg/environment-platform-update-managed.md") in the _AWS Elastic Beanstalk Developer Guide_.
