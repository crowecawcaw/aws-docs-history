# Release: AWS Elastic Beanstalk support for enhanced health rule customization on July 25, 2018

Elastic Beanstalk added the ability to ignore application HTTP 4xx errors when determining your environment's health.

**Release date:** July 25, 2018

## Changes

Elastic Beanstalk enhanced health reporting relies on a set of rules to determine the health of your environment. Some of these rules might not be appropriate for
your particular application. A common case is when frequent HTTP client (4xx) errors are expected, for example, as a result of using client-side test
tools. By default, Elastic Beanstalk concludes that something is wrong, and unnecessarily degrades your environment's health status.

Today's release adds the ability to configure enhanced health monitoring to ignore application HTTP 4xx errors when determining the environment's
health. For details, see [Configuring Enhanced Health Rules](../dg/health-enhanced-rules.md "../dg/health-enhanced-rules.md") in the _AWS Elastic Beanstalk
Developer Guide_.
