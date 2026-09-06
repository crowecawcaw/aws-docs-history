

# Allowed Domains
<a name="allowed-domains"></a>

## Streaming Instances
<a name="allowed-domains-streaming-instances"></a>

For WorkSpaces Applications users to access streaming instances, you must allow the following domain on the network from which users initiate access to the streaming instances.
+ Streaming Gateway: \*.amazonappstream.com
**Note**  
Instead of using a wildcard to allowlist all streaming gateways, you can create a VPC endpoint and allowlist only that specific endpoint. For more information, see [WorkSpaces Applications Interface VPC Endpoints](interface-vpc-endpoints.md).

For IPV4 support, you must allow the following domain on the network from which users initiate access to the streaming instances. It is region based and follows the following format: `*.streaming.{region}.appstream2.amazonappstream.com` and `*.dcv-streaming.{region}.appstream2.amazonappstream.com`. If its a FIPS compliant region, it will also need another endpoint with the format `*.streaming.{region}.appstream2-fips.amazonappstream.com` and `*.dcv-streaming.{region}.appstream2-fips.amazonappstream.com`. Check table below.

**Note**  
`*.streaming.*` URLs are not supported for the Asia Pacific (Malaysia), Asia Pacific (Osaka), Canada West (Calgary), Europe (Milan), Europe (Spain), Europe (Zurich), and Israel (Tel Aviv) Regions. For these Regions, allow only the `*.dcv-streaming.*` URLs listed in the table below.


| Region | Domain | 
| --- | --- | 
| US East (N. Virginia) | \*.streaming.us-east-1.appstream2.amazonappstream.com<br />\*.dcv-streaming.us-east-1.appstream2.amazonappstream.com<br />\*.streaming.us-east-1.appstream2-fips.amazonappstream.com<br />\*.dcv-streaming.us-east-1.appstream2-fips.amazonappstream.com | 
| US East (Ohio) | \*.streaming.us-east-2.appstream2.amazonappstream.com<br />\*.dcv-streaming.us-east-2.appstream2.amazonappstream.com | 
| US West (Oregon) | \*.streaming.us-west-2.appstream2.amazonappstream.com<br />\*.dcv-streaming.us-west-2.appstream2.amazonappstream.com<br />\*.streaming.us-west-2.appstream2-fips.amazonappstream.com<br />\*.dcv-streaming.us-west-2.appstream2-fips.amazonappstream.com | 
| Asia Pacific (Malaysia) | \*.dcv-streaming.ap-southeast-5.appstream2.amazonappstream.com | 
| Asia Pacific (Mumbai) | \*.streaming.ap-south-1.appstream2.amazonappstream.com<br />\*.dcv-streaming.ap-south-1.appstream2.amazonappstream.com | 
| Asia Pacific (Seoul) | \*.streaming.ap-northeast-2.appstream2.amazonappstream.com<br />\*.dcv-streaming.ap-northeast-2.appstream2.amazonappstream.com | 
| Asia Pacific (Singapore) | \*.streaming.ap-southeast-1.appstream2.amazonappstream.com<br />\*.dcv-streaming.ap-southeast-1.appstream2.amazonappstream.com | 
| Asia Pacific (Sydney) | \*.streaming.ap-southeast-2.appstream2.amazonappstream.com<br />\*.dcv-streaming.ap-southeast-2.appstream2.amazonappstream.com | 
| Asia Pacific (Tokyo) | \*.streaming.ap-northeast-1.appstream2.amazonappstream.com<br />\*.dcv-streaming.ap-northeast-1.appstream2.amazonappstream.com | 
| Asia Pacific (Osaka) | \*.dcv-streaming.ap-northeast-3.appstream2.amazonappstream.com | 
| Canada (Central) | \*.streaming.ca-central-1.appstream2.amazonappstream.com<br />\*.dcv-streaming.ca-central-1.appstream2.amazonappstream.com | 
| Canada West (Calgary) | \*.dcv-streaming.ca-west-1.appstream2.amazonappstream.com<br />\*.dcv-streaming.ca-west-1.appstream2-fips.amazonappstream.com | 
| Europe (Frankfurt) | \*.streaming.eu-central-1.appstream2.amazonappstream.com<br />\*.dcv-streaming.eu-central-1.appstream2.amazonappstream.com | 
| Europe (London) | \*.streaming.eu-west-2.appstream2.amazonappstream.com<br />\*.dcv-streaming.eu-west-2.appstream2.amazonappstream.com | 
| Europe (Ireland) | \*.streaming.eu-west-1.appstream2.amazonappstream.com<br />\*.dcv-streaming.eu-west-1.appstream2.amazonappstream.com | 
| Europe (Paris) | \*.streaming.eu-west-3.appstream2.amazonappstream.com<br />\*.dcv-streaming.eu-west-3.appstream2.amazonappstream.com | 
| Europe (Milan) | \*.dcv-streaming.eu-south-1.appstream2.amazonappstream.com | 
| Europe (Spain) | \*.dcv-streaming.eu-south-2.appstream2.amazonappstream.com | 
| Europe (Zurich) | \*.dcv-streaming.eu-central-2.appstream2.amazonappstream.com | 
| AWS GovCloud (US-East) | \*.streaming.us-gov-east-1.appstream2.amazonappstream.com<br />\*.dcv-streaming.us-gov-east-1.appstream2.amazonappstream.com<br />\*.streaming.us-gov-east-1.appstream2-fips.amazonappstream.com<br />\*.dcv-streaming.us-gov-east-1.appstream2-fips.amazonappstream.com | 
| AWS GovCloud (US-West) | \*.streaming.us-gov-west-1.appstream2.amazonappstream.com<br />\*.dcv-streaming.us-gov-west-1.appstream2.amazonappstream.com<br />\*.streaming.us-gov-west-1.appstream2-fips.amazonappstream.com<br />\*.dcv-streaming.us-gov-west-1.appstream2-fips.amazonappstream.com | 
| South America (São Paulo) | \*.streaming.sa-east-1.appstream2.amazonappstream.com<br />\*.dcv-streaming.sa-east-1.appstream2.amazonappstream.com | 
| Israel (Tel Aviv) | \*.dcv-streaming.il-central-1.appstream2.amazonappstream.com | 

