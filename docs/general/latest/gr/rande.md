

# AWS service endpoints
<a name="rande"></a>

To connect programmatically to an AWS service, you use an endpoint. An *endpoint* is the URL of the entry point for an AWS web service. The AWS SDKs and the AWS Command Line Interface (AWS CLI) automatically use the default endpoint for each service in an AWS Region. But you can specify an alternate endpoint for your API requests.

If a service supports Regions, the resources in each Region are independent of similar resources in other Regions. For example, you can create an Amazon EC2 instance or an Amazon SQS queue in one Region. When you do, the instance or queue is independent of instances or queues in all other Regions.

**Topics**
+ [Regional endpoints](#regional-endpoints)
+ [Global endpoints](#global-endpoints)
+ [View the service endpoints](#view-service-endpoints)
+ [FIPS endpoints](#FIPS-endpoints)
+ [Dual stack endpoints](#dual-stack-endpoints)
+ [Learn more](#learn-more)

## Regional endpoints
<a name="regional-endpoints"></a>

Most Amazon Web Services offer a Regional endpoint that you can use to make your requests. In general, these endpoints support IPv4 traffic and they use the following syntax.

```
{{protocol}}://{{service-code}}.{{region-code}}.amazonaws.com
```

For example, `https://dynamodb.us-west-2.amazonaws.com` is the endpoint for the Amazon DynamoDB service in the US West (Oregon) Region.<a name="region-names-codes"></a>

The following table lists the name and code of each Region.


| Name | Code | 
| --- | --- | 
| US East (Ohio) | us-east-2 | 
| US East (N. Virginia) | us-east-1 | 
| US West (N. California) | us-west-1 | 
| US West (Oregon) | us-west-2 | 
| Africa (Cape Town) | af-south-1 | 
| Asia Pacific (Hong Kong) | ap-east-1 | 
| Asia Pacific (Hyderabad) | ap-south-2 | 
| Asia Pacific (Jakarta) | ap-southeast-3 | 
| Asia Pacific (Malaysia) | ap-southeast-5 | 
| Asia Pacific (Melbourne) | ap-southeast-4 | 
| Asia Pacific (Mumbai) | ap-south-1 | 
| Asia Pacific (New Zealand) | ap-southeast-6 | 
| Asia Pacific (Osaka) | ap-northeast-3 | 
| Asia Pacific (Seoul) | ap-northeast-2 | 
| Asia Pacific (Singapore) | ap-southeast-1 | 
| Asia Pacific (Sydney) | ap-southeast-2 | 
| Asia Pacific (Taipei) | ap-east-2 | 
| Asia Pacific (Thailand) | ap-southeast-7 | 
| Asia Pacific (Tokyo) | ap-northeast-1 | 
| Canada (Central) | ca-central-1 | 
| Canada West (Calgary) | ca-west-1 | 
| Europe (Frankfurt) | eu-central-1 | 
| Europe (Ireland) | eu-west-1 | 
| Europe (London) | eu-west-2 | 
| Europe (Milan) | eu-south-1 | 
| Europe (Paris) | eu-west-3 | 
| Europe (Spain) | eu-south-2 | 
| Europe (Stockholm) | eu-north-1 | 
| Europe (Zurich) | eu-central-2 | 
| Israel (Tel Aviv) | il-central-1 | 
| Mexico (Central) | mx-central-1 | 
| Middle East (Bahrain) | me-south-1 | 
| Middle East (UAE) | me-central-1 | 
| South America (São Paulo) | sa-east-1 | 
| AWS GovCloud (US-East) | us-gov-east-1 | 
| AWS GovCloud (US-West) | us-gov-west-1 | 

**General endpoints**

The following services support Regional endpoints but also support a general endpoint that doesn't include a Region. When you use a general endpoint, AWS routes the API request to US East (N. Virginia) (`us-east-1`), which is the default Region for API calls.
+ Amazon EC2 – ec2.amazonaws.com
+ Amazon EC2 Auto Scaling – autoscaling.amazonaws.com
+ Amazon EMR – elasticmapreduce.amazonaws.com

## Global endpoints
<a name="global-endpoints"></a>

The following services each have a global endpoint that spans AWS Regions:
+ [AWS Cloud WAN](cloudwan.md#cloudwan_region)
+ [Amazon CloudFront](cf_region.md)
+ [AWS Global Accelerator](global_accelerator.md#global_accelerator_region)
+ [AWS Identity and Access Management](iam-service.md#iam_region) (IAM)
+ [AWS Organizations](ao.md#ao_region)
+ [Amazon Route 53](r53.md#r53_region)
+ [AWS Shield Advanced](shield.md#shield_region)
+ [AWS WAF Classic](waf-classic.md#waf-classic_region)

Note that some of these services have additional endpoints, such as FIPS endpoints.

## View the service endpoints
<a name="view-service-endpoints"></a>

You can view the AWS service endpoints using the following options:
+ Open [Service endpoints and quotas](aws-service-information.md), search for the service name, and click the link to open the page for that service. To view the supported endpoints for all AWS services in the documentation without switching pages, view the information in the [Service Endpoints and Quotas](https://docs.aws.amazon.com/general/latest/gr/aws-general.pdf#aws-service-information) page in the PDF instead.
+ To programmatically check for service availability using the SDK for Java, see [Check for service availability in an Region](https://docs.aws.amazon.com/sdk-for-java/v2/developer-guide/java-dg-region-selection.html#region-selection-query-service) in the *AWS SDK for Java Developer Guide*.
+ To programmatically view Region and service information using Systems Manager, see [Calling public parameters for AWS services, Regions, endpoints, and zones in parameter store](https://docs.aws.amazon.com/systems-manager/latest/userguide/parameter-store-public-parameters-global-infrastructure.html) in the *AWS Systems Manager User Guide*. For information about how to use public parameters, see [Query for AWS Regions, Endpoints, and More Using AWS Systems Manager Parameter Store](https://aws.amazon.com/blogs/aws/new-query-for-aws-regions-endpoints-and-more-using-aws-systems-manager-parameter-store/).
+ To see the supported AWS services in each Region (without endpoints), see the [Region Table](https://aws.amazon.com/about-aws/global-infrastructure/regional-product-services/).

## FIPS endpoints
<a name="FIPS-endpoints"></a>

Some AWS services offer endpoints that support Federal Information Processing Standard (FIPS) 140 in some Regions. Unlike standard AWS endpoints, FIPS endpoints use a TLS software library that complies with FIPS 140. These endpoints might be required by enterprises that interact with the United States government.

To specify a FIPS endpoint when you call an AWS operation, use a mechanism provided by the tool that you're using to make the call. For example, the AWS SDKs provide the following mechanisms to use FIPS endpoints:
+ Set the `AWS_USE_FIPS_ENDPOINT` environment variable to `true`
+ Add `use_fips_endpoint=true` to your `~/.aws/config` file

For information about FIPS endpoint support in AWS SDKs, see [Dual-stack and FIPS endpoints](https://docs.aws.amazon.com/sdkref/latest/guide/feature-endpoints.html) in the *AWS SDKs and Tools Reference Guide*.

The AWS Command Line Interface supports the preceding mechanisms, and also provides the `--endpoint-url` option. The following example uses `--endpoint-url` to specify the FIPS endpoint for AWS Key Management Service (AWS KMS) in the US West (Oregon) Region.

```
aws kms create-key --endpoint-url https://kms-fips.us-west-2.amazonaws.com
```

For a list of FIPS endpoints, see [FIPS endpoints by Service](https://aws.amazon.com/compliance/fips/#FIPS_Endpoints_by_Service).

### Minimum TLS version for FIPS endpoints
<a name="fips-tls-version"></a>

With FIPS endpoints, the minimum requirement is TLS 1.2. We recommend TLS 1.3. To determine whether your applications were affected by this change, see [this AWS Security Blog post](https://aws.amazon.com/blogs/security/tls-1-2-confirm-your-connections/).

## Dual stack endpoints
<a name="dual-stack-endpoints"></a>

Some AWS services offer dual stack endpoints, so that you can access them using either IPv4 or IPv6 requests. In general, the syntax of a dual stack endpoint is as follows:

```
{{protocol}}://{{service-code}}.{{region-code}}.api.aws
```

However, Amazon S3 uses the following syntax for [Amazon S3 dual stack endpoints](https://docs.aws.amazon.com/AmazonS3/latest/API/dual-stack-endpoints.html):

```
{{protocol}}://{{service-code}}.dualstack.{{region-code}}.amazonaws.com
```

To make a request to a dual stack endpoint, use the mechanism provided by the tool or AWS SDK to specify the endpoint. For information about dual stack endpoint support in AWS SDKs, see [Dual-stack and FIPS endpoints](https://docs.aws.amazon.com/sdkref/latest/guide/feature-endpoints.html) in the *AWS SDKs and Tools Reference Guide*.

The AWS CLI provides the `--endpoint-url` option. The following example uses `--endpoint-url` to specify the dual stack endpoint for Amazon EC2 in the US West (Oregon) Region.

```
aws ec2 describe-regions --region us-west-2 --endpoint-url https://ec2.us-west-2.api.aws
```

To use the AWS CLI to configure dual-stack endpoints for all AWS services, see [Set to use dual-stack endpoints for all AWS services](https://docs.aws.amazon.com/cli/latest/userguide/cli-configure-endpoints.html#endpoints-dual-stack) in the *AWS Command Line Interface User Guide*.

For a list of services that support dual stack endpoints, see [AWS services that support IPv6](https://docs.aws.amazon.com/vpc/latest/userguide/aws-ipv6-support.html).

## Learn more
<a name="learn-more"></a>

You can find endpoint information from the following sources:
+ To enable Regions that are disabled by default, see [Enable or disable AWS Regions in your account](https://docs.aws.amazon.com/accounts/latest/reference/manage-acct-regions.html) in the *AWS Account Management Reference Guide*.
+ For information about the AWS services and endpoints available in the China Regions, see [China (Beijing) Region Endpoints](https://docs.amazonaws.cn/en_us/general/latest/gr/endpoints-Beijing.html) and [China (Ningxia) Region Endpoints](https://docs.amazonaws.cn/en_us/general/latest/gr/endpoints-Ningxia.html).