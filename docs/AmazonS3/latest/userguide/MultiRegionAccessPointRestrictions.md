# Multi-Region Access Point restrictions and limitations

Multi-Region Access Points in Amazon S3 have the following restrictions and limitations. 


## Names and aliases


Multi-Region Access Point names must meet the following requirements:



* Must be unique within a single AWS account.
* Must begin with a number or lowercase letter.
* Must be between 3 and 50 characters long.
* Can't begin or end with a hyphen (`-`).
* Can't contain underscores (`_`), uppercase letters, or periods
 (`.`).
* Can't be edited after they are created.

Multi-Region Access Point aliases (which are different from a Multi-Region Access Point name), are automatically generated
 by Amazon S3 and can't be edited or reused. For more information about the difference between
 Multi-Region Access Point aliases and Multi-Region Access Point names and their respective naming rules, see [Rules for naming Amazon S3 Multi-Region Access Points](multi-region-access-point-naming.md "multi-region-access-point-naming.md").


## Accessing a Multi-Region Access Point


You can't access data through a Multi-Region Access Point by using gateway endpoints. However, you can access data through a Multi-Region Access Point by using interface
 endpoints. To use AWS PrivateLink, you must create VPC endpoints. For more
 information, see [Configuring a Multi-Region Access Point for use with
 AWS PrivateLink](MultiRegionAccessPointsPrivateLink.md "MultiRegionAccessPointsPrivateLink.md"). However, be aware that IPv6 isn't supported.


