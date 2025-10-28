This is version 2.18 of the AWS Elemental Server documentation.
This is the latest version. For prior versions, see
the _Previous Versions_ section of [AWS Elemental Conductor File and AWS Elemental Server Documentation](../../../elemental-server.md "../../../elemental-server.md").

# Using Dolby Atmos Passthrough with

AWS Elemental Server

AWS Elemental Server can create Dolby Digital Plus with Atmos outputs by either encoding
audio in 9.1.6, 7.1.4, or 5.1.4 PCM mono channels, or by passing through already encoded Dolby Digital
Plus with Atmos content.

You set up your job to pass through Dolby Digital Plus with Atmos content in the same
way that you pass through Dolby Digital and Dolby Digital Plus content.

###### To set up a Dolby Atmos job, passing through finished audio content

1. Set up your input audio and video as usual.
2. Create outputs and streams. To set up the audio in your streams, for
   **Audio Codec**, choose **Dolby Digital Pass Through**.

## Feature

Restrictions for Dolby Atmos Passthrough

Note the following restrictions in the AWS Elemental Server implementation of Dolby
Atmos passthrough:

- **Output codec:** You can create Dolby Atmos
  audio outputs encoded with only the Dolby Digital Plus (EAC3) codec.
- **Output containers:** For file outputs, you
  can create Dolby Atmos audio in only one of the video containers that
  supports Dolby Digital Plus: MPEG-4, MPEG-2 Transport Stream, or
  QuickTime.
