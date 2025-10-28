# Viewing notifications

There are different types of notifications in DevOps Guru.

###### Topics

- [New insight](#notification-new-insight "#notification-new-insight")
- [Closed insight](#notification-closed-insight "#notification-closed-insight")
- [New association](#notification-new-association "#notification-new-association")
- [New recommendation](#notification-new-recommendation "#notification-new-recommendation")
- [Severity upgraded](#notification-severity-upgraded "#notification-severity-upgraded")
- [Resource validation failure](#notification-resource-validation-failure "#notification-resource-validation-failure")
  The sections on this page show examples of each type of notification.

## New insight

Notifications for new insights contain the following information:

```
{
   "accountId":"123456789101",
   "region":"eu-west-1",
   "messageType":"NEW_INSIGHT",
   "insightId":"a1b2c3d4-5678-90ab-cdef-EXAMPLE22222",
   "insightName": "Repeated Insight: ApiGateway 5XXError Anomalous In Application CanaryCommonResources-123456789101-LogAnomaly-4",
   "insightUrl":"https://eu-west-1.console.aws.amazon.com/devops-guru/insight/reactive/a1b2c3d4-5678-90ab-cdef-EXAMPLE22222",
   "insightType":"REACTIVE",
   "insightDescription":"DevOps Guru has detected this is a repeated insight. DevOps Guru treats repeated insights as 'Low Severity'.",
   "insightSeverity":"medium",
   "startTime": 1680148920000,
   "startTimeISO": "2023-03-30T04:02:00Z",
   "anomalies":[
      {
         "id":"a1b2c3d4-5678-90ab-cdef-EXAMPLE11111",
         "startTime": 1680148800000,
         "startTimeISO": "2023-03-30T04:00:00Z",
         "openTime": 1680148920000,
         "openTimeISO": "2023-03-30T04:02:00Z",
         "sourceDetails":[
            {
               "dataSource":"CW_METRICS",
               "dataIdentifiers":{
                  "name":"ApproximateAgeOfOldestMessage",
                  "namespace":"AWS/SQS",
                  "period":"60",
                  "stat":"Maximum",
                  "unit":"None",
                  "dimensions":"{\"QueueName\":\"SampleQueue\"}"
               }
            }
         ],
         "associatedResourceArns":[
            "arn:aws:sqs:eu-west-1:123456789101:SampleQueue"
         ]
      }
   ],
   "resourceCollection":{
        "cloudFormation":{
            "stackNames":[
                "SampleApplication"
            ]
        },
   }
}
```

## Closed insight

Notifications for closed insights contain the following information:

```
{
"accountId":"123456789101",
   "region":"us-east-1",
   "messageType":"CLOSED_INSIGHT",
   "insightId":"a1b2c3d4-5678-90ab-cdef-EXAMPLE33333",
   "insightName": "DynamoDB table writes are under utilized in mock-stack",
   "insightUrl":"https://us-east-1.console.aws.amazon.com/devops-guru/insight/proactive/a1b2c3d4-5678-90ab-cdef-EXAMPLE33333",
   "insightType":"PROACTIVE",
   "insightDescription":"DynamoDB table writes are under utilized",
   "insightSeverity":"medium",
   "startTime": 1670612400000,
   "startTimeISO": "2022-12-09T19:00:00Z",
   "endTime": 1679994000000,
   "endTimeISO": "2023-03-28T09:00:00Z",
   "anomalies":[
      {
         "id":"a1b2c3d4-5678-90ab-cdef-EXAMPLEaaaaa",
         "startTime": 1665428400000,
         "startTimeISO": "2022-10-10T19:00:00Z",
         "endTime": 1679986800000,
         "endTimeISO": "2023-03-28T07:00:00Z",
         "openTime": 1670612400000,
         "openTimeISO": "2022-12-09T19:00:00Z",
         "closeTime": 1679994000000,
         "closeTimeISO": "2023-03-28T09:00:00Z",
         "description":"Empty receives while messages are available",
         "anomalyResources":[
            {
               "type":"AWS::SQS::Queue",
               "name":"SampleQueue"
            }
         ],
         "sourceDetails":[
            {
               "dataSource":"CW_METRICS",
               "dataIdentifiers":{
               "name":"NumberOfEmptyReceives",
                  "namespace":"AWS/SQS",
                  "period":"60",
                  "stat":"Sum",
                  "unit":"COUNT",
                  "dimensions":"{\"QueueName\":\"SampleQueue\"}"
               }
            }
         ],
        "associatedResourceArn": [
            "arn:aws:sqs:us-east-1:123456789101:SampleQueue"
        ]
      }
   ],
   "resourceCollection":{
        "cloudFormation":{
            "stackNames":[
                "SampleApplication"
            ]
        }
   }
}
```

## New association

Notifications for new associations contain the following information:

```
{
"accountId":"123456789101",
   "region":"eu-west-1",
   "messageType":"NEW_ASSOCIATION",
   "insightId":"a1b2c3d4-5678-90ab-cdef-EXAMPLE22222",
   "insightName": "Repeated Insight: Anomalous increase in Lambda ApigwLambdaDdbStack-22-GetOneFunction duration due to increased number of invocations",
   "insightUrl":"https://eu-west-1.console.aws.amazon.com/devops-guru/insight/reactive/a1b2c3d4-5678-90ab-cdef-EXAMPLE22222",
   "insightType":"REACTIVE",
   "insightDescription":"At March 29, 2023 22:02 GMT, Lambda function ApigwLambdaDdbStack-22-GetOneFunction had\nan increased duration anomaly possibly caused by the Lambda function invocation increase. DevOps Guru has detected this is a repeated insight. DevOps Guru treats repeated insights as 'Low Severity'.",
   "insightSeverity":"medium",
   "startTime": 1680127200000,
   "startTimeISO": "2023-03-29T22:00:00Z",
   "anomalies":[
      {
         "id":"a1b2c3d4-5678-90ab-cdef-EXAMPLE11111",
         "startTime":1672945500000,
         "startTimeISO": "2023-03-29T22:00:00Z",
         "openTime": 1680127740000,
         "openTimeISO": "2023-03-29T22:09:00Z",
         "sourceDetails":[
            {
               "dataSource":"CW_METRICS",
               "dataIdentifiers":{
               "namespace":"AWS/SQS",
                  "name":"ApproximateAgeOfOldestMessage",
                  "stat":"Maximum",
                  "unit":"None",
                  "period":"60",
                  "dimensions":"{\"QueueName\":\"SampleQueue\"}"
               }
            }
         ],
         "associatedResourceArns":[
            "arn:aws:sqs:eu-west-1:123456789101:SampleQueue"
         ]
      }
   ],
   "resourceCollection":{
        "cloudFormation":{
            "stackNames":[
                "SampleApplication"
            ]
        }
   }
}
```

## New recommendation

Notifications for new recommendations contain the following information:

```
{
   "accountId":"123456789101",
   "region":"us-east-1",
   "messageType":"NEW_RECOMMENDATION",
   "insightId":"a1b2c3d4-5678-90ab-cdef-EXAMPLE33333",
   "insightName": "Recreation of AWS SDK Service Clients",
   "insightUrl":"https://us-east-1.console.aws.amazon.com/devops-guru/insight/proactive/a1b2c3d4-5678-90ab-cdef-EXAMPLE33333",
   "insightType":"PROACTIVE",
   "insightDescription": "Usually for a given service you can create one [AWS SDK service client](https://docs.aws.amazon.com/sdk-for-java/v1/developer-guide/creating-clients.html) and reuse that client across your entire service.\n\nWhen instead you create a new AWS SDK service client for each call (e.g. for DynamoDB) it\u0027s generally a waste of CPU time.",
   "insightSeverity":"medium",
   "startTime": 1680125893576,
   "startTimeISO": "2023-03-29T21:38:13.576Z",
   "recommendations":[
      {
         "name":"Tune Availability Zones of your Lambda Function",
         "description":"Based on your configurations, we recommend that you set SampleFunction to be deployed in at least 3 Availability Zones to maintain Multi Availability Zone Redundancy.",
         "reason":"Lambda Function SampleFunction is currently only deployed to 2 unique Availability zones in a region with 7 total Availability zones.",
         "link":"https://docs.aws.amazon.com/lambda/latest/dg/configuration-vpc.html",
         "relatedAnomalies":[
            {
               "sourceDetails":{
                    "cloudWatchMetrics":null
               },
               "resources":[
                  {
                     "name":"SampleFunction",
                     "type":"AWS::Lambda::Function"
                  }
               ],
               "associatedResourceArns": [
                  "arn:aws:lambda:arn:123456789101:SampleFunction"
               ]
            }
         ]
      }
   ],
   "resourceCollection": {
        "cloudFormation": {
        "stackNames":[
            "SampleApplication"
         ]
      }
   }
}
```

## Severity upgraded

Notifications for severity upgrades contain the following information:

```
{
"accountId":"123456789101",
   "region":"eu-west-1",
   "messageType":"SEVERITY_UPGRADED",
   "insightId":"a1b2c3d4-5678-90ab-cdef-EXAMPLEbbbbb",
   "insightName": "Repeated Insight: ApiGateway 5XXError Anomalous In Application CanaryCommonResources-123456789101-LogAnomaly-11",
   "insightUrl":"https://eu-west-1.console.aws.amazon.com/devops-guru/insight/reactive/a1b2c3d4-5678-90ab-cdef-EXAMPLEbbbbb",
   "insightType":"REACTIVE",
   "insightDescription": "DevOps Guru has detected this is a repeated insight. DevOps Guru will treat future occurrences of this insight as 'Low Severity' for the next 7 days.",
   "insightSeverity":"high",
   "startTime": 1680127320000,
   "startTimeISO": "2023-03-29T22:02:00Z",
   "resourceCollection":{
        "cloudFormation":{
            "stackNames":[
                "SampleApplication"
            ]
        }
   }
}
```

## Resource validation failure

You can use AWS CloudFormation stacks and AWS tags to filter and identify the AWS resources that you want DevOps Guru to analyze.
When you choose an invalid stack or tag for DevOps Guru to identify resources with,
DevOps Guru creates a `SELECTED_RESOURCE_FILTER_VALIDATION_FAILURE` notification.
This can happen when the tag or stack name that you specify does not have resources associated with it.
To get the most out of DevOps Guru filtering methods, choose stacks and tags that have resources associated with them.

```

{
    "accountId":"123456789101",
    "region":"eu-west-1",
    "messageType":"SELECTED_RESOURCE_FILTER_VALIDATION_FAILURE",
    "ResourceFilterType": "Tags",
    "InvalidResourceNames": [
         "Devops-Guru-`tag-key`-`tag-value`"
    ],
    "awsInsightSource": "aws.devopsguru"
}

```
