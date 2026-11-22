

# Common scenarios with the CloudWatch agent

 This section provides you with different scenarios that outline how to complete common configuration and customization tasks for the CloudWatch agent. 

**Topics**
+ [Running the CloudWatch agent as a different user](#CloudWatch-Agent-run-as-user)
+ [How the CloudWatch agent handles sparse log files](#CloudWatch-Agent-sparse-log-files)
+ [Adding custom dimensions to metrics collected by the CloudWatch agent](#CloudWatch-Agent-adding-custom-dimensions)
+ [Aggregating or rolling up metrics collected by the CloudWatch agent](#CloudWatch-Agent-aggregating-metrics)
+ [Collecting high-resolution metrics with the CloudWatch agent](#CloudWatch-Agent-collect-high-resolution-metrics)
+ [Sending metrics, logs, and traces to a different account](#CloudWatch-Agent-send-to-different-AWS-account)
+ [Installing the CloudWatch agent on Amazon EKS](#CloudWatch-Agent-install-on-eks)

## Running the CloudWatch agent as a different user
<a name="CloudWatch-Agent-run-as-user"></a>

On Linux servers, the CloudWatch runs as the root user by default. To have the agent run as a different user, use the `run_as_user` parameter in the `agent` section in the CloudWatch agent configuration file. This option is available only on Linux servers.

If you're already running the agent with the root user and want to change to using a different user, use one of the following procedures.

**To run the CloudWatch agent as a different user on an EC2 instance running Linux**

1. Download and install a new CloudWatch agent package. For more information, see [Download the CloudWatch agent package](download-CloudWatch-Agent-on-EC2-Instance-commandline-first.md).

1. Create a new Linux user or use the default user named `cwagent` that the RPM or DEB file created.

1. Provide credentials for this user in one of these ways:
   + If the file `.aws/credentials` exists in the home directory of the root user, you must create a credentials file for the user you are going to use to run the CloudWatch agent. This credentials file will be `/home/{{username}}/.aws/credentials`. Then set the value of the `shared_credential_file` parameter in `common-config.toml` to the pathname of the credential file. For more information, see [Install the CloudWatch agent using AWS Systems Manager](installing-cloudwatch-agent-ssm.md).
   + If the file `.aws/credentials` does not exist in the home directory of the root user, you can do one of the following:
     + Create a credentials file for the user you are going to use to run the CloudWatch agent. This credentials file will be `/home/{{username}}/.aws/credentials`. Then set the value of the `shared_credential_file` parameter in `common-config.toml` to the pathname of the credential file. For more information, see [Install the CloudWatch agent using AWS Systems Manager](installing-cloudwatch-agent-ssm.md).
     + Instead of creating a credentials file, attach an IAM role to the instance. The agent uses this role as the credential provider.

1. In the CloudWatch agent configuration file, add the following line in the `agent` section:

   ```
   "run_as_user": "{{username}}"
   ```

   Make other modifications to the configuration file as needed. For more information, see [Create the Classic CloudWatch agent configuration file](create-cloudwatch-agent-configuration-file.md)

1. Give the user the required permissions. The user must have Read (r) permissions for the log files to be collected, and must have Execute (x) permission on every directory in the log files' path.

1. Start the agent with the configuration file that you just modified.

   ```
   sudo /opt/aws/amazon-cloudwatch-agent/bin/amazon-cloudwatch-agent-ctl -a fetch-config -m ec2 -s -c file:{{configuration-file-path}}
   ```

**To run the CloudWatch agent as a different user on an on-premises server running Linux**

1. Download and install a new CloudWatch agent package. For more information, see [Download the CloudWatch agent package](download-CloudWatch-Agent-on-EC2-Instance-commandline-first.md).

1. Create a new Linux user or use the default user named `cwagent` that the RPM or DEB file created.

1. Store the credentials of this user to a path that the user can access, such as `/home/{{username}}/.aws/credentials`.

1. Set the value of the `shared_credential_file` parameter in `common-config.toml` to the pathname of the credential file. For more information, see [Install the CloudWatch agent using AWS Systems Manager](installing-cloudwatch-agent-ssm.md).

1. In the CloudWatch agent configuration file, add the following line in the `agent` section:

   ```
   "run_as_user": "{{username}}"
   ```

   Make other modifications to the configuration file as needed. For more information, see [Create the Classic CloudWatch agent configuration file](create-cloudwatch-agent-configuration-file.md)

1. Give the user required permissions. The user must have Read (r) permissions for the log files to be collected, and must have Execute (x) permission on every directory in the log files' path.

1. Start the agent with the configuration file that you just modified.

   ```
   sudo /opt/aws/amazon-cloudwatch-agent/bin/amazon-cloudwatch-agent-ctl -a fetch-config -m ec2 -s -c file:{{configuration-file-path}}
   ```

## How the CloudWatch agent handles sparse log files
<a name="CloudWatch-Agent-sparse-log-files"></a>

Sparse files are files with both empty blocks and real contents. A sparse file uses disk space more efficiently by writing brief information representing the empty blocks to disk instead of the actual null bytes which makes up the block. This makes the actual size of a sparse file usually much smaller than its apparent size.

However, the CloudWatch agent doesn't treat sparse files differently than it treats normal files. When the agent reads a sparse file, the empty blocks are treated as "real" blocks filled with null bytes. Because of this, the CloudWatch agent publishes as many bytes as the apparent size of a sparse file to CloudWatch. 

Configuring the CloudWatch agent to publish a sparse file can cause higher than expected CloudWatch costs, so we recommend not to do so. For example, `/var/log/lastlog` in Linux is usually a very sparse file, and we recommend that you don't publish it to CloudWatch. 

## Adding custom dimensions to metrics collected by the CloudWatch agent
<a name="CloudWatch-Agent-adding-custom-dimensions"></a>

**Note**  
This applies to the Classic configuration. In the OpenTelemetry configuration, add labels to all telemetry with `resource_attributes`, and aggregate with PromQL at query time. For more information, see [Common customizations](CloudWatch-Agent-config-model.md#CloudWatch-Agent-OpenTelemetry-config-customize).

To add custom dimensions such as tags to metrics collected by the agent, add the `append_dimensions` field to the section of the agent configuration file that lists those metrics.

For example, the following example section of the configuration file adds a custom dimension named `stackName` with a value of `Prod` to the `cpu` and `disk` metrics collected by the agent.

```json
"cpu":{  
  "resources":[  
    "*"
  ],
  "measurement":[  
    "cpu_usage_guest",
    "cpu_usage_nice",
    "cpu_usage_idle"
  ],
  "totalcpu":false,
  "append_dimensions":{  
    "stackName":"Prod"
  }
},
"disk":{  
  "resources":[  
    "/",
    "/tmp"
  ],
  "measurement":[  
    "total",
    "used"
  ],
  "append_dimensions":{  
    "stackName":"Prod"
  }
}
```

Remember that any time you change the agent configuration file, you must restart the agent to have the changes take effect.

## Aggregating or rolling up metrics collected by the CloudWatch agent
<a name="CloudWatch-Agent-aggregating-metrics"></a>

**Note**  
This applies to the Classic configuration. In the OpenTelemetry configuration, add labels to all telemetry with `resource_attributes`, and aggregate with PromQL at query time. For more information, see [Common customizations](CloudWatch-Agent-config-model.md#CloudWatch-Agent-OpenTelemetry-config-customize).

To aggregate or roll up metrics collected by the agent, add an `aggregation_dimensions` field to the section for that metric in the agent configuration file.

For example, the following configuration file snippet rolls up metrics on the `AutoScalingGroupName` dimension. The metrics from all instances in each Auto Scaling group are aggregated and can be viewed as a whole.

```json
"metrics": {
  "cpu":{...}
  "disk":{...}
  "aggregation_dimensions" : [["AutoScalingGroupName"]]
}
```

To roll up along the combination of each `InstanceId` and `InstanceType` dimensions in addition to rolling up on the Auto Scaling group name, add the following.

```json
"metrics": {
  "cpu":{...}
  "disk":{...}
  "aggregation_dimensions" : [["AutoScalingGroupName"], ["InstanceId", "InstanceType"]]
}
```

To roll up metrics into one collection instead, use `[]`.

```json
"metrics": {
  "cpu":{...}
  "disk":{...}
  "aggregation_dimensions" : [[]]
}
```

Remember that any time you change the agent configuration file, you must restart the agent to have the changes take effect.

## Collecting high-resolution metrics with the CloudWatch agent
<a name="CloudWatch-Agent-collect-high-resolution-metrics"></a>

**Note**  
This applies to the Classic configuration, where metrics collected more often than every 60 seconds are published as high-resolution CloudWatch metrics. For the OpenTelemetry configuration, see [Common customizations](CloudWatch-Agent-config-model.md#CloudWatch-Agent-OpenTelemetry-config-customize).

The `metrics_collection_interval` field specifies the time interval for the metrics collected, in seconds. By specifying a value of less than 60 for this field, the metrics are collected as high-resolution metrics.

For example, if your metrics should all be high-resolution and collected every 10 seconds, specify 10 as the value for `metrics_collection_interval` under the `agent` section as a global metrics collection interval.

```json
"agent": {
  "metrics_collection_interval": 10
}
```

Alternatively, the following example sets the `cpu` metrics to be collected every second, and all other metrics are collected every minute.

```json
"agent":{  
  "metrics_collection_interval": 60
},
"metrics":{  
  "metrics_collected":{  
    "cpu":{  
      "resources":[  
        "*"
      ],
      "measurement":[  
        "cpu_usage_guest"
      ],
      "totalcpu":false,
      "metrics_collection_interval": 1
    },
    "disk":{  
      "resources":[  
        "/",
        "/tmp"
      ],
      "measurement":[  
        "total",
        "used"
      ]
    }
  }
}
```

Remember that any time you change the agent configuration file, you must restart the agent to have the changes take effect.

## Sending metrics, logs, and traces to a different account
<a name="CloudWatch-Agent-send-to-different-AWS-account"></a>

To have the CloudWatch agent send the metrics, logs, or traces to a different account, specify a `role_arn` parameter in the agent configuration file on the sending server. The `role_arn` value specifies an IAM role in the target account that the agent uses when sending data to the target account. This role enables the sending account to assume a corresponding role in the target account when delivering the metrics or logs to the target account.

You can also specify separate `role_arn` strings in the agent configuration file: one to use when sending metrics, another for sending logs, and another for sending traces.

The following example of part of the `agent` section of the configuration file sets the agent to use `CrossAccountAgentRole` when sending data to a different account.

```json
{
  "agent": {
    "credentials": {
      "role_arn": "arn:aws:iam::123456789012:role/CrossAccountAgentRole"
    }
  },
  .....
}
```

Alternatively, the following example sets different roles for the sending account to use for sending metrics, logs, and traces:

```json
"metrics": {
    "credentials": {
     "role_arn": "RoleToSendMetrics"
    },
    "metrics_collected": {....
```

```json
"logs": {
    "credentials": {
    "role_arn": "RoleToSendLogs"
    },
    ....
```

**Policies needed**

When you specify a `role_arn` in the agent configuration file, you must also make sure the IAM roles of the sending and target accounts have certain policies. The roles in both the sending and target accounts should have `CloudWatchAgentServerPolicy`. For more information about assigning this policy to a role, see [Prerequisites](prerequisites.md).

The role in the sending account also must include the following policy. You add this policy on the **Permissions** tab in the IAM console when you edit the role.

------
#### [ JSON ]

****  

```json
{
    "Version":"2012-10-17",		 	 	 
    "Statement": [
        {
            "Effect": "Allow",
            "Action": [
                "sts:AssumeRole"
            ],
            "Resource": [
                "arn:aws:iam::{{111122223333}}:role/{{agent-role-in-target-account}}"
            ]
        }
    ]
}
```

------

The role in the target account must include the following policy so that it recognizes the IAM role used by the sending account. You add this policy on the **Trust relationships** tab in the IAM console when you edit the role. This role is the role specified in `{{agent-role-in-target-account}}` in the policy used by the sending account.

------
#### [ JSON ]

****  

```json
{
    "Version":"2012-10-17",		 	 	 
    "Statement": [
        {
            "Effect": "Allow",
            "Principal": {
                "AWS": [
                    "arn:aws:iam::{{111122223333}}:role/{{role-in-sender-account}}"
                ]
            },
            "Action": "sts:AssumeRole"
        }
    ]
}
```

------

## Installing the CloudWatch agent on Amazon EKS
<a name="CloudWatch-Agent-install-on-eks"></a>

For Amazon EKS, install the CloudWatch agent using the Amazon CloudWatch Observability EKS add-on, or the equivalent Helm chart. This is the recommended and supported method for Amazon EKS. The add-on deploys and manages the CloudWatch agent and the Fluent Bit log collector for you. For instructions, see [Install the CloudWatch agent with the Amazon CloudWatch Observability EKS add-on or the Helm chart](install-CloudWatch-Observability-EKS-addon.md).

The Amazon CloudWatch Observability EKS add-on runs the agent with `hostNetwork: true` by default, so the default IMDSv2 hop limit of 1 is sufficient on the recommended path.

If you deploy the agent with a custom manifest that does not set `hostNetwork: true`, the agent pod's requests to the instance metadata service traverse an additional network hop. In that case, set the instance's IMDSv2 hop limit to 2, or the agent cannot retrieve credentials. To avoid relying on the instance metadata service, use EKS Pod Identity or IAM roles for service accounts (IRSA) to provide credentials to the agent.