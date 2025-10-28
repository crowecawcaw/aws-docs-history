# MediaTailor ad skipping prevention

best practices

Implementing these best practices helps prevent ad skipping issues before they occur,
ensuring better ad insertion performance and revenue protection with AWS Elemental MediaTailor. These
proactive measures address the most common causes of ad skipping and help maintain
consistent ad delivery.

## Proactive measures

- **Implement ad prefetching**: Use MediaTailor's
  prefetch feature to ensure ads are transcoded before playback. See [Prefetching ads](prefetching-ads.md "prefetching-ads.md") for implementation details
- **Maintain consistent creative IDs**: Ensure
  your ad decision server uses consistent creative IDs for the same ad content
  across sessions
- **Ensure proper duration formatting**: Use
  integer values for EXT-X-CUE-OUT duration parameters instead of ISO 8601
  format
- **Configure VOD optimization**: Set
  maxConcurrentAdsRequests for VOD streams with multiple ad breaks to reduce
  server load
- **Optimize ADS performance**: Configure your
  ad decision server to respond quickly and handle peak traffic volumes

## Implementation guidelines

- **Implement proper error handling**:
  Configure slate content to fill ad breaks when ads cannot be inserted
- **Test thoroughly**: Validate your ad
  insertion workflow across different devices and network conditions
- **Implement fallback strategies**: Configure
  backup ad sources or default ads for when primary ad sources fail
- **Monitor transcoding patterns**: Monitor
  CloudWatch logs for transcoding efficiency and contact [AWS Support](https://aws.amazon.com/premiumsupport/ "https://aws.amazon.com/premiumsupport/") if you notice
  patterns that indicate transcoding issues