To use Multi-Region Access Points with Amazon CloudFront, you must configure the Multi-Region Access Point as a `Custom
 Origin` distribution type. For more information about various origin
 types, see [Using various origins with CloudFront distributions](https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/DownloadDistS3AndCustomOrigins.html "https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/DownloadDistS3AndCustomOrigins.html"). For more information about using Multi-Region Access Points with Amazon CloudFront, see 
  [Building an active-active, proximity-based application across multiple
 Regions](https://aws.amazon.com/blogs/storage/building-an-active-active-latency-based-application-across-multiple-regions/ "https://aws.amazon.com/blogs/storage/building-an-active-active-latency-based-application-across-multiple-regions/") on the *AWS Storage Blog*.


###### Note

S3 on Outposts buckets aren't supported.


## Signing AWS API requests


To sign an AWS API request, your Multi-Region Access Point must meet the following minimum requirements:


###### Note

Multi-Region Access Points don't support anonymous requests.



* Support for Transport Layer Security (TLS) version 1.2.
* Support for Signature Version 4 (SigV4A)–This version of SigV4 allows
 requests to be signed for multiple AWS Regions. This feature is useful in
 API operations that might result in data access from one of several Regions.
 When using an AWS SDK, you supply your credentials, and the requests to
 Multi-Region Access Points will use Signature Version 4A without additional configuration. Make
 sure to check your [AWS SDK
 compatibility](https://docs.aws.amazon.com/sdkref/latest/guide/feature-s3-mrap.html "https://docs.aws.amazon.com/sdkref/latest/guide/feature-s3-mrap.html") with the SigV4A algorithm. For more information
 about SigV4A, see [Signing AWS API requests](https://docs.aws.amazon.com/general/latest/gr/signing_aws_api_requests.html "https://docs.aws.amazon.com/general/latest/gr/signing_aws_api_requests.html") in the
 *AWS General Reference*.


###### Note

To use SigV4A with temporary security credentials—for example, when
 using AWS Identity and Access Management (IAM) roles—you can request the
 temporary credentials from a Regional AWS Security Token Service (AWS STS) endpoint. If you request temporary credentials from the global AWS STS
 endpoint (`sts.amazonaws.com`), then you must first set the Region
 compatibility of session tokens for the global endpoint to be valid in
 all AWS Regions. For more information, see [Managing AWS STS in an AWS Region](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_credentials_temp_enable-regions.html "https://docs.aws.amazon.com/IAM/latest/UserGuide/id_credentials_temp_enable-regions.html") in the *IAM User Guide*.

## Amazon S3 API operations



* `CopyObject` is supported as a destination only when using the Multi-Region Access Point ARN.
* The S3 Batch Operations feature isn't supported.

## AWS SDKs


Certain AWS SDKs aren't supported. To confirm which AWS SDKs are supported
 for Multi-Region Access Points, see [Compatibility
 with AWS SDKs](https://docs.aws.amazon.com/sdkref/latest/guide/feature-s3-mrap.html#s3-mrap-sdk-compat "https://docs.aws.amazon.com/sdkref/latest/guide/feature-s3-mrap.html#s3-mrap-sdk-compat").


## Service quotas


Be aware of the following service quota limitations:



* There is a maximum of 100 Multi-Region Access Points per account.
* There is a limit of 17 Regions for a single Multi-Region Access Point.

## Creating, deleting, or modifying a Multi-Region Access Point


When you create, delete, or modify an Multi-Region Access Point, be aware of the following rules and restrictions:



* After you create a Multi-Region Access Point, you can’t add, modify, or remove buckets from the
 Multi-Region Access Point configuration. To change the buckets, you must delete the entire Multi-Region Access Point and
 create a new one. If a cross-account bucket in your Multi-Region Access Point is deleted, the only way
 to reconnect this bucket is to recreate the bucket, using the same name and Region
 in that account.
* Underlying buckets (in the same account) that are used in a Multi-Region Access Point can be deleted
 only after a Multi-Region Access Point is deleted.

## Region
 support


**Control plane requests**


All control plane requests to create or maintain Multi-Region Access Points must be routed to the
 `US West (Oregon)` Region. For Multi-Region Access Point data plane requests, Regions
 don't need to be specified. 


For the Multi-Region Access Point failover control plane, requests must be routed to one of these five
 supported Regions:



* `US East (N. Virginia)`
* `US West (Oregon)`
* `Asia Pacific (Sydney)`
* `Asia Pacific (Tokyo)`
* `Europe (Ireland)`

**Regions enabled by default**


Your Multi-Region Access Point supports buckets in the following default AWS Regions (which are [enabled by default](https://docs.aws.amazon.com/accounts/latest/reference/manage-acct-regions.html "https://docs.aws.amazon.com/accounts/latest/reference/manage-acct-regions.html") in your AWS account):



* `US East (N. Virginia)`
* `US East (Ohio)`
* `US West (N. California)`
* `US West (Oregon)`
* `Asia Pacific (Mumbai)`
* `Asia Pacific (Osaka)`
* `Asia Pacific (Seoul)`
* `Asia Pacific (Singapore)`
* `Asia Pacific (Sydney)`
* `Asia Pacific (Tokyo)`
* `Canada (Central)`
* `Europe (Frankfurt)`
* `Europe (Ireland)`
* `Europe (London)`
* `Europe (Paris)`
* `Europe (Stockholm)`
* `South America (São Paulo)`

**AWS opt-in Regions**


Your Multi-Region Access Point also supports buckets in the following opt-in AWS Regions (which are
 [disabled by default](https://docs.aws.amazon.com/accounts/latest/reference/manage-acct-regions.html "https://docs.aws.amazon.com/accounts/latest/reference/manage-acct-regions.html") in your AWS account):



* `Africa (Cape Town)`
* `Asia Pacific (Hong Kong)`
* `Asia Pacific (Jakarta)`
* `Asia Pacific (Melbourne)`
* `Asia Pacific (Hyderabad)`
* `Canada West (Calgary)`
* `Europe (Zurich)`
* `Europe (Milan)`
* `Europe (Spain)`
* `Israel (Tel Aviv)`
* `Middle East (Bahrain)`
* `Middle East (UAE)`

###### Note

There are no additional costs for enabling an opt-in Region. However, creating or
 using a resource in a Multi-Region Access Point results in billing charges.


An opt-in Region must be manually enabled when configuring or creating your
 Multi-Region Access Point. For more information about opt-in Region behaviors for
 Multi-Region Access Points, see [Configuring Multi-Region Access Point opt-in Regions](ConfiguringMrapOptInRegions.md "ConfiguringMrapOptInRegions.md"). For
 information about how to enable an opt-in Region in your AWS account, see [Enable or
 disable a Region for standalone accounts](https://docs.aws.amazon.com/accounts/latest/reference/manage-acct-regions.html#manage-acct-regions-enable-standalone "https://docs.aws.amazon.com/accounts/latest/reference/manage-acct-regions.html#manage-acct-regions-enable-standalone") in the *AWS Account Management Reference Guide*.
