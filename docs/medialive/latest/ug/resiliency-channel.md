# Implementing resiliency in the channel

AWS Elemental MediaLive has several features that provide resiliency in the channel:

## Input loss behavior

MediaLive always reacts to
loss of video input.You can
configure
the fine points of how MediaLive
behaves.
This feature covers all inputs—those that are set up with automatic input failover, and
those that aren't.

For more information, see [Handling loss of video input](feature-input-loss.md "feature-input-loss.md").

## Automatic input failover

With some inputs, you can set up two inputs
as an
automatic
input failover
_pair_,
in order to
provide resiliency for one input in the channel. Setting up this way provides resiliency in case
of a failure either in the upstream system, or between the upstream system and the channel.

Automatic input failover is a feature that applies to individual inputs. You don't have to
make a decision about implementing automatic input failover when planning the channel. You can
implement it later on, when attaching a new input, or when you want to upgrade an existing input
so that it implements automatic input failover.

To set up for automatic input failover, you set up two inputs (that have the exact same
source content) as an _input failover pair_. Setting up this way
provides resiliency in case of a failure in the upstream system, or between the upstream system
and the channel.

In the input pair, one of the inputs is the _active_ input
and one is on _standby_. MediaLive ingests both inputs, in order to
always be ready to switch, but it usually discards the standby input immediately. If the active
input fails, MediaLive immediately fails over and starts processing from the standby input, instead
of discarding it.

You can implement automatic input failover in a channel that is set up for pipeline
redundancy (a standard channel) or one that has no pipeline redundancy (a single-pipeline
channel).

For more information about implementing automatic input failover, see [Implementing automatic input failover](automatic-input-failover.md "automatic-input-failover.md").

## Pipeline redundancy

You can usually set up a channel with two pipelines, to provide resiliency within the
channel processing pipeline.

Pipeline redundancy is a feature that applies to the entire channel and to all the inputs
attached to the channel. Early on in your planning of the channel, you must decide how you want
to set up the pipelines. This feature is controlled by
the [class of the
inputs](class-channel-input.md "class-channel-input.md")
attached to the channel and by the class of the channel.

You set up for pipeline redundancy by setting up the channel as a _standard channel_ so that it has two encoding pipelines. Both pipelines ingest the
source content and produce output. If the current pipeline fails, the downstream system can
detect that it is no longer receiving content and can switch to the other output. There is no
disruption to the downstream system. MediaLive restarts the second pipeline within a few
minutes.

For more information about implementing pipeline redundancy, see [Implementing pipeline
redundancy](plan-redundancy-mode.md "plan-redundancy-mode.md").

## Comparison of automatic input failover and pipeline

redundancy

Following is a comparison of pipeline redundancy and automatic input failover.

- There is a difference in the failure that each feature deals with:

Pipeline redundancy provides resiliency in case of a failure in the MediaLive encoder
pipeline.

Automatic input failover provides resiliency in case of a failure ahead of MediaLive, either
in the upstream system or in the network connection between the upstream system and the MediaLive
input.

- Both features require two instances of the content source, so in both cases your upstream
  system must be able to provide two instances.

With pipeline redundancy, the two sources can originate from the same encoder.

With automatic input failover, the sources must originate from different encoders,
otherwise both sources will fail at the same time, and the input failover switch will
fail.

- Pipeline redundancy applies to the entire channel. Therefore you should decide whether you
  want to implement it when you plan the channel. Automatic input failover applies
  only
  to specific input types. Therefore you could, for example, decide to
  implement automatic input failover only when you attach your most important input.
- Automatic input failover requires that the downstream system be able to handle two
  instances of the output and be able to switch from one (when it fails) to the other. MediaPackage, for
  example, can handle two instances.

If your downstream system doesn't have this logic built in, then you can't implement
automatic input failover.
