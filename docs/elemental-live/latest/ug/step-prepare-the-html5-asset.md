# Step B: Prepare the

HTML5 asset

You use an authoring system to create the asset and to manage the
content, including implementation of features such as fade or
opacity.

1.  Choose an authoring system and create the asset – Use the
    authoring system to create the asset. The HTML5 content must
    meet these requirements:

        * It can be any HTML5 authoring system that uses
         standard browser-based rendering techniques.
        * It can use any HTML5 tags except video and
         audio.
        * It can incorporate javascript that interacts with a
         backend system to dynamically control the asset that is
         being published to the source URL. You should size the
         content to be the same size or smaller than the width
         and height of the largest video rendition in your
         channel. You can also use responsive HTML (HTML that
         resizes automatically to different frame sizes).

    See the list after this procedure for more guidelines for
    preparing the asset.

2.  Make a note of the URL of the asset. This URL must be
    accessible to Elemental Live.
3.  If the location of the motion graphics asset requires login
    in order for Elemental Live to download the asset, make a note
    of the user name and password.
    **Supported authoring
    features**

The asset can include features that are supported in Chrome
version 84.0.4147.125. If you include features that are supported
only in a later version, the asset might not render properly in
Elemental Live.

**CPU requirements**

An HTML5 asset increases CPU utilization for each enabled event
by _up to_ 20%, depending on
complexity of the asset. For example, if your event currently uses
30% of CPU (without HTML5 motion graphics), it might use
approximately 36% with HTML5 motion graphics.

**Resolution**

Elemental Live renders the asset to match full-frame for the
resolution of the first video input. If the input resolution changes
during the event, Elemental Live will continue to render at the
initial resolution, but will scale up or down to match the asset's
new resolution.

We recommend that you set up the asset to have the same pixel
ratio as the video. The resolution of the asset can change through
the life of the event, but its ratio shouldn't change.

**Color space**

If you set up the event to [convert the color space](hdr-working-with.md "hdr-working-with.md") of the video, Elemental Live will
convert the asset in the same way. For example, it will convert the
color space to HDR10. To perform this conversion, Elemental Live will
assume that the asset color space is SDR.
