

# Manage Your Amazon EFS Storage Volume in Amazon SageMaker Studio Classic
<a name="studio-tasks-manage-storage"></a>

**Note**  
As of November 30, 2023, the previous Amazon SageMaker Studio experience is now named Amazon SageMaker Studio Classic. The following section is specific to using the Studio Classic application. For information about using the updated Studio experience, see [Amazon SageMaker Studio](studio-updated.md).  
Studio Classic is still maintained for existing workloads but is no longer available for onboarding. You can only stop or delete existing Studio Classic applications and cannot create new ones. We recommend that you [migrate your workload to the new Studio experience](studio-updated-migrate.md).

The first time a user on your team onboards to Amazon SageMaker Studio Classic, Amazon SageMaker AI creates an Amazon Elastic File System (Amazon EFS) volume for the team. A home directory is created in the volume for each user who onboards to Studio Classic as part of your team. Notebook files and data files are stored in these directories. Users don't have access to other team member's home directories. Amazon SageMaker AI domain does not support mounting custom or additional Amazon EFS volumes.

**Important**  
Don't delete the Amazon EFS volume. If you delete it, the domain will no longer function and all of your users will lose their work.

**To find your Amazon EFS volume**

1. Open the [SageMaker AI console](https://console.aws.amazon.com/sagemaker/).

1. On the left navigation pane, choose **Admin configurations**.

1. Under **Admin configurations**, choose **domains**. 

1. From the **Domains** page, select the domain to find the ID for.

1. From the **Domain details** page, select the **Domain settings** tab.

1. Under **General settings**, find the **Domain ID**. The ID will be in the following format: `d-xxxxxxxxxxxx`.

1. Pass the `Domain ID`, as `DomainId`, to the [describe\_domain](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sagemaker.html#SageMaker.Client.describe_domain) method.

1. In the response from `describe_domain`, note the value for the `HomeEfsFileSystemId` key. This is the Amazon EFS file system ID.

1. Open the [Amazon EFS console](https://console.aws.amazon.com/efs#/file-systems/). Make sure the AWS Region is the same Region that's used by Studio Classic.

1. Under **File systems**, choose the file system ID from the previous step.

1. To verify that you've chosen the correct file system, select the **Tags** heading. The value corresponding to the `ManagedByAmazonSageMakerResource` key should match the `Studio Classic ID`.

For information on how to access the Amazon EFS volume, see [Using file systems in Amazon EFS](https://docs.aws.amazon.com/efs/latest/ug/using-fs.html).

To delete the Amazon EFS volume, see [Deleting an Amazon EFS file system](https://docs.aws.amazon.com/efs/latest/ug/delete-efs-fs.html).