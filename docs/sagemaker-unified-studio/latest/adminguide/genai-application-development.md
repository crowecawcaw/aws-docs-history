# Generative AI application development project

profile

A Generative AI application development project profile enables generative AI solutions
from Amazon Bedrock for your Amazon SageMaker unified domains. It provides project users in
Amazon SageMaker Unified Studio with the access to the following generative AI tools: Bedrock Chat Agents, Bedrock
Knowledge Bases, Bedrock Guardrails, Bedrock Functions, Bedrock Flows, Bedrock Prompts, and
Bedrock Evaluations.

You can complete either of the following procedures to create a Generative API application
development project profile in an Amazon Sagemaker unified domain.

###### Topics

- [Configure Amazon Bedrock in SageMaker Unified Studio
  for your domain](#configure-bedrock-ide "#configure-bedrock-ide")
- [Create a generative
  AI application development project profile](#create-genai-application-development-project-profile "#create-genai-application-development-project-profile")

## Configure Amazon Bedrock in SageMaker Unified Studio

for your domain

Complete the following procedure to configure Amazon Bedrock in SageMaker Unified Studio
for your domain.

###### Important

In the current release of Amazon SageMaker Unified Studio, project profiles for the
domain can be created only by a domain administrator from the AWS account that owns the
domain. Completing this procedure as a user from an associated account only enables the
generative AI blueprints but it doesn't create the Generative AI application development
project profile. A domain administrator from the AWS account that owns the domain must
create the Generative AI application development project profile in the domain for the
associated accounts.

1. Navigate to the Amazon SageMaker management console at [https://console.aws.amazon.com/datazone](https://console.aws.amazon.com/datazone "https://console.aws.amazon.com/datazone") and use the region selector in the
   top navigation bar to choose the appropriate AWS Region.
2. Either create a new domain or choose an existing domain where you want to configure
   Amazon Bedrock in SageMaker Unified Studio.
3. On the domain's details page, under the **Next steps for your
   domain** section, choose the **Configure** button next to
   the **Generative AI** domain capability.
4. On the **Create project profile: Amazon Bedrock generative AI**
   page, locate the **Generative AI blueprints** section and review the
   settings.

As part of configuring Amazon Bedrock in SageMaker Unified Studio for your domain
(this procedure) you are creating the Generative AI application development project
profile and therefore you must enable the blueprints that contain the tools, resources,
and parameters that this project profile requires. The following blueprints are enabled
when you create this project profile as part of this procedure:

    * AmazonBedrockChatAgent
    * AmazonBedrockKnowledgeBase
    * AmazonBedrockGuardrail
    * AmazonBedrockFunction
    * AmazonBedrockFlow
    * AmazonBedrockPrompt
    * AmazonBedrockEvaluation

###### Important

Note that by configuring Amazon Bedrock in SageMaker Unified Studio for your
domain (this procedure), you can only enable the generative AI blueprints for this
project profile in this domain's AWS account and Region. To enable these blueprints
in an associated account, see [Configure Amazon Bedrock in SageMaker Unified Studio
in an associated account](associated-accounts.md#configure-generative-ai "associated-accounts.md#configure-generative-ai").

Under **Provisioning role**, specify a new or existing service role
that is to be used by Amazon SageMaker Unified Studio to provision and manage resources defined in the
selected blueprints in your account. 5. On the **Create project profile: Amazon Bedrock generative AI**
page, locate the **Default tooling blueprint deployment settings**
section that contains the Tooling blueprint deployment settings used to create projects
from this project profile and review them and modify the following as needed. Note that
if you have already enabled the Tooling blueprint, you cannot use this procedure to
modify any of the Tooling blueprint settings.

    * Under **Manage access** role, specify a service role that gives
     Amazon SageMaker Unified Studio the authorization to create and configure project resources using AWS
     CloudFormation in the project account and region. If this service role already
     exists in this AWS account, it is selected by default.
    * For the Tooling blueprint deployment account and region, note that by
     configuring Amazon Bedrock in SageMaker Unified Studio capability for your domain
     (this procedure), you can only enable the Tooling blueprint in the same AWS
     account and region as your domain. To enable the Tooling blueprint in an associated
     account, see [Configure Amazon Bedrock in SageMaker Unified Studio
     in an associated account](associated-accounts.md#configure-generative-ai "associated-accounts.md#configure-generative-ai").
    * In the **Amazon S3 bucket for blueprints** section, specify an
     Amazon S3 bucket for blueprints in your AWS account.
    * In the **Networking** section, in the **Virtual private
     cloud (VPC) setting**, choose a VPC in which to provision your Amazon
     SageManker unified domain. VPCs tagged with Amazon SageMaker Unified Studio should be correctly
     configured.


    In the **Subnets** section, select at least 3 subnets in
     different **Availability Zones** that contain required VPC
     Endpoints. Private subnets are recommended, not all functionality is available when
     selecting public subnets.
    * In the **Data encryption** section, your data is encrypted by
     default with a key that AWS owns and manages for you. Encryption cannot be changed
     after the domain is created. Choose either **Use AWS owned key**
     (a key that AWS owns and manages for you) or the **Choose a different
     AWS KMS key (advanced)** (a key that you have permissions to use, or
     create a new one) and then specify an existing or create a new AWS KMS key.
    * In the **User role policy** section, you have the option to
     specify your own user role policy. Amazon SageMaker Unified Studio creates IAM roles for project users to
     perform data analytics, AI, and ML actions. You can attach your own AWS IAM
     policies to the role rather than using the default system-managed policy. This
     provides more granular control over permissions but requires knowledge of IAM policy
     configuration. The IAM policy must include all necessary permissions required for
     the service to function properly.

6. On the **Create project profile: Amazon Bedrock generative AI**
   page, in the **Authorization - optional** section, specify who can use
   this project profile to create projects in all domain units. This can also be done per
   domain unit in the Amazon SageMaker Unified Studio. Choose either **Selected users and
   groups** (select which users and groups are authorized to use this project
   profile) or **Allow all users and groups** (allow any user to use this
   project profile).

###### Note

Projects do not provide strong security isolation. To limit cross-domain and
cross-project resource discovery you can consider creating projects in separate
accounts. 7. On the **Create project profile: Amazon Bedrock generative AI**
page, in the **Permissions for Bedrock model access** section, specify
the permissions for users to interact with the enabled Amazon Bedrock models. The system
can automatically create roles to control user access and interactions with these models
or you can specify existing roles.

For the **Model provisioning** role, you can create a new or use an
existing role. The system uses the role you specify as the provisioning role to create
an inference profile that has access to an Amazon Bedrock model in a project. The role
you specify here is used as the provisioning role for all the Amazon Bedrock models
enabled for this domain.

For the **Model consumption** role, you can create a new or use an
existing role. The system uses a consumption role to grant users access to Amazon
Bedrock models in the playground in Amazon SageMaker Unified Studio. 8. Choose **Next** to advance to the **Configure model
access** page. 9. On the **Configure model access** page, in the
**Models** section, you can configure access to your Amazon Bedrock
serverless models by enabling or disabling them for this domain.

The system queries Amazon Bedrock and displays a list of Amazon Bedrock serverless
models to which you have access. If no models are listed or if a specific model is
missing, visit the Amazon Bedrock management console for the appropriate account and
Region to grant access. If you have updated model access in Amazon Bedrock, choose the
refresh icon in the **Amazon Bedrock Models** tab to refresh the
updated list of accessible models

The following are important elements to consider as you review the generated list of
models:

    * Every model in the list is prepopulated with certain details, including
     modality, inference type, whether it's enabled in projects and playground, and roles
     for model access. A model's modality indicates the type of output data it can
     generate. Amazon Bedrock in SageMaker Unified Studio supports Amazon Bedrock
     foundation models with on-demand throughput and on-demand cross-region inference. If
     a model supports both on-demand and on-demand cross-region inference, it appears in
     the list twice with the appropriate value listed in the
     **Inference** column. Amazon Bedrock in SageMaker Unified Studio
     does NOT support provisioned throughput, custom models, or imported models.
    * For easy setup, the system pre-selects accessible models that support on-demand
     throughput, excluding legacy models, to enable in projects and playground. Review
     and adjust the list to enable models for projects and playgrounds based on your
     specific requirements.
    * If the model that you want to manage for your Amazon SageMaker Unified Studio users is not present in
     the list, make sure that it has been enabled for access in Amazon SageMaker Unified Studio. This is done
     in the Amazon Bedrock management console. For more information, see [Amazon Bedrock Documentation](../../../bedrock.md "../../../bedrock.md").

10. On the **Configure model access** page, in the **Default
    models - optional** section, you can set default models for the generative AI
    playgrounds in Amazon SageMaker Unified Studio.

Amazon Bedrock in SageMaker Unified Studio supports generative AI playgrounds that
enable Amazon SageMaker unified domain users to easily experiment with Amazon Bedrock
models. Users can send prompt requests to various models and view the responses. There
are two types of playgrounds in the Amazon Bedrock in SageMaker Unified Studio: the chat
playground and the image and video playground.

For the **Chat playground - optional**, select a default model from
the drop-down menu. The drop-down menu includes only the models that support
**Text** as the output modality and are enabled for playground use.

For the **Image and video playground - optional**, select a default
model from the drop-down menu. The drop-down menu will include only the models that
support either **Image** or **Video** as the output
modality and are enabled for playground use. 11. Choose **Finish** to complete configuring Amazon Bedrock in
SageMaker Unified Studio for this domain.

Once the action is successfully completed and you've finished configuring Amazon Bedrock
in SageMaker Unified Studio for this domain, you are redirected to the domain's details page
where you can find the enabled generative AI blueprints under the
**Blueprints** tab, a Generative AI project profile under the
**Project profiles** tab, and the enabled models listed in the
**Amazon Bedrock models** tab. Note, that you can manage model access
directly from **Amazon Bedrock models** tab. For more information, see
[Amazon Bedrock in SageMaker Unified Studio](amazon-bedrock.md "amazon-bedrock.md")

## Create a generative

AI application development project profile

Complete the following procedure to create a Generative AI application development
project profile for your Amazon SageMaker unified domain. Once this procedure is complete,
your Generative AI application development project profile will only include the
capabilities defined in the [Tooling blueprint](blueprints.md "blueprints.md"). To
configure the full generative AI application development capability for your Amazon
SageMaker unified domain, you must then use the **Blueprints** tab and
configure the **AmazonBedrockGenerativeAI** blueprint for this project
profile. The **AmazonBedrockGenerativeAI** blueprint contains the following
generative AI blueprints:

- AmazonBedrockChatAgent
- AmazonBedrockKnowledgeBase
- AmazonBedrockGuardrail
- AmazonBedrockFunction
- AmazonBedrockFlow
- AmazonBedrockPrompt
- AmazonBedrockEvaluation

###### Important

Note that when you enable a blueprint, by default, you are enabling it in the same
region as your domain. When you are enabling blueprints for a project profile that is
created and enabled in a different region from your domain, you must enable these
blueprints in same region where this project profile is enabled (in addition to enabling
this blueprint in the same region as your domain). You can do this via the
**Regions** tab in the blueprint details page. This applies to all
blueprints, including the Tooling blueprint.

1. Navigate to the Amazon SageMaker management console at [https://console.aws.amazon.com/datazone](https://console.aws.amazon.com/datazone "https://console.aws.amazon.com/datazone") and use the region selector in the
   top navigation bar to choose the appropriate AWS Region.
2. Either create a new domain or choose an existing domain where you want to create a
   generative AI application development project profile.
3. On the domain's details page, choose the **Project profiles tab**
   and then choose **Create**.
4. On the **Create project profile** page, in the **Project
   profile name and description** section, specify the name of the project
   profile and the description.
5. On the **Create project profile** page, in the **Project
   profile creation options** section, choose **Create from a
   template**, and then under **Project profile templates**,
   choose **Generative AI application development**.
6. On the **Create project profile** page, in the **Default
   tooling blueprint deployment settings** section, review the selections for
   the default deployment settings for the Tooling blueprint.
   1. On the **Create project profile** page, in the
      **Project files storage** section, choose a storage configuration
      type from Amazon S3 - new and Git repository. For more information on storage types,
      see [.\_unified-storage.xml](._unified-storage.md "._unified-storage.md")###### Important

Note that by creating this project profile from a template, you can either enable
the Tooling blueprint in the same AWS account and region as your domain
(prepopulated by default) or you can enable the Tooling blueprint in a different AWS
account and region from this domain (an associated account). 7. On the **Create project profile** page, in the**Authorization - optional** section, specify who can use this project profile
to create projects in all domain units. This can also be done per domain unit in the
Amazon SageMaker Unified Studio. You can specify **Selected users and groups** or
**Allow all users and groups** options.

###### Note

Projects do not provide strong security isolation. To limit cross-domain and
cross-project resource discovery you can consider creating projects in separate
accounts. 8. On the **Create project profile** page, in the **Project
profile readiness** section, specify whether you want to enable this project
profile on creation. Unless you check the **Enable project profile on
creation** checkbox, your project profile is disabled and not available to
use for Amazon SageMaker Unified Studio projects after its creation. Leaving a project profile in a disabled
state upon creation gives you the opportunity to customize your blueprints before making
the project profile available. 9. Choose **Create project profile**.
