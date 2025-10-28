# Defining audience cohorts and alternate content with Program Rules

With Program Rules, you can define audience cohorts for a channel and specify alternate
media to play for those audiences. You can associate one or more alternate content sources
with an audience for a program. After the program ends, the default audience content will play
unless you specify further alternate media.

Program Rules are available on STANDARD tier channels with the LINEAR playback mode. MediaTailor
channels support alternate media for all VOD sources and live sources.

For an example use, see [Using program rules with AWS MediaTailor](https://aws.amazon.com/blogs/media/using-program-rules-with-aws-elemental-mediatailor/ "https://aws.amazon.com/blogs/media/using-program-rules-with-aws-elemental-mediatailor/").

## Defining audiences

Define audiences on a channel by typing audience one by one when configuring a MediaTailor
channel. You can do this through either the MediaTailor console or the MediaTailor
`CreateChannel` API. Each audience must be between 1 and 32 alphanumeric
characters long. If the values provided for the audiences are invalid, then the request
fails.

You can only define audiences on STANDARD tier channels with the LINEAR playback mode.

When you need to update the audiences, you can do this using either the MediaTailor console or the MediaTailor `UpdateChannel` API.

If you are using the `ProgramRules` feature, make sure that the `AudienceMedia` defined in `CreateProgram` or `UpdateProgram` request contain the existing audience defined in the channel.

## Creating alternate media

The following task explains how to define alternate media using the MediaTailor console. For
information about how to define alternate media using the MediaTailor API, see [`CreateProgram`](../apireference/API_CreateProgram.md "../apireference/API_CreateProgram.md") in the _AWS Elemental MediaTailor API Reference_.

To define alternate media on a new program:

1.  Open the MediaTailor console at [https://console.aws.amazon.com/mediatailor/](https://console.aws.amazon.com/mediatailor/ "https://console.aws.amazon.com/mediatailor/").
2.  In the navigation pane, select **Channel assembly** >
    **Channels**.
3.  Select the channel name to which you want to add alternate media.
4.  Create a program. For more information, see [Creating a program within a channel schedule using the MediaTailor console](channel-assembly-adding-programs.md "channel-assembly-adding-programs.md").
5.  Configure alternate media:
    - Select **Add** in the **Audiences** box to
      select the audience for which you are defining alternate media.
    - Select an audience defined on the channel from the **Audience** menu.
    - Select **Add alternate media** to begin defining alternate
      media for the program.
    - MediaTailor creates an **Alternate media
      1** box. This is the first content that MediaTailor plays as alternate media on
      the program.
    - Within the **Alternate media 1** box:
      - Select a **Source Location**.
      - Select either a **VOD** or **Live**
        Source Type:

      For VOD

          - Select VOD for the **Source Type**.
          - (Optional) specify a **Clip Range**. With VOD Sources,
           including alternate-media VOD sources, you can specify a portion of a VOD
           source to play, clipping from the start and/or the end of the source.
           Specify The start and end offsets are in milliseconds.
          - (Optional) a\Add Ad Breaks. This is done in the same way as when creating
           programs. For more information, see [Creating a program within a channel schedule using the MediaTailor console](channel-assembly-adding-programs.md "channel-assembly-adding-programs.md").

      For Live

          - Select Live for the **Source Type**.
          - Select a **Live source**.
          - Enter a **Start time** in milliseconds of the wal-clock
           time that this live source should start. The live source will only play
           within the time frame of the default program it is being defined on. If the
           start time is prior to the start of the default program, it will not begin
           until the default program does. If the start time is after the default
           program ends, MediaTailor will not play the live source.
          - Enter a **Duration** in milliseconds. The duration must
           be at least 10 minutes in length.
          - Additional alternate media can be added to this program for the audience
           by selecting **Add alternate media** again. This will
           create another box labeled **Alternate media 2**. You can
           specify upp to 5 alternate-media sources per program, per audience.
          - Once you are finished defining alternate media for all desired
           audiences, select **Next** and continue creating the program.


          For more information, see [Creating a program within a channel schedule using the MediaTailor console](channel-assembly-adding-programs.md "channel-assembly-adding-programs.md").

    ###### Note

    Alternate media only plays in the time frame of the program it is defined on.
    If all the alternate content overruns the default content, MediaTailor will truncate it.
    MediaTailor plays alternate media in the order in which it is defined. Live
    alternate-media start times will always take precedence and will truncate
    previously scheduled VOD sources or live sources. Any time that is not filled with
    alternate media for an audience will be filled withe the channel-defined filler
    slate
    - To define audience media for other audiences, select **Add**
      once again next to **Audiences**. Select the newly created
      audience, set the audience id and add alternate media as described above. Up to 5
      audiences can have alternate media on any one program.
