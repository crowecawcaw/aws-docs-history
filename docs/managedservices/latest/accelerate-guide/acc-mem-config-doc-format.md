# Accelerate Configuration profile: monitoring

Both the default configuration profile document and the customization configuration profile document follow the same structure
:

```
  {
    "<ResourceType>": {
        "<ConfigurationID>": {
            "Enabled": true,

            "Tag": {
                "Key": "...",
                "Value": "..."
            },
            "AlarmDefinition": {
                ...
            }
        },
        "<ConfigurationID>": {
            ...
        }
    },
    "<ResourceType>": {
        ...
    }
}
```

- **ResourceType**: This key must be one of the following supported strings. The configuration within this JSON object will relate
  only to the specified AWS resource type. Supported resource types:

```
AWS::EC2::Instance
AWS::EC2::Instance::Disk
AWS::RDS::DBInstance
AWS::RDS::DBCluster
AWS::Elasticsearch::Domain
AWS::OpenSearch::Domain
AWS::Redshift::Cluster
AWS::ElasticLoadBalancingV2::LoadBalancer
AWS::ElasticLoadBalancingV2::LoadBalancer::TargetGroup
AWS::ElasticLoadBalancing::LoadBalancer
AWS::FSx::FileSystem::ONTAP
AWS::FSx::FileSystem::ONTAP::Volume
AWS::FSx::FileSystem::Windows
AWS::EFS::FileSystem
AWS::EC2::NatGateway
AWS::EC2::VPNConnection
```

- **ConfigurationID**: This key must be unique in the profile, and uniquely names the following block of configuration. If two
  configuration blocks in the same **ResourceType** block have the same **ConfigurationID**, the one that appears latest in the profile
  takes effect. If you specify a **ConfigurationID** in your customization profile that is the same as one specified in the default profile, the
  configuration block defined in the customization profile takes effect.
  - **Enabled**: (optional, default=true) Specify if the configuration block will take effect. Set this to false to disable a
    configuration block. A disabled configuration block behaves as if it's not present in the profile.
  - **Tag**: Specify the tag that this alarm definition applies to. Any resource (of the appropriate resource type) that has
    this tag key and value will have a CloudWatch alarm created with the given definition. This field is a JSON object with the following fields:
    - **Key**: The key of the tag to match. Keep in mind that if you're using Resource Tagger to apply the tags to the resource,
      the key for the tag will always begin with **ams:rt:**.
    - **Value**: The value of the tag to match.

  - **AlarmDefinition**: Defines the alarm to be created. This is a JSON object whose fields are passed as is to the CloudWatch
    `PutMetricAlarm` API call (with the exception of pseudoparameters; for more information, see
    [Accelerate Configuration profile: pseudoparameter substitution](acc-mem-config-doc-sub.md "acc-mem-config-doc-sub.md")). For information about what fields are required, see the
    [PutMetricAlarm](../../../AmazonCloudWatch/latest/APIReference/API_PutMetricAlarm.md "../../../AmazonCloudWatch/latest/APIReference/API_PutMetricAlarm.md") documentation.

  OR

  **CompositeAlarmDefinition**: Defines a composite alarm to be created. When you create a composite alarm, you specify a rule
  expression for the alarm that takes into account the alarm state of other alarms that you have created. This is a JSON object whose fields are passed as-is to the
  `CloudWatchPutCompositeAlarm`. The composite alarm goes into ALARM state only if all conditions of the rule are met. The alarms specified in a
  composite alarm's rule expression can include metric alarms and other composite alarms. For information about what fields are required, see the
  [PutCompositeAlarm](../../../AmazonCloudWatch/latest/APIReference/API_PutCompositeAlarm.md "../../../AmazonCloudWatch/latest/APIReference/API_PutCompositeAlarm.md") documentation.

  Both options provide the following fields:

      - **AlarmName**: Specify the name of the alarm you want to create for the resource. This field has all of the same rules as
       specified in the
       [PutMetricAlarm](../../../AmazonCloudWatch/latest/APIReference/API_PutMetricAlarm.md "../../../AmazonCloudWatch/latest/APIReference/API_PutMetricAlarm.md") documentation; however, since the
       alarm name must be unique in a Region, the Alarm Manager has one additional requirement: you must specify the unique identifier pseudoparameter in the
       name of the alarm (otherwise, Alarm Manager appends the unique identifier of the resource to the front of the alarm name). For example, for the
       **AWS::EC2::Instance** resource type, you must specify `${EC2::InstanceId}` in the alarm name, or it's implicitly added
       at the start of the alarm name. For the list of identifiers, see [Accelerate Configuration profile: pseudoparameter substitution](acc-mem-config-doc-sub.md "acc-mem-config-doc-sub.md").


      All other fields are as specified in the
       [PutMetricAlarm](../../../AmazonCloudWatch/latest/APIReference/API_PutMetricAlarm.md "../../../AmazonCloudWatch/latest/APIReference/API_PutMetricAlarm.md") or the
       [PutCompositeAlarm](../../../AmazonCloudWatch/latest/APIReference/API_PutCompositeAlarm.md "../../../AmazonCloudWatch/latest/APIReference/API_PutCompositeAlarm.md") documentation.
      - **AlarmRule**: Specify which other alarms are to be evaluated to determine this composite alarm's state. For each alarm
       that you reference, they have to be either exist in CloudWatch or specified in Alarm Manager configuration profile in your account.

