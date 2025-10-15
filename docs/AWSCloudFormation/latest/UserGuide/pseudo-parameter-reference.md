# Get AWS values using pseudo parameters

Pseudo parameters are built-in variables that provide access to important AWS environment
 information such as account IDs, Region names, and stack details that can change between
 deployments or environments.

You can use pseudo parameters instead of hard-coded values to make your templates more
 portable and easier to reuse across different AWS accounts and Regions.


## Syntax


You can reference pseudo parameters using either the `Ref` intrinsic function
 or the `Fn::Sub` intrinsic function. 


### Ref


The `Ref` intrinsic function uses the following general syntax. For more
 information, see [Ref](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/intrinsic-function-reference-ref.html "https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/intrinsic-function-reference-ref.html").



#### JSON



```
{ "Ref" : "AWS::`PseudoParameter`" }
```



#### YAML



```
!Ref AWS::`PseudoParameter`
```


### Fn::Sub


The `Fn::Sub` intrinsic function uses a different format that includes the
 `${}` syntax around the pseudo parameter. For more information, see [Fn::Sub](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/intrinsic-function-reference-sub.html "https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/intrinsic-function-reference-sub.html").



#### JSON



```
{ "Fn::Sub" : "${AWS::`PseudoParameter`}" }
```



#### YAML



```
!Sub '${AWS::`PseudoParameter`}'
```


## Available pseudo parameters


### `AWS::AccountId`


Returns the AWS account ID of the account in which the stack is being created, such as
 `123456789012`.


This pseudo parameter is commonly used when defining IAM roles, policies, and other
 resource policies that involve account-specific ARNs.


### `AWS::NotificationARNs`


Returns the list of Amazon Resource Names (ARNs) for the Amazon SNS topics that receive stack
 event notifications. You can specify these ARNs through the `--notification-arns`
 option in the AWS CLI or through the console as you are creating or updating your
 stack.


Unlike other pseudo parameters that return a single value,
 `AWS::NotificationARNs` returns a list of ARNs. To access a specific ARN in the
 list, use the `Fn::Select` intrinsic function. For more information, see [Fn::Select](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/intrinsic-function-reference-select.html "https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/intrinsic-function-reference-select.html").


### `AWS::NoValue`


