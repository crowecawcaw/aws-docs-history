# Amazon Bedrock in SageMaker Unified Studio

Amazon Bedrock in SageMaker Unified Studio enables you to easily build and scale generative
AI applications. Amazon Bedrock in SageMaker Unified Studio provides a web interface that allow
users to interact with [Amazon
Bedrock](../../../bedrock/latest/userguide/what-is-bedrock.md "../../../bedrock/latest/userguide/what-is-bedrock.md") foundation models and use Amazon Bedrock tools, such as Agents, Guardrails,
Prompts, Flows, Evaluation, and Functions in a seamless unified fashion. Users can interact with
models in a generative AI playground or collaborate on developing generative AI applications in
projects.

Amazon Bedrock in SageMaker Unified Studio can be only used by the members of the [Amazon SageMaker unified domains](working-with-domains.md "working-with-domains.md"). For more information,
see [Amazon Bedrock in SageMaker Unified Studio](../userguide/bedrock.md "../userguide/bedrock.md").

In the current release of Amazon SageMaker Unified Studio, there are the following configuration paths available
for setting up Amazon Bedrock in SageMaker Unified Studio in your domain, each offering a
different level of customization:

- **Quick setup** - you can use this option as part of
  creating an Amazon SageMaker unified domain. Quick setup option simplifies the process of
  setting up Amazon Bedrock in SageMaker Unified Studio by automating key steps without
  requiring user input. When selected during domain creation, the **Quick
  setup** performs the following:

      + Creates the **Generative AI application development project
       profile** that the Amazon SageMaker Unified Studio user then uses to create Amazon SageMaker in
       SageMaker Unified Studio projects.
      + Activates all generative AI blueprints and the default Tooling blueprint needed to
       provision resources for the Amazon Bedrock capabilities.
      + Configures permissions for all enabled Amazon Bedrock serverless models accessible
       in the AWS account and Region, enabling their use in the generative AI projects and
       playgrounds.

  For more informaiton about creating an Amazon SageMaker unified domain with
  **Quick setup**, see [Create a Amazon SageMaker Unified Studio domain -
  quick setup](create-domain-sagemaker-unified-studio-quick.md "create-domain-sagemaker-unified-studio-quick.md").

