# Setting up AWS TNB

Set up AWS TNB by completing the tasks described in this topic.

###### Tasks

- [Sign up for an AWS account](#sign-up-for-aws "#sign-up-for-aws")
- [Choose an AWS Region](#choose-region "#choose-region")
- [Note the service endpoint](#endpoints "#endpoints")
- [(Optional) Install the AWS CLI](#install-aws-cli "#install-aws-cli")
- [Set up AWS TNB roles](#set-service-roles "#set-service-roles")

## Sign up for an AWS account

To get started with AWS, you need an AWS account. For information about creating an AWS account, see
[Getting started with an AWS account](../../../accounts/latest/reference/getting-started.md "../../../accounts/latest/reference/getting-started.md")
in the _AWS Account Management Reference Guide_.

## Choose an AWS Region

To view the list of available Regions for AWS TNB, see the [AWS Regional Services
List](https://aws.amazon.com/about-aws/global-infrastructure/regional-product-services/ "https://aws.amazon.com/about-aws/global-infrastructure/regional-product-services/"). To view the list of endpoints for programmatic access, see [AWS TNB endpoints](../../../general/latest/gr/tnb.md "../../../general/latest/gr/tnb.md") in
the _AWS General Reference_.

## Note the service endpoint

To connect programmatically to an AWS service, you use an endpoint. In addition to the
standard AWS endpoints, some AWS services offer FIPS endpoints in selected Regions. For
more information, see [AWS
service endpoints](../../../general/latest/gr/rande.md "../../../general/latest/gr/rande.md").

| Region Name               | Region         | Endpoint                         | Protocol |
| ------------------------- | -------------- | -------------------------------- | -------- |
| US East (N. Virginia)     | us-east-1      | tnb.us-east-1.amazonaws.com      | HTTPS    |
| US West (Oregon)          | us-west-2      | tnb.us-west-2.amazonaws.com      | HTTPS    |
| Asia Pacific (Seoul)      | ap-northeast-2 | tnb.ap-northeast-2.amazonaws.com | HTTPS    |
| Asia Pacific (Sydney)     | ap-southeast-2 | tnb.ap-southeast-2.amazonaws.com | HTTPS    |
| Canada (Central)          | ca-central-1   | tnb.ca-central-1.amazonaws.com   | HTTPS    |
| Europe (Frankfurt)        | eu-central-1   | tnb.eu-central-1.amazonaws.com   | HTTPS    |
| Europe (Paris)            | eu-west-3      | tnb.eu-west-3.amazonaws.com      | HTTPS    |
| Europe (Spain)            | eu-south-2     | tnb.eu-south-2.amazonaws.com     | HTTPS    |
| Europe (Stockholm)        | eu-north-1     | tnb.eu-north-1.amazonaws.com     | HTTPS    |
| South America (São Paulo) | sa-east-1      | tnb.sa-east-1.amazonaws.com      | HTTPS    |

## (Optional) Install the AWS CLI

The AWS Command Line Interface (AWS CLI) provides commands for a broad set of AWS products, and is
supported on Windows, macOS, and Linux. You can access AWS TNB using the AWS CLI. To get
started, see the [AWS Command Line Interface User Guide](../../../cli/latest/userguide.md "../../../cli/latest/userguide.md"). For more information about the commands for AWS TNB, see
[tnb](../../../cli/latest/reference/tnb.md "../../../cli/latest/reference/tnb.md") in the
_AWS CLI Command Reference_.

## Set up AWS TNB roles

You must create a IAM service role to manage different parts of your AWS TNB
solution. AWS TNB service roles can make API calls to other AWS services, such as AWS CloudFormation, AWS CodeBuild,
and various compute and storage services, on your behalf, to instantiate and manage
resources for your deployment.

For more information about the AWS TNB service role, see [Identity and access management for AWS TNB](security-iam.md "security-iam.md").
