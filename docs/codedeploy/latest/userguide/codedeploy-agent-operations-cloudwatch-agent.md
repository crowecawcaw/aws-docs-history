# Send CodeDeploy agent logs to

CloudWatch

You can send CodeDeploy agent metric and log data to CloudWatch using the [unified CloudWatch agent](../../../AmazonCloudWatch/latest/logs/UseCloudWatchUnifiedAgent.md "../../../AmazonCloudWatch/latest/logs/UseCloudWatchUnifiedAgent.md"),
or more simply, the CloudWatch agent.

Use the following instructions to install the CloudWatch agent and configure it for use with CodeDeploy
agents.

## Prerequisites

Before you begin, complete the following tasks:

- Install the CodeDeploy agent and make sure it's running. For more information, see [Install the CodeDeploy agent](codedeploy-agent-operations-install.md "codedeploy-agent-operations-install.md") and [Verify the CodeDeploy agent is running](codedeploy-agent-operations-verify.md "codedeploy-agent-operations-verify.md").
- Install the CloudWatch agent. For more information, see [Installing the CloudWatch agent](../../../AmazonCloudWatch/latest/monitoring/install-CloudWatch-Agent-on-EC2-Instance.md "../../../AmazonCloudWatch/latest/monitoring/install-CloudWatch-Agent-on-EC2-Instance.md").
- Add the following permissions to the CodeDeploy IAM instance profile:

      + CloudWatchLogsFullAccess
      + CloudWatchAgentServerPolicy

  For more information on the CodeDeploy instance profile, see [Step 4: Create an IAM instance
  profile for your Amazon EC2 instances](getting-started-create-iam-instance-profile.md "getting-started-create-iam-instance-profile.md") of [Getting started with CodeDeploy](getting-started-codedeploy.md "getting-started-codedeploy.md").

## Configure the CloudWatch agent to

collect CodeDeploy logs

You can configure the CloudWatch agent by stepping through a wizard or by manually creating or
editing a configuration file.

###### To configure the CloudWatch agent using the wizard (Linux)

