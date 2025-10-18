# DnsConfiguration

The DNS configuration for your domain names.


## Contents





**Domain** 


The domain name that you're verifying.


Type: String


Required: Yes




**Status** 


The status of your domain name.



* `valid-configuration`: The domain name is correctly configured and points to the correct routing endpoint of the connection group.
* `invalid-configuration`: There is either a missing DNS record or the DNS record exists but it's using an incorrect routing endpoint. Update the DNS record to point to the correct routing endpoint.
* `unknown-configuration`: CloudFront can't validate your DNS configuration. This status can appear if CloudFront can't verify the DNS record, or the DNS lookup request failed or timed out.

Type: String


Valid Values: `valid-configuration | invalid-configuration | unknown-configuration`



Required: Yes




**Reason** 


Explains the status of the DNS configuration.


Type: String


Required: No




## See Also


For more information about using this API in one of the language-specific AWS SDKs, see the following:



* [AWS SDK for C++](https://docs.aws.amazon.com/goto/SdkForCpp/cloudfront-2020-05-31/DnsConfiguration "https://docs.aws.amazon.com/goto/SdkForCpp/cloudfront-2020-05-31/DnsConfiguration")
* [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/cloudfront-2020-05-31/DnsConfiguration "https://docs.aws.amazon.com/goto/SdkForJavaV2/cloudfront-2020-05-31/DnsConfiguration")
* [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/cloudfront-2020-05-31/DnsConfiguration "https://docs.aws.amazon.com/goto/SdkForRubyV3/cloudfront-2020-05-31/DnsConfiguration")
