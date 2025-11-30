# Preconfigured distribution settings reference

When you create your CloudFront distribution, CloudFront automatically configures most distribution settings for you, based on your content origin type. Optionally, you can choose to manually edit your distribution settings. For more information, see [All distribution settings reference](distribution-web-values-specify.md "distribution-web-values-specify.md").

The following sections describe the default preconfiguration settings for distributions, and the settings that you can customize.

## Amazon S3 origin

Following are the origin settings that CloudFront preconfigures for your Amazon S3 origin in a multi-tenant distribution.

###### Origin settings (preconfigured)

- Origin Access Control (console only) – CloudFront sets this up for you. CloudFront attempts to add the S3 bucket policy for standard distributions and for multi-tenant distributions with no parameters used in the origin domain.
- Add custom header – None
- Enable Origin Shield – No
- Connection attempts – 3

Following are the cache settings that CloudFront preconfigures for your Amazon S3 origin in a multi-tenant distribution.

###### Cache settings (preconfigured)

- Compress objects automatically – Yes
- Viewer protocol policy – Redirect to HTTPS
- Allowed HTTP method – `GET, HEAD`
- Restrict viewer access – No
- Cache policy – `CachingOptimized`
- Origin request policy – None
- Response header policy – None
- Smooth Streaming – No
- Field level encryption – No
- Enable real-time access logs – No
- Functions – No

Following are the settings that you can customize for your Amazon S3 origin in a multi-tenant distribution.

###### Customizable settings

- S3 access – CloudFront sets this for you, based on your S3 bucket settings:
  - If your bucket is public – No Origin Access Control (OAC) policy is needed.
  - If your bucket is private – You can choose or create an OAC policy to use.

- Enable Origin Shield – No
- Compress objects automatically – Yes
  - If you choose **Yes**, then the `CachingOptimized` caching policy is used.
  - If you choose **No**, then the `CachingOptimizedForUncompressedObjects` caching policy is used.

## API Gateway origin

Following are the origin settings that CloudFront preconfigures for your API Gateway origin in a multi-tenant distribution.

###### Origin settings (preconfigured)

- Protocol – HTTPS only
- HTTPS port – 443
- Minimum origin SSL protocol – TLSv1.2
- Origin path – None
- Origin Access Control (console only) – CloudFront sets this up for you
- Add custom header – None
- Enable Origin Shield – No
- Connection attempts – 3
- Response timeout – 30
- Keep-alive timeout – 5

Following are the cache settings that CloudFront preconfigures for your API Gateway origin in a multi-tenant distribution.

###### Cache settings (preconfigured)

- Compress objects automatically – Yes
- Viewer protocol policy – Redirect to HTTPS
- Allowed HTTP method – `GET, HEAD, OPTIONS, PUT, POST, PATCH, DELETE`
- Cache HTTP methods – No
- Allow gRPC requests over HTTP/2 – No
- Restrict viewer access – No
- Cache policy – `CachingDisabled` (Possible values: `UseOriginCacheControlHeaders`, `UseOriginCacheControlHeaders-QueryStrings`)
- Origin request policy – `AllViewerExceptHostHeader` (Possible values: `AllViewer`, `AllViewerandCloudFrontHeaders-2022-06`)
- Response header policy – None
- Smooth Streaming – No
- Field level encryption – No
- Enable real-time access logs – No
- Functions – No

Following are the settings that you can customize for your API Gateway origin in a multi-tenant distribution.

###### Customizable settings

- Enable Origin Shield – (Default: No)
- Compress objects automatically – (Default: Yes)

## Custom origin and EC2 instance

Following are the origin settings that CloudFront preconfigures for your custom origin in a multi-tenant distribution.

###### Origin settings (preconfigured)

- Protocol – Match viewer
- HTTP port – 80
- HTTPS port – 443
- Minimum origin SSL protocol – TLSv1.2
- Origin path – None
- Add custom header – None
- Enable Origin Shield – No
- Connection attempts – 3
- Response timeout – 30
- Keep-alive timeout – 5

Following are the cache settings that CloudFront preconfigures for your custom origin and EC2 instance in a multi-tenant distribution.

###### Cache settings (preconfigured)

- Compress objects automatically – Yes
- Viewer protocol policy – Redirect to HTTPS
- Allowed HTTP method – `GET, HEAD, OPTIONS, PUT, POST, PATCH, DELETE`
- Cache HTTP methods – No
- Allow gRPC requests over HTTP/2 – No
- Restrict viewer access – No
- Cache policy – `UseOriginCacheControlHeaders` (Possible values: `UseOriginCacheControlHeaders-QueryStrings`, `CachingDisabled`, `CacheOptimized`, `CachingOptimizedForUncompressedObjects`)
- Origin request policy – `AllViewer` (Possible values: `AllViewerExceptHostHeader`, `AllViewerandCloudFrontHeaders-2022-06`)
- Response header policy – None
- Smooth Streaming – No
- Field level encryption – No
- Enable real-time access logs – No
- Functions – No

Following are the settings that you can customize for your custom origin and EC2 instance in a multi-tenant distribution.

###### Customizable settings

- Enable Origin Shield – (Default: No)
- Compress objects automatically – (Default: Yes)
- Caching – (Default: `Cache by Default`)
  - If `Cache by Default` is selected, the `UseOriginCacheControlHeaders` cache policy is used.
  - If `Do Not Cache by Default` is selected, the `CachingDisabled` cache policy is used.

- Include query string in cache – (Default: Yes, if `Cache by Default` is already selected)
  - If `Do Not Cache by Default` is already selected and you then choose to include the query string in the cache, the `UseOriginCacheControlHeaders-QueryStrings` cache policy is used.

## ELB origin

