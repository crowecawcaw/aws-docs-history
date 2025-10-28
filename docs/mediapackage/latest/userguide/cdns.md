# Working with AWS Elemental MediaPackage and CDNs

You can use a content delivery network (CDN) such as [Amazon CloudFront](../../../AmazonCloudFront/latest/DeveloperGuide.md "../../../AmazonCloudFront/latest/DeveloperGuide.md") to serve the content that you store in AWS Elemental MediaPackage. A CDN is a
globally distributed set of servers that caches content such as videos. When a user requests
your content, the CDN routes the request to the edge location that provides the lowest
latency. If your content is already cached in that edge location, the CDN delivers it
immediately. If your content is not currently in that edge location, the CDN retrieves it
from your origin (in this case, the MediaPackage endpoint) and distributes it to the user.
The following illustration shows this process.

![This illustration shows how content that's stored in MediaPackage is distributed using a CDN.](images/cf_flow.png)
The following sections provide more information about using a CDN in your MediaPackage
workflow.

###### Topics

- [CDN configuration recommendations](cdn-recommendations.md "cdn-recommendations.md")
- [Secure MediaPackage content with CDN authorization](cdn-auth.md "cdn-auth.md")
