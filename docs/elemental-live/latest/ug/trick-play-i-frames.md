# Trick-play track via

I-frames

In an HLS output group, you can support a trick-play track by
providing an I-frame-only manifest.

## How the method

works

When you create the HLS output group, you create one or more video outputs,
in
the usual way. In each video output, you enable the field to
create an I-frame-only manifest that conforms to the HLS specification.

Elemental Live produces two child manifests for each encode
(stream)—one manifest for handling the video in the usual way,
and the I-frame-only manifest. The I-frame-only manifest lets
the downstream player identify specific video frames to request,
to construct the trick-play track. So this trick-play track
method doesn't produce additional encodes in the output group.

Each I-frame-only manifest contains the following:

- One `#EXT-X-I-FRAMES-ONLY` tag, to indicate
  that the manifest is I-frame-only.
- Many `#EXT-X-BYTERANGE` entries. Each entry
  identifies the position of an I-frame position.

## Setting up

You set up the trick-play track once for the entire HLS output
group.

###### Note

The information in this section assumes that you are
familiar with the general steps for creating an
event.

###### To set up an I-frame-only manifest

Include these steps when you create the HLS output group.

1. In the **HLS Output Group**, in
   **HLS Outputs**, choose
   **Add Output** to add an output. Or
   display an existing output.
2. In the output, choose **Advanced** to
   open that section, then select **Add I-frame
   Only Manifest**.
3. Set up the remaining fields in the output group as you
   normally would. Set up the video, audio, and captions
   outputs and encodes as you normally would.
