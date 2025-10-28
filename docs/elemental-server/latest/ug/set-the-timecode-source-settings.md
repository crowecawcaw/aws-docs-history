This is version 2.18 of the AWS Elemental Server documentation.
This is the latest version. For prior versions, see
the _Previous Versions_ section of [AWS Elemental Conductor File and AWS Elemental Server Documentation](../../../elemental-server.md "../../../elemental-server.md").

# Setting the Timecode Source Settings

Before you start setting up the captions themselves, you need to make sure that the
timecode settings you make result in correctly synchronized captions. The simplest way to make
sure that your captions synchronize correctly with your video is to set both the input and
job-wide timecode source to **Start at 0** or to set them both to
**Embedded**.

###### Note

If you set both to **Embedded**, the timecodes in your captions files must
begin at the same time as the timecodes that are embedded in your input video.

###### To set your input timecode source setting

1. On the **Create New Job** page, in the **Input** section, under **Input 1**,
   choose **Advanced** to display more settings.
2. For **Timecode Source**, choose **Start at 0** or
   **Embedded**.

###### To set your job-wide timecode source setting

1. On the **Create New Job** page, at the bottom of the **Input** section, find the
   **Timecode Config** section.
2. For **Source** choose, choose the same value that you set for the input
   timecode source setting.
