# Endpoint

Amazon S3 on Outposts Access Points simplify managing data access at scale for shared datasets in S3 on Outposts. 
 S3 on Outposts uses endpoints to connect to AWS Outposts buckets so that you can perform actions within your 
 virtual private cloud (VPC). For more information, see [Accessing S3 on Outposts using VPC-only access points](../userguide/WorkingWithS3Outposts.md "../userguide/WorkingWithS3Outposts.md") in the *Amazon Simple Storage Service User Guide*.


## Contents





**AccessType** 


The type of connectivity used to access the Amazon S3 on Outposts endpoint.


Type: String


Valid Values: `Private | CustomerOwnedIp`



Required: No




**CidrBlock** 


The VPC CIDR committed by this endpoint.


Type: String


Required: No




**CreationTime** 


The time the endpoint was created.


Type: Timestamp


Required: No




**CustomerOwnedIpv4Pool** 


The ID of the customer-owned IPv4 address pool used for the endpoint.


Type: String


Pattern: `^ipv4pool-coip-([0-9a-f]{17})$`



Required: No




**EndpointArn** 


The Amazon Resource Name (ARN) of the endpoint.


Type: String


Pattern: `^arn:(aws|aws-cn|aws-us-gov|aws-iso|aws-iso-b):s3-outposts:[a-z\-0-9]*:[0-9]{12}:outpost/(op-[a-f0-9]{17}|ec2)/endpoint/[a-zA-Z0-9]{19}$`



Required: No




**FailedReason** 


The failure reason, if any, for a create or delete endpoint operation.


Type: [FailedReason](API_s3outposts_FailedReason.md "API_s3outposts_FailedReason.md") object


Required: No




**NetworkInterfaces** 


The network interface of the endpoint.


Type: Array of [NetworkInterface](API_s3outposts_NetworkInterface.md "API_s3outposts_NetworkInterface.md") objects


Required: No




**OutpostsId** 


The ID of the AWS Outposts.


Type: String


Pattern: `^(op-[a-f0-9]{17}|\d{12}|ec2)$`



Required: No




**SecurityGroupId** 


The ID of the security group used for the endpoint.


Type: String


Pattern: `^sg-([0-9a-f]{8}|[0-9a-f]{17})$`



Required: No




**Status** 


The status of the endpoint.


Type: String


Valid Values: `Pending | Available | Deleting | Create_Failed | Delete_Failed`



Required: No




**SubnetId** 


The ID of the subnet used for the endpoint.


Type: String


Pattern: `^subnet-([0-9a-f]{8}|[0-9a-f]{17})$`



Required: No




**VpcId** 


The ID of the VPC used for the endpoint.


Type: String


Required: No




## See Also


For more information about using this API in one of the language-specific AWS SDKs, see the following:



* [AWS SDK for C++](https://docs.aws.amazon.com/goto/SdkForCpp/s3outposts-2017-07-25/Endpoint "https://docs.aws.amazon.com/goto/SdkForCpp/s3outposts-2017-07-25/Endpoint")
* [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/s3outposts-2017-07-25/Endpoint "https://docs.aws.amazon.com/goto/SdkForJavaV2/s3outposts-2017-07-25/Endpoint")
* [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/s3outposts-2017-07-25/Endpoint "https://docs.aws.amazon.com/goto/SdkForRubyV3/s3outposts-2017-07-25/Endpoint")
