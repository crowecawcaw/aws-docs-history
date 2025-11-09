# Rules for most downstream systems

You can set up redundant manifests in a MediaLive HLS output group so long as the downstream
system can work with specific rules. Read this section if you are setting up redundant
manifests with any downstream system except Akamai. If your downstream system is an Akamai
CDN, see [Rules for Akamai CDNs](hls-redundant-manif-akamai.md "hls-redundant-manif-akamai.md").

You must make sure that the downstream system can work with the following rules.

- MediaLive pushes the files from both pipelines to the same location
  (protocol/domain/path).
- Given that the location is the same, the base filenames for the pipelines must be
  different.
- If you are also implementing [custom manifest
  paths](hls-manifests-how-work.md#hls-custom-manifest-paths "hls-manifests-how-work.md#hls-custom-manifest-paths"), the URL inside the manifests must be identical.

| Field                                                              | Rule                                                                                                                                                                                                                          |
| ------------------------------------------------------------------ | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Protocol/domain/path portion of the two destination URIs (A and B) | Must be identical in both fields.                                                                                                                                                                                             |
| Base-filename portion of the two destination URIs (A and B)        | Must be different in each field.<br>It \*cannot<br>• use [variable identifiers](variable-data-identifiers.md "variable-data-identifiers.md") that include the<br>date or time.                                                |
| NameModifier for each output                                       | There is only one instance of this field. Both pipelines use the same<br>value.<br>It \*cannot<br>• use [variable identifiers](variable-data-identifiers.md "variable-data-identifiers.md") that include the<br>date or time. |
| Segment modifier                                                   | There is only one instance of this field. Both pipelines use the same<br>value.<br>It \*can<br>• use [variable identifiers](variable-data-identifiers.md "variable-data-identifiers.md") that include the<br>date or time.    |
| Base URL Manifest A and Base URL Manifest B                        | These fields apply only if you are also implementing [custom manifest paths](hls-manifests-how-work.md#hls-custom-manifest-paths "hls-manifests-how-work.md#hls-custom-manifest-paths").<br>Complete both fields.             |
| Base URL Content A and Base URL Content B                          | These fields apply only if you are also implementing [custom manifest paths](hls-manifests-how-work.md#hls-custom-manifest-paths "hls-manifests-how-work.md#hls-custom-manifest-paths").<br>Complete both fields.             |
