This is version 2.18 of the AWS Elemental Server documentation.
This is the latest version. For prior versions, see
the _Previous Versions_ section of [AWS Elemental Conductor File and AWS Elemental Server Documentation](../../../elemental-server.md "../../../elemental-server.md").

# Still Image Inserter (Graphic Overlay) in

AWS Elemental Server

The following procedure walks you through setting up a still graphic overlay. To
begin, decide where in your job to specify the overlay. This choice affects how the
overlay appears in outputs.

###### Note

One job can have any combination of input, stream, and global overlays. To set up
multiple overlays, repeat this procedure.

###### To set up a still image overlay

1. Decide where in your job to specify the overlay.For information about how this
   choice affects how the overlay appears in the outputs, see [Choosing Between
   Input, Stream, and Global Overlay](choosing-between-input-overlay-and-output-overlay.md "choosing-between-input-overlay-and-output-overlay.md").
2. Prepare your overlay file.For more information, see [Overlay File
   Requirements](requirements-for-the-overlay-file.md "requirements-for-the-overlay-file.md") and [Sizing Your Overlay to Account for
   Scaling](about-overlay-scaling.md "about-overlay-scaling.md").
3. In the appropriate section of the job, choose the **Image
   Inserter** slider and then choose **Add Image**.
   Find the appropriate sections as follows:
   - Find the dark gray **Input** section at the top of
     the job.
   - Find the medium gray **Global Processors** section
     just below the **Input** section.
   - Add **Stream** sections in the
     **Output** sections that are on the appropriate
     group tab in the very light gray **Output Groups**
     section at the bottom of the job.

4. Specify values for the image inserter settings. For more information about
   these specific settings, see the following topics:
   - For information about **Start Time**,
     **Duration**, **Fade In**, and
     **Fade Out**, see [Setting Up When Your Overlay
     Plays](when-your-still-overlay-plays.md "when-your-still-overlay-plays.md").
   - For information about **Layer**, see [Setting Up Overlapping Overlays](using-multiple-overlays.md "using-multiple-overlays.md").
