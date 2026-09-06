

# **eb logs**
<a name="eb3-logs"></a>

## Description
<a name="eb3-logsdescription"></a>

The **eb logs** command has three distinct purposes: to enable or disable log streaming to CloudWatch Logs, to retrieve instance logs or CloudWatch Logs logs, and to request AI-powered analysis of your environment. With the `--cloudwatch-logs` (`-cw`) option, the command enables or disables log streaming. With the `--analyze` (`-ai`) option, the command requests an AI-powered analysis of your environment's logs, events, and instance health. Without either of these options, it retrieves logs.

When retrieving logs, specify the `--all`, `--zip`, or `--stream` option to retrieve complete logs. If you don't specify any of these options, Elastic Beanstalk retrieves tail logs.

The command processes logs for the specified or default environment. Relevant logs vary by container type. If the root directory contains a `platform.yaml` file specifying a custom platform, this command also processes logs for the builder environment.

For more information, see [Using Elastic Beanstalk with Amazon CloudWatch Logs](AWSHowTo.cloudwatchlogs.md). For more information about AI-powered analysis, see [AI-powered environment analysis](health-ai-analysis.md).

## Syntax
<a name="eb3-logssyntax"></a>

 To enable or disable log streaming to CloudWatch Logs: 

```
eb logs --cloudwatch-logs [enable | disable] [--cloudwatch-log-source instance | environment-health | all] [{{environment-name}}]
```

 To retrieve instance logs: 

```
eb logs [-all | --zip | --stream] [--cloudwatch-log-source instance] [--instance {{instance-id}}] [--log-group {{log-group}}] [{{environment-name}}]
```

 To retrieve environment health logs: 

```
eb logs [-all | --zip | --stream] --cloudwatch-log-source environment-health [{{environment-name}}]
```

 To request AI-powered analysis: 

```
eb logs --analyze [{{environment-name}}]
```

## Options
<a name="eb3-logsoptions"></a>



|  Name  |  Description  | 
| --- | --- | 
| `-cw [enable \| disable]`<br />or<br />`--cloudwatch-logs [enable \| disable]` | Enables or disables log streaming to CloudWatch Logs. If no argument is supplied, log streaming is enabled. If the `--cloudwatch-log-source` (`-cls`) option isn't specified in addition, instance log streaming is enabled or disabled. | 
| `-cls instance \| environment-health \| all`<br />or<br />`--cloudwatch-log-source instance \| environment-health \| all` | Specifies the source of logs when working with CloudWatch Logs. With the enable or disable form of the command, these are the logs for which to enable or disable CloudWatch Logs streaming. With the retrieval form of the command, these are the logs to retrieve from CloudWatch Logs.<br />Valid values:+  With `--cloudwatch-logs` (enable or disable) – `instance \| environment-health \| all` <br />+  Without `--cloudwatch-logs` (retrieve) – `instance \| environment-health` <br />Value meanings:+  `instance` (default) – Instance logs <br />+  `environment-health` – Environment health logs (supported only when enhanced health is enabled in the environment) <br />+  `all` – Both log sources  | 
| `-a`<br />or<br />`--all` | Retrieves complete logs and saves them to the `.elasticbeanstalk/logs` directory. | 
| `-z`<br />or<br />`--zip` | Retrieves complete logs, compresses them into a `.zip` file, and then saves the file to the `.elasticbeanstalk/logs` directory. | 
| `--stream` | Streams (continuously outputs) complete logs. With this option, the command keeps running until you interrupt it (press **Ctrl\+C**). | 
| `-i {{instance-id}}`<br />or<br />`--instance {{instance-id}}` | Retrieves logs for the specified instance only. | 
| `-g {{log-group}}`<br />or<br />`--log-group {{log-group}}` | Specifies the CloudWatch Logs log group from which to retrieve logs. The option is valid only when instance log streaming to CloudWatch Logs is enabled.<br />If instance log streaming is enabled, and you don't specify the `--log-group` option, the default log group is one of the following:+  Amazon Linux 2 – `/aws/elasticbeanstalk/{{environment-name}}/var/log/eb-engine.log` <br />+  Windows platforms – `/aws/elasticbeanstalk/{{environment-name}}/EBDeploy-Log` <br />+  Amazon Linux AMI (AL1) – `/aws/elasticbeanstalk/{{environment-name}}/var/log/eb-activity.log`   On [July 18, 2022](https://docs.aws.amazon.com/elasticbeanstalk/latest/relnotes/release-2022-07-18-linux-al1-retire.html), Elastic Beanstalk set the status of all platform branches based on Amazon Linux AMI (AL1) to **retired**. For more information about migrating to a current and fully supported Amazon Linux 2023 platform branch, see [Migrating your Elastic Beanstalk Linux application to Amazon Linux 2023 or Amazon Linux 2](using-features.migration-al.md).  <br />For information about the log group corresponding to each log file, see [How Elastic Beanstalk sets up CloudWatch Logs](AWSHowTo.cloudwatchlogs.md#AWSHowTo.cloudwatchlogs.loggroups). | 
| `-ai`<br />or<br />`--analyze` | Requests an AI-powered analysis of your environment's logs, events, and instance health. The analysis uses Amazon Bedrock to identify root causes and recommend solutions for environment health issues. The command sends the request, waits for the analysis to complete, and then displays the results.<br />This option is not compatible with `--instance`, `--all`, `--zip`, `--log-group`, or `--cloudwatch-logs`.<br />For prerequisites and required permissions, see [AI-powered environment analysis](health-ai-analysis.md). | 
| [Common options](eb3-cmd-options.md) |  | 

## Output
<a name="eb3-logsoutput"></a>

By default, displays the logs directly in the terminal. Uses a paging program to display the output. Press **Q** or **q** to exit.

With `--stream`, shows existing logs in the terminal and keeps running. Press **Ctrl\+C** to exit.

With `--all` and `--zip`, saves the logs to local files and displays the file location.

With `--analyze`, displays the AI-generated analysis directly in the terminal after the analysis completes.

## Examples
<a name="logsexample"></a>

The following example enables instance log streaming to CloudWatch Logs.

```
$ eb logs -cw enable
Enabling instance log streaming to CloudWatch for your environment
After the environment is updated you can view your logs by following the link:
https://console.aws.amazon.com/cloudwatch/home?region=us-east-1#logs:prefix=/aws/elasticbeanstalk/{{environment-name}}/
Printing Status:
2018-07-11 21:05:20    INFO: Environment update is starting.
2018-07-11 21:05:27    INFO: Updating environment {{environment-name}}'s configuration settings.
2018-07-11 21:06:45    INFO: Successfully deployed new configuration to environment.
```

The following example retrieves instance logs into a `.zip` file.

```
$ eb logs --zip
Retrieving logs...
Logs were saved to /home/workspace/environment/.elasticbeanstalk/logs/150622_173444.zip
```

The following example requests an AI-powered analysis of the environment.

```
$ eb logs --analyze
Analyzing environment...
No critical issues detected. Environment appears healthy.

---
Note: This analysis was generated by AI.
```