###### Important

You can specify either **AlarmDefinition** or **CompositeAlarmDefinition** in
your Alarm Manager configuration document, But they both can’t be used at the same time.

In the following example, the system creates an alarm when two specified metric alarms exceeds its threshold:

```
{
  "AWS::EC2::Instance": {
    "LinuxResourceAlarm": {
      "Enabled": true,
      "Tag": {
        "Key": "ams:rt:mylinuxinstance",
        "Value": "true"
      },
      "CompositeAlarmDefinition": {
        "AlarmName": "${EC2::InstanceId} Resource Usage High",
        "AlarmDescription": "Alarm when a linux EC2 instance is using too much CPU and too much Disk",
        "AlarmRule": "ALARM(\"${EC2::InstanceId}: Disk Usage Too High - ${EC2::Disk::UUID}\") AND ALARM(\"${EC2::InstanceId}: CPU Too High\")"
      }
    }
  }
}
```

###### Important

When Alarm Manager is not able to create or delete an alarm due to broke configuration, it sends
the notification to the **Direct-Customer-Alerts** SNS topic. This alarm is called
**AlarmDependencyError**.

We highly recommend that you have confirmed your subscription to this SNS topic. To receive messages published
to [a topic](../../../sns/latest/dg/sns-create-topic.md "../../../sns/latest/dg/sns-create-topic.md"), you must subscribe
[an endpoint](../../../sns/latest/dg/sns-create-subscribe-endpoint-to-topic.md#sns-endpoints "../../../sns/latest/dg/sns-create-subscribe-endpoint-to-topic.md#sns-endpoints")
to the topic. For details, see
[Step 1: Create a topic](../../../sns/latest/dg/sns-getting-started.md#step-create-queue "../../../sns/latest/dg/sns-getting-started.md#step-create-queue").

###### Note

When Anomaly Detection alarms are created, Alarm Manager automatically creates the required Anomaly Detection Models for the specified metrics.
When Anomaly Detection alarms are deleted, Alarm Manager doesn't delete the associated Anomaly Detection Models.

[Amazon CloudWatch limits the number of Anomaly Detection Models](../../../AmazonCloudWatch/latest/monitoring/cloudwatch_limits.md "../../../AmazonCloudWatch/latest/monitoring/cloudwatch_limits.md")
that you can have in a given AWS Region. If you exceed the model quota, then Alarm Manager doesn't create new Anomaly Detection Alarms.
You must either delete unused models, or work with your AMS partner to request a limit increase.

Many of the AMS Accelerate-provided baseline alarm definitions list the SNS topic, **MMS-Topic**, as a target. This is for use in the AMS Accelerate monitoring
service, and is the transport mechanism for your alarm notifications to get to AMS Accelerate. Do not specify **MMS-Topic** as the target for any alarms other
than those provided in the baseline (and overrides of the same), as the service ignores unknown alarms.
It **does not** result in AMS Accelerate acting on your custom alarms.
