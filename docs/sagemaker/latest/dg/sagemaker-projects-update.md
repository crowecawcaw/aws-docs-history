# Update a MLOps Project in

Amazon SageMaker Studio or Studio Classic

This procedure demonstrates how to update a MLOps project in Amazon SageMaker Studio or
Studio Classic. Updating the project gives you the option to modify your end-to-end ML solution. You can update the **Description**, template version, and template parameters.

**Prerequisites**

- An IAM account or IAM Identity Center to sign in to Studio or Studio Classic. For information, see [Amazon SageMaker AI domain overview](gs-studio-onboard.md "gs-studio-onboard.md").
- Basic familiarity with the Studio or Studio Classic user interface. For information about
  the Studio UI, see [Amazon SageMaker Studio](studio-updated.md "studio-updated.md"). For
  information about Studio Classic, see [Amazon SageMaker Studio Classic UI Overview](studio-ui.md "studio-ui.md").
- Add the following custom inline policies to the specified roles:

User-created role having `AmazonSageMakerFullAccess`

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Action": [
 "servicecatalog:CreateProvisionedProductPlan",
 "servicecatalog:DescribeProvisionedProductPlan",
 "servicecatalog:DeleteProvisionedProductPlan"
 ],
 "Resource": "*"
 }
 ]
}`

```

`AmazonSageMakerServiceCatalogProductsLaunchRole`

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Action": [
 "cloudformation:CreateChangeSet",
 "cloudformation:DeleteChangeSet",
 "cloudformation:DescribeChangeSet"
 ],
 "Resource": "arn:aws:cloudformation:*:*:stack/SC-*"
 },
 {
 "Effect": "Allow",
 "Action": [
 "codecommit:PutRepositoryTriggers"
 ],
 "Resource": "arn:aws:codecommit:*:*:sagemaker-*"
 }
 ]
}`

```

To update your project in Studio or Studio Classic, complete the following steps.

Studio

1. Open the SageMaker Studio console by following the instructions in [Launch
   Amazon SageMaker Studio](studio-updated-launch.md "studio-updated-launch.md").
2. In the left navigation pane, choose **Deployments**, and then
   choose **Projects**.
3. Choose the radio button next to the project you want to update.
4. Choose the vertical ellipsis above the upper-right corner of the projects list,
   and choose **Update**.
5. Choose **Next**.
6. Review the project updates in the summary table, and choose **Update**.
   It may take a few minutes for the project to update.

Studio Classic

###### To update a project in Studio Classic

1. Sign in to Studio Classic. For more information, see [Amazon SageMaker AI domain overview](gs-studio-onboard.md "gs-studio-onboard.md").
2. In the Studio Classic sidebar, choose the **Home** icon (
   ![Black square icon representing a placeholder or empty image.](images/studio/icons/house.png)
   ).
3. Select **Deployments** from the menu, and then
   select **Projects**. A list of your projects appears.
4. Select the name of the project you want to update in the projects list.
5. Choose **Update** from the **Actions** menu in the upper-right corner of the project tab.
6. In the **Update project** dialog box, you can edit the **Description** and listed template parameters.
7. Choose **View difference**.

A dialog box displays your original and updated project settings. Any change in your project settings can modify or delete resources in the current project. The dialog box displays these changes as well. 8. You may need to wait a few minutes for the **Update** button to become active. Choose **Update**. 9. The project update may take a few minutes to complete. Select **Settings** in the project tab and ensure the parameters have been updated correctly.
