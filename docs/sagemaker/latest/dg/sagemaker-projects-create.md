# Create a MLOps Project using

Amazon SageMaker Studio or Studio Classic

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

This procedure demonstrates how to create an MLOps project using Amazon SageMaker Studio Classic.

**Prerequisites**

- An IAM account or IAM Identity Center to sign in to Studio or Studio Classic. For more information, see [Amazon SageMaker AI domain overview](gs-studio-onboard.md "gs-studio-onboard.md").
- Permission to use SageMaker AI-provided project templates. For more information, see [Granting SageMaker Studio Permissions
  Required to Use
  Projects](sagemaker-projects-studio-updates.md "sagemaker-projects-studio-updates.md").
- Basic familiarity with the Studio Classic user interface. For nore information, see [Amazon SageMaker Studio Classic UI Overview](studio-ui.md "studio-ui.md").

Studio

1. Open the SageMaker Studio console by following the instructions in [Launch
   Amazon SageMaker Studio](studio-updated-launch.md "studio-updated-launch.md").
2. In the left navigation pane, choose **Deployments**, and then
   choose **Projects**.
3. In the upper-right corner above the projects list, choose **Create
   project**.
4. In the **Templates** page, choose a template to use for your project.
   For more information about project templates, see
   [MLOps Project Templates](sagemaker-projects-templates.md "sagemaker-projects-templates.md").
5. Choose **Next**.
6. In the **Project details** page, enter the following information:
   - **Name**: A name for your project.
   - **Description**: An optional description for your project.
   - The values for the Service Catalog provisioning parameters related to your
     chosen template.

7. Choose **Create project** and wait for the project to appear in the
   **Projects** list.
8. (Optional) In the Studio sidebar, choose **Pipelines** to view the pipeline created
   from your project. For more information about Pipelines, see [Pipelines](pipelines.md "pipelines.md").

Studio Classic

1. Sign in to Studio Classic. For more information, see [Amazon SageMaker AI domain overview](gs-studio-onboard.md "gs-studio-onboard.md").
2. In the Studio Classic sidebar, choose the **Home** icon (
   ![Black square icon representing a placeholder or empty image.](images/studio/icons/house.png)
   ).
3. Select **Deployments** from the menu, and then
   select **Projects**.
4. Choose **Create project**.

The **Create project** tab opens displaying a list of available
templates. 5. If not selected already, choose
**SageMaker AI templates**. For more information about project templates, see
[MLOps Project Templates](sagemaker-projects-templates.md "sagemaker-projects-templates.md"). 6. Choose the template **Model building, training, and deployment**. 7. Choose **Select project template**.

The **Create project** tab changes to display **Project details**. 8. Enter the following information:

    * For **Project details**, enter a name and description for your
     project.
    * Optionally, add tags, which are key-value pairs that you can use to track your
     projects.

9. Choose **Create project** and wait for the project to appear in the
   **Projects** list.
