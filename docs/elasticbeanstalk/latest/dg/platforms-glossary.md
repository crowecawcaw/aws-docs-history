# Elastic Beanstalk platforms glossary

Following are key terms related to AWS Elastic Beanstalk platforms and their lifecycle.

**Runtime**

The programming language-specific runtime software (framework, libraries, interpreter, vm, etc.) required to run your application code.

**Elastic Beanstalk Components**

Software components that Elastic Beanstalk adds to a platform to enable Elastic Beanstalk functionality. For example, the enhanced health agent is necessary for gathering
and reporting health information.

**Platform**

A combination of an operating system (OS), runtime, web server, application server, and Elastic Beanstalk components. Platforms provide components that are
available to run your application.

**Platform Version**

A combination of specific versions of an operating system (OS), runtime, web server, application server, and Elastic Beanstalk components. You create an Elastic Beanstalk
environment based on a platform version and deploy your application to it.

A platform version has a semantic version number of the form _X.Y.Z_, where _X_ is the major version,
_Y_ is the minor version, and _Z_ is the patch version.

A platform version can be in one of the following states:

- _Recommended_ – The latest platform version in a supported platform branch. This version contains the most up-to-date
  components and is recommended for use in production environments. When Elastic Beanstalk releases a new platform version, the new version supersedes the previous
  version and becomes the recommended platform version for the corresponding platform branch.
- _Not Recommended_ – Any platform version that is not the latest version in its platform branch. While these versions
  may remain functional, we strongly recommend updating to the latest platform version. You can use
  [managed platform updates](environment-platform-update-managed.md "environment-platform-update-managed.md") to help stay up-to-date automatically.

You can verify if a platform version is recommended using the AWS CLI command
**[describe-platform-version](../../../cli/latest/reference/elasticbeanstalk/describe-platform-version.md "../../../cli/latest/reference/elasticbeanstalk/describe-platform-version.md")**
and checking the `PlatformLifecycleState` field.

**Platform Branch**

A line of platform versions sharing specific (typically major) versions of some of their components, such as the operating system (OS), runtime,
or Elastic Beanstalk components. For example: _Python 3.13 running on 64bit Amazon Linux 2023_; _IIS 10.0 running on 64bit Windows Server
2025_. Platform branches receive updates in the form of new platform versions. Each successive platform version in a branch is an update
to the previous one.

The recommended version in each supported platform branch is available to you unconditionally for environment creation.
Previous platform versions remain accessible to accounts with active or terminated environments using them at the time they were superseded by a new version.
Previous platform versions lack the most up-to-date components and aren't recommended for use.

###### Note

If you need access to previous platform versions beyond the standard availability described above,
you can reach out to the [AWS Support Center](https://console.aws.amazon.com/support/home#/ "https://console.aws.amazon.com/support/home#/") for assistance.

A platform branch can be in one of the following states:

- _Supported_ – A current platform branch. It consists entirely of _supported components_.
  Supported components have not reached End of Life (EOL), as designated by their suppliers. It receives ongoing platform updates,
  and is recommended for use in production environments. For a list of supported platform branches, see [Elastic Beanstalk supported platforms](../platforms/platforms-supported.md "../platforms/platforms-supported.md") in the
  _AWS Elastic Beanstalk Platforms_ guide.
- _Beta_ – A preview, pre-release platform branch. It's experimental in nature. It may receive ongoing platform updates
  for a while, but has no long-term support. A beta platform branch isn't recommended for use in production environments. Use it only for evaluation.
  For a list of beta platform branches, see [Elastic Beanstalk Platform Versions in
  Public Beta](../platforms/platforms-beta.md "../platforms/platforms-beta.md") in the _AWS Elastic Beanstalk Platforms_ guide.
- _Deprecated_ – A platform branch where one or more components (such as the runtime or operating system) are approaching
  End of Life (EOL) or have reached EOL, as designated by their suppliers. While a deprecated platform branch continues to receive new platform versions
  until its retirement date, components that have reached EOL don't receive updates. For example, if a runtime version reaches EOL, the platform branch
  will be marked as deprecated but will continue to receive operating system updates until the platform branch retirement date. The platform branch
  will not continue to receive updates to the EOL runtime version. A deprecated platform branch isn't recommended for use.
- _Retired_ – A platform branch that no longer receives any updates. Retired platform branches aren't available to create new
  Elastic Beanstalk environments using the Elastic Beanstalk console. If your environment uses a retired platform branch, you must update to a supported platform branch to
  continue receiving updates. A retired platform branch isn't recommended for use. For more details about retired platform branches, see
  [Elastic Beanstalk platform support policy](platforms-support-policy.md "platforms-support-policy.md"). For a list of platform branches scheduled for retirement, see [Retiring platform branch schedule](platforms-schedule.md#platforms-support-policy.depracation "platforms-schedule.md#platforms-support-policy.depracation").
  To see past retired platform branches, see [Retired platform branch history](platforms-schedule.md#platforms-support-policy.retired "platforms-schedule.md#platforms-support-policy.retired").

If your environment uses a deprecated or retired platform branch, we recommend that you update it to a platform version in a supported platform
branch. For details, see [Updating your Elastic Beanstalk environment's platform version](using-features.platform.md "using-features.platform.md").

You can verify the state of a platform branch using the AWS CLI command
**[describe-platform-version](../../../cli/latest/reference/elasticbeanstalk/describe-platform-version.md "../../../cli/latest/reference/elasticbeanstalk/describe-platform-version.md")**
and checking the `PlatformBranchLifecycleState` field.

**Platform Update**

A release of a new platform version that contains updates to some components of the platform—OS, runtime, web server, application server,
and Elastic Beanstalk components. When Elastic Beanstalk releases a new platform version, the new version supersedes the previous version
and becomes the recommended platform version for the corresponding platform branch.
Platform updates follow semantic version taxonomy, and can have three levels:

- _Major update_ – An update that has changes that are incompatible with existing platform versions. You may need to
  modify your application to run correctly on a new major version. A major update has a new major platform version number.
- _Minor update_ – An update that has changes that are backward compatible with existing platform versions
  in most cases. Depending on your application, you may need to modify your application to run correctly on a new minor version. A minor update
  has a new minor platform version number.
- _Patch update_ – An update that consists of maintenance releases (bug fixes, security updates, and performance
  improvements) that are backward compatible with an existing platform version. A patch update has a new patch platform version number.

**Managed Updates**

An Elastic Beanstalk feature that automatically applies patch and minor updates to the operating system (OS), runtime, web server, application server, and
Elastic Beanstalk components for an Elastic Beanstalk supported platform version.
A managed update applies a newer platform version in the same platform branch to your environment.
You can configure managed updates to apply only patch updates, or minor and patch updates.
You can also disable managed updates completely.

For more information, see [Managed platform updates](environment-platform-update-managed.md "environment-platform-update-managed.md").
