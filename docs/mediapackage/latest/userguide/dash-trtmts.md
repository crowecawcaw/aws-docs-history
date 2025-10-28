# DASH manifest options in AWS Elemental MediaPackage

This section describes the options that AWS Elemental MediaPackage offers for modifying live output
DASH manifests.

###### Default DASH manifest

The following is a truncated example of a DASH manifest with no treatments:

```
<MPD>
  <Period>
    <AdaptationSet>
      <SegmentTemplate>
        <SegmentTimeline>
          <S />
        </SegmentTimeline>
      </SegmentTemplate>
      <Representation>
      </Representation>
    </AdaptationSet>
    .
    .
  </Period>
</MPD>
```

The elements of the DASH manifest are nested within the `MPD` (media presentation
description) object. These are the elements of the manifest:

- `Period` - The entire manifest is nested in one period.
- `AdaptationSet` - Groups together
  representations of the same type (video, audio, or captions). There are one or more
  `AdaptationSets` in the `Period`.
- `SegmentTemplate` - Defines properties of the
  `AdaptationSet`, such as the timescale and access URLs for media and initialization segments.
- `SegmentTimeline` - Describes when each segment
  is available for playback. There is one `SegmentTimeline` for each
  `SegmentTemplate`.
- `S` - Describes when the segment is available
  (`t` value), the duration of the segment (`d` value), and a count of
  how many additional consecutive segments have this same duration (`r` value).
  There are one or more segments in the `SegmentTimeline`.
- `Representation` - Describes an audio, video, or
  captions track. There are one or more `Representations` in each
  `AdaptationSet`. Each representation is a track.
  MediaPackage can modify how some of these elements are presented in the output
  manifest. You can use the following treatment options on the output live manifest:

- Separate the manifest into multiple periods, to permit ad breaks. See [Multi-period DASH in AWS Elemental MediaPackage](multi-period.md "multi-period.md").
