# Configuring inputs

If you want MediaLive to use the data in a SMPTE 2038 stream, you must
configure the input to read the SMPTE 2038.

1.  On the **Create channel** page, find the **Input
    attachment** for the relevant input.
2.  In **General input settings**, set
    **SMPTE-2038
    Data Preference** to one of the following:

        * **Prefer** – For a specific item of data, MediaLive first
         looks for the data in a SMPTE 2038 PID. If the data is not found in the SMPTE
         2038 stream or if there is no SMPTE 2038 stream, MediaLive looks for the data in
         other locations in the stream.
        * **Ignore** (default) – MediaLive never looks for a SMPTE
         2038 stream. Even if a specific item of data is not available in other places
         in the stream, MediaLive doesn't look for a SMPTE 2038 stream. For example, you
         might set the timecode source to Embedded (in the **General
         Configuration** section for the channel). With
         **Ignore**, if the timecode source isn't in the video
         stream, MediaLive won't look for it in a SMPTE 2038 stream.

    Note that with Elemental Link input, any KLV metadata is always in a SMPTE 2038, never
    in a different PID. Therefore, if you have been told that the source includes KLV
    metadata, always choose **Prefer**.
