

# Platform retirement FAQ
<a name="using-features.migration-al.FAQ"></a>

The answers in this FAQ reference the following topics:
+ [Elastic Beanstalk platform support policy](platforms-support-policy.md)
+  [Retired platform branch history](platforms-schedule.md#platforms-support-policy.retired) 
+ [ Elastic Beanstalk supported platforms](https://docs.aws.amazon.com/elasticbeanstalk/latest/platforms/platforms-supported.html) in *AWS Elastic Beanstalk Platforms*
+ [Migrate to a different platform branch](using-features.platform.upgrade.md#using-features.platform.upgrade.different-branch)

## 1. What does retirement of a platform branch mean?
<a name="using-features.migration-al.FAQ.what-retire-means"></a>

Following the announced retirement date of a platform branch, you will no longer be able to create a new environment based on the retired platform branch, unless you already have an active environment based on that platform branch. For more information, see [FAQ \#11](#using-features.migration-al.FAQ.new-env-create). Elastic Beanstalk will stop providing new maintenance updates for these platform branches. A retired platform branch isn't recommended for use in production environments. For more information, see [FAQ \#5](#using-features.migration-al.FAQ.remove-components). 

## 2. Why does Elastic Beanstalk retire platform branches?
<a name="using-features.migration-al.FAQ.why"></a>

Elastic Beanstalk retires a platform branch when one of its components, such as the operating system, runtime language version, application server, or web server, reaches End of Life (EOL) from its supplier. For more information, see [Elastic Beanstalk platform support policy](platforms-support-policy.md).

## 3. Which platform branches are retired or scheduled for retirement?
<a name="using-features.migration-al.FAQ.which-pb-retire"></a>

 For a list of platform components and platform branches that have been retired, see [Retired platform branch history](platforms-schedule.md#platforms-support-policy.retired). For platform branches that are scheduled for retirement, see [Retiring platform branch schedule](platforms-schedule.md#platforms-support-policy.depracation).

## 4. Which platforms are currently supported?
<a name="using-features.migration-al.FAQ.which-pb-supported"></a>

See [ Elastic Beanstalk supported platforms](https://docs.aws.amazon.com/elasticbeanstalk/latest/platforms/platforms-supported.html) in *AWS Elastic Beanstalk Platforms*.

## 5. Will Elastic Beanstalk remove or terminate any components of my environment after retirement?
<a name="using-features.migration-al.FAQ.remove-components"></a>

Our policy for retired platform branches does not remove access to environments nor delete resources. However, an environment based on a retired platform branch can end up in an unpredictable situation, because Elastic Beanstalk isn't able to provide security updates, technical support, or hotfixes for retired platform branches due to the supplier marking their component as End of Life (EOL). For example, a detrimental and critical security vulnerability may surface in an environment running on a retired platform branch. Or an EB API action may stop working for the environment if it becomes incompatible with the Elastic Beanstalk service over time. The opportunity for these types of risks increases the longer an environment based on a retired platform branch remains active. 

If your application should encounter issues while running on a retired platform branch and you're not able to migrate it to a supported platform, you'll need to consider other alternatives. Workarounds include encapsulating the application into a Docker image to run it as a Docker container. This would allow a customer to use any of our Docker solutions, such as our Elastic Beanstalk AL2023/AL2 Docker platforms, or other Docker based services such as Amazon ECS or Amazon EKS. Non-Docker alternatives include our AWS CodeDeploy service, which allows complete customization of the runtimes you desire. 

## 6. Can I submit a request to extend the retirement date?
<a name="using-features.migration-al.FAQ.extend-request"></a>

No. After the retirement date existing environments will continue to function. However, Elastic Beanstalk will no longer provide platform maintenance and security updates. Therefore, it's critical to migrate your environments to a supported platform branch. For more information about risks and workarounds, see [FAQ \#5](#using-features.migration-al.FAQ.remove-components). 

## 7. What are the workarounds if I can't complete my migration in time?
<a name="using-features.migration-al.FAQ.workarounds"></a>

Customers may continue to run the environment, although we strongly encourage you to plan to migrate all of your Elastic Beanstalk environments to a supported platform version. Doing so will minimize risk and provide continued benefit from important security, performance, and functionality enhancements offered in more recent releases. For more information about risks and workarounds, see [FAQ \#5](#using-features.migration-al.FAQ.remove-components).

## 8. What is the recommended process to migrate to a supported platform branch?
<a name="using-features.migration-al.FAQ.migration-process"></a>

We recommend a blue/green deployment. See [Migrate to a different platform branch](using-features.platform.upgrade.md#using-features.platform.upgrade.different-branch). If you're migrating from Amazon Linux 2 to Amazon Linux 2023, also see [Migrating your Elastic Beanstalk Linux application to Amazon Linux 2023](using-features.migration-al.md).

## 9. If I have an environment running on a retired platform, what would be the impact?
<a name="using-features.migration-al.FAQ.ret-env-impact"></a>

An environment based on a retired platform branch can end up in an unpredictable situation, because Elastic Beanstalk isn't able to provide security updates, technical support, or hotfixes for retired platform branches due to the supplier marking their component as End of Life (EOL). For example, a detrimental and critical security vulnerability may surface in an environment running on a retired platform branch. Or an EB API action may stop working for the environment if it becomes incompatible with the Elastic Beanstalk service over time. The opportunity for these types of risks increases the longer an environment on a retired platform branch remains active. For more information, see [FAQ \#5](#using-features.migration-al.FAQ.remove-components).

## 10. What happens 90 days after the retirement date?
<a name="using-features.migration-al.FAQ.after-grace"></a>

Our policy for retired platform branches does not remove access to environments nor delete resources. However, be aware that an environment based on a retired platform branch can end up in an unpredictable situation, because Elastic Beanstalk isn't able to provide security updates, technical support, or hotfixes for retired platform branches due to the supplier marking their component as End of Life (EOL). For example, a detrimental and critical security vulnerability may surface in an environment running on a retired platform branch. Or an EB API action may stop working for the environment if it becomes incompatible with the Elastic Beanstalk service over time. The opportunity for these types of risks increases the longer an environment on a retired platform branch remains active. For more information see [FAQ \#5](#using-features.migration-al.FAQ.remove-components).

## 11. Can I create a new environment based on a retired platform?
<a name="using-features.migration-al.FAQ.new-env-create"></a>

You can create a new environment based on a retired platform branch, if you've already used that platform branch to create an existing environment using the same account and in the same region. The retired platform branch will not be available in the Elastic Beanstalk console. However, for customers that have existing environments based on a retired platform branch, it will be available through the EB CLI, EB API, and AWS CLI. Also, existing customers can use the [Clone environment](using-features.managing.clone.md) and [Rebuild environment](environment-management-rebuild.md) consoles. However, be aware that an environment based on a retired platform branch can end up in an unpredictable situation. For more information, see [FAQ \#5](#using-features.migration-al.FAQ.remove-components).

## 12. If I have an existing environment running on a retired platform branch, until when can I create a new environment based on the retired platform branch? Can I do so using the console, CLI or API?
<a name="using-features.migration-al.FAQ.new-env-when"></a>

You can create the environment after the retirement date. However, keep in mind that a retired platform branch can end up in an unpredictable situation. The further out in time such an environment an environment is created or active, the higher the risk for the environment to encounter unexpected issues. For more information about creating a new environment, see [FAQ \#11](#using-features.migration-al.FAQ.new-env-create).

## 13. Can I clone or rebuild my environment which is based on retired platform?
<a name="using-features.migration-al.FAQ.clone"></a>

Yes. You can do so using the [Clone environment](using-features.managing.clone.md) and [Rebuild environment](environment-management-rebuild.md) consoles. You can also use the EB CLI, EB API, and AWS CLI. For more information about creating a new environment, see [FAQ \#11](#using-features.migration-al.FAQ.new-env-create).

However, we strongly encourage you to plan to migrate all your Elastic Beanstalk environments to a supported platform version. Doing so will minimize risk and provide continued benefit from important security, performance, and functionality enhancements offered in more recent releases. For more information about risks and workarounds, see [FAQ \#5](#using-features.migration-al.FAQ.remove-components). 

## 14. After the retirement date, what would happen to the AWS resources of my Elastic Beanstalk environment that is based on a retired platform branch? For example, if the running EC2 instance gets terminated, would Elastic Beanstalk be able to launch a new instance to maintain capacity?
<a name="using-features.migration-al.FAQ.auto-scale"></a>

The environment's resources remain active and continue to function. However, after a platform branch is retired, its base Elastic Beanstalk AMI might be made private. If that happens, the environment can't launch new instances, for example to scale out, to replace an unhealthy instance, or to apply a configuration change that replaces instances. To keep the ability to launch instances, see [Preserving access to an Amazon Machine Image (AMI) for a retired platform](using-features.customenv-env-copy.md). Elastic Beanstalk also stops providing platform maintenance updates to the environment. For more information, see [FAQ \#5](#using-features.migration-al.FAQ.remove-components).

## 15. Is a newer platform branch compatible with my application?
<a name="using-features.migration-al.FAQ.os-diff"></a>

Not necessarily. A newer platform branch can include a different operating system version, runtime version, build tools, and other dependencies, and isn't guaranteed to be backward compatible with your application. Even if your application deploys successfully, it might behave or perform differently. Test your application on the new platform branch before you migrate your production environment. For more information, see [Migrate to a different platform branch](using-features.platform.upgrade.md#using-features.platform.upgrade.different-branch).