# Manage Image Builder infrastructure configuration

You can use infrastructure configurations to specify the Amazon EC2 infrastructure that Image Builder uses
to build and test your EC2 Image Builder image. Infrastructure settings include:

- Instance types for your build and test infrastructure. We recommend that you specify more than one instance type because
  this allows Image Builder to launch an instance from a pool with sufficient capacity. This
  can reduce your transient build failures.

For Mac images, you might want to choose instance types that natively support the
macOS operating system. For more information, see [Amazon EC2 Mac instances](../../../AWSEC2/latest/UserGuide/ec2-mac-instances.md "../../../AWSEC2/latest/UserGuide/ec2-mac-instances.md")
in the _Amazon EC2 User Guide_.

- Instance placement settings where you can specify the host, host placement group,
  or Availability Zone where the instances that launch from your image should go.
- An instance profile that provides your build and test instances with the permissions
  that are required to perform customization activities. For example, if you have a component that retrieves
  resources from Amazon S3, the instance profile requires permissions to access those files.
  The instance profile also requires a minimal set of permissions for EC2 Image Builder to
  successfully communicate with the instance. For more information, see
  [Get set up to build custom images with Image Builder](set-up-ib-env.md "set-up-ib-env.md").
- The VPC, subnet, and security groups for your pipeline's build and test instances.
- The Amazon S3 location where Image Builder stores application logs from your build and testing. If you
  configure logging, the instance profile specified in your infrastructure configuration must
  have `s3:PutObject` permissions for the target bucket
  (`arn:aws:s3:::`BucketName`/*`).
- An Amazon EC2 key pair that allows you to log on to your instance to troubleshoot
  if your build fails and you set `terminateInstanceOnFailure` to
  `false`.
- An SNS topic where Image Builder sends event notifications. For more information about how Image Builder
  integrates with Amazon SNS, see [Amazon SNS integration in Image Builder](integ-sns.md "integ-sns.md").

###### Note

If your SNS topic is encrypted, the key that encrypts this topic must reside in the
account where the Image Builder service runs. Image Builder can't send notifications to SNS topics that
are encrypted with keys from other accounts.
You can create and manage infrastructure configurations using the Image Builder console,
through the Image Builder API, or with **imagebuilder** commands in the AWS CLI.

###### Contents

- [List and view infrastructure configuration details](infra-config-details.md "infra-config-details.md")
- [Create an infrastructure configuration](create-infra-config.md "create-infra-config.md")
- [Update an
  infrastructure configuration](update-infra-config.md "update-infra-config.md")
- [Image Builder and AWS PrivateLink interface VPC endpoints](vpc-interface-endpoints.md "vpc-interface-endpoints.md")

###### Tip

When you have multiple resources of the same type, tagging helps you to
identify a specific resource based on the tags you've assigned to it.
For more information about tagging your resources using Image Builder commands
in the AWS CLI, see the [Tag resources](tag-resources.md "tag-resources.md")
section of this guide.
