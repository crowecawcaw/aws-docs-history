

# ADVPERF05-BP02 Use edge services for static content caching and dynamic request acceleration to reduce latency and improve user experience
<a name="advperf05-bp02"></a>

 Edge services can accelerate requests for static content as well as improve the response time for dynamic requests. By using the advantages of the cloud backbone network, it can maximize the efficiency and stability of access after requests enter the cloud. 

## Implementation guidance
<a name="implementation-guidance-52"></a>

 If your advertising workload involves serving static content, such as images or videos, use [Amazon CloudFront](https://aws.amazon.com/cloudfront/) to cache and deliver your content from edge locations around the world. Amazon CloudFront reduces latency and improves user experience for your global audience by serving content from the nearest edge location. 

## Key AWS services
<a name="key-aws-services-28"></a>
+  [Amazon CloudFront](https://aws.amazon.com/cloudfront/) Regional Edge Caches (RECs) 
+  [Amazon CloudFront](https://aws.amazon.com/cloudfront/) Points of Presence (POPs) 
+  [AWS Lambda@Edge](https://aws.amazon.com/lambda/edge/) 

## Resources
<a name="resources-47"></a>
+  [Use an Amazon CloudFront distribution to serve a static website](https://docs.aws.amazon.com/Route 53/latest/DeveloperGuide/getting-started-cloudfront-overview.html) 
+  [Ways to use CloudFront](https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/IntroductionUseCases.html) 
+  [CloudFront configuration best practices](https://docs.aws.amazon.com/whitepapers/latest/amazon-cloudfront-media/cloudfront-configuration-best-practices.html) 
+  [Speeding up your website with Amazon CloudFront](https://docs.aws.amazon.com/AmazonS3/latest/userguide/website-hosting-cloudfront-walkthrough.html) 
+  [Customize at the edge with Lambda@Edge ](https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/lambda-at-the-edge.html) 