

# NetworkConfiguration
<a name="API_NetworkConfiguration"></a>

This structure specifies the network configuration for an Amazon ECS task.

## Contents
<a name="API_NetworkConfiguration_Contents"></a>

 ** awsvpcConfiguration **   <a name="eventbridge-Type-NetworkConfiguration-awsvpcConfiguration"></a>
Use this structure to specify the VPC subnets and security groups for the task, and whether a public IP address is to be used. This structure is relevant only for ECS tasks that use the `awsvpc` network mode.  
Type: [AwsVpcConfiguration](API_AwsVpcConfiguration.md) object  
Required: No

## See Also
<a name="API_NetworkConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/pipes-2015-10-07/NetworkConfiguration) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/pipes-2015-10-07/NetworkConfiguration) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/pipes-2015-10-07/NetworkConfiguration) 