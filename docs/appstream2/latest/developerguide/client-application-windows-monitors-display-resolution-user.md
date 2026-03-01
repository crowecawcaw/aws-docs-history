# Monitors

## Monitors and Display Resolution

WorkSpaces Applications supports the use of multiple monitors during streaming sessions, including monitors that have different resolutions. To help ensure an optimal streaming experience, we recommend that you set the display scale for your monitors to 100 percent if you use multiple monitors.

The WorkSpaces Applications client supports multiple monitors with the following display resolutions:

- Multiple monitors (up to 4K resolution) — Up to 4 monitors with a maximum display resolution of 4096x2160 pixels per monitor

###### Note

If you are connected to an WorkSpaces Applications streaming session using
native application mode, you can use monitors with up to 4K
resolution. If you use higher-resolution monitors, the WorkSpaces Applications client falls back to classic mode. In
this case, the WorkSpaces Applications classic mode streaming view occupies 4K of
the screen, and the remaining portion of the screen is black.

###### Important

Higher resolution monitors require significantly more compute
capacity and encoding resources to stream content effectively, with
actual performance depending on your display configuration (resolution
and number of monitors) and the compute instance being used. If you
experience suboptimal performance on 4K monitors, we recommend
reducing your display resolution to improve responsiveness.

Ultrawide monitors with resolutions exceeding 4096 pixels in either
dimension (e.g., 5120x2160) will display black bars on the sides, as
the maximum supported resolution is limited to 4096 pixels per
dimension.

## Using Multiple Monitors

When using multiple monitors, you can choose from the following
options:

- Extend full-screen across a _single_
  monitor
- Extend full-screen across _all_ monitors
- Extend full-screen across _selected_
  monitors

### Extending full-screen across a single monitor

You can extend full screen only on the current monitor if multiple
monitors are connected to your local computer. To enable this feature,
complete the following steps:

1. On the toolbar at the top of the window, choose the Full
   Screen (crossed arrows) icon.
2. From the drop-down menu, choose **Across a single
   monitor**.

### Extending full-screen across all monitors

You can extend the display for a session across all monitors at full
screen resolution. The extended display matches your physical display
layout and screen resolutions. For example, three monitors are connected
to your local computer. The server extends the display for a session
across all three monitors and matches the specific screen resolutions of
your display.

To enable this feature, complete the following steps:

1. On the toolbar at the top of the window, choose the Full
   Screen (crossed arrows) icon.
2. From the drop-down menu, choose **Across all
   monitors**.

### Extending full-screen across selected monitors

If there are three or more monitors connected, WorkSpaces Applications can also extend
full-screen across a selection of those available monitors. If your
selected monitors cannot go full screen, an error message will appear
and you will need to perform the procedure again. Selected monitors must
be set adjacent, or sharing a side with each other, in your display
setting.

The following are examples of adjacent monitor placement. If your
monitors are not set adjacent in your Windows display configuration, you
must exit WorkSpaces Applications and change your Display settings on your local
machine.

###### Note

The blue boxes are WorkSpaces Applications-enabled monitors, and the gray boxes are
other monitors.

![Adjacent and nonadjacent monitor placement](images/monitors.PNG)

To enable this feature, complete the following steps:

1. On the toolbar at the top of the window, choose the Full
   Screen (crossed arrows) icon.
2. From the drop-down menu, choose **Across selected
   monitors**.
3. The **Across selected monitors** window
   appears, displaying your current monitor layout. Select which
   monitors you want DCV to be displayed full screen, and choose
   **Apply**.
