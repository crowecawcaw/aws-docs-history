# Update VPC configuration and projects

Updating the VPC configuration for the domain will apply to new projects created after
that point automatically. Projects that had been created when a VPC configuration did not
exist will have the VPC configuration applied only after the project is updated.

## Update VPC

![Update VPC configuration in Amazon SageMaker Unified Studio](images/vpc/VPC_Edit.png)

To update a VPC, complete the following steps:

1. From the domain administration page, choose **Settings** in the
   left navigation pane.
2. Under the **Actions** column, select
   **Update**.
3. Update the VPC, Subnets, or Security group.
4. Choose **Update**.

## Update project with VPC configuration

To a project with VPC configuration settings, complete the following steps:

1. From the domain administration page, choose **Projects** in the
   left navigation pane.
2. From the projects list, choose the project you want to update.
3. On the project detail page, you will see a banner at the top indicating
   "Configurations have changed. Please update this project to access the latest
   configuration."
4. In the banner, choose **Update**.
5. Confirm the update when prompted.
