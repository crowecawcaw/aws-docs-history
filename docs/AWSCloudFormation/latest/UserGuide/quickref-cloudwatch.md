# Amazon CloudWatch template snippets

Use these sample template snippets to help describe your Amazon CloudWatch resources in AWS CloudFormation. For
more information, see the [Amazon CloudWatch resource type reference](../TemplateReference/AWS_CloudWatch.md "../TemplateReference/AWS_CloudWatch.md").

###### Topics

- [Billing alarm](#cloudwatch-sample-billing-alarm "#cloudwatch-sample-billing-alarm")
- [CPU utilization alarm](#cloudwatch-sample-cpu-utilization-alarm "#cloudwatch-sample-cpu-utilization-alarm")
- [Recover an Amazon Elastic Compute Cloud instance](#cloudwatch-sample-recover-instance "#cloudwatch-sample-recover-instance")
- [Create a basic dashboard](#cloudwatch-sample-dashboard-basic "#cloudwatch-sample-dashboard-basic")
- [Create a dashboard with side-by-side
  widgets](#cloudwatch-sample-dashboard-sidebyside "#cloudwatch-sample-dashboard-sidebyside")

## Billing alarm

In the following sample, Amazon CloudWatch sends an email notification when charges to your AWS
account exceed the alarm threshold. To receive usage notifications, enable billing alerts. For
more information, see [Create a billing alarm to monitor your estimated AWS charges](../../../AmazonCloudWatch/latest/monitoring/monitor_estimated_charges_with_cloudwatch.md "../../../AmazonCloudWatch/latest/monitoring/monitor_estimated_charges_with_cloudwatch.md") in the
_Amazon CloudWatch User Guide_.>

### JSON

```
"SpendingAlarm": {
  "Type": "AWS::CloudWatch::Alarm",
  "Properties": {
    "AlarmDescription": { "Fn::Join": ["", [
      "Alarm if AWS spending is over $",
      { "Ref": "`AlarmThreshold`" }
    ]]},
    "Namespace": "AWS/Billing",
    "MetricName": "EstimatedCharges",
    "Dimensions": [{
      "Name": "Currency",
      "Value" : "USD"
    }],
    "Statistic": "Maximum",
    "Period": "21600",
    "EvaluationPeriods": "1",
    "Threshold": { "Ref": "`AlarmThreshold`" },
    "ComparisonOperator": "GreaterThanThreshold",
    "AlarmActions": [{
      "Ref": "`BillingAlarmNotification`"
    }],
    "InsufficientDataActions": [{
      "Ref": "`BillingAlarmNotification`"
    }]
  }
}
```

### YAML

```
SpendingAlarm:
  Type: AWS::CloudWatch::Alarm
  Properties:
    AlarmDescription:
      'Fn::Join':
        - ''
        - - Alarm if AWS spending is over $
          - !Ref: AlarmThreshold
    Namespace: AWS/Billing
    MetricName: EstimatedCharges
    Dimensions:
    - Name: Currency
      Value: USD
    Statistic: Maximum
    Period: '21600'
    EvaluationPeriods: '1'
    Threshold:
      !Ref: "`AlarmThreshold`"
    ComparisonOperator: GreaterThanThreshold
    AlarmActions:
    - !Ref: "`BillingAlarmNotification`"
    InsufficientDataActions:
    - !Ref: "`BillingAlarmNotification`"
```

## CPU utilization alarm

The following sample snippet creates an alarm that sends a notification when the average
CPU utilization of an Amazon EC2 instance exceeds 90 percent for more than 60 seconds over three
evaluation periods.

### JSON

```
"CPUAlarm" : {
  "Type" : "AWS::CloudWatch::Alarm",
  "Properties" : {
    "AlarmDescription" : "CPU alarm for my instance",
    "AlarmActions" : [ { "Ref" : "`logical name of an AWS::SNS::Topic resource`" } ],
    "MetricName" : "CPUUtilization",
    "Namespace" : "AWS/EC2",
    "Statistic" : "Average",
    "Period" : "60",
    "EvaluationPeriods" : "3",
    "Threshold" : "90",
    "ComparisonOperator" : "GreaterThanThreshold",
    "Dimensions" : [ {
      "Name" : "InstanceId",
      "Value" : { "Ref" : "`logical name of an AWS::EC2::Instance resource`" }
    } ]
  }
}
```

### YAML

```
CPUAlarm:
  Type: AWS::CloudWatch::Alarm
  Properties:
    AlarmDescription: CPU alarm for my instance
    AlarmActions:
    - !Ref: "`logical name of an AWS::SNS::Topic resource`"
    MetricName: CPUUtilization
    Namespace: AWS/EC2
    Statistic: Average
    Period: '60'
    EvaluationPeriods: '3'
    Threshold: '90'
    ComparisonOperator: GreaterThanThreshold
    Dimensions:
    - Name: InstanceId
      Value: !Ref: "`logical name of an AWS::EC2::Instance resource`"
```

## Recover an Amazon Elastic Compute Cloud instance

The following CloudWatch alarm recovers an EC2 instance when it has status check failures for 15
consecutive minutes. For more information about alarm actions, see [Create alarms to stop,
terminate, reboot, or recover an EC2 instance](../../../AmazonCloudWatch/latest/monitoring/UsingAlarmActions.md "../../../AmazonCloudWatch/latest/monitoring/UsingAlarmActions.md") in the
_Amazon CloudWatch User Guide_.

### JSON

```
{
  "AWSTemplateFormatVersion": "2010-09-09",
  "Parameters" : {
    "RecoveryInstance" : {
      "Description" : "The EC2 instance ID to associate this alarm with.",
      "Type" : "AWS::EC2::Instance::Id"
    }
  },
  "Resources": {
    "RecoveryTestAlarm": {
      "Type": "AWS::CloudWatch::Alarm",
      "Properties": {
        "AlarmDescription": "Trigger a recovery when instance status check fails for 15 consecutive minutes.",
        "Namespace": "AWS/EC2" ,
        "MetricName": "StatusCheckFailed_System",
        "Statistic": "Minimum",
        "Period": "60",
        "EvaluationPeriods": "15",
        "ComparisonOperator": "GreaterThanThreshold",
        "Threshold": "0",
        "AlarmActions": [ {"Fn::Join" : ["", ["arn:aws:automate:", { "Ref" : "AWS::Region" }, ":ec2:recover" ]]} ],
        "Dimensions": [{"Name": "InstanceId","Value": {"Ref": "RecoveryInstance"}}]
      }
    }
  }
}
```

### YAML

```
AWSTemplateFormatVersion: '2010-09-09'
Parameters:
  RecoveryInstance:
    Description: The EC2 instance ID to associate this alarm with.
    Type: AWS::EC2::Instance::Id
Resources:
  RecoveryTestAlarm:
    Type: AWS::CloudWatch::Alarm
    Properties:
      AlarmDescription: Trigger a recovery when instance status check fails for 15
        consecutive minutes.
      Namespace: AWS/EC2
      MetricName: StatusCheckFailed_System
      Statistic: Minimum
      Period: '60'
      EvaluationPeriods: '15'
      ComparisonOperator: GreaterThanThreshold
      Threshold: '0'
      AlarmActions: [ !Sub "arn:aws:automate:${AWS::Region}:ec2:recover" ]
      Dimensions:
      - Name: InstanceId
        Value: !Ref: RecoveryInstance
```

## Create a basic dashboard

The following example creates a simple CloudWatch dashboard with one metric widget displaying
CPU utilization, and one text widget displaying a message.

### JSON

```
{
    "BasicDashboard": {
        "Type": "AWS::CloudWatch::Dashboard",
        "Properties": {
            "DashboardName": "Dashboard1",
            "DashboardBody": "{\"widgets\":[{\"type\":\"metric\",\"x\":0,\"y\":0,\"width\":12,\"height\":6,\"properties\":{\"metrics\":[[\"AWS/EC2\",\"CPUUtilization\",\"InstanceId\",\"`i-012345`\"]],\"period\":300,\"stat\":\"Average\",\"region\":\"us-east-1\",\"title\":\"EC2 Instance CPU\"}},{\"type\":\"text\",\"x\":0,\"y\":7,\"width\":3,\"height\":3,\"properties\":{\"markdown\":\"Hello world\"}}]}"
        }
    }
}

```

### YAML

```
BasicDashboard:
  Type: AWS::CloudWatch::Dashboard
  Properties:
    DashboardName: Dashboard1
    DashboardBody: '{"widgets":[{"type":"metric","x":0,"y":0,"width":12,"height":6,"properties":{"metrics":[["AWS/EC2","CPUUtilization","InstanceId","`i-012345`"]],"period":300,"stat":"Average","region":"us-east-1","title":"EC2 Instance CPU"}},{"type":"text","x":0,"y":7,"width":3,"height":3,"properties":{"markdown":"Hello world"}}]}'

```

## Create a dashboard with side-by-side

widgets

The following example creates a dashboard with two metric widgets that appear side by
side.

### JSON

```
{
    "DashboardSideBySide": {
        "Type": "AWS::CloudWatch::Dashboard",
        "Properties": {
            "DashboardName": "Dashboard1",
            "DashboardBody": "{\"widgets\":[{\"type\":\"metric\",\"x\":0,\"y\":0,\"width\":12,\"height\":6,\"properties\":{\"metrics\":[[\"AWS/EC2\",\"CPUUtilization\",\"InstanceId\",\"`i-012345`\"]],\"period\":300,\"stat\":\"Average\",\"region\":\"us-east-1\",\"title\":\"EC2 Instance CPU\"}},{\"type\":\"metric\",\"x\":12,\"y\":0,\"width\":12,\"height\":6,\"properties\":{\"metrics\":[[\"AWS/S3\",\"BucketSizeBytes\",\"BucketName\",\"`amzn-s3-demo-bucket`\"]],\"period\":86400,\"stat\":\"Maximum\",\"region\":\"us-east-1\",\"title\":\"`amzn-s3-demo-bucket` bytes\"}}]}"
        }
    }
}

```

### YAML

```
DashboardSideBySide:
  Type: AWS::CloudWatch::Dashboard
  Properties:
    DashboardName: Dashboard1
    DashboardBody: '{"widgets":[{"type":"metric","x":0,"y":0,"width":12,"height":6,"properties":{"metrics":[["AWS/EC2","CPUUtilization","InstanceId","`i-012345`"]],"period":300,"stat":"Average","region":"us-east-1","title":"EC2 Instance CPU"}},{"type":"metric","x":12,"y":0,"width":12,"height":6,"properties":{"metrics":[["AWS/S3","BucketSizeBytes","BucketName","`amzn-s3-demo-bucket`"]],"period":86400,"stat":"Maximum","region":"us-east-1","title":"`amzn-s3-demo-bucket` bytes"}}]}'


```
