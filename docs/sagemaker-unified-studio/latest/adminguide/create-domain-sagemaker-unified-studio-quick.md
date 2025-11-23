# Create a Amazon SageMaker Unified Studio domain -

quick setup

Complete the following procedure to create an Amazon SageMaker unified domain with the
Quick setup option.

###### Important

Note that there is an additional charge for any VPC or resources that AWS sets up if
you chose the Quick setup option for domain creation. The Quick setup option is intended
for testing purposes and we recommend deleting the domain after initial tests.

1. Navigate to the Amazon SageMaker management console at [https://console.aws.amazon.com/datazone](https://console.aws.amazon.com/datazone "https://console.aws.amazon.com/datazone") and use the region selector in the
   top navigation bar to choose the appropriate AWS Region.
2. Choose **Create a Unified Studio domain** and then choose
   **Quick setup**.

With this option, you're choosing to create an Amazon SageMaker unified domain and
you're letting Amazon SageMaker Unified Studio configure your domain with the following default capabilities
that you can customize later:

    * Data analytics, machine learning, SQL, and generative AI
    * Data and AI governance
    * Generative AI app development using Amazon Bedrock serverless models
    * Amazon Q - Free tier
    * Authentication via AWS IAM or AWS IAM Identity Center

3. If you see the following note **No VPC has been specifically set up for use
   with Amazon SageMaker Unified Studio**, you can use the **Choose
   VPC** or **Create VPC** buttons to **Create a new
   VPC (recommended)** or choose an existing properly-configured VPC.

If you plan to choose your own VPC, Amazon SageMaker Unified Studio enables you to
choose VPCs within the same account as well as shared VPCs from other member accounts of
the AWS organization. For more information, see [Share your VPC
subnets with other accounts](../../../vpc/latest/userguide/vpc-sharing.md "../../../vpc/latest/userguide/vpc-sharing.md").

###### Note

If you choose to create a new VPC, note that the VPC template with which it is
created is not intended for production use. You can use this template as a start and
modify it for your organization's purposes.

If you see the following note **No models accessible**, you can use
the **Grant model access** button to grant access to Amazon Bedrock
serverless models for use in Amazon SageMaker Unified Studio. 4. Expand the **Quick setup settings** section and review the selected
configurations, including domain name, domain execution role, domain service role, and
domain data encryption information under **Domain resources**, user
role policy, provisioning role, manage access role, Amazon S3 bucket for projects, and
Virtual private cloud (VPC) information under **Data analytics, machine
learning, and SQL analytics resources**, and the model provisioning role and
model consumption role under **Generative AI resources**. Modify as
needed or leave the defaults, and then choose **Continue**. 5. Expand the **Onboard your data - optional** section and review the
selected configuration. This allows you to make your existing AWS data available and
ready for use in Amazon SageMaker Unified Studio. You can specify where you data is stored - in the current
release, AWS Glue (SageMaker Lakehouse) is supported, make your data discoverable by
other users in the domain, and note the owner project that is auto-created for you and
where this onboarded data will be accessible in Amazon SageMaker Unified Studio. For more information, see
[Onboarding data in Amazon SageMaker Unified Studio](data-onboarding.md "data-onboarding.md"). 6. On the **Create IAM Identity Center user** page, create an SSO user
(account with IAM Identity Center) or select an existing SSO user to log in to the
Amazon SageMaker Unified Studio. IAM roles that create the Amazon SageMaker unified domains cannot log in to
the Amazon SageMaker Unified Studio. The SSO selected here is used as the administrator in the
Amazon SageMaker Unified Studio. 7. Choose **Create domain**.
