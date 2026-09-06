

# AWS Sign-In endpoints and quotas
<a name="signin-service"></a>

To connect programmatically to an AWS service, you use an endpoint. AWS services offer the following endpoint types in some or all of the AWS Regions that the service supports: IPv4 endpoints, dual-stack endpoints, and FIPS endpoints. Some services provide global endpoints. For more information, see [AWS service endpoints](rande.md).

Service quotas, also referred to as limits, are the maximum number of service resources or operations for your AWS account. For more information, see [AWS service quotas](aws_service_limits.md).

The following are the service endpoints and service quotas for this service.

## Service endpoints
<a name="signin_region"></a>


| Region Name | Region | Endpoint | Protocol | 
| --- | --- | --- | --- | 
| US East (Ohio) | us-east-2 |  us-east-2.signin.aws.amazon.com  | HTTPS | 
| US East (N. Virginia) | us-east-1 |  signin.aws.amazon.com  | HTTPS | 
| US West (N. California) | us-west-1 |  us-west-1.signin.aws.amazon.com  | HTTPS | 
| US West (Oregon) | us-west-2 |  us-west-2.signin.aws.amazon.com  | HTTPS | 
| Africa (Cape Town) | af-south-1 |  af-south-1.signin.aws.amazon.com  | HTTPS | 
| Asia Pacific (Hong Kong) | ap-east-1 |  ap-east-1.signin.aws.amazon.com  | HTTPS | 
| Asia Pacific (Hyderabad) | ap-south-2 |  ap-south-2.signin.aws.amazon.com  | HTTPS | 
| Asia Pacific (Jakarta) | ap-southeast-3 |  ap-southeast-3.signin.aws.amazon.com  | HTTPS | 
| Asia Pacific (Malaysia) | ap-southeast-5 |  ap-southeast-5.signin.aws.amazon.com  | HTTPS | 
| Asia Pacific (Melbourne) | ap-southeast-4 |  ap-southeast-4.signin.aws.amazon.com  | HTTPS | 
| Asia Pacific (Mumbai) | ap-south-1 |  ap-south-1.signin.aws.amazon.com  | HTTPS | 
| Asia Pacific (New Zealand) | ap-southeast-6 |  ap-southeast-6.signin.aws.amazon.com  | HTTPS | 
| Asia Pacific (Osaka) | ap-northeast-3 |  ap-northeast-3.signin.aws.amazon.com  | HTTPS | 
| Asia Pacific (Seoul) | ap-northeast-2 |  ap-northeast-2.signin.aws.amazon.com  | HTTPS | 
| Asia Pacific (Singapore) | ap-southeast-1 |  ap-southeast-1.signin.aws.amazon.com  | HTTPS | 
| Asia Pacific (Sydney) | ap-southeast-2 |  ap-southeast-2.signin.aws.amazon.com  | HTTPS | 
| Asia Pacific (Taipei) | ap-east-2 |  ap-east-2.signin.aws.amazon.com  | HTTPS | 
| Asia Pacific (Thailand) | ap-southeast-7 |  ap-southeast-7.signin.aws.amazon.com  | HTTPS | 
| Asia Pacific (Tokyo) | ap-northeast-1 |  ap-northeast-1.signin.aws.amazon.com  | HTTPS | 
| Canada (Central) | ca-central-1 |  ca-central-1.signin.aws.amazon.com  | HTTPS | 
| Canada West (Calgary) | ca-west-1 |  ca-west-1.signin.aws.amazon.com  | HTTPS | 
| Europe (Frankfurt) | eu-central-1 |  eu-central-1.signin.aws.amazon.com  | HTTPS | 
| Europe (Ireland) | eu-west-1 |  eu-west-1.signin.aws.amazon.com  | HTTPS | 
| Europe (London) | eu-west-2 |  eu-west-2.signin.aws.amazon.com  | HTTPS | 
| Europe (Milan) | eu-south-1 |  eu-south-1.signin.aws.amazon.com  | HTTPS | 
| Europe (Paris) | eu-west-3 |  eu-west-3.signin.aws.amazon.com  | HTTPS | 
| Europe (Spain) | eu-south-2 |  eu-south-2.signin.aws.amazon.com  | HTTPS | 
| Europe (Stockholm) | eu-north-1 |  eu-north-1.signin.aws.amazon.com  | HTTPS | 
| Europe (Zurich) | eu-central-2 |  eu-central-2.signin.aws.amazon.com  | HTTPS | 
| Israel (Tel Aviv) | il-central-1 |  il-central-1.signin.aws.amazon.com  | HTTPS | 
| Mexico (Central) | mx-central-1 |  mx-central-1.signin.aws.amazon.com  | HTTPS | 
| Middle East (Bahrain) | me-south-1 |  me-south-1.signin.aws.amazon.com  | HTTPS | 
| Middle East (UAE) | me-central-1 |  me-central-1.signin.aws.amazon.com  | HTTPS | 
| South America (São Paulo) | sa-east-1 |  sa-east-1.signin.aws.amazon.com  | HTTPS | 
|  AWS GovCloud (US-East) | us-gov-east-1 |  us-gov-east-1.signin.amazonaws-us-gov.com  | HTTPS | 
|  AWS GovCloud (US-West) | us-gov-west-1 |  signin.amazonaws-us-gov.com  | HTTPS | 

