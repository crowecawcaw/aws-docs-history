

# SCTE-35 markers and period boundaries in DASH
<a name="dash-scte-period-boundaries"></a>

MediaTailor supports DASH origins that deliver either single-period or multi-period manifests. For single-period manifests, MediaTailor converts the manifest into a multi-period format using timing information from the `EventStream` to define period boundaries. After conversion, both single-period and multi-period manifests go through the same ad personalization workflow.

When MediaTailor detects a linear ad break event in a period, it treats the entire period as an ad break and personalizes it accordingly. MediaTailor uses the period start time (`Period@start`) as the ad break start time, regardless of any timing offset signaled within the event itself.

## Key behaviors
<a name="dash-scte-period-boundaries-behaviors"></a>

MediaTailor applies the following rules when processing SCTE-35 events in DASH periods:
+ For linear ad breaks, if an event's timing indicates the ad break starts after the period boundary, MediaTailor ignores the signaled start time and begins personalization at `Period@start`. For non-linear (overlay) events, MediaTailor respects the signaled `presentationTime`.
+ If a new SCTE event appears in the middle of an existing linear ad break, MediaTailor ignores it.
+ If an active non-linear (overlay) event already exists in the origin period, MediaTailor ignores any new linear event in that period.

## Event signaling mid-period
<a name="dash-scte-mid-period-signaling"></a>

With AWS Elemental MediaPackage v2, MediaTailor receives SCTE-35 markers even when a new period is not created at the marker boundary. This might result in SCTE markers appearing in the middle of content periods.

When a new SCTE-35 event signals a linear ad break in the middle of a content period, MediaTailor recognizes it as an ad break opportunity but starts personalization at `Period@start` rather than at the signaled event time. This mismatch might cause the following issues:
+ Ads that never appear to the viewer
+ Slate inserted to fill a remainder period created by the timing gap

### Calculating the event offset from period start
<a name="dash-scte-event-offset-calculation"></a>

Use the following formula to determine how far an event is offset from its period start:

`Offset = (presentationTime - presentationTimeOffset) / timescale`

The following example shows an `EventStream` with a `presentationTime` that is offset from the period start:

```
<Period id="1741948755359" start="PT10522H39M15.359S">
  <EventStream schemeIdUri="urn:scte:scte35:2013:xml" timescale="90000"
               presentationTimeOffset="156775387982400">
    <Event presentationTime="156775484008800" duration="36900000">
      <scte35:SpliceInfoSection protocolVersion="0" ptsAdjustment="0" tier="4095">
        <scte35:TimeSignal>
          <scte35:SpliceTime ptsTime="587770208"/>
        </scte35:TimeSignal>
        <scte35:SegmentationDescriptor segmentationEventId="168602131"
            segmentationEventCancelIndicator="false"
            segmentationDuration="36900000"
            segmentationTypeId="34"
            segmentNum="0" segmentsExpected="1">
        </scte35:SegmentationDescriptor>
      </scte35:SpliceInfoSection>
    </Event>
  </EventStream>
</Period>
```

For this example, the offset calculation is:

`156775484008800 - 156775387982400 = 96026400 ticks`

`96026400 / 90000 = 1066.96 seconds (approximately 17 minutes 46 seconds)`

The advertised break duration is:

`36900000 / 90000 = 410 seconds (approximately 6 minutes 50 seconds)`

Because the event does not start at the period boundary, MediaTailor begins personalization at `Period@start`, which is over 17 minutes earlier than the intended break. This results in ads that do not align with the actual break window. If slate is configured, MediaTailor inserts slate periods to fill the gap.

## Early cue-in
<a name="dash-scte-early-cue-in"></a>

An early cue-in occurs when an ad break ends before its originally signaled duration. In a multi-period manifest, this creates a new period that ends the original ad break early.

Behavior differs between AWS Elemental MediaPackage versions:
+ **MediaPackage v1** – Creates the new period and removes any event information within it.
+ **MediaPackage v2** – Includes two ad markers in the `EventStream`: the original cue-out and the cue-in. To signal the cue-in, set `outOfNetworkIndicator` to `false`.

MediaTailor recognizes the early cue-in by checking the `outOfNetworkIndicator` value. When MediaTailor finds a cue-in that matches a cue-out in the same period, it does not treat the cue-in as a new ad break opportunity.

The following example shows an `EventStream` with both a cue-out and an early cue-in:

```
<EventStream schemeIdUri="urn:scte:scte35:2013:xml" timescale="90000"
             presentationTimeOffset="276012000">
  <Event presentationTime="273308400" duration="5400000">
    <scte35:SpliceInfoSection duration="5400000" protocolVersion="0"
                              ptsAdjustment="183600" tier="4095">
      <scte35:SpliceInsert spliceEventId="222" spliceEventCancelIndicator="false"
          outOfNetworkIndicator="true" spliceImmediateFlag="false"
          uniqueProgramId="1" availNum="1" availsExpected="1">
        <scte35:Program>
          <scte35:SpliceTime ptsTime="273124800"/>
        </scte35:Program>
        <scte35:BreakDuration autoReturn="true" duration="5400000"/>
      </scte35:SpliceInsert>
    </scte35:SpliceInfoSection>
  </Event>
  <Event presentationTime="276012000">
    <scte35:SpliceInfoSection protocolVersion="0" ptsAdjustment="183600" tier="4095">
      <scte35:SpliceInsert spliceEventId="1" spliceEventCancelIndicator="false"
          outOfNetworkIndicator="false" spliceImmediateFlag="false"
          uniqueProgramId="1" availNum="1" availsExpected="1">
        <scte35:Program>
          <scte35:SpliceTime ptsTime="275828400"/>
        </scte35:Program>
      </scte35:SpliceInsert>
    </scte35:SpliceInfoSection>
  </Event>
</EventStream>
```

The first event (`outOfNetworkIndicator="true"`) signals the ad break start. The second event (`outOfNetworkIndicator="false"`) signals the early cue-in that ends the break.

## Mitigating mid-period SCTE-35 marker issues
<a name="dash-scte-marker-mitigation"></a>

If you experience unexpected ad personalization behavior due to SCTE-35 markers that appear mid-period in your DASH live streams, MediaTailor can suppress or pass through specific markers that are not applicable to your ad personalization workflow.

When marker suppression is enabled, MediaTailor performs the following actions:
+ **Suppress markers** – MediaTailor ignores specified markers and removes the corresponding events from the generated manifest. If no other events remain, MediaTailor also removes the empty `EventStream` from the period.
+ **Pass through markers** – MediaTailor ignores specified markers for personalization purposes, but the markers remain in the generated manifest.

The following break types are supported for suppression or passthrough:
+ `BREAK`
+ `PROVIDER_ADVERTISEMENT`
+ `DISTRIBUTOR_ADVERTISEMENT`
+ `PROVIDER_PLACEMENT_OPPORTUNITY`
+ `DISTRIBUTOR_PLACEMENT_OPPORTUNITY`
+ `PROVIDER_OVERLAY_PLACEMENT_OPPORTUNITY`

MediaTailor logs each suppressed or passed-through marker and emits a count metric when one or more markers are suppressed in a manifest response.

**Important**  
This configuration applies to DASH manifests in live streaming mode only. To have marker suppression or passthrough configured for your configuration, contact AWS Support. When contacting support, specify which break types you want suppressed or passed through.