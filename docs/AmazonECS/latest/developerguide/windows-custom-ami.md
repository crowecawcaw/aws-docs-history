# Building your own Amazon ECS-optimized Windows AMI

Use EC2 Image Builder to build your own custom Amazon ECS-optimized Windows AMI. This
makes it easy to use a Windows AMI with your own license on Amazon ECS. Amazon ECS provides a
managed Image Builder component which provides the system configuration needed to run Windows
instances to host your containers. Each Amazon ECS managed component includes a specific
container agent and Docker version. You can customize your image to use either the
latest Amazon ECS managed component, or if an older container agent or Docker version is
needed you can specify a different component.

For a full walkthrough of using EC2 Image Builder, see [Getting started
with EC2 Image Builder](../../../imagebuilder/latest/userguide/set-up-ib-env.md#image-builder-accessing-prereq "../../../imagebuilder/latest/userguide/set-up-ib-env.md#image-builder-accessing-prereq") in the _EC2 Image Builder User Guide_.

When building your own Amazon ECS-optimized Windows AMI using EC2 Image Builder, you create an image
recipe. Your image recipe must meet the following requirements:

- The **Source image** should be based on Windows Server 2019 Core, Windows Server 2019 Full, Windows Server 2022 Core, or
  Windows Server 2022 Full. Any other Windows operating system is not supported and
  may not be compatible with the component.
- When specifying the **Build components**, the
  `ecs-optimized-ami-windows` component is required. The
  `update-windows` component is recommended, which ensures the image
  contains the latest security updates.

To specify a different component version, expand the **Versioning
options** menu and specify the component version you want to use. For
more information, see [Listing the
ecs-optimized-ami-windows component versions](#windows-component-list "#windows-component-list").

## Listing the

`ecs-optimized-ami-windows` component versions

When creating an EC2 Image Builder recipe and specifying the
`ecs-optimized-ami-windows` component, you can either use the default
option or you can specify a specific component version. To determine what component
versions are available, along with the Amazon ECS container agent and Docker versions
contained within the component, you can use the AWS Management Console.

###### To list the available `ecs-optimized-ami-windows` component

versions

1. Open the EC2 Image Builder console at
   [https://console.aws.amazon.com/imagebuilder/](https://console.aws.amazon.com/imagebuilder/ "https://console.aws.amazon.com/imagebuilder/").
2. On the navigation bar, select the Region that are building your image
   in.
3. In the navigation pane, under the **Saved configurations**
   menu, choose **Components**.
4. On the **Components** page, in the search bar type
   `ecs-optimized-ami-windows` and pull down the qualification menu
   and select **Quick start (Amazon-managed)**.
5. Use the **Description** column to determine the component
   version with the Amazon ECS container agent and Docker version your image
   requires.
