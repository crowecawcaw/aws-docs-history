

# Setting up AWS TNB
<a name="setting-up"></a>

Set up AWS TNB by completing the tasks described in this topic.

**Topics**
+ [Sign up for an AWS account](#sign-up-for-aws)
+ [Choose an AWS Region](#choose-region)
+ [Note the service endpoint](#endpoints)
+ [(Optional) Install the AWS CLI](#install-aws-cli)
+ [Set up AWS TNB roles](#set-service-roles)

## Sign up for an AWS account
<a name="sign-up-for-aws"></a>

To get started with AWS, you need an AWS account. For information about creating an AWS account, see [Getting started with an AWS account](https://docs.aws.amazon.com/accounts/latest/reference/getting-started.html) in the *AWS Account Management Reference Guide*.

## Choose an AWS Region
<a name="choose-region"></a>

To view the list of available Regions for AWS TNB, see the [AWS Regional Services List](https://aws.amazon.com/about-aws/global-infrastructure/regional-product-services/). To view the list of endpoints for programmatic access, see [AWS TNB endpoints](https://docs.aws.amazon.com/general/latest/gr/tnb.html) in the *AWS General Reference*.

## Note the service endpoint
<a name="endpoints"></a>

To connect programmatically to an AWS service, you use an endpoint. In addition to the standard AWS endpoints, some AWS services offer FIPS endpoints in selected Regions. For more information, see [AWS service endpoints](https://docs.aws.amazon.com/general/latest/gr/rande.html).


| Region Name | Region | Endpoint | Protocol | 
| --- | --- | --- | --- | 
| US East (N. Virginia) | us-east-1 |  tnb.us-east-1.amazonaws.com  | HTTPS | 
| US West (Oregon) | us-west-2 |  tnb.us-west-2.amazonaws.com  | HTTPS | 
| Asia Pacific (Seoul) | ap-northeast-2 |  tnb.ap-northeast-2.amazonaws.com  | HTTPS | 
| Asia Pacific (Sydney) | ap-southeast-2 |  tnb.ap-southeast-2.amazonaws.com  | HTTPS | 
| Canada (Central) | ca-central-1 |  tnb.ca-central-1.amazonaws.com  | HTTPS | 
| Europe (Frankfurt) | eu-central-1 |  tnb.eu-central-1.amazonaws.com  | HTTPS | 
| Europe (Paris) | eu-west-3 |  tnb.eu-west-3.amazonaws.com  | HTTPS | 
| Europe (Spain) | eu-south-2 |  tnb.eu-south-2.amazonaws.com  | HTTPS | 
| Europe (Stockholm) | eu-north-1 |  tnb.eu-north-1.amazonaws.com  | HTTPS | 
| South America (São Paulo) | sa-east-1 |  tnb.sa-east-1.amazonaws.com  | HTTPS | 

## (Optional) Install the AWS CLI
<a name="install-aws-cli"></a>

The AWS Command Line Interface (AWS CLI) provides commands for a broad set of AWS products, and is supported on Windows, macOS, and Linux. You can access AWS TNB using the AWS CLI. To get started, see the [AWS Command Line Interface User Guide](https://docs.aws.amazon.com/cli/latest/userguide/). For more information about the commands for AWS TNB, see [tnb](https://docs.aws.amazon.com/cli/latest/reference/tnb/) in the *AWS CLI Command Reference*.

## Set up AWS TNB roles
<a name="set-service-roles"></a>

You must create a IAM service role to manage different parts of your AWS TNB solution. AWS TNB service roles can make API calls to other AWS services, such as AWS CloudFormation, AWS CodeBuild, and various compute and storage services, on your behalf, to instantiate and manage resources for your deployment.

For more information about the AWS TNB service role, see [Identity and access management for AWS TNB](security-iam.md).