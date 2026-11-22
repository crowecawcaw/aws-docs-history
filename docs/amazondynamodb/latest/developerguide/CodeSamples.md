

# Running the code examples in this Developer Guide

The AWS SDKs provide broad support for Amazon DynamoDB in the following languages:
+ [ Java](https://aws.amazon.com/sdk-for-java)
+ [JavaScript in the browser](https://aws.amazon.com/sdk-for-browser)
+ [.NET](https://aws.amazon.com/sdk-for-net)
+ [Node.js](https://aws.amazon.com/sdk-for-node-js)
+ [PHP](https://aws.amazon.com/sdk-for-php)
+ [Python](https://aws.amazon.com/sdk-for-python)
+ [Ruby](https://aws.amazon.com/sdk-for-ruby)
+ [C\+\+](https://aws.amazon.com/sdk-for-cpp)
+ [Go](https://aws.amazon.com/sdk-for-go)
+ [Android](https://aws.amazon.com/mobile/sdk/)
+ [iOS](https://aws.amazon.com/mobile/sdk/)

The code examples in this developer guide provide more in-depth coverage of DynamoDB operations, using the following programming languages:
+ [Java code examples](CodeSamples.Java.md)
+ [.NET code examples](CodeSamples.DotNet.md)

Before you can begin with this exercise, you need to create an AWS account, get your access key and secret key, and set up the AWS Command Line Interface (AWS CLI) on your computer. For more information, see [Setting up DynamoDB (web service)](SettingUp.DynamoWebService.md).

**Note**  
To create the sample tables and data on your computer, use ExtendDB or the downloadable version of DynamoDB. Follow the AWS CLI or AWS SDK instructions in the following topics. The DynamoDB console works only with the DynamoDB web service. Point each AWS CLI command or SDK client at your local endpoint. With the AWS CLI, add the `--endpoint-url` parameter to each command. If you omit the endpoint, the command runs against the DynamoDB web service, which can incur AWS charges or change data in your AWS account. For more information, see [Connecting your application](ExtendDB.Endpoint.md) or [Setting the local endpoint](DynamoDBLocal.UsageNotes.md#DynamoDBLocal.Endpoint).