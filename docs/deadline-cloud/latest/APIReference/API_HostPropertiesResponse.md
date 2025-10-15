# HostPropertiesResponse

The host property details.


## Contents





**ec2InstanceArn** 


The ARN of the host EC2 instance.


Type: String


Required: No




**ec2InstanceType** 


The instance type of the host EC2 instance.


Type: String


Pattern: `[a-zA-Z0-9]+\.[a-zA-Z0-9]+`



Required: No




**hostName** 


The host name.


Type: String


Pattern: `[a-zA-Z0-9_\.\-]{0,255}`



Required: No




**ipAddresses** 


The IP address of the host.


Type: [IpAddresses](API_IpAddresses.md "API_IpAddresses.md") object


Required: No




## See Also


For more information about using this API in one of the language-specific AWS SDKs, see the following:



* [AWS SDK for C++](https://docs.aws.amazon.com/goto/SdkForCpp/deadline-2023-10-12/HostPropertiesResponse "https://docs.aws.amazon.com/goto/SdkForCpp/deadline-2023-10-12/HostPropertiesResponse")
* [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/deadline-2023-10-12/HostPropertiesResponse "https://docs.aws.amazon.com/goto/SdkForJavaV2/deadline-2023-10-12/HostPropertiesResponse")
* [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/deadline-2023-10-12/HostPropertiesResponse "https://docs.aws.amazon.com/goto/SdkForRubyV3/deadline-2023-10-12/HostPropertiesResponse")
