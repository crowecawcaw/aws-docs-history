# Configuring service control policies for monitoring schedules

You have to specify the parameters of a monitoring job when you create or update a schedule for it with the
[CreateMonitoringSchedule](../APIReference/API_CreateMonitoringSchedule.md "../APIReference/API_CreateMonitoringSchedule.md") API or
the [UpdateMonitoringSchedule](../APIReference/API_UpdateMonitoringSchedule.md "../APIReference/API_UpdateMonitoringSchedule.md") API,
respectively. Depending on your use case, you can do this in one of the following ways:

- You can specify the [MonitoringJobDefinition](../APIReference/API_MonitoringJobDefinition.md "../APIReference/API_MonitoringJobDefinition.md")
  field of [MonitoringScheduleConfig](../APIReference/API_MonitoringScheduleConfig.md "../APIReference/API_MonitoringScheduleConfig.md"),
  when you invoke `CreateMonitoringSchedule` or `UpdateMonitoringSchedule`. You can
  use this only to create or update a schedule for a data quality monitoring job.
- You can specify the name of a monitoring job definition, that you have already created, for the
  `MonitoringJobDefinitionName` field of `MonitoringScheduleConfig`, when you invoke
  `CreateMonitoringSchedule` or `UpdateMonitoringSchedule`. You can use this for any
  job definition that you create with one of the following APIs:
  - [CreateDataQualityJobDefinition](../APIReference/API_CreateDataQualityJobDefinition.md "../APIReference/API_CreateDataQualityJobDefinition.md")
  - [CreateModelQualityJobDefinition](../APIReference/API_CreateModelQualityJobDefinition.md "../APIReference/API_CreateModelQualityJobDefinition.md")
  - [CreateModelBiasJobDefinition](../APIReference/API_CreateModelBiasJobDefinition.md "../APIReference/API_CreateModelBiasJobDefinition.md")
  - [CreateModelExplainabilityJobDefinition](../APIReference/API_CreateModelExplainabilityJobDefinition.md "../APIReference/API_CreateModelExplainabilityJobDefinition.md")

If you want to use the SageMaker Python SDK to create or update schedules, then you have to use this process.

The aforementioned processes are mutually exclusive, that is, you can either specify the
`MonitoringJobDefinition` field or the `MonitoringJobDefinitionName` field when creating
or updating monitoring schedules.

When you create a monitoring job definition, or specify one in the `MonitoringJobDefinition` field,
you can set security parameters, such as `NetworkConfig` and `VolumeKmsKeyId`. As an
administrator, you might want that these parameters are always set to certain values, so that the monitoring
jobs always run in a secure environment. To ensure this, set up appropriate [Service control policies](../../../organizations/latest/userguide/orgs_manage_policies_scps.md "../../../organizations/latest/userguide/orgs_manage_policies_scps.md") (SCPs).
SCPs are a type of organization policy that you can use to manage permissions in your organization.

The following example shows a SCP that you can use to ensure that infrastructure parameters are properly set
when creating or updating schedules for monitoring jobs.

```
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Effect": "Deny",
            "Action": [
                "sagemaker:CreateDataQualityJobDefinition",
                "sagemaker:CreateModelBiasJobDefinition",
                "sagemaker:CreateModelExplainabilityJobDefinition",
                "sagemaker:CreateModelQualityJobDefinition"
            ],
            "Resource": "arn:*:sagemaker:*:*:*",
            "Condition": {
                "Null": {
                    "sagemaker:VolumeKmsKey":"true",
                    "sagemaker:VpcSubnets": "true",
                    "sagemaker:VpcSecurityGroupIds": "true"
                }
            }
        },
        {
            "Effect": "Deny",
            "Action": [
                "sagemaker:CreateDataQualityJobDefinition",
                "sagemaker:CreateModelBiasJobDefinition",
                "sagemaker:CreateModelExplainabilityJobDefinition",
                "sagemaker:CreateModelQualityJobDefinition"
            ],
            "Resource": "arn:*:sagemaker:*:*:*",
            "Condition": {
                "Bool": {
                    "sagemaker:InterContainerTrafficEncryption": "false"
                }
            }
        },
        {
            "Effect": "Deny",
            "Action": [
                "sagemaker:CreateMonitoringSchedule",
                "sagemaker:UpdateMonitoringSchedule",
            ],
            "Resource": "arn:*:sagemaker:*:*:monitoring-schedule/*",
            "Condition": {
                "Null": {
                    "sagemaker:ModelMonitorJobDefinitionName": "true"
                }
            }
        }
    ]
}

```

The first two rules in the example, ensure that the security parameters are always set for monitoring job
definitions. The final rule requires that anyone, in your organization, creating or updating a schedule, have to
always specify the `MonitoringJobDefinitionName` field. This ensures that no one in your
organization, can set insecure values for the security parameters by specifying the
`MonitoringJobDefinition` field, when creating or updating schedules.
