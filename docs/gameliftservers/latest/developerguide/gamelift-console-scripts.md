# Amazon GameLift Servers Realtime scripts in the Amazon GameLift Servers console

On the **Scripts** page of the [Amazon GameLift Servers console](https://console.aws.amazon.com/gamelift/ "https://console.aws.amazon.com/gamelift/"), you can view information about and manage all the Amazon GameLift Servers Realtime scripts
that you've uploaded to Amazon GameLift Servers for deployment on managed EC2 fleets. In the navigation pane,
choose **Hosting**, **Scripts**.

The **Scripts** page shows the following information for each
script. You can adjust the table content as needed using the **Preferences**
tool (see the ![Gear icon representing settings or configuration options.](images/settings.png)
icon in the upper right corner of the table). Custom preferences are saved to your AWS
account user and are automatically applied whenever you view this page.

###### Note

The **Scripts** page shows scripts in your current AWS Region
only.

- **Name** – The name associated with the uploaded
  script.
- **ID** – The unique ID assigned to the script on
  upload.
- **Version** – The version label associated with the
  uploaded script.
- **Size** – The size, in megabytes (MB), of the
  script file uploaded to Amazon GameLift Servers.
- **Creation time** – The date and time that you uploaded
  the script to Amazon GameLift Servers.
- **Fleets** – The number of fleets deployed
  with the script.
  From this page you can do any of the following:

- View script details. Choose a build's name to open its script details page.
- Create a new fleet from a script. Select a script, and then choose
  **Create fleet**.
- Filter and sort the script list. Use the controls at the top of the table.
- Delete a script. Select a script, and then choose
  **Delete**.

## Script details

On the **Scripts** page, choose a script's name to open its details
page. The **Overview** section of the details page displays the same
script summary information as the **Builds** page. The
**Fleets** section shows a list of fleets created with the script,
including the same summary information as the [Fleets page](gamelift-console-fleets.md "gamelift-console-fleets.md").
