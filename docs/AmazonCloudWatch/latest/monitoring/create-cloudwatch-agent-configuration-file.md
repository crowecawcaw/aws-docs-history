# Create the CloudWatch agent

configuration file

Before running the CloudWatch agent on any servers, you must create one or more CloudWatch agent
configuration files.

The agent configuration file is a JSON file that specifies the metrics, logs, and traces
that the agent is to collect, including custom metrics. You can create it by using the wizard
or by creating it yourself from scratch. You could also use the wizard to initially create the
configuration file and then modify it manually. If you create or modify the file manually, the
process is more complex, but you have more control over the metrics collected and can specify
metrics not available through the wizard.

Any time you change the agent configuration file, you must then restart the agent to have
the changes take effect. To restart the agent, follow the instructions in [(Optional) Modify the common
configuration and named profile for CloudWatch agent](installing-cloudwatch-agent-ssm.md#CloudWatch-Agent-profile-instance-fleet "installing-cloudwatch-agent-ssm.md#CloudWatch-Agent-profile-instance-fleet").

After you have created a configuration file, you can save it manually as a JSON file and
then use this file when installing the agent on your servers. Alternatively, you can store it
in Systems Manager Parameter Store if you're going to use Systems Manager when you install the agent on servers.

The CloudWatch agent supports using multiple configuration files. For more information, see
[Creating multiple CloudWatch agent
configuration files](#CloudWatch-Agent-multiple-config-files "#CloudWatch-Agent-multiple-config-files").

Metrics, logs, and traces collected by the CloudWatch agent incur charges. For more information
about pricing, see [Amazon CloudWatch
Pricing](http://aws.amazon.com/cloudwatch/pricing "http://aws.amazon.com/cloudwatch/pricing").

###### Contents

- [Create the CloudWatch agent
  configuration file with the wizard](create-cloudwatch-agent-configuration-file-wizard.md "create-cloudwatch-agent-configuration-file-wizard.md")
- [Creating multiple CloudWatch agent
  configuration files](#CloudWatch-Agent-multiple-config-files "#CloudWatch-Agent-multiple-config-files")
- [Manually create or edit the
  CloudWatch agent configuration file](CloudWatch-Agent-Configuration-File-Details.md "CloudWatch-Agent-Configuration-File-Details.md")

## Creating multiple CloudWatch agent

configuration files

On both Linux servers and Windows servers, you can set up the CloudWatch agent to use multiple
configuration files. For example, you can use a common configuration file that collects a
set of metrics, logs, and traces that you always want to collect from all servers in your
infrastructure. You can then use additional configuration files that collect metrics from
certain applications or in certain situations.

To set this up, first create the configuration files that you want to use. Any
configuration files that will be used together on the same server must have different file
names. You can store the configuration files on servers or in Parameter Store.

Start the CloudWatch agent using the `fetch-config` option and specify the first
configuration file. To append the second configuration file to the running agent, use the
same command but with the `append-config` option. All metrics, logs, and traces
listed in either configuration file are collected. The following example commands illustrate
this scenario using configurations stores as files. The first line starts the agent using
the `infrastructure.json` configuration file, and the second line appends
the `app.json` configuration file.

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

The following example configuration files illustrate a use for this feature. The first
configuration file is used for all servers in the infrastructure, and the second collects
only logs from a certain application and is appended to servers running that
application.

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

Any configuration files appended to the configuration must have different file names
from each other and from the initial configuration file. If you use
`append-config` with a configuration file with the same file name as a
configuration file that the agent is already using, the append command overwrites the
information from the first configuration file instead of appending to it. This is true even
if the two configuration files with the same file name are on different file paths.

The preceding example shows the use of two configuration files, but there is no limit to
the number of configuration files that you can append to the agent configuration. You can
also mix the use of configuration files located on servers and configurations located in
Parameter Store.
