# Optimizing MediaTailor performance with CloudFront

features

AWS Elemental MediaTailor performance with Amazon CloudFront can be enhanced through additional features beyond
basic configuration. After setting up your basic CloudFront configuration with MediaTailor, you can
implement additional features to enhance performance, reliability, and customization
options. These optimizations help deliver a better viewing experience. They also reduce
costs and origin load.

For performance optimization using dynamic routing and parameter handling, see [MediaTailor dynamic ad variables for ADS requests](variables.md "variables.md"). For query parameter optimization
strategies, see [MediaTailor manifest query parameters](manifest-query-parameters.md "manifest-query-parameters.md").

## Reducing origin load with Origin

Shield

Origin Shield adds a caching layer between CloudFront edge locations and your origin server.
This feature is valuable for live streaming and popular VOD content. It helps when many
viewers request the same content at the same time.

By consolidating requests from multiple edge locations, Origin Shield reduces the load
on MediaTailor and your content origins.

###### To enable Origin Shield for your MediaTailor origin

1. Open the CloudFront console and navigate to your distribution.
2. Select the origin that points to your MediaTailor playback configuration.
3. Under **Origin Shield**, select
   **Yes**.
4. From the dropdown menu, select the AWS Region that's closest to your MediaTailor
   endpoint.
5. Save your changes.

For high-traffic events, Origin Shield significantly reduces request load on your
origin and improves reliability. For detailed instructions, see [Enabling Origin Shield](../../../AmazonCloudFront/latest/DeveloperGuide/origin-shield.md#enable-origin-shield "../../../AmazonCloudFront/latest/DeveloperGuide/origin-shield.md#enable-origin-shield") in the CloudFront developer guide.

## Customizing content delivery with

CloudFront Functions

CloudFront Functions let you run lightweight JavaScript code at the edge to modify viewer
requests and responses. You can use these functions for simple customizations like URL
modifications, header manipulation, or basic authentication. For MediaTailor workflows,
Functions help with tasks that don't require complex processing.

CloudFront Functions provide a lightweight way to customize content delivery at the edge.
Here's how to implement them for your MediaTailor integration:

###### To implement CloudFront Functions for MediaTailor

1. In the CloudFront console, navigate to **Functions**.
2. Create a new function and select the appropriate purpose:
   - **URL manipulation** - To modify
     multivariant playlist, media playlist, and MPD request URLs before they
     reach MediaTailor
   - **Header manipulation** - To add or
     modify request headers
   - **Simple authentication** - To validate
     tokens or query parameters

3. Write your JavaScript function code.
4. Test your function with sample MediaTailor requests.
5. Publish and associate the function with your distribution's cache
   behavior.

###### Example Sample CloudFront Function for URL normalization

```

function handler(event) {
    var request = event.request;
    var uri = request.uri;

    // Normalize URLs to lowercase to improve cache hit ratio
    if (uri.includes('.m3u8') || uri.includes('.mpd')) {
        request.uri = uri.toLowerCase();
    }

    return request;
}

```

For more information and code examples, see [Customize at
the edge by using CloudFront Functions](../../../AmazonCloudFront/latest/DeveloperGuide/cloudfront-functions.md "../../../AmazonCloudFront/latest/DeveloperGuide/cloudfront-functions.md") in the CloudFront developer guide.

## Implementing advanced customizations with

Lambda@Edge

When you need more complex processing capabilities than CloudFront Functions can provide,
use Lambda@Edge. This service lets you run Node.js or Python functions at CloudFront edge
locations.

Lambda@Edge functions can perform sophisticated operations like complex authentication,
larger response modifications, or third-party API integrations.

For more complex customizations, use Lambda@Edge functions with your MediaTailor and CloudFront
integration:

###### To implement Lambda@Edge with MediaTailor

1. Create a Lambda function in the US East (N. Virginia) Region.
2. Write your function code for one of these use cases:
   - **URL manipulation** - To modify
     multivariant playlist, media playlist, and MPD request URLs before they
     reach MediaTailor
   - **A/B testing** - To route users to
     different ad decision servers
   - **Request authentication** - To add
     authentication headers
   - **Response header modification** - To add
     CORS headers

3. Publish a version of your function and create a function alias.
4. Associate the function with your CloudFront distribution at the appropriate trigger
   point (viewer request or viewer response).

###### Note

When using Lambda@Edge with MediaTailor, avoid using origin-facing triggers (origin
request and origin response) if you plan to use Media Quality-Aware Resiliency
(MQAR) features, as these are currently incompatible.

For more information and code examples, see [Customize at
the edge by using Lambda@Edge](../../../AmazonCloudFront/latest/DeveloperGuide/lambda-at-the-edge.md "../../../AmazonCloudFront/latest/DeveloperGuide/lambda-at-the-edge.md") in the CloudFront developer guide.

## Additional performance optimization

tips

Consider these additional optimizations to further improve performance:

Optimize cache hit ratios

Monitor your cache hit ratio in CloudFront metrics and look for opportunities to
improve it:

- Standardize URL patterns to improve cache key consistency
- Use query string whitelisting to include only necessary parameters
  in the cache key
- Consider implementing URL normalization with CloudFront Functions

Reduce latency

Implement these techniques to minimize latency:

- Enable Brotli compression for text-based responses
- Use HTTP/2 or HTTP/3 for improved connection efficiency
- Consider enabling IPv6 support for modern networks

Cost optimization

Balance performance with cost efficiency:

- Use Origin Shield to reduce redundant origin requests
- Consider price class selection based on your audience
  geography
- Implement aggressive caching for segments to reduce origin
  traffic

## Next steps

After optimizing performance with CloudFront features, consider these next steps:

- Implement multi-Region resilience with MQAR (see [Implement multi-Region resilience for MediaTailor with
  MQAR](media-quality-resiliency.md "media-quality-resiliency.md"))
- Set up monitoring and troubleshooting (see [Monitor and troubleshoot your CloudFront and
  MediaTailor integration](monitoring-and-troubleshooting.md "monitoring-and-troubleshooting.md"))
