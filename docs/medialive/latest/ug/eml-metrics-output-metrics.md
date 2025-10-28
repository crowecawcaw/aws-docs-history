# Output metrics

Output metrics relate to the video and audio assets that have been
processed by MediaLive as an output.

###### Topics

- [Active
  outputs](#eml-metrics-active-outputs "#eml-metrics-active-outputs")
- [Dropped
  frames](#eml-metrics-dropped-frames "#eml-metrics-dropped-frames")
- [Fill msec](#eml-metrics-fill "#eml-metrics-fill")
- [Output audio level
  dBFS](#eml-metrics-audio-dbfs "#eml-metrics-audio-dbfs")
- [Output audio level
  LKFS](#eml-metrics-audio-lkfs "#eml-metrics-audio-lkfs")
- [Network Out](#eml-metrics-network-out "#eml-metrics-network-out")
- [Output 4xx errors](#eml-metrics-4xx "#eml-metrics-4xx")
- [Output 5xx errors](#eml-metrics-5xx "#eml-metrics-5xx")
- [SVQ time](#eml-metrics-svq-time "#eml-metrics-svq-time")

## Active

outputs

The number of outputs that are being produced and successfully
written to the destination.

**Details:**

- Name: ActiveOutputs
- Units: Count.
- Meaning of zero: None of the outputs are successfully
  being written to their destinations.

If the outputs are configured to pause on input loss
(according to the **Input loss action** setting for the output group), that behavior
might be intentional.

- Meaning of no datapoints: The channel isn’t generating
  output audio (it might still be starting or waiting for
  initial input).
- Supported dimension sets: OutputGroupName, ChannelId,
  Pipeline
- Recommended statistic: Minimum, which helps you
  identify situations when one or more outputs is not
  being produced.

## Dropped

frames

The number of input frames that MediaLive has dropped in the
period. A value of 0 is expected and indicates that MediaLive is
processing incoming frames in real time. A value other than 0
indicates that the encoder can't process the incoming video fast
enough to keep up with real time.

**Details**

- Name: DroppedFrames
- Units: Count
- Meaning of zero: The encoder hasn't had to drop
  frames.
- Meaning of no datapoints: The channel isn’t producing
  output. This means that it isn’t running, or that it is
  running but it is initializing, or waiting for initial
  input, or paused.

- Supported dimensions sets: Pipeline, Region

- Recommended statistic: Sum.

## Fill msec

The current length of time (the _fill
period_) during which MediaLive has filled the
video output with fill frames. The fill period starts when the
pipeline does not receive content from the input within
the _expected time._ The
_expected time_ is based on
the input frame rate. The fine points of the fill frame behavior
are controlled by the input loss behavior fields in the channel
configuration. For information about these fields, see [Global configuration – input loss
behavior](creating-a-channel-step3.md#input-loss-behavior "creating-a-channel-step3.md#input-loss-behavior").

A value of 0 means that fill frames aren't being used. A
non-zero value means that fill frames are being used and that
the input is unhealthy.

The count is capped at 60,000 milliseconds (1 minute), which
means that after the cap, the metric will be 60,000 until it
drops to zero.

Use this metric as follows:

- If you have automatic input failover enabled – This
  metric typically shows zero all the time, even when
  there is a failover. The channel fails over to the other
  input immediately, which means that there is no need for
  MediaLive to use fill frames.
- If you don’t have automatic input failover enabled – A
  non-zero value indicates that the input has failed, has
  been disrupted, or isn't keeping up with real
  time.

**Details:**

- Name: FillMsec
- Units: Count.
- Meaning of zero: The input is healthy and the output
  contains the expected video (rather than fill
  frames).
- Meaning of no datapoints: The channel isn’t producing
  output, which means that it isn’t running. Or that it is
  running but it is initializing, or waiting for initial
  input, or paused.
- Supported dimension sets: ChannelId, Pipeline
- Recommended statistic: Maximum, to capture the capped
  count when fill frames are being used.

## Output audio level

dBFS

The output audio level in decibels relative to full scale
(dBFS).

**Details:**

- Name: OutputAudioLevelDbfs
- Units: Count.
- Meaning of zero: The output audio level is 0
  dBFS.
- Meaning of no datapoints: The channel isn’t generating
  output audio (it might still be starting or waiting for
  initial input).
- Supported dimension sets: AudioDescriptionName,
  ChannelId, Pipeline
- Recommended statistic: Minimum or maximum, which
  identify the lowest and highest audio level during the
  period.

## Output audio level

LKFS

The output audio level in loudness, K-weighted, relative to
full scale (LKFS).

**Details:**

- Name: OutputAudioLevelLkfs
- Units: Count.
- Meaning of zero: Output audio level is 0 LFKS.
- Meaning of no datapoints: The channel isn’t generating
  output audio (it might still be starting or waiting for
  initial input).
- Supported dimension sets: AudioDescriptionName,
  ChannelId, Pipeline
- Recommended statistic: Minimum or maximum, which
  identify the lowest and highest audio level during the
  period.

## Network Out

The rate of traffic out of MediaLive. This number includes all
traffic sent from MediaLive — the media output, HTTP GET requests
for pull inputs, NTP traffic, and DNS traffic. Even when a
channel is not delivering output, there will be some traffic.

**Details:**

- Name: NetworkOut
- Units: Megabits per second.
- Meaning of zero: No traffic is being sent.
- Meaning of no datapoints: The channel is not
  running.
- Supported dimension sets: ChannelId, Pipeline
- Recommended statistic: Average.

## Output 4xx errors

The number of 4xx HTTP errors that have been received from the
destination while delivering output.

**Details:**

- Name: Output4xxErrors
- Units: Count.
- Meaning of zero: The output is being delivered over
  HTTP and there are no errors.
- Meaning of no datapoints: The output is not being
  delivered to the destination over HTTP. Or the channel
  is not running.
- Supported dimension sets: OutputGroupName, ChannelId,
  Pipeline
- Recommended statistic: Sum.

## Output 5xx errors

The number of 5xx HTTP errors that have been received from the
destination while delivering output.

**Details:**

- Name: Output5xxErrors
- Units: Count.
- Meaning of zero: The output is being delivered over
  HTTP and there are no errors.
- Meaning of no datapoints: The output is not being
  delivered to the destination over HTTP. Or the channel
  is not running.
- Supported dimension sets: OutputGroupName, ChannelId,
  Pipeline
- Recommended statistic: Sum.

## SVQ time

The percentage of time that MediaLive has had to reduce quality
optimizations in order to emit output in real time. SVQ stands
for speed versus quality. Any encoding task must balance
emitting output in real time against a desire to produce the
best quality possible. But sometimes MediaLive must reduce quality
in order to encode fast enough to keep up with real time.

**Details**

- Name: SvqTime
- Units: Percent
- Meaning of zero: MediaLive hasn't had to reduce quality in
  order to produce output in real time.
- Meaning of no datapoints: The channel isn’t producing
  output. This means that it isn’t running, or that it is
  running but it is initializing, or waiting for initial
  input, or paused.

- Supported dimensions sets: Pipeline, Region

- Recommended statistic: Max.
