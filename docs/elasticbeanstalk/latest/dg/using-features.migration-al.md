# Platform retirement FAQ

###### Note

Elastic Beanstalk retired all platform branches based on Amazon Linux AMI (AL1) on
July 18, 2022
.

The answers in this FAQ reference the following topics:

- [Elastic Beanstalk platform support policy](platforms-support-policy.md "platforms-support-policy.md")
- [Retired platform branch history](platforms-schedule.md#platforms-support-policy.retired "platforms-schedule.md#platforms-support-policy.retired")
- [Elastic Beanstalk supported platforms](../platforms/platforms-supported.md "../platforms/platforms-supported.md") in
  _AWS Elastic Beanstalk Platforms_
- [Migrating your Elastic Beanstalk Linux application to Amazon Linux 2023 or Amazon Linux 2](using-features.md "using-features.md")
- [Amazon Linux 2 FAQs](https://aws.amazon.com//amazon-linux-2/faqs/ "https://aws.amazon.com//amazon-linux-2/faqs/").

## 1. What does retirement of a platform branch mean?

Following the announced retirement date of a platform branch, you will no longer be able to create a new environment based on the retired platform
branch, unless you already have an active environment based on that platform branch. For more information, see [FAQ #11](#using-features.migration-al.FAQ.new-env-create "#using-features.migration-al.FAQ.new-env-create"). Elastic Beanstalk will stop providing new maintenance updates for these platform branches.
A retired platform branch isn't recommended for use in production environments. For more information, see [FAQ #5](#using-features.migration-al.FAQ.remove-components "#using-features.migration-al.FAQ.remove-components").

## 2. Why has AWS retired the AL1-based platforms branches?

Elastic Beanstalk retires platform branches when platform components are deprecated or retired by their vendors. In this case, the Amazon Linux AMI (AL1) has ended
standard support as of [December 31, 2020](https://aws.amazon.com/blogs/aws/update-on-amazon-linux-ami-end-of-life/ "https://aws.amazon.com/blogs/aws/update-on-amazon-linux-ami-end-of-life/"). While Elastic Beanstalk
continued to offer AL1 based platforms through 2022, we have since released AL2 and AL2023 and based platforms that have the latest features. In order for customers
to continue to benefit from the latest security and features going forward, it's critical for customers to migrate to our AL2 or AL2023 based platforms.

## 3. Which platform branches are retired?

For a list of platform components and platform branches
that have been retired, see [Retired platform branch history](platforms-schedule.md#platforms-support-policy.retired "platforms-schedule.md#platforms-support-policy.retired").

## 4. Which platforms are currently supported?

See [Elastic Beanstalk supported platforms](../platforms/platforms-supported.md "../platforms/platforms-supported.md") in
_AWS Elastic Beanstalk Platforms_.

## 5. Will Elastic Beanstalk remove or terminate any components of my environment after

retirement?

Our policy for retired platform branches does not remove access to environments nor delete resources. However, an environment based on a retired
platform branch can end up in an unpredictable situation, because Elastic Beanstalk isn't able to provide security updates, technical support, or hotfixes for retired
platform branches due to the supplier marking their component as End of Life (EOL). For example, a detrimental and critical security vulnerability may
surface in an environment running on a retired platform branch. Or an EB API action may stop working for the environment if it becomes incompatible with
the Elastic Beanstalk service over time. The opportunity for these types of risks increases the longer an environment based on a retired platform branch remains
active.

If your application should encounter issues while running on a retired platform branch and you're not able to migrate it to a supported platform, you'll
need to consider other alternatives. Workarounds include encapsulating the application into a Docker image to run it as a Docker container. This would allow a
customer to use any of our Docker solutions, such as our Elastic Beanstalk AL2023/AL2 Docker platforms, or other Docker based services such as Amazon ECS or
Amazon EKS. Non-Docker alternatives include our AWS CodeDeploy service, which allows complete customization of the runtimes you desire.

## 6. Can I submit a request to extend the retirement date?

No. After the retirement date existing environments will continue to function. However, Elastic Beanstalk will no longer provide platform maintenance and security
updates. Therefore, it’s critical to migrate to AL2 or AL2023 if you are still running applications on an AL1-based platform. For more information
about risks and workarounds, see [FAQ #5](#using-features.migration-al.FAQ.remove-components "#using-features.migration-al.FAQ.remove-components").

## 7. What are the workarounds if I can't complete my AL2 or AL2023 migration in

time?

Customers may continue to run the environment, although we strongly encourage you to plan to migrate all of your Elastic Beanstalk environments to a
supported platform version. Doing so will minimize risk and provide continued benefit from important security, performance, and functionality enhancements
offered in more recent releases. For more information about risks and workarounds, see [FAQ #5](#using-features.migration-al.FAQ.remove-components "#using-features.migration-al.FAQ.remove-components").

## 8. What is the recommended process to migrate to AL2 or AL2023 platforms?

For comprehensive AL1 to AL2023/AL2 migration instructions, see [Migrating your Elastic Beanstalk Linux application to Amazon Linux 2023 or Amazon Linux 2](using-features.md "using-features.md").
This topic explains that Elastic Beanstalk requires a blue/green deployment to perform the upgrade.

## 9. If I have an environment running on a retired platform, what would be the

impact?

An environment based on a retired platform branch can end up in an unpredictable situation, because Elastic Beanstalk isn't able to provide security updates,
technical support, or hotfixes for retired platform branches due to the supplier marking their component as End of Life (EOL). For example, a detrimental
and critical security vulnerability may surface in an environment running on a retired platform branch. Or an EB API action may stop working for the
environment if it becomes incompatible with the Elastic Beanstalk service over time. The opportunity for these types of risks increases the longer an environment on a
retired platform branch remains active. For more information, see [FAQ #5](#using-features.migration-al.FAQ.remove-components "#using-features.migration-al.FAQ.remove-components").

## 10. What happens 90 days after the retirement date?

Our policy for retired platform branches does not remove access to environments nor delete resources. However, be aware that an environment based on
a retired platform branch can end up in an unpredictable situation, because Elastic Beanstalk isn't able to provide security updates, technical support, or hotfixes
for retired platform branches due to the supplier marking their component as End of Life (EOL). For example, a detrimental and critical security
vulnerability may surface in an environment running on a retired platform branch. Or an EB API action may stop working for the environment if it becomes
incompatible with the Elastic Beanstalk service over time. The opportunity for these types of risks increases the longer an environment on a retired platform branch
remains active. For more information see [FAQ #5](#using-features.migration-al.FAQ.remove-components "#using-features.migration-al.FAQ.remove-components").

## 11. Can I create a new environment based on a retired platform?

You can create a new environment based on a retired platform branch, if you've already used that platform branch to create an existing environment
using the same account and in the same region. The retired platform branch will not be available in the Elastic Beanstalk console.
However, for customers that have existing environments based on a retired platform branch, it will be available through the EB CLI, EB API, and AWS CLI.
Also, existing customers can use the [Clone environment](using-features.managing.md "using-features.managing.md") and [Rebuild environment](environment-management-rebuild.md "environment-management-rebuild.md") consoles. However, be aware that an environment based on a retired platform branch
can end up in an unpredictable situation. For more information, see [FAQ
#5](#using-features.migration-al.FAQ.remove-components "#using-features.migration-al.FAQ.remove-components").

## 12. If I have an existing environment running on a retired platform branch,

until when can I create a new environment based on the retired
platform branch? Can I do so using the console, CLI or API?

You can create the environment after the retirement date. However, keep in mind that a retired platform branch can end up in an unpredictable
situation. The further out in time such an environment an environment is created or active, the higher the risk for the environment to encounter
unexpected issues. For more information about creating a new environment, see [FAQ
#11](#using-features.migration-al.FAQ.new-env-create "#using-features.migration-al.FAQ.new-env-create").

## 13. Can I clone or rebuild my environment which is based on retired platform?

Yes. You can do so using the [Clone environment](using-features.managing.md "using-features.managing.md") and [Rebuild environment](environment-management-rebuild.md "environment-management-rebuild.md") consoles. You can also use the EB CLI, EB API, and AWS CLI. For more information about creating a new environment, see [FAQ #11](#using-features.migration-al.FAQ.new-env-create "#using-features.migration-al.FAQ.new-env-create").

However, we strongly encourage you to plan to migrate all your Elastic Beanstalk environments to a supported platform version. Doing so will minimize
risk and provide continued benefit from important security, performance, and functionality enhancements offered in more recent releases. For more
information about risks and workarounds, see [FAQ #5](#using-features.migration-al.FAQ.remove-components "#using-features.migration-al.FAQ.remove-components").

## 14. After the retirement date, what would happen to the AWS resources of my Elastic Beanstalk

environment that is based on a retired platform branch? For example, if the running EC2 instance gets terminated, would Elastic Beanstalk be able to launch a new
AL1 based EC2 instance to maintain capacity?

The environment’s resources would remain active and continue to function. And, yes, Elastic Beanstalk will auto scale for AL1 EC2 instances in the environment.
However, Elastic Beanstalk will stop providing new platform maintenance updates to the environment, which can lead to the environment ending up in an unpredictable
situation over time. For more information, see [FAQ #5](#using-features.migration-al.FAQ.remove-components "#using-features.migration-al.FAQ.remove-components").

## 15. What are key differences between the AL2023/AL2 and Amazon Linux AMI (AL1) operating systems? How are the Elastic Beanstalk

AL2023/AL2 platform branches affected?

Although Amazon Linux AMI and AL2023/AL2 share the same Linux kernel, they differ in their initialization system, `libc` versions, the compiler
tool chain, and various packages. For more information, see [Amazon Linux 2 FAQs](https://aws.amazon.com//amazon-linux-2/faqs/ "https://aws.amazon.com//amazon-linux-2/faqs/").

The Elastic Beanstalk service has also updated platform specific versions of runtime, build tools, and other dependencies. The AL2023/AL2 based platform branches aren't
guaranteed to be backward compatible with your existing application. Furthermore, even if your application code successfully deploys to the new platform
version, it might behave or perform differently due to operating system and run time differences. For a list and description of configurations and
customizations that you'll need to review and test, see [Migrating your Elastic Beanstalk Linux application to Amazon Linux 2023 or Amazon Linux 2](using-features.md "using-features.md").
