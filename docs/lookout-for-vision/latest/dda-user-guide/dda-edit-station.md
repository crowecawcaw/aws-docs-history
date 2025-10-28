Defect Detection App is in preview release and is subject to change.

# Editing a station

You can use the Defect Detection App Console to edit a station. For example,
you can change the number of workflows assigned to a station or change the description
for a station.

###### To edit a station

1. Make sure that the edge device that hosts the station is online.
2. [Sign in](dda-signin-dda-web-app.md "dda-signin-dda-web-app.md") to the Defect Detection App Console.
3. In the top navigation pane, choose **Stations**.
4. On the stations page, choose the station that you want to edit.
5. Choose **Edit** to open the edit station page.
6. Update the station. You can make the following changes:
   - **Station name** — The name for the station.
   - **Description** — The description of the station.
   - **Workflow quantity** — The number of workflows on the station. If you choose a number
     that is smaller than the number of stations currently deployed to the station, select the stations that you want to remove.
   - **Device configuration** — The target
     configuration for the edge device that the station is deployed to. For
     more information, see [Creating the station for your edge device](dda-set-up-station.md "dda-set-up-station.md").

7. Choose **Save** to save your changes.

###### Important

Defect Detection App updates the station when the edge device that hosts the station
is next online.
