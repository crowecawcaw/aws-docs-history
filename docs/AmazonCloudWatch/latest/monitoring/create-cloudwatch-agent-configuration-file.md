

# Create the CloudWatch agent configuration file
<a name="create-cloudwatch-agent-configuration-file"></a>

Before running the CloudWatch agent on any servers, you must create one or more CloudWatch agent configuration files. 

The agent configuration file is a JSON file that specifies the metrics, logs, and traces that the agent is to collect, including custom metrics. You can create it by using the wizard or by creating it yourself from scratch. You could also use the wizard to initially create the configuration file and then modify it manually. If you create or modify the file manually, the process is more complex, but you have more control over the metrics collected and can specify metrics not available through the wizard.

Any time you change the agent configuration file, you must then restart the agent to have the changes take effect. To restart the agent, follow the instructions in [(Optional) Modify the common configuration and named profile for CloudWatch agent](installing-cloudwatch-agent-ssm.md#CloudWatch-Agent-profile-instance-fleet).

After you have created a configuration file, you can save it manually as a JSON file and then use this file when installing the agent on your servers. Alternatively, you can store it in Systems Manager Parameter Store if you're going to use Systems Manager when you install the agent on servers.

The CloudWatch agent supports using multiple configuration files. For more information, see [Creating multiple CloudWatch agent configuration files](#CloudWatch-Agent-multiple-config-files).

Metrics, logs, and traces collected by the CloudWatch agent incur charges. For more information about pricing, see [Amazon CloudWatch Pricing](http://aws.amazon.com/cloudwatch/pricing).

**Topics**
+ [Create the CloudWatch agent configuration file with the wizard](create-cloudwatch-agent-configuration-file-wizard.md)
+ [Creating multiple CloudWatch agent configuration files](#CloudWatch-Agent-multiple-config-files)
+ [Manually create or edit the CloudWatch agent configuration file](CloudWatch-Agent-Configuration-File-Details.md)
+ [Log collection patterns and limitations](#CloudWatch-Agent-log-collection-patterns)
+ [Optimize custom metrics cost](#CloudWatch-Agent-custom-metrics-cost)
+ [Configuration changes and restart behavior](#CloudWatch-Agent-config-restart-behavior)

## Creating multiple CloudWatch agent configuration files
<a name="CloudWatch-Agent-multiple-config-files"></a>

On both Linux servers and Windows servers, you can set up the CloudWatch agent to use multiple configuration files. For example, you can use a common configuration file that collects a set of metrics, logs, and traces that you always want to collect from all servers in your infrastructure. You can then use additional configuration files that collect metrics from certain applications or in certain situations.

To set this up, first create the configuration files that you want to use. Any configuration files that will be used together on the same server must have different file names. You can store the configuration files on servers or in Parameter Store.

Start the CloudWatch agent using the `fetch-config` option and specify the first configuration file. To append the second configuration file to the running agent, use the same command but with the `append-config` option. All metrics, logs, and traces listed in either configuration file are collected. The following example commands illustrate this scenario using configurations stores as files. The first line starts the agent using the `infrastructure.json` configuration file, and the second line appends the `app.json` configuration file.

The following example commands are for Linux.

```
/opt/aws/amazon-cloudwatch-agent/bin/amazon-cloudwatch-agent-ctl -a fetch-config -m ec2 -s -c file:/tmp/infrastructure.json
```

```
/opt/aws/amazon-cloudwatch-agent/bin/amazon-cloudwatch-agent-ctl -a append-config -m ec2 -s -c file:/tmp/app.json
```

The following example commands are for Windows Server.

```
& "C:\Program Files\Amazon\AmazonCloudWatchAgent\amazon-cloudwatch-agent-ctl.ps1" -a fetch-config -m ec2 -s -c file:"C:\Program Files\Amazon\AmazonCloudWatchAgent\infrastructure.json"
```

```
& "C:\Program Files\Amazon\AmazonCloudWatchAgent\amazon-cloudwatch-agent-ctl.ps1" -a append-config -m ec2 -s -c file:"C:\Program Files\Amazon\AmazonCloudWatchAgent\app.json"
```

The following example configuration files illustrate a use for this feature. The first configuration file is used for all servers in the infrastructure, and the second collects only logs from a certain application and is appended to servers running that application.

**infrastructure.json**

```
{
  "metrics": {
    "metrics_collected": {
      "cpu": {
        "resources": [
          "*"
        ],
        "measurement": [
          "usage_active"
        ],
        "totalcpu": true
      },
      "mem": {
         "measurement": [
           "used_percent"
        ]
      }
    }
  },
  "logs": {
    "logs_collected": {
      "files": {
        "collect_list": [
          {
            "file_path": "/opt/aws/amazon-cloudwatch-agent/logs/amazon-cloudwatch-agent.log",
            "log_group_name": "amazon-cloudwatch-agent.log"
          },
          {
            "file_path": "/var/log/messages",
            "log_group_name": "/var/log/messages"
          }
        ]
      }
    }
  }
}
```

**app.json**

```
{
    "logs": {
        "logs_collected": {
            "files": {
                "collect_list": [
                    {
                        "file_path": "/app/app.log*",
                        "log_group_name": "/app/app.log"
                    }
                ]
            }
        }
    }
}
```

Any configuration files appended to the configuration must have different file names from each other and from the initial configuration file. If you use `append-config` with a configuration file with the same file name as a configuration file that the agent is already using, the append command overwrites the information from the first configuration file instead of appending to it. This is true even if the two configuration files with the same file name are on different file paths.

The preceding example shows the use of two configuration files, but there is no limit to the number of configuration files that you can append to the agent configuration. You can also mix the use of configuration files located on servers and configurations located in Parameter Store.

## Log collection patterns and limitations
<a name="CloudWatch-Agent-log-collection-patterns"></a>

Understanding how the CloudWatch agent selects and tails log files is important for proper configuration:
+ By default, the `file_path` wildcard matches files by modification time, and the agent tails only the newest matching file. To tail every matching file instead, set `publish_multi_logs` to true.
+ If multiple new files appear between poll cycles, earlier ones might be skipped entirely
+ This design targets continuously appended or rotated logs, not batches of discrete complete files

The agent handles log rotation as follows:
+ Without `auto_removal`, the agent does not stop the tailer on the old file; it keeps reading the old file alongside the new one.
+ With `auto_removal`, the agent reads the old file to the end, stops, and then deletes it. `auto_removal` does not work together with `publish_multi_logs`.

For batch file patterns (for example, thousands of discrete files appearing at once), consider using Amazon S3 upload or direct `PutLogEvents` API calls instead of the CloudWatch agent.

## Optimize custom metrics cost
<a name="CloudWatch-Agent-custom-metrics-cost"></a>

These common sources cause unexpectedly high metric counts:
+ Broad procstat collection. Using `"exe": ".*"` matches every process, creating a separate metric for each process and measurement.
+ Metrics for each filesystem. On instances with many mounts (containers, EBS volumes), each mount generates separate metrics.
+ Per-CPU metrics. Setting `"resources": ["*"]` on CPU with many vCPUs multiplies metrics by core count.

To reduce cost, use the following strategies:
+ Use `aggregation_dimensions` to reduce cardinality (aggregate across instances, volumes, and other resources).
+ Only include measurement values you actually need and will alert on
+ Use `drop_original_metrics` when using aggregation to avoid publishing both aggregated and per-dimension metrics.

## Configuration changes and restart behavior
<a name="CloudWatch-Agent-config-restart-behavior"></a>

All configuration changes require an agent restart to take effect. Use the fetch-config action.

If your configuration is stored in SSM Parameter Store, reference it with `ssm:`. In the following commands, replace {{parameter-name}} with the name of your Parameter Store parameter.

The following command fetches the configuration from Parameter Store on Linux:

```
sudo /opt/aws/amazon-cloudwatch-agent/bin/amazon-cloudwatch-agent-ctl \
    -a fetch-config \
    -s -m ec2 \
    -c ssm:{{parameter-name}}
```

The following command fetches the configuration from Parameter Store on Windows. Run it in PowerShell as an administrator:

```
& "$Env:ProgramFiles\Amazon\AmazonCloudWatchAgent\amazon-cloudwatch-agent-ctl.ps1" -a fetch-config -m ec2 -s -c ssm:{{parameter-name}}
```

If the configuration is stored in a local file on the instance, reference it with `file:` and the full path instead.

The following command fetches the configuration from a local file on Linux:

```
sudo /opt/aws/amazon-cloudwatch-agent/bin/amazon-cloudwatch-agent-ctl \
    -a fetch-config \
    -s -m ec2 \
    -c file:/opt/aws/amazon-cloudwatch-agent/etc/cloudwatch-agent.json
```

The following command fetches the configuration from a local file on Windows. Run it in PowerShell as an administrator:

```
& "$Env:ProgramFiles\Amazon\AmazonCloudWatchAgent\amazon-cloudwatch-agent-ctl.ps1" -a fetch-config -m ec2 -s -c file:"$Env:ProgramData\Amazon\AmazonCloudWatchAgent\cloudwatch-agent.json"
```

The Windows commands use the following elements:
+ `$Env:ProgramFiles` resolves to the program files directory (typically `C:\Program Files`) where the agent control script is installed.
+ `$Env:ProgramData` resolves to the program data directory (typically `C:\ProgramData`). If your configuration file is in a different location, replace the path after `file:` with its full path.

The state file preserves log read offsets across restarts, so the agent does not re-send logs after a restart. The agent sends only the new log lines that are written after the last saved offset.