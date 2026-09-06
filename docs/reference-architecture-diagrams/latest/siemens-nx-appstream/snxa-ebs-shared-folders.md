

# Siemens NX with Amazon EBS shared folders
<a name="snxa-ebs-shared-folders"></a>

With this architecture, you can securely access Siemens NX hosted in AWS Cloud by using an [Amazon Elastic Block Store](https://docs.aws.amazon.com/ebs/latest/userguide/) (Amazon EBS) volume for shared folders. This architecture uses [Amazon WorkSpaces Applications](https://docs.aws.amazon.com/appstream2/latest/developerguide/), [Amazon Elastic Compute Cloud](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/) (Amazon EC2), and [Amazon S3](https://docs.aws.amazon.com/AmazonS3/latest/userguide/).

![Reference architecture for Siemens NX on Amazon WorkSpaces Applications with Amazon EBS shared folders.](http://docs.aws.amazon.com/reference-architecture-diagrams/latest/siemens-nx-appstream/images/siemens-nx-architecture-diagram-ra-1.png)


The following steps describe the architecture:

1. When setting up the WorkSpaces Applications image builder, you can select the Amazon S3 folder as the user home folder to persist application settings, user data, and files.

1. An Amazon EC2 instance hosts the Amazon EBS volume. The instance acts as a server message block (SMB) share to serve its Amazon EBS volume as a shared folder for all WorkSpaces Applications users.

1. The Windows Remote Desktop Protocol (RDP) instance acts as a jump server to connect to the Amazon EC2 instance on a private subnet.

1. Users connect to their streaming instances through a web browser or the WorkSpaces Applications Windows client.