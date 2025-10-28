# Launch a Solution

###### Important

As of November 30, 2023, the previous Amazon SageMaker Studio experience is now named
Amazon SageMaker Studio Classic. The following section is specific to using the Studio Classic application. For
information about using the updated Studio experience, see [Amazon SageMaker Studio](studio-updated.md "studio-updated.md").

Studio Classic is still maintained for existing
workloads but is no longer available for onboarding. You can only stop or delete existing Studio Classic
applications and cannot create new ones. We recommend that you [migrate your workload to the new Studio experience](studio-updated-migrate.md "studio-updated-migrate.md").

###### Note

JumpStart Solutions are only available in Studio Classic.

First, choose a solution through the SageMaker JumpStart landing page in the Amazon SageMaker Studio Classic
UI. For information on the onboarding steps to sign in to Amazon SageMaker Studio Classic, see [Onboard to
Amazon SageMaker AI domain](gs-studio-onboard.md "gs-studio-onboard.md"). For details on getting to the SageMaker JumpStart landing page, see
[Open and use JumpStart in Studio Classic](studio-jumpstart.md#jumpstart-open-use "studio-jumpstart.md#jumpstart-open-use").

After you choose a solution, a solution's tab opens showing a description of the
solution and a `Launch` button. To launch a solution, select `Launch`
in the **Launch Solution** section. JumpStart then creates all of the
resources needed to run the solution. This includes training and model hosting instances.

## Advanced parameters

The solution that you choose may have advanced parameters that you can select. Choose
**Advanced Parameters** to specify the AWS Identity and Access Management role for the solution.

Solutions are able to launch resources across 9 AWS services that interact with each
other. For the solution to work as expected, newly created components from one service
must be able to act on newly created components from another service. We recommend that
you use the default IAM role to ensure that all needed permissions are added. For more
information about IAM roles, see [AWS Identity and Access Management for Amazon SageMaker AI](security-iam.md "security-iam.md").

**Default IAM role**

If you select this option, the default IAM roles that are required by this solution
are used. Each solution requires different resources. The following list describes the
default roles that are used for the solutions based on the service needed. For a
description of the permissions required for each service, see [AWS Managed Policies for SageMaker Projects and JumpStart](security-iam-awsmanpol-sc.md "security-iam-awsmanpol-sc.md").

- API Gateway –
  AmazonSageMakerServiceCatalogProductsApiGatewayRole
- CloudFormation –
  AmazonSageMakerServiceCatalogProductsCloudformationRole
- CodeBuild –
  AmazonSageMakerServiceCatalogProductsCodeBuildRole
- CodePipeline –
  AmazonSageMakerServiceCatalogProductsCodePipelineRole
- Events –
  AmazonSageMakerServiceCatalogProductsEventsRole
- Firehose –
  AmazonSageMakerServiceCatalogProductsFirehoseRole
- Glue –
  AmazonSageMakerServiceCatalogProductsGlueRole
- Lambda –
  AmazonSageMakerServiceCatalogProductsLambdaRole
- SageMaker AI –
  AmazonSageMakerServiceCatalogProductsExecutionRole

If you are using a new SageMaker AI domain with JumpStart project templates enabled, these
roles are automatically created in your account.

If you are using an existing SageMaker AI domain, these roles may not exist in your account.
If this is the case, you will receive the following error when launching the solution.

```
Unable to locate the updated roles required to launch this solution, a general role '/service-role/AmazonSageMakerServiceCatalogProductsUseRole' will be used. Please update your studio domain to generate these roles.
```

You can still launch a solution without the needed role, but the legacy default role
`AmazonSageMakerServiceCatalogProductsUseRole` is used in place of the needed
role. The legacy default role has trust relationships with all of the services that
JumpStart solutions need to interact with. For the best security, we recommend that you
update your domain to have the newly created default roles for each AWS service.

If you have already onboarded to a SageMaker AI domain, you can update your domain to generate
the default roles using the following procedure.

1. Open the Amazon SageMaker AI console at [https://console.aws.amazon.com/sagemaker/](https://console.aws.amazon.com/sagemaker/ "https://console.aws.amazon.com/sagemaker/").
2. Choose **Control Panel** at the top left of the page.
3. From the **domain** page, choose the
   **Settings** icon (
   ![Black square icon representing a placeholder or empty image.](images/icons/Settings_squid.png)
   ) to edit the domain settings.
4. On **General Settings** choose **Next**.
5. Under **SageMaker Projects and JumpStart**, select **Enable
   Amazon SageMaker project templates and Amazon SageMaker JumpStart for this account** and
   **Enable Amazon SageMaker project templates and Amazon SageMaker JumpStart for Studio Classic
   users**, choose **Next**.
6. Select **Submit**.

You should be able to see the default roles listed in **Projects - Amazon SageMaker
project templates enabled for this account** under the **Apps -
Studio** tab.

**Find IAM role**

If you select this option, you must select an existing IAM role from the dropdown
list for each of the required services. The selected role must have at least the minimum
permissions required for the corresponding service. For a description of the permissions
required for each service, see [AWS Managed Policies for SageMaker Projects and JumpStart](security-iam-awsmanpol-sc.md "security-iam-awsmanpol-sc.md").

**Input IAM role**

If you select this option, you must manually enter the ARN for an existing IAM role.
The selected role must have at least the minimum permissions required for the
corresponding service. For a description of the permissions required for each service, see
[AWS Managed Policies for SageMaker Projects and JumpStart](security-iam-awsmanpol-sc.md "security-iam-awsmanpol-sc.md").
