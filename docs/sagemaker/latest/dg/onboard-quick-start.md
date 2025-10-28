# Use quick setup for Amazon SageMaker AI

The **Set up for single users** (quick setup) procedure gets you set up with
default settings. Use this option if you want to get started with SageMaker AI quickly and you do not
intend to customize your settings at this time. The default settings include granting access to
the common SageMaker AI services for individual users to get started. For example, Amazon SageMaker Studio and
Amazon SageMaker Canvas.

## Setup for single users (Quick setup)

After satisfying the prerequisites in [Complete Amazon SageMaker AI prerequisites](gs-set-up.md "gs-set-up.md"),
use the following instructions.

1. Open the [SageMaker AI console](https://console.aws.amazon.com/sagemaker/ "https://console.aws.amazon.com/sagemaker/").
2. Open the left navigation pane.
3. Under **Admin configurations**, choose
   **Domains**.
4. Choose **Create domain**.
5. Choose **Set up for single user (Quick setup)**. Your domain and user
   profile are created automatically.

The **Set up for single user** process creates a domain and user
profile for you automatically. If you want to learn about how the domain is set up for you
when using the quick setup option, expand the following section.

When you onboard to Amazon SageMaker AI domain using the **Set up for single user**
procedure, your domain is automatically set up with the following default settings. For
information about domains, see [Amazon SageMaker AI domain overview](gs-studio-onboard.md "gs-studio-onboard.md").

- Domain name: SageMaker AI automatically assigns the name of the
  domain with a timestamp in the following format.

```
QuickSetupDomain-YYYYMMDDTHHMMSS
```

- User profile name: SageMaker AI automatically assigns the name of
  the user profile with a timestamp in the following format.

```
default-YYYYMMDDTHHMMSS
```

- Domain execution role: SageMaker AI creates a new IAM role and
  attaches the [`AmazonSageMakerFullAccess`](../../../aws-managed-policy/latest/reference/AmazonSageMakerFullAccess.md "../../../aws-managed-policy/latest/reference/AmazonSageMakerFullAccess.md") policy. When using the quick setup and the
  updated Amazon SageMaker Studio is your default experience, your IAM role also includes the [`AmazonSageMakerCanvasFullAccess`](../../../aws-managed-policy/latest/reference/AmazonSageMakerCanvasFullAccess.md "../../../aws-managed-policy/latest/reference/AmazonSageMakerCanvasFullAccess.md"), [`AmazonSageMakerCanvasAIServicesAccess`](../../../aws-managed-policy/latest/reference/AmazonSageMakerCanvasAIServicesAccess.md "../../../aws-managed-policy/latest/reference/AmazonSageMakerCanvasAIServicesAccess.md"), [`AmazonS3FullAccess`](../../../aws-managed-policy/latest/reference/AmazonS3FullAccess.md "../../../aws-managed-policy/latest/reference/AmazonS3FullAccess.md") policies.
- User profile execution role: SageMaker AI sets the user profile
  execution role to the same IAM role used for the domain execution role.
- Shared space execution role: SageMaker AI sets the shared space
  execution role to the same IAM role used for the domain execution role.
- SageMaker Canvas time series forecasting role: SageMaker AI creates a new
  IAM role with the permissions required to use the SageMaker Canvas time series forecasting
  feature.
- Amazon S3 bucket: SageMaker AI creates an Amazon S3 bucket named with the
  following format.

```
sagemaker-studio-XXXXXXXXXXXXXXX
```

- Amazon VPC: SageMaker AI selects a public VPC with the following
  logic.
  1.  If there is a default VPC with associated subnets in the Region, SageMaker AI uses it.
  2.  If there is no default VPC or the default VPC has no associated subnets, then SageMaker AI
      uses any existing VPC with associated subnets. If there are multiple existing VPCs, SageMaker AI
      can select any of them.

- Studio experience: Amazon SageMaker Studio is set as the UI
  default experience and Studio Classic is made hidden. That is, in [`UserSettings`](../APIReference/API_UserSettings.md "../APIReference/API_UserSettings.md"):
  - `DefaultLandingUri` is set to `studio::`.
  - [`StudioWebPortalSettings`](../APIReference/API_StudioWebPortalSettings.md "../APIReference/API_StudioWebPortalSettings.md")
    `HiddenAppTypes` is set to `["JupyterServer"]`

  For information about hidden applications, see [Hide machine learning tools and
  applications in the Amazon SageMaker Studio UI](studio-updated-ui-customize-tools-apps.md "studio-updated-ui-customize-tools-apps.md").

After the domain is set up, the administrative user can [Edit domain settings](domain-edit.md "domain-edit.md").

## After quick setup

Do you want to start SageMaker AI features right away, and do not intend to learn about domains
or customize your domain? If so, skip the rest of this [Guide to getting set up with Amazon SageMaker AI](gs.md "gs.md") chapter and do the following:

- Open the [SageMaker AI console](https://console.aws.amazon.com/sagemaker "https://console.aws.amazon.com/sagemaker") and choose an
  environment from the left navigation pane.

For example, choose **Studio** from the left navigation pane and
choose **Open Studio**.

- Begin learning how to:
  - [Automated ML, no-code, or low-code](use-auto-ml.md "use-auto-ml.md")
  - [Machine learning environments offered by Amazon SageMaker AI](machine-learning-environments.md "machine-learning-environments.md")

RStudio support is not currently available when onboarding using the **Set up for
single users** ([Use quick setup for Amazon SageMaker AI](onboard-quick-start.md "onboard-quick-start.md")) option. To use RStudio, you must onboard using the **Set up for
organizations** ([Use custom setup for Amazon SageMaker AI](onboard-custom.md "onboard-custom.md"))
option. For more information, see [Use custom setup for Amazon SageMaker AI](onboard-custom.md "onboard-custom.md").
