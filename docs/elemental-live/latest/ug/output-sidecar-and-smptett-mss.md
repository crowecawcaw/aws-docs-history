

# Sidecar captions or SMPTE-TT captions in MS Smooth
<a name="output-sidecar-and-smptett-mss"></a>

Follow this procedure if the format of the captions asset that you want to add is a sidecar, as identified in [Step 4: Match formats to categories](categories-captions.md), or if the format is SMPTE-TT for an MS Smooth output.

When you follow this procedure, you set up each captions asset in its own output within the output group. When the event runs, the captions will be set up as sidecars in the output package, except for SMPT-TT captions in MS Smooth, which will be set up as streams in the output package.

**To create captions (sidecar and SMPTE-TT)**

1. On the web interface, on the **Event** screen, click the output group. (You should have already created this output group).

1. In the output group, choose **Add Output**. A new output appears, and by default this output has one stream. Make note of this stream. For example, **Stream 2**.

1. In the **Streams** section (for example, in **Stream 2**), hover over **Video** and choose the **x** icon. Hover over **Audio** and choose the **x** icon. The stream is now empty. 

1. Beside **Captions**, choose the **\+** icon. The stream now contains one captions encode and no video or audio encodes.

1. Complete the fields as shown in the table after this procedure.

1. Repeat these steps to create more sidecar captions in this or another output group, as applicable.

1. When you are ready, save the event.

   If the “Caption Stream Incompatible” message appears, see ["Caption Stream Incompatible" message](output-embedded-and-more.md#embedded-caption-incompatible-message).    
[See the AWS documentation website for more details](http://docs.aws.amazon.com/elemental-live/latest/ug/output-sidecar-and-smptett-mss.html)

## "Caption Stream Incompatible" message
<a name="sidecar-caption-incompatible-message"></a>

When you save the event, this validation message might appear:

Stream Caption Destination Type Is Incompatible With XX Output...

Typically, this error will occur because of the following scenario:
+ You have two outputs – perhaps HLS and RTMP – that will have the same audio and video descriptions, which means you want them to share the same stream:
+ You set up the HLS output group and add an Output and Stream 1. You add embedded captions.
+ You then set up the RTMP output group and add an Output and associate that output with the existing Stream 1.
+ The problem is that RTMP cannot contain embedded captions. Therefore, when you save the event, you will get the validation message.

The solution to this problem is:
+ When you set up the RTMP output, instead of associating it with the existing Stream 1, create a new stream (Stream 2)
+ In Stream 2, set up the video and audio to be identical to the video and audio in Stream 1.
+ For the RTMP output, add the captions in the appropriate way.

The result: Assuming that you have set up the video and audio in both streams to be identical, the encoder will notice that they are identical and will in fact encode the video only once and the audio only once. So there will be no extra video encoding load from creating separate streams.