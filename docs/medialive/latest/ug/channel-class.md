# Channel class

When you [planned the workflow](plan-redundancy-mode.md "plan-redundancy-mode.md"), you
decided whether to set up the MediaLive channel as a standard channel (with two
pipelines) or a single-pipeline channel. You must now specify the class in the
channel configuration.

For **Channel class**, choose `STANDARD` or
`SINGLE_PIPELINE`.

## Standard class

With this class, the channel contains two pipelines. The input for the channel
has two entry points. The upstream system sends identical source streams to
these two entry points, to provide content to two pipelines within the channel.
MediaLive performs identical processing on both pipelines. For each output that you
configure (for example, for both HLS output and RTMP output), the two pipelines
deliver identical content to two destinations on the downstream system.

## Single pipeline class

With this class, the channel contains one pipeline. For each output that you
configure, the channel delivers content to one destination on the downstream
system.

### Linked channels for single-pipeline

channels

When you select **SINGLE_PIPELINE** as the channel class,
additional fields appear for configuring linked channels. Linked channels enable
pipeline locking for single-pipeline channels.

You can configure a single-pipeline channel as either:

- **Primary channel**: The owner of the
  linked group. The primary channel establishes the linked channel
  relationship. The primary channel does not need to be running for
  the follower channel to function.
- **Follower channel**: A channel that
  participates in the linked group. You must specify the ARN of the
  primary channel to join the linked group.

Linked channels have the following requirements:

- Primary and follower channels must belong to the same AWS
  account.
- Only one follower channel can be linked to a primary channel.
- The follower channel must reference a valid primary channel
  ARN.

For more information about pipeline locking, see
[Implementing pipeline locking](pipeline-lock.md "pipeline-lock.md").
