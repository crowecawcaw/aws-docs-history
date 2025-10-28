# Release: Elastic Beanstalk introduces authorization for enhanced health information on September 10, 2020

AWS Elastic Beanstalk added an option to require authorization of enhanced health information traffic from environment instances to the
Elastic Beanstalk service.

**Release date:** September 10, 2020

## Changes

Elastic Beanstalk environment instances use an API to communicate enhanced health information traffic from environment instances to the Elastic Beanstalk service. Today we
added an option that requires authorization of this API. When you enable this option, the instance profile that you associate with your environment
instances must include a permission to use the respective action with your application and environment resources.

We recommend that you take advantage of this security option. It prevents bad actors from spoofing health data on your behalf. To make it easy to use,
we also added the required permission to the managed policies that Elastic Beanstalk provides for use in instance profiles. If you use our managed policies, enabling
the new option by setting it to `true` is all you have to do to activate enhanced health authorization. If you use a custom instance profile,
you'll need to add a new action permission to the profile.

If you don't want to use enhanced health authorization at this time, you don't need to change anything in your environment's configuration.

For details, see [Enhanced health authorization](../dg/health-enhanced.md#health-enhanced-authz "../dg/health-enhanced.md#health-enhanced-authz") in the
_AWS Elastic Beanstalk Developer Guide_.
