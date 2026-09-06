

# Image Builders
<a name="managing-image-builders"></a>

Amazon WorkSpaces Applications uses EC2 instances to stream applications. You launch instances from base images, called *image builders*, which WorkSpaces Applications provides. To create your own custom image, you connect to an image builder instance, install and configure your applications for streaming, and then create your image by creating a snapshot of the image builder instance.

When you launch an image builder, you choose:
+ An instance type — WorkSpaces Applications provides different instance types with various compute, memory, and graphics configurations. The instance type must align with the instance family you need. For more information, see [WorkSpaces Applications Instance Families](instance-types.md).
+ An operating system — WorkSpaces Applications provides the following operating systems:
  + Windows 11
  + Windows Server 2025 Base
  + Windows Server 2022 Base
  + Windows Server 2019 Base
  + Windows Server 2016 Base
  + Red Hat Enterprise Linux 8
  + Rocky Linux 8 ([Rocky Linux from CIQ](https://ciq.com/products/rocky-linux/))
+ The subnet and security groups to use — Make sure that the subnet and security groups provide access to the network resources that your applications require. Typical network resources required by applications may include licensing servers, database servers, file servers, and application servers.

**Topics**
+ [Launch an Image Builder to Install and Configure Streaming Applications](tutorial-image-builder-create.md)
+ [Connect to an Image Builder in Amazon WorkSpaces Applications](managing-image-builders-connect.md)
+ [Image Builder Actions](managing-image-builders-actions.md)
+ [Instance Metadata for WorkSpaces Applications Image Builders](user-instance-metadata-image-builders.md)
+ [Install AMD Driver on Graphics Design Instances](AMD-driver.md)
+ [WorkSpaces Applications Base Image and Managed Image Update Release Notes](base-image-version-history.md)