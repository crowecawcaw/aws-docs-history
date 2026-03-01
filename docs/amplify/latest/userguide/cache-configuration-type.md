# How Amplify applies cache configuration to an app

To manage caching for your app, Amplify determines the type of content that is being
served by examining the app's platform type and rewrite rules. For `Compute` apps,
Amplify also examines the routing rules in the deployment manifest.

###### Note

The app's platform type is set by Amplify Hosting during deployment. An SSG (static) app
is set to the platform type `WEB`. An SSR app (Next.js 12 or later) is set to the
platform type `WEB_COMPUTE`.

Amplify identifies the following four types of content and applies the specified managed cache policy.

**Static**

The content served from apps with the `WEB` platform, or the static routes in
a `WEB_COMPUTE` app.

This content uses the Amplify-StaticContent cache policy.

**Image Optimization**

The images served by the `ImageOptimization` routes in a
`WEB_COMPUTE` app.

This content uses the Amplify-ImageOptimization cache policy.

**Compute**

The content served by the `Compute` routes in a `WEB_COMPUTE` app.
This includes all server-side rendered (SSR) content.

This content uses either the Amplify-Default or
Amplify-DefaultNoCookies cache policy depending on the value of
`cacheConfig.type` that is set on your Amplify `App`.

**Reverse Proxy**

The content served by paths that match a reverse proxy rewrite custom rule. For more
information about creating this custom rule, see [Reverse proxy rewrite](redirect-rewrite-examples.md#reverse-proxy-rewrite "redirect-rewrite-examples.md#reverse-proxy-rewrite") in the _Using redirects_
chapter.

This content uses either the Amplify-Default or
Amplify-DefaultNoCookies cache policy depending on the value of
`cacheConfig.type` that is set on your Amplify `App`.

## Understanding Amplify's managed cache policies

Amplify uses the following predefined managed cache policies to optimize the default cache
configuration for your hosted applications.

- Amplify-Default
- Amplify-DefaultNoCookies
- Amplify-ImageOptimization
- Amplify-StaticContent

### Amplify-Default managed cache policy settings

[View
this policy in the CloudFront console](https://console.aws.amazon.com/cloudfront/v4/home#/policies/cache/4d1d2f1d-3a71-49ad-9e08-7ea5d843a556 "https://console.aws.amazon.com/cloudfront/v4/home#/policies/cache/4d1d2f1d-3a71-49ad-9e08-7ea5d843a556")

This policy is designed for use with an origin that is an [AWS Amplify](https://aws.amazon.com/amplify/ "https://aws.amazon.com/amplify/") web app.

This policy has the following settings:

- **Minimum TTL:** 0 seconds
- **Maximum TTL:** 31536000 seconds (one year)
- **Default TTL:** 0 seconds
- **Headers included in cache key:**
  - `Authorization`
  - `Accept`
  - `CloudFront-Viewer-Country`
  - `Host`

- **Cookies included in cache key:** All
  cookies are included.
- **Query strings included in cache key:** All
  query strings are included.
- **Cache compressed objects setting:**
  Gzip and Brotli enabled.

### Amplify-DefaultNoCookies managed cache policy settings

[View
this policy in the CloudFront console](https://console.aws.amazon.com/cloudfront/v4/home#/policies/cache/a6bad946-36c3-4c33-aa98-362c74a7fb13 "https://console.aws.amazon.com/cloudfront/v4/home#/policies/cache/a6bad946-36c3-4c33-aa98-362c74a7fb13")

This policy is designed for use with an origin that is an [AWS Amplify](https://aws.amazon.com/amplify/ "https://aws.amazon.com/amplify/") web app.

This policy has the following settings:

- **Minimum TTL:** 0 seconds
- **Maximum TTL:** 31536000 seconds (one year)
- **Default TTL:** 0 seconds
- **Headers included in cache key:**
  - `Authorization`
  - `Accept`
  - `CloudFront-Viewer-Country`
  - `Host`

- **Cookies included in cache key:** No cookies are
  included.
- **Query strings included in cache key:** All
  query strings are included.
- **Cache compressed objects setting:**
  Gzip and Brotli enabled.

### Amplify-ImageOptimization managed cache policy settings

[View
this policy in the CloudFront console](https://console.aws.amazon.com/cloudfront/v4/home#/policies/cache/1c6db51a-a33f-469a-8245-dae26771f530 "https://console.aws.amazon.com/cloudfront/v4/home#/policies/cache/1c6db51a-a33f-469a-8245-dae26771f530")

This policy is designed for use with an origin that is an [AWS Amplify](https://aws.amazon.com/amplify/ "https://aws.amazon.com/amplify/") web app.

This policy has the following settings:

- **Minimum TTL:** 0 seconds
- **Maximum TTL:** 31536000 seconds (one year)
- **Default TTL:** 0 seconds
- **Headers included in cache key:**
  - `Authorization`
  - `Accept`
  - `Host`

- **Cookies included in cache key:** No cookies are
  included.
- **Query strings included in cache key:** All
  query strings are included.
- **Cache compressed objects setting:**
  Gzip and Brotli enabled.

### Amplify-StaticContent managed cache policy settings

[View
this policy in the CloudFront console](https://console.aws.amazon.com/cloudfront/v4/home#/policies/cache/7e5fad67-ee98-4ad0-b05a-394999eefc1a "https://console.aws.amazon.com/cloudfront/v4/home#/policies/cache/7e5fad67-ee98-4ad0-b05a-394999eefc1a")

This policy is designed for use with an origin that is an [AWS Amplify](https://aws.amazon.com/amplify/ "https://aws.amazon.com/amplify/") web app.

This policy has the following settings:

- **Minimum TTL:** 0 seconds
- **Maximum TTL:** 31536000 seconds (one year)
- **Default TTL:** 0 seconds
- **Headers included in cache key:**
  - `Authorization`
  - `Host`

- **Cookies included in cache key:** No cookies are
  included.
- **Query strings included in cache key:** No
  query strings are included.
- **Cache compressed objects setting:**
  Gzip and Brotli enabled.
