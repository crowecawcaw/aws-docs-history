# Release: Elastic Beanstalk support for traffic-splitting deployments on May 18, 2020

AWS Elastic Beanstalk added the ability to perform canary testing during application deployments by shifting some of the incoming traffic to
the new application version and evaluating its health.

**Release date:** May 18, 2020

## Changes

Elastic Beanstalk provides several application deployment policies, such as _All at once_, _Rolling_, and
_Immutable_. The various policies behave differently in multiple ways: deployment time, application downtime, how rollback works, and
what the impact of a failed deployment is. They provide different tradeoffs that you can choose from to suit your needs.

Today's release adds a new policy—_Traffic splitting_. Traffic-splitting deployments let you perform canary testing as part
of your application deployment. In a traffic-splitting deployment, Elastic Beanstalk launches a full set of new instances just like during an immutable deployment. It
then forwards a specified percentage of incoming client traffic to the new application version for a specified evaluation period. If the new instances
stay healthy, Elastic Beanstalk forwards all traffic to them and terminates the old ones. If the new instances don't pass health checks, or if you choose to abort the
deployment, Elastic Beanstalk moves traffic back to the old instances and terminates the new ones. There's never any service interruption.

For details, see [Deployment policies and settings](../dg/using-features.md "../dg/using-features.md") in the
_AWS Elastic Beanstalk Developer Guide_.
