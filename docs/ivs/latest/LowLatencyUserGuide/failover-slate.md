

# Amazon IVS Failover Slate
<a name="failover-slate"></a>

Amazon IVS failover slate helps you maintain viewer engagement when broadcasters experience temporary network disruptions or technical difficulties. When a broadcaster's connection is interrupted, IVS automatically displays a failover slate to viewers instead of showing a buffering wheel or frozen frame. This provides a smoother viewing experience and helps retain your audience during momentary interruptions. Failover slate is particularly useful when broadcasting from a mobile device with unreliable connectivity.

When you enable failover slate for a channel, IVS monitors the incoming stream. If the stream is unexpectedly interrupted, IVS automatically switches to display an animated default slate to viewers. When the broadcaster reconnects, playback resumes automatically. Viewers experience continuous playback without needing to refresh their player.

Failover slate activates only on unexpected interruptions. If the broadcaster intentionally stops streaming (a clean disconnect), the stream ends normally and IVS does not show a slate.

## Getting Started with Failover Slate
<a name="failover-slate-getting-started"></a>

This tutorial helps you get started with Amazon IVS failover slate. At the end of this tutorial, you have an IVS channel configured with a failover slate enabled. IVS uses the following default slate when failover slate is enabled.

![Default Amazon IVS failover slate showing an animated pattern displayed to viewers during stream interruptions](https://docs.aws.amazon.com/ivs/latest/LowLatencyUserGuide/images/failover_slate.png)


**Note**  
The default failover slate is an animated image provided by Amazon IVS, shown as a static screenshot in the preceding image. Custom slate assets are not currently supported.

### Step 1: Create a Failover Slate Configuration
<a name="failover-slate-step-1"></a>

A failover slate configuration controls when and how long the slate is displayed during stream disruptions. You can reuse a single failover slate configuration across multiple channels.

To create a failover slate configuration (AWS CLI):

```
aws ivs create-failover-slate-configuration \
  --name "my-failover-slate" \
  --activation-threshold-seconds 5 \
  --min-slate-display-seconds 2 \
  --max-slate-display-seconds 180
```

### Step 2: Create or Update the Channel
<a name="failover-slate-step-2"></a>

Associate your failover slate configuration with an IVS channel. You can do this when creating a new channel or by updating an existing one.

To create a new channel with failover slate (AWS CLI):

```
aws ivs create-channel \
  --name "my-channel" \
  --failover-slate-configuration-arn \
    "arn:aws:ivs:us-west-2:123456789012:failover-slate-configuration/ABcdef12ghIJ"
```

To update an existing channel with failover slate configuration (AWS CLI):

```
aws ivs update-channel \
  --arn "arn:aws:ivs:us-west-2:123456789012:channel/ABcdef12ghIJ" \
  --failover-slate-configuration-arn \
    "arn:aws:ivs:us-west-2:123456789012:failover-slate-configuration/ABcdef12ghIJ"
```

**Note**  
Live channels cannot be updated. You must stop the ongoing stream, update the channel, and restart the stream for changes to take effect.

### Step 3: Start Streaming
<a name="failover-slate-step-3"></a>

To start streaming, use the ingest endpoint and stream key from your channel.

### Step 4: Test the Failover Slate
<a name="failover-slate-step-4"></a>

IVS shows the failover slate only when it detects an unexpected stream interruption. There are two detection mechanisms:
+ **Inferred** — No data is received for the duration specified by `activationThresholdSeconds`. The slate is then shown to viewers.
+ **Explicit** — The encoder sends a signal indicating an unexpected disconnection, and the slate is shown immediately.

If the broadcaster intentionally stops streaming (a clean disconnect), the stream ends normally and no slate is shown.

To test the failover slate, simulate an unexpected interruption by abruptly cutting network connectivity. The simplest option is to disable network connectivity at the OS level. For example, disable Wi-Fi on your mobile phone while broadcasting. Do not use the stop-stream button in your streaming software, as that sends a clean disconnect signal and does not trigger the slate.

After the activation threshold elapses, viewers should see the slate image. When you resume streaming, the slate is replaced by your live content once the minimum display duration has elapsed. If the disruption exceeds the maximum display duration, the channel goes offline.

**Note**  
If recording is enabled for the channel, recordings include the failover slate content. Slate frames are written to your configured S3 bucket during the interruption period.

**Important**  
Not all third-party encoders send a clean disconnect signal when a stream ends intentionally. If your encoder does not send a clean disconnect, IVS may display the failover slate when the broadcaster stops streaming. Test failover slate with your encoder to verify the expected behavior for both intentional stops and unexpected interruptions.

### Step 5: Disable Failover Slate
<a name="failover-slate-step-5"></a>

To remove a failover slate configuration from a channel, update the channel with an empty failover slate configuration ARN:

```
aws ivs update-channel \
  --arn "arn:aws:ivs:us-west-2:123456789012:channel/ABcdef12ghIJ" \
  --failover-slate-configuration-arn ""
```

The channel no longer displays a slate during stream interruptions.

## Monitoring
<a name="failover-slate-monitoring"></a>

You can monitor failover slate activity with the following AWS services:
+ **EventBridge** — Amazon IVS sends `Failover Slate Start` and `Failover Slate End` events when a slate starts and ends. For more information, see [Using Amazon EventBridge with IVS Low-Latency Streaming](https://docs.aws.amazon.com/ivs/latest/LowLatencyUserGuide/eventbridge.html).
+ **CloudWatch** — The `FailoverSlateStarts` metric provides aggregate visibility into slate activations across channels. For more information, see [Monitoring Amazon IVS Low-Latency Streaming](https://docs.aws.amazon.com/ivs/latest/LowLatencyUserGuide/stream-health.html).

## Billing
<a name="failover-slate-billing"></a>

While a failover slate is active, your channel remains live and continues to incur standard Amazon IVS charges. You are billed for both video input and video output for the entire duration that the slate is displayed to viewers, exactly as you are during normal streaming.

For details on how video input and output are billed, see the [Amazon IVS Pricing](https://aws.amazon.com/ivs/pricing/) page.

## Known Issues
<a name="failover-slate-known-issues"></a>
+ **Brief visual artifacts after the slate ends** — When playback switches from the failover slate back to live content, viewers may see visual artifacts until the next keyframe. Playback then returns to normal on its own.