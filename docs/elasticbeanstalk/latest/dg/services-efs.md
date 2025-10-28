# Using Elastic Beanstalk with Amazon Elastic File System

With Amazon Elastic File System (Amazon EFS), you can create network file systems that can be mounted by instances across multiple Availability Zones. An Amazon EFS file system is
an AWS resource that uses security groups to control access over the network that's in your default or custom VPC.

In an Elastic Beanstalk environment, you can use Amazon EFS to create a shared directory that stores files for your application that users upload and modify. Your
application can treat a mounted Amazon EFS volume such as local storage. That way, you don't have to change your application code to scale up to multiple
instances.

For more information about Amazon EFS, see the [Amazon Elastic File System User
Guide](../../../efs/latest/ug.md "../../../efs/latest/ug.md").

###### Note

Elastic Beanstalk creates a
_webapp_ user that you can set up as the owner for application
directories on Amazon EC2 instances. For more information, see [Persistent Storage](concepts.concepts.md#concepts.concepts.design.storage "concepts.concepts.md#concepts.concepts.design.storage") in the _Design
considerations_ topic of this guide.

###### Sections

- [Configuration files](#services-efs-configs "#services-efs-configs")
- [Encrypted file systems](#services-efs-encrypted "#services-efs-encrypted")
- [Sample applications](#services-efs-samples "#services-efs-samples")
- [Cleaning up file systems](#services-efs-cleanup "#services-efs-cleanup")

## Configuration files

Elastic Beanstalk provides [configuration files](ebextensions.md "ebextensions.md") that you can use to create and mount Amazon EFS file systems. You can create an
Amazon EFS volume as part of your environment, or mount an Amazon EFS volume that you created independently of Elastic Beanstalk.

- **[storage-efs-createfilesystem.config](https://github.com/awslabs/elastic-beanstalk-samples/blob/master/configuration-files/aws-provided/instance-configuration/storage-efs-createfilesystem.config "https://github.com/awslabs/elastic-beanstalk-samples/blob/master/configuration-files/aws-provided/instance-configuration/storage-efs-createfilesystem.config")** – Uses the
  `Resources` key to create a new file system and mount points in
  Amazon EFS. All instances in your environment can connect to the same file system for shared,
  scalable storage. Use `storage-efs-mountfilesystem.config` to mount the
  file system on each instance.

###### Internal resources

Any resources that you create with configuration files are tied to the lifecycle of your environment. If you terminate your environment or
remove the configuration file, these resources are lost.

- **[storage-efs-mountfilesystem.config](https://github.com/awslabs/elastic-beanstalk-samples/blob/master/configuration-files/aws-provided/instance-configuration/storage-efs-mountfilesystem.config "https://github.com/awslabs/elastic-beanstalk-samples/blob/master/configuration-files/aws-provided/instance-configuration/storage-efs-mountfilesystem.config")** – Mount an Amazon EFS file system to a local path on the instances in your environment.
  You can create the volume as part of the environment with `storage-efs-createfilesystem.config`. Or, you can mount it to your
  environment using the Amazon EFS console, AWS CLI, or AWS SDK.

To use the configuration files, start by creating your Amazon EFS file system with
`storage-efs-createfilesystem.config`. Follow the instructions in the
configuration file and add it to the [.ebextensions](ebextensions.md "ebextensions.md") directory in your
source code to create the file system in your VPC.

Deploy your updated source code to your Elastic Beanstalk environment. This is to confirm that the file system was created successfully. Then, add the
`storage-efs-mountfilesystem.config` to mount the file system to the instances in your environment. Doing this in two separate
deployments ensures that, if the mount operation fails, the file system is kept intact. If you do both in the same deployment, an issue with either step
will cause the file system to terminate when the deployment fails.

## Encrypted file systems

Amazon EFS supports encrypted file systems. The [`storage-efs-createfilesystem.config`](https://github.com/awslabs/elastic-beanstalk-samples/blob/master/configuration-files/aws-provided/instance-configuration/storage-efs-createfilesystem.config "https://github.com/awslabs/elastic-beanstalk-samples/blob/master/configuration-files/aws-provided/instance-configuration/storage-efs-createfilesystem.config") configuration file that's discussed in this topic defines two custom options. You
can use these options to create an Amazon EFS encrypted file system. For more information, refer to the instructions in the configuration file.

## Sample applications

Elastic Beanstalk also provides sample applications that use Amazon EFS for shared storage. The two projects have configuration files that you can use with a standard
WordPress or Drupal installer to run a blog or other content management system in a load-balanced environment. When a user uploads a photo or other media,
the file is stored on an Amazon EFS file system. This avoids having to use the alternative, which is using a plugin to store uploaded files in Amazon S3.

- **[Load-balanced WordPress](https://github.com/awslabs/eb-php-wordpress "https://github.com/awslabs/eb-php-wordpress")** – This includes
  the configuration files to install WordPress securely and run it in a load-balanced Elastic Beanstalk environment.
- **[Load-balanced Drupal](https://github.com/awslabs/eb-php-drupal "https://github.com/awslabs/eb-php-drupal")** – This includes the
  configuration files and instructions for installing Drupal securely and running it in a load-balanced Elastic Beanstalk environment.

## Cleaning up file systems

If you created an Amazon EFS file system that uses a configuration file as part of your Elastic Beanstalk environment, Elastic Beanstalk removes the file system when you terminate
the environment. To minimize storage costs of a running application, routinely delete files that your application doesn't need. Or, ensure that the
application code maintains file lifecycle correctly.

###### Important

If you created an Amazon EFS file system that's outside of an Elastic Beanstalk environment and mounted it to the environment's instances, Elastic Beanstalk doesn't remove the file
system when you terminate the environment. To ensure that your personal information isn't retained and avoid storage costs, delete the files that your
application stored if you don't need them anymore. Alternatively, you can remove the entire file system.
