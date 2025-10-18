# Restrictions on
 CloudFront Functions

The following restrictions apply only to CloudFront Functions.

###### Contents

* [Logs](cloudfront-function-restrictions.md#cloudfront-function-restrictions-logs "cloudfront-function-restrictions.md#cloudfront-function-restrictions-logs")
* [Request body](cloudfront-function-restrictions.md#cloudfront-function-restrictions-request-body "cloudfront-function-restrictions.md#cloudfront-function-restrictions-request-body")
* [Using temporary credentials
 with the CloudFront KeyValueStore API](cloudfront-function-restrictions.md#regional-endpoint-for-key-value-store "cloudfront-function-restrictions.md#regional-endpoint-for-key-value-store")
* [Runtime](cloudfront-function-restrictions.md#cloudfront-function-runtime-restrictions "cloudfront-function-restrictions.md#cloudfront-function-runtime-restrictions")
* [Compute
 utilization](cloudfront-function-restrictions.md#cloudfront-function-restrictions-compute-utilization "cloudfront-function-restrictions.md#cloudfront-function-restrictions-compute-utilization")
For information about quotas (formerly referred to as limits), see [Quotas on CloudFront Functions](cloudfront-limits.md#limits-functions "cloudfront-limits.md#limits-functions").


## Logs


Function logs in CloudFront Functions are truncated at 10 KB.


## Request body


CloudFront Functions can't access the body of the HTTP request.


## Using temporary credentials
 with the CloudFront KeyValueStore API


You can use AWS Security Token Service (AWS STS) to generate temporary security credentials (also
 known as *session tokens*). Session tokens allow you to
 temporarily assume an AWS Identity and Access Management (IAM) role so that you can access
 AWS services.


To call the [CloudFront KeyValueStore API](../../../cloudfront/latest/APIReference/API_Operations_Amazon_CloudFront_KeyValueStore.md "../../../cloudfront/latest/APIReference/API_Operations_Amazon_CloudFront_KeyValueStore.md"), use a *Regional*
 endpoint in AWS STS to return a *version 2* session token. If you
 use the *global* endpoint for AWS STS
 (`sts.amazonaws.com`), AWS STS will generate a *version
 1* session token, which isn't supported by Signature Version 4A
 (SigV4A). As a result, you will receive an authentication error.


To call the CloudFront KeyValueStore API, you can use the following options: 




**AWS CLI and AWS SDKs**

You can configure the AWS CLI or an AWS SDK to use Regional AWS STS
 endpoints. For more information, see [AWS STS Regionalized endpoints](https://docs.aws.amazon.com/sdkref/latest/guide/feature-sts-regionalized-endpoints.html "https://docs.aws.amazon.com/sdkref/latest/guide/feature-sts-regionalized-endpoints.html") in the
 *AWS SDK and Tools Reference Guide*.


For more information about available AWS STS endpoints, see [Regions and endpoints](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_credentials_temp_enable-regions.html#id_credentials_region-endpoints "https://docs.aws.amazon.com/IAM/latest/UserGuide/id_credentials_temp_enable-regions.html#id_credentials_region-endpoints") in the
 *IAM User Guide*.



**SAML**

You can configure SAML to use Regional AWS STS endpoints. For more
 information, see the [How to use regional SAML endpoints for failover](https://aws.amazon.com/blogs/security/how-to-use-regional-saml-endpoints-for-failover/ "https://aws.amazon.com/blogs/security/how-to-use-regional-saml-endpoints-for-failover/") blog
 post.



**`SetSecurityTokenServicePreferences` API**

Instead of using a Regional AWS STS endpoint, you can configure the
 global endpoint for AWS STS to return version 2 session tokens. To do so,
 use the [SetSecurityTokenServicePreferences](https://docs.aws.amazon.com/IAM/latest/APIReference/API_SetSecurityTokenServicePreferences.html "https://docs.aws.amazon.com/IAM/latest/APIReference/API_SetSecurityTokenServicePreferences.html") API
 operation to configure your AWS account. 


###### Example: IAM CLI command


```
aws iam set-security-token-service-preferences --global-endpoint-token-version v2Token
```
###### Tip

We recommend that you use the AWS STS Regional endpoints instead
 of this option. Regional endpoints provide higher availability
 and failover scenarios.



**Custom identity provider**

If you're using a custom identity provider that does the federation
 and assumes the role, use one of the previous options for the parent
 identity provider system that is responsible for generating the session
 token.




## Runtime


The CloudFront Functions runtime environment doesn't support dynamic code evaluation,
 and it restricts access to the network, file system, environment variables, and
 timers. For more information, see [Restricted
 features](functions-javascript-runtime-10.md#writing-functions-javascript-features-restricted-features "functions-javascript-runtime-10.md#writing-functions-javascript-features-restricted-features").


###### Note

To use CloudFront KeyValueStore, your CloudFront function must use [JavaScript runtime
 2.0](functions-javascript-runtime-20.md "functions-javascript-runtime-20.md").


## Compute
 utilization


CloudFront Functions have a limit on the time they can take to run, measured as
 *compute utilization*. Compute utilization is a
 number between 0 and 100 that indicates the amount of time that the function took to
 run as a percentage of the maximum allowed time. For example, a compute utilization
 of 35 means that the function completed in 35% of the maximum allowed time.


When you [test a function](test-function.md "test-function.md"), you can see the
 compute utilization value in the output of the test event. For production functions,
 you can view the [compute
 utilization metric](viewing-cloudfront-metrics.md#monitoring-console.cloudfront-functions "viewing-cloudfront-metrics.md#monitoring-console.cloudfront-functions") on the [Monitoring page in the CloudFront console](https://console.aws.amazon.com/cloudfront/v4/home?#/monitoring "https://console.aws.amazon.com/cloudfront/v4/home?#/monitoring"), or in CloudWatch.
