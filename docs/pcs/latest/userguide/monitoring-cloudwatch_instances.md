# Monitoring AWS PCS instances using

Amazon CloudWatch

AWS PCS launches Amazon EC2 instances as needed to meet the scaling requirements defined in
your PCS compute node groups. You can monitor these instances while they are running using
Amazon CloudWatch. You can inspect the logs of running instances by logging into them and using
interactive command line tools. However, by default, CloudWatch metrics data is only retained
for a limited period once an instance is terminated, and instance logs are usually deleted along
with the EBS volumes that back the instance. To retain metrics or logging data from the
instances launched by PCS after they are terminated, you can configure the CloudWatch agent on
your instances with an EC2 launch template. This topic provides an overview of monitoring
running instances and provides examples of how to configure persistent instance metrics and
logs.

## Monitoring running instances

### Finding AWS PCS instances

To monitor instances launched by PCS, find the running instances associated with a
cluster or compute node group. Then, in the EC2 console for a given instance, inspect the
**Status and alarms** and **Monitoring** sections. If
login access is configured for those instances, you can connect to them and inspect various
log files on the instances. For more information on identifying which instances are managed
by PCS, see [Finding compute node group instances in
AWS PCS](working-with_compute-instances.md "working-with_compute-instances.md").

### Enabling detailed

metrics

