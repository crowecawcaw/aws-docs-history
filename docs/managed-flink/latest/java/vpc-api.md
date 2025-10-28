Amazon Managed Service for Apache Flink (Amazon MSF) was previously known as Amazon Kinesis Data Analytics for Apache Flink.

# Use the Managed Service for Apache Flink VPC API

Use the following Managed Service for Apache Flink API operations to manage VPCs for your application. For information on using the Managed Service for Apache Flink API, see [Managed Service for Apache Flink API example code](api-examples.md "api-examples.md").

## Create application

Use the [CreateApplication](../apiv2/API_CreateApplication.md "../apiv2/API_CreateApplication.md") action to add a VPC configuration to your application during creation.

The following example request code for the `CreateApplication` action includes a VPC configuration when the application is created:

```
{
  "ApplicationName":"MyApplication",
  "ApplicationDescription":"My-Application-Description",
  "RuntimeEnvironment":"FLINK-1_15",
  "ServiceExecutionRole":"arn:aws:iam::123456789123:role/myrole",
  "ApplicationConfiguration": {
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
    },
  `"VpcConfigurations": [
 {
 "SecurityGroupIds": [ "sg-0123456789abcdef0" ],
 "SubnetIds": [ "subnet-0123456789abcdef0" ]
 }
 ]`
  }
}
```

## AddApplicationVpcConfiguration

Use the [AddApplicationVpcConfiguration](../apiv2/API_AddApplicationVpcConfiguration.md "../apiv2/API_AddApplicationVpcConfiguration.md") action to add a VPC configuration to your application after it has been created.

The following example request code for the `AddApplicationVpcConfiguration` action adds a VPC configuration to an existing application:

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

## DeleteApplicationVpcConfiguration

Use the [DeleteApplicationVpcConfiguration](../apiv2/API_DeleteApplicationVpcConfiguration.md "../apiv2/API_DeleteApplicationVpcConfiguration.md") action to remove a VPC configuration from your application.

The following example request code for the `AddApplicationVpcConfiguration` action removes an existing VPC configuration from an application:

```
{
   "ApplicationName": "MyApplication",
   "CurrentApplicationVersionId": 9,
   "VpcConfigurationId": "1.1"
}

```

## Update application

Use the [UpdateApplication](../apiv2/API_UpdateApplication.md "../apiv2/API_UpdateApplication.md") action to update all of an application's VPC configurations at once.

The following example request code for the `UpdateApplication` action updates all of the VPC configurations for an application:

```
{
   "ApplicationConfigurationUpdate": {
      "VpcConfigurationUpdates": [
         {
            "SecurityGroupIdUpdates": [ "sg-0123456789abcdef0" ],
            "SubnetIdUpdates": [ "subnet-0123456789abcdef0" ],
            "VpcConfigurationId": "2.1"
         }
      ]
   },
   "ApplicationName": "MyApplication",
   "CurrentApplicationVersionId": 9
}

```
