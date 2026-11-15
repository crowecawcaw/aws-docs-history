

# Managed Service for Apache Flink API example code
<a name="api-examples"></a>

This topic contains example request blocks for Managed Service for Apache Flink actions.

To use JSON as the input for an action with the AWS Command Line Interface (AWS CLI), save the request in a JSON file. Then pass the file name into the action using the `--cli-input-json` parameter. 

The following example demonstrates how to use a JSON file with an action.

```
$ aws kinesisanalyticsv2 start-application --cli-input-json file://start.json
```

For more information about using JSON with the AWS CLI, see [Generate CLI Skeleton and CLI Input JSON Parameters](https://docs.aws.amazon.com/cli/latest/userguide/generate-cli-skeleton.html) in the *AWS Command Line Interface User Guide*.

**Topics**
+ [AddApplicationCloudWatchLoggingOption](#api-examples-addapplicationcloudwatchloggingoption)
+ [AddApplicationInput](#api-examples-addapplicationinput)
+ [AddApplicationInputProcessingConfiguration](#api-examples-addapplicationinputprocessingconfiguration)
+ [AddApplicationOutput](#api-examples-addapplicationoutput)
+ [AddApplicationReferenceDataSource](#api-examples-addapplicationreferencedatasource)
+ [AddApplicationVpcConfiguration](#api-examples-AddApplicationVpcConfiguration)
+ [CreateApplication](#api-examples-createapplication)
+ [CreateApplicationSnapshot](#api-examples-createapplicationsnapshot)
+ [DeleteApplication](#api-examples-deleteapplication)
+ [DeleteApplicationCloudWatchLoggingOption](#api-examples-deleteapplicationcloudwatchloggingoption)
+ [DeleteApplicationInputProcessingConfiguration](#api-examples-deleteapplicationinputprocessingconfiguration)
+ [DeleteApplicationOutput](#api-examples-deleteapplicationoutput)
+ [DeleteApplicationReferenceDataSource](#api-examples-deleteapplicationreferencedatasource)
+ [CreateSnapshot](#api-examples-createsnapshot)
+ [DeleteApplicationSnapshot](#api-examples-deleteapplicationsnapshot)
+ [DeleteApplicationVpcConfiguration](#api-examples-DeleteApplicationVpcConfiguration)
+ [DeleteSnapshot](#api-examples-deletesnapshot)
+ [DescribeApplication](#api-examples-describeapplication)
+ [DescribeApplicationSnapshot](#api-examples-describeapplicationsnapshot)
+ [DescribeSnapshot](#api-examples-describesnapshot)
+ [DescribeSnapshotOperation](#api-examples-describesnapshotoperation)
+ [DiscoverInputSchema](#api-examples-discoverinputschema)
+ [ExportSnapshot](#api-examples-exportsnapshot)
+ [ImportSnapshot](#api-examples-importsnapshot)
+ [ListApplications](#api-examples-listapplications)
+ [ListApplicationSnapshots](#api-examples-listapplicationsnapshots)
+ [ListSnapshotOperations](#api-examples-listsnapshotoperations)
+ [ListSnapshots](#api-examples-listsnapshots)
+ [StartApplication](#api-examples-startapplication)
+ [StopApplication](#api-examples-stopapplication)
+ [UpdateApplication](#api-examples-updateapplication)
+ [Enhanced snapshot APIs](#api-examples-snapshot-apis)

## AddApplicationCloudWatchLoggingOption
<a name="api-examples-addapplicationcloudwatchloggingoption"></a>

The following example request code for the [AddApplicationCloudWatchLoggingOption](https://docs.aws.amazon.com/managed-service-for-apache-flink/latest/apiv2/API_AddApplicationCloudWatchLoggingOption.html) action adds an Amazon CloudWatch logging option to a Managed Service for Apache Flink application:

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
<a name="api-examples-addapplicationinput"></a>

The following example request code for the [AddApplicationInput](https://docs.aws.amazon.com/managed-service-for-apache-flink/latest/apiv2/API_AddApplicationInput.html) action adds an application input to a Managed Service for Apache Flink application:

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
<a name="api-examples-addapplicationinputprocessingconfiguration"></a>

The following example request code for the [AddApplicationInputProcessingConfiguration](https://docs.aws.amazon.com/managed-service-for-apache-flink/latest/apiv2/API_AddApplicationInputProcessingConfiguration.html) action adds an application input processing configuration to a Managed Service for Apache Flink application:

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
<a name="api-examples-addapplicationoutput"></a>

The following example request code for the [AddApplicationOutput](https://docs.aws.amazon.com/managed-service-for-apache-flink/latest/apiv2/API_AddApplicationOutput.html) action adds a Kinesis data stream as an application output to a Managed Service for Apache Flink application:

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
<a name="api-examples-addapplicationreferencedatasource"></a>

The following example request code for the [AddApplicationReferenceDataSource](https://docs.aws.amazon.com/managed-service-for-apache-flink/latest/apiv2/API_AddApplicationReferenceDataSource.html) action adds a CSV application reference data source to a Managed Service for Apache Flink application:

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
<a name="api-examples-AddApplicationVpcConfiguration"></a>

The following example request code for the [AddApplicationVpcConfiguration](https://docs.aws.amazon.com/managed-flink/latest/apiv2/API_AddApplicationVpcConfiguration.html) action adds a VPC configuration to an existing application:

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
<a name="api-examples-createapplication"></a>

The following example request code for the [CreateApplication](https://docs.aws.amazon.com/managed-service-for-apache-flink/latest/apiv2/API_CreateApplication.html) action creates a Managed Service for Apache Flink application:

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

The following JSON example request for the `CreateApplication` action creates an application in enhanced snapshot mode. Set `SnapshotMode` to `ENHANCED_SNAPSHOTS` in `ApplicationSnapshotConfiguration`. If you omit `SnapshotMode`, the application uses `APPLICATION_SNAPSHOTS_LEGACY`. Enhanced snapshot mode requires Apache Flink version 1.20 or later.

In the following example, replace `MyApplication`, the `ServiceExecutionRole` ARN, the bucket ARN, and the file key with your own values.

```
{
    "ApplicationName": "MyApplication",
    "RuntimeEnvironment": "FLINK-1_20",
    "ServiceExecutionRole": "arn:aws:iam::111122223333:role/MyApplicationServiceRole",
    "ApplicationConfiguration": {
        "ApplicationCodeConfiguration": {
            "CodeContent": {
                "S3ContentLocation": {
                    "BucketARN": "arn:aws:s3:::amzn-s3-demo-bucket",
                    "FileKey": "my-flink-app.jar"
                }
            },
            "CodeContentType": "ZIPFILE"
        },
        "ApplicationSnapshotConfiguration": {
            "SnapshotsEnabled": true,
            "SnapshotMode": "ENHANCED_SNAPSHOTS"
        }
    }
}
```

## CreateApplicationSnapshot
<a name="api-examples-createapplicationsnapshot"></a>

The following JSON example request for the [`CreateApplicationSnapshot`](https://docs.aws.amazon.com/managed-service-for-apache-flink/latest/apiv2/API_CreateApplicationSnapshot.html) action creates an application snapshot (legacy). For an application in enhanced snapshot mode, this action returns `InvalidApplicationConfigurationException`. For the response syntax, see [`CreateApplicationSnapshot`](https://docs.aws.amazon.com/managed-service-for-apache-flink/latest/apiv2/API_CreateApplicationSnapshot.html#API_CreateApplicationSnapshot_ResponseSyntax) in the *Managed Service for Apache Flink API Reference*.

```
{
   "ApplicationName": "MyApplication",
   "SnapshotName": "MySnapshot"
}
```

## DeleteApplication
<a name="api-examples-deleteapplication"></a>

The following example request code for the [DeleteApplication](https://docs.aws.amazon.com/managed-service-for-apache-flink/latest/apiv2/API_DeleteApplication.html) action deletes a Managed Service for Apache Flink application:

```
{"ApplicationName": "MyApplication",
"CreateTimestamp": 12345678912}
```

In enhanced snapshot mode, `DeleteApplication` does not delete the enhanced snapshots of the application. For more information, see [Delete an enhanced snapshot](snapshots-manage.md#snapshots-manage-delete-a-snapshot).

## DeleteApplicationCloudWatchLoggingOption
<a name="api-examples-deleteapplicationcloudwatchloggingoption"></a>

The following example request code for the [DeleteApplicationCloudWatchLoggingOption](https://docs.aws.amazon.com/managed-service-for-apache-flink/latest/apiv2/API_DeleteApplicationCloudWatchLoggingOption.html) action deletes an Amazon CloudWatch logging option from a Managed Service for Apache Flink application:

```
{
    "ApplicationName": "MyApplication",
    "CloudWatchLoggingOptionId": "3.1"
    "CurrentApplicationVersionId": 3
}
```

## DeleteApplicationInputProcessingConfiguration
<a name="api-examples-deleteapplicationinputprocessingconfiguration"></a>

The following example request code for the [DeleteApplicationInputProcessingConfiguration](https://docs.aws.amazon.com/managed-service-for-apache-flink/latest/apiv2/API_DeleteApplicationInputProcessingConfiguration.html) action removes an input processing configuration from a Managed Service for Apache Flink application:

```
{
   "ApplicationName": "MyApplication",
   "CurrentApplicationVersionId": 4,
   "InputId": "2.1"
}
```

## DeleteApplicationOutput
<a name="api-examples-deleteapplicationoutput"></a>

The following example request code for the [DeleteApplicationOutput](https://docs.aws.amazon.com/managed-service-for-apache-flink/latest/apiv2/API_DeleteApplicationOutput.html) action removes an application output from a Managed Service for Apache Flink application:

```
{
   "ApplicationName": "MyApplication",
   "CurrentApplicationVersionId": 4,
   "OutputId": "4.1"
}
```

## DeleteApplicationReferenceDataSource
<a name="api-examples-deleteapplicationreferencedatasource"></a>

The following example request code for the [DeleteApplicationReferenceDataSource](https://docs.aws.amazon.com/managed-service-for-apache-flink/latest/apiv2/API_DeleteApplicationReferenceDataSource.html) action removes an application reference data source from a Managed Service for Apache Flink application:

```
{
   "ApplicationName": "MyApplication",
   "CurrentApplicationVersionId": 5,
   "ReferenceId": "5.1"
}
```

## CreateSnapshot
<a name="api-examples-createsnapshot"></a>

The following JSON example request for the [`CreateSnapshot`](https://docs.aws.amazon.com/managed-service-for-apache-flink/latest/apiv2/API_CreateSnapshot.html) action creates an enhanced snapshot of a running application. The application must use enhanced snapshot mode.

```
{
   "ApplicationName": "MyApplication",
   "SnapshotName": "MyApplication-snapshot-1",
   "SnapshotDescription": "Before code update"
}
```

The following example shows the response:

```
{
   "SnapshotArn": "arn:aws:kinesisanalytics:aa-example-1:111122223333:snapshot/MyApplication-snapshot-1",
   "SnapshotStatus": "CREATING",
   "SnapshotOperationId": "a1B2c3D4e5F6",
   "SnapshotOperationStatus": "IN_PROGRESS"
}
```

## DeleteApplicationSnapshot
<a name="api-examples-deleteapplicationsnapshot"></a>

The following JSON example request for the [`DeleteApplicationSnapshot`](https://docs.aws.amazon.com/managed-service-for-apache-flink/latest/apiv2/API_DeleteApplicationSnapshot.html) action deletes an application snapshot (legacy). For an enhanced snapshot, use [`DeleteSnapshot`](https://docs.aws.amazon.com/managed-service-for-apache-flink/latest/apiv2/API_DeleteSnapshot.html). For the response syntax, see [`DeleteApplicationSnapshot`](https://docs.aws.amazon.com/managed-service-for-apache-flink/latest/apiv2/API_DeleteApplicationSnapshot.html#API_DeleteApplicationSnapshot_ResponseSyntax) in the *Managed Service for Apache Flink API Reference*.

```
{
   "ApplicationName": "MyApplication",
   "SnapshotCreationTimestamp": 12345678912,
   "SnapshotName": "MySnapshot"
}
```

## DeleteApplicationVpcConfiguration
<a name="api-examples-DeleteApplicationVpcConfiguration"></a>

The following example request code for the [DeleteApplicationVpcConfiguration](https://docs.aws.amazon.com/managed-flink/latest/apiv2/API_DeleteApplicationVpcConfiguration.html) action removes an existing VPC configuration from an application:

```
{
   "ApplicationName": "MyApplication",
   "CurrentApplicationVersionId": 9,
   "VpcConfigurationId": "1.1"
}
```

## DeleteSnapshot
<a name="api-examples-deletesnapshot"></a>

The following JSON example request for the [`DeleteSnapshot`](https://docs.aws.amazon.com/managed-service-for-apache-flink/latest/apiv2/API_DeleteSnapshot.html) action deletes an enhanced snapshot. Copy the `SnapshotCreationTimestamp` value from the `DescribeSnapshot` response.

```
{
   "SnapshotName": "MyApplication-snapshot-1",
   "SnapshotCreationTimestamp": 1767225600
}
```

The following example shows the response:

```
{
   "SnapshotArn": "arn:aws:kinesisanalytics:aa-example-1:111122223333:snapshot/MyApplication-snapshot-1",
   "SnapshotStatus": "DELETING",
   "SnapshotOperationId": "g7H8i9J0k1L2",
   "SnapshotOperationStatus": "IN_PROGRESS"
}
```

## DescribeApplication
<a name="api-examples-describeapplication"></a>

The following example request code for the [DescribeApplication](https://docs.aws.amazon.com/managed-service-for-apache-flink/latest/apiv2/API_DescribeApplication.html) action returns details about a Managed Service for Apache Flink application:

```
{"ApplicationName": "MyApplication"}
```

## DescribeApplicationSnapshot
<a name="api-examples-describeapplicationsnapshot"></a>

The following JSON example request for the [`DescribeApplicationSnapshot`](https://docs.aws.amazon.com/managed-service-for-apache-flink/latest/apiv2/API_DescribeApplicationSnapshot.html) action returns details about an application snapshot (legacy). For an enhanced snapshot, use [`DescribeSnapshot`](https://docs.aws.amazon.com/managed-service-for-apache-flink/latest/apiv2/API_DescribeSnapshot.html). For the response syntax, see [`DescribeApplicationSnapshot`](https://docs.aws.amazon.com/managed-service-for-apache-flink/latest/apiv2/API_DescribeApplicationSnapshot.html#API_DescribeApplicationSnapshot_ResponseSyntax) in the *Managed Service for Apache Flink API Reference*.

```
{
   "ApplicationName": "MyApplication",
   "SnapshotName": "MySnapshot"
}
```

## DescribeSnapshot
<a name="api-examples-describesnapshot"></a>

The following JSON example request for the [`DescribeSnapshot`](https://docs.aws.amazon.com/managed-service-for-apache-flink/latest/apiv2/API_DescribeSnapshot.html) action returns the details of an enhanced snapshot.

```
{
   "SnapshotName": "MyApplication-snapshot-1"
}
```

The following example shows part of the response:

```
{
   "SnapshotInfoDetails": {
      "SnapshotName": "MyApplication-snapshot-1",
      "SnapshotArn": "arn:aws:kinesisanalytics:aa-example-1:111122223333:snapshot/MyApplication-snapshot-1",
      "SnapshotStatus": "READY",
      "SnapshotCreationTimestamp": 1767225600,
      "RuntimeEnvironment": "FLINK-1_20",
      "SnapshotInitiator": "USER",
      "SnapshotInitiatorOperation": "CreateSnapshot",
      "SnapshotFormat": "CANONICAL"
   }
}
```

## DescribeSnapshotOperation
<a name="api-examples-describesnapshotoperation"></a>

The following JSON example request for the [`DescribeSnapshotOperation`](https://docs.aws.amazon.com/managed-service-for-apache-flink/latest/apiv2/API_DescribeSnapshotOperation.html) action returns the details of one operation on an enhanced snapshot.

```
{
   "SnapshotName": "MyApplication-snapshot-1",
   "SnapshotOperationId": "s9T0u1V2w3X4"
}
```

The following example shows the response for a successful export:

```
{
   "SnapshotOperationInfoDetails": {
      "SnapshotOperationId": "s9T0u1V2w3X4",
      "SnapshotOperation": "ExportSnapshot",
      "SnapshotOperationStatus": "SUCCESSFUL",
      "SnapshotArn": "arn:aws:kinesisanalytics:aa-example-1:111122223333:snapshot/MyApplication-snapshot-1",
      "StartTime": 1767229200,
      "EndTime": 1767229800
   }
}
```

## DiscoverInputSchema
<a name="api-examples-discoverinputschema"></a>

The following example request code for the [DiscoverInputSchema](https://docs.aws.amazon.com/managed-service-for-apache-flink/latest/apiv2/API_DiscoverInputSchema.html) action generates a schema from a streaming source:

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

The following example request code for the [DiscoverInputSchema](https://docs.aws.amazon.com/managed-service-for-apache-flink/latest/apiv2/API_DiscoverInputSchema.html) action generates a schema from a reference source:

```
{
   "S3Configuration": { 
      "BucketARN": "arn:aws:s3:::amzn-s3-demo-bucket",
      "FileKey": "TickerReference.csv"
   },
   "ServiceExecutionRole": "arn:aws:iam::123456789123:role/myrole"
}
```

## ExportSnapshot
<a name="api-examples-exportsnapshot"></a>

The following JSON example request for the [`ExportSnapshot`](https://docs.aws.amazon.com/managed-service-for-apache-flink/latest/apiv2/API_ExportSnapshot.html) action exports an enhanced snapshot to an Amazon S3 bucket. For the role and bucket requirements, see [Import and export enhanced snapshots](snapshots-import-export.md).

In the following example, replace the snapshot name, the role ARN, the bucket ARN, and the key prefix with your own values.

```
{
   "SnapshotName": "MyApplication-snapshot-1",
   "ExportDestinationConfiguration": {
      "DestinationType": "S3",
      "ExportRoleArn": "arn:aws:iam::111122223333:role/MSFSnapshotExportRole",
      "DestinationEncryptionConfiguration": {
         "KeyType": "AWS_OWNED_KEY"
      },
      "DestinationS3PrefixLocation": {
         "BucketARN": "arn:aws:s3:::amzn-s3-demo-bucket",
         "KeyPrefix": "exports/my-app/"
      }
   }
}
```

The following example shows the response:

```
{
   "SnapshotOperationId": "s9T0u1V2w3X4",
   "SnapshotOperationStatus": "IN_PROGRESS"
}
```

## ImportSnapshot
<a name="api-examples-importsnapshot"></a>

The following JSON example request for the [`ImportSnapshot`](https://docs.aws.amazon.com/managed-service-for-apache-flink/latest/apiv2/API_ImportSnapshot.html) action creates a new enhanced snapshot from the state files in an Amazon S3 prefix. For the file, role, and bucket requirements, see [Import and export enhanced snapshots](snapshots-import-export.md).

In the following example, replace the snapshot name, the role ARN, the bucket ARN, and the key prefix with your own values.

```
{
   "SnapshotName": "MyApplication-snapshot-imported",
   "ImportSourceConfiguration": {
      "SourceType": "S3",
      "ImportRoleArn": "arn:aws:iam::111122223333:role/MSFSnapshotImportRole",
      "SourceS3PrefixLocation": {
         "BucketARN": "arn:aws:s3:::amzn-s3-demo-bucket",
         "KeyPrefix": "imports/my-app/"
      }
   },
   "SnapshotDescription": "Imported from self-managed Apache Flink"
}
```

The following example shows the response:

```
{
   "SnapshotArn": "arn:aws:kinesisanalytics:aa-example-1:111122223333:snapshot/MyApplication-snapshot-imported",
   "SnapshotStatus": "CREATING",
   "SnapshotOperationId": "m3N4o5P6q7R8",
   "SnapshotOperationStatus": "IN_PROGRESS"
}
```

## ListApplications
<a name="api-examples-listapplications"></a>

The following example request code for the [ListApplications](https://docs.aws.amazon.com/managed-service-for-apache-flink/latest/apiv2/API_ListApplications.html) action returns a list of Managed Service for Apache Flink applications in your account:

```
{
   "ExclusiveStartApplicationName": "MyApplication",
   "Limit": 50
}
```

## ListApplicationSnapshots
<a name="api-examples-listapplicationsnapshots"></a>

The following JSON example request for the [`ListApplicationSnapshots`](https://docs.aws.amazon.com/managed-service-for-apache-flink/latest/apiv2/API_ListApplicationSnapshots.html) action returns a list of the application snapshots (legacy) of an application. For enhanced snapshots, use [`ListSnapshots`](https://docs.aws.amazon.com/managed-service-for-apache-flink/latest/apiv2/API_ListSnapshots.html). For the response syntax, see [`ListApplicationSnapshots`](https://docs.aws.amazon.com/managed-service-for-apache-flink/latest/apiv2/API_ListApplicationSnapshots.html#API_ListApplicationSnapshots_ResponseSyntax) in the *Managed Service for Apache Flink API Reference*.

```
{"ApplicationName": "MyApplication",
   "Limit": 50,
   "NextToken": "aBcDeFgHiJkLmNoPqRsTuVwXyZ0123"
}
```

## ListSnapshotOperations
<a name="api-examples-listsnapshotoperations"></a>

The following JSON example request for the [`ListSnapshotOperations`](https://docs.aws.amazon.com/managed-service-for-apache-flink/latest/apiv2/API_ListSnapshotOperations.html) action lists the failed operations of an enhanced snapshot.

```
{
   "SnapshotName": "MyApplication-snapshot-1",
   "SnapshotOperationStatus": "FAILED",
   "Limit": 50
}
```

The following example shows the response:

```
{
   "SnapshotOperationInfoList": [
      {
         "SnapshotOperationId": "y5Z6a7B8c9D0",
         "SnapshotOperation": "ExportSnapshot",
         "SnapshotOperationStatus": "FAILED",
         "StartTime": 1767232800,
         "EndTime": 1767233100
      }
   ]
}
```

## ListSnapshots
<a name="api-examples-listsnapshots"></a>

The following JSON example request for the [`ListSnapshots`](https://docs.aws.amazon.com/managed-service-for-apache-flink/latest/apiv2/API_ListSnapshots.html) action lists the first 50 enhanced snapshots in the account and Region.

```
{
   "Limit": 50
}
```

The following example shows part of the response:

```
{
   "SnapshotInfoList": [
      {
         "SnapshotName": "MyApplication-snapshot-1",
         "SnapshotArn": "arn:aws:kinesisanalytics:aa-example-1:111122223333:snapshot/MyApplication-snapshot-1",
         "SnapshotStatus": "READY",
         "SnapshotCreationTimestamp": 1767225600,
         "SnapshotInitiator": "USER",
         "SnapshotInitiatorOperation": "CreateSnapshot",
         "SourceApplicationName": "MyApplication",
         "SnapshotFormat": "CANONICAL"
      }
   ]
}
```

## StartApplication
<a name="api-examples-startapplication"></a>

The following example request code for the [StartApplication](https://docs.aws.amazon.com/managed-service-for-apache-flink/latest/apiv2/API_StartApplication.html) action starts a Managed Service for Apache Flink application, and loads the application state from the latest snapshot (if any):

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

In enhanced snapshot mode, this request restores from the newest enhanced snapshot in the `READY` status that the application created. The request does not use an application snapshot (legacy). The caller needs the `kinesisanalytics:RestoreFromSnapshot` IAM permission on that enhanced snapshot. For more information, see [Restore from the latest snapshot](snapshots-restore.md#snapshots-restore-restore-from-the-latest-snapshot) and [IAM permissions](snapshots-setup.md#snapshots-setup-iam-permissions).

The following JSON example request for the `StartApplication` action starts an application in enhanced snapshot mode from a specific enhanced snapshot. Set `ApplicationRestoreType` to `RESTORE_FROM_CUSTOM_SNAPSHOT` and identify the enhanced snapshot with `SnapshotArn`. Use `SnapshotName` for an application snapshot (legacy), and use `SnapshotArn` for an enhanced snapshot. The caller needs the `kinesisanalytics:RestoreFromSnapshot` IAM permission on the enhanced snapshot. For more information, see [IAM permissions](snapshots-setup.md#snapshots-setup-iam-permissions).

In the following example, replace `MyApplication` and the `SnapshotArn` value with your application name and the ARN of your enhanced snapshot.

```
{
    "ApplicationName": "MyApplication",
    "RunConfiguration": {
        "ApplicationRestoreConfiguration": {
            "ApplicationRestoreType": "RESTORE_FROM_CUSTOM_SNAPSHOT",
            "SnapshotArn": "arn:aws:kinesisanalytics:aa-example-1:111122223333:snapshot/MyApplication-snapshot-1"
        }
    }
}
```

## StopApplication
<a name="api-examples-stopapplication"></a>

The following example request code for the [API\_StopApplication](https://docs.aws.amazon.com/managed-service-for-apache-flink/latest/apiv2/API_StopApplication.html) action stops a Managed Service for Apache Flink application:

```
{"ApplicationName": "MyApplication"}
```

## UpdateApplication
<a name="api-examples-updateapplication"></a>

The following example request code for the [UpdateApplication](https://docs.aws.amazon.com/managed-service-for-apache-flink/latest/apiv2/API_UpdateApplication.html) action updates a Managed Service for Apache Flink application to change the location of the application code:

```
{"ApplicationName": "MyApplication",
"CurrentApplicationVersionId": 1,
"ApplicationConfigurationUpdate": { 
      "ApplicationCodeConfigurationUpdate": { 
         "CodeContentTypeUpdate": "ZIPFILE",
         "CodeContentUpdate": { 
            "S3ContentLocationUpdate": { 
               "BucketARNUpdate": "{{arn:aws:s3:::amzn-s3-demo-bucket}}",
               "FileKeyUpdate": "{{my_new_code.zip}}",
               "ObjectVersionUpdate": "2"
         }
      }
   }
}
```

The following JSON example request for the `UpdateApplication` action upgrades an existing application to enhanced snapshot mode. The request must include `SnapshotsEnabledUpdate` together with `SnapshotModeUpdate`.

**Note**  
You cannot set `SnapshotModeUpdate` back to `APPLICATION_SNAPSHOTS_LEGACY`. For more information, see [Upgrade an existing application to enhanced snapshots](snapshots-upgrade.md).  
The application must already use Apache Flink 1.20 or later. If you upgrade an application to enhanced snapshot mode in the `READY` status, the next start with `RESTORE_FROM_LATEST_SNAPSHOT` starts the application without state. To keep the state, upgrade the application to enhanced snapshot mode while it is `RUNNING`.

In the following example, replace `MyApplication` with your application name. Set `CurrentApplicationVersionId` to the current version ID from the `DescribeApplication` response.

```
{
    "ApplicationName": "MyApplication",
    "CurrentApplicationVersionId": 3,
    "ApplicationConfigurationUpdate": {
        "ApplicationSnapshotConfigurationUpdate": {
            "SnapshotsEnabledUpdate": true,
            "SnapshotModeUpdate": "ENHANCED_SNAPSHOTS"
        }
    }
}
```

The following JSON example request for the `UpdateApplication` action restores a running application in enhanced snapshot mode from a specific enhanced snapshot. The application must be in the `RUNNING` status. The caller needs `kinesisanalytics:RestoreFromSnapshot` on the enhanced snapshot.

In the following example, replace `MyApplication`, the `CurrentApplicationVersionId` value, and the `SnapshotArn` value with your own values.

```
{
    "ApplicationName": "MyApplication",
    "CurrentApplicationVersionId": 4,
    "RunConfigurationUpdate": {
        "ApplicationRestoreConfiguration": {
            "ApplicationRestoreType": "RESTORE_FROM_CUSTOM_SNAPSHOT",
            "SnapshotArn": "arn:aws:kinesisanalytics:aa-example-1:111122223333:snapshot/MyApplication-snapshot-1"
        }
    }
}
```

## Enhanced snapshot APIs
<a name="api-examples-snapshot-apis"></a>

Enhanced snapshots use different API actions than application snapshots (legacy). For sample requests and responses for these actions, see [Enhanced snapshot API examples](snapshots-api-examples.md).
+ [`CreateSnapshot`](https://docs.aws.amazon.com/managed-service-for-apache-flink/latest/apiv2/API_CreateSnapshot.html)
+ [`DescribeSnapshot`](https://docs.aws.amazon.com/managed-service-for-apache-flink/latest/apiv2/API_DescribeSnapshot.html)
+ [`ListSnapshots`](https://docs.aws.amazon.com/managed-service-for-apache-flink/latest/apiv2/API_ListSnapshots.html)
+ [`DeleteSnapshot`](https://docs.aws.amazon.com/managed-service-for-apache-flink/latest/apiv2/API_DeleteSnapshot.html)
+ [`ImportSnapshot`](https://docs.aws.amazon.com/managed-service-for-apache-flink/latest/apiv2/API_ImportSnapshot.html)
+ [`ExportSnapshot`](https://docs.aws.amazon.com/managed-service-for-apache-flink/latest/apiv2/API_ExportSnapshot.html)
+ [`DescribeSnapshotOperation`](https://docs.aws.amazon.com/managed-service-for-apache-flink/latest/apiv2/API_DescribeSnapshotOperation.html)
+ [`ListSnapshotOperations`](https://docs.aws.amazon.com/managed-service-for-apache-flink/latest/apiv2/API_ListSnapshotOperations.html)