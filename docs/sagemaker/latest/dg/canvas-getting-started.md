# Getting started with using Amazon SageMaker Canvas

This guide tells you how to get started with using SageMaker Canvas. If you're an IT administrator and would
like more in-depth details, see
[Amazon SageMaker Canvas setup and permissions management (for IT
administrators)](canvas-setting-up.md "canvas-setting-up.md") to set up SageMaker Canvas for your
users.

###### Topics

- [Prerequisites for setting up Amazon SageMaker Canvas](#canvas-prerequisites "#canvas-prerequisites")
- [Step 1: Log in to SageMaker Canvas](#canvas-getting-started-step1 "#canvas-getting-started-step1")
- [Step 2: Use SageMaker Canvas to get predictions](#canvas-getting-started-step2 "#canvas-getting-started-step2")

## Prerequisites for setting up Amazon SageMaker Canvas

To set up a SageMaker Canvas application, onboard using one of the following setup methods:

1. **Onboard with the AWS console.** To onboard
   through the AWS console, you first create an Amazon SageMaker AI domain. SageMaker AI domains support the various machine learning (ML) environments such as Canvas and
   [SageMaker Studio](studio.md "studio.md"). For more information
   about domains, see [Amazon SageMaker AI domain overview](gs-studio-onboard.md "gs-studio-onboard.md").
   1. (Quick) [Use quick setup for Amazon SageMaker AI](onboard-quick-start.md "onboard-quick-start.md") – Choose this option if you’d like to quickly
      set up a domain. This grants your user all of the default Canvas permissions and basic functionality.
      Any additional features such as [document querying](canvas-fm-chat.md#canvas-fm-chat-query "canvas-fm-chat.md#canvas-fm-chat-query")
      can be enabled later by an admin. If you want to configure more granular permissions, we recommend that you choose the Advanced option instead.
   2. (Standard) [Use custom setup for Amazon SageMaker AI](onboard-custom.md "onboard-custom.md") – Choose
      this option if you’d like to complete a more advanced setup of your domain. Maintain
      granular control over user permissions such as access to data preparation features,
      generative AI functionality, and model deployments.

2. **Onboard with AWS CloudFormation.** [AWS CloudFormation](../../../AWSCloudFormation/latest/UserGuide/Welcome.md "../../../AWSCloudFormation/latest/UserGuide/Welcome.md")
   automates the provisioning of resources and configurations so that you can set up Canvas for one or more user profiles at the same time.
   Use this option if you want to automate the onboarding process at scale and make sure that your applications are configured the same way
   every time. The following [CloudFormation template](https://github.com/aws-samples/cloudformation-studio-domain "https://github.com/aws-samples/cloudformation-studio-domain") provides
   a streamlined way to onboard to Canvas, ensuring that all required components are properly set up and allowing you to focus on building
   and deploying your machine learning models.

The following section describes how to onboard to Canvas by using the AWS console to create a domain.

###### Important

For you to set up Amazon SageMaker Canvas, your version of Amazon SageMaker Studio must be 3.19.0 or later. For
information about updating Amazon SageMaker Studio, see [Shut Down and Update Amazon SageMaker Studio Classic](studio-tasks-update-studio.md "studio-tasks-update-studio.md").

### Onboard with the AWS console

If you’re doing the quick domain setup, then you can follow the instructions in [Use quick setup for Amazon SageMaker AI](onboard-quick-start.md "onboard-quick-start.md"), skip the rest of this
section, and move on to [Step 1: Log in to SageMaker Canvas](#canvas-getting-started-step1 "#canvas-getting-started-step1").

If you’re doing the standard domain setup, then you can specify the Canvas features to which you’d like to grant
your users access. Use the rest of this section as you complete the standard domain setup to help you configure the
permissions that are specific to Canvas.

In the [Use custom setup for Amazon SageMaker AI](onboard-custom.md "onboard-custom.md")
setup instructions, for **Step 2: Users and ML Activities**, you must select the Canvas permissions
that you want to grant. In the **ML activities** section, you can select the following permissions policies
to grant access to Canvas features. You can only select up to 8 **ML activities** total when setting up your domain.
The first two permissions in the following list are required to use Canvas, while the rest are for additional features.

- **Run Studio Applications** – These permissions are necessary to start up the Canvas application.
- **[Canvas Core Access](../../../aws-managed-policy/latest/reference/AmazonSageMakerCanvasFullAccess.md "../../../aws-managed-policy/latest/reference/AmazonSageMakerCanvasFullAccess.md")**
  – These permissions grant you access to the Canvas
  application and the basic functionality of Canvas, such as creating datasets, using basic data transforms, and building and analyzing models.
- (Optional) **[Canvas Data Preparation (powered by Data Wrangler)](../../../aws-managed-policy/latest/reference/AmazonSageMakerCanvasDataPrepFullAccess.md "../../../aws-managed-policy/latest/reference/AmazonSageMakerCanvasDataPrepFullAccess.md")**
  – These permissions grant
  you access to create data flows and use advanced transforms to prepare your data in Canvas. These permissions are also necessary for
  creating data processing jobs and data preparation job schedules.
- (Optional) **[Canvas AI Services](../../../aws-managed-policy/latest/reference/AmazonSageMakerCanvasAIServicesAccess.md "../../../aws-managed-policy/latest/reference/AmazonSageMakerCanvasAIServicesAccess.md")**
  – These permissions grant you access to the
  Ready-to-use models, foundation models, and Chat with Data features in Canvas.
- (Optional) **Kendra access** – This permission grants you access to the
  [document querying](canvas-fm-chat.md#canvas-fm-chat-query "canvas-fm-chat.md#canvas-fm-chat-query")
  feature, where you can query documents stored in an Amazon Kendra index using foundation models in Canvas.

If you select this option, then in the **Canvas Kendra Access** section, enter the IDs for
your Amazon Kendra indexes to which you want to grant access.

- (Optional) **[Canvas MLOps](../../../aws-managed-policy/latest/reference/AmazonSageMakerCanvasDirectDeployAccess.md "../../../aws-managed-policy/latest/reference/AmazonSageMakerCanvasDirectDeployAccess.md")**
  – This permission grants you access to the
  [model deployment](canvas-deploy-model.md "canvas-deploy-model.md") feature in Canvas,
  where you can deploy models for use in production.

In the domain setup’s **Step 3: Applications** section, choose **Configure Canvas** and then do the following:

1. For the **Canvas storage configuration**, specify where you want
   Canvas to store the application data, such as model artifacts, batch predictions, datasets, and logs.
   SageMaker AI creates a `Canvas/` folder inside this bucket to store the data.
   For more information, see [Configure your Amazon S3 storage](canvas-storage-configuration.md "canvas-storage-configuration.md").
   For this section, do the following:
   1. Select **System managed** if you want to set the location to the
      default SageMaker AI-created bucket that follows the pattern
      `s3://sagemaker-`{Region}`-`{your-account-id}``.
   2. Select **Custom S3** to specify your own Amazon S3 bucket as the storage
      location. Then, enter the Amazon S3 URI.
   3. (Optional) For **Encryption key**, specify a KMS key for encrypting
      Canvas artifacts stored at the specified location.

2. (Optional) For **Amazon Q Developer**, do the following:
   1. Turn on **Enable Amazon Q Developer in SageMaker Canvas for natural language ML** to
      give your users permissions to leverage generative AI assistance during their ML workflow in Canvas.
      This option only grants permissions to query Amazon Q Developer for help with predetermined tasks that
      can be completed in the Canvas application.
   2. Turn on **Enable Amazon Q Developer chat for general AWS questions** to
      give your users permissions to make generative AI queries related to AWS services.

3. (Optional) Configure the **Large data processing** section if your users
   plan to process datasets larger than 5 GB in Canvas. For more detailed information about how
   to configure these options, see [Grant Users Permissions to Use Large Data
   across the ML Lifecycle](canvas-large-data-permissions.md "canvas-large-data-permissions.md").
4. (Optional) For the **ML Ops permissions configuration** section, do the following:
   1. Leave the **Enable direct deployment of Canvas models** option
      turned on to give your users permissions to deploy their models from Canvas to a SageMaker AI endpoint.
      For more information about model deployment in Canvas, see
      [Deploy your models to an endpoint](canvas-deploy-model.md "canvas-deploy-model.md").
   2. Leave the **Enable Model Registry registration permissions for all users** option
      turned on to give your users permissions to register their model version to the SageMaker AI model
      registry (it is turned on by default). For more information, see [Register a model version in the SageMaker AI model
      registry](canvas-register-model.md "canvas-register-model.md").
   3. If you left the **Enable Model Registry registration permissions for all users** option turned on,
      then select either **Register to Model Registry only** or **Register and approve model in Model Registry**.

5. (Optional) For the **Local file upload configuration** section, turn on the **Enable local file upload**
   option to give your users permissions to upload files to Canvas from their local machines. Turning this option on attaches a cross-origin resource sharing (CORS)
   policy to the Amazon S3 bucket specified in the **Canvas storage configuration** (and overrides any existing CORS policy).
   To learn more about local file upload permissions, see [Grant Your Users Permissions to Upload Local
   Files](canvas-set-up-local-upload.md "canvas-set-up-local-upload.md").
6. (Optional) For the **OAuth settings** section, do the following:
   1. Choose **Add OAuth configuration**.
   2. For **Data source**, select your data source.
   3. For **Secret setup**, select **Create a new secret** and enter the
      information you have from your identity provider. If you haven’t done the initial OAuth setup with your data source yet,
      see [Set up connections to data sources with OAuth](canvas-setting-up-oauth.md "canvas-setting-up-oauth.md").

7. (Optional) For the **Canvas Ready-to-use models configuration**, do
   the following:
   1. Leave the **Enable Canvas Ready-to-use models** option
      turned on to give your users permissions to generate predictions with Ready-to-use models in
      Canvas (it is turned on by default). This option also gives you permissions to chat with
      generative-AI powered models. For more information, see [Generative AI foundation models in SageMaker Canvas](canvas-fm-chat.md "canvas-fm-chat.md").
   2. Leave the **Enable document query using Amazon Kendra** option turned on to give your
      users permissions to use foundation models for querying documents stored in an Amazon Kendra index.
      Then, from the dropdown menu, select the existing indexes to which you want to grant access. For more information, see
      [Generative AI foundation models in SageMaker Canvas](canvas-fm-chat.md "canvas-fm-chat.md").
   3. For **Amazon Bedrock role**, select **Create and use a new execution
      role** to create a new IAM execution role that has a trust relationship with
      Amazon Bedrock. This IAM role is assumed by Amazon Bedrock to fine-tune large language models (LLMs) in
      Canvas. If you already have an execution role with a trust relationship, then select
      **Use an existing execution role** and choose your role from the dropdown.
      For more information about manually configuring permissions for your own execution role, see
      [Grant Users Permissions to Use Amazon Bedrock
      and Generative AI Features in Canvas](canvas-fine-tuning-permissions.md "canvas-fine-tuning-permissions.md").

8. Finish configuring the rest of the domain settings using the [Use custom setup for Amazon SageMaker AI](onboard-custom.md "onboard-custom.md")
   procedures.

###### Note

If you encounter any issues with granting permissions through the console, such as
permissions for Ready-to-use models, see the topic [Troubleshooting issues with granting permissions through the SageMaker AI console](canvas-limits.md#canvas-troubleshoot-trusted-services "canvas-limits.md#canvas-troubleshoot-trusted-services").

You should now have a SageMaker AI domain set up and all of the Canvas permissions configured.

You can edit the Canvas permissions for a domain or a specific user after the initial domain setup.
Individual user settings override the domain settings. To learn how to edit your Canvas permissions in
the domain settings, see [Edit domain settings](domain-edit.md "domain-edit.md").

### Give yourself permissions to use specific

features in Canvas

The following information outlines the various permissions that you can grant to a
Canvas user to allow the use of various features and functionalities within Canvas. Some
of these permissions can be granted during the domain setup, but some require additional
permissions or configuration. Refer to the specific permissions information for each feature that you want
to enable:

- **Local file upload.** The permissions for local file upload
  are turned on by default in the Canvas base permissions when setting up your domain.
  If you can't upload local files from your machine to SageMaker Canvas, you can attach a CORS policy to
  the Amazon S3 bucket that you specified in the Canvas storage configuration. If you allowed
  SageMaker AI to use the default bucket, the bucket follows the naming pattern
  `s3://sagemaker-`{Region}`-`{your-account-id}``.
  For more information, see [Grant Your Users Permissions to
  Upload Local Files](canvas-set-up-local-upload.md "canvas-set-up-local-upload.md").
- **Custom image and text prediction models.** The permissions
  for building custom image and text prediction models are turned on by default in the
  Canvas base permissions when setting up your domain. However, if you have a custom
  IAM configuration and don't want to attach the [AmazonSageMakerCanvasFullAccess](security-iam-awsmanpol-canvas.md#security-iam-awsmanpol-AmazonSageMakerCanvasFullAccess "security-iam-awsmanpol-canvas.md#security-iam-awsmanpol-AmazonSageMakerCanvasFullAccess") policy to your user's IAM execution role, then you
  must explicitly grant your user the necessary permissions. For more information, see [Grant Your Users Permissions to Build Custom Image and
  Text Prediction Models](canvas-set-up-cv-nlp.md "canvas-set-up-cv-nlp.md").
- **Ready-to-use models and foundation models.** You might
  want to use the Canvas Ready-to-use models to make predictions for your data. With the
  Ready-to-use models permissions, you can also chat with generative AI-powered models. The
  permissions are turned on by default when setting up your domain, or you can edit the
  permissions for a domain that you’ve already created. The Canvas Ready-to-use models
  permissions option adds the [AmazonSageMakerCanvasAIServicesAccess](security-iam-awsmanpol-canvas.md#security-iam-awsmanpol-AmazonSageMakerCanvasAIServicesAccess "security-iam-awsmanpol-canvas.md#security-iam-awsmanpol-AmazonSageMakerCanvasAIServicesAccess") policy to your execution role. For more
  information, see the [Get started](canvas-ready-to-use-models.md#canvas-ready-to-use-get-started "canvas-ready-to-use-models.md#canvas-ready-to-use-get-started") section of the Ready-to-use models
  documentation.

For more information about getting started with generative AI foundation models,
see [Generative AI foundation models in SageMaker Canvas](canvas-fm-chat.md "canvas-fm-chat.md").

- **Fine-tune foundation models.** If you'd like to fine-tune
  foundation models in Canvas, you can either add the permissions when setting up your
  domain, or you can edit the permissions for the domain or user profile after creating
  your domain. You must add the [AmazonSageMakerCanvasAIServicesAccess](security-iam-awsmanpol-canvas.md#security-iam-awsmanpol-AmazonSageMakerCanvasAIServicesAccess "security-iam-awsmanpol-canvas.md#security-iam-awsmanpol-AmazonSageMakerCanvasAIServicesAccess") policy to the AWS IAM role you chose when
  setting up the user profile, and you must also add a trust relationship with Amazon Bedrock to
  the role. For instructions on how to add these permissions to your IAM role, see [Grant Users Permissions to Use Amazon Bedrock
  and Generative AI Features in Canvas](canvas-fine-tuning-permissions.md "canvas-fine-tuning-permissions.md").
- **Send batch predictions to Quick Suite.** You might want to [send _batch predictions_](canvas-send-predictions.md "canvas-send-predictions.md"), or datasets of predictions you generate
  from a custom model, to Quick Suite for analysis. In [QuickSight](../../../quicksight/latest/user/welcome.md "../../../quicksight/latest/user/welcome.md"), you can build and publish
  predictive dashboards with your prediction results. For instructions on how to add these
  permissions to your Canvas user's IAM role, see [Grant Your Users Permissions to
  Send Predictions to Quick Suite](canvas-quicksight-permissions.md "canvas-quicksight-permissions.md").
- **Deploy Canvas models to a SageMaker AI endpoint.** SageMaker AI
  Hosting offers _endpoints_ which you can use to deploy your
  model for use in production. You can deploy models built in Canvas to a SageMaker AI endpoint and then
  make predictions programmatically in a production environment. For more information, see
  [Deploy your models to an endpoint](canvas-deploy-model.md "canvas-deploy-model.md").
- **Register model versions to the model registry.** You might
  want to register _versions_ of your model to the [SageMaker AI model
  registry](model-registry.md "model-registry.md"), which is a repository for tracking the status of updated versions of your
  model. A data scientist or MLOps team working in the SageMaker Model Registry can view the versions
  of your model that you’ve built and approve or reject them. Then, they can deploy your model
  version to production or kick off an automated workflow. Model registration permissions are
  turned on by default for your domain. You can manage permissions at the user profile level
  and grant or remove permissions to specific users. For more information, see [Register a model version in the SageMaker AI model
  registry](canvas-register-model.md "canvas-register-model.md").
- **Import data from Amazon Redshift.** If you want to import data from
  Amazon Redshift, you must give yourself additional permissions. You must add the
  `AmazonRedshiftFullAccess` managed policy to the AWS IAM role you chose when
  setting up the user profile. For instructions on how to add the policy to the role, see [Grant Users
  Permissions to Import Amazon Redshift Data](canvas-redshift-permissions.md "canvas-redshift-permissions.md").

###### Note

The necessary permissions to import through other data sources, such as Amazon Athena and SaaS
platforms, are included in the [AmazonSageMakerFullAccess](../../../aws-managed-policy/latest/reference/AmazonSageMakerFullAccess.md "../../../aws-managed-policy/latest/reference/AmazonSageMakerFullAccess.md") and [AmazonSageMakerCanvasFullAccess](security-iam-awsmanpol-canvas.md#security-iam-awsmanpol-AmazonSageMakerCanvasFullAccess "security-iam-awsmanpol-canvas.md#security-iam-awsmanpol-AmazonSageMakerCanvasFullAccess") policies. If you followed the standard setup
instructions, these policies should already be attached to your execution role. For more
information about these data sources and their permissions, see [Connect to data sources](canvas-connecting-external.md "canvas-connecting-external.md").

## Step 1: Log in to SageMaker Canvas

When the initial setup is complete, you can access SageMaker Canvas with any of the
following methods, depending on your use case:

- In the [SageMaker AI console](https://console.aws.amazon.com/sagemaker/ "https://console.aws.amazon.com/sagemaker/"), choose the **Canvas** in the left navigation pane.
  Then, on the **Canvas** page, select your user from the dropdown and launch the Canvas application.
- Open [SageMaker Studio](studio.md "studio.md"),
  and in the Studio interface, go to the Canvas page and launch the Canvas application.
- Use your organization’s SAML 2.0-based SSO methods, such as Okta or the IAM Identity Center.

When you log into SageMaker Canvas for the first time, SageMaker AI creates the application and
a SageMaker AI _space_ for you. The Canvas application’s
data is stored in the space. To learn more about spaces, see [Collaboration with shared spaces](domain-space.md "domain-space.md").
The space consists of your user profile’s applications and a shared directory for all of your
applications’ data. If you don’t want to use the default space created by SageMaker AI and would prefer
to create your own space for storing application data, see the page [Store SageMaker Canvas application data in your own SageMaker AI
space](canvas-spaces-setup.md "canvas-spaces-setup.md").

## Step 2: Use SageMaker Canvas to get predictions

After you’ve logged in to Canvas, you can start building models and generating
predictions for your data.

You can either use Canvas Ready-to-use models to make predictions without building a
model, or you can build a custom model for your specific business problem. Review the following
information to decide whether Ready-to-use models or custom models are best for your use
case.

- **Ready-to-use models.** With Ready-to-use models, you can
  use pre-built models to extract insights from your data. The Ready-to-use models cover a
  variety of use cases, such as language detection and document analysis. To get started making
  predictions with Ready-to-use models, see [Ready-to-use models](canvas-ready-to-use-models.md "canvas-ready-to-use-models.md").
- **Custom models.** With custom models, you can build a
  variety of model types that are customized to make predictions for your data. Use custom models
  if you’d like to build a model that is trained on your business-specific data and if you’d like
  to use features such as [evaluating
  your model’s performance](canvas-evaluate-model.md "canvas-evaluate-model.md"). To get started with building a custom model, see [Custom models](canvas-custom-models.md "canvas-custom-models.md").
