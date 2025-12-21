# Notifications and

troubleshooting

###### Try Amazon Q Developer CLI for AI-assisted troubleshooting

Amazon Q Developer CLI can help you troubleshoot environment issues quickly. The Q CLI provides
solutions by checking environment status, reviewing events, analyzing logs, and asking clarifying questions. For
more information and detailed walkthroughs, see [Troubleshooting Elastic Beanstalk Environments with Amazon Q Developer CLI](https://aws.amazon.com/blogs/devops/troubleshooting-elastic-beanstalk-environments-with-amazon-q-developer-cli/ "https://aws.amazon.com/blogs/devops/troubleshooting-elastic-beanstalk-environments-with-amazon-q-developer-cli/") in the AWS blogs.

This page lists messages for common issues and links to more information.
Messages appear in the [Environment overview pane](environments-dashboard-envoverview.md "environments-dashboard-envoverview.md")
of the Elastic Beanstalk console and are recorded in [events](using-features.md "using-features.md") when
health issues persist across several checks.

## Deployments

Elastic Beanstalk monitors your environment for consistency following deployments. If a rolling
deployment fails, the version of your application running on the instances in your environment
may vary. This can occur if a deployment succeeds on one or more batches but fails prior to
all batches completing.

_Incorrect application version found on 2 out of 5 instances. Expected version
"v1" (deployment 1)._

_Incorrect application version on environment instances. Expected version "v1"
(deployment 1)._

The expected application version is not running on some or all instances in an environment.

_Incorrect application version "v2" (deployment 2). Expected version "v1"
(deployment 1)._

The application deployed to an instance differs from the
expected version. If a deployment fails, the expected version is reset to the version from the
most recent successful deployment. In the above example, the first deployment (version "v1")
succeeded, but the second deployment (version "v2") failed. Any instances running "v2" are
considered unhealthy.

To solve this issue, start another deployment. You can [redeploy a previous version](using-features.md "using-features.md") that you
know works, or configure your environment to [ignore health checks](using-features.md#environments-cfg-rollingdeployments-console "using-features.md#environments-cfg-rollingdeployments-console") during
deployment and redeploy the new version to force the deployment to complete.

You can also identify and terminate the instances that are running the wrong application
version. Elastic Beanstalk will launch instances with the correct version to replace any instances that
you terminate. Use the [EB CLI health command](health-enhanced-ebcli.md "health-enhanced-ebcli.md") to
identify instances that are running the wrong application version.

## Application server

_15% of requests are erroring with HTTP 4xx_

_20% of the requests to the ELB are erroring with HTTP 4xx._

A high percentage of HTTP requests to an instance or
environment are failing with 4xx errors.

A 400 series status code indicates that the user made a bad request, such as requesting a
page that doesn't exist (404 File Not Found) or that the user doesn't have access to (403
Forbidden). A low number of 404s is not unusual but a large number could mean that there are
internal or external links to unavailable pages. These issues can be resolved by fixing bad
internal links and adding redirects for bad external links.

_5% of the requests are failing with HTTP 5xx_

_3% of the requests to the ELB are failing with HTTP 5xx._

A high percentage of HTTP requests to an instance or
environment are failing with 500 series status
codes.

A 500 series status code indicates that the application server encountered an internal
error. These issues indicate that there is an error in your application code and should be
identified and fixed quickly.

_95% of CPU is in use_

On an instance, the health agent is reporting an
extremely high percentage of CPU usage and sets the instance health to **Warning** or **Degraded**.

Scale your environment to take load off of instances.

## Worker instance

_20 messages waiting in the queue (25 seconds ago)_

Requests are being added to your worker environment's queue faster than they can be
processed. Scale your environment to increase capacity.

_5 messages in Dead Letter Queue (15 seconds ago)_

Worker requests are failing repeatedly and being added to the [Dead-letter queues](using-features-managing-env-tiers.md#worker-deadletter "using-features-managing-env-tiers.md#worker-deadletter"). Check the requests in the dead-letter
queue to see why they are failing.

## Other resources

_4 active instances is below Auto Scaling group minimum size 5_

The number of instances running in your environment is fewer than the minimum configured
for the Auto Scaling group.

_Auto Scaling group (groupname) notifications have been deleted or
modified_

The notifications configured for your Auto Scaling group have been modified outside of
Elastic Beanstalk.
