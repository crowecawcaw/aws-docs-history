# Launch RSessions from the RStudio Launcher

###### Important

Custom IAM policies that allow Amazon SageMaker Studio or Amazon SageMaker Studio Classic to create Amazon SageMaker
resources must also grant permissions to add tags to those resources. The permission to
add tags to resources is required because Studio and Studio Classic automatically tag
any resources they create. If an IAM policy allows Studio and Studio Classic to
create resources but does not allow tagging, "AccessDenied" errors can occur when
trying to create resources. For more information, see [Provide permissions for tagging SageMaker AI
resources](security_iam_id-based-policy-examples.md#grant-tagging-permissions "security_iam_id-based-policy-examples.md#grant-tagging-permissions").

[AWS managed policies for Amazon SageMaker AI](security-iam-awsmanpol.md "security-iam-awsmanpol.md")
that give permissions to create SageMaker resources already include permissions to add tags
while creating those resources.

The following sections show how to use the RStudio Launcher to launch RSessions. They also
include information about how to open the RStudio Launcher when using RStudio on
Amazon SageMaker AI.

## Open RStudio Launcher

Open the RStudio launcher using the following set of procedures that matches your environment.

1. Open the Amazon SageMaker AI console at [https://console.aws.amazon.com/sagemaker/](https://console.aws.amazon.com/sagemaker/ "https://console.aws.amazon.com/sagemaker/").
2. From the left navigation, select **RStudio**.
3. Under **Get Started**, select the domain and user profile to
   launch.
4. Choose **Launch RStudio**.
5. Navigate to Studio following the steps in [Launch Amazon SageMaker Studio](studio-updated-launch.md "studio-updated-launch.md").
6. Under **Applications**, select **RStudio**.
7. From the RStudio landing page, choose **Launch application**.
   The procedure to open the RStudio Launcher using the AWS CLI differs depending on the method
   used to manage your users.

**IAM Identity Center**

1. Use the AWS access portal to open your Amazon SageMaker AI domain.
2. Modify the URL path to “/rstudio/default” as follows.

```
#Studio URL
https://<domain-id>.studio.<region>.sagemaker.aws/jupyter/default/lab

#modified URL
https://<domain-id>.studio.<region>.sagemaker.aws/rstudio/default
```

**IAM**

To open the RStudio Launcher from the AWS CLI in IAM mode, complete the following procedure.

1. Create a presigned URL using the following command.

```
aws sagemaker create-presigned-domain-url --region `<REGION>` \
    --domain-id `<DOMAIN-ID>` \
    --user-profile-name `<USER-PROFILE-NAME>`
```

2. Append _&redirect=RStudioServerPro_ to the
   generated URL.
3. Navigate to the updated URL.

## Launch RSessions

After you’ve launched the RStudio Launcher, you can create a new RSession.

1. Select **New Session**.
2. Enter a **Session Name**.
3. Select an instance type that your RSession runs on. This defaults to
   `ml.t3.medium`.
4. Select an Image that your RSession uses as the kernel.
5. Select Start Session.
6. After your session has been created, you can start it by selecting
   the name. 

###### Note

If you receive a warning that there is a version mismatch between your RSession and
RStudioServerPro apps, then you must upgrade the version of your RStudioServerPro app.
For more information, see [RStudio Versioning](rstudio-version.md "rstudio-version.md").
