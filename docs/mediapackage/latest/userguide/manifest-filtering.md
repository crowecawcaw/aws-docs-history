# Manifest filtering from AWS Elemental MediaPackage

With manifest filtering, AWS Elemental MediaPackage dynamically produces client manifests based on filter
parameters that you specify. This enables you to do things such as restrict viewer access to
premium 4K HEVC content, or target specific device types and audio sample rate ranges, all
from a single endpoint.

With manifest filtering, the resulting manifest from MediaPackage includes only the audio and
video streams that match the characteristics that you specify in your filters. If no
manifest filter is used, then all of the ingested streams are present in the endpoint output
stream. The exception to this is if you have set stream filters for the endpoint, such as
minimum video bitrate. In that case, the manifest filter is applied after the stream filter,
which could skew your output, and is not recommended.

Manifest filtering can be used on all origin endpoint types supported by MediaPackage.

To use manifest filtering, you can do one of the following:

- Apply filters to all manifests that originate from an endpoint: Set the filters on
  the origin endpoint through the MediaPackage console or API. For console instructions, see
  [Creating an origin endpoint](endpoints-create.md "endpoints-create.md").
- Apply filters dynamically across requests: Ensure that downstream video players
  include the appropriate query parameters in their manifest requests. For information
  about using query parameters, see [Manifest filtering query
  parameters](manifest-filter-query-parameters.md "manifest-filter-query-parameters.md").

###### Note

When configuring Manifest filters as part of the Filter Configuration for your
endpoint, be aware that using corresponding query parameters in the manifest's
endpoint URL can lead to issues. Specifically, if you include a Manifest filter in
your Filter Configuration and then attempt to use matching query parameters in the
endpoint URL, you will encounter a `404` HTTP error code. For example, if
your Filter Configuration includes a Manifest filter with an
`audio_sample_rate` key set to `44100`, and you
subsequently make an HTTP request to
`https://<example-url>/?aws.manifestfilter=audio_sample_rate:44100`
this will result in a `404` error. The Filter Configuration applies
universally to all egress requests for your endpoint, and duplicating these settings
in the URL query can lead to conflicts and errors. For more information about
Manifest filters, see Manifest filtering from AWS Elemental MediaPackage.

The following topics describe how manifest filtering works with MediaPackage.

###### Topics

- [Manifest filtering query
  parameters](manifest-filter-query-parameters.md "manifest-filter-query-parameters.md")
- [Special conditions
  for TS and CMAF manifests](special-conditions-TS-CMAF-manifests.md "special-conditions-TS-CMAF-manifests.md")
- [Manifest filtering
  examples](manifest-filtering-examples.md "manifest-filtering-examples.md")
- [Manifest filtering error
  conditions](error-conditions-and-handling.md "error-conditions-and-handling.md")
