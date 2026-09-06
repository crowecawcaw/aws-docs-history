

# Use quick setup for Amazon SageMaker AI
<a name="onboard-quick-start"></a>

The **Set up for single users** (quick setup) procedure gets you set up with default settings. Use this option if you want to get started with SageMaker AI quickly and you do not intend to customize your settings at this time. The default settings include granting access to the common SageMaker AI services for individual users to get started. For example, Amazon SageMaker Studio and Amazon SageMaker Canvas.

## Setup for single users (Quick setup)
<a name="onboard-quick-start-instructions"></a>

After satisfying the prerequisites in [Complete Amazon SageMaker AI prerequisites](gs-set-up.md), use the following instructions.

1. Open the [SageMaker AI console](https://console.aws.amazon.com/sagemaker/).

1. Open the left navigation pane.

1. Under **Admin configurations**, choose **Domains**.

1. Choose **Create domain**.

1. Choose **Set up for single user (Quick setup)**. Your domain and user profile are created automatically.

The **Set up for single user** process creates a domain and user profile for you automatically. If you want to learn about how the domain is set up for you when using the quick setup option, expand the following section.

### Default settings
<a name="onboard-quick-start-defaults"></a>

When you onboard to Amazon SageMaker AI domain using the **Set up for single user** procedure, your domain is automatically set up with the following default settings. For information about domains, see [Amazon SageMaker AI domain overview](gs-studio-onboard.md).
+ **Domain name**: SageMaker AI automatically assigns the name of the domain with a timestamp in the following format.

  ```
  QuickSetupDomain-YYYYMMDDTHHMMSS
  ```
+ **User profile name**: SageMaker AI automatically assigns the name of the user profile with a timestamp in the following format.

  ```
  default-YYYYMMDDTHHMMSS
  ```
+ **Domain execution role**: SageMaker AI creates a new IAM role and attaches the [`AmazonSageMakerFullAccess`](https://docs.aws.amazon.com/aws-managed-policy/latest/reference/AmazonSageMakerFullAccess.html) policy. When using the quick setup and the updated Amazon SageMaker Studio is your default experience, your IAM role also includes the [`AmazonSageMakerCanvasFullAccess`](https://docs.aws.amazon.com/aws-managed-policy/latest/reference/AmazonSageMakerCanvasFullAccess.html), [`AmazonSageMakerCanvasAIServicesAccess`](https://docs.aws.amazon.com/aws-managed-policy/latest/reference/AmazonSageMakerCanvasAIServicesAccess.html), [`AmazonS3FullAccess`](https://docs.aws.amazon.com/aws-managed-policy/latest/reference/AmazonS3FullAccess.html) policies.
+ **User profile execution role**: SageMaker AI sets the user profile execution role to the same IAM role used for the domain execution role.
+ **Shared space execution role**: SageMaker AI sets the shared space execution role to the same IAM role used for the domain execution role.
+ **SageMaker Canvas time series forecasting role**: SageMaker AI creates a new IAM role with the permissions required to use the SageMaker Canvas time series forecasting feature.
+ **Amazon S3 bucket**: SageMaker AI creates an Amazon S3 bucket named with the following format.

  ```
  sagemaker-studio-XXXXXXXXXXXXXXX
  ```
+ **Amazon VPC**: SageMaker AI selects a public VPC with the following logic.

  1. If there is a default VPC with associated subnets in the Region, SageMaker AI uses it. 

  1. If there is no default VPC or the default VPC has no associated subnets, then SageMaker AI uses any existing VPC with associated subnets. If there are multiple existing VPCs, SageMaker AI can select any of them.
+ **Storage configurations**: SageMaker AI configures the domain with the following default storage settings.
  + `HomeEfsCreation`: Disabled. An Amazon EFS volume is not created by default during quick setup. You can enable EFS creation later through Domain Settings. To enable EFS after domain creation, see [Amazon EFS creation and auto-mounting in Studio](studio-updated-automount.md).
  + `AutoMountHomeEFS`: Disabled. This setting becomes active only after EFS creation is enabled at the domain level.
  + Space EBS storage: Default space size is 5 GB, maximum space size is 100 GB (applies to both private and shared spaces).
+ **Studio experience**: Amazon SageMaker Studio is set as the UI default experience and Studio Classic is made hidden. That is, in [`UserSettings`](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_UserSettings.html):
  + `DefaultLandingUri` is set to `studio::`.
  + [`StudioWebPortalSettings`](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_StudioWebPortalSettings.html) `HiddenAppTypes` is set to `["JupyterServer"]`

    For information about hidden applications, see [Hide machine learning tools and applications in the Amazon SageMaker Studio UI](studio-updated-ui-customize-tools-apps.md).

After the domain is set up, the administrative user can [Edit domain settings](domain-edit.md).

## After quick setup
<a name="onboard-quick-start-what-next"></a>

Do you want to start SageMaker AI features right away, and do not intend to learn about domains or customize your domain? If so, skip the rest of this [Guide to getting set up with Amazon SageMaker AI](gs.md) chapter and do the following:
+ Open the [SageMaker AI console](https://console.aws.amazon.com/sagemaker) and choose an environment from the left navigation pane.

  For example, choose **Studio** from the left navigation pane and choose **Open Studio**.
+ Begin learning how to:
  + [Automated ML, no-code, or low-code](use-auto-ml.md)
  + [Machine learning environments offered by Amazon SageMaker AI](machine-learning-environments.md)

RStudio requires Amazon EFS to be enabled on your domain. When using quick setup, EFS is not created by default and RStudio will not appear in the Applications section. To use RStudio with a quick setup domain, enable EFS creation through Domain Settings. Alternatively, you can onboard using the **Set up for organizations** ([Use custom setup for Amazon SageMaker AI](onboard-custom.md)) option and EFS creation is enabled by default during the Configure storage step.