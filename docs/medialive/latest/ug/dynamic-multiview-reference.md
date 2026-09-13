

# Dynamic Multiview: MediaLive Configuration Reference
<a name="dynamic-multiview-reference"></a>

Reference for multiview-specific configuration fields and the encoder settings that participating outputs must use.

## outputUsage
<a name="dynamic-multiview-ref-outputusage"></a>

`MediaPackageV2DestinationSettings` include a new `outputUsage` list. It is a list of declared multiview usages. Setting any multiview usage on any video-carrying output in an output group puts the whole group into multiview mode and requires that all video-carrying outputs in that output group contain one or more multiview usage indications.

Here are the enum values that can be indicated:



| Value | Meaning | 
| --- | --- | 
| MULTIVIEW\_EQUAL\_SIZE\_VIEW | Eligible for any view in a layout where all views are the same size (2EH, 3EL, 4E) | 
| MULTIVIEW\_PRIMARY\_VIEW | Eligible for the large view in a layout with one dominant primary view (2PL, 3PL, 4PL) | 
| MULTIVIEW\_SECONDARY\_VIEW | Eligible for a smaller secondary view alongside a primary view | 

An output can declare multiple usages. Declaring more than one does not create additional renditions — it makes the single rendition eligible for more view positions, which increases the set of layouts a player can request.

Common multi-role cases:
+ A rendition that is half the size of a larger rendition and double the size of a smaller one can be both a primary and a secondary.
+ Any rendition sized for a primary/secondary pair can also serve equal-size layouts, since equal-size layouts place same-size views in every position.

## H.264 per-output constraints
<a name="dynamic-multiview-ref-h264"></a>

Every H.264 video description that has a multiview usage indicated must satisfy all of the following.



| Setting | Required value | 
| --- | --- | 
| width | Divisible by 16 | 
| height | Divisible by 16 | 
| gopClosedCadence | 1 | 
| sceneChangeDetect | DISABLED | 
| subgopLength | FIXED | 
| framerateControl | SPECIFIED | 
| entropyEncoding | CABAC | 

## H.265 per-output constraints
<a name="dynamic-multiview-ref-h265"></a>

Every H.265 video description that has a multiview usage indicated must satisfy all of the following.



| Setting | Required value | 
| --- | --- | 
| width | Divisible by 32 | 
| height | Divisible by 32 | 
| gopClosedCadence | 1 | 
| sceneChangeDetect | DISABLED | 
| subgopLength | FIXED | 
| deblocking | DISABLED | 
| mvOverPictureBoundaries | DISABLED | 
| mvTemporalPredictor | DISABLED | 
| tilePadding | PADDED | 
| treeblockSize | TREE\_SIZE\_32X32 | 

## Cross-output consistency
<a name="dynamic-multiview-ref-consistency"></a>

The following settings must be identical across all participating outputs **of the same codec** in the output group. H.264 and H.265 are evaluated independently.



| Setting | Applies to | 
| --- | --- | 
| gopSize | Both codecs | 
| gopNumBFrames | Both codecs | 
| profile | Both codecs | 
| level | Both codecs | 
| colorSpaceSettingsChoice | Both codecs | 
| colorSpaceSettings | Both codecs | 
| parControl | H.264 only | 
| parNumerator | Both codecs | 
| parDenominator | Both codecs | 

## Dimensional pairing
<a name="dynamic-multiview-ref-pairing"></a>



| Rule | Detail | 
| --- | --- | 
| Primary to secondary | Every primary needs a same-codec secondary in the same group at exactly half its width and half its height | 
| Secondary to primary | Every secondary needs a same-codec primary in the same group at exactly double its width and double its height | 

## Output group settings
<a name="dynamic-multiview-ref-opg"></a>



| Setting | Requirement | 
| --- | --- | 
| Destination | MediaPackage V2 | 
| Outputs | CMAF Ingest | 
| scte35Type | NONE or SCTE\_35\_WITHOUT\_IDR | 