For IPV6 support, you must allow the following domain on the network from which users initiate access to the streaming instances. It is region based and follows the following format: `*.streaming.appstream2.{region}.on.aws` and `*.dcv-streaming.appstream2.{region}.on.aws`. If its a FIPS compliant region, it will also need another endpoint with the format `*.streaming.appstream2-fips.{region}.on.aws` and `*.dcv-streaming.appstream2-fips.{region}.on.aws`. Check table below.

In order to use IPV6 address your base images must be updated to the images published on September 05, 2025 or later. For more information check [managed image updates](https://docs.aws.amazon.com/appstream2/latest/developerguide/keep-image-updated-managed-image-updates.html).


| Region | Domain | 
| --- | --- | 
| US East (N. Virginia) | \*.streaming.appstream2.us-east-1.on.aws<br />\*.dcv-streaming.appstream2.us-east-1.on.aws<br />\*.streaming.appstream2-fips.us-east-1.on.aws<br />\*.dcv-streaming.appstream2-fips.us-east-1.on.aws | 
| US East (Ohio) | \*.streaming.appstream2.us-east-2.on.aws<br />\*.dcv-streaming.appstream2.us-east-2.on.aws | 
| US West (Oregon) | \*.streaming.appstream2.us-west-2.on.aws<br />\*.dcv-streaming.appstream2.us-west-2.on.aws<br />\*.streaming.appstream2-fips.us-west-2.on.aws<br />\*.dcv-streaming.appstream2-fips.us-west-2.on.aws | 
| Asia Pacific (Malaysia) | \*.dcv-streaming.appstream2.ap-southeast-5.on.aws | 
| Asia Pacific (Mumbai) | \*.streaming.appstream2.ap-south-1.on.aws<br />\*.dcv-streaming.appstream2.ap-south-1.on.aws | 
| Asia Pacific (Seoul) | \*.streaming.appstream2.ap-northeast-2.on.aws<br />\*.dcv-streaming.appstream2.ap-northeast-2.on.aws | 
| Asia Pacific (Singapore) | \*.streaming.appstream2.ap-southeast-1.on.aws<br />\*.dcv-streaming.appstream2.ap-southeast-1.on.aws | 
| Asia Pacific (Sydney) | \*.streaming.appstream2.ap-southeast-2.on.aws<br />\*.dcv-streaming.appstream2.ap-southeast-2.on.aws | 
| Asia Pacific (Tokyo) | \*.streaming.appstream2.ap-northeast-1.on.aws<br />\*.dcv-streaming.appstream2.ap-northeast-1.on.aws | 
| Asia Pacific (Osaka) | \*.dcv-streaming.appstream2.ap-northeast-3.on.aws | 
| Canada (Central) | \*.streaming.appstream2.ca-central-1.on.aws<br />\*.dcv-streaming.appstream2.ca-central-1.on.aws | 
| Canada West (Calgary) | \*.dcv-streaming.appstream2.ca-west-1.on.aws<br />\*.dcv-streaming.appstream2-fips.ca-west-1.on.aws | 
| Europe (Frankfurt) | \*.streaming.appstream2.eu-central-1.on.aws<br />\*.dcv-streaming.appstream2.eu-central-1.on.aws | 
| Europe (London) | \*.streaming.appstream2.eu-west-2.on.aws<br />\*.dcv-streaming.appstream2.eu-west-2.on.aws | 
| Europe (Ireland) | \*.streaming.appstream2.eu-west-1.on.aws<br />\*.dcv-streaming.appstream2.eu-west-1.on.aws | 
| Europe (Paris) | \*.streaming.appstream2.eu-west-3.on.aws<br />\*.dcv-streaming.appstream2.eu-west-3.on.aws | 
| Europe (Milan) | \*.dcv-streaming.appstream2.eu-south-1.on.aws | 
| Europe (Spain) | \*.dcv-streaming.appstream2.eu-south-2.on.aws | 
| Europe (Zurich) | \*.dcv-streaming.appstream2.eu-central-2.on.aws | 
| AWS GovCloud (US-East) | \*.streaming.appstream2.us-gov-east-1.on.aws<br />\*.dcv-streaming.appstream2.us-gov-east-1.on.aws<br />\*.streaming.appstream2-fips.us-gov-east-1.on.aws<br />\*.dcv-streaming.appstream2-fips.us-gov-east-1.on.aws | 
| AWS GovCloud (US-West) | \*.streaming.appstream2.us-gov-west-1.on.aws<br />\*.dcv-streaming.appstream2.us-gov-west-1.on.aws<br />\*.streaming.appstream2-fips.us-gov-west-1.on.aws<br />\*.dcv-streaming.appstream2-fips.us-gov-west-1.on.aws | 
| South America (São Paulo) | \*.streaming.appstream2.sa-east-1.on.aws<br />\*.dcv-streaming.appstream2.sa-east-1.on.aws | 
| Israel (Tel Aviv) | \*.dcv-streaming.appstream2.il-central-1.on.aws | 

## User Authentication
<a name="allowed-domains-user-authentication"></a>

One or more of the following domains must be allowed to enable user authentication. You must allow the domains and subdomains that correspond to the Regions where WorkSpaces Applications is deployed. 


| Region | Domain | 
| --- | --- | 
| US East (N. Virginia) | \*.appstream2.us-east-1.aws.amazon.com | 
| US East (Ohio) | \*.appstream2.us-east-2.aws.amazon.com | 
| US West (Oregon) | \*.appstream2.us-west-2.aws.amazon.com | 
| Asia Pacific (Malaysia) | \*.appstream2.ap-southeast-5.aws.amazon.com | 
| Asia Pacific (Mumbai) | \*.appstream2.ap-south-1.aws.amazon.com | 
| Asia Pacific (Seoul) | \*.appstream2.ap-northeast-2.aws.amazon.com | 
| Asia Pacific (Singapore) | \*.appstream2.ap-southeast-1.aws.amazon.com | 
| Asia Pacific (Sydney) | \*.appstream2.ap-southeast-2.aws.amazon.com | 
| Asia Pacific (Tokyo) | \*.appstream2.ap-northeast-1.aws.amazon.com | 
| Asia Pacific (Osaka) | \*.appstream2.ap-northeast-3.aws.amazon.com | 
| Canada (Central) | \*.appstream2.ca-central-1.aws.amazon.com | 
| Canada West (Calgary) | \*.appstream2.ca-west-1.aws.amazon.com | 
| Europe (Frankfurt) | \*.appstream2.eu-central-1.aws.amazon.com | 
| Europe (London) | \*.appstream2.eu-west-2.aws.amazon.com | 
| Europe (Ireland) | \*.appstream2.eu-west-1.aws.amazon.com | 
| Europe (Milan) | \*.appstream2.eu-south-1.aws.amazon.com | 
| Europe (Paris) | \*.appstream2.eu-west-3.aws.amazon.com | 
| Europe (Spain) | \*.appstream2.eu-south-2.aws.amazon.com | 
| Europe (Zurich) | \*.appstream2.eu-central-2.aws.amazon.com | 
| AWS GovCloud (US-East) | \*.appstream2.us-gov-east-1.amazonaws-us-gov.com | 
| AWS GovCloud (US-West) | \*.appstream2.us-gov-west-1.amazonaws-us-gov.com | 
| South America (São Paulo) | \*.appstream2.sa-east-1.aws.amazon.com | 
| Israel (Tel Aviv) | \*.appstream2.il-central-1.aws.amazon.com | 

**Note**  
If your users use a network proxy to access streaming instances, disable any proxy caching for the user auth domains in the table and the session gateway, \*.amazonappstream.com.

For SAML 2.0 [single sign-on (SSO)] authentication, you must allow these three additional endpoints:

1. AWS Sign-in endpoint

1. AWS Sign-in region endpoints where WorkSpaces Applications is available

1. WorkSpaces Applications relay state region endpoints

The following table lists the AWS Sign-in endpoint.


| AWS Sign-in endpoint | 
| --- | 
| signin.aws.amazon.com | 

The following table lists the AWS Sign-in region endpoints for the Regions where WorkSpaces Applications is available.


**AWS Sign-in region endpoints**  

| Region | Domain | 
| --- | --- | 
| US East (N. Virginia) | us-east-1.signin.aws.amazon.com | 
| US East (Ohio) | us-east-2.signin.aws.amazon.com | 
| US West (Oregon) | us-west-2.signin.aws.amazon.com | 
| Asia Pacific (Malaysia) | ap-southeast-5.signin.aws.amazon.com | 
| Asia Pacific (Mumbai) | ap-south-1.signin.aws.amazon.com | 
| Asia Pacific (Seoul) | ap-northeast-2.signin.aws.amazon.com | 
| Asia Pacific (Singapore) | ap-southeast-1.signin.aws.amazon.com | 
| Asia Pacific (Sydney) | ap-southeast-2.signin.aws.amazon.com | 
| Asia Pacific (Tokyo) | ap-northeast-1.signin.aws.amazon.com | 
| Canada (Central) | ca-central-1.signin.aws.amazon.com | 
| Europe (Frankfurt) | eu-central-1.signin.aws.amazon.com | 
| Europe (Ireland) | eu-west-1.signin.aws.amazon.com | 
| Europe (London) | eu-west-2.signin.aws.amazon.com | 
| Europe (Milan) | eu-south-1.signin.aws.amazon.com | 
| Europe (Paris) | eu-west-3.signin.aws.amazon.com | 
| Europe (Spain) | eu-south-2.signin.aws.amazon.com | 
| AWS GovCloud (US-East) | us-gov-east-1.signin.amazonaws-us-gov.com | 
| AWS GovCloud (US-West) | signin.amazonaws-us-gov.com | 
| South America (São Paulo) | sa-east-1.signin.aws.amazon.com | 
| Israel (Tel Aviv) | il-central-1.signin.aws.amazon.com | 

The following table lists the WorkSpaces Applications relay state region endpoints.


**WorkSpaces Applications relay state region endpoints**  

| Region | Domain | 
| --- | --- | 
| US East (N. Virginia) | `appstream2.euc-sso.us-east-1.aws.amazon.com`<br />(FIPS) `appstream2.euc-sso-fips.us-east-1.aws.amazon.com` | 
| US East (Ohio) | appstream2.euc-sso.us-east-2.aws.amazon.com | 
| US West (Oregon) | `appstream2.euc-sso.us-west-2.aws.amazon.com`<br />(FIPS) `appstream2.euc-sso-fips.us-west-2.aws.amazon.com` | 
| Asia Pacific (Malaysia) | appstream2.euc-sso.ap-southeast-5.aws.amazon.com | 
| Asia Pacific (Mumbai) | appstream2.euc-sso.ap-south-1.aws.amazon.com | 
| Asia Pacific (Seoul) | appstream2.euc-sso.ap-northeast-2.aws.amazon.com | 
| Asia Pacific (Singapore) | appstream2.euc-sso.ap-southeast-1.aws.amazon.com | 
| Asia Pacific (Sydney) | appstream2.euc-sso.ap-southeast-2.aws.amazon.com | 
| Asia Pacific (Tokyo) | appstream2.euc-sso.ap-northeast-1.aws.amazon.com | 
| Canada (Central) | appstream2.euc-sso.ca-central-1.aws.amazon.com | 
| Europe (Frankfurt) | appstream2.euc-sso.eu-central-1.aws.amazon.com | 
| Europe (Ireland) | appstream2.euc-sso.eu-west-1.aws.amazon.com | 
| Europe (London) | appstream2.euc-sso.eu-west-2.aws.amazon.com | 
| Europe (Milan) | appstream2.euc-sso.eu-south-1.aws.amazon.com | 
| Europe (Paris) | appstream2.euc-sso.eu-west-3.aws.amazon.com | 
| Europe (Spain) | appstream2.euc-sso.eu-south-2.aws.amazon.com | 
| AWS GovCloud (US-East) | `appstream2.euc-sso.us-gov-east-1.amazonaws-us-gov.com`<br />(FIPS) `appstream2.euc-sso-fips.us-gov-east-1.amazonaws-us-gov.com` For more information about using WorkSpaces Applications in AWS GovCloud (US) Regions, see [Amazon WorkSpaces Applications](https://docs.aws.amazon.com/govcloud-us/latest/UserGuide/govcloud-appstream2.html) in the *AWS GovCloud (US) User Guide*.  | 
| AWS GovCloud (US-West) | `appstream2.euc-sso.us-gov-west-1.amazonaws-us-gov.com`<br />(FIPS) `appstream2.euc-sso-fips.us-gov-west-1.amazonaws-us-gov.com` For more information about using WorkSpaces Applications in AWS GovCloud (US) Regions, see [Amazon WorkSpaces Applications](https://docs.aws.amazon.com/govcloud-us/latest/UserGuide/govcloud-appstream2.html) in the *AWS GovCloud (US) User Guide*.  | 
| South America (São Paulo) | appstream2.euc-sso.sa-east-1.aws.amazon.com | 
| Israel (Tel Aviv) | appstream2.euc-sso.il-central-1.aws.amazon.com | 

## WorkSpaces Applications MCP endpoints
<a name="allowed-domains-mcp-endpoints"></a>

The following table lists the WorkSpaces Applications Model Context Protocol (MCP) endpoints.


**WorkSpaces Applications MCP endpoints**  

| Region | Domain | 
| --- | --- | 
| Asia Pacific (Tokyo) | agentaccess-mcp.ap-northeast-1.api.aws | 
| Asia Pacific (Seoul) | agentaccess-mcp.ap-northeast-2.api.aws | 
| Asia Pacific (Mumbai) | agentaccess-mcp.ap-south-1.api.aws | 
| Asia Pacific (Singapore) | agentaccess-mcp.ap-southeast-1.api.aws | 
| Asia Pacific (Sydney) | agentaccess-mcp.ap-southeast-2.api.aws | 
| Canada (Central) | agentaccess-mcp.ca-central-1.api.aws | 
| Europe (Frankfurt) | agentaccess-mcp.eu-central-1.api.aws | 
| Europe (Ireland) | agentaccess-mcp.eu-west-1.api.aws | 
| Europe (London) | agentaccess-mcp.eu-west-2.api.aws | 
| Europe (Paris) | agentaccess-mcp.eu-west-3.api.aws | 
| US East (N. Virginia) | agentaccess-mcp.us-east-1.api.aws | 
| US East (Ohio) | agentaccess-mcp.us-east-2.api.aws | 
| US West (Oregon) | agentaccess-mcp.us-west-2.api.aws | 

## AWS IP address ranges
<a name="allowed-domains-aws-ip-ranges"></a>

AWS publishes its current IP address ranges, including the ranges that the Session Gateway and CloudFront domains may resolve to, in JSON format. For information about how to download the .json file and view the current ranges, see [AWS IP Address Ranges](https://docs.aws.amazon.com/general/latest/gr/aws-ip-ranges.html) in the Amazon Web Services General Reference. Or, if you are using AWS Tools for Windows PowerShell, you can access the same information by using the `Get-AWSPublicIpAddressRange` cmdlet. For more information, see [Querying the Public IP Address Ranges for AWS](https://aws.amazon.com/blogs/developer/querying-the-public-ip-address-ranges-for-aws/).

For WorkSpaces Applications users that are accessing Elastic fleets, you must allow access to the domain for the Amazon Simple Storage Service (S3) bucket that contains the application icon.

**Note**  
If your S3 bucket has a “.” character in the name, the domain used is https://s3.<AWS Region>.amazonaws.com. If your S3 bucket does not have a “.” character in the name, the domain used is https://<{{bucket name}}>.s3.<{{AWS Region}}>.amazonaws.com.