By default, instance metrics are collected at 5-minute intervals. To collect metrics at
one minute intervals, enable detailed CloudWatch monitoring in your compute node group
launch template. For more information, see [Turn on detailed CloudWatch
monitoring](working-with_launch-templates_parameters.md#working-with_launch-templates_parameters_cw "working-with_launch-templates_parameters.md#working-with_launch-templates_parameters_cw").

## Configuring persistent

instance metrics and logs

You can retain the metrics and logs from your instances by installing and configuring the
Amazon CloudWatch agent on them. This consists of three main steps:

1. Create a CloudWatch agent configuration.
2. Store the configuration where it can be retrieved by PCS instances.
3. Write an EC2 launch template that installs the CloudWatch agent software, fetches
   your configuration, and starts the CloudWatch agent using the configuration.

For more information, see [Collect metrics,
logs, and traces with the CloudWatch agent](../../../AmazonCloudWatch/latest/monitoring/Install-CloudWatch-Agent.md "../../../AmazonCloudWatch/latest/monitoring/Install-CloudWatch-Agent.md") in the _Amazon CloudWatch User
Guide_, and [Using Amazon EC2 launch templates
with AWS PCS](working-with_launch-templates.md "working-with_launch-templates.md").

### Create a CloudWatch Agent

configuration

Before deploying the CloudWatch agent on your instances, you must generate a JSON
configuration file that specifies the metrics, logs, and traces to collect. Configuration
files can be created using a wizard or manually, using a text editor. The configuration file
will be created manually for this demonstration.

On a computer where you have the AWS CLI installed, create a CloudWatch configuration
file named **config.json** with the contents that follow. You
can also use the following URL to download a copy of the file.

```
https://aws-hpc-recipes.s3.amazonaws.com/main/recipes/pcs/cloudwatch/assets/config.json
```

###### Notes

- The log paths in the sample file are for Amazon Linux 2. If your instances will use
  a different base operating system, change the paths as appropriate.
- To capture other logs, add additional entries under
  `collect_list`.
- Values in `{brackets}` are templated variables. For the complete list of
  supported variables, see [Manually create or edit the CloudWatch agent configuration file](../../../AmazonCloudWatch/latest/monitoring/CloudWatch-Agent-Configuration-File-Details.md "../../../AmazonCloudWatch/latest/monitoring/CloudWatch-Agent-Configuration-File-Details.md") in the
  _Amazon CloudWatch User Guide_.
- You can choose to omit `logs` or `metrics` if you don't want
  to collect these information types.

```
{
    "agent": {
        "metrics_collection_interval": 60
    },
    "logs": {
        "logs_collected": {
            "files": {
                "collect_list": [
                    {
                        "file_path": "/var/log/cloud-init.log",
                        "log_group_class": "STANDARD",
                        "log_group_name": "/PCSLogs/instances",
                        "log_stream_name": "{instance_id}.cloud-init.log",
                        "retention_in_days": 30
                    },
                    {
                        "file_path": "/var/log/cloud-init-output.log",
                        "log_group_class": "STANDARD",
                        "log_stream_name": "{instance_id}.cloud-init-output.log",
                        "log_group_name": "/PCSLogs/instances",
                        "retention_in_days": 30
                    },
                    {
                        "file_path": "/var/log/amazon/pcs/bootstrap.log",
                        "log_group_class": "STANDARD",
                        "log_stream_name": "{instance_id}.bootstrap.log",
                        "log_group_name": "/PCSLogs/instances",
                        "retention_in_days": 30
                    },
                    {
                        "file_path": "/var/log/slurmd.log",
                        "log_group_class": "STANDARD",
                        "log_stream_name": "{instance_id}.slurmd.log",
                        "log_group_name": "/PCSLogs/instances",
                        "retention_in_days": 30
                    },
                    {
                        "file_path": "/var/log/messages",
                        "log_group_class": "STANDARD",
                        "log_stream_name": "{instance_id}.messages",
                        "log_group_name": "/PCSLogs/instances",
                        "retention_in_days": 30
                    },
                    {
                        "file_path": "/var/log/secure",
                        "log_group_class": "STANDARD",
                        "log_stream_name": "{instance_id}.secure",
                        "log_group_name": "/PCSLogs/instances",
                        "retention_in_days": 30
                    }
                ]
            }
        }
    },
    "metrics": {
        "aggregation_dimensions": [
            [
                "InstanceId"
            ]
        ],
        "append_dimensions": {
            "AutoScalingGroupName": "${aws:AutoScalingGroupName}",
            "ImageId": "${aws:ImageId}",
            "InstanceId": "${aws:InstanceId}",
            "InstanceType": "${aws:InstanceType}"
        },
        "metrics_collected": {
            "cpu": {
                "measurement": [
                    "cpu_usage_idle",
                    "cpu_usage_iowait",
                    "cpu_usage_user",
                    "cpu_usage_system"
                ],
                "metrics_collection_interval": 60,
                "resources": [
                    "*"
                ],
                "totalcpu": false
            },
            "disk": {
                "measurement": [
                    "used_percent",
                    "inodes_free"
                ],
                "metrics_collection_interval": 60,
                "resources": [
                    "*"
                ]
            },
            "diskio": {
                "measurement": [
                    "io_time"
                ],
                "metrics_collection_interval": 60,
                "resources": [
                    "*"
                ]
            },
            "mem": {
                "measurement": [
                    "mem_used_percent"
                ],
                "metrics_collection_interval": 60
            },
            "swap": {
                "measurement": [
                    "swap_used_percent"
                ],
                "metrics_collection_interval": 60
            }
        }
    }
}
```

This file instructs the CloudWatch agent to monitor several files that can be helpful
in diagnosing errors in instance bootstrapping, authentication and login, and other
troubleshooting domains. These include:

- `/var/log/cloud-init.log` – Output from the initial stage of
  instance configuration
- `/var/log/cloud-init-output.log` – Output from commands that run
  during instance configuration
- `/var/log/amazon/pcs/bootstrap.log` – Output from PCS-specific
  operations that run during instance configuration
- `/var/log/slurmd.log` – Output from the Slurm workload manager's
  daemon slurmd
- `/var/log/messages` – System messages from the kernel, system
  services, and applications
- `/var/log/secure` – Logs related to authentication attempts, such
  as SSH, sudo, and other security events

The log files are sent to a CloudWatch log group named `/PCSLogs/instances`.
The log streams are a combination of the instance ID and the base name of the log file. The
log group has a retention time of 30 days.

In addition, the file instructs CloudWatch agent to collect several common metrics,
aggregating them by instance ID.

### Store the

configuration

The CloudWatch agent configuration file has to be stored where it can be accessed by
PCS compute node instances. There are two common ways to do this. You can upload it to an
Amazon S3 bucket that your compute node group instances will have access to via their
instance profile, Alternatively, you can store it as an SSM parameter in Amazon Systems
Manager Parameter Store.

#### Upload to an S3

bucket

To store your file in S3, use the AWS CLI commands that follow. Before running the
command, make these replacements:

- Replace `amzn-s3-demo-bucket` with your own S3 bucket
  name

First, (this is optional if you have an existing bucket), create a bucket to hold
your configuration file(s).

```
aws s3 mb s3://`amzn-s3-demo-bucket`
```

Next, upload the file to the bucket.

```
aws s3 cp ./config.json s3://`amzn-s3-demo-bucket`/
```

#### Store as an SSM

parameter

To store your file as an SSM parameter, use the command that follows. Before running
the command, make these replacements:

- Replace `region-code` with the AWS Region where you are
  working with AWS PCS.
- (Optional) Replace `AmazonCloudWatch-PCS` with your own
  name for the parameter. Note that if you change the prefix of the name from
  `AmazonCloudWatch-` you will need to specifically add read access to the
  SSM parameter in your node group instance profile.

```
aws ssm put-parameter \
   --region `region-code` \
   --name "`AmazonCloudWatch-PCS`" \
   --type String \
   --value file://config.json
```

### Write an EC2 launch template

The specific details for the launch template depend on whether your configuration file
is stored in S3 or SSM.

#### Use a configuration stored in S3

This script installs CloudWatch agent, imports a configuration file from an S3 bucket,
and launches the CloudWatch agent with it. Replace the following values in this script
with your own details:

- `amzn-s3-demo-bucket` – The name of an S3 bucket your
  account can read from
- `/config.json` – Path relative to the S3 bucket root
  where the configuration is stored

```
MIME-Version: 1.0
Content-Type: multipart/mixed; boundary="==MYBOUNDARY=="

--==MYBOUNDARY==
Content-Type: text/cloud-config; charset="us-ascii"

packages:
- amazon-cloudwatch-agent

runcmd:
- aws s3 cp s3://`amzn-s3-demo-bucket``/config.json` /etc/s3-cw-config.json
- /opt/aws/amazon-cloudwatch-agent/bin/amazon-cloudwatch-agent-ctl -a fetch-config -m ec2 -s -c file://etc/s3-cw-config.json

--==MYBOUNDARY==--
```

The IAM instance profile for the node group must have access to the bucket. Here is
an example IAM policy for the bucket in the user data script above.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Action": [
 "s3:GetObject",
 "s3:ListBucket"
 ],
 "Resource": [
 "arn:aws:s3:::`amzn-s3-demo-bucket`",
 "arn:aws:s3:::`amzn-s3-demo-bucket`/*"
 ]
 }
 ]
}`

```

