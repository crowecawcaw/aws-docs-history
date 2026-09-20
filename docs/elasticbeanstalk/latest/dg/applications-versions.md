

# Managing application versions
<a name="applications-versions"></a>

This topic explains application versions and how to create and manage them.

Elastic Beanstalk creates an application version whenever you upload a source bundle. This usually occurs when you create an environment or upload and deploy code using the [environment management console](environments-console.md) or [EB CLI](eb-cli3.md). Elastic Beanstalk deletes these application versions according to the application's lifecycle policy and when you delete the application. For details about application lifecycle policy, see [Configuring application version lifecycle settings](applications-lifecycle.md).

You can also upload a source bundle without deploying it from the [application management console](applications-console.md) or with the EB CLI command **[**eb appversion**](eb3-appversion.md)**. Elastic Beanstalk stores source bundles in Amazon Simple Storage Service (Amazon S3) and doesn't automatically delete them.

Application versions work the same way in both Beanstalk Standard and Beanstalk Cluster. An application version is a labeled, deployable iteration of your application, and deploying, deleting, tagging, and version quotas apply to both Standard and Cluster. In Beanstalk Standard an application version corresponds to a source bundle stored in Amazon Simple Storage Service (Amazon S3), described below. In Beanstalk Cluster a version is a container image you provide or build from source. For how Cluster versions are created, see [Building container images for Beanstalk Cluster environments](beanstalk-cluster-app-versions.md).

You can apply tags to an application version when you create it, and edit tags of existing application versions. For details, see [Tagging application versions](applications-versions-tagging.md).

## Creating application versions
<a name="applications-versions.creating"></a>

**Note**  
Over time, your application can accumulate many application versions. To save storage space and avoid hitting the [application version quota](https://docs.aws.amazon.com/general/latest/gr/aws_service_limits.html#limits_elastic_beanstalk), it's a good idea to delete application versions that you no longer need. 

The file you specify in the following procedure is associated with your application. You can deploy the application version to a new or existing environment.

The following procedure uploads a source bundle, which is how a Beanstalk Standard application version is created. With Beanstalk Cluster, an application version is a container image that you provide, or source that Elastic Beanstalk builds into an image. For that procedure, see [Building container images for Beanstalk Cluster environments](beanstalk-cluster-app-versions.md).

**To create a new application version**

1. Open the [Elastic Beanstalk console](https://console.aws.amazon.com/elasticbeanstalk), and in the **Regions** list, select your AWS Region.

1. In the navigation pane, choose **Applications**, and then choose your application's name from the list.

1. In the navigation pane, find your application's name and choose **Application versions**.

1. Choose **Upload**. Use the on-screen form to upload your application's [source bundle](applications-sourcebundle.md).
**Note**  
The source bundle's file size limit is 500 MB.

1. Optionally, provide a brief description, and add tag keys and values.

1. Choose **Upload**.

You can also create a new application version using the EB CLI. For more information, see [**eb appversion**](eb3-appversion.md) in the *EB CLI commands* chapter.

## Deleting application versions
<a name="applications-versions.deleting"></a>

**Note**  
Deleting an application version doesn't affect environments currently running that version.

You can also configure Elastic Beanstalk to delete old versions automatically by configuring application version lifecycle settings. If you configure these lifecycle settings, they're applied when you create new application versions. For example, if you configure a maximum of 25 application versions, Elastic Beanstalk deletes the oldest version when you upload a 26th version. If you set a maximum age of 90 days, any versions older than 90 days are deleted when you upload a new version. For details, see [Configuring application version lifecycle settings](applications-lifecycle.md).

**Note**  
With Beanstalk Cluster, deleting an application version removes the Elastic Beanstalk version record only. It doesn't delete the container image, the Amazon Elastic Container Registry (Amazon ECR) repository that holds the image, or a source bundle in Amazon S3, and the **Delete versions from Amazon S3** option doesn't apply. For the resources that are retained and for the processing statuses that block a deletion, see [Building container images for Beanstalk Cluster environments](beanstalk-cluster-app-versions.md).

**To delete an application version**

1. Open the [Elastic Beanstalk console](https://console.aws.amazon.com/elasticbeanstalk), and in the **Regions** list, select your AWS Region.

1. In the navigation pane, choose **Applications**, and then choose your application's name from the list.

1. In the navigation pane, find your application's name and choose **Application versions**.

1. Select one or more application versions that you want to delete.

1. Choose **Actions**, then choose **Delete**.

1. (Optional) To leave the application source bundle for these application versions in your Amazon Simple Storage Service (Amazon S3) bucket, clear the box for **Delete versions from Amazon S3**.

1. Choose **Delete**.

If you don't choose to delete the source bundle from Amazon S3, Elastic Beanstalk still deletes the version from its records. However, the source bundle is left in your [Elastic Beanstalk storage bucket](AWSHowTo.S3.md). The application version quota applies only to versions Elastic Beanstalk tracks. Therefore, you can delete versions to stay within the quota, but retain all source bundles in Amazon S3.

**Note**  
The application version quota doesn't apply to source bundles, but you might still incur Amazon S3 charges, and retain personal information beyond the time you need it. Elastic Beanstalk never deletes source bundles automatically. You should delete source bundles when you no longer need them.

You can also delete an application version using the EB CLI. For more information, see [**eb appversion**](eb3-appversion.md) in the *EB CLI commands* chapter.