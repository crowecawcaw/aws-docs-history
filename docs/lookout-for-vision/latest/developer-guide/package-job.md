End of support notice: On October 31, 2025, AWS
will discontinue support for Amazon Lookout for Vision. After October 31, 2025, you will
no longer be able to access the Lookout for Vision console or Lookout for Vision resources.
For more information, visit this [blog post](https://aws.amazon.com/blogs/machine-learning/exploring-alternatives-and-seamlessly-migrating-data-from-amazon-lookout-for-vision "https://aws.amazon.com/blogs/machine-learning/exploring-alternatives-and-seamlessly-migrating-data-from-amazon-lookout-for-vision").

# Packaging your Amazon Lookout for Vision model

A model packaging job packages an Amazon Lookout for Vision model as a model component.

To create a model packaging job, you choose the model you want to package and provide
settings for the model component that the job creates. You can only package a model that
has been successfully trained.

You can use the Lookout for Vision console or AWS SDK to create the model packaging job. You can also get information about the
model packaging jobs you create. For more information, see [Getting information about model packaging jobs](package-job-info.md "package-job-info.md").
You can use AWS IoT Greengrass V2 console or the AWS SDK to deploy the components to the AWS IoT Greengrass Version 2 core device.

###### Topics

- [Package settings](package-settings.md "package-settings.md")
- [Packaging your model (Console)](package-job-console.md "package-job-console.md")
- [Packaging your model (SDK)](package-job-sdk.md "package-job-sdk.md")
- [Getting information about model packaging jobs](package-job-info.md "package-job-info.md")
