# Starting, stopping, and pausing a channel

You can start or stop a channel. You can pause one or both pipelines in a channel.

For information about charges for a channel, see [Pricing in MediaLive](pricing.md "pricing.md"). There are
different charges depending on the state of the channel:

- Charges when the channel is running. A channel is running if it has started. If the pipelines
  are paused, the channel is still running.
- Charges when the channel is idle. A channel is idle when it has stopped.

## Starting a channel

You must always start a channel manually. The channel never starts automatically except when
it is already running and attempts to recover from a failure.

1. Open the MediaLive console at [https://console.aws.amazon.com/medialive/](https://console.aws.amazon.com/medialive/ "https://console.aws.amazon.com/medialive/").
2. Identify the input
   that you want to start the channel with. Make sure this input is ready:
   - If you are implementing
     [pipeline
     locking](pipeline-lock.md "pipeline-lock.md")
     using epoch locking, the first input must be a live input that contains a timecode. Epoch
     locking will get initialized in the channel only if the first input has a timecode.
   - Make sure that MediaLive will start on the desired input. You can add an immediate input
     switch to this input using the [MediaLiveschedule](x-actions-in-schedule-ips.md "x-actions-in-schedule-ips.md").
     Or you can make sure that the first input is the input that appears first in the list of
     inputs attached to the channel. We recommend that you use the schedule.
   - If the first input is a push input, it must be pushing to MediaLive before you start the
     channel. If the input is a pull input, the upstream system must be delivering to the endpoint
     before you start the channel. You might need to coordinate with the operator at the upstream
     system for this input.

3. In the navigation pane, choose **Channels**, and then on the
   **Channels** page, choose the channel that you want to start.
4. Before you start the channel, decide if you want to [enable
   thumbnails](thumbnails.md "thumbnails.md") for the channel. You won't be able to enable thumbnails after the channel
   starts.
5. Choose **Start**. The channel state changes to one of the
   following:
   - **Starting**
   - **Running** (encoding on the pipeline or pipelines)

6. Choose the channel name. The details for the channel appear. After a few seconds, the
   thumbnail preview of the current input appears (if thumbnail preview is enabled).

### Start times for

AWS Cloud channels

Most channels start in 3 minutes or less, but a startup time up to 10 minutes is still
normal. The time it takes for a channel to start depends on several factors. One factor is the
complexity of the channel configuration. Another factor is the size of the Amazon EC2 instance that
must be started up for the channel.

We recommend that you start a channel 2 hours in advance of high-value events so that there
is ample time to start, stop and restart a channel before the event begins.

### Start times for MediaLive Anywhere

channels

Most [MediaLive Anywhere](feature-emla.md "feature-emla.md") channels start in 3 minutes or less, but a
startup time up to 10 minutes is still normal. The time it takes for a channel to start depends
on several factors. One factor is the complexity of the channel configuration. Another factor is
the size of the Amazon EC2 instance that must be started up for the channel.

We recommend that you start a channel 2 hours in advance of high-value events so that there
is ample time to start, stop and restart a channel before the event begins.

## Stopping a channel

You can stop a running channel at any time.

1. Open the MediaLive console at [https://console.aws.amazon.com/medialive/](https://console.aws.amazon.com/medialive/ "https://console.aws.amazon.com/medialive/").
2. In the navigation pane, choose **Channels**, and then on the
   **Channels** page, choose the channel that you want to stop.
3. Choose **Stop**.

The thumbnail preview (if thumbnails preview is enabled in the channel)
stops updating. After a few seconds, the current thumbnail is replaced by a
message.

## Pausing a channel

You can also pause one or both the pipelines in a channel by adding a Pause action to the
schedule for the channel. For more information, see [How pause and
unpause actions work](x-actions-in-schedule-pause.md "x-actions-in-schedule-pause.md").
