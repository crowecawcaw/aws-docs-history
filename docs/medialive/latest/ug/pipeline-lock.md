# Implementing pipeline locking

You can configure MediaLive to use pipeline locking to synchronize outputs. Pipeline locking
works with standard channels (which have two pipelines) and with single-pipeline channels
using linked channels. Pipeline locking ensures that the outputs are frame-accurate with
each other. Pipeline locking is enabled by default.

When pipeline locking
is enabled. MediaLive locks the pipelines on a best-efforts basis. When
pipeline locking isn't possible, processing continues. The inability to lock pipelines isn't
considered to be a fault condition.

The default mode for pipeling locking is pipeline locking You can't disable pipeline
locking in the applicable output types. But you should configure the behavior, to make sure
it suits your workflow.

###### Note

You might be familiar with the term _output locking_.
In MediaLive, the term used is _pipeline locking_. Whatever
term is used, the effect is identical: frame accurate outputs.

**Pipeline locking modes**

There are two output locking modes:

- Pipeline locking (the default): lock the two pipelines to each other
- Epoch locking: lock the pipelines using the Unix epoch as the reference.
  **Pipeline locking methods**

When you use pipeline locking mode, you can choose the method that MediaLive uses to
synchronize the pipelines:

- Source timecode (the default): MediaLive uses embedded timecodes from the input
  source to synchronize the pipelines. This method works best with reliable
  timecodes.
- Video alignment: MediaLive uses visual signature comparison between encoders to
  synchronize the pipelines. This method does not require embedded timecodes and
  is useful when your input sources lack timecodes or have unreliable timecodes.
  For more information, see [Requirements for
  video aligned pipeline locking](pipeline-locking-verify-input.md#pipeline-locking-video-alignment-inputs "pipeline-locking-verify-input.md#pipeline-locking-video-alignment-inputs").
  **Applicable outputs**

**Source timecode** pipeline locking applies only to the following types of outputs:

- HLS (Live mode)
- MediaPackage
- CMAF Ingest
- Microsoft Smooth
- UDP outputs
  that are segmented. You might have configured a UDP output group for segmented
  outputs. To verify, in a UDP output group, choose **Output** then
  **Network Settings**, then **Container
  Settings**. Look for the three fields that start with the term
  _Segmentation_.
  **Video aligned** pipeline locking applies only to the following types of outputs:

- HLS (Live mode)
- CMAF Ingest
  The channel can contain other types of outputs, but MediaLive won't attempt to lock their
  outputs. This means that in those other output groups, there is no guarantee that the
  content of the two pipelines will be frame-accurate with each other.

###### Topics

- [Input and output
  requirements](pipeline-locking-verify-input.md "pipeline-locking-verify-input.md")
- [Setting up for locking](pipeline-locking-set-up.md "pipeline-locking-set-up.md")
- [Troubleshooting](pipeline-locking-tshoot.md "pipeline-locking-tshoot.md")