## OAuth service endpoints
<a name="signin_oauth_region"></a>

The following table lists the endpoints that you can use for AWS Sign-In OAuth operations.


| Region name | Region | Endpoint | Protocol | 
| --- | --- | --- | --- | 
| US East (N. Virginia) | us-east-1 | https://us-east-1.oauth.signin.aws | HTTPS | 
| US East (Ohio) | us-east-2 | https://us-east-2.oauth.signin.aws | HTTPS | 
| US West (N. California) | us-west-1 | https://us-west-1.oauth.signin.aws | HTTPS | 
| US West (Oregon) | us-west-2 | https://us-west-2.oauth.signin.aws | HTTPS | 
| Africa (Cape Town) | af-south-1 | https://af-south-1.oauth.signin.aws | HTTPS | 
| Asia Pacific (Hong Kong) | ap-east-1 | https://ap-east-1.oauth.signin.aws | HTTPS | 
| Asia Pacific (Hyderabad) | ap-south-2 | https://ap-south-2.oauth.signin.aws | HTTPS | 
| Asia Pacific (Jakarta) | ap-southeast-3 | https://ap-southeast-3.oauth.signin.aws | HTTPS | 
| Asia Pacific (Melbourne) | ap-southeast-4 | https://ap-southeast-4.oauth.signin.aws | HTTPS | 
| Asia Pacific (Mumbai) | ap-south-1 | https://ap-south-1.oauth.signin.aws | HTTPS | 
| Asia Pacific (Osaka) | ap-northeast-3 | https://ap-northeast-3.oauth.signin.aws | HTTPS | 
| Asia Pacific (Seoul) | ap-northeast-2 | https://ap-northeast-2.oauth.signin.aws | HTTPS | 
| Asia Pacific (Singapore) | ap-southeast-1 | https://ap-southeast-1.oauth.signin.aws | HTTPS | 
| Asia Pacific (Sydney) | ap-southeast-2 | https://ap-southeast-2.oauth.signin.aws | HTTPS | 
| Asia Pacific (Tokyo) | ap-northeast-1 | https://ap-northeast-1.oauth.signin.aws | HTTPS | 
| Canada (Central) | ca-central-1 | https://ca-central-1.oauth.signin.aws | HTTPS | 
| Canada West (Calgary) | ca-west-1 | https://ca-west-1.oauth.signin.aws | HTTPS | 
| Europe (Frankfurt) | eu-central-1 | https://eu-central-1.oauth.signin.aws | HTTPS | 
| Europe (Ireland) | eu-west-1 | https://eu-west-1.oauth.signin.aws | HTTPS | 
| Europe (London) | eu-west-2 | https://eu-west-2.oauth.signin.aws | HTTPS | 
| Europe (Milan) | eu-south-1 | https://eu-south-1.oauth.signin.aws | HTTPS | 
| Europe (Paris) | eu-west-3 | https://eu-west-3.oauth.signin.aws | HTTPS | 
| Europe (Spain) | eu-south-2 | https://eu-south-2.oauth.signin.aws | HTTPS | 
| Europe (Stockholm) | eu-north-1 | https://eu-north-1.oauth.signin.aws | HTTPS | 
| Europe (Zurich) | eu-central-2 | https://eu-central-2.oauth.signin.aws | HTTPS | 
| Israel (Tel Aviv) | il-central-1 | https://il-central-1.oauth.signin.aws | HTTPS | 
| Middle East (Bahrain) | me-south-1 | https://me-south-1.oauth.signin.aws | HTTPS | 
| Middle East (UAE) | me-central-1 | https://me-central-1.oauth.signin.aws | HTTPS | 
| South America (São Paulo) | sa-east-1 | https://sa-east-1.oauth.signin.aws | HTTPS | 

## Service quotas
<a name="limits_signin"></a>

AWS Sign-In has no increasable quotas.