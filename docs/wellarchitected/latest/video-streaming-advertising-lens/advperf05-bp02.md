# ADVPERF05-BP02 Use edge services for static content caching and dynamic request acceleration to reduce latency and improve user experience

Edge services can accelerate requests for static content as well
as improve the response time for dynamic requests. By using the
advantages of the cloud backbone network, it can maximize the
efficiency and stability of access after requests enter the cloud.

## Implementation guidance

If your advertising workload involves serving static content,
such as images or videos, use
[Amazon CloudFront](https://aws.amazon.com/cloudfront/ "https://aws.amazon.com/cloudfront/") to cache and deliver your content from edge
locations around the world. Amazon CloudFront reduces latency
and improves user experience for your global audience by serving
content from the nearest edge location.

## Key AWS services

- [Amazon CloudFront](https://aws.amazon.com/cloudfront/ "https://aws.amazon.com/cloudfront/") Regional Edge Caches (RECs)
- [Amazon CloudFront](https://aws.amazon.com/cloudfront/ "https://aws.amazon.com/cloudfront/") Points of Presence (POPs)
- [AWS Lambda@Edge](https://aws.amazon.com/lambda/edge/ "https://aws.amazon.com/lambda/edge/")

## Resources

- [Use
  an Amazon CloudFront distribution to serve a static website](../../../Route%C2%A053/latest/DeveloperGuide/getting-started-cloudfront-overview.md "../../../Route%C2%A053/latest/DeveloperGuide/getting-started-cloudfront-overview.md")
- [Ways
  to use CloudFront](../../../AmazonCloudFront/latest/DeveloperGuide/IntroductionUseCases.md "../../../AmazonCloudFront/latest/DeveloperGuide/IntroductionUseCases.md")
- [CloudFront
  configuration best practices](../../../whitepapers/latest/amazon-cloudfront-media/cloudfront-configuration-best-practices.md "../../../whitepapers/latest/amazon-cloudfront-media/cloudfront-configuration-best-practices.md")
- [Speeding
  up your website with Amazon CloudFront](../../../AmazonS3/latest/userguide/website-hosting-cloudfront-walkthrough.md "../../../AmazonS3/latest/userguide/website-hosting-cloudfront-walkthrough.md")
- [Customize
  at the edge with Lambda@Edge](../../../AmazonCloudFront/latest/DeveloperGuide/lambda-at-the-edge.md "../../../AmazonCloudFront/latest/DeveloperGuide/lambda-at-the-edge.md")
