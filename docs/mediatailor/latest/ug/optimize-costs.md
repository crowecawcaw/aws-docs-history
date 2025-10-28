# Optimize costs for CDN and MediaTailor integrations

Content delivery network (CDN) costs can vary significantly based on traffic patterns, geographic distribution,
and feature usage with AWS Elemental MediaTailor. For current pricing information, see [CloudFront pricing](https://aws.amazon.com/cloudfront/pricing/ "https://aws.amazon.com/cloudfront/pricing/"). You can
also consult your CDN provider's documentation.

Balance the performance with the cost efficiency by using these strategies:

1.  Analyze your CDN traffic patterns to select the most cost-effective pricing
    tier. Review the following factors with your CDN provider:

        * Data transfer volumes by region and time period
        * Request patterns for manifests and segments
        * Geographic distribution requirements
        * Peak versus average usage patterns

    For help with cost analysis, use the [AWS Pricing Calculator](https://calculator.aws/#/ "https://calculator.aws/#/") to estimate your CloudFront costs based on
    your specific usage patterns.

2.  For predictable workloads, evaluate reserved capacity agreements with your CDN
    provider. These agreements can offer benefits such as:

        * Discounted rates for committed usage volumes
        * Predictable monthly costs for budgeting
        * Priority support and capacity allocation

    Consult with your CDN provider to determine if reserved capacity is
    appropriate for your usage patterns. For CloudFront, see [CloudFront premium features](../../../AmazonCloudFront/latest/DeveloperGuide/distribution-premium-features.md "../../../AmazonCloudFront/latest/DeveloperGuide/distribution-premium-features.md"). This provides information about
    reserved capacity options.

3.  Optimize egress costs by balancing traffic between MediaTailor and your CDN
    provider. Strategies include:

        * Maximize cache hit ratios to reduce origin requests
        * Use origin shield to consolidate requests
        * Implement compression to reduce data transfer volumes
        * Choose CDN regions that align with AWS Region pricing

    For implementation guidance on compression, see [Serving compressed files](../../../AmazonCloudFront/latest/DeveloperGuide/ServingCompressedFiles.md "../../../AmazonCloudFront/latest/DeveloperGuide/ServingCompressedFiles.md") in the CloudFront Developer Guide.

4.  Implement appropriate caching strategies for different content types to reduce
    origin requests. For guidance on cache optimization, see [Improving cache hit ratios](../../../AmazonCloudFront/latest/DeveloperGuide/cache-hit-ratio.md "../../../AmazonCloudFront/latest/DeveloperGuide/cache-hit-ratio.md"). Focus on:

        * Content segments (you can cache these for extended periods)
        * Ad segments (typically reused across viewers)
        * Static assets like player files and images

    Improved cache hit ratios significantly reduce origin costs. Work with your
    CDN provider to optimize cache configurations for your specific content
    patterns. For detailed implementation steps, see [Configuring cache behaviors](../../../AmazonCloudFront/latest/DeveloperGuide/ConfiguringCaching.md "../../../AmazonCloudFront/latest/DeveloperGuide/ConfiguringCaching.md").