Following are the origin settings that CloudFront preconfigures for your ELB origin in a multi-tenant distribution.

###### Origin settings (preconfigured)

- Protocol – HTTPS only
- HTTPS port – 443
- Minimum origin SSL protocol – TLSv1.2
- Origin path – None
- Add custom header – None
- Enable Origin Shield – No
- Connection attempts – 3
- Response timeout – 30
- Keep-alive timeout – 5

Following are the cache settings that CloudFront preconfigures for your ELB origin in a multi-tenant distribution.

###### Cache settings (preconfigured)

- Compress objects automatically – Yes
- Viewer protocol policy – Redirect to HTTPS
- Allowed HTTP method – `GET, HEAD, OPTIONS, PUT, POST, PATCH, DELETE`
- Cache HTTP methods – No
- Allow gRPC requests over HTTP/2 – No
- Restrict viewer access – No
- Caching – (Default: `Cache by Default`)
  - If `Cache by Default` is selected, the `UseOriginCacheControlHeaders` cache policy is used.
  - If `Do Not Cache by Default` is selected, the `CachingDisabled` cache policy is used.

- Include query string in cache – (Default: Yes, if `Cache by Default` is already selected)
  - If `Do Not Cache by Default` is already selected and you then choose to include the query string in the cache, the `UseOriginCacheControlHeaders-QueryStrings` cache policy is used.

- Origin request policy – `All Viewer` (Possible values: `AllViewerExceptHostHeader`, `AllViewerandCloudFrontHeaders-2022-06`)
- Response header policy – None
- Smooth Streaming – No
- Field level encryption – No
- Enable real-time access logs – No
- Functions – No

Following are the settings that you can customize for your ELB origin in a multi-tenant distribution.

###### Customizable settings

- Enable Origin Shield – (Default: No)
- Compress objects automatically – (Default: Yes)
- Caching – (Default: `Cache by Default`)
  - If `Cache by Default` is selected, the `UseOriginCacheControlHeaders` cache policy is used.
  - If `Do Not Cache by Default` is selected, the `CachingDisabled` cache policy is used.

- Include query string in cache – (Default: Yes, if `Cache by Default` is already selected)
  - If `Do Not Cache by Default` is already selected and you then choose to include the query string in the cache, the `UseOriginCacheControlHeaders-QueryStrings` cache policy is used.

## MediaPackage v1 origin

Following are the origin settings that CloudFront preconfigures for your MediaPackage v1 origin in a multi-tenant distribution.

###### Origin settings (preconfigured)

- Protocol – HTTPS only
- HTTPS port – 443
- Minimum origin SSL protocol – TLSv1.2
- Origin path – You provide this by entering your MediaPackage URL.
- Add custom header – None
- Enable Origin Shield – No
- Connection attempts – 3
- Response timeout – 30
- Keep-alive timeout – 5

Following are the cache settings that CloudFront preconfigures for your MediaPackage v1 origin in a multi-tenant distribution.

###### Cache settings (preconfigured)

- Compress objects automatically – Yes
- Viewer protocol policy – Redirect to HTTPS
- Allowed HTTP method – `GET, HEAD`
- Cache HTTP methods – No
- Allow gRPC requests over HTTP/2 – No
- Restrict viewer access – No
- Cache policy – `Elemental-MediaPackage`
- Origin request policy – None
- Response header policy – None
- Smooth Streaming – No
- Field level encryption – No
- Enable real-time access logs – No
- Functions – No

## MediaPackage v2 origin

Following are the origin settings that CloudFront preconfigures for your MediaPackage v2 origin in a multi-tenant distribution.

###### Origin settings (preconfigured)

- Origin Access Control – CloudFront sets this up for you and adds the policy
- Protocol – HTTPS only
- HTTPS port – 443
- Minimum origin SSL protocol – TLSv1.2
- Origin path – None
- Add custom header – None
- Enable Origin Shield – No
- Connection attempts – 3
- Response timeout – 30
- Keep-alive timeout – 5

Following are the cache settings that CloudFront preconfigures for your MediaPackage v2 origin in a multi-tenant distribution.

###### Cache settings (preconfigured)

- Compress objects automatically – Yes
- Viewer protocol policy – Redirect to HTTPS
- Allowed HTTP method – `GET, HEAD`
- Cache HTTP methods – No
- Allow gRPC requests over HTTP/2 – No
- Restrict viewer access – No
- Cache policy – `Elemental-MediaPackage`
- Origin request policy – None
- Response header policy – None
- Smooth Streaming – No
- Field level encryption – No
- Enable real-time access logs – No
- Functions – No

## MediaTailor origin

Following are the origin settings that CloudFront preconfigures for your MediaTailor origin in a multi-tenant distribution.

###### Origin settings (preconfigured)

- Protocol – HTTPS only
- HTTPS port – 443
- Minimum origin SSL protocol – TLSv1.2
- Origin path – You provide this by entering your MediaPackage URL.
- Add custom header – None
- Enable Origin Shield – No
- Connection attempts – 3
- Response timeout – 30
- Keep-alive timeout – 5

Following are the cache settings that CloudFront preconfigures for your MediaTailor origin in a multi-tenant distribution.

###### Cache settings (preconfigured)

- Compress objects automatically – Yes
- Viewer protocol policy – Redirect to HTTPS
- Allowed HTTP method – `GET, HEAD`
- Cache HTTP methods – No
- Allow gRPC requests over HTTP/2 – No
- Restrict viewer access – No
- Cache policy – None
- Origin request policy – `Elemental-MediaTailor-PersonalizedManifests`
- Response header policy – None
- Smooth Streaming – No
- Field level encryption – No
- Enable real-time access logs – No
- Functions – No
