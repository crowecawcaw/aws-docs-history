# SCTE-35 settings in MediaPackage

You can modify how MediaPackage interacts with SCTE-35 messages from your source content.
Configure the following settings on your origin endpoints. For more information, see the
following:

- For the MediaPackage console, see [Creating an origin endpoint in AWS Elemental MediaPackage](endpoints-create.md "endpoints-create.md").
- For the MediaPackage API, see [CreateOriginEndpoint](../apireference/origin_endpoints.md#origin_endpointspost "../apireference/origin_endpoints.md#origin_endpointspost") in the _AWS Elemental MediaPackage Live API
  Reference_.

###### Important

To modify how MediaPackage handles SCTE-35 messages, you should be familiar with the
SCTE-35 standard. You can view the most recent standards here: [SCTE Standards
Catalog](https://www.scte.org/standards/library/catalog/ "https://www.scte.org/standards/library/catalog/"). You should also be familiar with how SCTE-35 is implemented in
your source content.

The SCTE configuration is achieved through settings available both at the segment
level and at the manifest level.

\***\*Enable SCTE support\*\***

This setting is available on TS and CMAF origin endpoints, in the Segment
settings parameters group. When enabled, it allows to define the SCTE
configuration options in both the Segment settings and Manifest definitions
parameters groups.

\***\*SCTE filtering\*\***

This setting is available on TS and CMAF origin endpoints.

**SCTE filtering** specifies which SCTE-35 message types
MediaPackage uses to create new periods in the output manifest. All SCTE-35 markers
are preserved and passed through to the endpoint manifest, but only the
markers that match your specified filter will trigger period boundaries.

If you don't change this setting, MediaPackage treats these message types as
ads:

- Splice insert
- Break
- Provider advertisement
- Distributor advertisement
- Provider placement opportunity
- Distributor placement opportunity
- Provider overlay placement opportunity
- Distributor overlay placement opportunity
- Program

\***\*Ad markers\*\***

This setting is available for both HLS and DASH manifests, in the SCTE
configuration section of the Manifest definitions parameters group.

**Ad markers** allows you to specify what MediaPackage does when
it detects SCTE-35 messages. These are the options for HLS manifests:

- **Daterange** - inserts
  `EXT-X-DATERANGE` tags with SCTE-35 data
- **SCTE-35 enhanced** - inserts
  `EXT-X-CUE-OUT`, `EXT-X-CUE-IN`, and
  related CUE tags

For DASH manifests on CMAF endpoints, these are the options:

- **XML** - inserts EventStream
  elements with the `urn:scte:scte35:2013:xml`
  scheme
- **Binary** - inserts EventStream
  elements with the `urn:scte:scte35:2014:xml+bin`
  scheme
