

# Use case D: One captions output shared by multiple video encodes
<a name="use-case-one-captions-output-multiple-video-encodes"></a>

This use case for deals with including captions in an ABR workflow in MediaLive.

For example, assume that there are three video/audio media combinations: one for low-resolution video, one for medium, and one for high. Assume that there is one output captions asset (English and Spanish embedded) that you want to associate with all three video/audio media combinations.

![Diagram showing input captions flowing to output captions, which connect to three video quality outputs and HLS output.](http://docs.aws.amazon.com/medialive/latest/ug/images/captions_INembed_OUTembed_ABRhls.png)
