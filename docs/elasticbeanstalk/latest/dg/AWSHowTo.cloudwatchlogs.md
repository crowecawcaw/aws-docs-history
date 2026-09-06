

# Using Elastic Beanstalk with Amazon CloudWatch Logs
<a name="AWSHowTo.cloudwatchlogs"></a>

This topic explains the monitoring features that the Amazon CloudWatch Logs service can provide to Elastic Beanstalk. It also walks you through the configuration setup and lists the locations of the logs for each Elastic Beanstalk platform. 

Implementing CloudWatch Logs can enable you to do the following monitoring activities:
+ Monitor and archive your Elastic Beanstalk application, system, and custom log files from the Amazon EC2 instances of your environments.
+ Configure alarms that make it easier for you to react to specific log stream events that your metric filters extract.

The CloudWatch Logs agent installed on each Amazon EC2 instance in your environment publishes metric data points to the CloudWatch service for each log group you configure. Each log group applies its own filter patterns to determine what log stream events to send to CloudWatch as data points. Log streams that belong to the same log group share the same retention, monitoring, and access control settings. You can configure Elastic Beanstalk to automatically stream logs to the CloudWatch service, as described in [Streaming instance logs to CloudWatch Logs](#AWSHowTo.cloudwatchlogs.streaming). For more information about CloudWatch Logs, including terminology and concepts, see the [Amazon CloudWatch Logs User Guide](https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/WhatIsCloudWatchLogs.html).

In addition to instance logs, if you enable [enhanced health](health-enhanced.md) for your environment, you can configure the environment to stream health information to CloudWatch Logs. See [Streaming Elastic Beanstalk environment health information to Amazon CloudWatch Logs](AWSHowTo.cloudwatchlogs.envhealth.md).

**Topics**
+ [Prerequisite for instance log streaming to CloudWatch Logs](#AWSHowTo.cloudwatchlogs.prereqs)
+ [How Elastic Beanstalk sets up CloudWatch Logs](#AWSHowTo.cloudwatchlogs.loggroups)
+ [Streaming instance logs to CloudWatch Logs](#AWSHowTo.cloudwatchlogs.streaming)
+ [Troubleshooting CloudWatch Logs integration](#AWSHowTo.cloudwatchlogs.troubleshoot)
+ [Streaming Elastic Beanstalk environment health information to Amazon CloudWatch Logs](AWSHowTo.cloudwatchlogs.envhealth.md)

## Prerequisite for instance log streaming to CloudWatch Logs
<a name="AWSHowTo.cloudwatchlogs.prereqs"></a>

If you don't have the *AWSElasticBeanstalkWebTier* or *AWSElasticBeanstalkWorkerTier* Elastic Beanstalk managed policy in your [Elastic Beanstalk instance profile](concepts-roles-instance.md), you must add the following permissions to your profile to enable this feature.

------
#### [ JSON ]

****  

```
{
  "Version":"2012-10-17",		 	 	 
  "Statement": [
  {
    "Effect": "Allow",
    "Action": [
      "logs:PutLogEvents",
      "logs:CreateLogStream"
    ],
    "Resource": [
    "*"
    ]
  }
  ]
}
```

------

## How Elastic Beanstalk sets up CloudWatch Logs
<a name="AWSHowTo.cloudwatchlogs.loggroups"></a>

Elastic Beanstalk installs a CloudWatch log agent with the default configuration settings on each instance it creates. Learn more in the [CloudWatch agent documentation](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/Install-CloudWatch-Agent.html).

When you enable instance log streaming to CloudWatch Logs, Elastic Beanstalk sends log files from your environment's instances to CloudWatch Logs. Different platforms stream different logs. The following table lists the logs, by platform.



|  Platform / Platform Branch  |  Logs  | 
| --- | --- | 
| Docker |  +  /var/log/eb-engine.log <br />+  /var/log/eb-hooks.log <br />+  /var/log/docker <br />+  /var/log/docker-events.log <br />+  /var/log/eb-docker/containers/eb-current-app/stdouterr.log <br />+  /var/log/nginx/access.log <br />+  /var/log/nginx/error.log   | 
| ECS on Docker |  +  /var/log/docker-events.log <br />+  /var/log/eb-ecs-mgr.log <br />+  /var/log/eb-engine.log <br />+  /var/log/eb-hooks.log <br />+  /var/log/ecs/ecs-agent.log <br />+  /var/log/ecs/ecs-init.log   | 
| Go<br />.NET Core on Linux<br />Java |  +  /var/log/eb-engine.log <br />+  /var/log/eb-hooks.log <br />+  /var/log/web.stdout.log <br />+  /var/log/nginx/access.log <br />+  /var/log/nginx/error.log   | 
| Node.js<br />Python |  +  /var/log/eb-engine.log <br />+  /var/log/eb-hooks.log <br />+  /var/log/web.stdout.log <br />+  /var/log/httpd/access\_log <br />+  /var/log/httpd/error\_log <br />+  /var/log/nginx/access.log <br />+  /var/log/nginx/error.log   | 
| Tomcat<br />PHP |  +  /var/log/eb-engine.log <br />+  /var/log/eb-hooks.log <br />+  /var/log/httpd/access\_log <br />+  /var/log/httpd/error\_log <br />+  /var/log/nginx/access.log <br />+  /var/log/nginx/error.log   | 
| .NET on Windows Server |  +  C:\\inetpub\\logs\\LogFiles\\W3SVC1\\u\_ex\*.log <br />+  C:\\Program Files\\Amazon\\ElasticBeanstalk\\logs\\AWSDeployment.log <br />+  C:\\Program Files\\Amazon\\ElasticBeanstalk\\logs\\Hooks.log   | 
| Ruby |  +  /var/log/eb-engine.log <br />+  /var/log/eb-hooks.log <br />+  /var/log/puma/puma.log <br />+  /var/log/web.stdout.log <br />+  /var/log/nginx/access.log <br />+  /var/log/nginx/error.log   | 

### Log files on Amazon Linux AMI platforms
<a name="AWSHowTo.cloudwatchlogs.loggroups.alami"></a>

**Note**  
 On [July 18, 2022](https://docs.aws.amazon.com/elasticbeanstalk/latest/relnotes/release-2022-07-18-linux-al1-retire.html), Elastic Beanstalk set the status of all platform branches based on Amazon Linux AMI (AL1) to **retired**. For more information about migrating to a current and fully supported Amazon Linux 2023 platform branch, see [Migrating your Elastic Beanstalk Linux application to Amazon Linux 2023 or Amazon Linux 2](using-features.migration-al.md).

The following table lists the log files streamed from instances on platform branches based on Amazon Linux AMI (preceding Amazon Linux 2), by platform.



|  Platform / Platform Branch  |  Logs  | 
| --- | --- | 
| Docker / <br />Platform Branch: Docker Running on 64bit Amazon Linux |  +  /var/log/eb-activity.log <br />+  /var/log/nginx/error.log <br />+  /var/log/docker-events.log <br />+  /var/log/docker <br />+  /var/log/nginx/access.log <br />+  /var/log/eb-docker/containers/eb-current-app/stdouterr.log   | 
| Docker / <br />Platform Branch: Multicontainer Docker Running on 64bit Amazon Linux |  +  /var/log/eb-activity.log <br />+  /var/log/ecs/ecs-init.log <br />+  /var/log/eb-ecs-mgr.log <br />+  /var/log/ecs/ecs-agent.log <br />+  /var/log/docker-events.log   | 
| Glassfish (Preconfigured Docker) |  +  /var/log/eb-activity.log <br />+  /var/log/nginx/error.log <br />+  /var/log/docker-events.log <br />+  /var/log/docker <br />+  /var/log/nginx/access.log   | 
| Go |  +  /var/log/eb-activity.log <br />+  /var/log/nginx/error.log <br />+  /var/log/nginx/access.log   | 
| Java /<br />Platform Branch: Java 8 running on 64bit Amazon Linux<br />Platform Branch: Java 7 running on 64bit Amazon Linux |  +  /var/log/eb-activity.log <br />+  /var/log/nginx/access.log <br />+  /var/log/nginx/error.log <br />+  /var/log/web-1.error.log <br />+  /var/log/web-1.log   | 
| Tomcat |  +  /var/log/eb-activity.log <br />+  /var/log/httpd/error\_log <br />+  /var/log/httpd/access\_log <br />+  /var/log/nginx/error\_log <br />+  /var/log/nginx/access\_log   | 
| Node.js |  +  /var/log/eb-activity.log <br />+  /var/log/nodejs/nodejs.log <br />+  /var/log/nginx/error.log <br />+  /var/log/nginx/access.log <br />+  /var/log/httpd/error.log <br />+  /var/log/httpd/access.log   | 
| PHP |  +  /var/log/eb-activity.log <br />+  /var/log/httpd/error\_log <br />+  /var/log/httpd/access\_log   | 
| Python |  +  /var/log/eb-activity.log <br />+  /var/log/httpd/error\_log <br />+  /var/log/httpd/access\_log <br />+  /opt/python/log/supervisord.log   | 
| Ruby /<br />Platform Branch: Puma with Ruby running on 64bit Amazon Linux |  +  /var/log/eb-activity.log <br />+  /var/log/nginx/error.log <br />+  /var/log/puma/puma.log <br />+  /var/log/nginx/access.log   | 
| Ruby / Platform Branch: Passenger with Ruby running on 64bit Amazon Linux |  +  /var/log/eb-activity.log <br />+  /var/app/support/logs/passenger.log <br />+  /var/app/support/logs/access.log <br />+  /var/app/support/logs/error.log   | 

Elastic Beanstalk configures log groups in CloudWatch Logs for the various log files that it streams. To retrieve specific log files from CloudWatch Logs, you have to know the name of the corresponding log group. The log group naming scheme depends on the platform's operating system.

For Linux platforms, prefix the on-instance log file location with `/aws/elasticbeanstalk/{{environment_name}}` to get the log group name. For example, to retrieve the file `/var/log/nginx/error.log`, specify the log group `/aws/elasticbeanstalk/{{environment_name}}/var/log/nginx/error.log`.

For Windows platforms, see the following table for the log group corresponding to each log file.


|  On-instance log file  |  Log group  | 
| --- | --- | 
| `C:\Program Files\Amazon\ElasticBeanstalk\logs\AWSDeployment.log` | `/aws/elasticbeanstalk/<environment-name>/EBDeploy-Log` | 
| `C:\Program Files\Amazon\ElasticBeanstalk\logs\Hooks.log` | `/aws/elasticbeanstalk/<environment-name>/EBHooks-Log` | 
| `C:\inetpub\logs\LogFiles` (the entire directory) | `/aws/elasticbeanstalk/<environment-name>/IIS-Log` | 

## Streaming instance logs to CloudWatch Logs
<a name="AWSHowTo.cloudwatchlogs.streaming"></a>

You can enable instance log streaming to CloudWatch Logs using the Elastic Beanstalk console, the EB CLI, or configuration options.

Before you enable it, set up IAM permissions to use with the CloudWatch Logs agent. If you're using the *AWSElasticBeanstalkWebTier* or *AWSElasticBeanstalkWorkerTier* managed policy (see [Prerequisite for instance log streaming to CloudWatch Logs](#AWSHowTo.cloudwatchlogs.prereqs)), you already have the necessary permissions. Otherwise, attach the following custom policy to the [instance profile](concepts-roles-instance.md) that you assign to your environment.

------
#### [ JSON ]

****  

```
{
  "Version":"2012-10-17",		 	 	 
  "Statement": [
    {
      "Effect": "Allow",
      "Action": [
        "logs:CreateLogStream",
        "logs:PutLogEvents",
        "logs:DescribeLogGroups",
        "logs:DescribeLogStreams"
      ],
      "Resource": [
        "*"
      ]
    }
  ]
}
```

------

### Instance log streaming using the Elastic Beanstalk console
<a name="AWSHowTo.cloudwatchlogs.streaming.console"></a>

**To stream instance logs to CloudWatch Logs**

1. Open the [Elastic Beanstalk console](https://console.aws.amazon.com/elasticbeanstalk), and in the **Regions** list, select your AWS Region.

1. In the navigation pane, choose **Environments**, and then choose the name of your environment from the list.

1. In the navigation pane, choose **Configuration**.

1. In the **Updates, monitoring, and logging** configuration category, choose **Edit**.

1. Under **Instance log streaming to CloudWatch Logs**:
   + Enable **Log streaming**.
   + Set **Retention** to the number of days to save the logs.
   + Select the **Lifecycle** setting that determines whether the logs are saved after the environment is terminated.
**Important**  
If you select **Delete logs upon termination**, the log groups and all log data are permanently deleted when you terminate the environment. This action cannot be undone. To preserve logs for debugging or compliance, select **Keep logs after terminating environment**.

1. To save the changes choose **Apply** at the bottom of the page.

After you enable log streaming, Elastic Beanstalk displays the streamed CloudWatch Logs log groups in the environment management console, on the **Logs** page. Choose a log group to view its log events in a built-in viewer—Elastic Beanstalk automatically selects the most recently active log stream, and you can switch streams, search and filter events, and load earlier events.

### Instance log streaming using the EB CLI
<a name="AWSHowTo.cloudwatchlogs.streaming.ebcli"></a>

To enable instance log streaming to CloudWatch Logs using the EB CLI, use the [**eb logs**](eb3-logs.md) command.

```
$ eb logs --cloudwatch-logs enable
```

You can also use **eb logs** to retrieve logs from CloudWatch Logs. You can retrieve all the environment's instance logs, or use the command's many options to specify subsets of logs to retrieve. For example, the following command retrieves the complete set of instance logs for your environment, and saves them to a directory under `.elasticbeanstalk/logs`.

```
$ eb logs --all
```

In particular, the `--log-group` option enables you to retrieve instance logs of a specific log group, corresponding to a specific on-instance log file. To do that, you need to know the name of the log group that corresponds to the log file you want to retrieve. You can find this information in [How Elastic Beanstalk sets up CloudWatch Logs](#AWSHowTo.cloudwatchlogs.loggroups).

### Instance log streaming using configuration files
<a name="AWSHowTo.cloudwatchlogs.files"></a>

When you create or update an environment, you can use a configuration file to set up and configure instance log streaming to CloudWatch Logs. The following example configuration file enables default instance log streaming. Elastic Beanstalk streams the default set of log files for your environment's platform. To use the example, copy the text into a file with the `.config` extension in the `.ebextensions` directory at the top level of your application source bundle.

```
option_settings:
  - namespace: aws:elasticbeanstalk:cloudwatch:logs
    option_name: StreamLogs
    value: true
```

### Custom log file streaming
<a name="AWSHowTo.cloudwatchlogs.streaming.custom"></a>

The Elastic Beanstalk integration with CloudWatch Logs doesn't directly support the streaming of custom log files that your application generates. To stream custom logs, use a configuration file to directly install the CloudWatch agent and to configure the files to be pushed. For an example configuration file, see [`logs-streamtocloudwatch-linux.config`](https://github.com/awsdocs/elastic-beanstalk-samples/tree/main/configuration-files/aws-provided/instance-configuration/logs-streamtocloudwatch-linux.config).

**Note**  
The example doesn't work on the Windows platform.

For more information about configuring CloudWatch Logs, see the [CloudWatch agent configuration file reference](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch-Agent-Configuration-File-Details.html) in the *Amazon CloudWatch User Guide*.

## Troubleshooting CloudWatch Logs integration
<a name="AWSHowTo.cloudwatchlogs.troubleshoot"></a>

**Try Amazon Q Developer CLI for AI-assisted troubleshooting**  
 Amazon Q Developer CLI can help you troubleshoot environment issues quickly. The Q CLI provides solutions by checking environment status, reviewing events, analyzing logs, and asking clarifying questions. For more information and detailed walkthroughs, see [Troubleshooting Elastic Beanstalk Environments with Amazon Q Developer CLI ](https://aws.amazon.com/blogs/devops/troubleshooting-elastic-beanstalk-environments-with-amazon-q-developer-cli/) in the AWS blogs.

**Unable to locate environment instance logs**  
If you can't find some of the environment's instance logs that you expect in CloudWatch Logs, investigate the following common issues:
+ Your IAM role lacks the required IAM permissions.
+ You launched your environment in an AWS Region that doesn't support CloudWatch Logs.
+ One of your custom log files doesn't exist in the path you specified.

**Application logs missing or intermittent**  
If your Elastic Beanstalk application logs, (`/var/log/web.stdout.log`), appear to be missing or intermittent, this may be due to default rate-limiting settings in rsyslog and journald. While disabling rate-limiting entirely can resolve this issue, it's not recommended as it could lead to excessive disk usage, potential denial of service, or system performance degradation during unexpected log bursts. Instead, you can adjust the rate limits using the following [`.ebextensions configuration`](https://github.com/awsdocs/elastic-beanstalk-samples/tree/main/configuration-files/aws-provided/instance-configuration/logs-ratelimitcloudwatchlogs-linux.config). This configuration increases the rate limit interval to 600 seconds with higher burst limits, providing a balance between proper logging and system protection. 

**Log stream creation fails due to API throttling**  
If an Elastic Beanstalk operation that concurrently launches a large number of instances returns a message like `Error: fail to create log stream: ThrottlingException: Rate exceeded`, the operation is making too many concurrent calls to the CloudWatch API.

To resolve the throttling issue take one of the following actions:
+ Use a smaller batch size with rolling deployments to reduce concurrent updates.
+ Request an increase for your AWS account's Transaction Per Second (TPS) limit service quota for *CreateLogStream*. For more information, see [ CloudWatch Logs quotas](https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/cloudwatch_limits_cwl.html) and [ Managing your CloudWatch Logs service quotas](https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/cloudwatch_limits_cwl.html#service-quotas-manage) in the *Amazon CloudWatch Logs User Guide*.