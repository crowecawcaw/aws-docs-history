# Billing and cost in SageMaker Canvas

To track the costs associated with your SageMaker Canvas application, you can use the AWS Billing and Cost Management service.
Billing and Cost Management provides tools to help you gather information related to your cost and usage, analyze your
cost drivers and usage trends, and take action to budget your spending. For more information, see
[What is
AWS Billing and Cost Management?](../../../awsaccountbilling/latest/aboutv2/billing-what-is.md "../../../awsaccountbilling/latest/aboutv2/billing-what-is.md")

Billing in SageMaker Canvas consists of the following components:

- Workspace instance charges – You are charged for the number of hours that you are
  logged in to or using SageMaker Canvas. We recommend that you log out or create a schedule to shut down any
  Canvas applications that you’re not actively using to reduce costs. For more information, see
  [Logging out of Amazon SageMaker Canvas](canvas-log-out.md "canvas-log-out.md").
- AWS service charges – You are charged for building and making predictions with custom models,
  or for making predictions with Ready-to-use models:

      + Training charges – For all model types, you are charged based on your resource
       usage while the model builds. These resources include any compute instances that
       Canvas spins up. You may see these charges on your account as Hosting, Training, Processing, or Batch Transform jobs.
      + Prediction charges – You are charged for the resources used to generate predictions,
       depending on the type of custom model that you built or the type of Ready-to-use model you
       used.

  The [Ready-to-use models](canvas-ready-to-use-models.md "canvas-ready-to-use-models.md") in Canvas leverage other AWS services to
  generate predictions. When you use a Ready-to-use model, you are charged by the respective service, and their pricing conditions apply:

- For sentiment analysis, entities extraction, language detection, and personal information
  detection, you’re charged with [Amazon Comprehend
  pricing](https://aws.amazon.com/comprehend/pricing/ "https://aws.amazon.com/comprehend/pricing/").
- For object detection in images and text detection in images, you’re charged with [Amazon Rekognition pricing](https://aws.amazon.com/rekognition/pricing/ "https://aws.amazon.com/rekognition/pricing/").
- For expense analysis, identity document analysis, and document analysis, you’re charged with
  [Amazon Textract pricing](https://aws.amazon.com/textract/pricing/ "https://aws.amazon.com/textract/pricing/").
  For more information, see [SageMaker Canvas pricing](https://aws.amazon.com/sagemaker/canvas/pricing/ "https://aws.amazon.com/sagemaker/canvas/pricing/").

To help you track your costs in Billing and Cost Management, you can assign custom tags to your SageMaker Canvas app and users. You can track the costs your apps incur,
and by tagging individual user profiles, you can track costs based on the user profile. For more information about tags, see
[Using Cost Allocation Tags](../../../awsaccountbilling/latest/aboutv2/cost-alloc-tags.md "../../../awsaccountbilling/latest/aboutv2/cost-alloc-tags.md").

You can add tags to your SageMaker Canvas app and users by doing the following:

- If you are setting up your Amazon SageMaker AI domain and SageMaker Canvas for the first time, follow the
  [Getting Started](canvas-getting-started.md "canvas-getting-started.md") instructions
  and add tags when creating your domain or users. You can add tags either through the **General settings** in
  the domain console setup, or through the APIs ([CreateDomain](../APIReference/API_CreateDomain.md "../APIReference/API_CreateDomain.md")
  or [CreateUserProfile](../APIReference/API_CreateUserProfile.md "../APIReference/API_CreateUserProfile.md")). SageMaker AI adds the tags
  specified in your domain or UserProfile to any SageMaker Canvas apps or users you create after you create the domain.
- If you want to add tags to apps in an existing domain, you must add tags to either the
  domain or the UserProfile. You can adds tags through either the console or the [AddTags](../APIReference/API_AddTags.md "../APIReference/API_AddTags.md") API.
  If you add tags through the console, then you must delete and relaunch your SageMaker Canvas app in order
  for the tags to propagate to the app. If you use the API, the tags are added directly to the app. For
  more information about deleting and relaunching a SageMaker Canvas app, see [Manage apps](canvas-manage-apps.md "canvas-manage-apps.md").
  After you add tags to your domain, it might take up to 24 hours for the tags to appear in
  the AWS Billing and Cost Management console for activation. After they appear in the console, it takes another 24 hours
  for the tags to activate.

On the **Cost explorer** page, you can group and filter your costs by tags
and usage types to separate your Workspace instance charges from your Training
charges. The charges for each are listed as the following:

- Workspace instance charges: Charges show up under the usage type `REGION-Canvas:Session-Hrs (Hrs)`.
- Training charges: Charges show up under the usage types for SageMaker AI Hosting, Training, Processing, or Batch Transform jobs.
