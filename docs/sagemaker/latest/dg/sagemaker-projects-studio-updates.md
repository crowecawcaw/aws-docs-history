# Granting SageMaker Studio Permissions

Required to Use
Projects

The Amazon SageMaker Studio (or Studio Classic) administrator and Studio (or Studio Classic) users that you add to your domain can view
project templates provided by SageMaker AI and create projects with those templates.
By default, the administrator can view the SageMaker AI templates in the Service Catalog console.
The administrator can see what another user creates if the user has permission
to use SageMaker Projects. The administrator can also view the AWS CloudFormation template that the SageMaker AI project
templates define in the Service Catalog console. For information about using the Service Catalog
console, see [What Is
Service Catalog](../../../servicecatalog/latest/adminguide/introduction.md "../../../servicecatalog/latest/adminguide/introduction.md") in the _Service Catalog User Guide_.

Studio (and Studio Classic) users of the domain who are configured to use the same
execution role as the domain by default have permission to create projects using SageMaker AI
project templates.

###### Important

Do not manually create your roles. Always create roles through **Studio Settings**
using the steps described in the following procedure.

For users who use any role other than the domain's execution role to view and use
SageMaker AI-provided project templates, you need to grant **Projects**
permissions to the individual user profiles by turning on **Enable Amazon SageMaker AI
project templates and Amazon SageMaker JumpStart** for Studio users when you
add them to your domain. For more information about this step, see [Add user profiles](domain-user-profile-add.md "domain-user-profile-add.md").

Since SageMaker Projects is backed by Service Catalog, you must add each role that requires access to
SageMaker Projects to the **Amazon SageMaker AI Solutions and ML Ops products**
Portfolio in the service catalog. You can do this in the **Groups, roles, and
users** tab, as shown in the following image. If each user profile in
Studio Classic has a different role, you should add each of those roles to the service
catalog. You can also do this while creating a user profile in Studio Classic.

## Grant new domain roles access to projects

When you change your domain's execution role or add user profiles with different roles,
you must grant these new roles access to the Service Catalog portfolio to use SageMaker Projects.
Follow these steps to ensure all roles have the necessary permissions:

###### To grant new domain roles access to projects

1. Open the [Service Catalog console](https://console.aws.amazon.com/servicecatalog/ "https://console.aws.amazon.com/servicecatalog/").
2. In the left navigation menu, choose **Portfolios**.
3. Select the **Imported** section.
4. Select **Amazon SageMaker Solutions and ML Ops products**.
5. Choose the **Access** tab.
6. Choose **Grant access**.
7. In the **Grant access** dialog, select **Roles**.
8. Grant access for all roles that are used by the domain's user profiles, including:
   - The domain's execution role
   - Any custom execution roles assigned to individual user profiles

9. Choose **Grant access** to confirm.

###### Important

You must complete this process whenever you change your domain's execution role
or add user profiles with new execution roles. Without this access, users will not
be able to create or use SageMaker Projects.

The following procedures show how to grant **Projects** permissions
after you onboard to Studio or Studio Classic. For more information about onboarding to
Studio or Studio Classic, see [Amazon SageMaker AI domain overview](gs-studio-onboard.md "gs-studio-onboard.md").

###### To confirm that your SageMaker AI Domain has active project template permissions:

1. Open the [SageMaker AI console](https://console.aws.amazon.com/sagemaker/ "https://console.aws.amazon.com/sagemaker/").
2. On the left navigation pane, choose **Admin configurations**.
3. Under **Admin configurations**, choose **domains**.
4. Select your domain.
5. Choose the **Domain Settings** tab.
6. Under **SageMaker Projects and JumpStart**, make sure the
   following options are turned on:
   - **Enable Amazon SageMaker AI project templates and Amazon SageMaker JumpStart
     for this account**
   - **Enable Amazon SageMaker AI project templates and Amazon SageMaker JumpStart
     for Studio users**

###### To view a list of your roles:

1. Open the [SageMaker AI console](https://console.aws.amazon.com/sagemaker/ "https://console.aws.amazon.com/sagemaker/").
2. On the left navigation pane, choose **Admin configurations**.
3. Under **Admin configurations**, choose **domains**.
4. Select your domain.
5. Choose the **Domain Settings** tab.
6. A list of your roles appears in the `Apps` card under the **Studio** tab.

###### Important

As of July 25, we require additional roles to use project templates. Here is the complete
list of roles you should see under `Projects`:

`AmazonSageMakerServiceCatalogProductsLaunchRole`
`AmazonSageMakerServiceCatalogProductsUseRole`
`AmazonSageMakerServiceCatalogProductsApiGatewayRole`
`AmazonSageMakerServiceCatalogProductsCloudformationRole`
`AmazonSageMakerServiceCatalogProductsCodeBuildRole`
`AmazonSageMakerServiceCatalogProductsCodePipelineRole`
`AmazonSageMakerServiceCatalogProductsEventsRole`
`AmazonSageMakerServiceCatalogProductsFirehoseRole`
`AmazonSageMakerServiceCatalogProductsGlueRole`
`AmazonSageMakerServiceCatalogProductsLambdaRole`
`AmazonSageMakerServiceCatalogProductsExecutionRole`

For descriptions of these roles, see [AWS Managed Policies for SageMaker Projects and JumpStart](security-iam-awsmanpol-sc.md "security-iam-awsmanpol-sc.md").
