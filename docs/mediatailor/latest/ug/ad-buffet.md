

# Ad buffet
<a name="ad-buffet"></a>

The Interactive Advertising Bureau (IAB) Video Ad Serving Template (VAST) specification defines ad pods and ad buffet. This mechanism supports ordered ad insertion with automatic fallback on ad insertion failure. In an ad pod, sequenced ads play in order. Standalone ads serve as a buffet from which MediaTailor selects replacement ads when a sequenced ad fails.

AWS Elemental MediaTailor supports this specification through the `AdSequencingMode` setting in the `AdDecisionServerConfiguration` of the `PlaybackConfiguration`. When set to `FOLLOW_AD_SEQUENCE`, MediaTailor inserts sequenced ads in order and uses standalone ads only as substitutes when a sequenced ad fails to insert.

## Example VAST response
<a name="ad-buffet-vast-example"></a>

The following example shows a VAST response that contains sequenced ads and standalone ads:

```
<VAST>
  <Ad sequence="1" id="sequencedAd1">...</Ad>    <!-- Sequenced Ad 1 -->
  <Ad sequence="2" id="sequencedAd2">...</Ad>    <!-- Sequenced Ad 2 -->
  <Ad id="standAloneAd1">...</Ad>                <!-- Standalone Ad 1 -->
  <Ad id="standAloneAd2">...</Ad>                <!-- Standalone Ad 2 -->
  <Ad id="standAloneAd3">...</Ad>                <!-- Standalone Ad 3 -->
</VAST>
```

In this example, the two sequenced ads form an ad pod. The three standalone ads form the ad buffet. Together they constitute one buffet group. If `sequencedAd1` fails, MediaTailor first attempts to replace it with an eligible standalone ad from the same buffet group. If no eligible standalone ad is available in that group, MediaTailor selects from standalone ads in other buffet groups.

The following diagram shows a VAST response with an ad pod (sequenced ads) and an ad buffet (standalone ads) that together form a buffet group.

