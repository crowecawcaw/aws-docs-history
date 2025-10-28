# How does 30-day free trial work in

Runtime Monitoring

The 30-day free trial period works differently for the new GuardDuty accounts and the existing
accounts that have already enabled EKS Runtime Monitoring prior to when Runtime Monitoring capability extended to
Amazon EC2 instances and AWS Fargate (Amazon ECS only).

## I am using GuardDuty trial

period or I have never enabled EKS Runtime Monitoring

The following list explains how the 30-day free trial period works if you're either using
the GuardDuty 30-day trial period or have never enabled EKS Runtime Monitoring:

- When you enable GuardDuty for the first time, Runtime Monitoring and EKS Runtime Monitoring will not be enabled by
  default.

When you enable Runtime Monitoring for your account or organization, make sure to also configure
the GuardDuty security agent for the resource that you want to monitor for threat detection. For
example, if you want to use Runtime Monitoring for your Amazon EC2 instances, then after you enable Runtime Monitoring,
you must also configure the security agent for Amazon EC2. You can choose to do this either
manually or automatically through GuardDuty.

- The Runtime Monitoring protection plan is enabled at the **account
  level**. The 30-day free trial period works at the **resource
  level**. After the GuardDuty security agent gets deployed to a specific resource type,
  the 30-day free trial starts when GuardDuty receives its **first runtime
  event** associated with this resource type. For example, you have deployed the GuardDuty
  agent at the resource level (for Amazon EC2 instance, Amazon ECS cluster, and Amazon EKS cluster). When GuardDuty
  receives the first runtime event for an Amazon EC2 instance, the 30-day free trial will start for
  Amazon EC2 only.
- When you want to enable only EKS Runtime Monitoring – When you enable GuardDuty for the first
  time, EKS Runtime Monitoring is not enabled by default (after the release of Runtime Monitoring). You will need to
  enable EKS Runtime Monitoring. To use it optimally, make sure that you either manage the GuardDuty security
  agent manually or enable automated agent configuration so that GuardDuty manages the agent on your
  behalf. Your 30-day free trial period for EKS Runtime Monitoring starts when GuardDuty receives its first
  runtime event for the Amazon EKS resource.
