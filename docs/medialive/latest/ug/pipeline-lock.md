# Implementing pipeline locking

You can configure
MediaLive
so that it
locks the two pipelines in a standard
channel.
Pipeline
locking
ensures
that the output from the two pipelines are frame-accurate with each other.
Pipeline locking is
enabled by default.

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

**Applicable outputs**

Pipeline locking applies only to the following types of outputs:

- HLS
- MediaPackage
- Microsoft Smooth
- SRT caller outputs that are segmented. You might have configured an SRT output
  group for segmented outputs. To verify, in an SRT caller output group, choose
  **Output** then **Network Settings**, then
  **Container Settings**. Look for the three fields that start
  with the term _Segmentation_.
- UDP outputs
  that are segmented. You might have configured a UDP output group for segmented
  outputs. To verify, in a UDP output group, choose **Output** then
  **Network Settings**, then **Container
  Settings**. Look for the three fields that start with the term
  _Segmentation_.
  The channel can contain other types of outputs, but MediaLive won't attempt to lock their
  outputs. This means that in those other output groups, there is no guarantee that the
  content of the two pipelines will be frame-accurate with each other.

**Pipeline locking modes**

There are two modes of pipeline locking:

- Pipeline locking (the default): lock the two pipelines to each other
- Epoch locking: lock the pipelines using the Unix epoch as the reference.

###### Topics

- [Input and output
  requirements](pipeline-locking-verify-input.md "pipeline-locking-verify-input.md")
- [Setting up for locking](pipeline-locking-set-up.md "pipeline-locking-set-up.md")
- [Troubleshooting](pipeline-locking-tshoot.md "pipeline-locking-tshoot.md")
