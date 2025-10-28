This is version 2.18 of the AWS Elemental Server documentation.
This is the latest version. For prior versions, see
the _Previous Versions_ section of [AWS Elemental Conductor File and AWS Elemental Server Documentation](../../../elemental-server.md "../../../elemental-server.md").

# Choosing Between

Input, Stream, and Global Overlay

You can add still image overlays to your inputs, your streams, and throughout the
job globally. Where you specify your graphic overlays affects where in your
transcoded assets the overlays appear. One job can have any combination of input,
stream, and global overlays.

The following diagram shows how input, stream, and global overlays appear in the
video files that are created by a job. Input overlays appear on all outputs, but
only in the portions of the outputs that come from the input that has the
overlay.Stream overlays appear throughout the entirety of any output that uses the
stream. Global overlays appear on all outputs throughout the entire length of the
outputs.

###### Note

In this diagram, all overlays are specified for the entire duration of the
input or output. You can instead specify a shorter overlay duration within that
time.

![In this example, the job has three inputs. Input 1 and Input 3 have an input overlay. The job has two outputs. Output 1 has no overlays; output 2 has a stream overlay. The job has one overlay specified in the global job settings. The job produces two output files, which have the content from each of the inputs joined together. Output 1 has the global overlay and the input overlays, which appear at the beginning and end of the final asset. The middle portion of Output 1, made from the content of Input 2, has only the global overlay. Output 2 has the overlays in Output 1, plus the stream overlay for the entire duration of the asset.](images/image-inserter.png)

## Input Overlays

Choose input overlay for the following situations:

- You want the same overlays on every output.
- You want an overlay on only the parts of your outputs that correspond
  to individual inputs.

Here are examples of situations where you would use an input overlay:

- Some of your inputs already have your logo as an overlay and some of
  them don't. You want to add the logo to the inputs that don't already
  have it.
- Some of your inputs are programming that you want your logo on. Other
  inputs are advertisements or blank slates that you don't want your
  overlay on.
- Your job has only one input and you want your overlay to appear for
  the entire duration of the video on every output of the job.

## Global Overlays

Choose Global Overlay for these situations:

- You want overlays that appear the same way on every output.
- You have multiple inputs, but you want the same overlay across all of
  them.

## Stream Overlays

Choose Stream Overlay for the following situations:

- You want overlays on some outputs but not others.
- You want different overlays on different outputs.
- You want different overlays on different renditions within one ABR
  stack.
- You have multiple inputs, but you want the same overlay across all of
  them.

These examples are situations where you would use stream overlay:

- You set up a standalone file output with high definition and another
  standalone file output with standard definition. You want to include an
  HD indicator in the corner of the frame on the high definition output
  only.
- You set up one of the renditions in your ABR stack with high
  definition. You want to include an HD indicator in the corner of the
  frame on this rendition only.
- You are stitching together several films as separate inputs to create
  a single-asset film marathon. You want to put a graphic on all of them
  indicating that they are part of the larger marathon.
