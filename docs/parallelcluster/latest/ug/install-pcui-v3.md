# Installing the PCUI

The AWS ParallelCluster UI (PCUI) is a web-based user interface that mirrors the AWS ParallelCluster `pcluster` CLI, while providing a console-like
experience. You install and access the PCUI in your AWS account. When you run it, the PCUI accesses an instance of the AWS ParallelCluster API
hosted on Amazon API Gateway in your AWS account. For more information about the PCUI, see [AWS ParallelCluster UI](pcui-using-v3.md "pcui-using-v3.md").

###### Prerequisites:

- You must have an AWS account
- You must have access to the AWS Management Console
  For more information, see [Setting up an AWS account](install-v3.md#setting-up "install-v3.md#setting-up").

###### Topics

- [Install the PCUI](#install-pcui-steps-v3 "#install-pcui-steps-v3")
- [Stack parameters](#install-pcui-steps-v3-stack-params "#install-pcui-steps-v3-stack-params")
- [Configure a custom domain](tutorials_08_custom_domain-v3.md "tutorials_08_custom_domain-v3.md")
- [Amazon Cognito user pool options](install-pcui-cognito-v3.md "install-pcui-cognito-v3.md")
- [Identify the AWS ParallelCluster and PCUI version](install-pcui-version-v3.md "install-pcui-version-v3.md")
- [PCUI costs](install-pcui-costs-v3.md "install-pcui-costs-v3.md")

## Install the PCUI

To install an instance of the AWS ParallelCluster UI (PCUI), choose an CloudFormation quick-create link for the AWS Region in which you create clusters. The
quick-create URL takes you to a **Create Stack Wizard** where you provide quick-create stack template inputs and deploy the
stack. For more information about CloudFormation quick-create stacks, see [Creating quick-create links for stacks](../../../AWSCloudFormation/latest/UserGuide/cfn-console-create-stacks-quick-create-links.md "../../../AWSCloudFormation/latest/UserGuide/cfn-console-create-stacks-quick-create-links.md") in
the _AWS CloudFormation User Guide_.

###### Note

You can only create and edit clusters or build images with the same AWS ParallelCluster version that you use to install the PCUI.

###### Use an AWS CloudFormation quick-create link to deploy a PCUI stack with nested Amazon Cognito, API Gateway, and Amazon EC2 Systems Manager stacks.

1. Sign in to the AWS Management Console.
2. Deploy the PCUI by choosing an AWS Region quick-create link from the list here. This
   takes you to the CloudFormation **Create Stack Wizard** in the console.
   - [us-east-1](https://us-east-1.console.aws.amazon.com/cloudformation/home?region=us-east-1#/stacks/create/review?stackName=parallelcluster-ui&templateURL=https://parallelcluster-ui-release-artifacts-us-east-1.s3.us-east-1.amazonaws.com/parallelcluster-ui.yaml "https://us-east-1.console.aws.amazon.com/cloudformation/home?region=us-east-1#/stacks/create/review?stackName=parallelcluster-ui&templateURL=https://parallelcluster-ui-release-artifacts-us-east-1.s3.us-east-1.amazonaws.com/parallelcluster-ui.yaml")
   - [us-east-2](https://us-east-2.console.aws.amazon.com/cloudformation/home?region=us-east-2#/stacks/create/review?stackName=parallelcluster-ui&templateURL=https://parallelcluster-ui-release-artifacts-us-east-1.s3.us-east-1.amazonaws.com/parallelcluster-ui.yaml "https://us-east-2.console.aws.amazon.com/cloudformation/home?region=us-east-2#/stacks/create/review?stackName=parallelcluster-ui&templateURL=https://parallelcluster-ui-release-artifacts-us-east-1.s3.us-east-1.amazonaws.com/parallelcluster-ui.yaml")
   - [us-west-1](https://us-west-1.console.aws.amazon.com/cloudformation/home?region=us-west-1#/stacks/create/review?stackName=parallelcluster-ui&templateURL=https://parallelcluster-ui-release-artifacts-us-east-1.s3.us-east-1.amazonaws.com/parallelcluster-ui.yaml "https://us-west-1.console.aws.amazon.com/cloudformation/home?region=us-west-1#/stacks/create/review?stackName=parallelcluster-ui&templateURL=https://parallelcluster-ui-release-artifacts-us-east-1.s3.us-east-1.amazonaws.com/parallelcluster-ui.yaml")
   - [us-west-2](https://us-west-2.console.aws.amazon.com/cloudformation/home?region=us-west-2#/stacks/create/review?stackName=parallelcluster-ui&templateURL=https://parallelcluster-ui-release-artifacts-us-east-1.s3.us-east-1.amazonaws.com/parallelcluster-ui.yaml "https://us-west-2.console.aws.amazon.com/cloudformation/home?region=us-west-2#/stacks/create/review?stackName=parallelcluster-ui&templateURL=https://parallelcluster-ui-release-artifacts-us-east-1.s3.us-east-1.amazonaws.com/parallelcluster-ui.yaml")
   - [eu-west-1](https://eu-west-1.console.aws.amazon.com/cloudformation/home?region=eu-west-1#/stacks/create/review?stackName=parallelcluster-ui&templateURL=https://parallelcluster-ui-release-artifacts-us-east-1.s3.us-east-1.amazonaws.com/parallelcluster-ui.yaml "https://eu-west-1.console.aws.amazon.com/cloudformation/home?region=eu-west-1#/stacks/create/review?stackName=parallelcluster-ui&templateURL=https://parallelcluster-ui-release-artifacts-us-east-1.s3.us-east-1.amazonaws.com/parallelcluster-ui.yaml")
   - [eu-west-2](https://eu-west-2.console.aws.amazon.com/cloudformation/home?region=eu-west-2#/stacks/create/review?stackName=parallelcluster-ui&templateURL=https://parallelcluster-ui-release-artifacts-us-east-1.s3.us-east-1.amazonaws.com/parallelcluster-ui.yaml "https://eu-west-2.console.aws.amazon.com/cloudformation/home?region=eu-west-2#/stacks/create/review?stackName=parallelcluster-ui&templateURL=https://parallelcluster-ui-release-artifacts-us-east-1.s3.us-east-1.amazonaws.com/parallelcluster-ui.yaml")
   - [eu-west-3](https://eu-west-3.console.aws.amazon.com/cloudformation/home?region=eu-west-3#/stacks/create/review?stackName=parallelcluster-ui&templateURL=https://parallelcluster-ui-release-artifacts-us-east-1.s3.us-east-1.amazonaws.com/parallelcluster-ui.yaml "https://eu-west-3.console.aws.amazon.com/cloudformation/home?region=eu-west-3#/stacks/create/review?stackName=parallelcluster-ui&templateURL=https://parallelcluster-ui-release-artifacts-us-east-1.s3.us-east-1.amazonaws.com/parallelcluster-ui.yaml")
   - [eu-central-1](https://eu-central-1.console.aws.amazon.com/cloudformation/home?region=eu-central-1#/stacks/create/review?stackName=parallelcluster-ui&templateURL=https://parallelcluster-ui-release-artifacts-us-east-1.s3.us-east-1.amazonaws.com/parallelcluster-ui.yaml "https://eu-central-1.console.aws.amazon.com/cloudformation/home?region=eu-central-1#/stacks/create/review?stackName=parallelcluster-ui&templateURL=https://parallelcluster-ui-release-artifacts-us-east-1.s3.us-east-1.amazonaws.com/parallelcluster-ui.yaml")
   - [eu-north-1](https://eu-north-1.console.aws.amazon.com/cloudformation/home?region=eu-north-1#/stacks/create/review?stackName=parallelcluster-ui&templateURL=https://parallelcluster-ui-release-artifacts-us-east-1.s3.us-east-1.amazonaws.com/parallelcluster-ui.yaml "https://eu-north-1.console.aws.amazon.com/cloudformation/home?region=eu-north-1#/stacks/create/review?stackName=parallelcluster-ui&templateURL=https://parallelcluster-ui-release-artifacts-us-east-1.s3.us-east-1.amazonaws.com/parallelcluster-ui.yaml")
   - [me-south-1](https://me-south-1.console.aws.amazon.com/cloudformation/home?region=me-south-1#/stacks/create/review?stackName=parallelcluster-ui&templateURL=https://parallelcluster-ui-release-artifacts-us-east-1.s3.us-east-1.amazonaws.com/parallelcluster-ui.yaml "https://me-south-1.console.aws.amazon.com/cloudformation/home?region=me-south-1#/stacks/create/review?stackName=parallelcluster-ui&templateURL=https://parallelcluster-ui-release-artifacts-us-east-1.s3.us-east-1.amazonaws.com/parallelcluster-ui.yaml")
   - [sa-east-1](https://sa-east-1.console.aws.amazon.com/cloudformation/home?region=sa-east-1#/stacks/create/review?stackName=parallelcluster-ui&templateURL=https://parallelcluster-ui-release-artifacts-us-east-1.s3.us-east-1.amazonaws.com/parallelcluster-ui.yaml "https://sa-east-1.console.aws.amazon.com/cloudformation/home?region=sa-east-1#/stacks/create/review?stackName=parallelcluster-ui&templateURL=https://parallelcluster-ui-release-artifacts-us-east-1.s3.us-east-1.amazonaws.com/parallelcluster-ui.yaml")
   - [ca-central-1](https://ca-central-1.console.aws.amazon.com/cloudformation/home?region=ca-central-1#/stacks/create/review?stackName=parallelcluster-ui&templateURL=https://parallelcluster-ui-release-artifacts-us-east-1.s3.us-east-1.amazonaws.com/parallelcluster-ui.yaml "https://ca-central-1.console.aws.amazon.com/cloudformation/home?region=ca-central-1#/stacks/create/review?stackName=parallelcluster-ui&templateURL=https://parallelcluster-ui-release-artifacts-us-east-1.s3.us-east-1.amazonaws.com/parallelcluster-ui.yaml")
   - [ap-northeast-1](https://ap-northeast-1.console.aws.amazon.com/cloudformation/home?region=ap-northeast-1#/stacks/create/review?stackName=parallelcluster-ui&templateURL=https://parallelcluster-ui-release-artifacts-us-east-1.s3.us-east-1.amazonaws.com/parallelcluster-ui.yaml "https://ap-northeast-1.console.aws.amazon.com/cloudformation/home?region=ap-northeast-1#/stacks/create/review?stackName=parallelcluster-ui&templateURL=https://parallelcluster-ui-release-artifacts-us-east-1.s3.us-east-1.amazonaws.com/parallelcluster-ui.yaml")
   - [ap-northeast-2](https://ap-northeast-2.console.aws.amazon.com/cloudformation/home?region=ap-northeast-2#/stacks/create/review?stackName=parallelcluster-ui&templateURL=https://parallelcluster-ui-release-artifacts-us-east-1.s3.us-east-1.amazonaws.com/parallelcluster-ui.yaml "https://ap-northeast-2.console.aws.amazon.com/cloudformation/home?region=ap-northeast-2#/stacks/create/review?stackName=parallelcluster-ui&templateURL=https://parallelcluster-ui-release-artifacts-us-east-1.s3.us-east-1.amazonaws.com/parallelcluster-ui.yaml")
   - [ap-south-1](https://ap-south-1.console.aws.amazon.com/cloudformation/home?region=ap-south-1#/stacks/create/review?stackName=parallelcluster-ui&templateURL=https://parallelcluster-ui-release-artifacts-us-east-1.s3.us-east-1.amazonaws.com/parallelcluster-ui.yaml "https://ap-south-1.console.aws.amazon.com/cloudformation/home?region=ap-south-1#/stacks/create/review?stackName=parallelcluster-ui&templateURL=https://parallelcluster-ui-release-artifacts-us-east-1.s3.us-east-1.amazonaws.com/parallelcluster-ui.yaml")
   - [ap-southeast-1](https://ap-southeast-1.console.aws.amazon.com/cloudformation/home?region=ap-southeast-1#/stacks/create/review?stackName=parallelcluster-ui&templateURL=https://parallelcluster-ui-release-artifacts-us-east-1.s3.us-east-1.amazonaws.com/parallelcluster-ui.yaml "https://ap-southeast-1.console.aws.amazon.com/cloudformation/home?region=ap-southeast-1#/stacks/create/review?stackName=parallelcluster-ui&templateURL=https://parallelcluster-ui-release-artifacts-us-east-1.s3.us-east-1.amazonaws.com/parallelcluster-ui.yaml")
   - [ap-southeast-2](https://ap-southeast-2.console.aws.amazon.com/cloudformation/home?region=ap-southeast-2#/stacks/create/review?stackName=parallelcluster-ui&templateURL=https://parallelcluster-ui-release-artifacts-us-east-1.s3.us-east-1.amazonaws.com/parallelcluster-ui.yaml "https://ap-southeast-2.console.aws.amazon.com/cloudformation/home?region=ap-southeast-2#/stacks/create/review?stackName=parallelcluster-ui&templateURL=https://parallelcluster-ui-release-artifacts-us-east-1.s3.us-east-1.amazonaws.com/parallelcluster-ui.yaml")
   - [us-gov-west-1](https://console.amazonaws-us-gov.com/cloudformation/home?region=us-gov-west-1#/stacks/create/review?stackName=parallelcluster-ui&templateURL=https://parallelcluster-ui-release-artifacts-us-east-1.s3.us-east-1.amazonaws.com/parallelcluster-ui.yaml "https://console.amazonaws-us-gov.com/cloudformation/home?region=us-gov-west-1#/stacks/create/review?stackName=parallelcluster-ui&templateURL=https://parallelcluster-ui-release-artifacts-us-east-1.s3.us-east-1.amazonaws.com/parallelcluster-ui.yaml")

3. Enter a valid email address for **Admin's Email** and a
   **ParallelCluster version**.

After deployment completes successfully, the PCUI will send a temporary password to this email address that you can use
to access the PCUI. If you delete the email before you save or use the temporary password, you must delete the stack and reinstall the
PCUI. 4. Keep the rest of the form blank or enter values for (optional) parameters to customize the PCUI build. 5. Note the stack name for use in later steps. 6. Navigate to **Capabilities**. Agree to the CloudFormation capabilities. 7. Choose **Create**. It takes about 15 minutes to complete the AWS ParallelCluster API and PCUI deployment. 8. View the stack details as the stack is created. 9. After the deployment completes, open the admin email that was sent to the address you entered and that contains the temporary password. Use that
to access the PCUI. (Remember, if you permanently delete the email before you log in to the PCUI, you must delete the PCUI stack you
created and reinstall the PCUI. 10. In the CloudFormation console list of stacks, choose the link to the stack name that you noted in a previous step. 11. In **Stack details**, choose **Outputs** and select the link for the key named **`Stackname`URL** to
open the PCUI (where **`Stackname`** is the name
that you noted in a previous step). 12. Enter the temporary password. Follow the steps to create your own password and log in again. 13. You are now on the home page of the PCUI in the AWS Region that you selected. 14. To get started using the PCUI, see [Configure and create a cluster with the
PCUI](configure-create-pcui-v3.md "configure-create-pcui-v3.md").

###### Note

PCUI sessions have a default duration of 5 minutes, which is the minimum value provided by Cognito as of PCUI 2023.12.0. So,
it is expected that a user removed from Cognito User Pools will still able to access the system until the session expires.

## Stack parameters

**AdditionalPoliciesPCAPI:**

Description: (Optional) ARN of the additional IAM policy to be attached to the default
execution role for the ParallelCluster Lambda function. Only one policy can be specified.

Type: String

Default: ''

AllowedPattern: "^(arn:.\*:iam::.\*:policy\\/([a-zA-Z0-9\_-]+))|()$"

**AdminUserEmail:**

Description: Email address of administrative user to setup by default (only with new Cognito
instances).

Type: String

Default: ''

**CognitoCustomDomain:**

Description: (Optional) Custom domain name for Cognito. If omitted, the default Cognito domain
name will be used.

Type: String

Default: ''

**CognitoCustomDomainCertificateArn:**

Description: (Optional) ARN of the ACM Certificate issued for the Cognito custom domain.
This is required only if `CognitoCustomDomain` is specified.

Type: String

Default: ''

**CustomDomain:**

Description: (Optional) Custom domain name. If omitted, the default domain name will be used.

Type: String

Default: ''

**CustomDomainCertificateArn:**

Description: (Optional) ARN of the ACM Certificate issued for the custom domain. This is
required only if `CustomDomain` is specified.

Type: String

Default: ''

**IAMRoleAndPolicyPrefix:**

Description: Prefix applied to the name of every IAM role and policy (max length: 10).
[ParallelCluster >= 3.8.0]

Type: String

Default: ''

MaxLength: 10

**ImageBuilderSubnetId:**

Description: (Optional) Select the subnet to use for building the container images.
The subnet must be public and auto-assign public IPs. If not selected, the default Subnet
will be used.

Type: String

Default: ''

**ImageBuilderVpcId:**

Description: (Optional) Select the VPC to use for building the container images. If not
selected, the default VPC will be used.

Type: String

Default: ''

**InfrastructureBucket:**

Description: (Optional) S3 bucket where CloudFormation files are stored. Change this parameter
only when testing changes made to the infrastructure itself.

Type: String

Default: ''

**LambdaSecurityGroupIds:**

Description: Comma separated list of security groups to be associated with the PCUI
Lambda function.

Type: CommaDelimitedList

Default: ''

**LambdaSubnetIds:**

Description: Comma separated list of subnet IDs to be associated with the PCUI Lambda
function. These subnets should be private and associated with your VPC endpoint.

Type: CommaDelimitedList

Default: ''

**PermissionsBoundaryPolicy:**

Description: ARN of the IAM policy to use as permissions boundary for every IAM role created
by ParallelCluster UI infrastructure.'

Type: String

Default: ''

AllowedPattern: "^(arn:.\*:iam::.\*:policy\\/([a-zA-Z0-9\_-]+))|()$"

**PermissionsBoundaryPolicyPCAPI:**

Description: ARN of the IAM policy to use as permissions boundary for every IAM role
created by ParallelCluster API infrastructure. [ParallelCluster >= 3.8.0]

Type: String

Default: ''

AllowedPattern: "^(arn:.\*:iam::.\*:policy\\/([a-zA-Z0-9\_-]+))|()$"

**PublicEcrImageUri:**

Description: When specified, the URI of the Docker image for the Lambda of the ParallelCluster
UI container.

Type: String

Default: public.ecr.aws/pcm/parallelcluster-ui:2024.11.0

**SNSRole:**

Description: SNSRole ARN of a previously deployed PCUI Cognito Stack. Leave blank to
create a new one.

Type: String

Default: ''

**UserPoolAuthDomain:**

Description: UserPoolAuthDomain of a previously deployed PCUI Cognito User Pool. Leave
blank to create a new one.

Type: String

Default: ''

**UserPoolId:**

Description: UserPoolId of a previously deployed PCUI Cognito User Pool. Leave blank
to create a new one.

Type: String

Default: ''

**Version:**

Description: Version of AWS ParallelCluster to deploy.

Type: String

Default: 3.11.1

**VpcEndpointId:**

Description: Enter a VPC endpoint with type interface for the execute-api service to enable
private PCUI implementation. When enabled, the API will only accept requests from within the
given VPC.

Type: String

Default: ''
