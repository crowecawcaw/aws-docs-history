# Delete a MLOps Project using

Amazon SageMaker Studio or Studio Classic

This procedure demonstrates how to delete a MLOps project using Amazon SageMaker Studio or Studio Classic.

**Prerequisites**

###### Note

You can only delete projects in Studio or Studio Classic that you have created. This condition is part
of the service catalog permission `servicecatalog:TerminateProvisionedProduct` in the
`AmazonSageMakerFullAccess` policy. If needed, you can update this policy to remove this
condition.

- An IAM account or IAM Identity Center to sign in to Studio or Studio Classic. For information, see [Amazon SageMaker AI domain overview](gs-studio-onboard.md "gs-studio-onboard.md").
- Basic familiarity with the Studio or Studio Classic user interface. For information about
  the Studio UI, see [Amazon SageMaker Studio](studio-updated.md "studio-updated.md"). For
  information about Studio Classic, see [Amazon SageMaker Studio Classic UI Overview](studio-ui.md "studio-ui.md").

Studio

1. Open the SageMaker Studio console by following the instructions in [Launch
   Amazon SageMaker Studio](studio-updated-launch.md "studio-updated-launch.md").
2. In the left navigation pane, choose **Deployments**, and then
   choose **Projects**.
3. Choose the radio button next to the project you want to delete.
4. Choose the vertical ellipsis above the upper-right corner of the projects
   list, and choose **Delete**.
5. Review the information in the **Delete project** dialog box, and choose
   **Yes, delete the project** if you still want to delete the project.
6. Choose **Delete**.
7. Your projects list appears. Confirm that your project no longer appears in the list.

Studio Classic

1. Sign in to Studio Classic. For more information, see [Amazon SageMaker AI domain overview](gs-studio-onboard.md "gs-studio-onboard.md").
2. In the Studio Classic sidebar, choose the **Home** icon (
   ![Black square icon representing a placeholder or empty image.](/images/sagemaker/latest/dg/images/studio/icons/house.png)
   ).
3. Select **Deployments** from the menu, and then
   select **Projects**.
4. Select the target project from the dropdown list. If you don’t see
   your project, type the project name and apply the filter to find your
   project.
5. Once you've found your project, select the project name to view
   details.
6. Choose **Delete** from the
   **Actions** menu.
7. Confirm your choice by choosing **Delete** from the
   **Delete Project** window.
