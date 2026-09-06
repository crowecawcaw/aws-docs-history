

# Reserved queue job settings limitations
<a name="feature-limitations-with-reserved-queues"></a>

The following features are available only in jobs that you send to an *on-demand* queue. For jobs that you send to a *reserved* queue, you must disable the following features:
+ [8k output resolution](supported-output-resolution-maximums-by-codec.md)
+ [Automated ABR](auto-abr.md)
+ [AV1 encoding](reference-codecs-containers.md)
+ [Dolby Vision encoding](dolby-vision.md)
+ [MV-HEVC spatial video encoding](mv-hevc-spatial-video.md)
+ [FrameFormer frame rate conversion algorithm](working-with-video-frame-rates.md#settings-for-frame-rate-conversion)
+ [Accelerated transcoding](accelerated-transcoding.md)
**Note**  
Reserved queues cannot run accelerated jobs. However, you can submit a job to a reserved queue with **Accelerated transcoding** set as **Preferred**. When you do, if the job hops to an on-demand queue, it will run with acceleration. For more information, see [Using accelerated transcoding with hopped jobs](accelerated-transcoding-queue-hopping.md).