# Access AWS IoT SiteWise through an interface VPC endpoint

When you create an interface endpoint, we generate endpoint-specific DNS hostnames that
you can use to communicate with AWS IoT SiteWise. The private DNS option is enabled by default. For more
information, see [Using private hosted zones](../../../vpc/latest/userguide/AmazonDNS-concepts.md#vpc-private-hosted-zones "../../../vpc/latest/userguide/AmazonDNS-concepts.md#vpc-private-hosted-zones") in the _Amazon VPC User Guide_.

_If you enable private DNS for the endpoint_, you can make API requests
to AWS IoT SiteWise through one of the following VPC endpoints.

- For the **data plane** API operations, use the following
  endpoint: Replace `region` with your
  AWS Region.

```
data.iotsitewise.`region`.amazonaws.com
```

- For the **control plane** API operations, use the
  following endpoint: Replace `region`
  with your AWS Region.

```
api.iotsitewise.`region`.amazonaws.com
```

_If you disable private DNS for the endpoint_, you must do the
following to access AWS IoT SiteWise through the endpoint:

1. Specify the VPC endpoint url in API requests.
   - For the **data plane** API operations, use the
     following endpoint url. Replace `vpc-endpoint-id` and `region` with your VPC
     endpoint ID and Region.

   ```
   `vpc-endpoint-id`.data.iotsitewise.`region`.vpce.amazonaws.com
   ```

   - For the **control plane** API operations, use the
     following endpoint url. Replace `vpc-endpoint-id` and `region` with your VPC
     endpoint ID and Region.

   ```
   `vpc-endpoint-id`.api.iotsitewise.`region`.vpce.amazonaws.com
   ```

2. Disable host prefix injection. The AWS CLI and AWS SDKs prepend the service endpoint
   with various host prefixes when you call each API operation. This feature causes the AWS CLI
   and AWS SDKs to produce URLs that are not valid for AWS IoT SiteWise when you specify a VPC
   endpoint.

###### Important

You can't disable host prefix injection in the AWS CLI or the AWS Tools for PowerShell. This means
that if you disable private DNS, then you can't use these tools to access AWS IoT SiteWise through
the VPC endpoint. Enable private DNS to use the AWS CLI or the AWS Tools for PowerShell to access
AWS IoT SiteWise through the endpoint.

For more information about how to disable host prefix injection in the AWS SDKs, see
the following documentation sections for each SDK:

    * [AWS SDK for C++](https://sdk.amazonaws.com/cpp/api/LATEST/struct_aws_1_1_client_1_1_client_configuration.html#a3579c1a2f2e1c9d54e99c59d27643499 "https://sdk.amazonaws.com/cpp/api/LATEST/struct_aws_1_1_client_1_1_client_configuration.html#a3579c1a2f2e1c9d54e99c59d27643499")
    * [AWS SDK for Go](../../../sdk-for-go/api/aws.md#Config.WithDisableEndpointHostPrefix "../../../sdk-for-go/api/aws.md#Config.WithDisableEndpointHostPrefix")
    * [AWS SDK for Go
     v2](https://pkg.go.dev/github.com/aws/aws-sdk-go-v2/config "https://pkg.go.dev/github.com/aws/aws-sdk-go-v2/config")
    * [AWS SDK for Java](../../../AWSJavaSDK/latest/javadoc/com/amazonaws/ClientConfiguration.md#setDisableHostPrefixInjection-boolean- "../../../AWSJavaSDK/latest/javadoc/com/amazonaws/ClientConfiguration.md#setDisableHostPrefixInjection-boolean-")
    * [AWS SDK for Java 2.x](https://sdk.amazonaws.com/java/api/latest/software/amazon/awssdk/core/client/config/SdkAdvancedClientOption.html "https://sdk.amazonaws.com/java/api/latest/software/amazon/awssdk/core/client/config/SdkAdvancedClientOption.html")
    * [AWS SDK for JavaScript](../../../AWSJavaScriptSDK/latest/AWS/Config.md#hostPrefixEnabled-property "../../../AWSJavaScriptSDK/latest/AWS/Config.md#hostPrefixEnabled-property")
    * [AWS SDK for .NET](../../../sdkfornet/v4/apidocs/items/Runtime/TClientConfig.md "../../../sdkfornet/v4/apidocs/items/Runtime/TClientConfig.md")
    * [AWS SDK for PHP](../../../aws-sdk-php/v3/api/class-Aws.md#___construct "../../../aws-sdk-php/v3/api/class-Aws.md#___construct")
    * [AWS SDK for Python (Boto3)](https://botocore.amazonaws.com/v1/documentation/api/latest/reference/config.html "https://botocore.amazonaws.com/v1/documentation/api/latest/reference/config.html")
    * [AWS SDK for Ruby](../../../sdk-for-ruby/v3/api/Aws/IoTSiteWise/Client.md#initialize-instance_method "../../../sdk-for-ruby/v3/api/Aws/IoTSiteWise/Client.md#initialize-instance_method")

For more information, see [Access an AWS service using an interface VPC endpoint](../../../vpc/latest/privatelink/create-interface-endpoint.md#access-service-though-endpoint "../../../vpc/latest/privatelink/create-interface-endpoint.md#access-service-though-endpoint") in the
_AWS PrivateLink Guide_.
