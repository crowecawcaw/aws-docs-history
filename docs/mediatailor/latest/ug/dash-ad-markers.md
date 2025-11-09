# DASH ad markers

MediaTailor

AWS Elemental MediaTailor uses SCTE-35 cue-out markers to identify ad avails in the DASH
manifest using the following logic:

- **Multi-period DASH**: MediaTailor inserts ads for the first
  `Event` in each `Period` that contains either
  `SpliceInsert` or `TimeSignal` cue-out markers. MediaTailor
  ignores additional `Event` markers in the `Period`.
- **Single-period DASH**: MediaTailor inserts ads each
  `Event` in the `Period` that contains either
  `SpliceInsert` or `TimeSignal` cue-out markers.
  By default, AWS Elemental MediaTailor manages DASH manifests as multi-period manifests. You can
  change your configuration to handle single-period DASH manifests from your origin server.
  For information, see [Creating an MediaTailor playback
  configuration](configurations-create.md "configurations-create.md").

The following sections provide additional detail about DASH ad marker handling and
provides decorated manifests from the origin.

## DASH origin manifest XML requirements

Ad markers in DASH manifests from the origin must be formatted properly for MediaTailor to
identify ad breaks. The following topics describe these formatting requirements in clear
XML.

### `SpliceInsert` in clear XML

`SpliceInsert` ad markers in clear XML must contain the
following:

- `EventStream` must have the following attribute:
  `schemeIdUri=urn:scte:scte35:2013:xml`
- `Event` must hold `scte35:SpliceInfoSection`
- `scte35:SpliceInfoSection` must hold `scte35:SpliceInsert`
- `scte35:SpliceInsert` must have the following attribute:
  `outOfNetworkIndicator="true"`

###### Example `SpliceInsert` in XML

In the following example, required SCTE markers are in bold.

```
<Period start="PT444806.040S" id="123586" duration="PT15.000S">
  <EventStream timescale="90000" **schemeIdUri="urn:scte:scte35:2013:xml"**>
    <Event duration="1350000">
      **<scte35:SpliceInfoSection** protocolVersion="0" ptsAdjustment="180832" tier="4095">
        **<scte35:SpliceInsert** spliceEventId="4026531855" spliceEventCancelIndicator="false" **outOfNetworkIndicator="true"** spliceImmediateFlag="false" uniqueProgramId="1" availNum="1" availsExpected="1">
            <scte35:Program><scte35:SpliceTime ptsTime="5672624400"/></scte35:Program>
            <scte35:BreakDuration autoReturn="true" duration="1350000"/>
        </scte35:SpliceInsert>
      </scte35:SpliceInfoSection>
    </Event>
  .
  .
  .
</Period>
```

### `TimeSignal` in clear XML

`TimeSignal` ad markers in clear XML must contain the following:

- `EventStream` must have the following attribute:
  `schemeIdUri=urn:scte:scte35:2013:xml`
- `Event` must hold `scte35:SpliceInfoSection`
- `scte35:SpliceInfoSection` must hold
  `scte35:TimeSignal`
- `scte35:SpliceInfoSection` must also hold
  `scte35:SegmentationDescriptor`
