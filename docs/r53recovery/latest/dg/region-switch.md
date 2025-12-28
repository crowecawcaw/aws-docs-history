# Region switch in ARC

You can use Region switch in ARC to orchestrate large-scale, complex recovery tasks for your
application resources across AWS accounts, to help ensure business continuity and reduce operational
overhead. Region switch provides a centralized and observable solution that you can perform
manually, or automate by using Amazon CloudWatch alarm triggers. If an AWS Region becomes impaired,
you can execute the plans that you create by using Region switch to fail over or switch your resources to
another Region. This ensures that your application can continue to operate, running in a healthy
AWS Region.

Region switch is built around the concept of a _plan_, which you design and configure for your
specific recovery needs. Each plan includes _workflows_ that are made up of steps. A step runs
one or more _execution blocks_, which Region switch runs in parallel or in sequence,
to complete an application recovery. Each execution block handles a different task, such as switching
over resources or managing traffic redirection for your application. For even more flexibility, you can
create nested plans, by adding child plans to an overall parent plan.

Region switch includes the following:

- Support for active/passive and active/active configurations. You can failover and
  failback if you have an active/passive multi-Region configurations, or shift-away and return if
  your application is set up as active/active in multiple Regions.
- Cross-account support for application resources that you include in your
  application recovery. You can also share Region switch plans across accounts.
- Automatic failover or switchover, by triggering plan execution based on Amazon CloudWatch alarms.
  Or, you can choose to execute a Region switch plan manually.
- Full-featured dashboards that give you real-time visibility into the recovery process.
- A data plane in each AWS Region, so that you can execute your Region switch plan without
  taking a dependency on the Region that you’re deactivating.
  Region switch is fully managed by AWS. Using Region switch enables you to benefit from the resilience of a recovery platform
  that focuses on your application's specific requirements, instead of building and maintaining scripts, and manually gathering data
  about recoveries.
