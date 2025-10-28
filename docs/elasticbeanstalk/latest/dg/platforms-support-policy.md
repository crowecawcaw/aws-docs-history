# Elastic Beanstalk platform support policy

Elastic Beanstalk supports platform branches that still receive ongoing minor and patch
updates from their suppliers (owners or community). For a complete definition of related terms, see [Elastic Beanstalk platforms glossary](platforms-glossary.md "platforms-glossary.md").

## Retired platform branches

When a component of a supported platform branch is marked End of Life (EOL) by its supplier, Elastic Beanstalk marks the platform branch as retired. Components of
a platform branch include the following: operating system (OS), runtime language version, application server, or web server.

Once a platform branch is marked as retired the following policies apply:

- Elastic Beanstalk stops providing maintenance updates, including security updates.
- Elastic Beanstalk no longer provides technical support for retired platform branches.
- Elastic Beanstalk no longer makes the platform branch available to new Elastic Beanstalk customers for deployments to new environments. There is a
  90 day grace period from the published retirement date for existing customers with active environments that are running
  on retired platform branches.

###### Note

A retired platform branch will not be available in the Elastic Beanstalk console. However, it will be available through the AWS CLI, EB CLI and EB API for customers
that have existing environments based on the retired platform branch. Existing customers can also use the [Clone
environment](using-features.managing.md "using-features.managing.md") and [Rebuild environment](environment-management-rebuild.md "environment-management-rebuild.md") consoles.

For a list of platform branches that are scheduled for retirement see the
[Retiring platform branch schedule](platforms-schedule.md#platforms-support-policy.depracation "platforms-schedule.md#platforms-support-policy.depracation")
in the _Elastic Beanstalk platform
schedule_ topic that follows.

For more information about what to expect when your environment’s platform branch retires, see [Platform retirement FAQ](using-features.migration-al.md "using-features.migration-al.md").

## Beyond the 90 day grace period

Our policy for retired platform branches does not remove access to environments nor delete resources. However, existing customers running an Elastic
Beanstalk environment on a retired platform branch should be aware of the risks of doing so. Such environments can end up in an unpredictable situation,
because Elastic Beanstalk isn't able to provide security updates, technical support, or hotfixes for retired platform branches due to the supplier marking their
component EOL.

For example, a detrimental and critical security vulnerability may surface in an environment running on a retired platform branch. Or an EB API action
may stop working for the environment if it becomes incompatible with the Elastic Beanstalk service over time. The opportunity for these types of risks increases the
longer an environment on a retired platform branch remains active. To continue to benefit from important security, performance, and functionality
enhancements offered by component suppliers in more recent releases, we strongly encourage you to update all your Elastic Beanstalk environments to a supported
platform version.

If your application should encounter issues while running on a retired platform branch and you're not able to migrate it to a supported platform, you'll
need to consider other alternatives. Workarounds include encapsulating the application into a Docker image to run it as a Docker container. This would allow a
customer to use any of our Docker solutions, such as our Elastic Beanstalk AL2023/AL2 Docker platforms, or other Docker based services such as Amazon ECS or
Amazon EKS. Non-Docker alternatives include our AWS CodeDeploy service, which allows complete customization of the runtimes you desire.
