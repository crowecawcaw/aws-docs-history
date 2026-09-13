

# Contextual ad targeting with Elemental Inference
<a name="monetization-functions-elemental-inference-integration"></a>

Elemental Inference analyzes video content and produces IAB Content Taxonomy classifications and GARM brand safety signals for each shot. By integrating MediaTailor with Elemental Inference, you can enrich ad requests with contextual metadata. Your ad decision server can then target ads based on what is happening in the content.

With this integration, you use the `AWS_SERVICE_REQUEST` function type to call the Elemental Inference `GetMetadata` API during ad breaks. For more information about the function type, see [AWS service request](monetization-functions-types-aws-service-request.md).

The following describes the integration flow:

1. Elemental Inference analyzes your content and produces shot-level classifications.

1. AWS Elemental MediaLive decorates SCTE-35 markers with Elemental Inference query parameters.

1. At each ad break, MediaTailor sends an authenticated request to `GetMetadata` to retrieve classifications for the content window.

1. Your function's output expressions extract IAB and GARM signals and pass them to the ad decision server.

## Prerequisites
<a name="monetization-functions-elemental-inference-integration-prereqs"></a>

Before you configure this integration, you need the following:
+ An Elemental Inference feed with a contextual metadata output. For instructions on creating the feed, see [Create the feed](https://docs.aws.amazon.com/elemental-inference/latest/userguide/create-feed.html) in the *Elemental Inference User Guide*.
+ A resource policy on the feed that grants MediaTailor access. See [Grant MediaTailor access to your Elemental Inference feed](#monetization-functions-elemental-inference-integration-access).
+ An AWS Elemental MediaLive channel with contextual metadata enrichment enabled. To provide accurate PTS timing values for Elemental Inference queries, enable MediaLive enrichment. For instructions on configuring contextual metadata enrichment, see [Set up contextual metadata enrichment](https://docs.aws.amazon.com/medialive/latest/ug/cm-enrichment-setup.html) in the *AWS Elemental MediaLive User Guide*.

MediaTailor and Elemental Inference do not need to be in the same AWS Region. The supported combinations depend on whether each service is in an opt-in Region. For details, see [Grant MediaTailor access to your Elemental Inference feed](#monetization-functions-elemental-inference-integration-access). For the Regions where Elemental Inference is available, see [Elemental Inference endpoints and quotas](https://docs.aws.amazon.com/elemental-inference/latest/userguide/endpoints.html).

## Grant MediaTailor access to your Elemental Inference feed
<a name="monetization-functions-elemental-inference-integration-access"></a>

MediaTailor calls `GetMetadata` using its own service credentials. The target Elemental Inference feed must have a resource policy that trusts the MediaTailor service principal.

MediaTailor automatically adds security headers that identify your account and playback configuration, ensuring your Elemental Inference feed can verify the request originates from your MediaTailor resources.

The following table shows which service principal to use based on your deployment scenario.


| Scenario | Service principal | 
| --- | --- | 
| MediaTailor and Elemental Inference in the same non-opt-in Region, or in different non-opt-in Regions | mediatailor.amazonaws.com | 
| MediaTailor in an opt-in Region calling Elemental Inference in a non-opt-in Region | mediatailor.{{region}}.amazonaws.com (for example, mediatailor.af-south-1.amazonaws.com) | 
| Restrict access to a single MediaTailor Region | mediatailor.{{region}}.amazonaws.com | 

**Note**  
MediaTailor does not currently support cross-opt-in-Region access (opt-in to different opt-in, or non-opt-in to opt-in).

The following example resource policy grants MediaTailor permission to call `GetMetadata` on a feed.

```
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Effect": "Allow",
            "Principal": {
                "Service": "mediatailor.amazonaws.com"
            },
            "Action": "elemental-inference:GetMetadata",
            "Resource": "arn:aws:elemental-inference:us-west-2:123456789012:feed/my-contextual-feed",
            "Condition": {
                "StringEquals": {
                    "aws:SourceAccount": "123456789012"
                },
                "ArnLike": {
                    "aws:SourceArn": "arn:aws:mediatailor:us-west-2:123456789012:playbackConfiguration/*"
                }
            }
        }
    ]
}
```

Replace `us-west-2`, `123456789012`, and `my-contextual-feed` with your Region, account ID, and feed ID.

The `aws:SourceAccount` condition ensures only MediaTailor operating on behalf of your account can access the feed. The `aws:SourceArn` condition further restricts access to specific playback configurations. Replace the wildcard with a specific playback configuration name for tighter scoping.

The following example shows a resource policy for an opt-in Region, where the service principal includes the Region name.

```
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Effect": "Allow",
            "Principal": {
                "Service": "mediatailor.af-south-1.amazonaws.com"
            },
            "Action": "elemental-inference:GetMetadata",
            "Resource": "arn:aws:elemental-inference:us-west-2:123456789012:feed/my-contextual-feed",
            "Condition": {
                "StringEquals": {
                    "aws:SourceAccount": "123456789012"
                },
                "ArnLike": {
                    "aws:SourceArn": "arn:aws:mediatailor:af-south-1:123456789012:playbackConfiguration/*"
                }
            }
        }
    ]
}
```

## Configure using the MediaTailor console
<a name="monetization-functions-elemental-inference-integration-console"></a>

The MediaTailor console provides a guided recipe for configuring Elemental Inference contextual metadata functions. The recipe automatically constructs the URL, templates the request body, and generates output expressions.

### Before you begin
<a name="monetization-functions-elemental-inference-integration-console-prereqs"></a>

Complete the steps in [Prerequisites](#monetization-functions-elemental-inference-integration-prereqs). You need an Elemental Inference feed with a contextual metadata output, a resource policy granting MediaTailor access, and a MediaLive channel with contextual metadata enrichment enabled.

### Create the function
<a name="monetization-functions-elemental-inference-integration-console-steps"></a>

1. Open the [MediaTailor console](https://console.aws.amazon.com/mediatailor/home). In the navigation pane, choose **Functions**.

1. Choose **Create function**.

1. For **Function type**, choose **AWS\_SERVICE\_REQUEST**.

1. Choose the **Elemental Inference — Contextual Metadata** recipe.

1. For **Feed source**, choose one of the following:
   + **From SCTE-35 markers** (recommended) — MediaTailor extracts the feed endpoint, region, and timing information from SCTE-35 markers decorated by MediaLive. You do not need to configure anything else.
   + **Browse feeds in my account** — The console lists your Elemental Inference feeds in the selected Region. Choose a feed to auto-populate the configuration. Use this when your Elemental Inference feed is in the same account as your MediaTailor resources.

1. For **Output name**, choose or enter the name of the contextual metadata output configured on your Elemental Inference feed.
**Note**  
If you selected a feed using the feed browser, the console auto-populates available output names from your feed configuration.

1. Under **Output configuration**, select which contextual signals to extract:
   + **IAB Content Categories** — Extracts IAB taxonomy category IDs as a comma-separated string.
   + **GARM Brand Safety** — Extracts flagged GARM brand safety categories.

   You can customize the output key names (for example, `player_params.iabCategories`) to match your ad decision server parameter names.

1. For **Timeout**, enter the maximum time to wait for a response. The default is 2000 milliseconds.

1. (Optional) Under **Resource policy**, review the generated policy snippet. If you have not yet configured access on your Elemental Inference feed, copy the policy and apply it using the Elemental Inference console or `PutFeedPolicy` API.

1. Choose **Create**.

### Attach to a playback configuration
<a name="monetization-functions-elemental-inference-integration-console-attach"></a>

After creating the function, attach it to a playback configuration at the `PRE_ADS_REQUEST` lifecycle hook. You can attach it directly or as a step within a `SEQUENTIAL_EXECUTOR` function.

1. In the navigation pane, choose **Playback configurations** and choose your configuration.

1. Under **Function mappings**, choose **Edit**.

1. For the `PRE_ADS_REQUEST` hook, select the function you created.

1. Save the configuration.

**Important**  
If your stream contains ad breaks without Elemental Inference markers, use a `SEQUENTIAL_EXECUTOR` with a run condition that checks `inference.enriched` before invoking the contextual metadata function. See [Chain with other functions](#monetization-functions-elemental-inference-integration-chaining).

## Configure using the API or CLI
<a name="monetization-functions-elemental-inference-integration-configure"></a>

To provide accurate timing information for Elemental Inference queries, enable MediaLive contextual metadata enrichment. The following sections describe the recommended production configuration using SCTE-35 markers from MediaLive, and a manual configuration option for testing purposes.

### Using SCTE-35 markers from MediaLive (production)
<a name="monetization-functions-elemental-inference-integration-configure-scte"></a>

When MediaLive is configured for contextual metadata enrichment, it embeds Elemental Inference query parameters directly in SCTE-35 ad break markers. MediaTailor parses these automatically and exposes them as `inference.*` variables. For the full list of available variables, see [Elemental Inference contextual metadata variables (inference.\*)](monetization-functions-hooks-pre-ads.md#monetization-functions-hooks-pre-ads-elemental-inference-vars).

Use this approach for production deployments for the following reasons:
+ No hardcoded endpoints are needed.
+ Region and feed are resolved automatically from the stream.
+ PTS alignment is handled by the encoder.

For instructions on enabling contextual metadata enrichment on your MediaLive channel, see [Set up contextual metadata enrichment](https://docs.aws.amazon.com/medialive/latest/ug/cm-enrichment-setup.html) in the *AWS Elemental MediaLive User Guide*.

The following example shows a complete function configuration using SCTE-35 enrichment.

```
{
    "FunctionId": "eiContextualMetadata",
    "FunctionType": "AWS_SERVICE_REQUEST",
    "AwsServiceRequestConfiguration": {
        "Runtime": "JSONATA",
        "TargetService": "elemental-inference",
        "TargetRegion": "{%inference.region%}",
        "MethodType": "POST",
        "Url": "{%inference.dataEndpoint & '/v1/feed/' & inference.feedId & '/input/0/metadata'%}",
        "Headers": {
            "Content-Type": "application/json"
        },
        "Body": "{%'{\"outputName\": \"my-contextual-output\", \"timeSpecification\": {\"ptsBased\": {\"startPts\": ' & $string(($exists(inference.previousBreakEndPts) and inference.previousBreakEndPts > inference.pts - 30 * inference.timescale ? inference.previousBreakEndPts : inference.pts - 30 * inference.timescale)) & ', \"endPts\": ' & $string(inference.pts + 1) & ', \"timescale\": ' & $string(inference.timescale) & '}}, \"parameters\": {\"contextualMetadata\": {}}}' %}",
        "RequestTimeoutMilliseconds": 2000,
        "Output": {
            "player_params.iabCategories": "{%response.statusCode = 200 ? $join($distinct(response.body.items.metadata.contextualMetadata.iabTaxonomy.categories.uniqueId), ',') : ''%}",
            "player_params.garmExcluded": "{%response.statusCode = 200 ? $join($distinct(response.body.items.metadata.contextualMetadata.garm.suitability.categories[flagged = true].category), ',') : ''%}"
        }
    }
}
```

The following list explains the key fields in the preceding example:
+ `TargetRegion` uses `inference.region` to dynamically sign for the correct Region.
+ The URL is constructed from `inference.dataEndpoint` and `inference.feedId`.
+ The Body queries from the end of the previous ad break (or up to 30 seconds lookback) to the current break.
+ Output extracts IAB category IDs and flagged GARM categories.

**Note**  
Replace `my-contextual-output` with the name of your Elemental Inference feed's contextual metadata output.

**Note**  
In the URL path `/v1/feed/{feed-id}/input/0/metadata`, the `0` refers to the input index on your Elemental Inference feed. Most feeds have a single input at index `0`. If your feed has multiple inputs, replace `0` with the appropriate index.

**Note**  
MediaTailor automatically includes the `x-amzn-elemental-inference-skip-poll` header on requests to Elemental Inference. This ensures low-latency responses suitable for ad break timing. You do not need to configure this header.

**Important**  
If your stream contains ad breaks that do not have Elemental Inference markers (for example, mixed content sources), wrap this function in a `SEQUENTIAL_EXECUTOR` with a `RunCondition` that checks `inference.enriched`:  

```
{ "FunctionId": "eiContextualMetadata", "RunCondition": "{%inference.enriched = true%}" }
```
When `inference.enriched` is `false` or absent, the `inference.*` variables are not available, and expressions referencing them will not produce valid results.

### Manual configuration (testing only)
<a name="monetization-functions-elemental-inference-integration-configure-manual"></a>

Use this configuration for testing only. Without SCTE-35 enrichment from MediaLive, you must determine PTS values manually and cannot benefit from dynamic timing alignment. This mode has limited functionality. We do not support it for production workflows.

```
{
    "FunctionId": "eiContextualMetadataManual",
    "FunctionType": "AWS_SERVICE_REQUEST",
    "AwsServiceRequestConfiguration": {
        "Runtime": "JSONATA",
        "TargetService": "elemental-inference",
        "TargetRegion": "us-west-2",
        "MethodType": "POST",
        "Url": "https://abc123.elemental-inference-data.us-west-2.amazonaws.com/v1/feed/my-feed-id/input/0/metadata",
        "Headers": {
            "Content-Type": "application/json"
        },
        "Body": "{%'{\"outputName\": \"my-contextual-output\", \"timeSpecification\": {\"ptsBased\": {\"startPts\": 6300001, \"endPts\": 9000001, \"timescale\": 90000}}, \"parameters\": {\"contextualMetadata\": {}}}' %}",
        "RequestTimeoutMilliseconds": 2000,
        "Output": {
            "player_params.iabCategories": "{%response.statusCode = 200 ? $join($distinct(response.body.items.metadata.contextualMetadata.iabTaxonomy.categories.uniqueId), ',') : ''%}"
        }
    }
}
```

**Note**  
Replace `my-contextual-output` with the name of your Elemental Inference feed's contextual metadata output.

**Note**  
Replace the `startPts` and `endPts` values with appropriate PTS values for your content. In this example, the values represent a 30-second window at 90 kHz timescale. Without SCTE-35 marker enrichment, you must determine PTS values from your content pipeline.

**Note**  
Replace `abc123.elemental-inference-data.us-west-2.amazonaws.com`, `my-feed-id`, and `us-west-2` with your feed's data endpoint, feed ID, and Region. You can find the data endpoint in the Elemental Inference `GetFeed` API response or console.

### Attach to a playback configuration
<a name="monetization-functions-elemental-inference-integration-attach-api"></a>

After creating the function, attach it to a playback configuration at the `PRE_ADS_REQUEST` lifecycle hook using the `PutPlaybackConfiguration` API. Include the function ID in the function mapping:

```
{
    "FunctionMappings": {
        "PRE_ADS_REQUEST": {
            "FunctionId": "eiContextualMetadata"
        }
    }
}
```

You can also wrap it in a `SEQUENTIAL_EXECUTOR` to chain with other functions. For more information, see [Chain with other functions](#monetization-functions-elemental-inference-integration-chaining).

## Understand the time window
<a name="monetization-functions-elemental-inference-integration-timewindow"></a>

The Body expression builds a PTS-based time window for the `GetMetadata` request. The following list describes the lookback logic:
+ `endPts` = PTS of the current ad break (from `inference.pts`) plus 1 (inclusive end).
+ `startPts` = the later of: end of the previous ad break (`inference.previousBreakEndPts`) or 30 seconds before the current break.
+ This queries only the content that played between ad breaks, avoiding content from within previous ad pods.
+ For the first ad break in a session, `inference.previousBreakEndPts` is not available, so the full 30-second lookback is used.
+ The 30-second window is the maximum lookback that Elemental Inference supports. When `inference.previousBreakEndPts` is available, the expression uses the later of that value or the 30-second lookback. This ensures the query covers only content since the previous ad break.

## Use the response in ad requests
<a name="monetization-functions-elemental-inference-integration-output"></a>

The following table describes the available output destination prefixes and their behavior.


| Destination prefix | Behavior | 
| --- | --- | 
| player\_params.\* | Available in the current ad break's ad decision server URL through [player\_params.key] substitution. Not persisted across ad breaks. | 
| temp.\* | Intermediate values for subsequent functions in a SEQUENTIAL\_EXECUTOR. Not persisted. | 
| adsRequest.headers.\* | Sent as HTTP headers on the ad decision server request. | 
| adsRequest.url | Overrides the ad decision server URL entirely. | 

For more output expression recipes, see [Example 3: Contextual metadata](monetization-functions-examples-contextual-metadata.md).

## Chain with other functions
<a name="monetization-functions-elemental-inference-integration-chaining"></a>

To combine the Elemental Inference call with other functions, wrap them in a `SEQUENTIAL_EXECUTOR`. The following example shows a pipeline where the second function only runs when Elemental Inference successfully returned categories.

```
{
    "FunctionId": "contextualAdPipeline",
    "FunctionType": "SEQUENTIAL_EXECUTOR",
    "SequentialExecutorConfiguration": {
        "Runtime": "JSONATA",
        "FunctionList": [
            { "FunctionId": "eiContextualMetadata" },
            {
                "FunctionId": "buildEnrichedAdsRequest",
                "RunCondition": "{%$exists(player_params.iabCategories) and player_params.iabCategories != ''%}"
            }
        ],
        "TimeoutMilliseconds": 3000
    }
}
```

The `RunCondition` ensures that `buildEnrichedAdsRequest` only runs when the Elemental Inference function produces data. You can then build the ad decision server request using the contextual data.

## Troubleshooting
<a name="monetization-functions-elemental-inference-integration-troubleshooting"></a>

The following table describes common issues and their resolutions.


| Symptom | Cause | Resolution | 
| --- | --- | --- | 
| 403 AccessDenied in function logs | Resource policy missing or incorrect | Verify the feed policy includes the MediaTailor service principal and that the aws:SourceAccount condition matches your account ID. For information about viewing function execution logs, see [Troubleshooting and monitoring](monetization-functions-troubleshooting.md). | 
| inference.enriched is false | SCTE-35 markers do not contain Elemental Inference data | Verify that contextual metadata enrichment is enabled on your MediaLive channel. | 
| inference.parseError is true | Malformed Elemental Inference data in SCTE-35 markers | Check the MediaLive channel configuration and encoder software version. | 
| Empty response (no items) | No analyzed content in the query time window | Verify the Elemental Inference feed is actively processing content and that the time window covers analyzed segments. | 
| Response truncated | Response exceeds 20,000 characters limit | Reduce the time window to return fewer analyzed shots. | 

**Note**  
If the function fails for any reason (timeout, authorization error, or empty response), MediaTailor proceeds with ad insertion using the values available without the function's contribution. The ad break is not blocked.