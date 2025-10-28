# Manage Tooling blueprint parameters

The tooling blueprint creates resources for the project, including IAM user roles,
security groups, and Amazon SageMaker unified domains.

You can perform the following procedure to manage the parameters of the Tooling
blueprint.

1. Navigate to the Amazon SageMaker management console at [https://console.aws.amazon.com/datazone](https://console.aws.amazon.com/datazone "https://console.aws.amazon.com/datazone") and use the region selector
   in the top navigation bar to choose the appropriate AWS Region.
2. Choose **View domains** and choose the domain’s name from the
   list. The name is a hyperlink.
3. On the domain's details page, navigate to the **Project
   profiles** tab.
4. In the **Project profiles** tab, choose a project profile,
   for example, **All capabilities**. The name of the project
   profile is a hyperlink.
5. On the project profile details page, choose **Tooling
   configuration**.
6. In the Blueprint parameters section, review the parameter values that will be
   used during project creation.

To modify a parameter value, first, on the **Tooling
configuration** tab, choose **Edit**, then choose
the parameter that you want to edit by checking its radio button, and then
choose **Edit**.

In the **Edit blueprint parameter** pop up window, modify the
parameter value, and check the **Editable** box if you want the
values to be provided during project creation.

You can modify the following parameters:

    * `minIdleTimeoutInMinutes` - the minimum time (in minutes)
     that Amazon SageMaker waits after the application becomes idle before
     shutting the user's space down.
    * `maxEbsVolumeSize` - the maximum EBS storage volume size
     (in GB) for the user's private spaces.
    * `idleTimeoutInMinutes` - the time (in minutes) that Amazon
     SageMaker waits after the application becomes idle before shutting the
     user's space down.
    * `enableNetworkIsolation` - enable network isolation for
     training and deployed inference container.
    * `lifecycleManagement` - indicates whether idle shutdown is
     activated for this project's Amazon SageMaker unified domain.
    * `sagemakerDomainNetworkType` - The network type for this
     project's Amazon SageMaker unified domain.
    * `maxIdleTimeoutInMinutes` - the maximum time (in minutes)
     that Amazon SageMaker waits after the application becomes idle before
     shutting this project's Amazon SageMaker unified domain down.
    * `allowConnectionToUserGovernedEmrClusters` - allow
     connection creation to existing user governed EMR Clusters.
    * `enableSpaces` - enable creation of private compute spaces
     for development tools.
    * `enableProjectRepositoryAutoSync` - synchronise your Git
     repository code artifacts to your Amazon SageMaker Unified Studio
     project’s S3 bucket at
     `s3://{bucket}/{domain_id}/{project_id}/sys/code/dev/{repository_id}/{branch}/`.
     This synchronisation can be triggered via Git `commit push`
     events. Keeping the S3 bucket in sync with the Git repository ensures
     that any changes pushed by the user are immediately available for
     utilization.

###### Note

Enabling `maxEbsVolumeSize`, `enableSpaces`, or
`enableProjectRepositoryAutoSync` parameters might result in
incurring additional costs. For more infromation, see [Amazon SageMaker
pricing](https://aws.amazon.com/sagemaker/pricing/ "https://aws.amazon.com/sagemaker/pricing/").
