# Creating environments in Elastic Beanstalk

This chapter describes how to create and manage your Elastic Beanstalk environments. This introductory page provides an overview of updates, maintenance, and
configurations that you'll apply over time as your application and environment evolve.

###### Environment functions

You can create and manage separate environments for development, testing, and production use, and you can [deploy any version](using-features.md "using-features.md") of your application to any environment. Environments can be long-running or
temporary. When you terminate an environment, you can save its configuration to recreate it later.

###### Application deployments

As you develop your application, you will deploy it often, possibly to several different environments for different purposes. Elastic Beanstalk lets you [configure how deployments are performed](using-features.md "using-features.md"). You can deploy to all of the instances in your
environment simultaneously, or split a deployment into batches with rolling deployments.

###### Configuration changes

[Configuration changes](environments-updating.md "environments-updating.md") are processed separately from deployments, and have their own scope. For example,
if you change the type of the EC2 instances running your application, all of the instances must be replaced. On the other hand, if you modify the
configuration of the environment's load balancer, that change can be made in-place without interrupting service or lowering capacity. You can also apply
configuration changes that modify the instances in your environment in batches with [rolling configuration
updates](using-features.md "using-features.md").

###### Note

Modify the resources in your environment only by using Elastic Beanstalk. If you modify resources using another service's console, CLI commands, or SDKs, Elastic Beanstalk
won't be able to accurately monitor the state of those resources, and you won't be able to save the configuration or reliably recreate the environment.
Out-of band-changes can also cause issues when updating or terminating an environment.

###### Platform updates

When you launch an environment, you choose a platform version. We update platforms periodically with new platform versions to provide performance
improvements and new features. You can [update your environment to the latest platform version](using-features.platform.md "using-features.platform.md") at
any time. See the _AWS Elastic Beanstalk Platforms_ guide for a list of [supported platforms](../platforms/platforms-supported.md "../platforms/platforms-supported.md") and a [platform version history](../platforms/platform-history.md "../platforms/platform-history.md") that includes the date ranges they were current.

###### Architecture options

As your application grows in complexity, you can split it into multiple components, each running in a separate environment. For long-running
workloads, you can launch [worker environments](using-features-managing-env-tiers.md "using-features-managing-env-tiers.md") that process jobs from an Amazon Simple Queue Service (Amazon SQS)
queue.

###### Topics

- [Using the Elastic Beanstalk environment management console](environments-console.md "environments-console.md")
- [Creating an Elastic Beanstalk environment](using-features.md "using-features.md")
- [Managing multiple Elastic Beanstalk environments as a group with the EB
  CLI](ebcli-compose.md "ebcli-compose.md")
- [Deploying applications to Elastic Beanstalk environments](using-features.md "using-features.md")
- [Configuration changes](environments-updating.md "environments-updating.md")
- [Updating your Elastic Beanstalk environment's platform version](using-features.platform.md "using-features.platform.md")
- [Canceling environment configuration updates
  and application deployments](using-features.rollingupdates.md "using-features.rollingupdates.md")
- [Rebuilding Elastic Beanstalk environments](environment-management-rebuild.md "environment-management-rebuild.md")
- [Environment types](using-features-managing-env-types.md "using-features-managing-env-types.md")
- [Elastic Beanstalk worker environments](using-features-managing-env-tiers.md "using-features-managing-env-tiers.md")
- [Creating links between Elastic Beanstalk environments](environment-cfg-links.md "environment-cfg-links.md")
- [Recovering your Elastic Beanstalk environment from an invalid state](environment-management-invalid-stack.md "environment-management-invalid-stack.md")
