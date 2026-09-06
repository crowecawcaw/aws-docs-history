

# SCTE-35 settings in MediaPackage
<a name="scte-settings"></a>

You can modify how MediaPackage interacts with SCTE-35 messages from your source content. Configure the following settings on your origin endpoints. For more information, see the following:
+ For the MediaPackage console, see [Creating an origin endpoint in AWS Elemental MediaPackage](endpoints-create.md).
+ For the MediaPackage API, see [CreateOriginEndpoint](https://docs.aws.amazon.com/mediapackage/latest/apireference/origin_endpoints.html#origin_endpointspost) in the *AWS Elemental MediaPackage Live API Reference*.

**Important**  
To modify how MediaPackage handles SCTE-35 messages, you should be familiar with the SCTE-35 standard. You can view the most recent standards here: [SCTE Standards Catalog](https://www.scte.org/standards/library/catalog/). You should also be familiar with how SCTE-35 is implemented in your source content.

The SCTE configuration is achieved through settings available both at the segment level and at the manifest level.

****Enable SCTE support****  
This setting is available on TS and CMAF origin endpoints, in the Segment settings parameters group. When enabled, it allows to define the SCTE configuration options in both the Segment settings and Manifest definitions parameters groups.

****SCTE filtering****  
This setting is available on TS and CMAF origin endpoints.  
**SCTE filtering** specifies which SCTE-35 message types MediaPackage uses to create new periods in the output manifest. All SCTE-35 markers are preserved and passed through to the endpoint manifest, but only the markers that match your specified filter will trigger period boundaries.   
If you don't change this setting, MediaPackage treats these message types as ads:  
+ Splice insert
+ Break
+ Provider advertisement
+ Distributor advertisement
+ Provider placement opportunity
+ Distributor placement opportunity
+ Provider overlay placement opportunity
+ Distributor overlay placement opportunity
+ Program
+ Chapter
+ Unscheduled event
+ Alternate content opportunity
+ Network
+ Provider promo
+ Distributor promo
+ Provider ad block
+ Distributor ad block
The default filter includes the first nine values in the preceding list. The remaining values (Chapter, Unscheduled event, Alternate content opportunity, Network, Provider promo, Distributor promo, Provider ad block, and Distributor ad block) require explicit opt-in through the SCTE filtering configuration.

****Ad markers****  
This setting is available for both HLS and DASH manifests, in the SCTE configuration section of the Manifest definitions parameters group.  
**Ad markers** allows you to specify what MediaPackage does when it detects SCTE-35 messages. These are the options for HLS manifests:  
+ **Daterange** - inserts `EXT-X-DATERANGE` tags with SCTE-35 data
+ **SCTE-35 enhanced** - inserts `EXT-X-CUE-OUT`, `EXT-X-CUE-IN`, and related CUE tags
For DASH manifests on CMAF endpoints, these are the options:  
+ **XML** - inserts EventStream elements with the `urn:scte:scte35:2013:xml` scheme
+ **Binary** - inserts EventStream elements with the `urn:scte:scte35:2014:xml+bin` scheme

****SCTE in segments****  
Choose whether to include SCTE-35 messages in the segment files of MediaPackage outputs. This setting works independently of the **SCTE filtering** and **Ad markers** settings. Choose from the following options:  
+ **None** – SCTE-35 messages are not included in segment output. This is the default setting.
+ **All** – All SCTE-35 messages are embedded in the segment data, allowing downstream players and ad insertion systems to access the messages directly from segments without parsing manifest files.
+ **Matches filter** – Only SCTE-35 messages from events whose type matches the configured SCTE filtering are embedded in the segment data. This option allows you to limit which SCTE-35 messages are included in segments based on your filter configuration.
When you enable SCTE in segments:  
+ For TS segments, SCTE-35 messages are embedded directly in the transport stream.
+ For CMAF segments, SCTE-35 messages are embedded in the segment data.
+ For DASH manifests, when you set SCTE in segments to **All** or **Matches filter**, MediaPackage adds an `InbandEventStream` element with `schemeIdUri="urn:scte:scte35:2013:bin"` to signal the presence of SCTE-35 messages in the segment data.
Your downstream components or players must be implemented to consume SCTE-35 messages from segments to take advantage of this feature. If your players cannot handle SCTE-35 messages in segments, playback may fail when this setting is enabled.

****Custom ad types****  
This setting is available on TS and CMAF origin endpoints, in the Segment settings parameters group.  
**Custom ad types** allows you to designate additional SCTE-35 event types as advertisements. By default, MediaPackage treats only splice insert and time signal placement opportunity events as ads. Use this setting to expand the set of event types that MediaPackage treats as ads.  
Choose from the following values:  
+ `PROGRAM`
+ `CHAPTER`
+ `UNSCHEDULED_EVENT`
+ `ALTERNATE_CONTENT_OPPORTUNITY`
+ `NETWORK`

****SCTE in manifests****  
This setting is available for HLS, LL-HLS, and DASH manifests, in the SCTE configuration section of the Manifest definitions parameters group.  
**SCTE in manifests** controls which SCTE-35 events appear in the output manifests. Choose from the following options:  
+ **All** – All SCTE-35 events appear in the manifest. This is the default setting.
+ **Matches filter** – Only SCTE-35 events whose type matches the configured SCTE filtering appear in the manifest. You must have SCTE support enabled with at least one SCTE filter value configured to use this option.
This setting is not available for MSS manifests.