Also note that the instances must allow outbound traffic to the S3 and CloudWatch
endpoints. This can be accomplished using security groups or VPC endpoints, depending on
your cluster architecture.

#### Use a configuration stored in

SSM

This script installs CloudWatch agent, imports a configuration file from an SSM
parameter, and launches the CloudWatch agent with it. Replace the following values in this
script with your own details:

- (Optional) Replace `AmazonCloudWatch-PCS` with your own
  name for the parameter.

```
MIME-Version: 1.0
Content-Type: multipart/mixed; boundary="==MYBOUNDARY=="

--==MYBOUNDARY==
Content-Type: text/cloud-config; charset="us-ascii"

packages:
- amazon-cloudwatch-agent

runcmd:
- /opt/aws/amazon-cloudwatch-agent/bin/amazon-cloudwatch-agent-ctl -a fetch-config -m ec2 -s -c ssm:`AmazonCloudWatch-PCS`

--==MYBOUNDARY==--
```

The IAM instance policy for the node group must have the **CloudWatchAgentServerPolicy** attached to it.

If your parameter name does not start with `AmazonCloudWatch-` you will need to
specifically add read access to the SSM parameter in your node group instance profile.
Here is an example IAM policy that illustrates this for prefix `DOC-EXAMPLE-PREFIX`.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement" : [
 {
 "Sid" : "CustomCwSsmMParamReadOnly",
 "Effect" : "Allow",
 "Action" : [
 "ssm:GetParameter"
 ],
 "Resource" : "arn:aws:ssm:*:*:parameter/`DOC-EXAMPLE-PREFIX`*"
 }
 ]
}`

```

Also note that the instances must allow outbound traffic to the SSM and CloudWatch
endpoints. This can be accomplished using security groups or VPC endpoints, depending on
your cluster architecture.
