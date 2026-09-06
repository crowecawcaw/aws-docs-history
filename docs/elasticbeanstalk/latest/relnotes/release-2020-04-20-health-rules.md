

# Release: Elastic Beanstalk support for load balancer enhanced health rule customization on April 20, 2020
<a name="release-2020-04-20-health-rules"></a>

AWS Elastic Beanstalk added the ability to ignore HTTP 4xx errors returned by the load balancer when determining your environment's health.

**Release date:** April 20, 2020

## Changes
<a name="release-2020-04-20-health-rules.changes"></a>

Elastic Beanstalk enhanced health reporting relies on a set of rules to determine the health of your environment. Some of these rules might not be appropriate for your particular application. A common case is when frequent HTTP client (4xx) errors are expected, for example, as a result of using client-side test tools. By default, Elastic Beanstalk concludes that something is wrong, and unnecessarily degrades your environment's health status.

Elastic Beanstalk already provides the ability to configure enhanced health monitoring to ignore HTTP 4xx errors returned from your application when determining the environment's health. However, until now, you could only ignore application errors—there was no way to ignore errors returned from the environment's load balancer. Today's release adds this ability. You can now configure enhanced health monitoring to ignore HTTP 4xx errors returned from the load balancer. For details, see [Configuring enhanced health rules for an environment](https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/health-enhanced-rules.html) in the *AWS Elastic Beanstalk Developer Guide*.