

# Accessing AWS services with temporary credentials
<a name="accessing-aws-services"></a>

The result of a successful authentication with an identity pool is a set of AWS credentials. With these credentials, your application can make requests to AWS resources that are protected with IAM authentication. With the various AWS SDKs that you can add to your applications to access identity pools API operations, you can make unauthenticated API requests that produce temporary credentials. Then you can add SDKs for other AWS services to your client and sign requests with those temporary credentials. The IAM permissions granted to your temporary-credentials role must permit the operations that you request from other services.

After you configure your Amazon Cognito credentials provider and retrieve AWS credentials, create an AWS service client. The following are some examples from AWS SDK documentation.

**AWS SDK resources for creating a client**
+ [AWS Client configuration](https://docs.aws.amazon.com/sdk-for-cpp/v1/developer-guide/client-config.html) in the AWS SDK for C\+\+ Developer Guide
+ [Using the AWS SDK for Go V2 with AWS services](https://aws.github.io/aws-sdk-go-v2/docs/making-requests/) in the AWS SDK for Go Developer Guide
+ [Configuring HTTP clients](https://docs.aws.amazon.com/sdk-for-java/latest/developer-guide/http-configuration.html) in the AWS SDK for Java 2.x Developer Guide
+ [Creating and calling service objects](https://docs.aws.amazon.com/sdk-for-javascript/v3/developer-guide/creating-and-calling-service-objects.html) in the AWS SDK for JavaScript Developer Guide
+ [Creating clients](https://boto3.amazonaws.com/v1/documentation/api/latest/guide/clients.html#creating-clients) in the AWS SDK for Python (Boto3) documentation
+ [Creating a service client](https://docs.aws.amazon.com/sdk-for-rust/latest/dg/client.html) in the AWS SDK for Rust Developer Guide
+ [Using clients](https://docs.aws.amazon.com/sdk-for-swift/latest/developer-guide/using-client-services.html) in the AWS SDK for Swift Developer Guide

The following snippet initializes an Amazon DynamoDB client: 

## Android
<a name="accessing-aws-services-1.android"></a>

To use a Amazon Cognito identity pool in an Android app, set up AWS Amplify. For more information, see [Authentication](https://docs.amplify.aws/lib/auth/getting-started/q/platform/android/) in the *Amplify Dev Center*.

```
// Create a service client with the provider
AmazonDynamoDB client = new AmazonDynamoDBClient(credentialsProvider);
```

 The credentials provider communicates with Amazon Cognito, retrieving both the unique identifier for authenticated and unauthenticated users as well as temporary, limited privilege AWS credentials for the AWS Mobile SDK. The retrieved credentials are valid for one hour, and the provider refreshes them when they expire. 

## iOS - Objective-C
<a name="accessing-aws-services-1.ios-objc"></a>

To use a Amazon Cognito identity pool in an iOS app, set up AWS Amplify. For more information, see [Swift Authentication](https://docs.amplify.aws/lib/auth/getting-started/q/platform/ios/) and [Flutter Authentication](https://docs.amplify.aws/lib/auth/getting-started/q/platform/flutter/) in the *Amplify Dev Center*.

```
// create a configuration that uses the provider
AWSServiceConfiguration *configuration = [AWSServiceConfiguration configurationWithRegion:AWSRegionUSEast1 provider:credentialsProvider];
// get a client with the default service configuration
AWSDynamoDB *dynamoDB = [AWSDynamoDB defaultDynamoDB];
```

 The credentials provider communicates with Amazon Cognito, retrieving both the unique identifier for authenticated and unauthenticated users as well as temporary, limited privilege AWS credentials for the AWS Mobile SDK. The retrieved credentials are valid for one hour, and the provider refreshes them when they expire. 

## iOS - Swift
<a name="accessing-aws-services-1.ios-swift"></a>

To use a Amazon Cognito identity pool in an iOS app, set up AWS Amplify. For more information, see [Swift Authentication](https://docs.amplify.aws/lib/auth/getting-started/q/platform/ios/) in the *Amplify Dev Center*.

```
// get a client with the default service configuration
let dynamoDB = AWSDynamoDB.default()

// get a client with a custom configuration
AWSDynamoDB.register(with: configuration!, forKey: "USWest2DynamoDB");
let dynamoDBCustom = AWSDynamoDB(forKey: "USWest2DynamoDB")
```

The credentials provider communicates with Amazon Cognito, retrieving both the unique identifier for authenticated and unauthenticated users as well as temporary, limited privilege AWS credentials for the AWS Mobile SDK. The retrieved credentials are valid for one hour, and the provider refreshes them when they expire. 

## JavaScript
<a name="accessing-aws-services-1.javascript"></a>



```
// Create a service client with the provider
var dynamodb = new AWS.DynamoDB({region: 'us-west-2'});
```

 The credentials provider communicates with Amazon Cognito, retrieving both the unique identifier for authenticated and unauthenticated users as well as temporary, limited-privilege AWS credentials for the AWS Mobile SDK. The retrieved credentials are valid for one hour, and the provider refreshes them when they expire. 

## Unity
<a name="accessing-aws-services-1.unity"></a>

The [AWS SDK for Unity](https://docs.aws.amazon.com/mobile/sdkforunity/developerguide/what-is-unity-plugin.html) is now part of the [SDK for .NET](https://docs.aws.amazon.com/sdk-for-net/v3/developer-guide/welcome.html). To get started with Amazon Cognito in the SDK for .NET, see [Amazon Cognito credentials provider](https://docs.aws.amazon.com/sdk-for-net/v3/developer-guide/cognito-creds-provider.html) in the AWS SDK for .NET Developer Guide. Or see [Amplify Dev Center](https://docs.amplify.aws/) for options for building an app with AWS Amplify.

```
// create a service client that uses credentials provided by Cognito
AmazonDynamoDBClient client = new AmazonDynamoDBClient(credentials, REGION);
```

 The credentials provider communicates with Amazon Cognito, retrieving both the unique identifier for authenticated and unauthenticated users as well as temporary, limited-privilege AWS credentials for the AWS Mobile SDK. The retrieved credentials are valid for one hour, and the provider refreshes them when they expire. 

## Xamarin
<a name="accessing-aws-services-1.xamarin"></a>

The [AWS SDK for Xamarin](https://docs.aws.amazon.com/mobile/sdkforxamarin/developerguide/Welcome.html) is now part of the [SDK for .NET](https://docs.aws.amazon.com/sdk-for-net/v3/developer-guide/welcome.html). To get started with Amazon Cognito in the SDK for .NET, see [Amazon Cognito credentials provider](https://docs.aws.amazon.com/sdk-for-net/v3/developer-guide/cognito-creds-provider.html) in the AWS SDK for .NET Developer Guide. Or see [Amplify Dev Center](https://docs.amplify.aws/) for options for building an app with AWS Amplify.

```
// create a service client that uses credentials provided by Cognito
var client = new AmazonDynamoDBClient(credentials, REGION)
```

 The credentials provider communicates with Amazon Cognito, retrieving both the unique identifier for authenticated and unauthenticated users as well as temporary, limited-privilege AWS credentials for the AWS Mobile SDK. The retrieved credentials are valid for one hour, and the provider refreshes them when they expire. 