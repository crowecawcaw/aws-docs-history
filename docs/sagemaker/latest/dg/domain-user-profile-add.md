# Add user profiles

The following section shows how to add user profiles to a domain using the SageMaker AI
console or the AWS CLI.

After you add a user profile to the domain, users can login using a URL. If the domain
uses AWS IAM Identity Center for authentication, users receive an email that contains the URL to sign in to
the domain. If the domain uses AWS Identity and Access Management, you can create a URL for a user profile using [CreatePresignedDomainUrl](../APIReference/API_CreatePresignedDomainUrl.md "../APIReference/API_CreatePresignedDomainUrl.md")

## Add user profiles from the console

You can add user profiles to a domain from the SageMaker AI console by following this
procedure.

1. Open the Amazon SageMaker AI console at [https://console.aws.amazon.com/sagemaker/](https://console.aws.amazon.com/sagemaker/ "https://console.aws.amazon.com/sagemaker/").
2. On the left navigation pane, choose **Admin
   configurations**.
3. Under **Admin configurations**, choose
   **domains**.
4. From the list of domains, select the domain that you want to add a user
   profile to.
5. On the **domain details** page, choose the **User
   profiles** tab.
6. Choose **Add user**. This opens a new page.
7. Use the default name for your user profile or add a custom name.
8. For **Execution role**, choose an option from the role selector. If
   you choose **Enter a custom IAM role ARN**, the role must have, at a
   minimum, an attached trust policy that grants SageMaker AI permission to assume the role. For
   more information, see [SageMaker AI Roles](sagemaker-roles.md "sagemaker-roles.md").

If you choose **Create a new role**, the **Create an IAM
role** dialog box opens:

    1. For **S3 buckets you specify**, specify additional Amazon S3
     buckets that users of your notebooks can access. If you don't want to add access to
     more buckets, choose **None**.
    2. Choose **Create role**. SageMaker AI creates a new IAM role,
     `AmazonSageMaker-ExecutionPolicy`, with the [AmazonSageMakerFullAccess](https://console.aws.amazon.com//iam/home?#/policies/arn:aws:iam::aws:policy/AmazonSageMakerFullAccess "https://console.aws.amazon.com//iam/home?#/policies/arn:aws:iam::aws:policy/AmazonSageMakerFullAccess") policy attached.

9. (Optional) Add tags to the user profile. All resources that the user profile creates
   will have a domain ARN tag and a user profile ARN tag. The domain ARN tag is
   based on domain ID, while the user profile ARN tag is based on the user profile
   name.
10. Choose **Next**.
11. In the **SageMaker Studio** section, you have the option to choose
    between the newer and classic version of Studio as your default experience.
    - If you choose **SageMaker Studio** (recommended) as your
      default experience, the Studio Classic IDE has default settings. For information on the
      default settings, see [Default settings](onboard-quick-start.md#onboard-quick-start-defaults "onboard-quick-start.md#onboard-quick-start-defaults").

    For information on Studio, see [Amazon SageMaker Studio](studio-updated.md "studio-updated.md").
    - If you choose **Studio Classic** as your default experience, you
      can choose to enable or disable notebook resource sharing. Notebook resources
      include artifacts such as cell output and Git repositories. For more information on
      Notebook resources, see [Share and Use an Amazon SageMaker Studio Classic Notebook](notebooks-sharing.md "notebooks-sharing.md").

12. Under **SageMaker Canvas** , you can configure your SageMaker Canvas settings. For the
    instructions and configuration details for onboarding, see [Getting started with using Amazon SageMaker Canvas](canvas-getting-started.md "canvas-getting-started.md").
    1. For the **Canvas base permissions configuration**, select
       whether to establish the minimum required permissions to use the SageMaker Canvas
       application.

13. Under **RStudio**, if RStudio license, select whether you want to
    create the user with one of the following authorizations:
    - Unauthorized
    - RStudio Admin
    - RStudio User

14. Choose **Next**.
15. In the **Customize Studio UI** page you can customize the
    viewable applications and machine learning (ML) tools displayed in Studio. This
    customization only hides the applications and ML tools in the left navigation pane in
    Studio. For information on the Studio UI, see [Amazon SageMaker Studio UI overview](studio-updated-ui.md "studio-updated-ui.md").

For information about the applications, see [Applications supported in Amazon SageMaker Studio](studio-updated-apps.md "studio-updated-apps.md").

The customize Studio UI feature is not available in Studio Classic. If you wish to
set Studio as your default experience, choose **Previous** and to
return to the previous step. 16. Choose **Next**. 17. After you have reviewed your changes, choose **Create user
profile**.

## Create user profiles from the AWS CLI

To create a user profile in a domain from the AWS CLI, run the following command from
the terminal of your local machine. For information about the available JupyterLab version
ARNs, see [Setting a default JupyterLab
version](studio-jl.md#studio-jl-set "studio-jl.md#studio-jl-set").

```
aws --region `region` \
sagemaker create-user-profile \
--domain-id `domain-id` \
--user-profile-name `user-name` \
--user-settings '{
  "JupyterServerAppSettings": {
    "DefaultResourceSpec": {
      "SageMakerImageArn": "`sagemaker-image-arn`",
      "InstanceType": "system"
    }
  }
}'
```

You can use the AWS CLI to customize the applications and ML tools displayed in
Studio for the user, using [StudioWebPortalSettings](../APIReference/API_StudioWebPortalSettings.md "../APIReference/API_StudioWebPortalSettings.md"). Use `HiddenAppTypes` to hide applications and
`HiddenMlTools` to hide ML tools. For more information on customizing the left
navigation of the Studio UI, see [Hide machine learning tools and
applications in the Amazon SageMaker Studio UI](studio-updated-ui-customize-tools-apps.md "studio-updated-ui-customize-tools-apps.md"). This feature is not available for
Studio Classic.
