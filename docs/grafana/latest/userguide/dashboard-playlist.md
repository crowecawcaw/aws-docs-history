# Playlist

This documentation topic is designed
for Grafana workspaces that support **Grafana version
8.x**.

For Grafana workspaces that support Grafana version 10.x, see
[Working in Grafana version 10](using-grafana-v10.md "using-grafana-v10.md").

For Grafana workspaces that support Grafana version 9.x, see
[Working in Grafana version 9](using-grafana-v9.md "using-grafana-v9.md").

A playlist is a list of dashboards that are displayed in a sequence. You can use a
playlist to build situational awareness or to present your metrics to your team or
visitors.

Amazon Managed Grafana automatically scales dashboards to any resolution, including big screens.

You can access the **Playlist** feature from the side menu, in the
**Dashboards** submenu.

## Creating a playlist

A playlist presents dashboards in a sequence, with a set order and a time
interval between dashboards.

1. To access the **Playlist** feature, pause on the side
   menu.
2. Choose **Playlists**.
3. Choose **New playlist**.
4. In the **Name** text box, enter a name for your
   playlist.
5. In the **Interval** text box, enter a time interval.

The time interval is the amount of time for Amazon Managed Grafana to stay on a particular dashboard before advancing to the next one on the playlist. 6. Next to each dashboard that you want to add to your playlist, choose
**Add to playlist**. 7. Choose **Create**.

## Editing a playlist

You can edit playlists while creating them or after saving them.

1. To access the Playlist feature, pause on the side menu.
2. Choose **Playlists**.
3. Choose the playlist that you want to edit.

### Editing the name of a

playlist

1. Choose the **Name** text box.
2. Edit the name.
3. Choose **Save** to save your changes.

### Editing the interval of a

playlist

1. Choose the **Interval** text box.
2. Edit the interval.
3. Choose **Save** to save your changes.

### Adding a dashboard to a

playlist

1. Next to the dashboard that you want to add, choose **Add to
   playlist**.
2. Choose **Save** to save your changes.

### Searching for a dashboard to

add

1. Under **Add dashboards**, choose the **Search
   dashboards by name** text box.
2. Enter a name or regular expression.
3. If needed, filter your results by starred status or tags. By default,
   your starred dashboards appear as options to add to the playlist.
4. Choose **Save**to save your changes.

### Rearranging dashboard order

1. Next to the dashboard that you want to move, choose the up or down
   arrow.
2. Choose **Save** to save your changes.

### Removing a dashboard

1. Choose the x icon to remove a dashboard from the playlist.
2. Choose **Save** to save your changes.

### Deleting a playlist

1. Choose **Playlists**.
2. Next to the playlist that you want to delete, choose the x icon.

## Saving a playlist

You can save a playlist to add it to your **Playlists** page,
where you can start it. Be sure to add all the dashboards that you want to appear in
your playlist before you save it.

1. To access the **Playlist** feature, pause on the side
   menu.
2. Choose **Playlists**.
3. Choose the playlist.
4. Edit the playlist.

Ensure that your playlist has a **Name**,
**Interval**, and at least one
**Dashboard** added to it. 5. Choose **Save**.

## Starting a playlist

You can start a playlist in five different view modes. The mode determines how
the menus and navigation bar are displayed on the dashboards.

By default, each dashboard is displayed for the amount of time entered in the
**Interval** field, which can be set while creating or editing
a playlist. After you start a playlist, you can control it by using the navbar at
the top of your screen.

1. On the **Dashboards** menu, choose
   **Playlists**.
2. Next to the playlist that you want to start, choose **Start
   playlist**.
3. In the dropdown list, choose one of the following display modes:
   - Normal mode
     - The side menu remains visible.
     - The navbar, row, and panel controls appear at the top of
       the screen.

   - TV mode
     - The side menu is hidden or removed.
     - The navbar, row, and panel controls appear at the top of
       the screen.
     - TV mode is turned on automatically after 1 minute of user
       inactivity.
     - You can turn TV mode on manually by using the **d v** sequence shortcut, or by
       appending the parameter `?inactive` to the
       dashboard URL.
     - You can disable TV mode with any mouse movement or
       keyboard action.

   - TV mode (with auto fit panels)
     - The side menu is hidden or removed.
     - The navbar, row, and panel controls appear at the top of
       the screen.
     - Dashboard panels automatically adjust to optimize space
       on screen.

   - Kiosk mode
     - The side menu, navbar, row, and panel controls are
       completely hidden or removed from view.
     - You can turn Kiosk mode on manually by using the
       **d v** sequence shortcut
       after the playlist has started.
     - You can turn off Kiosk mode manually by using the same
       shortcut.

   - Kiosk mode (with auto fit panels):
     - The side menu, navbar, row, and panel controls are
       completely hidden or removed from view.
     - Dashboard panels automatically adjust to optimize space
       on screen.

## Controlling a playlist

You can control a playlist in **Normal** or
**TV** mode after it has started by using the
navigation bar at the top of your screen.

| Button                         | Result                                                                                                                                                      |
| ------------------------------ | ----------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Next (double right arrow)      | Advances to the next dashboard.                                                                                                                             |
| Back (left arrow)              | Returns to the previous dashboard.                                                                                                                          |
| Stop (square)                  | Ends the playlist, and exits to the current dashboard.                                                                                                      |
| Cycle view mode (monitor icon) | Changes the display of the dashboards to different view modes.                                                                                              |
| Time range                     | Displays data within a time range. It can be set to display the<br>last 5 minutes up to 5 years ago, or a custom time range, using the<br>dropdown arrow.   |
| Refresh (circle arrow)         | Reloads the dashboard to display the current data. It can be set<br>to reload automatically, from every 5 seconds to 1 day, by using the<br>dropdown arrow. |

To stop the playlist from your keyboard, press **Esc**.

## Sharing a playlist in a view

mode

You can share a playlist by copying the URL in the view mode that you want and
pasting the URL to your destination.

1. From the **Dashboards** menu, choose **Playlists**.
2. Next to the playlist that you want to share, choose **Start
   playlist**, and then choose the view mode that you want.
3. To copy the URL to your clipboard, choose **Copy Link
   Address**.

For example, the URL for a playlist on the Grafana Play site in Kiosk
mode could be
`https://play.grafana.org/d/000000010/annotations?orgId=1&kiosk` 4. Paste the URL to your destination.
