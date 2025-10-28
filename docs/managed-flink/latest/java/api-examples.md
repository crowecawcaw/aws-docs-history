Amazon Managed Service for Apache Flink (Amazon MSF) was previously known as Amazon Kinesis Data Analytics for Apache Flink.

# Managed Service for Apache Flink API example code

This topic contains example request blocks for Managed Service for Apache Flink actions.

To use JSON as the input for an action with the AWS Command Line Interface (AWS CLI), save the request in a
JSON file. Then pass the file name into the action using the `--cli-input-json`
parameter.

The following example demonstrates how to use a JSON file with an action.

```
$ aws kinesisanalyticsv2 start-application --cli-input-json file://start.json
```

For more information about using JSON with the AWS CLI, see [Generate CLI Skeleton and CLI Input JSON
Parameters](../../../cli/latest/userguide/generate-cli-skeleton.md "../../../cli/latest/userguide/generate-cli-skeleton.md") in the _AWS Command Line Interface User Guide_.

###### Topics

- [AddApplicationCloudWatchLoggingOption](#api-examples-addapplicationcloudwatchloggingoption "#api-examples-addapplicationcloudwatchloggingoption")
- [AddApplicationInput](#api-examples-addapplicationinput "#api-examples-addapplicationinput")
- [AddApplicationInputProcessingConfiguration](#api-examples-addapplicationinputprocessingconfiguration "#api-examples-addapplicationinputprocessingconfiguration")
- [AddApplicationOutput](#api-examples-addapplicationoutput "#api-examples-addapplicationoutput")
- [AddApplicationReferenceDataSource](#api-examples-addapplicationreferencedatasource "#api-examples-addapplicationreferencedatasource")
- [AddApplicationVpcConfiguration](#api-examples-AddApplicationVpcConfiguration "#api-examples-AddApplicationVpcConfiguration")
- [CreateApplication](#api-examples-createapplication "#api-examples-createapplication")
- [CreateApplicationSnapshot](#api-examples-createapplicationsnapshot "#api-examples-createapplicationsnapshot")
- [DeleteApplication](#api-examples-deleteapplication "#api-examples-deleteapplication")
- [DeleteApplicationCloudWatchLoggingOption](#api-examples-deleteapplicationcloudwatchloggingoption "#api-examples-deleteapplicationcloudwatchloggingoption")
- [DeleteApplicationInputProcessingConfiguration](#api-examples-deleteapplicationinputprocessingconfiguration "#api-examples-deleteapplicationinputprocessingconfiguration")
- [DeleteApplicationOutput](#api-examples-deleteapplicationoutput "#api-examples-deleteapplicationoutput")
- [DeleteApplicationReferenceDataSource](#api-examples-deleteapplicationreferencedatasource "#api-examples-deleteapplicationreferencedatasource")
- [DeleteApplicationSnapshot](#api-examples-deleteapplicationsnapshot "#api-examples-deleteapplicationsnapshot")
- [DeleteApplicationVpcConfiguration](#api-examples-DeleteApplicationVpcConfiguration "#api-examples-DeleteApplicationVpcConfiguration")
- [DescribeApplication](#api-examples-describeapplication "#api-examples-describeapplication")
- [DescribeApplicationSnapshot](#api-examples-describeapplicationsnapshot "#api-examples-describeapplicationsnapshot")
- [DiscoverInputSchema](#api-examples-discoverinputschema "#api-examples-discoverinputschema")
- [ListApplications](#api-examples-listapplications "#api-examples-listapplications")
- [ListApplicationSnapshots](#api-examples-listapplicationsnapshots "#api-examples-listapplicationsnapshots")
- [StartApplication](#api-examples-startapplication "#api-examples-startapplication")
- [StopApplication](#api-examples-stopapplication "#api-examples-stopapplication")
- [UpdateApplication](#api-examples-updateapplication "#api-examples-updateapplication")

## AddApplicationCloudWatchLoggingOption

The following example request code for the
[AddApplicationCloudWatchLoggingOption](../../../managed-service-for-apache-flink/latest/apiv2/API_AddApplicationCloudWatchLoggingOption.md "../../../managed-service-for-apache-flink/latest/apiv2/API_AddApplicationCloudWatchLoggingOption.md")
action adds an Amazon CloudWatch
logging option to a Managed Service for Apache Flink application:

```
{
    "ApplicationName": "MyApplication",
    "CloudWatchLoggingOption": {
        "LogStreamARN": "arn:aws:logs:us-east-1:123456789123:log-group:my-log-group:log-stream:My-LogStream"
    },
    "CurrentApplicationVersionId": 2
}

```

## AddApplicationInput

The following example request code for the [AddApplicationInput](../../../managed-service-for-apache-flink/latest/apiv2/API_AddApplicationInput.md "../../../managed-service-for-apache-flink/latest/apiv2/API_AddApplicationInput.md")
action adds an application input to a Managed Service for Apache Flink application:

```
{
   "ApplicationName": "MyApplication",
   "CurrentApplicationVersionId": 2,
   "Input": {
      "InputParallelism": {
         "Count": 2
      },
      "InputSchema": {
         "RecordColumns": [
            {
               "Mapping": "$.TICKER",
               "Name": "TICKER_SYMBOL",
               "SqlType": "VARCHAR(50)"
            },
            {
                "SqlType": "REAL",
                "Name": "PRICE",
                "Mapping": "$.PRICE"
            }
         ],
         "RecordEncoding": "UTF-8",
         "RecordFormat": {
            "MappingParameters": {
               "JSONMappingParameters": {
                  "RecordRowPath": "$"
               }
            },
            "RecordFormatType": "JSON"
         }
      },
      "KinesisStreamsInput": {
         "ResourceARN": "arn:aws:kinesis:us-east-1:012345678901:stream/ExampleInputStream"
      }
   }
}

```

## AddApplicationInputProcessingConfiguration

The following example request code for the [AddApplicationInputProcessingConfiguration](../../../managed-service-for-apache-flink/latest/apiv2/API_AddApplicationInputProcessingConfiguration.md "../../../managed-service-for-apache-flink/latest/apiv2/API_AddApplicationInputProcessingConfiguration.md")
action adds an application input processing configuration to a Managed Service for Apache Flink application:

```
{
   "ApplicationName": "MyApplication",
   "CurrentApplicationVersionId": 2,
   "InputId": "2.1",
   "InputProcessingConfiguration": {
      "InputLambdaProcessor": {
         "ResourceARN": "arn:aws:lambda:us-east-1:012345678901:function:MyLambdaFunction"
      }
   }
}

```

## AddApplicationOutput

The following example request code for the [AddApplicationOutput](../../../managed-service-for-apache-flink/latest/apiv2/API_AddApplicationOutput.md "../../../managed-service-for-apache-flink/latest/apiv2/API_AddApplicationOutput.md")

action adds a Kinesis data stream as an application output to a Managed Service for Apache Flink application:

```
{
   "ApplicationName": "MyApplication",
   "CurrentApplicationVersionId": 2,
   "Output": {
      "DestinationSchema": {
         "RecordFormatType": "JSON"
      },
      "KinesisStreamsOutput": {
         "ResourceARN": "arn:aws:kinesis:us-east-1:012345678901:stream/ExampleOutputStream"
      },
      "Name": "DESTINATION_SQL_STREAM"
   }
}

```

## AddApplicationReferenceDataSource

The following example request code for the [AddApplicationReferenceDataSource](../../../managed-service-for-apache-flink/latest/apiv2/API_AddApplicationReferenceDataSource.md "../../../managed-service-for-apache-flink/latest/apiv2/API_AddApplicationReferenceDataSource.md")

action adds a CSV application reference data source to a Managed Service for Apache Flink application:

```
{
   "ApplicationName": "MyApplication",
   "CurrentApplicationVersionId": 5,
   "ReferenceDataSource": {
      "ReferenceSchema": {
         "RecordColumns": [
            {
               "Mapping": "$.TICKER",
               "Name": "TICKER",
               "SqlType": "VARCHAR(4)"
            },
            {
               "Mapping": "$.COMPANYNAME",
               "Name": "COMPANY_NAME",
               "SqlType": "VARCHAR(40)"
            },
         ],
         "RecordEncoding": "UTF-8",
         "RecordFormat": {
            "MappingParameters": {
               "CSVMappingParameters": {
                  "RecordColumnDelimiter": " ",
                  "RecordRowDelimiter": "\r\n"
               }
            },
            "RecordFormatType": "CSV"
         }
      },
      "S3ReferenceDataSource": {
         "BucketARN": "arn:aws:s3:::amzn-s3-demo-bucket",
         "FileKey": "TickerReference.csv"
      },
      "TableName": "string"
   }
}

```

## AddApplicationVpcConfiguration

The following example request code for the
[AddApplicationVpcConfiguration](../apiv2/API_AddApplicationVpcConfiguration.md "../apiv2/API_AddApplicationVpcConfiguration.md") action adds a VPC configuration to an existing application:

```
{
   "ApplicationName": "MyApplication",
   "CurrentApplicationVersionId": 9,
   "VpcConfiguration": {
      "SecurityGroupIds": [ "sg-0123456789abcdef0" ],
      "SubnetIds": [ "subnet-0123456789abcdef0" ]
   }
}

```

## CreateApplication

The following example request code for the [CreateApplication](../../../managed-service-for-apache-flink/latest/apiv2/API_CreateApplication.md "../../../managed-service-for-apache-flink/latest/apiv2/API_CreateApplication.md")
action creates a Managed Service for Apache Flink application:

```
{
  "ApplicationName":"MyApplication",
  "ApplicationDescription":"My-Application-Description",
  "RuntimeEnvironment":"FLINK-1_15",
  "ServiceExecutionRole":"arn:aws:iam::123456789123:role/myrole",
  "CloudWatchLoggingOptions":[
    {
      "LogStreamARN":"arn:aws:logs:us-east-1:123456789123:log-group:my-log-group:log-stream:My-LogStream"
    }
  ],
  "ApplicationConfiguration": {
    "EnvironmentProperties":
      {"PropertyGroups":
        [
          {"PropertyGroupId": "ConsumerConfigProperties",
            "PropertyMap":
              {"aws.region": "us-east-1",
              "flink.stream.initpos": "LATEST"}
          },
          {"PropertyGroupId": "ProducerConfigProperties",
            "PropertyMap":
              {"aws.region": "us-east-1"}
          },
        ]
      },
    "ApplicationCodeConfiguration":{
      "CodeContent":{
        "S3ContentLocation":{
          "BucketARN":"arn:aws:s3:::amzn-s3-demo-bucket",
          "FileKey":"myflink.jar",
          "ObjectVersion":"AbCdEfGhIjKlMnOpQrStUvWxYz12345"
        }
      },
      "CodeContentType":"ZIPFILE"
    },
      "FlinkApplicationConfiguration":{
      "ParallelismConfiguration":{
        "ConfigurationType":"CUSTOM",
        "Parallelism":2,
        "ParallelismPerKPU":1,
        "AutoScalingEnabled":true
      }
    }
  }
}

```

## CreateApplicationSnapshot

The following example request code for the
[CreateApplicationSnapshot](../../../managed-service-for-apache-flink/latest/apiv2/API_CreateApplicationSnapshot.md "../../../managed-service-for-apache-flink/latest/apiv2/API_CreateApplicationSnapshot.md")
action creates a snapshot of application state:

```
{
   "ApplicationName": "MyApplication",
   "SnapshotName": "MySnapshot"
}

```

## DeleteApplication

The following example request code for the [DeleteApplication](../../../managed-service-for-apache-flink/latest/apiv2/API_DeleteApplication.md "../../../managed-service-for-apache-flink/latest/apiv2/API_DeleteApplication.md")
action deletes a Managed Service for Apache Flink application:

```
{"ApplicationName": "MyApplication",
"CreateTimestamp": 12345678912}

```

## DeleteApplicationCloudWatchLoggingOption

The following example request code for the [DeleteApplicationCloudWatchLoggingOption](../../../managed-service-for-apache-flink/latest/apiv2/API_DeleteApplicationCloudWatchLoggingOption.md "../../../managed-service-for-apache-flink/latest/apiv2/API_DeleteApplicationCloudWatchLoggingOption.md")
action deletes an Amazon CloudWatch
logging option from a Managed Service for Apache Flink application:

```
{
    "ApplicationName": "MyApplication",
    "CloudWatchLoggingOptionId": "3.1"
    "CurrentApplicationVersionId": 3
}

```

## DeleteApplicationInputProcessingConfiguration

The following example request code for the [DeleteApplicationInputProcessingConfiguration](../../../managed-service-for-apache-flink/latest/apiv2/API_DeleteApplicationInputProcessingConfiguration.md "../../../managed-service-for-apache-flink/latest/apiv2/API_DeleteApplicationInputProcessingConfiguration.md")

action removes an input processing configuration from a Managed Service for Apache Flink application:

```
{
   "ApplicationName": "MyApplication",
   "CurrentApplicationVersionId": 4,
   "InputId": "2.1"
}

```

## DeleteApplicationOutput

The following example request code for the [DeleteApplicationOutput](../../../managed-service-for-apache-flink/latest/apiv2/API_DeleteApplicationOutput.md "../../../managed-service-for-apache-flink/latest/apiv2/API_DeleteApplicationOutput.md")

action removes an application output from a Managed Service for Apache Flink application:

```
{
   "ApplicationName": "MyApplication",
   "CurrentApplicationVersionId": 4,
   "OutputId": "4.1"
}

```

## DeleteApplicationReferenceDataSource

The following example request code for the [DeleteApplicationReferenceDataSource](../../../managed-service-for-apache-flink/latest/apiv2/API_DeleteApplicationReferenceDataSource.md "../../../managed-service-for-apache-flink/latest/apiv2/API_DeleteApplicationReferenceDataSource.md")

action removes an application reference data source from a Managed Service for Apache Flink application:

```
{
   "ApplicationName": "MyApplication",
   "CurrentApplicationVersionId": 5,
   "ReferenceId": "5.1"
}

```

## DeleteApplicationSnapshot

The following example request code for the [DeleteApplicationSnapshot](../../../managed-service-for-apache-flink/latest/apiv2/API_DeleteApplicationSnapshot.md "../../../managed-service-for-apache-flink/latest/apiv2/API_DeleteApplicationSnapshot.md")
action deletes a snapshot of application state:

```
{
   "ApplicationName": "MyApplication",
   "SnapshotCreationTimestamp": 12345678912,
   "SnapshotName": "MySnapshot"
}

```

## DeleteApplicationVpcConfiguration

The following example request code for the [DeleteApplicationVpcConfiguration](../apiv2/API_DeleteApplicationVpcConfiguration.md "../apiv2/API_DeleteApplicationVpcConfiguration.md") action removes an existing VPC configuration from an application:

```
{
   "ApplicationName": "MyApplication",
   "CurrentApplicationVersionId": 9,
   "VpcConfigurationId": "1.1"
}

```

## DescribeApplication

The following example request code for the [DescribeApplication](../../../managed-service-for-apache-flink/latest/apiv2/API_DescribeApplication.md "../../../managed-service-for-apache-flink/latest/apiv2/API_DescribeApplication.md")

action returns details about a Managed Service for Apache Flink application:

```
{"ApplicationName": "MyApplication"}

```

## DescribeApplicationSnapshot

The following example request code for the [DescribeApplicationSnapshot](../../../managed-service-for-apache-flink/latest/apiv2/API_DescribeApplicationSnapshot.md "../../../managed-service-for-apache-flink/latest/apiv2/API_DescribeApplicationSnapshot.md")

action returns details about a snapshot of application state:

```
{
   "ApplicationName": "MyApplication",
   "SnapshotName": "MySnapshot"
}

```

## DiscoverInputSchema

The following example request code for the [DiscoverInputSchema](../../../managed-service-for-apache-flink/latest/apiv2/API_DiscoverInputSchema.md "../../../managed-service-for-apache-flink/latest/apiv2/API_DiscoverInputSchema.md")

action generates a schema from a streaming source:

```
{
   "InputProcessingConfiguration": {
      "InputLambdaProcessor": {
         "ResourceARN": "arn:aws:lambda:us-east-1:012345678901:function:MyLambdaFunction"
      }
   },
   "InputStartingPositionConfiguration": {
      "InputStartingPosition": "NOW"
   },
   "ResourceARN": "arn:aws:kinesis:us-east-1:012345678901:stream/ExampleInputStream",
   "S3Configuration": {
      "BucketARN": "string",
      "FileKey": "string"
   },
   "ServiceExecutionRole": "string"
}

```

The following example request code for the [DiscoverInputSchema](../../../managed-service-for-apache-flink/latest/apiv2/API_DiscoverInputSchema.md "../../../managed-service-for-apache-flink/latest/apiv2/API_DiscoverInputSchema.md")

action generates a schema from a reference source:

```
{
   "S3Configuration": {
      "BucketARN": "arn:aws:s3:::amzn-s3-demo-bucket",
      "FileKey": "TickerReference.csv"
   },
   "ServiceExecutionRole": "arn:aws:iam::123456789123:role/myrole"
}

```

## ListApplications

The following example request code for the [ListApplications](../../../managed-service-for-apache-flink/latest/apiv2/API_ListApplications.md "../../../managed-service-for-apache-flink/latest/apiv2/API_ListApplications.md")
action returns a list of Managed Service for Apache Flink applications in your account:

```
{
   "ExclusiveStartApplicationName": "MyApplication",
   "Limit": 50
}

```

## ListApplicationSnapshots

The following example request code for the [ListApplicationSnapshots](../../../managed-service-for-apache-flink/latest/apiv2/API_ListApplicationSnapshots.md "../../../managed-service-for-apache-flink/latest/apiv2/API_ListApplicationSnapshots.md")

action returns a list of snapshots of application state:

```
{"ApplicationName": "MyApplication",
   "Limit": 50,
   "NextToken": "aBcDeFgHiJkLmNoPqRsTuVwXyZ0123"
}

```

## StartApplication

The following example request code for the [StartApplication](../../../managed-service-for-apache-flink/latest/apiv2/API_StartApplication.md "../../../managed-service-for-apache-flink/latest/apiv2/API_StartApplication.md")

action starts a Managed Service for Apache Flink application, and loads the application state from the latest
snapshot (if any):

```
{
    "ApplicationName": "MyApplication",
    "RunConfiguration": {
        "ApplicationRestoreConfiguration": {
         "ApplicationRestoreType": "RESTORE_FROM_LATEST_SNAPSHOT"
         }
    }
}

```

## StopApplication

The following example request code for the
[API_StopApplication](../../../managed-service-for-apache-flink/latest/apiv2/API_StopApplication.md "../../../managed-service-for-apache-flink/latest/apiv2/API_StopApplication.md")
action stops a Managed Service for Apache Flink application:

```
{"ApplicationName": "MyApplication"}

```

## UpdateApplication

The following example request code for the [UpdateApplication](../../../managed-service-for-apache-flink/latest/apiv2/API_UpdateApplication.md "../../../managed-service-for-apache-flink/latest/apiv2/API_UpdateApplication.md")
action updates a Managed Service for Apache Flink application to change the location
of the application code:

```
{"ApplicationName": "MyApplication",
"CurrentApplicationVersionId": 1,
"ApplicationConfigurationUpdate": {
      "ApplicationCodeConfigurationUpdate": {
         "CodeContentTypeUpdate": "ZIPFILE",
         "CodeContentUpdate": {
            "S3ContentLocationUpdate": {
               "BucketARNUpdate": "`arn:aws:s3:::amzn-s3-demo-bucket`",
               "FileKeyUpdate": "`my_new_code.zip`",
               "ObjectVersionUpdate": "2"
         }
      }
   }
}

```