Removes the corresponding resource property when specified as a return value in the
 `Fn::If` intrinsic function. For more information, see [Fn::If](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/intrinsic-function-reference-conditions.html#intrinsic-function-reference-conditions-if "https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/intrinsic-function-reference-conditions.html#intrinsic-function-reference-conditions-if").


This pseudo parameter is particularly useful for creating conditional resource
 properties that should only be included under certain conditions.


### `AWS::Partition`


Returns the partition that the resource is in. For standard AWS Regions, the partition
 is `aws`. For resources in other partitions, the partition is
 `aws-``partitionname`. For example, the partition for
 resources in the China (Beijing and Ningxia) Regions is `aws-cn` and the
 partition for resources in the AWS GovCloud (US-West) Region is
 `aws-us-gov`.


The partition forms part of the ARN for resources. Using `AWS::Partition`
 ensures your templates work correctly across different AWS partitions.


### `AWS::Region`


Returns a string representing the Region in which the encompassing resource is being
 created, such as `us-west-2`.


This is one of the most commonly used pseudo parameters, as it allows templates to adapt
 to different AWS Regions without modification.


### `AWS::StackId`


Returns the ID (ARN) of the stack, such as
 `arn:aws:cloudformation:us-west-2:123456789012:stack/teststack/51af3dc0-da77-11e4-872e-1234567db123`.


### `AWS::StackName`


Returns the name of the stack, such as `teststack`.


The stack name is commonly used to create unique resource names that are easily
 identifiable as belonging to a specific stack.


### `AWS::URLSuffix`


Returns the suffix for the AWS domain in the AWS Region where the stack is deployed.
 The suffix is typically `amazonaws.com`, but for the China (Beijing) Region,
 the suffix is `amazonaws.com.cn`.


This parameter is particularly useful when constructing URLs for AWS service
 endpoints.


## Examples


###### Topics

* [Basic usage](#pseudo-parameter-basic-example "#pseudo-parameter-basic-example")
* [Using
 AWS::NotificationARNs](#pseudo-parameter-notification-example "#pseudo-parameter-notification-example")
* [Conditional properties with
 AWS::NoValue](#pseudo-parameter-novalue-example "#pseudo-parameter-novalue-example")

### Basic usage


The following examples create two resources: an Amazon SNS topic and a CloudWatch alarm that sends
 notifications to that topic. They use `AWS::StackName`, `AWS::Region`,
 and `AWS::AccountId` to dynamically insert the stack name, current AWS Region,
 and account ID into resource names, descriptions, and ARNs.



#### JSON



```
{
    "Resources": {
        "MyNotificationTopic": {
            "Type": "AWS::SNS::Topic",
            "Properties": {
                "DisplayName": { "Fn::Sub": "Notifications for ${AWS::StackName}" }
            }
        },
        "CPUAlarm": {
            "Type": "AWS::CloudWatch::Alarm",
            "Properties": {
                "AlarmDescription": { "Fn::Sub": "Alarm for high CPU in ${AWS::Region}" },
                "AlarmName": { "Fn::Sub": "${AWS::StackName}-HighCPUAlarm" },
                "MetricName": "CPUUtilization",
                "Namespace": "AWS/EC2",
                "Statistic": "Average",
                "Period": 300,
                "EvaluationPeriods": 1,
                "Threshold": 80,
                "ComparisonOperator": "GreaterThanThreshold",
                "AlarmActions": [{ "Fn::Sub": "arn:aws:sns:${AWS::Region}:${AWS::AccountId}:${MyNotificationTopic}" }]
            }
        }
    }
}
```



#### YAML



```
Resources:
  MyNotificationTopic:
    Type: AWS::SNS::Topic
    Properties:
      DisplayName: !Sub Notifications for ${AWS::StackName}
  CPUAlarm:
    Type: AWS::CloudWatch::Alarm
    Properties:
      AlarmDescription: !Sub Alarm for high CPU in ${AWS::Region}
      AlarmName: !Sub ${AWS::StackName}-HighCPUAlarm
      MetricName: CPUUtilization
      Namespace: AWS/EC2
      Statistic: Average
      Period: 300
      EvaluationPeriods: 1
      Threshold: 80
      ComparisonOperator: GreaterThanThreshold
      AlarmActions:
        - !Sub arn:aws:sns:${AWS::Region}:${AWS::AccountId}:${MyNotificationTopic}
```


### Using
 AWS::NotificationARNs


The following examples configure an Auto Scaling group to send notifications for instance launch
 events and launch errors. The configuration uses the `AWS::NotificationARNs`
 pseudo parameter, which provides a list of Amazon SNS topic ARNs that were specified during stack
 creation. The `Fn::Select` function chooses the first ARN from that list.



#### JSON



```
"myASG": {
   "Type": "AWS::AutoScaling::AutoScalingGroup",
   "Properties": {
      "LaunchTemplate": {
         "LaunchTemplateId": { "Ref": "myLaunchTemplate" },
         "Version": { "Fn::GetAtt": [ "myLaunchTemplate", "LatestVersionNumber" ] }
       },
       "MaxSize": "1",
       "MinSize": "1",
       "VPCZoneIdentifier": [
          "subnetIdAz1",
          "subnetIdAz2",
          "subnetIdAz3"
      ],
      "NotificationConfigurations" : [{
         "TopicARN" : { "Fn::Select" : [ "0", { "Ref" : "AWS::NotificationARNs" } ] },
         "NotificationTypes" : [ "autoscaling:EC2_INSTANCE_LAUNCH", "autoscaling:EC2_INSTANCE_LAUNCH_ERROR" ]
      }]
   }
}
```



#### YAML



```
myASG:
  Type: AWS::AutoScaling::AutoScalingGroup
  Properties:
    LaunchTemplate:
      LaunchTemplateId: !Ref myLaunchTemplate
      Version: !GetAtt myLaunchTemplate.LatestVersionNumber
    MinSize: '1'
    MaxSize: '1'
    VPCZoneIdentifier:
      - subnetIdAz1
      - subnetIdAz2
      - subnetIdAz3
    NotificationConfigurations:
      - TopicARN:
          Fn::Select:
          - '0'
          - Ref: AWS::NotificationARNs
        NotificationTypes:
        - autoscaling:EC2_INSTANCE_LAUNCH
        - autoscaling:EC2_INSTANCE_LAUNCH_ERROR
```


### Conditional properties with
 AWS::NoValue


The following examples create an Amazon RDS DB instance that uses a snapshot only if a snapshot ID is
 provided. If the `UseDBSnapshot` condition evaluates to true, CloudFormation uses the
 `DBSnapshotName` parameter value for the `DBSnapshotIdentifier`
 property. If the condition evaluates to false, CloudFormation removes the
 `DBSnapshotIdentifier` property. 



#### JSON



```
"MyDB" : {
  "Type" : "AWS::RDS::DBInstance",
  "Properties" : {
    "AllocatedStorage" : "5",
    "DBInstanceClass" : "db.t2.small",
    "Engine" : "MySQL",
    "EngineVersion" : "5.5",
    "MasterUsername" : { "Ref" : "DBUser" },
    "MasterUserPassword" : { "Ref" : "DBPassword" },
    "DBParameterGroupName" : { "Ref" : "MyRDSParamGroup" },
    "DBSnapshotIdentifier" : {
      "Fn::If" : [
        "UseDBSnapshot",
        {"Ref" : "DBSnapshotName"},
        {"Ref" : "AWS::NoValue"}
      ]
    }
  }
}
```



#### YAML



```
MyDB:
  Type: AWS::RDS::DBInstance
  Properties:
    AllocatedStorage: '5'
    DBInstanceClass: db.t2.small
    Engine: MySQL
    EngineVersion: '5.5'
    MasterUsername:
      Ref: DBUser
    MasterUserPassword:
      Ref: DBPassword
    DBParameterGroupName:
      Ref: MyRDSParamGroup
    DBSnapshotIdentifier:
      Fn::If:
        - UseDBSnapshot
        - Ref: DBSnapshotName
        - Ref: AWS::NoValue
```