- `scte35:SegmentationDescriptor` must have the following attribute,
  where the value is a valid [Cue-out numbers](#dash-signal-xml-values "#dash-signal-xml-values"):
  `segmentationTypeId="`xx`"`

- `scte35:SegmentationDescriptor` must hold
  `scte35:SegmentationUpid`

###### Cue-out numbers

The following are supported cue-out numbers for the
`segmentationTypeId`.

| Segmentation message                         | segmentationTypeId value | Hexadecimal value |
| -------------------------------------------- | ------------------------ | ----------------- |
| Distributor advertisement end                | 51                       | 0x51              |
| Distributor advertisement start              | 50                       | 0x32              |
| Distributor placement opportunity end        | 55                       | 0x37              |
| Distributor placement opportunity start      | 54                       | 0x36              |
| End break                                    | 35                       | 0x23              |
| Provider advertisement end                   | 49                       | 0x31              |
| Provider advertisement start                 | 48                       | 0x30              |
| Provider overlay placement opportunity end   | 57                       | 0x39              |
| Provider overlay placement opportunity start | 56                       | 0x38              |
| Provider placement opportunity end           | 53                       | 0x35              |
| Provider placement opportunity start         | 52                       | 0x34              |
| Start break                                  | 34                       | 0x22              |

###### Example `TimeSignal` in XML

In the following example, required SCTE markers are in bold.

```
<Period start="PT346530.250S" id="178443" duration="PT61.561S">
  <EventStream timescale="90000" **schemeIdUri="urn:scte:scte35:2013:xml"**>
    <Event duration="5310000">
      **<scte35:SpliceInfoSection** protocolVersion="0" ptsAdjustment="183003" tier="4095">
        **<scte35:TimeSignal>**
          <scte35:SpliceTime ptsTime="3442857000"/>
         </scte35:TimeSignal>
        **<scte35:SegmentationDescriptor** segmentationEventId="1414668" segmentationEventCancelIndicator="false" segmentationDuration="8100000" **segmentationTypeId="52"** segmentNum="0" segmentsExpected="0">
            <scte35:DeliveryRestrictions webDeliveryAllowedFlag="false" noRegionalBlackoutFlag="false" archiveAllowedFlag="false" deviceRestrictions="3"/>
            **<scte35:SegmentationUpid** segmentationUpidType="12" segmentationUpidLength="2">0100</scte35:SegmentationUpid>
          </scte35:SegmentationDescriptor>
        </scte35:SpliceInfoSection>
    </Event>
  .
  .
  .
</Period>
```

## DASH origin manifest base64-encoded binary requirements

Ad markers in DASH manifests from the origin must be formatted properly for MediaTailor to
identify ad breaks. The following topics describe these formatting requirements in
base64-encoded binary.

Both `TimeSignal` and `SpliceInsert` ad markers in
base64-encoded manifests must contain the following:

- `EventStream` must have the following attribute:
  `urn:scte:scte35:2014:xml+bin`
- `Event` must hold `scte35:Signal`
- `scte35:Signal` must hold `scte35:Binary` that contains a
  base64-encoded binary.

The decoded binary must provide a `splice_info_section` with the same
information as what's required for clear XML ad markers.

- The command type must be either `splice_insert()` or
  `time_signal()`
- The additional settings must comply with those described in [TimeSignal in clear XML](#dash-signal-xml "#dash-signal-xml") and [SpliceInsert in clear XML](#dash-splice-xml "#dash-splice-xml").

The decoded binary must provide a `splice_info_section` with the same set
of information as the clear XML would provide in a `scte35:SpliceInfoSection`
element. The command type must be either `splice_insert()` or
`time_signal()`, and the additional settings must comply with those described
previously for clear XML delivery.

The following example shows this option, with the required markers in bold.

```
<Period start="PT444806.040S" id="123586" duration="PT15.000S">
    <EventStream **schemeIdUri="urn:scte:scte35:2014:xml+bin"** timescale="1">
      <Event presentationTime="1541436240" duration="24" id="29">
        **<scte35:Signal** xmlns="http://www.scte.org/schemas/35/2016">
          **<scte35:Binary>**/DAhAAAAAAAAAP/wEAUAAAHAf+9/fgAg9YDAAAAAAAA25aoh</scte35:Binary>
        </scte35:Signal>
      </Event>
      <Event presentationTime="1541436360" duration="24" id="30">
        <scte35:Signal xmlns="http://www.scte.org/schemas/35/2016">
          <scte35:Binary>QW5vdGhlciB0ZXN0IHN0cmluZyBmb3IgZW5jb2RpbmcgdG8gQmFzZTY0IGVuY29kZWQgYmluYXJ5Lg==</scte35:Binary>
        </scte35:Signal>
      </Event>
  .
  .
  .
</Period>
```

The following is the decoded binary for the first event listed in the preceding example.
The setting for `splice_command_type` is 5, which indicates
`splice_insert`.

```
{
        "table_id": 252,
        "section_syntax_indicator": false,
        "private_indicator": false,
        "section_length": 33,
        "protocol_version": 0,
        "encrypted_packet": false,
        "encryption_algorithm": 0,
        "pts_adjustment": 0,
        "cw_index": 0,
        "tier": "0xFFF",
        "splice_command_length": 16,
        **"splice\_command\_type": 5,**
        "splice_command": {
          "splice_event_id": 448,
          "splice_event_cancel_indicator": false,
          **"out\_of\_network\_indicator": true,**
          "program_splice_flag": true,
          "duration_flag": true,
          "splice_immediate_flag": false,
          "utc_splice_time": {
            "time_specified_flag": false,
            "pts_time": null
          },
          "component_count": 0,
          "components": null,
          "break_duration": {
            "auto_return": false,
            "duration": {
              "pts_time": 2160000,
              "wall_clock_seconds": 24.0,
              "wall_clock_time": "00:00:24:00000"
            }
          },
          "unique_program_id": 49152,
          "avail_num": 0,
          "avails_expected": 0
        },
        "splice_descriptor_loop_length": 0,
        "splice_descriptors": null,
        "Scte35Exception": {
          "parse_status": "SCTE-35 cue parsing completed with 0 errors.",
          "error_messages": [],
          "table_id": 252,
          "splice_command_type": 5
        }
      }
```
