

# All captions except sidecar or SMPTE-TT in MS Smooth
<a name="output-embedded-and-more"></a>

Follow this procedure if the format of the captions asset that you want to add belongs to the category of embedded, burn-in, or object. You will set up the captions and video and audio in the same output.

**To create captions (*not* sidecar or SMPTE-TT)**

1. On the web interface, on the **Event** screen, click the appropriate output group.

1. If you have already set up this output group with video and audio, find the outputs where you want to add the captions. Or if you have not set up with video and audio, create a new output in this output group; you can set up the captions now and you can set up the video and audio later.

1. Go to the output, then go to the stream that is associated with that output. For example, go to Stream 1.

1. Click the \+ beside **Caption** to add a Caption section.

1. Complete the fields that appear for the selected format. For details about a field, choose the Info link beside the field.     
[See the AWS documentation website for more details](http://docs.aws.amazon.com/elemental-live/latest/ug/output-embedded-and-more.html)

1. If the output format is embedded and the output group is HLS, you can include captions language information in the manifest. You perform this setup in the output settings (separate from the captions encode). See [Set up the HLS Manifest (embedded captions)](set-up-the-hls-manifest.md).

1. If the output format is ARIB or DVB-Sub or SCTE-27, you must perform some extra setup in the output settings (separate from the captions encode). See [PIDS for ARIB output](complete-the-pids-for-arib.md) or [PIDs for DVB-Sub output](complete-the-pids-for-dvb-sub.md) or [PIDs for teletext output](complete-the-pids-for-teletext.md).

1. You now have a captions encode that is fully defined.

1. Repeat these steps to create captions, as applicable.

1. Go to the output group and output that this stream belongs to. Set the Stream field in that output to match the stream you created. 

1. When you are ready, save the event. 

   If the “Caption Stream Incompatible” message appears, see ["Caption Stream Incompatible" message](#embedded-caption-incompatible-message).

## "Caption Stream Incompatible" message
<a name="embedded-caption-incompatible-message"></a>

When you save the event, this validation message might appear:

Stream Caption Destination Type Is Incompatible With XX Output...

Typically, this error will occur because of the following scenario:
+ You have two outputs – perhaps HLS and DASH – that will have the same audio and video descriptions, which means you want them to share the same stream:
+ You set up the HLS output group and add an Output and Stream 1. You add embedded captions.
+ You then set up the DASH output group and add an Output and associate that output with the existing Stream 1.
+ The problem is that DASH cannot contain embedded captions. Therefore, when you save the event, you will get the validation message.

The solution to this problem is:
+ When you set up the DASH output, instead of associating it with the existing Stream 1, create a new stream (Stream 2)
+ In Stream 2, set up the video and audio to be identical to the video and audio in Stream 1.
+ For the DASH output, add the captions in the appropriate way.

The result: Assuming that you have set up the video and audio in both streams to be identical, the encoder will notice that they are identical and will in fact encode the video only once and the audio only once. So there will be no extra video encoding load from creating separate streams.