- **Guided setup** - this is the guided setup with a
  step-by-step walkthrough of configuring Generative AI capabilities for your Amazon SageMaker
  unified domains. You can use this option only after you've created your Amazon SageMaker
  unified domain by navigating to the domain details page and using the **Next steps
  for your domain** section. It pre-populates system-recommended configurations
  which you can review and modify. Key steps include:

      + Creating the **Generative AI application development project
       profile** - the system generates a project profile specific to the domain's
       AWS account and Region. This step also automatically enables the generative AI
       blueprints if they are not already enabled. If the Tooling blueprint is not yet enabled
       in the domain, the system augments steps to enable it as well.
      + Configuring model access - the system identifies all Amazon Bedrock serverless
       models available in the account and Region, then configures access permissions for these
       models. You can review the model list and selectively enable models for use in Amazon
       Bedrock in SageMaker Unified Studio projects and domain playgrounds.

  For detailed steps of using the guided setup of Generative AI capabilities for your
  Amazon SageMaker unified domain, see [Configure Amazon Bedrock in SageMaker Unified Studio
  for your domain](genai-application-development.md#configure-bedrock-ide "genai-application-development.md#configure-bedrock-ide").

- **Manual setup** - this is a step-by-step configuration of
  project profiles, blueprints, and model access with granular control over configurations.
  You can use this option only after you've created your Amazon SageMaker unified domain by
  navigating to the domain details page and using the configuration settings under the
  **Project profiles**, **Blueprints**, and
  **Amazon Bedrock models** tabs. Manual setup is recommended for advanced
  scenarios, such as enabling generative AI in a different Region or account from the domain.
  Manual setup includes:

      + Manually creating [custom project profiles](custom.md "custom.md")
      + Enabling specific [blueprints](blueprints.md "blueprints.md")
      + [Configuring access to your Amazon Bedrock serverless
       models for the selected AWS accounts and regions](#manage-models "#manage-models")

  Once Amazon Bedrock in SageMaker Unified Studio for a domain is set up, you can perform the
  following procedures to further customize and configure it.

###### Topics

- [Configure access to your Amazon Bedrock serverless models for
  the selected AWS accounts and regions](#manage-models "#manage-models")
- [Set default models for the generative AI
  playgrounds in Amazon SageMaker Unified Studio](#set-default-models-for-playground "#set-default-models-for-playground")
- [Publishing models from associated
  accounts](#publishing-models-associated-account "#publishing-models-associated-account")

## Configure access to your Amazon Bedrock serverless models for

the selected AWS accounts and regions

You can configure access to your Amazon Bedrock serverless models for Amazon Bedrock in
SageMaker Unified Studio projects and playgrounds by enabling or disabling access in the
**Amazon Bedrock models** tab. To configure access, follow these
steps:

1. Navigate to the Amazon SageMaker management console at [https://console.aws.amazon.com/datazone](https://console.aws.amazon.com/datazone "https://console.aws.amazon.com/datazone") and use the region selector in the top
   navigation bar to choose the appropriate AWS Region.
2. Choose **View domains** and then choose the domain where you want to
   manage your Amazon Bedrock serverless models.
3. Choose the **Amazon Bedrock models** tab.
4. Amazon Bedrock in SageMaker Unified Studio uses the Amazon Bedrock to enable model
   interaction. The in SageMaker Unified Studio allows you to use the model that you have
   granted access in Amazon Bedrock. An Amazon Bedrock in SageMaker Unified Studio project
   can only access models from the project’s AWS account and AWS Region. A playground can
   access models from any account and region. On the **Amazon Bedrock
   models** page, under the **Select account and region**
   section, choose the AWS account and Region where you want to manage your serverless
   models.
5. On the **Amazon Bedrock models** page, under the **Models
   enabled for the selected account and region** section, choose the refresh
   icon.

The system queries Amazon Bedrock and displays a list of Amazon Bedrock serverless
models to which you have access. If no models are listed or if a specific model is
missing, visit the Amazon Bedrock management console for the appropriate account and
Region to grant access. If you have updated model access in Amazon Bedrock, choose the
refresh icon in the **Amazon Bedrock Models** tab to refresh the updated
list of accessible models

The following are important elements to consider as you review the generated list of
models:

    * Every model in the list is prepopulated with certain details, including modality,
     inference type, whether it's enabled in projects and playground, and roles for model
     access. A model's modality indicates the type of output data it can generate. Amazon
     Bedrock in SageMaker Unified Studio supports Amazon Bedrock foundation models with
     on-demand throughput and on-demand cross-region inference. If a model supports both
     on-demand and on-demand cross-region inference, it appears in the list twice with the
     appropraite value listed in the **Inference** column. You have the
     flexibility to enable your preferred inference type for use in projects and
     playgrounds. Amazon Bedrock in SageMaker Unified Studio does NOT support provisioned
     throughput, custom models, or imported models.
    * For easy setup, the system pre-selects accessible models that support on-demand
     throughput, excluding legacy models, to enable in projects and playground. Review and
     adjust the list to enable models for projects and playgrounds based on your specific
     requirements.
    * The models that you have not yet enabled for projects and playground access are
     grayed out in the list. To enable or disable access, choose
     **Manage** and then use the checkboxes in the **Enable in
     project** and **Enable in playground** columns. If you
     choose to disable project access of a model, confirm the disable action in the pop up
     window that appears.

6. To enable or disable your models in the Amazon SageMaker Unified Studio projects and playgrounds, choose
   **Manage** and then use the checkboxes in the **Enable in
   project** and **Enable in playground** columns to enable or
   disable your models. If you choose to disable a model in a project, confirm the disable
   action in the pop up window that appears.

## Set default models for the generative AI

playgrounds in Amazon SageMaker Unified Studio

Amazon Bedrock in SageMaker Unified Studio supports generative AI playgrounds that enable
the Amazon SageMaker unified domain users to easily experiment with Amazon Bedrock models.
Users can send prompt requests to various models and view the responses. There are two types
of playgrounds in the Amazon Bedrock in SageMaker Unified Studio: the chat playground and the
image and video playground.

As the administrator of an Amazon SageMaker unified domain, you can complete the following
procedure to set default chat and video and image generative AI playgrounds in the Amazon SageMaker Unified Studio
for your domain and their respective default models. When users access the playground, the
default model is preselected for them to begin interacting.

1. Navigate to the Amazon SageMaker management console at [https://console.aws.amazon.com/datazone](https://console.aws.amazon.com/datazone "https://console.aws.amazon.com/datazone") and use the region selector in the top
   navigation bar to choose the appropriate AWS Region.
2. Choose **View domains** and then choose the domain where you want to
   configure the detaul playgrounds and models.
3. Choose the **Amazon Bedrock models** tab.
4. In the **Default models** section, choose
   **Manage**.
5. On the **Default models - optional** page:
   - For the **Chat playground - optional**, select a default model
     from the drop-down menu. The drop-down menu includes only the models that support
     **Text** as the output modality and are enabled for playground use.
   - For the **Image and video playground - optional**, select a
     default model from the drop-down menu. The drop-down menu will include only the models
     that support either **Image** or **Video** as the
     output modality and are enabled for playground use.
   - Choose **Save** to save your choices for the default playgrounds
     and their respective default models.

## Publishing models from associated

accounts

Amazon Bedrock models are published to the domain as model assets through the
**GenerativeAIModelGovernanceProject** project. This project is is created
by Amazon SageMaker Unified Studio automatically and by default, the IAM identity (IAM user or role) who configures
Amazon Bedrock in SageMaker Unified Studio for the domain is the owner of this project. If the
domain was created via Quick setup, SSO users that were configured during Quick setup are also
owners of the **GenerativeAIModelGovernanceProject** project.

If you want to publish models from your associated account, the IAM identity of the
associated account must be added to the
**GenerativeAIModelGovernanceProject** project. In the current release of
Amazon SageMaker Unified Studio, you must complete the following procedure to do this:

1. Navigate to the Amazon SageMaker management console at [https://console.aws.amazon.com/datazone](https://console.aws.amazon.com/datazone "https://console.aws.amazon.com/datazone") and use the region selector in the top
   navigation bar to choose the appropriate AWS Region.
2. Choose **View domains** and then choose the domain where you want to
   add an associated account user to the model governance project.
3. Choose the **Amazon Bedrock models** tab and locate the
   **Model governance project section**.
4. In the **Model governance project section**, choose **Add IAM
   users or roles**, then choose **Associated account**, specify
   the ARN of the user that you want to add from the associated account, then choose
   **Add**, and then choose **Add user(s)**.
