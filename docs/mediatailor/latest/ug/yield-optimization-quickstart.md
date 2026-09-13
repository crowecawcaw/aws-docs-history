

# Yield Optimization quick start guide
<a name="yield-optimization-quickstart"></a>

This guide walks you through enabling Yield Optimization on a playback configuration and verifying that it works.

**Goal:** By the end of this guide, you will have a playback configuration that automatically fills unfilled ad inventory with programmatic ads from APS.

## Prerequisites
<a name="yield-optimization-quickstart-prereqs"></a>
+ An existing MediaTailor playback configuration with a live content source.
+ An APS Publisher ID. See [Integrating with APS](yield-optimization-integrating-aps.md) if you don't have one.

## Step 1: Enable Yield Optimization in the console
<a name="yield-optimization-quickstart-step1"></a>

1. Open the [MediaTailor console](https://console.aws.amazon.com/mediatailor/home).

1. In the left navigation pane, choose **Configurations**.

1. Choose the playback configuration you want to update.

1. Choose **Edit**.

1. Expand the **Yield Optimization Settings** section (marked with a **New** badge at launch). The section description reads: "Configure Yield Optimization settings including publisher ID, ad duration limits, and regional targeting."

1. Set the enablement dropdown to **Enabled**.

1. Fill in the following fields:
   + **APS Publisher ID**: The APS Publisher ID associated with your Publisher account (for example, `8caf35b3-402b-4d75-bab2-f2aef63a66d3`). See [Integrating with APS](yield-optimization-integrating-aps.md) for how to obtain this.
   + **Minimum Unfilled Duration**: The minimum unfilled duration in seconds that Yield Optimization will attempt to fill. Set this to **15** or higher. Values below 15 seconds will not return ads because APS ad creatives are typically 15 seconds or longer.
   + **Amazon Ads Region**: The Amazon Ads region to route bid requests to. Choose one of `Americas`, `Europe`, or `Asia Pacific` based on your primary audience. This maps to the `Region` field in the `YieldOptimizationConfiguration` API model, and the region names correspond to the APS regions described in [Integrating with APS](yield-optimization-integrating-aps.md).
   + **OpenRTB Template Configuration**: Your JSON template. See [Example templates](yield-optimization-examples.md) for starting points. The console validates JSON syntax and shows errors and warnings inline. The default template pre-populates with the console's starter template. See [Bid construction and templating](yield-optimization-bid-construction.md).

1. Choose **Save**.

## Step 2: Configure the OpenRTB template
<a name="yield-optimization-quickstart-step2"></a>

The console provides a JSON editor for the OpenRTB template. At minimum, your template must include:

```
{
  "app": {
    "bundle": "your.app.bundle.id",
    "storeurl": "https://your-app-store-url",
    "content": {}
  },
  "device": {
    "ua": "{{session.user_agent}}",
    "ip": "{{session.client_ip}}"
  },
  "imp": [
    {
      "video": {
        "mimes": ["video/mp4"],
        "protocols": [2, 3, 5, 6],
        "ext": {
          "slotId": "your-aps-slot-id"
        }
      },
      "bidfloor": 1.0
    }
  ]
}
```

The console will warn you if required fields are missing.

## Step 3: Start a session and verify
<a name="yield-optimization-quickstart-step3"></a>

1. Start a playback session that includes your player parameters (user agent, IP address, and so on).

1. Wait for an ad break with unfilled duration.

1. Check CloudWatch metrics for `YieldOptimization.BidRequest` and `YieldOptimization.AdsInserted`.

If `BidRequest` is emitting but `AdsInserted` is 0, check the `RAW_BID_REQUEST` event in the `ads_interaction_log` to verify your template is producing valid bid requests.

## Step 2 (alternative): Configure using the API
<a name="yield-optimization-quickstart-step2-api"></a>

Use the `PutPlaybackConfiguration` API with the `YieldOptimizationConfiguration` parameter:

```
aws mediatailor put-playback-configuration \
  --name "MyStreamingService" \
  --ad-decision-server-url "https://ads.example.com/vast" \
  --video-content-source-url "https://origin.example.com/hls/" \
  --yield-optimization-configuration '{
    "MinimumUnfilledDuration": 15,
    "PublisherId": "your-aps-publisher-id",
    "Region": "AMERICAS",
    "OpenRtbTemplate": "{\"app\":{\"bundle\":\"your.app.bundle\",\"storeurl\":\"https://store-url\",\"content\":{}},\"device\":{\"ua\":\"{{session.user_agent}}\",\"ip\":\"{{session.client_ip}}\"},\"imp\":[{\"video\":{\"mimes\":[\"video/mp4\"],\"protocols\":[2,3,5,6],\"ext\":{\"slotId\":\"your-slot-id\"}},\"bidfloor\":1.0}]}"
  }'
```

## Next steps
<a name="yield-optimization-quickstart-next-steps"></a>
+ To register with APS and get your Publisher ID, see [Integrating with APS](yield-optimization-integrating-aps.md).
+ To understand how MediaTailor decides when to make bid requests, see [How Yield Optimization works](yield-optimization-how-it-works.md).
+ To see complete template examples, see [Example templates](yield-optimization-examples.md).