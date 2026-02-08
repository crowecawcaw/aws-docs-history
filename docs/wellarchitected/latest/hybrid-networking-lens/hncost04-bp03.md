# HNCOST04-BP03 Implement compression and caching for repetitive

data transfers

Reduce data transfer volumes by compressing in-transit data and
caching frequently accessed content at the edge.

**Desired outcome:** Reduction in
data transfer volumes and associated costs.

**Level of risk exposed if this best practice
is not established:** Low

**Benefits of establishing this best
practice:**

- Lower bandwidth consumption
- Faster transfer times
- Reduced storage costs for compressed data

## Implementation guidance

- Enable compression for payloads
- Configure TTL for static assets in content delivery network
  such as Amazon CloudFront
- Use compression for file/volume syncs using services such as
  AWS Storage Gateway

## Resources

- [Manage
  how long content stays in the cache](../../../AmazonCloudFront/latest/DeveloperGuide/Expiration.md "../../../AmazonCloudFront/latest/DeveloperGuide/Expiration.md")
- [Payload
  compression for REST APIs in API Gateway](../../../apigateway/latest/developerguide/api-gateway-gzip-compression-decompression.md "../../../apigateway/latest/developerguide/api-gateway-gzip-compression-decompression.md")
- [AWS Storage Gateway FAQ](https://aws.amazon.com/storagegateway/faqs/ "https://aws.amazon.com/storagegateway/faqs/")
