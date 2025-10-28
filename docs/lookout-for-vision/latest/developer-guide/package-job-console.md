End of support notice: On October 31, 2025, AWS
will discontinue support for Amazon Lookout for Vision. After October 31, 2025, you will
no longer be able to access the Lookout for Vision console or Lookout for Vision resources.
For more information, visit this [blog post](https://aws.amazon.com/blogs/machine-learning/exploring-alternatives-and-seamlessly-migrating-data-from-amazon-lookout-for-vision "https://aws.amazon.com/blogs/machine-learning/exploring-alternatives-and-seamlessly-migrating-data-from-amazon-lookout-for-vision").

# Packaging your model (Console)

You can create a model packaging job by using the Amazon Lookout for Vision console.

For information about package settings, see [Package settings](package-settings.md "package-settings.md").

###### To package a model (console)

1. [Create an Amazon S3 bucket](../../../AmazonS3/latest/userguide/create-bucket-overview.md "../../../AmazonS3/latest/userguide/create-bucket-overview.md"), or reuse an existing bucket, that Lookout for Vision uses to store the packaging job artifacts (model component).
2. Open the Amazon Lookout for Vision console at [https://console.aws.amazon.com/lookoutvision/](https://console.aws.amazon.com/lookoutvision/ " https://console.aws.amazon.com/lookoutvision/").
3. Choose **Get started**.
4. In the left navigation pane, choose **Projects**.
5. In the **Projects** section, choose the project that contains the model you want to package.
6. In the left navigation pane, under the project name, choose **Edge model packages**.
7. In the **Model packaging jobs** section, choose **Create model packaging job**.
8. Enter the settings for the package. For more information, see [Package settings](package-settings.md "package-settings.md").
9. Choose **Create model packaging job**.
10. Wait until the packaging job finishes. The job is finished when the status of the job
    is **Success**.
11. Choose the packaging job in the **Model packaging jobs** section.
12. Choose **Continue deployment in Greengrass** to continue deployment of your model component in AWS IoT Greengrass Version 2.
    For more information, see [Deploying your components to a device](device-deploy-components.md "device-deploy-components.md").
