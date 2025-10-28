# MediaTailor manifest query parameters

AWS Elemental MediaTailor handles query parameters for different purposes: manifest query parameters for
CDN routing and authorization, and other query parameters that may be used for
origin-specific functionality.

AWS Elemental MediaTailor preserves query parameters from session initialization and appends them to
personalized manifest URLs and other assets. Use this functionality when you have a Content
Delivery Network (CDN) between MediaTailor and the client player.

Use manifest query parameters when your CDN needs the query parameters for the
following:

- Dynamic routing to different MediaTailor endpoints
- Token authorization

###### Client-side vs CDN behavior

MediaTailor appends query parameters for client-side reporting endpoints, but does not
append them for CDN segments. The updated functionality provides more comprehensive
support for query parameters across various MediaTailor assets, enhancing flexibility for CDN
routing and authorization use cases.

MediaTailor appends query parameters for client-side reporting endpoints, but it doesn't append
the query parameters for the CloudFront (or other CDN) segments.

To use parameter preservation, contact [AWS Support](https://aws.amazon.com/premiumsupport/ "https://aws.amazon.com/premiumsupport/") to request that manifest query parameter
pass through be enabled.

The behavior varies between HLS and DASH, and between explicit and implicit session
initialization. The following topics describe how to configure session initialization
requests so that MediaTailor passes through parameters to the manifest:

###### Topics

- [MediaTailor
  HLS implicit sessions](manifest-query-parameters-hls-implicit-session-initialization.md "manifest-query-parameters-hls-implicit-session-initialization.md")
- [MediaTailor DASH implicit sessions](manifest-query-parameters-dash-implicit-session-initialization.md "manifest-query-parameters-dash-implicit-session-initialization.md")
- [MediaTailor explicit session initialization](manifest-query-parameters-hls-and-dash-explicit-session-initialization.md "manifest-query-parameters-hls-and-dash-explicit-session-initialization.md")
- [MediaTailor
  protocol-specific behavior](manifest-query-parameters-protocol-differences.md "manifest-query-parameters-protocol-differences.md")
- [MediaTailor CDN
  integration](manifest-query-parameters-cdn-integration.md "manifest-query-parameters-cdn-integration.md")
