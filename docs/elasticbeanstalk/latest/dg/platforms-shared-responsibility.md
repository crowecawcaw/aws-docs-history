# Shared responsibility model for Elastic Beanstalk platform maintenance

AWS and our customers share responsibility for achieving a high level of software component security and compliance. This shared model reduces your
operational burden.

For details, see the AWS [Shared Responsibility Model](https://aws.amazon.com/compliance/shared-responsibility-model/ "https://aws.amazon.com/compliance/shared-responsibility-model/").

AWS Elastic Beanstalk helps you perform your side of the shared responsibility model by providing a _managed updates_ feature. This feature
automatically applies patch and minor updates for an Elastic Beanstalk supported platform version. If a managed update fails, Elastic Beanstalk notifies you of the failure to
ensure that you are aware of it and can take immediate action.

For more information, see [Managed platform updates](environment-platform-update-managed.md "environment-platform-update-managed.md").

In addition, Elastic Beanstalk does the following:

- Publishes its [platform support policy](platforms-support-policy.md "platforms-support-policy.md") and retirement schedule for the coming 12 months.
- Releases patch, minor, and major updates of operating system (OS), runtime, application server, and web server components typically within 30 days
  of their availability. Elastic Beanstalk is responsible for creating updates to Elastic Beanstalk components that are present on its supported platform versions. All other
  updates come directly from their suppliers (owners or community).
  We announce all updates to our supported platforms in our [release notes](../relnotes/relnotes.md "../relnotes/relnotes.md") in the
  _AWS Elastic Beanstalk Release Notes_ guide. We also provide a list of all supported platforms and their components, along with a platform history, in
  the _AWS Elastic Beanstalk Platforms_ guide. For more information see [Supported platforms and component history](concepts.md#concepts.platforms.list "concepts.md#concepts.platforms.list").

You are responsible to do the following:

- Update all the components that you control (identified as **Customer** in the AWS [Shared Responsibility Model](https://aws.amazon.com/compliance/shared-responsibility-model/ "https://aws.amazon.com/compliance/shared-responsibility-model/")). This includes ensuring the security of your
  application, your data, and any components that your application requires and that you downloaded.
- Ensure that your Elastic Beanstalk environments are running on a supported platform version, and migrate any environment running on a retired platform version
  to a supported version.
- If you’re using a custom Amazon machine image (AMI) for your Elastic Beanstalk environment, patch, maintain, and test your custom AMI so that it remains current and
  compatible with a supported Elastic Beanstalk platform version. For more information about managing environments with a custom AMI, see [Using a custom Amazon machine image (AMI) in your Elastic Beanstalk environment](using-features.md "using-features.md").
- Resolve all issues that come up in failed managed update attempts and retry the update.
- Patch the OS, runtime, application server, and web server yourself if you opted out of Elastic Beanstalk managed updates. You can do this by [applying platform updates manually](using-features.platform.md "using-features.platform.md") or directly patching the components on all relevant environment
  resources.
- Manage the security and compliance of any AWS services that you use outside of Elastic Beanstalk according to the AWS [Shared Responsibility Model](https://aws.amazon.com/compliance/shared-responsibility-model/ "https://aws.amazon.com/compliance/shared-responsibility-model/").
