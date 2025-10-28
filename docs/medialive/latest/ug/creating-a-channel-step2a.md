# Complete the settings for each input

As soon as you attach the input on the **Attach
input** sections, the **Input
attachment** section closes and the **General
input settings** section appears for that input. You
must complete these fields to configure the input:

- Configure the input connection.

- Identify the video, audio, and captions to extract from the input.

###### To configure the input

1. Complete the fields as required. See the topics links below. For details about
   a field, choose the **Info** link next to the field on the
   MediaLive console:
   - For most fields, the default values are sufficient.
   - However, if you want to include audio and captions in the outputs, you
     must complete the **Audio selectors** and
     **Caption selectors** sections; the defaults do not
     specify enough information.

2. Complete the following field in the **General settings**
   section in the navigation pane:
   - **Global configuration** - **Input loss
     behavior**. These fields configure how the channel behaves
     when it stops receiving content from any input. For more details, see
     [Handling loss of video input](feature-input-loss.md "feature-input-loss.md"). These fields apply to all
     inputs, therefore you only need to set them once for the entire
     channel.

3. If you are setting up the channel with multiple inputs, add more inputs to the
   channel. For guidelines about implementing input switching, see [Setting up for input switching](scheduled-input-switching.md "scheduled-input-switching.md").
4. When ready, go to the [next
   step](creating-a-channel-step3.md "creating-a-channel-step3.md").

###### Topics

- [Input settings—Network input
  settings](input-network-input.md "input-network-input.md")
- [Input settings—Other settings](input-other-settings.md "input-other-settings.md")
- [Input settings—Video selector](input-video-selector.md "input-video-selector.md")
- [Input settings—Audio
  selectors](input-audio-selectors.md "input-audio-selectors.md")
- [Input settings—Caption
  selectors](input-caption-selectors.md "input-caption-selectors.md")
