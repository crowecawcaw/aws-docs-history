# Image Builders

Amazon AppStream 2.0 uses EC2 instances to stream applications. You launch instances from base images,
called _image builders_, which AppStream 2.0 provides. To create
your own custom image, you connect to an image builder instance, install and configure your
applications for streaming, and then create your image by creating a snapshot of the image
builder instance.

When you launch an image builder, you choose:

- An instance type — AppStream 2.0 provides different instance types with
  various compute, memory, and graphics configurations. The instance type must align
  with the instance family you need. For more information, see [AppStream 2.0 Instance Families](instance-types.md "instance-types.md").
- An operating system — AppStream 2.0 provides the following operating systems:
  - Windows Server 2016 Base
  - Windows Server 2019 Base
  - Windows Server 2022 Base
  - Amazon Linux 2
  - Red Hat Enterprise Linux 8
  - Rocky Linux 8 ([Rocky
    Linux from CIQ](https://ciq.com/products/rocky-linux/ "https://ciq.com/products/rocky-linux/"))

- The subnet and security groups to use — Make sure that the subnet and security groups provide access to the network resources that your applications require. Typical network resources required by applications may include licensing servers, database servers, file servers, and application servers.

###### Contents

- [Launch an Image Builder to Install and Configure Streaming Applications](tutorial-image-builder-create.md "tutorial-image-builder-create.md")
- [Connect to an Image Builder in Amazon AppStream 2.0](managing-image-builders-connect.md "managing-image-builders-connect.md")
- [Image Builder Actions](managing-image-builders-actions.md "managing-image-builders-actions.md")
- [Instance Metadata for AppStream 2.0
  Image Builders](user-instance-metadata-image-builders.md "user-instance-metadata-image-builders.md")
- [Install AMD Driver on Graphics Design Instances](AMD-driver.md "AMD-driver.md")
- [AppStream 2.0 Base Image and Managed Image Update
  Release Notes](base-image-version-history.md "base-image-version-history.md")
