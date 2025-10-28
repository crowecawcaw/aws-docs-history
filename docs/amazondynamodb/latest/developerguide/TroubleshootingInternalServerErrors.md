# Troubleshooting internal server errors in

Amazon DynamoDB

In DynamoDB, internal server errors (500 errors) indicate that the service is unable to serve
the request. These errors can occur for various reasons, such as transient network issues in the
fleet, infrastructure issues, storage node related issues, and more.

You may encounter some internal server errors during the lifecycle of your DynamoDB table. This
is expected due to the distributed nature of the service and usually shouldn't be a cause for
concern. DynamoDB automatically repairs and heals any transient issues with the
service in real time, without requiring any intervention from you. However, if you observe a
consistently high number of internal server errors on requests to your table (as seen in the [SystemErrors](metrics-dimensions.md#SystemErrors "metrics-dimensions.md#SystemErrors") metric), you should investigate further.

###### Topics

- [Investigating internal server errors](#ServerErrors-investigating "#ServerErrors-investigating")
- [Minimizing the impact from internal server errors](#ServerErrors-minimizing-impact "#ServerErrors-minimizing-impact")
- [Improving operational awareness](#ServerErrors-improving-operational-awareness "#ServerErrors-improving-operational-awareness")

## Investigating internal server errors

If you encounter internal server errors in your DynamoDB table, consider these options:

1. **Check the AWS Health Dashboard.**

To identify the issue, the first step is to check the [AWS Service Health Dashboard](https://health.aws.amazon.com/health/status "https://health.aws.amazon.com/health/status") and
your AWS Account Health Dashboard. These dashboards provide valuable information about any
service-wide issues, impacted tables, ongoing problems, and the root cause once the issue has
been resolved.

Reviewing the details in these dashboards will give you a better understanding of the
current status of the AWS services you're using and any potential problems affecting your
account. This information can help you determine the next steps to address the issue and
minimize any disruptions to your operations. 2. **Reach out to Support.**

If you observe prolonged, sustained errors in your requests, it may indicate an issue with
the service. As a general rule, if you see an overall failure rate of 1% or more over the last
15 minutes, it's an appropriate time to escalate the issue to the AWS Support team. See, [DynamoDB Service
Level Agreement](https://aws.amazon.com/dynamodb/sla/ "https://aws.amazon.com/dynamodb/sla/") to learn more.

When opening a case with the AWS Support team, provide the following details to help
expedite the troubleshooting process:

    * Impacted DDB; tables or secondary indexes
    * Time window when the errors were observed
    * DynamoDB request IDs, such as `4KBNVRGD25RG1KEO9UT4V3FQDJVV4KQNSO5AEMVJF66Q9ASUAAJG`,
     which you can find in your application logs.

Including these details in the support case will help the AWS team understand the problem
and provide a faster resolution. If you don't have the request IDs, you should still log the
case with the other available details.

## Minimizing the impact from internal server errors

If internal server errors happen when using DynamoDB, minimize the impact of these on your application,
consider the following best practices:

- Use backoffs and retries – DynamoDB's default SDK behaviors are designed to find the
  right balance for most applications in terms of back-off and retry strategy. However, you can adjust these
  settings based on your application's tolerance for downtime and performance requirements. Learn more
  about back-offs and retries to understand how you can fine-tune these retry settings.
- Use eventually consistent reads – If your application doesn't require strongly consistent reads,
  consider using eventually consistent reads. These reads are lower cost and less likely to experience
  transient issues due to internal server errors as it would be served from any of the available Storage Nodes.
  For more information, see [DynamoDB read consistency](HowItWorks.md "HowItWorks.md").

## Improving operational awareness

Maintaining high availability and reliability of your applications is crucial in today's digital landscape.
One key aspect of this is proactively monitoring for internal server errors (ISEs) in your DynamoDB tables and
global secondary indexes (GSIs). By creating CloudWatch alarms to monitor these errors, you can gain better
operational awareness and be alerted to potential issues before they impact your end-users. This approach aligns
with the Operational Excellence pillar of the AWS Well-Architected Framework, ensuring your DynamoDB workload is
optimized for performance, security, and reliability.

**Creating CloudWatch alarms**

You should have CloudWatch alarms set on your DynamoDB tables to receive notifications for consistently high numbers of
internal server errors instead of observing the metrics manually. This ties with the operational excellence pillar of
the Well-Architected framework for any workload on AWS.
See [Using the DynamoDB Well-Architected Lens to optimize your DynamoDB
workload](bp-wal.md "bp-wal.md") to learn more about Well-Architecting
your DynamoDB tables.

These alarms use custom metric math to calculate the failed request percentage for a 5-minute window. The recommended best practice
is to configure the alarm to enter the `ALARM` state when 3 consecutive data points breach the 1% threshold,
which means that overall 1% of requests fail within a 15-minute period.

The sample below is a AWS CloudFormation template that can help you create CloudWatch alarms on your table and GSI on the table.

```
AWSTemplateFormatVersion: "2010-09-09"
Description: Sample template for monitoring DynamoDB
Parameters:
 DynamoDBProvisionedTableName:
    Description: Name of DynamoDB Provisioned Table to create
    Type: String
    MinLength: 3
    MaxLength: 255
    ConstraintDescription : https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/Limits.html#limits-naming-rules
  DynamoDBSNSEmail:
    Description : Email Address subscribed to newly created SNS Topic
    Type: String
    AllowedPattern: "^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\\.[a-zA-Z0-9-.]+$"
    MinLength: 1
    MaxLength: 255

Resources:
  DynamoDBMonitoringSNSTopic:
    Type: AWS::SNS::Topic
    Properties:
      DisplayName: DynamoDB Monitoring SNS Topic
      Subscription:
        - Endpoint: !Ref DynamoDBSNSEmail
          Protocol: email
      TopicName: dynamodb-monitoring

  DynamoDBTableSystemErrorAlarm:
    Type: 'AWS::CloudWatch::Alarm'
    Properties:
      AlarmName: 'DynamoDBTableSystemErrorAlarm'
      AlarmDescription: 'Alarm when system errors exceed 1% of total number of requests for 15 minutes'
      AlarmActions:
        - !Ref DynamoDBMonitoringSNSTopic
      Metrics:
        - Id: 'e1'
          Expression: 'm1/(m1+m2+m3)'
          Label: SystemErrorsOverTotalRequests
        - Id: 'm1'
          MetricStat:
            Metric:
              Namespace: 'AWS/DynamoDB'
              MetricName: 'SystemErrors'
              Dimensions:
                - Name: 'TableName'
                  Value: !Ref DynamoDBProvisionedTableName
            Period: 300
            Stat: 'SampleCount'
            Unit: 'Count'
          ReturnData: False
        - Id: 'm2'
          MetricStat:
            Metric:
              Namespace: 'AWS/DynamoDB'
              MetricName: 'ConsumedReadCapacityUnits'
              Dimensions:
                - Name: 'TableName'
                  Value: !Ref DynamoDBProvisionedTableName
            Period: 300
            Stat: 'SampleCount'
            Unit: 'Count'
          ReturnData: False
        - Id: 'm3'
          MetricStat:
            Metric:
              Namespace: 'AWS/DynamoDB'
              MetricName: 'ConsumedWriteCapacityUnits'
              Dimensions:
                - Name: 'TableName'
                  Value: !Ref DynamoDBProvisionedTableName
            Period: 300
            Stat: 'SampleCount'
            Unit: 'Count'
          ReturnData: False
      EvaluationPeriods: 3
      Threshold: 1.0
      ComparisonOperator: 'GreaterThanThreshold'
  DynamoDBGSISystemErrorAlarm:
    Type: 'AWS::CloudWatch::Alarm'
    Properties:
      AlarmName: 'DynamoDBGSISystemErrorAlarm'
      AlarmDescription: 'Alarm when GSI system errors exceed 2% of total number of requests for 15 minutes'
      AlarmActions:
        - !Ref DynamoDBMonitoringSNSTopic
      Metrics:
        - Id: 'e1'
          Expression: 'm1/(m1+m2+m3)'
          Label: GSISystemErrorsOverTotalRequests
        - Id: 'm1'
          MetricStat:
            Metric:
              Namespace: 'AWS/DynamoDB'
              MetricName: 'SystemErrors'
              Dimensions:
                - Name: 'TableName'
                  Value: !Ref DynamoDBProvisionedTableName
                - Name: 'GlobalSecondaryIndexName'
                  Value: !Join [ '-', [!Ref DynamoDBProvisionedTableName, 'gsi1'] ]
            Period: 300
            Stat: 'SampleCount'
            Unit: 'Count'
          ReturnData: False
        - Id: 'm2'
          MetricStat:
            Metric:
              Namespace: 'AWS/DynamoDB'
              MetricName: 'ConsumedReadCapacityUnits'
              Dimensions:
                - Name: 'TableName'
                  Value: !Ref DynamoDBProvisionedTableName
                - Name: 'GlobalSecondaryIndexName'
                  Value: !Join [ '-', [!Ref DynamoDBProvisionedTableName, 'gsi1'] ]
            Period: 300
            Stat: 'SampleCount'
            Unit: 'Count'
          ReturnData: False
        - Id: 'm3'
          MetricStat:
            Metric:
              Namespace: 'AWS/DynamoDB'
              MetricName: 'ConsumedWriteCapacityUnits'
              Dimensions:
                - Name: 'TableName'
                  Value: !Ref DynamoDBProvisionedTableName
                - Name: 'GlobalSecondaryIndexName'
                  Value: !Join [ '-', [!Ref DynamoDBProvisionedTableName, 'gsi1'] ]
            Period: 300
            Stat: 'SampleCount'
            Unit: 'Count'
          ReturnData: False
      EvaluationPeriods: 3
      Threshold: 1.0
      ComparisonOperator: 'GreaterThanThreshold'
```
