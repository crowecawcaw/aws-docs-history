# PrivateLinkConfig

Specifies how your AWS DataSync agent connects to AWS using a
[virtual private cloud (VPC) service endpoint](choose-service-endpoint.md#choose-service-endpoint-vpc "choose-service-endpoint.md#choose-service-endpoint-vpc"). An agent that uses a VPC endpoint
isn't accessible over the public internet.

## Contents

**PrivateLinkEndpoint**

Specifies the VPC endpoint provided by [AWS PrivateLink](../../../vpc/latest/privatelink/privatelink-share-your-services.md "../../../vpc/latest/privatelink/privatelink-share-your-services.md") that your agent connects to.

Type: String

Length Constraints: Minimum length of 7. Maximum length of 15.

Pattern: `\A(25[0-5]|2[0-4]\d|[0-1]?\d?\d)(\.(25[0-5]|2[0-4]\d|[0-1]?\d?\d)){3}\z`

Required: No

**SecurityGroupArns**

Specifies the Amazon Resource Names (ARN) of the security group that provides DataSync access to your VPC endpoint. You can only specify one ARN.

Type: Array of strings

Array Members: Fixed number of 1 item.

Length Constraints: Maximum length of 128.

Pattern: `^arn:(aws|aws-cn|aws-us-gov|aws-eusc|aws-iso|aws-iso-b):ec2:[a-z\-0-9]*:[0-9]{12}:security-group/sg-[a-f0-9]+$`

Required: No

**SubnetArns**

Specifies the ARN of the subnet where your VPC endpoint is located. You can only specify
one ARN.

Type: Array of strings

Array Members: Fixed number of 1 item.

Length Constraints: Maximum length of 128.

Pattern: `^arn:(aws|aws-cn|aws-us-gov|aws-eusc|aws-iso|aws-iso-b):ec2:[a-z\-0-9]*:[0-9]{12}:subnet/subnet-[a-f0-9]+$`

Required: No

**VpcEndpointId**

Specifies the ID of the VPC endpoint that your agent connects to.

Type: String

Pattern: `^vpce-[0-9a-f]{17}$`

Required: No

## See Also

For more information about using this API in one of the language-specific AWS SDKs, see the following:

- [AWS SDK for C++](../../../goto/SdkForCpp/datasync-2018-11-09/PrivateLinkConfig.md "../../../goto/SdkForCpp/datasync-2018-11-09/PrivateLinkConfig.md")
- [AWS SDK for Java V2](../../../goto/SdkForJavaV2/datasync-2018-11-09/PrivateLinkConfig.md "../../../goto/SdkForJavaV2/datasync-2018-11-09/PrivateLinkConfig.md")
- [AWS SDK for Ruby V3](../../../goto/SdkForRubyV3/datasync-2018-11-09/PrivateLinkConfig.md "../../../goto/SdkForRubyV3/datasync-2018-11-09/PrivateLinkConfig.md")
