# Creating a program within a channel schedule using the MediaTailor console

The following procedure describes how to create a program within your channel's schedule
using the MediaTailor console. It also describes how to configure ad breaks, which are optional. For
information about how to create programs using the MediaTailor API, see [CreateProgram](../apireference/API_CreateProgram.md "../apireference/API_CreateProgram.md") in the
_AWS Elemental MediaTailor API Reference_.

###### To add a program

1.  Open the MediaTailor console at [https://console.aws.amazon.com/mediatailor/](https://console.aws.amazon.com/mediatailor/ "https://console.aws.amazon.com/mediatailor/").
2.  In the navigation pane, choose **Channel assembly** >
    **Channels**.
3.  In the **Channels** pane, choose the channel that you created in the
    [To create a channel](channel-assembly-creating-channels.md#create-channel-procedure "channel-assembly-creating-channels.md#create-channel-procedure")
    procedure.
4.  In the **Program details** enter details about your program:
    - **Name**: This is the name of the program that you add to your channel.
    - **Source type**: Determines what type of source video the program plays. This option is only available for Standard channels.
      - **VOD** - The program plays a video-on-demand source, such as a pre-recorded TV episode.
      - **Live** - The program plays a live source, such as a live news broadcast.

    - **Source location name**: The source location that MediaTailor associates with the program.
      - If you choose **Select an existing source location**, choose a sourcelocation name from the **Select a source location** menu. Alternatively, search for your source location by name. This is helpful if you have a large number of source locations.
      - If you choose **Enter the source location name**, search for your source location by name.
      - **VOD source name**: The name of the VOD source that MediaTailor associates with the program:
        - If you choose **Select an existing VOD source**, select a VOD source name from the list of VOD sources that are associated with your account. Alternatively, search for your VOD source by name. This is helpful if you have a large number of VOD sources.
        - If you choose **Search by name**, search for your live source by name.

      - **Live source name**: The name of the live source to be associated with the program. This option is only available if you selected **Live** as the source type.
        - If you choose **Select an existing source location**, choose a sourcelocation name from the **Select a source location** menu. Alternatively, search for your source location by name. This is helpful if you have a large number of source locations.
        - If you choose **Enter the source location name**, search for your source location by name.
        - **VOD source name**: The name of the VOD source that MediaTailor associates with the program:
          - If you choose **Select an existing live source**,select a live source name from the list of live sources that are associated with your account. You can alternatively search for your live source by name. This is helpful if you have a large number of live sources.
          - If you choose **Search by name**, search for your live source by name.

5.  Select **Next** to go to the **Schedule Configuration** tab.
6.  Under **Playback configuration**, define when a program plays in your channel's schedule:

        * **Duration in milliseconds**: Defines the duration of the program in milliseconds. This option is only available for programs that use live sources.
        * **Transition type**: Defines the transitions from program to program in the schedule:




        	+ **Relative**: The program plays either before or after another program in the schedule. This option is only available for programs that use VOD sources.
        	+ **Absolute**: The program plays at a specific wall-clock time. MediaTailor makes a best effort to play the program at the clock time that you specify. MediaTailor starts playback of the program on a common segment boundary between the preceding program or slate. This option is only available for channels configured to use the linear .
        	+ **Program start time**: For absolute transition types, the wall-clock time when the program is scheduled to play. If you are adding this program to a running linear channel, you must enter a start time that's 15 minutes or later from the current time.
        	+ **Relative position**: Choose where to insert the program into the schedule, relative to another program. You can select **Before program** or **After program**. This setting does not apply if this is the first program in your channel's schedule.




        		- If you choose **Select an existing program**, select the program name from a predefined list of the next 100 programs played by the channel from the **Use existing program** menu.
        		- If you choose **Search for a program by name**, enter the name of an existing program in your channel.

    If you'd like to add ad breaks to your program, continue to the next step. Ad breaks are only configurable for programs that use VOD sources. For live sources, ad breaks in DASH manifests and ad breaks in HLS manifests that use the `EXT-X-DATERANGE` tag are passed through automatically.

7.  Select **Next** to go to **Add ad breaks**.
8.  Select **Add ad break**. Under **Ad breaks**, configure the settings for the ad break:
    - **Slate source location name**: Choose **Select an existing source location** and choose the source location where your slate is stored that you created earlier in this task.
    - **VOD source name**: Choose **Select an existing VOD source** and choose the VOD source you're using for slate that you added earlier in this task. The duration of the slate determines the duration of the ad break.
    - **Offset in milliseconds**: This value determines the ad break start time in milliseconds, as an offset relative to the beginning of the program. Enter any value that's less than the duration of the VOD source, and that aligns with a segment boundary on all tracks within the program's VOD source (all audio, video and closed caption tracks), otherwise the ad break will be skipped. For example, if you enter **0**, this creates a pre-roll ad break that plays before the program begins.
    - **Avail number**: MediaTailor writes this value is written to
      `splice_insert.avail_num`, as defined in section 9.7.3.1. of the SCTE-35
      specification, [Digital Program Insertion Cueing Message](https://webstore.ansi.org/Standards/SCTE/ANSISCTE352022 "https://webstore.ansi.org/Standards/SCTE/ANSISCTE352022"). The default value is 0. Values
      have to be between 0 and 256, inclusive.
    - **Avail expected**: MediaTailor writes this value to `splice_insert.avails_expected`, as defined in section 9.7.3.1. of the SCTE-35 specification. The default value is 0. Values have to be between 0 and 256, inclusive.
    - **Splice event ID**: MediaTailor writes this value to `splice_insert.splice_event_id`, as defined in section 9.7.3.1. of the SCTE-35 specification. The default value is 1.
    - **Unique program ID**: MediaTailor writes this value to
      `splice_insert.unique_program_id`, as defined in section 9.7.3.1. of the
      SCTE-35 specification. The default value is 0. Values have to be between 0 and 256,
      inclusive.

9.  For a Standard Linear Channel, select **Next** to go to **Set alternate media**.

For more information on using MediaTailor to create alternate media, see [Creating alternate media](working-with-program-rules.md#program-rules-creating-alternate-media "working-with-program-rules.md#program-rules-creating-alternate-media").

For more advanced information on using MediaTailor to personalize your ad breaks, see [Insert personalized ads and ad
breaks in a channel stream](channel-assembly-integrating-mediatailor-ssai.md "channel-assembly-integrating-mediatailor-ssai.md"). 10. Select **Next** to go to **Review and create**. 11. Select **Add program**.

For more advanced information on using MediaTailor to personalize your ad breaks, see [Insert personalized ads and ad
breaks in a channel stream](channel-assembly-integrating-mediatailor-ssai.md "channel-assembly-integrating-mediatailor-ssai.md"). 12. ###### Important

For looping channels, if you modify the program list for a program that is scheduled
within the next 10 minutes, the edit won't become apparent until the next loop.

Under **Program details**, enter details about your program:

    * **Name**: This is the name of the program that you add to your
     channel.
    * **Source type**: Determines what type of source the program
     plays. This option is only available for Standard channels.




    	+ **VOD** - The program plays a VOD source, such as a
    	 pre-recorded TV episode.
    	+ **Live** - The program plays a live source, such as a live
    	 news broadcast.
    * **Source location name**: The source location to be associated
     with the program.


    If you choose **Select an existing source location**, select a
     source location name from the **Select a source location** drop-down
     menu. You can alternatively search for your source location by name. This is helpful
     if you have a large number of source locations.


    If you choose **Enter the source location name**, search for your
     source location by name.
    * **VOD source name**: The name of the VOD source to be associated
     with the program.


    If you choose **Select an existing VOD source**, select a VOD
     source name from the list of VOD sources that are associated with your account. You
     can alternatively search for your VOD source by name. This is helpful if you have a
     large number of VOD sources.


    If you choose **Search by name**, search for your VOD source by
     name.
    * **Live source name**: The name of the live source to be
     associated with the program. This option is only available if you selected
     **Live** as the source type.


    If you choose **Select an existing live source**, select a live
     source name from the list of live sources that are associated with your account. You
     can alternatively search for your live source by name. This is helpful if you have a
     large number of live sources.


    If you choose **Search by name**, search for your live source by
     name.

13. Under **Playback configuration**, define when a program plays in your
    channel's schedule:

        * **Duration in milliseconds**: Defines the duration of the program
         in milliseconds. This option is only available for programs that use live
         sources.
        * **Transition type**: Defines the transitions from program to
         program in the schedule.




        	+ **Relative** - The program plays either before or after
        	 another program in the schedule. This option is only available for programs that
        	 use VOD sources.
        	+ **Absolute** - The program plays at a specific wall clock
        	 time. MediaTailor makes a best effort to play the program at the clock time that you
        	 specify. We start playback of the program on a common segment boundary between the
        	 preceding program or slate. This option is only available for channels configured
        	 to use the [linear playback mode](channel-assembly-creating-channels.md#linear-playback-mode "channel-assembly-creating-channels.md#linear-playback-mode").


        	###### Note

        	Be aware of the following behavior for absolute transition types:



        		- If the preceding program in the schedule has a duration that extends
        		 beyond the wall clock time, MediaTailor truncates the preceding program on the
        		 common segment boundary closest to the wall clock time.
        		- If there are gaps between programs in the schedule, MediaTailor plays [filler slate](channel-assembly-creating-channels.md#filler-slate "channel-assembly-creating-channels.md#filler-slate"). If the duration of the slate is less than the
        		 duration of the gap, MediaTailor loops the slate.
        * **Program start time** - For absolute transition types, the wall
         clock time when the program is scheduled to play. If you are adding this program to a
         running linear channel, you must enter a start time that's 15 minutes or later from
         the current time.
        * **Relative position**: Choose where to insert the program into
         schedule relative to another program. You can select **Before
         program** or **After program**. This setting does not
         apply if this is the first program in your channel's schedule.
        * **Relative program**: The name of the program to be used to
         insert the new program before or after. This setting does not apply if this is the
         first program in your channel's schedule.


        If you choose **Select an existing program**, select the program
         name from a predefined list of the next 100 programs played by the channel in the
         **Use existing program** drop-down menu.


        If you choose **Search for a program by name**, enter name of an
         existing program in your channel.

    If you'd like to add ad breaks to your program, continue to the next step. Ad breaks
    are only configurable for programs that use VOD sources. For live sources, ad breaks in
    DASH manifests and ad breaks in HLS manifests that use the `EXT-X-DATERANGE`
    tag are passed through automatically.

14. Select **Add ad break**. Under **Ad breaks**,
    configure the settings for the ad break:
    - **Slate source location name**: Choose **Select an
      existing source location** and choose the source location where your slate
      is stored that you created earlier in this tutorial.
    - **VOD source name**: Choose **Select an existing VOD
      source** and choose the VOD source you're using for slate that you added
      earlier in this tutorial. The duration of the slate determines the duration of the ad
      break.
    - For **Offset in milliseconds**: This value determines the ad
      break start time in milliseconds, as an offset relative to the beginning of the
      program. Enter any value that's less than the duration of the VOD source, and that
      aligns with a segment boundary on all tracks within the program's VOD source (all
      audio, video and closed caption tracks), otherwise the ad break will be skipped. For
      example, if you enter **0**, this creates a pre-roll ad break that
      plays before the program begins.

    ###### Note

    If MediaTailor detects ad markers, such as`DATERANGE` or
    `EXT-X-CUE-OUT` for HLS and `EventStream` for DASH, with
    durations of zero within your VOD source, you can select the offset of those ad
    markers from the drop-down menu to be used as the ad break’s offset. In order for an
    ad opportunity to be detected, it must be present at the same offset across all
    package configurations within a VOD source, and its duration must be zero.
    - **Message type**: The SCTE-35 ad insertion type. Choose either
      **SPLICE_INSERT** or **TIME_SIGNAL**:

          + **SPLICE\_INSERT**: Provides basic metadata about the ad break
           using splice insert parameters.
          + **TIME\_SIGNAL**: Provides more advanced metadata using
           segmentation descriptors. For more information about the differences between
           message types, see [SCTE-35 messages for ad breaks](ca-scte-35-messages.md "ca-scte-35-messages.md").

      For **SPLICE_INSERT** message type:

          + For **Avail number**, this is written to
           `splice_insert.avail_num`, as defined in section 9.7.3.1. of the
           SCTE-35 specification. The default value is `0`. Values have to be
           between `0` and `256`, inclusive.
          + For **Avail expected**, this is written to
           `splice_insert.avails_expected`, as defined in section 9.7.3.1. of
           the SCTE-35 specification. The default value is `0`. Values have to be
           between `0` and `256`, inclusive.
          + For **Splice event ID**, this is written to
           `splice_insert.splice_event_id`, as defined in section 9.7.3.1. of
           the SCTE-35 specification. The default value is `1`.
          + For **Unique program ID**, this is written to
           `splice_insert.unique_program_id`, as defined in section 9.7.3.1. of
           the SCTE-35 specification. The default value is `0`. Values have to be
           between `0` and `256`, inclusive.

      For **TIME_SIGNAL** message type:

          + For **Segmentation event ID**, this is written to
           `segmentation_descriptor.segmentation_event_id`, as defined in
           section 10.3.3.1 of the SCTE-35 specification. The default value is
           `1`.
          + For **Segmentation type ID**, this is written to
           `segmentation_descriptor.segmentation_type_id`, as defined in section
           10.3.3.1 of the SCTE-35 specification. The default value is `48`
           (0x30). Values have to be between `0` and `256`,
           inclusive.
          + For **Segmentation UPID**, this is written to
           `segmentation_descriptor.segmentation_upid`, as defined in section
           10.3.3.1 of the SCTE-35 specification. The value must be a hexadecimal string
           containing characters `0-9` and `A-F`. The default value is
           an empty string.
          + For **Segmentation UPID type**, this is written to
           `segmentation_descriptor.segmentation_upid_type`, as defined in
           section 10.3.3.1 of the SCTE-35 specification. The default value is
           `14` (0x0E). Values have to be between `0` and
           `256`, inclusive.
          + For **Segment number**, this is written to
           `segmentation_descriptor.segment_num`, as defined in section 10.3.3.1
           of the SCTE-35 specification. The default value is `0`. Values have to
           be between `0` and `256`, inclusive.
          + For **Segments expected**, this is written to
           `segmentation_descriptor.segments_expected`, as defined in section
           10.3.3.1 of the SCTE-35 specification. The default value is `0`. Values
           have to be between `0` and `256`, inclusive.

15. Choose **Add program**.

For more advanced information using MediaTailor to personalize your ad breaks, see [Insert personalized ads and ad
breaks in a channel stream](channel-assembly-integrating-mediatailor-ssai.md "channel-assembly-integrating-mediatailor-ssai.md").

###### Note

If your channel has at least one output with an `Enhanced Scte35` Ad markup
type, you can submit ad-break metadata. MediaTailor writes the submitted key-value pairs to the
`EXT-X-ASSET` tag for your ad break.