1. Run the wizard, as described in [Run the CloudWatch agent configuration wizard](../../../AmazonCloudWatch/latest/monitoring/create-cloudwatch-agent-configuration-file-wizard.md#cloudwatch-agent-running-wizard "../../../AmazonCloudWatch/latest/monitoring/create-cloudwatch-agent-configuration-file-wizard.md#cloudwatch-agent-running-wizard").
2. In the wizard, when asked `Do you want to monitor any log files?` enter
   `1`.
3. Specify the CodeDeploy agent log file, as follows:
   1. For `Log file path` enter the path for the CodeDeploy log file, for example:
      `/var/log/aws/codedeploy-agent/codedeploy-agent.log`.
   2. For `Log group name` enter a log group name, for example:
      `codedeploy-agent-log`.
   3. For `Log stream name` enter a log stream name, for example:
      `{instance_id}-codedeploy-agent-log`.

4. When asked `Do you want to specify any additional log files?`, enter
   `1`.
5. Specify the CodeDeploy agent deployment logs, as follows:
   1. For `Log file path` enter the path for the CodeDeploy deployment log file,
      for example:
      `/opt/codedeploy-agent/deployment-root/deployment-logs/codedeploy-agent-deployments.log`.
   2. For `Log group name` enter a log group name, for example:
      `codedeploy-agent-deployment-log`.
   3. For `Log stream name` enter a log stream name, for example:
      `{instance_id}-codedeploy-agent-deployment-log`.

6. When asked `Do you want to specify any additional log files?`, enter
   `1`.
7. Specify the CodeDeploy agent updater logs, as follows:
   1. For `Log file path` enter the path for the CodeDeploy updater log file, for
      example: `/tmp/codedeploy-agent.update.log`.
   2. For `Log group name` enter a log group name, for example:
      `codedeploy-agent-updater-log`.
   3. For `Log stream name` enter a log stream name, for example:
      `{instance_id}-codedeploy-agent-updater-log`.

###### To configure the CloudWatch agent using the wizard (Windows)

1. Run the wizard, as described in [Run the CloudWatch agent configuration wizard](../../../AmazonCloudWatch/latest/monitoring/create-cloudwatch-agent-configuration-file-wizard.md#cloudwatch-agent-running-wizard "../../../AmazonCloudWatch/latest/monitoring/create-cloudwatch-agent-configuration-file-wizard.md#cloudwatch-agent-running-wizard").
2. In the wizard, when asked `Do you want to monitor any customized log
files?` enter `1`.
3. Specify the CodeDeploy log file, as follows:
   1. For `Log file path` enter the path r the CodeDeploy agent log file, for
      example:
      `C:\ProgramData\Amazon\CodeDeploy\log\codedeploy-agent-log.txt`.
   2. For `Log group name` enter a log group name, for example:
      `codedeploy-agent-log`.
   3. For `Log stream name` enter a log stream name, for example:
      `{instance_id}-codedeploy-agent-log`.

4. When asked `Do you want to specify any additional log files?`, enter
   `1`.
5. Specify the CodeDeploy agent deployment logs, as follows:
   1. For `Log file path` enter the path the CodeDeploy deployment log file, for example:
      `C:\ProgramData\Amazon\CodeDeploy\deployment-logs\codedeploy-agent-deployments.log`.
   2. For `Log group name` enter a log group name, for example:
      `codedeploy-agent-deployment-log`.
   3. For `Log stream name` enter a log stream name, for example:
      `{instance_id}-codedeploy-agent-deployment-log`.

###### To configure the CloudWatch agent by manually creating or editing a configuration file

(Linux)

1. Create or edit the CloudWatch agent configuration file as described in [Manually create or edit the CloudWatch agent configuration file](../../../AmazonCloudWatch/latest/monitoring/CloudWatch-Agent-Configuration-File-Details.md "../../../AmazonCloudWatch/latest/monitoring/CloudWatch-Agent-Configuration-File-Details.md").
2. Make sure that the file is called
   `/opt/aws/amazon-cloudwatch-agent/etc/amazon-cloudwatch-agent.json`
   and that it contains the following code:

```
...
"logs": {
    "logs_collected": {
        "files": {
            "collect_list": [
                {
                    "file_path": "/var/log/aws/codedeploy-agent/codedeploy-agent.log",
                    "log_group_name": "codedeploy-agent-log",
                    "log_stream_name": "{instance_id}-agent-log"
                },
                {
                    "file_path": "/opt/codedeploy-agent/deployment-root/deployment-logs/codedeploy-agent-deployments.log",
                    "log_group_name": "codedeploy-agent-deployment-log",
                    "log_stream_name": "{instance_id}-codedeploy-agent-deployment-log"
                },
                {
                    "file_path": "/tmp/codedeploy-agent.update.log",
                    "log_group_name": "codedeploy-agent-updater-log",
                    "log_stream_name": "{instance_id}-codedeploy-agent-updater-log"
                }
            ]
        }
    }
}
...
```

###### To configure the CloudWatch agent by manually creating or editing a configuration file

(Windows)

1. Create or edit the CloudWatch agent configuration file as described in [Manually create or edit the CloudWatch agent configuration file](../../../AmazonCloudWatch/latest/monitoring/CloudWatch-Agent-Configuration-File-Details.md "../../../AmazonCloudWatch/latest/monitoring/CloudWatch-Agent-Configuration-File-Details.md").
2. Make sure that the file is called
   `C:\ProgramData\Amazon\AmazonCloudWatchAgent\amazon-cloudwatch-agent.json`
   and that it contains the following code:

```
...
"logs": {
        "logs_collected": {
            "files": {
                "collect_list": [
                    {
                        "file_path": "C:\\ProgramData\\Amazon\\CodeDeploy\\log\\codedeploy-agent-log.txt",
                        "log_group_name": "codedeploy-agent-log",
                        "log_stream_name": "{instance_id}-codedeploy-agent-log"
                    },
                    {
                        "file_path": "C:\\ProgramData\\Amazon\\CodeDeploy\\deployment-logs\\codedeploy-agent-deployments.log",
                        "log_group_name": "codedeploy-agent-deployment-log",
                        "log_stream_name": "{instance_id}-codedeploy-agent-deployment-log"
                    }
                ]
            },
            ...
        }
    },
...
```

## Restart the CloudWatch

agent

After making your changes, restart the CloudWatch agent as described in [Start the CloudWatch agent](../../../AmazonCloudWatch/latest/monitoring/install-CloudWatch-Agent-on-EC2-Instance-fleet.md#start-CloudWatch-Agent-EC2-fleet "../../../AmazonCloudWatch/latest/monitoring/install-CloudWatch-Agent-on-EC2-Instance-fleet.md#start-CloudWatch-Agent-EC2-fleet").
