# Game server builds

The build resource represents your game server software. You upload your build package to
Amazon GameLift Servers for deployment to managed EC2 fleets.

View information about game server builds in the Amazon GameLift Servers console or using the or AWS SDK for Amazon GameLift Servers.

Console
On the **Builds** page of the [Amazon GameLift Servers
console](https://console.aws.amazon.com/gamelift/ "https://console.aws.amazon.com/gamelift/"), you can view information about and manage all the game server builds
that you've uploaded to Amazon GameLift Servers for deployment on managed EC2 fleets. In the navigation pane,
choose **Hosting**, **Managed EC2**,
**Builds**.

The **Builds** page shows the following information for each build.
You can adjust the table content as needed using the **Preferences**
tool (see the ![Gear icon representing settings or configuration options.](images/settings.png)
icon in the upper right corner of the table). Custom preferences are saved to your AWS
account user and are automatically applied whenever you view this page.

###### Note

The **Builds** page shows builds in your current AWS Region
only.

- **Name** – The name associated with the uploaded
  build.
- **Status** – The status of the build. Displays one of
  three status messages:
  - **Initialized** – The upload hasn't started or is
    still in progress.
  - **Ready** – The build is ready for fleet
    creation.
  - **Failed** – The build timed out before Amazon GameLift Servers
    received the binaries.

- **Creation time** – The date and time that you uploaded
  the build to Amazon GameLift Servers.
- **Build ID** – The unique ID assigned to the build on
  upload.
- **Version** – The version label associated with the
  uploaded build.
- **Operating system** – The OS that the build runs on. The
  build OS determines which operating system Amazon GameLift Servers installs on a fleet's
  instances.
- **Size** – The size, in megabytes (MB), of the
  build file uploaded to Amazon GameLift Servers.
- **Fleets** – The number of fleets deployed
  with the build.

From this page you can do any of the following:

- View build details. Choose a build's name to open its build details page.
- Create a new fleet from a build. Select a build, and then choose **Create
  fleet**.
- Filter and sort the build list. Use the controls at the top of the table.
- Delete a build. Select a build, and then choose
  **Delete**.

###### Build details

On the **Builds** page, choose a build's name to open its details
page. The **Overview** section of the details page displays
the same build summary information as the **Builds** page.
The **Fleets** section shows a list of fleets that are
running the build, including the same summary information as the [Fleets
page](gamelift-console-fleets.md "gamelift-console-fleets.md").

AWS SDK
Use the following AWS CLI commands to retrieve information about this resource:

- [ListBuild](../apireference/API_ListBuilds.md "../apireference/API_ListBuilds.md")
- [DescribeBuild](../apireference/API_DescribeBuild.md "../apireference/API_DescribeBuild.md")
