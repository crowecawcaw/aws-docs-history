

# Access AWS Secrets Manager
<a name="asm_access"></a>

**Topics**
+ [Secrets Manager console](#asm-console)
+ [Command line tools](#asm-cli)
+ [AWS SDKs](#asm-sdks)
+ [HTTPS Query API](#asm-sdks_query-api)
+ [AWS Secrets Manager endpoints](#endpoints)

## Secrets Manager console
<a name="asm-console"></a>

You can manage your secrets using the browser-based [Secrets Manager console](https://console.aws.amazon.com/secretsmanager/) and perform almost any task related to your secrets by using the console.

## Command line tools
<a name="asm-cli"></a>

The AWS command line tools allows you to issue commands at your system command line to perform Secrets Manager and other AWS tasks. This can be faster and more convenient than using the console. The command line tools can be useful if you want to build scripts to perform AWS tasks.

When you enter commands in a command shell, there is a risk of the command history being accessed or utilities having access to your command parameters. See [Mitigate the risks of using the AWS CLI to store your AWS Secrets Manager secrets](security_cli-exposure-risks.md).

The command line tools automatically use the default endpoint for the service in an AWS Region. You can specify a different endpoint for your API requests. See [AWS Secrets Manager endpoints](#endpoints).

AWS provides two sets of command line tools: 
+ [AWS Command Line Interface (AWS CLI)](https://docs.aws.amazon.com/cli/latest/reference/secretsmanager/index.html) 
+ [AWS Tools for Windows PowerShell](https://docs.aws.amazon.com/powershell/latest/reference/)

## AWS SDKs
<a name="asm-sdks"></a>

The AWS SDKs consist of libraries and sample code for various programming languages and platforms. The SDKs include tasks such as cryptographically signing requests, managing errors, and retrying requests automatically. To download and install any of the SDKs, see [Tools for Amazon Web Services](https://aws.amazon.com/tools/#sdk).

The AWS SDKs automatically use the default endpoint for the service in an AWS Region. You can specify a different endpoint for your API requests. See [AWS Secrets Manager endpoints](#endpoints).

For SDK documentation, see:
+ [C\+\+](http://sdk.amazonaws.com/cpp/api/LATEST/namespace_aws_1_1_secrets_manager.html)
+ [Go](https://docs.aws.amazon.com/sdk-for-go/api/service/secretsmanager/)
+ [Java](https://docs.aws.amazon.com/AWSJavaSDK/latest/javadoc/com/amazonaws/services/secretsmanager/package-summary.html)
+ [JavaScript](https://docs.aws.amazon.com/AWSJavaScriptSDK/latest/AWS/SecretsManager.html)
+ [Kotlin](https://sdk.amazonaws.com/kotlin/api/latest/secretsmanager/index.html)
+ [.NET](https://docs.aws.amazon.com/sdkfornet/v3/apidocs/items/SecretsManager/NSecretsManagerModel.html)
+ [PHP](https://docs.aws.amazon.com/aws-sdk-php/v3/api/namespace-Aws.SecretsManager.html)
+ [Python (Boto3)](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/secretsmanager.html)
+ [Ruby](https://docs.aws.amazon.com/sdk-for-ruby/v3/api/Aws/SecretsManager.html)
+ [Rust](https://crates.io/crates/aws-sdk-secretsmanager)
+ [SAP ABAP](https://docs.aws.amazon.com/sdk-for-sap-abap/v1/api/latest/smr/index.html)
+ [Swift](https://awslabs.github.io/aws-sdk-swift/reference/0.x/AWSSecretsManager/Home)

## HTTPS Query API
<a name="asm-sdks_query-api"></a>

The HTTPS Query API gives you [programmatic access](https://docs.aws.amazon.com/secretsmanager/latest/apireference/Welcome.html) to Secrets Manager and AWS. The HTTPS Query API allows you to issue HTTPS requests directly to the service. 

Although you can make direct calls to the Secrets Manager HTTPS Query API, we recommend that you use one of the SDKs instead. The SDK performs many useful tasks you otherwise must perform manually. For example, the SDKs automatically sign your requests and convert responses into a structure syntactically appropriate to your language.

To make HTTPS calls to Secrets Manager, you connect to [AWS Secrets Manager endpoints](#endpoints).

## AWS Secrets Manager endpoints
<a name="endpoints"></a>

To connect programmatically to Secrets Manager, you use an *endpoint*, the URL of the entry point for the service. Secrets Manager endpoints are dual-stack endpoints, which means they support both IPv4 and IPv6. 

Secrets Manager offers endpoints that support [Federal Information Processing Standard (FIPS) 140-2](http://aws.amazon.com/compliance/fips/) in some Regions.

Secrets Manager supports TLS 1.2 and 1.3. Secrets Manager supports [PQTLS](pqtls.md) in all regions except China Regions.

**Note**  
The Python AWS SDK and the AWS CLI attempt to call IPv6 and then IPv4 in sequence, so if you don't have IPv6 enabled, it can take some time before the call times out and retries with IPv4. To work around this issue, you can disable IPv6 completely or [migrate to IPv6](https://docs.aws.amazon.com/vpc/latest/userguide/vpc-migrate-ipv6.html). 

The following are the service endpoints for Secrets Manager. Note that the naming differs from the [typical dual-stack naming convention](https://docs.aws.amazon.com/general/latest/gr/rande.html#dual-stack-endpoints). For information about using dual-stack addressing in Secrets Manager, see [IPv4 and IPv6 access](ip-access.md).


| Region Name | Region | Endpoint | Protocol | 
| --- | --- | --- | --- | 
| US East (Ohio) | us-east-2 |  secretsmanager.us-east-2.amazonaws.com <br /> secretsmanager-fips.us-east-2.amazonaws.com  | HTTPS<br />HTTPS | 
| US East (N. Virginia) | us-east-1 |  secretsmanager.us-east-1.amazonaws.com <br /> secretsmanager-fips.us-east-1.amazonaws.com  | HTTPS<br />HTTPS | 
| US West (N. California) | us-west-1 |  secretsmanager.us-west-1.amazonaws.com <br /> secretsmanager-fips.us-west-1.amazonaws.com  | HTTPS<br />HTTPS | 
| US West (Oregon) | us-west-2 |  secretsmanager.us-west-2.amazonaws.com <br /> secretsmanager-fips.us-west-2.amazonaws.com  | HTTPS<br />HTTPS | 
| Africa (Cape Town) | af-south-1 |  secretsmanager.af-south-1.amazonaws.com  | HTTPS | 
| Asia Pacific (Hong Kong) | ap-east-1 |  secretsmanager.ap-east-1.amazonaws.com  | HTTPS | 
| Asia Pacific (Hyderabad) | ap-south-2 |  secretsmanager.ap-south-2.amazonaws.com  | HTTPS | 
| Asia Pacific (Jakarta) | ap-southeast-3 |  secretsmanager.ap-southeast-3.amazonaws.com  | HTTPS | 
| Asia Pacific (Malaysia) | ap-southeast-5 |  secretsmanager.ap-southeast-5.amazonaws.com  | HTTPS | 
| Asia Pacific (Melbourne) | ap-southeast-4 |  secretsmanager.ap-southeast-4.amazonaws.com  | HTTPS | 
| Asia Pacific (Mumbai) | ap-south-1 |  secretsmanager.ap-south-1.amazonaws.com  | HTTPS | 
| Asia Pacific (New Zealand) | ap-southeast-6 |  secretsmanager.ap-southeast-6.amazonaws.com  | HTTPS | 
| Asia Pacific (Osaka) | ap-northeast-3 |  secretsmanager.ap-northeast-3.amazonaws.com  | HTTPS | 
| Asia Pacific (Seoul) | ap-northeast-2 |  secretsmanager.ap-northeast-2.amazonaws.com  | HTTPS | 
| Asia Pacific (Singapore) | ap-southeast-1 |  secretsmanager.ap-southeast-1.amazonaws.com  | HTTPS | 
| Asia Pacific (Sydney) | ap-southeast-2 |  secretsmanager.ap-southeast-2.amazonaws.com  | HTTPS | 
| Asia Pacific (Taipei) | ap-east-2 |  secretsmanager.ap-east-2.amazonaws.com  | HTTPS | 
| Asia Pacific (Thailand) | ap-southeast-7 |  secretsmanager.ap-southeast-7.amazonaws.com  | HTTPS | 
| Asia Pacific (Tokyo) | ap-northeast-1 |  secretsmanager.ap-northeast-1.amazonaws.com  | HTTPS | 
| Canada (Central) | ca-central-1 |  secretsmanager.ca-central-1.amazonaws.com <br /> secretsmanager-fips.ca-central-1.amazonaws.com  | HTTPS<br />HTTPS | 
| Canada West (Calgary) | ca-west-1 |  secretsmanager.ca-west-1.amazonaws.com <br /> secretsmanager-fips.ca-west-1.amazonaws.com  | HTTPS<br />HTTPS | 
| Europe (Frankfurt) | eu-central-1 |  secretsmanager.eu-central-1.amazonaws.com  | HTTPS | 
| Europe (Ireland) | eu-west-1 |  secretsmanager.eu-west-1.amazonaws.com  | HTTPS | 
| Europe (London) | eu-west-2 |  secretsmanager.eu-west-2.amazonaws.com  | HTTPS | 
| Europe (Milan) | eu-south-1 |  secretsmanager.eu-south-1.amazonaws.com  | HTTPS | 
| Europe (Paris) | eu-west-3 |  secretsmanager.eu-west-3.amazonaws.com  | HTTPS | 
| Europe (Spain) | eu-south-2 |  secretsmanager.eu-south-2.amazonaws.com  | HTTPS | 
| Europe (Stockholm) | eu-north-1 |  secretsmanager.eu-north-1.amazonaws.com  | HTTPS | 
| Europe (Zurich) | eu-central-2 |  secretsmanager.eu-central-2.amazonaws.com  | HTTPS | 
| Israel (Tel Aviv) | il-central-1 |  secretsmanager.il-central-1.amazonaws.com  | HTTPS | 
| Mexico (Central) | mx-central-1 |  secretsmanager.mx-central-1.amazonaws.com  | HTTPS | 
| Middle East (Bahrain) | me-south-1 |  secretsmanager.me-south-1.amazonaws.com  | HTTPS | 
| Middle East (UAE) | me-central-1 |  secretsmanager.me-central-1.amazonaws.com  | HTTPS | 
| South America (São Paulo) | sa-east-1 |  secretsmanager.sa-east-1.amazonaws.com  | HTTPS | 
|  AWS GovCloud (US-East) | us-gov-east-1 |  secretsmanager.us-gov-east-1.amazonaws.com <br /> secretsmanager-fips.us-gov-east-1.amazonaws.com  | HTTPS<br />HTTPS | 
|  AWS GovCloud (US-West) | us-gov-west-1 |  secretsmanager.us-gov-west-1.amazonaws.com <br /> secretsmanager-fips.us-gov-west-1.amazonaws.com  | HTTPS<br />HTTPS | 