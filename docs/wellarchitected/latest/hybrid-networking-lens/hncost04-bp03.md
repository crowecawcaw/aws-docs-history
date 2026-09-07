

# HNCOST04-BP03 Implement compression and caching for repetitive data transfers
<a name="hncost04-bp03"></a>

 Reduce data transfer volumes by compressing in-transit data and caching frequently accessed content at the edge. 

 **Desired outcome:** Reduction in data transfer volumes and associated costs. 

 **Level of risk exposed if this best practice is not established:** Low 

 **Benefits of establishing this best practice:** 
+  Lower bandwidth consumption 
+  Faster transfer times 
+  Reduced storage costs for compressed data 

## Implementation guidance
<a name="implementation-guidance-54"></a>
+  Enable compression for payloads 
+  Configure TTL for static assets in content delivery network such as Amazon CloudFront 
+  Use compression for file/volume syncs using services such as AWS Storage Gateway 

## Resources
<a name="resources-45"></a>
+  [Manage how long content stays in the cache](https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/Expiration.html) 
+  [Payload compression for REST APIs in API Gateway](https://docs.aws.amazon.com/apigateway/latest/developerguide/api-gateway-gzip-compression-decompression.html) 
+  [AWS Storage Gateway FAQ](https://aws.amazon.com/storagegateway/faqs/) 