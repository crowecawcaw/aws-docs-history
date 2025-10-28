# Viewing thumbnails on the

console

When thumbnails is enabled, MediaLive generates thumbnails for the currently active input
in a channel that is running. For a standard channel, MediaLive generates two thumbnails.
For a single-pipeline channel, MediaLive generates one thumbnail.

1. Open the MediaLive console at [https://console.aws.amazon.com/medialive/](https://console.aws.amazon.com/medialive/ "https://console.aws.amazon.com/medialive/").
2. Choose **Channels** from the navigation
   bar. On the list of channels, select the channel by its
   name. The Details page appears.

The **Status** section includes a
thumbnail frame. If the channel has two inputs, the screen
includes a tab for each input.
When the channel is running and the Details page is displayed, the
thumbnail automatically updates every 2 seconds, for the pipeline in
the active tab. MediaLive doesn't generate any thumbnails if this page
isn't displayed.

If the channel isn't running, the frame is black.

If the channel stops running, the thumbnail preview stops
updating. After a few seconds, the current thumbnail is replaced by
a message.
