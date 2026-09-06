

# Access AWS IoT SiteWise through an interface VPC endpoint
<a name="vpc-endpoint-access"></a>

When you create an interface endpoint, we generate endpoint-specific DNS hostnames that you can use to communicate with AWS IoT SiteWise. The private DNS option is enabled by default. For more information, see [Using private hosted zones](https://docs.aws.amazon.com/vpc/latest/userguide/AmazonDNS-concepts.html#vpc-private-hosted-zones) in the *Amazon VPC User Guide*.

*If you enable private DNS for the endpoint*, you can make API requests to AWS IoT SiteWise through one of the following VPC endpoints.
+ For the **data plane** API operations, use the following endpoint: Replace {{region}} with your AWS Region.

  ```
  data.iotsitewise.{{region}}.amazonaws.com
  ```
+ For the **control plane** API operations, use the following endpoint: Replace {{region}} with your AWS Region.

  ```
  api.iotsitewise.{{region}}.amazonaws.com
  ```

*If you disable private DNS for the endpoint*, you must do the following to access AWS IoT SiteWise through the endpoint:

1. Specify the VPC endpoint url in API requests.
   + For the **data plane** API operations, use the following endpoint url. Replace {{vpc-endpoint-id}} and {{region}} with your VPC endpoint ID and Region.

     ```
     {{vpc-endpoint-id}}.data.iotsitewise.{{region}}.vpce.amazonaws.com
     ```
   + For the **control plane** API operations, use the following endpoint url. Replace {{vpc-endpoint-id}} and {{region}} with your VPC endpoint ID and Region.

     ```
     {{vpc-endpoint-id}}.api.iotsitewise.{{region}}.vpce.amazonaws.com
     ```

1. Disable host prefix injection. The AWS CLI and AWS SDKs prepend the service endpoint with various host prefixes when you call each API operation. This feature causes the AWS CLI and AWS SDKs to produce URLs that are not valid for AWS IoT SiteWise when you specify a VPC endpoint.
**Important**  
You can't disable host prefix injection in the AWS CLI or the AWS Tools for PowerShell. This means that if you disable private DNS, then you can't use these tools to access AWS IoT SiteWise through the VPC endpoint. Enable private DNS to use the AWS CLI or the AWS Tools for PowerShell to access AWS IoT SiteWise through the endpoint.

   For more information about how to disable host prefix injection in the AWS SDKs, see the following documentation sections for each SDK:
   + [AWS SDK for C\+\+](https://sdk.amazonaws.com/cpp/api/LATEST/struct_aws_1_1_client_1_1_client_configuration.html#a3579c1a2f2e1c9d54e99c59d27643499)
   + [AWS SDK for Go](https://docs.aws.amazon.com/sdk-for-go/api/aws/#Config.WithDisableEndpointHostPrefix)
   + [AWS SDK for Go v2](https://pkg.go.dev/github.com/aws/aws-sdk-go-v2/config)
   + [AWS SDK for Java](https://docs.aws.amazon.com/AWSJavaSDK/latest/javadoc/com/amazonaws/ClientConfiguration.html#setDisableHostPrefixInjection-boolean-)
   + [AWS SDK for Java 2.x](https://sdk.amazonaws.com/java/api/latest/software/amazon/awssdk/core/client/config/SdkAdvancedClientOption.html)
   + [AWS SDK for JavaScript](https://docs.aws.amazon.com/AWSJavaScriptSDK/latest/AWS/Config.html#hostPrefixEnabled-property)
   + [AWS SDK for .NET](https://docs.aws.amazon.com/sdkfornet/v4/apidocs/items/Runtime/TClientConfig.html)
   + [AWS SDK for PHP](https://docs.aws.amazon.com/aws-sdk-php/v3/api/class-Aws.AwsClient.html#___construct)
   + [AWS SDK for Python (Boto3)](https://botocore.amazonaws.com/v1/documentation/api/latest/reference/config.html)
   + [AWS SDK for Ruby](https://docs.aws.amazon.com/sdk-for-ruby/v3/api/Aws/IoTSiteWise/Client.html#initialize-instance_method)

For more information, see [Access an AWS service using an interface VPC endpoint](https://docs.aws.amazon.com/vpc/latest/privatelink/create-interface-endpoint.html#access-service-though-endpoint) in the *AWS PrivateLink Guide*.