![Diagram of a VAST response with an ad pod (two sequenced ads) and an ad buffet (three standalone ads) forming one buffet group.](http://docs.aws.amazon.com/mediatailor/latest/ug/images/vastVisualizedAdBuffetBuffetGroup.png)


## Key concepts
<a name="ad-buffet-key-concepts"></a>

The following terms describe the core concepts of ad buffet:
+ **Sequenced ads** – Ads with a `sequence` attribute in the `<Ad>` element. These form an ordered ad pod and are inserted in increasing sequence order.
+ **Standalone (buffet) ads** – Ads without a `sequence` attribute. These are used only as substitutes when a sequenced ad fails to insert.
+ **Buffet group** – MediaTailor pairs an ad pod with its standalone ads within a single VAST response. When a sequenced ad is a wrapper, its redirected VAST forms its own independent buffet group. When replacing a failed sequenced ad, MediaTailor prioritizes standalone ads from the same buffet group. If no eligible standalone ad exists in the same buffet group, MediaTailor falls back to standalone ads from other buffet groups.

**Note**  
`sequence` refers to the `<Ad>` element-level attribute, not the `sequence` attribute found in the `<Creative>` element.

## Benefits of ad buffet
<a name="ad-buffet-benefits"></a>

Without ad buffet, MediaTailor treats all ads identically, which can result in the following issues:
+ **VOD** – Standalone ads are inserted even when no failures occur, disrupting agreed-upon ad break positions and overfilling ad breaks.
+ **Live** – Lower-revenue standalone ads can be inserted before sequenced ads and occupy avail duration, leaving no room for higher-revenue sequenced ads.

With ad buffet enabled, MediaTailor inserts only sequenced ads and uses standalone ads only as substitutes when a sequenced ad fails to insert. This ensures that the highest-revenue ads are played first.

**Warning**  
If your Ad Decision Server (ADS) response does not contain any sequenced ads (no `<Ad>` element has a `sequence` attribute), enabling ad buffet results in no ad insertion.

## Enabling ad buffet
<a name="ad-buffet-enable"></a>

Ad buffet is an opt-in feature that you configure for each playback configuration using the `PutPlaybackConfiguration` API.

### AdSequencingMode values
<a name="ad-buffet-sequencing-modes"></a>

The following table describes the available `AdSequencingMode` values.


| Value | Description | 
| --- | --- | 
| IGNORE\_AD\_SEQUENCE (default) | MediaTailor inserts ads in the order they appear in the VAST response, regardless of sequence attributes. | 
| FOLLOW\_AD\_SEQUENCE | MediaTailor inserts sequenced ads in order for both live and VOD workflows. Failed sequenced ads are replaced with standalone ads. | 
| FOLLOW\_AD\_SEQUENCE\_ONLY\_LIVE | Ad buffet behavior is enabled for live workflows only. | 
| FOLLOW\_AD\_SEQUENCE\_ONLY\_VOD | Ad buffet behavior is enabled for VOD workflows only. | 

**Note**  
When you enable ad buffet, MediaTailor respects the `Wrapper.fallbackOnNoAd` and `Wrapper.allowMultipleAds` attributes.

### Midroll configuration
<a name="ad-buffet-midroll-config"></a>

The following example enables ad buffet for both live and VOD workflows:

```
{
    "PlaybackConfiguration": {
        "AdDecisionServerConfiguration": {
            "VastResponse": {
                "AdSequencingMode": "FOLLOW_AD_SEQUENCE"
            }
        }
    }
}
```

The following example enables ad buffet for live workflows only:

```
{
    "PlaybackConfiguration": {
        "AdDecisionServerConfiguration": {
            "VastResponse": {
                "AdSequencingMode": "FOLLOW_AD_SEQUENCE_ONLY_LIVE"
            }
        }
    }
}
```

The following example enables ad buffet for VOD workflows only:

```
{
    "PlaybackConfiguration": {
        "AdDecisionServerConfiguration": {
            "VastResponse": {
                "AdSequencingMode": "FOLLOW_AD_SEQUENCE_ONLY_VOD"
            }
        }
    }
}
```

### Live preroll configuration
<a name="ad-buffet-preroll-config"></a>

The following example enables ad buffet for live preroll ads:

```
{
    "PlaybackConfiguration": {
        "LivePrerollConfiguration": {
            "AdDecisionServerConfiguration": {
                "VastResponse": {
                    "AdSequencingMode": "FOLLOW_AD_SEQUENCE"
                }
            }
        }
    }
}
```

**Note**  
`LivePrerollConfiguration` only supports `FOLLOW_AD_SEQUENCE` and `IGNORE_AD_SEQUENCE`. Configure ad buffet for VOD preroll through the midroll configuration.

## How ad buffet works
<a name="ad-buffet-how-it-works"></a>

### Ad replacement conditions
<a name="ad-buffet-replacement-conditions"></a>

If a sequenced ad encounters one of the following failure cases, MediaTailor attempts to replace the sequenced ad with an eligible standalone ad from the same buffet group. If no standalone ad is available in the same buffet group, MediaTailor uses a standalone ad from other buffet groups, if available.


| Failure case | Description | 
| --- | --- | 
| VAST parse failure | A sequenced ad fails to parse because of missing required VAST elements (for example, MediaFiles, Creatives, or Impression are missing, or MediaFile or VASTAdTagURI is invalid). | 
| VAST wrapper resolution failure | A redirect times out, fails, or returns an empty response. | 
| VPAID ad dropped | A sequenced ad is VPAID and the session uses server-side reporting or has no slate configured. | 
| Ad transcode not ready | A sequenced ad's transcode status is not SUCCESS (for example, IN\_PROGRESS or ERROR). | 
| Avail duration exceeded | A sequenced ad's duration exceeds the remaining avail duration (live workflows). | 

### Standalone ad eligibility
<a name="ad-buffet-standalone-eligibility"></a>

To be eligible as a replacement, a standalone ad must meet the following criteria:
+ Not be a VPAID ad
+ Have a completed transcode
+ Have a duration that fits within the remaining avail duration

### Standalone ad selection
<a name="ad-buffet-standalone-selection"></a>

When a sequenced ad fails, MediaTailor selects a replacement from eligible standalone ads using the following priority:

1. **Same buffet group first** – MediaTailor prefers standalone ads from the failed ad's own buffet group.

1. **Other buffet groups** – Used only if no eligible ad exists in the same buffet group.

If no eligible standalone ad is found, the position is unfilled and the appropriate `SkippedReason` is emitted.

## VAST wrapper behavior
<a name="ad-buffet-wrapper-behavior"></a>

The handling of a Wrapper redirect response by MediaTailor depends on the value of two Wrapper variables: `Wrapper.fallbackOnNoAd` and `Wrapper.allowMultipleAds`.
+ `fallbackOnNoAd` takes effect when the redirect response is empty, times out, or an error occurs during the ADS request.
+ `allowMultipleAds` takes effect if the ADS response contains one or more ads.

### Empty VAST, request error, or request timeout
<a name="ad-buffet-wrapper-empty-response"></a>

The following table describes MediaTailor behavior when the redirect response is empty, times out, or an error occurs.


| fallbackOnNoAd | MediaTailor behavior | 
| --- | --- | 
| true (default) | MediaTailor selects a standalone ad to replace the failed wrapper, preferring the same buffet group. If no eligible same-group ad is available, MediaTailor selects from other buffet groups. | 
| false | MediaTailor drops the ad position and moves on to the next ad in the pod. No replacement occurs. | 

**Example fallbackOnNoAd=true (redirect fails)**  
**Parent VAST:**  

```
<VAST>
  <Ad sequence="1" id="seqAd1">...</Ad>
  <Ad sequence="2">
    <Wrapper fallbackOnNoAd="true">
      <VASTAdTagURI>https://ads.example.com/vast</VASTAdTagURI>
    </Wrapper>
  </Ad>
  <Ad id="standAloneAd1">...</Ad>
  <Ad id="standAloneAd2">...</Ad>
</VAST>
```
**Wrapper redirect response:** Empty VAST, times out, or errors.  
**Resolved VAST:**  

```
<VAST>
  <Ad sequence="1" id="seqAd1">...</Ad>
  <!-- standAloneAd1 replaced failed Wrapper Ad and now has the Wrapper's sequence (2) -->
  <Ad sequence="2" id="standAloneAd1">...</Ad>
  <Ad id="standAloneAd2">...</Ad>
</VAST>
```
**Playback order:**  

1. seqAd1

1. standAloneAd1

**Example fallbackOnNoAd=false (redirect fails)**  
**Parent VAST:**  

```
<VAST>
  <Ad sequence="1" id="seqAd1">...</Ad>
  <Ad sequence="2">
    <Wrapper fallbackOnNoAd="false">
      <VASTAdTagURI>https://ads.example.com/vast</VASTAdTagURI>
    </Wrapper>
  </Ad>
  <Ad id="standAloneAd1">...</Ad>
  <Ad id="standAloneAd2">...</Ad>
</VAST>
```
**Wrapper redirect response:** Empty VAST, times out, or errors.  
**Resolved VAST:**  

```
<VAST>
  <Ad sequence="1" id="seqAd1">...</Ad>
  <!-- sequence 2 is not replaced -->
  <Ad id="standAloneAd1">...</Ad>
  <Ad id="standAloneAd2">...</Ad>
</VAST>
```
**Playback order:**  

1. seqAd1

### Response contains one or more ads
<a name="ad-buffet-wrapper-ads-response"></a>

The following table describes MediaTailor behavior when the redirect response contains one or more ads.


| allowMultipleAds | MediaTailor behavior | 
| --- | --- | 
| false (default) | MediaTailor selects one ad from the redirect response and discards the remaining ads. The selected ad inherits the sequence value from the parent Wrapper Ad. Selection strategy: MediaTailor selects the lowest sequenced ad in the redirect response. If there is no sequenced ad available, MediaTailor picks a standalone ad, if available. | 
| true | When the wrapper has a sequence attribute, MediaTailor inserts redirect ads at the wrapper's position. When the wrapper has no sequence attribute, MediaTailor inserts redirect ads after the parent's sequenced ads. The resolved ads form their own buffet group. | 

**Example allowMultipleAds=false, wrapper has sequence=2**  
**Parent VAST:**  

```
<VAST>
  <Ad sequence="1" id="seqAd1">...</Ad>
  <Ad sequence="2">
    <Wrapper allowMultipleAds="false">
      <VASTAdTagURI>https://ads.example.com/vast</VASTAdTagURI>
    </Wrapper>
  </Ad>
  <Ad sequence="3" id="seqAd3">...</Ad>
  <Ad id="standAloneAd1">...</Ad>
  <Ad id="standAloneAd2">...</Ad>
</VAST>
```
**Wrapper redirect response:**  

```
<VAST>
  <Ad sequence="1" id="redirectSeqAd1">...</Ad>
  <Ad sequence="2" id="redirectSeqAd2">...</Ad>
  <Ad id="redirectStandAloneAd1">...</Ad>
</VAST>
```
**Resolved VAST:**  

```
<VAST>
  <Ad sequence="1" id="seqAd1">...</Ad>
  <Ad sequence="2" id="redirectSeqAd1">...</Ad> <!-- redirectSeqAd1 selected, inherits Wrapper's sequence (2) -->
  <Ad sequence="3" id="seqAd3">...</Ad>
  <Ad id="standAloneAd1">...</Ad>
  <Ad id="standAloneAd2">...</Ad>
</VAST>
```
**Playback order:**  

1. seqAd1

1. redirectSeqAd1

1. seqAd3

**Example allowMultipleAds=false, wrapper has no sequence**  
**Parent VAST:**  

```
<VAST>
  <Ad sequence="1" id="seqAd1">...</Ad>
  <Ad>
    <Wrapper allowMultipleAds="false">
      <VASTAdTagURI>https://ads.example.com/vast</VASTAdTagURI>
    </Wrapper>
  </Ad>
  <Ad sequence="3" id="seqAd3">...</Ad>
  <Ad id="standAloneAd1">...</Ad>
  <Ad id="standAloneAd2">...</Ad>
</VAST>
```
**Wrapper redirect response:**  

```
<VAST>
  <Ad sequence="1" id="redirectSeqAd1">...</Ad>
  <Ad sequence="2" id="redirectSeqAd2">...</Ad>
  <Ad id="redirectStandAloneAd1">...</Ad>
</VAST>
```
**Resolved VAST:**  

```
<VAST>
  <Ad sequence="1" id="seqAd1">...</Ad>
  <Ad id="redirectSeqAd1">...</Ad> <!-- redirectSeqAd1 selected, inherits Wrapper's sequence (UNDEFINED) -->
  <Ad sequence="3" id="seqAd3">...</Ad>
  <Ad id="standAloneAd1">...</Ad>
  <Ad id="standAloneAd2">...</Ad>
</VAST>
```
**Playback order:**  

1. seqAd1

1. seqAd3
redirectSeqAd1 is not played because it has no sequence defined.

**Example allowMultipleAds=true, wrapper has sequence=2**  
**Parent VAST:**  

```
<VAST>
  <Ad sequence="1" id="seqAd1">...</Ad>
  <Ad sequence="2">
    <Wrapper allowMultipleAds="true">
      <VASTAdTagURI>https://ads.example.com/vast</VASTAdTagURI>
    </Wrapper>
  </Ad>
  <Ad sequence="3" id="seqAd3">...</Ad>
  <Ad id="standAloneAd1">...</Ad>
  <Ad id="standAloneAd2">...</Ad>
</VAST>
```
**Wrapper redirect response:**  

```
<VAST>
  <Ad sequence="1" id="redirectSeqAd1">...</Ad>
  <Ad sequence="2" id="redirectSeqAd2">...</Ad>
  <Ad id="redirectStandAloneAd1">...</Ad>
</VAST>
```
**Resolved VAST:**  

```
<VAST>
  <Ad sequence="1" id="seqAd1">...</Ad>
  <!-- Redirect response merged at sequence 2 -->
  <Ad sequence="1" id="redirectSeqAd1">...</Ad>
  <Ad sequence="2" id="redirectSeqAd2">...</Ad>
  <Ad id="redirectStandAloneAd1">...</Ad>
  <Ad sequence="3" id="seqAd3">...</Ad>
  <Ad id="standAloneAd1">...</Ad>
  <Ad id="standAloneAd2">...</Ad>
</VAST>
```
**Playback order:**  

1. seqAd1

1. redirectSeqAd1

1. redirectSeqAd2

1. seqAd3

**Example allowMultipleAds=true, wrapper has no sequence**  
**Parent VAST:**  

```
<VAST>
  <Ad sequence="1" id="seqAd1">...</Ad>
  <Ad>
    <Wrapper allowMultipleAds="true">
      <VASTAdTagURI>https://ads.example.com/vast</VASTAdTagURI>
    </Wrapper>
  </Ad>
  <Ad sequence="3" id="seqAd3">...</Ad>
  <Ad id="standAloneAd1">...</Ad>
  <Ad id="standAloneAd2">...</Ad>
</VAST>
```
**Wrapper redirect response:**  

```
<VAST>
  <Ad sequence="1" id="redirectSeqAd1">...</Ad>
  <Ad sequence="2" id="redirectSeqAd2">...</Ad>
  <Ad id="redirectStandAloneAd1">...</Ad>
</VAST>
```
**Resolved VAST:**  

```
<VAST>
  <Ad sequence="1" id="seqAd1">...</Ad>
  <Ad sequence="3" id="seqAd3">...</Ad>
  <!-- Redirect response merged after sequenced ads -->
  <Ad sequence="1" id="redirectSeqAd1">...</Ad>
  <Ad sequence="2" id="redirectSeqAd2">...</Ad>
  <Ad id="redirectStandAloneAd1">...</Ad>
  <Ad id="standAloneAd1">...</Ad>
  <Ad id="standAloneAd2">...</Ad>
</VAST>
```
**Playback order:**  

1. seqAd1

1. seqAd3

1. redirectSeqAd1

1. redirectSeqAd2

## Metrics and log monitoring
<a name="ad-buffet-metrics"></a>

### Changes to existing metrics
<a name="ad-buffet-existing-metrics"></a>

When ad buffet is enabled, the following existing metrics change behavior.


| Metric | Behavior with ad buffet | 
| --- | --- | 
| AdDecisionServer.Ads | Count of sequenced ads parsed from the ADS response. | 
| AdDecisionServer.Duration | Total duration of sequenced ads only. | 
| AdDecisionServer.FillRate | Fill rate calculated using sequenced ads only. | 

### New metrics
<a name="ad-buffet-new-metrics"></a>

The following new metrics are available when ad buffet is enabled.


| Metric | Description | 
| --- | --- | 
| AdNotReady.SequencedAd | Number of sequenced ads not ready for insertion. | 
| AdNotReady.StandaloneAd | Number of standalone ads not ready for insertion (excludes ads skipped with StandaloneAdNotNeeded). | 
| Avail.FillRate.SequencedAd | Percentage of avail filled by sequenced ads. | 
| Avail.FillRate.StandaloneAd | Percentage of avail filled by standalone ads. | 
| Avail.FilledDuration.SequencedAd | Duration of avail filled with sequenced ads. | 
| Avail.FilledDuration.StandaloneAd | Duration of avail filled with standalone ads. | 
| AdsBilled.SequencedAd | Number of billed ads that are sequenced. | 
| AdsBilled.StandaloneAd | Number of billed ads that are standalone. | 
| SkippedReason.StandaloneAdNotNeeded | Emitted when a standalone ad was not needed because all sequenced ads were successfully inserted. | 

### New skipped ad reason
<a name="ad-buffet-skipped-reason"></a>

The following new skipped ad reason is available when ad buffet is enabled.


| Reason | Description | 
| --- | --- | 
| STANDALONE\_AD\_NOT\_NEEDED | A standalone ad was eligible but not needed because all sequenced ads were successfully inserted. No error beacon is fired. | 

For standalone ads that are not eligible for insertion (for example, VPAID or transcode not ready), the actual failure reason is emitted (for example, `TRANSCODE_IN_PROGRESS` or `VPAID_AD`) as `SkippedReason`.

### Error beaconing
<a name="ad-buffet-error-beaconing"></a>

MediaTailor handles error beacons for ad buffet as follows:
+ Sequenced ads that fail – error beacons are fired (existing behavior).
+ Standalone ads that are not ready (ad transcode status is not SUCCESS) – error beacons are fired (same as sequenced ads).
+ Unused standalone ads that were eligible for insertion but not needed – no error beacons are fired.

## ADS event changes
<a name="ad-buffet-ads-events"></a>

When ad buffet is enabled, MediaTailor adds the following fields to two ADS events:

### VAST\_RESPONSE event
<a name="ad-buffet-vast-response-event"></a>

Each `VastAd` in the `VAST_RESPONSE` event includes the following fields.


| Field | Type | Description | 
| --- | --- | --- | 
| buffetGroup | String | MediaTailor generated string that defines which buffet group the ad belongs to. | 
| sequence | Int | The sequence value from the Ad element. | 

### FILLED\_AVAIL event
<a name="ad-buffet-filled-avail-event"></a>

Each entry in `creativeAds` and `skippedAds` in the `FILLED_AVAIL` event includes the following fields.


| Field | Type | Description | 
| --- | --- | --- | 
| buffetGroup | String | MediaTailor generated string that defines which buffet group the ad belongs to. | 
| sequence | Int | The sequence value from the Ad element. | 

These fields allow you to determine:
+ Which ads were parsed as sequenced versus standalone
+ Which ads were inserted and their type
+ Why a sequenced ad was skipped and whether a standalone ad replaced it
+ Why a standalone ad was unavailable

## See also
<a name="ad-buffet-see-also"></a>

For more information about the `PutPlaybackConfiguration` API and the IAB VAST specification, see the following:
+ [PutPlaybackConfiguration API Reference](https://docs.aws.amazon.com/mediatailor/latest/apireference/API_PutPlaybackConfiguration.html) – Full parameter reference for configuring `AdSequencingMode` and related settings.
+ [IAB VAST 4.x Specification](https://iabtechlab.com/standards/vast/) on the IAB Tech Lab website – The industry standard defining ad pods, sequenced ads, and standalone ads.
+ [Monitoring AWS Elemental MediaTailor with Amazon CloudWatch metrics](monitoring-cloudwatch-metrics.md) – Full reference for all MediaTailor CloudWatch metrics, including new ad buffet metrics.