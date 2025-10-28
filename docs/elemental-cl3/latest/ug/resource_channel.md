# Resources: Elemental Live Channels

This section describes how to use AWS Elemental Conductor Live to create, modify or delete a channel.

A _channel_ is a session that decodes and encodes a live
video stream or a video file and produces a live output. Video input comes into the channel and
video output is the final outcome of the channel. All the encoding activity occurs within a
channel.

When you use Conductor Live, you create a channel by first selecting a profile. If you aren't
familiar with profiles, first read [Creating a profile from
scratch](creating-a-profile-from-scratch.md "creating-a-profile-from-scratch.md").

After you have selected the profile, you complete fields that were set up as profile
parameters in the profile. When you save the channel, Conductor Live creates the channel using the
following data:

- The values that you entered in the profile parameters in the channel.
- The values that were set up as permanent values in the profile.
  You can't add or delete fields on the channel. Instead, you must use a profile that has all
  the fields and sections of fields that you need. Specifically, you can't add or delete output
  groups, outputs, or streams.

###### Topics

- [Creating a channel](creating-a-channel.md "creating-a-channel.md")
- [Creating a channel by duplicating an existing
  channel](creating-a-channel-by-duplicating.md "creating-a-channel-by-duplicating.md")
- [Modifying a channel](modifying-a-channel.md "modifying-a-channel.md")
- [Changing the profile used by
  multiple channels](changing-the-profile-used-by-multiple-channels.md "changing-the-profile-used-by-multiple-channels.md")
- [Deleting channels](deleting-channels.md "deleting-channels.md")
