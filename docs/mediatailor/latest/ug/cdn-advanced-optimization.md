# Advanced optimization techniques for CDN and

MediaTailor integrations

After implementing basic caching and routing optimizations, consider these advanced
techniques to further enhance performance:

## Origin Shield implementation

Origin Shield adds a caching layer between CDN edge locations and your origin
server, reducing origin load and improving performance:

- Enable Origin Shield for high-traffic content and live streaming
- Choose Origin Shield locations close to your MediaTailor regions
- Monitor Origin Shield cache hit ratios and adjust as needed
- Consider multiple Origin Shield locations for global deployments

## Content compression optimization

Optimize content compression to reduce bandwidth and improve delivery
speed:

- Enable gzip compression for manifest files
- Configure Accept-Encoding header forwarding for MediaTailor manifest
  compression
- Use Brotli compression where supported for additional bandwidth
  savings
- Avoid compressing already-compressed video segments

## Regional optimization strategies

Optimize performance for global audiences through regional strategies:

- Deploy MediaTailor configurations in multiple regions for global
  audiences
- Use geo-routing to direct viewers to the nearest MediaTailor region
- Configure regional failover for high availability
- Monitor regional performance metrics separately
