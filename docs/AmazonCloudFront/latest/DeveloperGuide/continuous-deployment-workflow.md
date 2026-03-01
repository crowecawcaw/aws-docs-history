# CloudFront continuous deployment workflow

The following high-level workflow explains how to safely test and deploy configuration
changes with CloudFront continuous deployment.

1. Choose the distribution that you want to use as the _primary distribution_. The primary distribution is one that currently
   serves production traffic.
2. From the primary distribution, create a _staging
   distribution_. A staging distribution starts as a copy of the primary
   distribution.
3. Create a _traffic configuration_ inside a
   _continuous deployment policy_, and attach it
   to the primary distribution. This determines how CloudFront routes traffic to the
   staging distribution. For more information about routing requests to a staging
   distribution, see [Route requests to the staging distribution](understanding-continuous-deployment.md#understanding-continuous-deployment-routing "understanding-continuous-deployment.md#understanding-continuous-deployment-routing").
4. Update the configuration of the staging distribution. For more information
   about the settings that you can update, see [Update primary and staging distributions](understanding-continuous-deployment.md#updating-staging-and-primary-distributions "understanding-continuous-deployment.md#updating-staging-and-primary-distributions").
5. Monitor the staging distribution to determine whether the configuration
   changes perform as expected. For more information about monitoring a staging
   distribution, see [Monitor a staging distribution](monitoring-staging-distribution.md "monitoring-staging-distribution.md").

As you monitor the staging distribution, you can:

    * Update the configuration of the staging distribution again, to
     continue testing configuration changes.
    * Update the continuous deployment policy (traffic configuration) to
     send more or less traffic to the staging distribution.

6. When you're satisfied with the performance of the staging distribution,
   _promote_ the staging distribution's
   configuration to the primary distribution, which copies the staging
   distribution's configuration to the primary distribution. This also disables the
   continuous deployment policy which means that CloudFront routes all traffic to the
   primary distribution.
   You can build automation that monitors the performance of the staging distribution
   (step 5) and promotes the configuration automatically (step 6) when certain criteria are
   met.

After you promote a configuration, you can reuse the same staging distribution the
next time you want to test a configuration change.

For more information about working with staging distributions and continuous deployment
policies in the CloudFront console, the AWS CLI, or the CloudFront API, see the following
section.
