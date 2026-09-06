

# Managing playlists
<a name="v12-dash-managing-playlists"></a>

****  
This documentation topic is designed for Grafana workspaces that support **Grafana version 12.x**.  
For Grafana workspaces that support Grafana version 10.x, see [Working in Grafana version 10](using-grafana-v10.md).  
For Grafana workspaces that support Grafana version 9.x, see [Working in Grafana version 9](using-grafana-v9.md).  
For Grafana workspaces that support Grafana version 8.x, see [Working in Grafana version 8](using-grafana-v8.md).

A *playlist* is a list of dashboards that are displayed in a sequence. You might use a playlist to build situational awareness or to present your metrics to your team or visitors. Grafana automatically scales dashboards to any resolution, which makes them perfect for large screens. You can access the playlist feature from Grafana’s side menu in the **Dashboards** submenu.

## Accessing, sharing, and controlling a playlist
<a name="v12-dash-access-share-control-playlist"></a>

Use the information in this section to access existing playlists. Start and control the display of a playlist using one of the five available modes.

**To access a playlist**

1. Select **Playlists** from the left menu.

1. Choose a playlist from the list of existing playlists.

**Starting a playlist**

You can start a playlist in five different view modes. View mode determines how the menus and navigation bar appear on the dashboards.

By default, each dashboard is displayed for the amount of time entered in the **Interval** field, which you set when you create or edit a playlist. After you start a playlist, you can control it with the navigation bar at the top of the page.

**To start a playlist**

1. Access the playlist page to see a list of existing playlists.

1. Find the playlist that you want to start, then click **Start playlist**.

   The start playlist dialog box will open.

1. Select one of the five playlist modes available based on the information in the following table.

1. Click **Start <playlist name>**.

The playlist displays each dashboard for the time specified in the `Interval` field, set when creating or editing a playlist. After a playlist starts, you can control it using the navigation bar at the top of your screen.


| Mode | Description | 
| --- | --- | 
| Normal mode |  +  The side menu remains visible. <br />+  The navigation bar, row, and panel controls appear at the top of the screen.   | 
| TV mode |  +  The side menu and dashboard submenu (including variable dropdowns and dashboard links) are hidden or removed. <br />+  The navigation bar, row, and panel controls appear at the top of the screen. <br />+  Enabled automatically after one minute of user inactivity. <br />+  Enable it manually using the `d v` sequence shortcut, or by appending the parameter `?inactive` to the dashboard URL. <br />+  Disable it with any pointer movement or keyboard action.   | 
| TV mode (with auto fit panels) |  +  The navigation bar, row, and panel controls appear at the top of the screen. <br />+  Dashboard panels automatically adjust to optimize space on screen.   | 
| Kiosk mode |  +  The side menu, navigation bar, row and panel controls are completely hidden/removed from view. <br />+  You can enable it manually using the `d v` sequence shortcut after the playlist has started. <br />+  You can disable it manually with the same shortcut.   | 
| Kiosk mode (with auto fit panels) |  +  The side menu, navigation bar, row, and panel controls are completely hidden/removed from view. <br />+  Dashboard panels automatically adjust to optimize space on screen.   | 

**Controlling a playlist**

You can control a playlist in **Normal** or **TV** mode after it has started, using the navigation bar at the top of your screen. Press the `Esc` key in your keyboard to stop the playlist.


| Button | Action | 
| --- | --- | 
| Next (double-right arrow) | Advances to the next dashboard. | 
| Back (left arrow) | Returns to the previous dashboard. | 
| Stop (square) | Ends the playlist, and exits to the current dashboard. | 
| Cycle view mode (monitor icon) | Rotates the display of the dashboards in different view modes. | 
| Time range | Displays data within a time range. It can be set to display the last 5 minutes up to 5 years ago, or a custom time range, using the down arrow. | 
| Refresh (circle arrow) | Reloads the dashboard, to display the current data. It can be set to reload automatically every 5 seconds to 1 day, using the dropdown arrow. | 

## Creating a playlist
<a name="v12-dash-create-playlist"></a>

You can create a playlist to present dashboards in a sequence with a set order and time interval between dashboards.

**To create a playlist**

1. Select **Dashboards** from the left menu.

1. Select **Playlists** on the playlist page.

1. Select **New playlist**.

1. Enter a descriptive name in the **Name** text box.

1. Enter a time interval in the **Interval** text box. The dashboards you add are listed in a sequential order.

1. In **Dashboards**, add existing dashboards to the playlist using the **Add by title** and **Add by tag** dropdown options.

1. Optionally:
   + Search for a dashboard by its name, a regular expression, or a tag.
   + Filter your results by starred status or tags.
   + Rearrange the order of the dashboards you have added using the up and down arrow icon.
   + Remove a dashboard from the playlist by clicking the **x** icon beside the dashboard.

1. Select **Save** to save your changes.

## Saving a playlist
<a name="v12-dash-save-playlist"></a>

You can save a playlist and add it to your **Playlists** page, where you can start it.

**Important**  
Ensure all the dashboards that you want to appear in your playlist are added when creating or editing the playlist before saving it.

**To save a playlist**

1. Select **Dashboards** in the left menu.

1. Select **Playlists** to view the playlists available to you.

1. Choose the playlist of your choice.

1. Edit the playlist.

1. Check that the playlist has a **Name**, **Interval**, and at least one **Dashboard** added to it.

1. Select **Save** to save your changes.

## Editing or deleting a playlist
<a name="v12-dash-edit-delete-playlist"></a>

You can edit a playlist by updating its name, interval time, and by adding, removing, and rearranging the order of dashboards, or you can delete the playlist.

**To edit a playlist**

1. Select **Edit playlist** on the playlist page.

1. Update the name and time interval, then add or remove dashboards from the playlist using instructions in Create a playlist, above.

1. Select **Save** to save your changes.

**To delete a playlist**

1. Select **Playlists**.

1. Select **Remove** next to the playlist you want to delete.

**To rearrange dashboard order in a playlist**

1. Next to the dashboard you want to move, click the up or down arrow.

1. Select **Save** to save your changes.

**To remove a dashboard**

1. Select **Remove** to remove a dashboard from the playlist.

1. Select **Save** to save your changes.

## Sharing a playlist in view mode
<a name="v12-dash-share-playlist-view-mode"></a>

You can share a playlist by copying the link address on the view mode you prefer, and pasting the URL to your destination.

**To share a playlist in view mode**

1. From the **Dashboards** left side menu, choose **Playlists**.

1. Select **Start playlist** next to the playlist you want to share.

1. In the dropdown, right click the view mode you prefer.

1. Select **Copy Link Address** to copy the URL to your clipboard.

1. Paste the URL to your destination.