

# Manage Image Builder infrastructure configuration
<a name="manage-infra-config"></a>

An infrastructure configuration is a reusable Image Builder resource that defines the Amazon EC2 environment where Image Builder builds and tests your image. When you create an image pipeline, you attach one infrastructure configuration to it. Image Builder then uses those settings every time the pipeline runs a build.

Because the infrastructure configuration is a separate resource, you can reuse the same build environment across many pipelines. You can also update the environment in one place without modifying individual pipelines. When you update an infrastructure configuration, your changes take effect on the *next* build. Your changes don't affect builds that are already in progress or images that Image Builder already created.

**Note**  
An infrastructure configuration is independent from the images it helps create. Deleting or editing an infrastructure configuration doesn't change images that Image Builder already built. If a pipeline references an infrastructure configuration, you can't delete that configuration until you remove the reference.

Use an infrastructure configuration to specify the following settings for your build and test environment. For API field names, required settings, and constraints, see [CreateInfrastructureConfiguration](https://docs.aws.amazon.com/imagebuilder/latest/APIReference/API_CreateInfrastructureConfiguration.html) in the *EC2 Image Builder API Reference*.
+ **Instance types** for your build and test instances. We recommend that you specify more than one instance type because this allows Image Builder to launch an instance from a pool with sufficient capacity. This can reduce your transient build failures. If you specify more than one type, Image Builder launches an instance from the first type that has available capacity. If none of your instance types are available in the , the build fails.

  For Mac images, choose instance types that natively support macOS. For more information, see [Amazon EC2 Mac instances](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ec2-mac-instances.html) in the *Amazon EC2 User Guide*.
+ **An instance profile** that gives your build and test instances the permissions to run your components. For example, if you have a component that retrieves resources from Amazon S3, the instance profile requires permissions to access those files. The instance profile also requires a minimal set of permissions for EC2 Image Builder to successfully communicate with the instance. For more information, see [Get set up to build custom images with Image Builder](set-up-ib-env.md).
+ **Instance placement settings** that control the Availability Zone, tenancy, and Dedicated Host where Image Builder launches your instances.
+ **Networking** – the VPC subnet and security groups for your build and test instances. If you specify a subnet, you must also specify at least one security group.
+ **Logging** – the Amazon S3 location where Image Builder stores AWSTOE application logs from your build and test phases. To use Amazon S3 logging, the instance profile must have `s3:PutObject` permissions for the target bucket (`arn:aws:s3:::BucketName/*`). If you don't configure Amazon S3 logging, Image Builder keeps the AWSTOE application logs on the build and test instances only.
+ **Troubleshooting settings** – an Amazon EC2 key pair and the `terminateInstanceOnFailure` setting. With these settings, you can keep a failed build instance running and connect to it to investigate.
+ **Instance metadata options** that control whether instances require IMDSv2 tokens, and the metadata response hop limit.
+ **An SNS topic** where Image Builder publishes messages about your image build status, such as when an image becomes available or a build fails. For more information, see [Amazon SNS integration in Image Builder](integ-sns.md).
**Note**  
If your SNS topic is encrypted, the key that encrypts this topic must reside in the account where the Image Builder service runs. Image Builder can't send notifications to SNS topics that are encrypted with keys from other accounts.

**Topics**
+ [Instance placement and tenancy](infra-config-placement.md)
+ [List and view infrastructure configuration details](infra-config-details.md)
+ [Create an infrastructure configuration](create-infra-config.md)
+ [Update an infrastructure configuration](update-infra-config.md)
+ [Delete an infrastructure configuration](delete-infra-config.md)
+ [Image Builder and AWS PrivateLink interface VPC endpoints](vpc-interface-endpoints.md)

**Tip**  
When you have multiple resources of the same type, tagging helps you to identify a specific resource based on the tags you've assigned to it. For more information about tagging your resources using Image Builder commands in the AWS CLI, see the [Tag resources](tag-resources.md) section of this guide.