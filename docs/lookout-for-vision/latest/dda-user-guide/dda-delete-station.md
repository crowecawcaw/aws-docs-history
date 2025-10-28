Defect Detection App is in preview release and is subject to change.

# Delete a station

Deleting a station removes the station from Defect Detection App but doesn't remove any
artifacts, such as deployed models and station components, from the edge device.
To delete local artifacts, run the `uninstallGreengrassCore.sh` after you delete the station.
The script is in the configuration zip file that you downloaded when creating the station.

Use the following instructions to delete a station from the Defect Detection App Console.

###### To delete a station

1. Make sure that your edge device that hosts the station is online.
2. [Sign in](dda-signin-dda-web-app.md "dda-signin-dda-web-app.md") to the Defect Detection App Console.
3. In the top navigation pane, choose **Stations**.
4. On the stations page, choose the station that you want to delete.
5. Choose **Delete** to open the delete station dialog box.
6. Enter the station name and choose **Delete** to delete the station.
7. On the edge device, run the `uninstallGreengrassCore.sh` script to uninstall components from the device.
