# Prepare for CloudFormation deployment of

CDN and MediaTailor integrations

AWS Elemental MediaTailor deployment with AWS CloudFormation requires specific prerequisites and preparation steps. Before you begin working with CloudFormation to integrate MediaTailor and Amazon CloudFront, make sure
you have the following.

- An AWS account with permissions to create MediaTailor, CloudFront, and CloudFormation
  resources
- A content origin where your video content is hosted (such as AWS Elemental MediaPackage, Amazon S3,
  or another origin server)
- An ad decision server (ADS) that can respond to VAST requests
  Before deploying the CloudFormation template, gather these required parameters:

`AdServerUrl`

URL of the VAST ad server for dynamic ad insertion. A static VAST endpoint
is provided for testing.

`ContentOriginDomainName`

Domain name of your content origin without protocol (e.g.,
`mediapackage-domain.mediapackagev2.us-west-2.amazonaws.com`,
`mybucket.s3.amazonaws.com`, or
`custom-origin.example.com`). Do not include
http:// or https:// prefixes or any paths.

`ContentOriginType`

The type of content origin:

- _mediapackagev2_: For AWS Elemental MediaPackage origins
- _s3_: For Amazon S3 bucket origins
- _custom_: For any other origin type

The template will create several AWS resources that work together to deliver your
content with personalized ads. The following describes what each component does:

## Origin access control

Origin Access Control (OAC) is a security feature that ensures your content can
only be accessed through CloudFront, not directly from your origin server. This helps
protect your content from unauthorized access.

For MediaPackage and Amazon S3 origins, the template creates an Origin Access Control (OAC)
resource to secure access to your content.

## MediaTailor playback configuration

The MediaTailor playback configuration is the core component that handles ad insertion.
It receives content from your origin, requests ads from your ad server, and combines
them into a personalized stream for each viewer.

The template creates an MediaTailor playback configuration with the following
settings:

- Video content source pointing to your CloudFront distribution
- Ad decision server URL configured to your specified VAST endpoint
- Live pre-roll configuration for ad insertion during live streams
- CDN configuration with appropriate segment URL prefixes

## CloudFront distribution

The CloudFront distribution delivers your content to viewers worldwide with low latency.
It handles different types of requests (manifests, content segments, ad segments)
and routes them to the appropriate origins.

For broadcast professionals new to CDNs, here are some key terms:

Origin

A server where your original content is stored (like MediaPackage or
Amazon S3)

Cache behavior

Rules that determine how different types of content are cached and
delivered

Cache policy

Settings that control how long content is cached and what request
components affect caching

The template creates a CloudFront distribution with the following components:

- Three origins:
  - Content origin (MediaPackage, Amazon S3, or custom)
  - MediaTailor manifests origin
  - MediaTailor segments origin

- Cache behaviors with appropriate patterns:
  - Default behavior for content segments
  - Behavior for MediaTailor ad segments (/tm/\*)
  - Behavior for MediaTailor interstitial media (/v1/i-media/\*)
  - Behavior for personalized manifests (/v1/\*)
  - Behavior for segment redirect requests (/segment/\*)

- Optimized cache policies for each behavior:
  - `CachingOptimized` for cacheable content
  - `CachingDisabled` for personalized manifests

- Origin request policies to ensure proper header forwarding
- Response header policies for CORS support
