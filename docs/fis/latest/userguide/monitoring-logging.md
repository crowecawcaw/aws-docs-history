

# Experiment logging for AWS FIS
<a name="monitoring-logging"></a>

You can use experiment logging to capture detailed information about your experiment as it runs.

You are charged for experiment logging based on the costs associated with each log destination type. For more information, see [Amazon CloudWatch Pricing](https://aws.amazon.com/cloudwatch/pricing/) (under **Paid Tier**, **Logs**, **Vended Logs**) and [Amazon S3 Pricing](https://aws.amazon.com/s3/pricing/).

## Permissions
<a name="permissions-experiment-logging"></a>

You must grant AWS FIS permissions to send logs to each log destination that you configure. For more information, see the following in the *Amazon CloudWatch Logs User Guide*:
+ [Logs sent to CloudWatch Logs](https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/AWS-logs-and-resource-policy.html#AWS-logs-infrastructure-CWL)
+ [Logs sent to Amazon S3](https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/AWS-logs-and-resource-policy.html#AWS-logs-infrastructure-S3)

## Log schema
<a name="experiment-log-schema"></a>

The following is the schema used in experiment logging. The current schema version is 2. The fields for `details` depend on the value of `log_type`. The fields for `resolved_targets` depend on the value of `target_type`. For more information, see [Example log records](#example-log-records).

```
{
    "id": "EXP123abc456def789",
    "log_type": "experiment-start | target-resolution-start | target-resolution-detail | target-resolution-end | action-start | action-error | action-end | experiment-end",
    "event_timestamp": "yyyy-mm-ddThh:mm:ssZ",
    "version": "2",
    "details": {
        "account_id":"123456789012",
        "action_end_time": "yyyy-mm-ddThh:mm:ssZ",
        "action_id": "String",
        "action_name": "String",
        "action_start_time": "yyyy-mm-ddThh:mm:ssZ",
        "action_state": {
            "status": "pending | initiating | running | completed | cancelled | stopping | stopped | failed",
            "reason": "String"
        },
        "action_targets": "String to string map",
        "error_information": "String",
        "experiment_end_time": "yyyy-mm-ddThh:mm:ssZ",
        "experiment_state": {
            "status": "pending | initiating | running | completed | stopping | stopped | failed",
            "reason": "String"
        },
        "experiment_start_time": "yyyy-mm-ddThh:mm:ssZ",
        "experiment_template_id": "String",
        "page": Number,
        "parameters": "String to string map",
        "resolved_targets": [
            {
               "{{field}}": "{{value}}"
            }
        ],
        "resolved_targets_count": Number,
        "status": "failed | completed",
        "target_name": "String",
        "target_resolution_end_time": "yyyy-mm-ddThh:mm:ssZ",
        "target_resolution_start_time": "yyyy-mm-ddThh:mm:ssZ",
        "target_type": "String",
        "total_pages": Number,
        "total_resolved_targets_count": Number

    }
}
```

**Release notes**
+ Version 2 introduces:
  + The `target_type` field and changes the `resolved_targets` field from a list of ARNs to a list of objects. The valid fields for the `resolved_targets` object depend on the value of `target_type`, which is the [resource type](targets.md#resource-types) of the targets.
  + The `action-error` and `target-resolution-detail` event types which add the `account_id` field.
+ Version 1 is the initial release.

## Log destinations
<a name="experiment-log-destinations"></a>

AWS FIS supports log delivery to the following destinations:
+ An Amazon S3 bucket
+ An Amazon CloudWatch Logs log group

**S3 log delivery**  
The logs are delivered to the following location.

```
{{bucket-and-optional-prefix}}/AWSLogs/{{account-id}}/fis/{{region}}/{{experiment-id}}/{{YYYY}}/{{MM}}/{{DD}}/{{account-id}}_awsfislogs_{{region}}_{{experiment-id}}_{{YYYYMMDDHHMM}}Z_{{hash}}.log
```

It can take several minutes before the logs are delivered to the bucket.

**CloudWatch Logs log delivery**  
The logs are delivered to a log stream named /aws/fis/{{experiment-id}}.

Logs are delivered to the log group in less than one minute.

## Example log records
<a name="example-log-records"></a>

The following are example log records for an experiment that runs the **aws:ec2:reboot-instances** action on an EC2 instance selected at random.

**Records**
+ [experiment-start](#experiment-start)
+ [target-resolution-start](#target-resolution-start)
+ [target-resolution-detail](#target-resolution-detail)
+ [target-resolution-end](#target-resolution-end)
+ [action-start](#action-start)
+ [action-end](#action-end)
+ [action-error](#action-error)
+ [experiment-end](#experiment-end)<a name="experiment-start"></a>

**experiment-start**  
The following is an example record for the `experiment-start` event.

```
{
    "id": "EXPhjAXCGY78HV2a4A",
    "log_type": "experiment-start",
    "event_timestamp": "2023-05-31T18:50:45Z",
    "version": "2",
    "details": {
        "experiment_template_id": "EXTCDh1M8HHkhxoaQ",
        "experiment_start_time": "2023-05-31T18:50:43Z"
    }
}
```<a name="target-resolution-start"></a>

**target-resolution-start**  
The following is an example record for the `target-resolution-start` event.

```
{
    "id": "EXPhjAXCGY78HV2a4A",
    "log_type": "target-resolution-start",
    "event_timestamp": "2023-05-31T18:50:45Z",
    "version": "2",
    "details": {
        "target_resolution_start_time": "2023-05-31T18:50:45Z",
        "target_name": "EC2InstancesToReboot"
    }
}
```<a name="target-resolution-detail"></a>

**target-resolution-detail**  
The following is an example record for the `target-resolution-detail` event. If target resolution fails, the record also includes the `error_information` field.

```
{
    "id": "EXPhjAXCGY78HV2a4A",
    "log_type": "target-resolution-detail",
    "event_timestamp": "2023-05-31T18:50:45Z",
    "version": "2",
    "details": {
        "target_resolution_end_time": "2023-05-31T18:50:45Z",
        "target_name": "EC2InstancesToReboot",
        "target_type": "aws:ec2:instance",
        "account_id": "123456789012",
        "resolved_targets_count": 2,
        "status": "completed"

    }
}
```<a name="target-resolution-end"></a>

**target-resolution-end**  
If target resolution fails, the record also includes the `error_information` field. If `total_pages` is greater than 1, the number of resolved targets exceeded the size limit for one record. There are additional `target-resolution-end` records that contain the remaining resolved targets.

The following is example record for the `target-resolution-end` event for an EC2 action.

```
{
    "id": "EXPhjAXCGY78HV2a4A",
    "log_type": "target-resolution-end",
    "event_timestamp": "2023-05-31T18:50:45Z",
    "version": "2",
    "details": {
        "target_resolution_end_time": "2023-05-31T18:50:46Z",
        "target_name": "EC2InstanceToReboot",
        "target_type": "aws:ec2:instance",
        "resolved_targets": [
            {
                "arn": "arn:aws:ec2:us-east-1:123456789012:instance/i-0f7ee2abffc330de5"
            }
        ],
        "page": 1,
        "total_pages": 1
    }
}
```

The following is example record for the `target-resolution-end` event for an EKS action.

```
{
    "id": "EXP24YfiucfyVPJpEJn",
    "log_type": "target-resolution-end",
    "event_timestamp": "2023-05-31T18:50:45Z",
    "version": "2",
    "details": {
        "target_resolution_end_time": "2023-05-31T18:50:46Z",
        "target_name": "myPods",
        "target_type": "aws:eks:pod",
        "resolved_targets": [
            {
                "pod_name": "example-696fb6498b-sxhw5",
                "namespace": "default",
                "cluster_arn": "arn:aws:eks:us-east-1:123456789012:cluster/fis-demo-cluster",
                "target_container_name": "example"
            }
        ],
        "page": 1,
        "total_pages": 1
    }
}
```<a name="action-start"></a>

**action-start**  
The following is an example record for the `action-start` event. If the experiment template specifies parameters for the action, the record also includes the `parameters` field.

```
{
    "id": "EXPhjAXCGY78HV2a4A",
    "log_type": "action-start",
    "event_timestamp": "2023-05-31T18:50:56Z",
    "version": "2",
    "details": {
        "action_name": "Reboot",
        "action_id": "aws:ec2:reboot-instances",
        "action_start_time": "2023-05-31T18:50:56Z",
        "action_targets": {"Instances":"EC2InstancesToReboot"}
    }
}
```<a name="action-error"></a>

**action-error**  
The following is an example record for the `action-error` event. This event is only returned when an action fails. It is returned for each account where the action fails. 

```
{
    "id": "EXPhjAXCGY78HV2a4A",
    "log_type": "action-error",
    "event_timestamp": "2023-05-31T18:50:56Z",
    "version": "2",
    "details": {
        "action_name": "pause-io",
        "action_id": "aws:ebs:pause-volume-io",
        "account_id": "123456789012",
        "action_state": {
            "status": "failed",
            "reason":"Unable to start Pause Volume IO. Target volumes must be attached to an instance type based on the Nitro system. VolumeId(s): [vol-1234567890abcdef0]:"
        }
    }
}
```<a name="action-end"></a>

**action-end**  
The following is an example record for the `action-end` event.

```
{
    "id": "EXPhjAXCGY78HV2a4A",
    "log_type": "action-end",
    "event_timestamp": "2023-05-31T18:50:56Z",
    "version": "2",
    "details": {
        "action_name": "Reboot",
        "action_id": "aws:ec2:reboot-instances",
        "action_end_time": "2023-05-31T18:50:56Z",
        "action_state": {
            "status": "completed",
            "reason": "Action was completed."
        }
    }
}
```<a name="experiment-end"></a>

**experiment-end**  
The following is an example record for the `experiment-end` event.

```
{
    "id": "EXPhjAXCGY78HV2a4A",
    "log_type": "experiment-end",
    "event_timestamp": "2023-05-31T18:50:57Z",
    "version": "2",
    "details": {
        "experiment_end_time": "2023-05-31T18:50:57Z",
        "experiment_state": {
            "status": "completed",
            "reason": "Experiment completed"
        }
    }
}
```

## Enable experiment logging
<a name="enable-experiment-logging"></a>

Experiment logging is disabled by default. To receive experiment logs for an experiment, you must create the experiment from an experiment template with logging enabled. The first time that you run an experiment that is configured to use a destination that hasn't been used previously for logging, we delay the experiment to configure log delivery to this destination, which takes about 15 seconds.

**To enable experiment logging using the console**

1. Open the AWS FIS console at [https://console.aws.amazon.com/fis/](https://console.aws.amazon.com/fis/).

1. In the navigation pane, choose **Experiment templates**.

1. Select the experiment template, and choose **Actions**, **Update experiment template**.

1. For **Logs**, configure the destination options. To send logs to an S3 bucket, choose **Send to an Amazon S3 bucket** and enter the bucket name and prefix. To send logs to CloudWatch Logs, choose **Send to CloudWatch Logs** and enter the log group.

1. Choose **Update experiment template**.

**To enable experiment logging using the AWS CLI**  
Use the [update-experiment-template](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/fis/update-experiment-template.html) command and specify a log configuration.

## Disable experiment logging
<a name="disable-experiment-logging"></a>

If you no longer want to receive logs for your experiments, you can disable experiment logging.

**To disable experiment logging using the console**

1. Open the AWS FIS console at [https://console.aws.amazon.com/fis/](https://console.aws.amazon.com/fis/).

1. In the navigation pane, choose **Experiment templates**.

1. Select the experiment template, and choose **Actions**, **Update experiment template**.

1. For **Logs**, clear **Send to an Amazon S3 bucket** and **Send to CloudWatch Logs**.

1. Choose **Update experiment template**.

**To disable experiment logging using the AWS CLI**  
Use the [update-experiment-template](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/fis/update-experiment-template.html) command and specify an empty log configuration.