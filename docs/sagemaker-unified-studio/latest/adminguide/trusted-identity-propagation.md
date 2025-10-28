# Trusted identity propagation

Trusted identity propagation in IAM Identity Center enables administrators of AWS
services to grant permissions based on user attributes, such as user ID or group associations.
With trusted identity propagation, identity context is added to an IAM role to identify the
user requesting access to AWS resources. This context is propagated to other AWS services.

Starting on 9/30/2025, Amazon SageMaker Unified Studio supports trusted identity propagation for tasks
that include Amazon Athena, Amazon Redshift, AWS Glue, Amazon EMR on EC2, and Amazon EMR Serverless. To enable trusted identity propagation within your Amazon SageMaker
unified domains, you can do either of the following:

- [Create a new Amazon
  SageMaker unified domain](create-domain-sagemaker-unified-studio-manual.md "create-domain-sagemaker-unified-studio-manual.md") - from 9/30/2025 and beyond, all newly created Amazon
  SageMaker unified domains support trusted identity propagation with IdC for tasks
  that include Amazon Athena, Amazon Redshift, AWS Glue, Amazon EMR on EC2, and Amazon EMR Serverless. Other than creating a new domain, no
  further action is required from the administrator to configure trusted identity
  propagation for their new
  domain.
- Update your existing Amazon SageMaker unified domain - if your domain was created
  prior to 9/30/2025, navigate to your domain's details page and locate the update notification banner. To update your domain to support Trusted Identity
  Propagation in AWS Glue, Amazon EMR on EC2, and Amazon EMR Serverless as well as Amazon Athena and Amazon Redshift, choose the **Update
  now** button.
  Once this update is complete, you must set the
  `enableTrustedIdentityPropagationPermissions` property in your project profile's
  default Tooling blueprint To do this, complete the following procedure:

1. Navigate to the Amazon SageMaker management console at [https://console.aws.amazon.com/datazone](https://console.aws.amazon.com/datazone "https://console.aws.amazon.com/datazone") and use the region selector in the top
   navigation bar to choose the appropriate AWS Region.
2. Choose the domain that contains the project profile whose Tooling blueprint you want
   to update.
3. Choose the **Project profiles** tab and then choose the project
   profile that you want to update.
4. In the project profile details page, choose **Edit**.
5. On the project profile's edit page, in the **Tooling blueprint
   parameters** section, choose the
   **enableTrustedIdentityPropagationPermissions** parameter and then
   choose **Edit**.
6. On the **Edit blueprint parameter** page, set the
   **enableTrustedIdentityPropagationPermissions** parameter value to
   **True**.
7. Optional - to enforce authorization based on trusted identity propagation identity,
   you can make the **enableTrustedIdentityPropagationPermissions**
   parameter non-editable by unchecking the **Editable** checkbox under
   **Editable value**.
8. Choose **Save** in the **Edit blueprint parameter**
   page.

###### Important

In the current release, trusted identity propagation within Amazon SageMaker unified
domains is only supported for SQL analytics,
interactive Spark sessions, and end-to-end machine learning lifecycle tasks with Amazon Athena, Amazon Redshift, AWS Glue, Amazon EMR on EC2, and Amazon EMR Serverless.
Therefore, even though you can set the "enableTrustedIdentityPropagationPermissions"
parameter value to "True" in the Tooling blueprint of any of your project profiles, such as
All capabilities, Generative AI application development, SQL analytics, or any custom
project profile, trusted identity propagation and authorization based on Trusted Identity
Propagation is only supported for the Amazon Athena, Amazon Redshift, AWS Glue, Amazon EMR on EC2, and Amazon EMR Serverless tools within the
chosen project profile.

We recommend creating a dedicated project profile for trusted identity propagation
supported tools and setting enableTrustedIdentityPropagationPermissions to True. This
approach clearly establishes trusted identity propagation as the data authorization method
for all projects using this profile.
