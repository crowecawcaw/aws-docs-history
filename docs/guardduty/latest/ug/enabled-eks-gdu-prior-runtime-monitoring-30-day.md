# I enabled EKS Runtime Monitoring prior to

the launch of Runtime Monitoring

Use this section only when EKS Runtime Monitoring was enabled for your AWS account, and now you want
to migrate to Runtime Monitoring.

The following list includes scenarios that might apply to your use case of enabling
Runtime Monitoring:

- For an existing GuardDuty account that has the EKS Runtime Monitoring protection plan enabled and uses
  the GuardDuty console experience to use this protection plan – With the announcement of
  Runtime Monitoring, the EKS Runtime Monitoring console experience has now been consolidated into Runtime Monitoring. Your
  existing configuration for EKS Runtime Monitoring remains the same. You can continue to use the API/CLI
  support to perform operations associated with EKS Runtime Monitoring.
- To use EKS Runtime Monitoring as a part of Runtime Monitoring, you will need to configure Runtime Monitoring for your
  account or organization. To keep the same configuration for Runtime Monitoring, see [Migrating from EKS Runtime Monitoring to
  Runtime Monitoring](migrating-from-eksrunmon-to-runtime-monitoring.md "migrating-from-eksrunmon-to-runtime-monitoring.md"). However, this will not
  impact your 30-day free trial for Amazon EKS resource.
- The Runtime Monitoring protection plan is enabled at the account level per Region. After the GuardDuty
  security agent gets deployed to one of the specified resource types (Amazon EC2 instance and Amazon ECS
  cluster), the 30-day free trial starts when GuardDuty receives the first runtime event associated
  with the resource. There is a 30-day free trial associated with each resource type.

For example, after enabling Runtime Monitoring, you choose to deploy the GuardDuty agent only on Amazon EC2
instance, the 30-day free trial for this resource will start only when GuardDuty receives its
first runtime event for an Amazon EC2 instance. Later, when you deploy the GuardDuty agent for
Fargate (Amazon ECS only), the 30-day free trial for this resource will start only when GuardDuty
receives its first runtime event for Amazon ECS cluster. Considering you already have EKS Runtime Monitoring
enabled for your account, GuardDuty doesn't reset the 30-day free trial for an Amazon EKS
resource.
