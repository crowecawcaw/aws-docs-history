

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

To get started with AWS, you need an AWS account. There are two ways to sign up for AWS. If you want complete control over account configuration and where your content is stored, or if you have regulated workloads such as HIPAA or FedRAMP, use [Sign up for AWS (advanced)](https://docs.aws.amazon.com/accounts/latest/reference/getting-started.html). If you are a new user and want to use a login you already own to sign in to AWS and create an AWS environment with preconfigured defaults in select [AWS Regions](https://docs.aws.amazon.com/accounts/latest/reference/project-regions.html), use [Sign up for AWS](https://docs.aws.amazon.com/accounts/latest/reference/sign-in-new.html).

## Choose an AWS Region
<a name="choose-region"></a>

To view the list of available Regions for AWS TNB, see the [AWS Regional Services List](https://aws.amazon.com/about-aws/global-infrastructure/regional-product-services/). To view the list of endpoints for programmatic access, see [AWS TNB endpoints](https://docs.aws.amazon.com/general/latest/gr/tnb.html) in the *AWS General Reference*.

## Note the service endpoint
<a name="endpoints"></a>

To connect programmatically to an AWS service, you use an endpoint. In addition to the standard AWS endpoints, some AWS services offer FIPS endpoints in selected Regions. For more information, see [AWS service endpoints](https://docs.aws.amazon.com/general/latest/gr/rande.html).

## (Optional) Install the AWS CLI
<a name="install-aws-cli"></a>

The AWS Command Line Interface (AWS CLI) provides commands for a broad set of AWS products, and is supported on Windows, macOS, and Linux. You can access AWS TNB using the AWS CLI. To get started, see the [AWS Command Line Interface User Guide](https://docs.aws.amazon.com/cli/latest/userguide/). For more information about the commands for AWS TNB, see [tnb](https://docs.aws.amazon.com/cli/latest/reference/tnb/) in the *AWS CLI Command Reference*.

## Set up AWS TNB roles
<a name="set-service-roles"></a>

You must create a IAM service role to manage different parts of your AWS TNB solution. AWS TNB service roles can make API calls to other AWS services, such as AWS CloudFormation, AWS CodeBuild, and various compute and storage services, on your behalf, to instantiate and manage resources for your deployment.

For more information about the AWS TNB service role, see [Identity and access management for AWS TNB](security-iam.md).