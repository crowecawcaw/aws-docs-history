# Identify encode sharing

opportunities

If you have already identified the details for all the output encodes,
you can now identify opportunities for encode sharing.

If you plan to identify details later, we recommend that you come back
to this section to identify opportunties.

Read about encode sharing and encode cloning in [Sharing encodes among outputs](feature-share-encode.md "feature-share-encode.md").

You will use encode sharing and encode cloning when you create the
encodes in the channel, starting with [Set up the video encode](creating-a-channel-step6.md "creating-a-channel-step6.md").

- When you have a complete list, compare the values for the
  encodes:

      + If you have two (or more) encodes with identical values, you can
       share the encode. When you create the channel, you can create this encode
       once, in one output. You can then reuse that encode in other outputs. The
       procedure for creating the encode provides detailed instructions for
       reusing.


      Keep in mind that two encodes are identical only if they are
       identical in all their fields, including sharing the same video source.
       For example, in the sample table earlier in this section, the first video
       encode for HLS and the video encode for RTMP share the same video
       source.
      + If you have two (or more) encodes with nearly identical values, you
       can clone an encode to create a second encode, and then change specific
       fields in the second encode. The procedure for creating the encode
       provides detailed instructions for cloning.

  Then identify opportunities for sharing, in the same way as you did
  for the video encodes. Keep in mind that two encodes are identical only if
  they are identical in all their fields, including sharing the same audio
  source.

Carefully identify the video encodes to share by noting the outputs
and output groups each belongs to.
Then identify opportunities for sharing, in the same way as you did for
the video encodes. Keep in mind that two encodes are identical only if they
are identical in all their fields, including sharing the same captions
source.

**Example**

Following from the example in the earlier steps in this section about
channel planning, you might decide you have these opportunities shown in the
last two columns of this table.
