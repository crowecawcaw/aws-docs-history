# Setting up Amazon SageMaker

Complete the following tasks to set up Amazon SageMaker.

###### Topics

- [Step 1 - Create an Amazon SageMaker unified domain](#create-domain "#create-domain")
- [Step 2 - Create a new project](#create-new-project "#create-new-project")

## Step 1 - Create an Amazon SageMaker unified domain

Complete the following procedure to create an Amazon SageMaker unified domain with the Quick
setup option.

###### Important

Note that there is an additional charge for any VPC or resources that AWS sets up if you
chose the Quick setup option for domain creation.

1. Navigate to the Amazon SageMaker management console at [https://console.aws.amazon.com/datazone](https://console.aws.amazon.com/datazone "https://console.aws.amazon.com/datazone")
   and use the region selector in the top navigation bar to choose the appropriate AWS
   Region.
2. Choose **Create a Unified Studio domain** and then choose **Quick
   setup**.

With this option, you're choosing to create an Amazon SageMaker unified domain and you're
letting Amazon SageMaker configure your domain with the following default capabilities that you can
customize later:

    * Data analytics, machine learning, SQL, and generative AI
    * Data and AI governance
    * Generative AI app development using Amazon Bedrock serverless models
    * Amazon Q - Free tier
    * Authentication via AWS IAM or AWS IAM Identity Center

3. If you see the following note **No VPC has been specifically set up for use with
   Amazon SageMaker Unified Studio**, you can use the **Choose VPC** or
   **Create VPC** buttons to **Create a new VPC (recommended)**
   or choose an existing properly-configured VPC.

If you plan to choose your own VPC, Amazon SageMaker Unified Studio enables you to choose
VPCs within the same account as well as shared VPCs from other member accounts of the AWS
organization. For more information, see [Share your VPC subnets
with other accounts](../../../vpc/latest/userguide/vpc-sharing.md "../../../vpc/latest/userguide/vpc-sharing.md").

###### Note

If you choose to create a new VPC, note that the VPC template with which it is created is
not intended for production use. You can use this template as a start and modify it for your
organization’s purposes. 4. If you see the following note **No models accessible**, you can use the
**Grant model access** button to grant access to Amazon Bedrock serverless
models for use in Amazon SageMaker. 5. Expand the **Quick setup settings** section and review the
specified configurations for the domain. Leave these defaults and then choose **Continue** to
proceed with creating your domain.

###### Note

For more information, see [IAM roles for Amazon SageMaker Unified Studio](../../../sagemaker-unified-studio/latest/adminguide/security-iam-roles.md "../../../sagemaker-unified-studio/latest/adminguide/security-iam-roles.md"). 6. On the **Create IAM Identity Center user** page, create a new or select
an existing SSO user that you want to enable to log in to Amazon SageMaker Unified Studio. This
is done because IAM roles that are used to create Amazon SageMaker unified domains cannot log
in to Amazon SageMaker Unified Studio. The SSO user specified here is used as the administrator
in Amazon SageMaker Unified Studio. 7. Choose **Create domain**.

After some time, an email will be sent to the address you provided as part of the IAM Identity Center user setup.
The email will prompt you to set a password that you can use to access the domain.

## Step 2 - Create a new project

In Amazon SageMaker, projects enable a group of users to collaborate on various business use cases.
Within projects, you can manage data assets in the Amazon SageMaker catalog, perform data analysis,
organize workflows, develop machine learning models, build generative AI apps, and more.

### Navigate to Amazon SageMaker Unified Studio

To begin creating a project, navigate to Amazon SageMaker Unified Studio.
You can do this by using the link in your email that you used to set an IAM Identity Center password,
or by selecting the domain in the Amazon SageMaker management console and choosing **Open unified studio**.

Sign in using your SSO credentials that you configured using the email from IAM Identity Center.

If your IAM Identity Center is configured to require
multi-factor authentication (MFA), set up and use an MFA device. Follow
the instructions on the screen to register or use an MFA device as
needed, or contact your admin for support. For more information about configuring
MFA device enforcement, see [Configure MFA device enforcement](../../../singlesignon/latest/userguide/how-to-configure-mfa-device-enforcement.md "../../../singlesignon/latest/userguide/how-to-configure-mfa-device-enforcement.md") in the IAM Identity
Center User Guide.

### Project name and description

After navigating to Amazon SageMaker Unified Studio, choose
**Create project**.

The project name and description includes the following fields:

- Project name - the name of your project. Enter a name here. The name of the project can
  not be edited after the project is created.
- Description - an optional description of your project. You can edit this later.
- Project profile - project profiles define which resources and tools should be provisioned
  in the project. These include tools and compute resources for SQL, data science, data
  engineering, and machine learning development. Project profiles can include resources and
  tools from Amazon Redshift, Amazon SageMaker AI, and other AWS services. To
  complete the use cases in this getting started guide, choose the **All
  capabilities** project profile.

Choose **Continue** to review parameters.

### Review parameters

On the next page of project creation, you can review and optionally edit the names and
values for different resources that are created when the project is created. You can leave all
the defaults and then choose **Continue**.

### Review

Use the last page of project creation to review the configurations you have selected. When
everything is configured as desired on the project creation review page, choose **Create
project**.

You are then redirected to the project home page. The project will start building and a
progress bar will appear with the status.
