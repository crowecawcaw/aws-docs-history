

# Environment detail
<a name="environments-dashboard-tabs"></a>

This topic describes the additional information that the environment management console provides from the left navigation pane and the tabbed pages.

The following image illustrates the environment management console.

![Image of the environment management console.](http://docs.aws.amazon.com/elasticbeanstalk/latest/dg/images/environment-overview-v2-margin.png)


The bottom half of the environment management console lists tabs that provide more detailed and varied information about the environment. To view a page, either select its tab or select its name from the left navigation pane under the environment name. The **Events** tab displays by default.

The left navigation pane also includes **Go to environment**, which isn't one of the tabbed pages.

**Note**  
Select **Go to environment** to open the running application.

## Events
<a name="environments-console-events"></a>

The **Events** tab shows the event stream for your environment. Elastic Beanstalk outputs event messages whenever you interact with the environment, and when any of your environment's resources are created or modified as a result.

For more information, see [Viewing an Elastic Beanstalk environment's event stream](using-features.events.md).

## Configuration
<a name="environments-console-configuration"></a>

Use the **Configuration** tab to view and update current configuration settings for your environment and its resources. Settings include networking, database, load balancing, notifications, health monitoring, managed platform updates, deployments, instance log streaming, CloudWatch integration, AWS X-Ray, proxy server, environment properties, and platform-specific options. Use these settings to customize the behavior of your environment during deployments and enable additional features. You can also modify the instance type and other settings that you chose during environment creation.

For more information, see [Configuring Elastic Beanstalk environments](customize-containers.md).

## Deployments
<a name="environments-console-deployments"></a>

The **Deployments** tab shows the deployment history for your environment. Each row lists a deployment's request ID, status, type, policy, start time, and duration. By default, the tab shows deployments from the last 42 days (6 weeks); you can adjust this window. You can filter the list to find a specific deployment.

Select a deployment's request ID to open its detail page, which includes the following.

**Deployment summary**  
Shows the deployment's request ID, status, type, start time, duration, and deployment policy. For an application deployment, it also shows the application version deployed and the previous version, with links to their source bundles.

**Events**  
Lists the environment events that Elastic Beanstalk emitted during the deployment, so you can trace its progress and pinpoint where a failure occurred.

**Deployment Logs**  
Provides a consolidated view of the deployment logs from your environment's instances. You can search the log, filter by log level, follow the tail as new entries arrive, and download the log. For more information, see [Viewing logs from Amazon EC2 instances in your Elastic Beanstalk environment](using-features.logging.md).

For more information about deploying application versions, see [Deploying applications to Elastic Beanstalk environments](using-features.deploy-existing-version.md).

## Health & monitoring
<a name="environments-console-health"></a>

The **Health & monitoring** tab combines health, monitoring, and alarms information for your environment in a single view. It contains the following sections.

**Overall health** and **Enhanced instance health**  
If enhanced health monitoring is enabled, this section lists the EC2 instances in your environment and live health information for each instance. The **Overall health** view shows health data as an average for all of your environment’s instances combined. The **Enhanced instance health** view shows live health information for each individual EC2 instance, including information about the requests served by the instances and metrics from the operating system, such as latency, load, and CPU utilization. Enhanced health monitoring enables Elastic Beanstalk to closely monitor the resources in your environment so that it can assess the health of your application more accurately. For more information, see [Enhanced health reporting and monitoring in Elastic Beanstalk](health-enhanced.md).

**Monitoring**  
Shows an overview of health information for your environment. This includes the default set of metrics provided by Elastic Load Balancing and Amazon EC2, and graphs that show how the environment's health has changed over time. For more information, see [Monitoring environment health in the AWS management console](environment-health-console.md).

**Alarms**  
Shows information about any alarms that you have configured for your environment. You can use the options in this section to create or delete alarms. For more information, see [Manage alarms](using-features.alarms.md).

## Logs
<a name="environments-console-logs"></a>

The **Logs** tab has two sections.

**CloudWatch Logs**  
Lists the CloudWatch log groups that your environment streams logs to, with each group's stored bytes, retention, and creation time. Select a log group to view its log streams, or use the actions to open the group in the CloudWatch console, run **Logs Insights**, or view **Live Tail**. If log streaming isn't enabled, choose **Enable CloudWatch log streaming** to turn it on. For more information, see [Using Elastic Beanstalk with Amazon CloudWatch Logs](AWSHowTo.cloudwatchlogs.md).

Requesting instance logs  
Retrieve logs from the EC2 instances in your environment. When you request logs, Elastic Beanstalk sends a command to the instances, which then upload logs to your Elastic Beanstalk storage bucket in Amazon S3. When you request logs on this tab, Elastic Beanstalk automatically deletes them from Amazon S3 after 15 minutes. You can also configure your environment's instances to upload logs to Amazon S3 for permanent storage after they have been rotated locally. For more information, see [Viewing logs from Amazon EC2 instances in your Elastic Beanstalk environment](using-features.logging.md).

## Managed updates
<a name="environments-console-managedupdates"></a>

The **Managed updates** tab shows information about upcoming and completed managed platform updates and instance replacement.

The managed update feature lets you configure your environment to update to the latest platform version automatically during a weekly maintenance window that you choose. In between platform releases, you can choose to have your environment replace all of its Amazon EC2 instances during the maintenance window. This can alleviate issues that occur when your application runs for extended periods of time.

For more information, see [Managed platform updates](environment-platform-update-managed.md).

## Tags
<a name="environments-console-tags"></a>

The **Tags** tab shows the tags that Elastic Beanstalk applied to the environment when you created it, and any tags that you added. You can add, edit, and delete custom tags. You can't edit or delete the tags that Elastic Beanstalk applied.

Environment tags are applied to every resource that Elastic Beanstalk creates to support your application.

For more information, see [Tagging resources in your Elastic Beanstalk environments](using-features.tagging.md).