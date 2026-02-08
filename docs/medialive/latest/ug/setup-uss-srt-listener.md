# Provide connection information to the upstream system

After you create the SRT Listener input, you must provide connection information to
the operator at the upstream system so they can configure their SRT caller to connect
to MediaLive.

###### To obtain the connection information

1. On the **Inputs** page, choose the name of the SRT Listener
   input that you just created.
2. On the input details page, in the **Destinations** section,
   note the IP addresses and port. For a standard-class input, there are two
   destinations. For a single-class input, there is one destination.

The destinations will be in the format
`srt://`ip-address`:5050`. For example:

`srt://54.123.45.67:5050`

`srt://54.123.45.68:5050` 3. Provide these destination URLs to the operator of the upstream system. The
operator must configure their SRT caller to connect to these addresses.
Make sure that the operator at the upstream system sets up as follows:

- They set up to deliver the correct number of sources:
  - If the MediaLive channel is a standard channel, they must push to both
    destination addresses. Make sure that the two source contents are
    identical in terms of video resolution and bitrate.
  - If the MediaLive channel is a single-pipeline channel, they must push to
    the single destination address.

- They configure their SRT caller to use the same encryption algorithm and
  passphrase that you agreed on.
- They configure their SRT caller to use a latency value. SRT will negotiate
  and use the maximum of the latency values configured on both sides.
- If you specified a stream ID in the input configuration, the upstream system
  can optionally send a stream ID value during connection. MediaLive accepts connections
  with any stream ID value (or no stream ID). The stream ID is logged for
  monitoring and troubleshooting purposes only.
