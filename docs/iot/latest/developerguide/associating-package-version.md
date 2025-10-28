# Associating a package version to an AWS IoT thing

After you install software on your device, you can associate a package version to an AWS IoT thing’s reserved named shadow.
If AWS IoT jobs has been configured to update the thing’s reserved named shadow after the job deploys and successfully completes,
you don’t need to complete this procedure. For more information, see
[Reserved named shadow](preparing-to-use-software-package-catalog.md#reserved-named-shadow "preparing-to-use-software-package-catalog.md#reserved-named-shadow").

**Prerequisites:**

Before you begin, do the following:

- Create an AWS IoT thing, or things, and establish telemetry through AWS IoT Core.
  For more information, see
  [Getting started with AWS IoT Core](iot-gs.md "iot-gs.md").
- Create a software package and package version. For more information, see
  [Creating a software package and package version](creating-package-and-version.md "creating-package-and-version.md").
- Install the package version software on the device.

###### Note

Associating a package version to an AWS IoT thing doesn’t update or install software on the physical device.
The package version must be deployed to the device.

###### To associate a package version to an AWS IoT thing

1. On the [AWS IoT console](https://console.aws.amazon.com/iot/home "https://console.aws.amazon.com/iot/home") navigation pane, expand the **All devices** menu and
   choose **Things**.
2. Identify the AWS IoT thing that you want to update from the list and choose the thing name to display its details page.
3. In the **Details** section, choose **Packages and versions**.
4. Choose **Add to package and version**.
5. For **Choose a device package**, choose the software package you want.
6. For **Choose a version**, choose the software version you want.
7. Choose **Add device package**.

The package and version appear on the **Selected packages and versions** list. 8. Repeat these steps for each package and version that you want to associate to this thing. 9. When you’re finished, choose **Add package and version details**.
The **Thing details** page opens and you can see the new package and version in the list.
