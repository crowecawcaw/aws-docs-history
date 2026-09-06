

# Test and validate your CloudFormation deployment for CDN and MediaTailor integration
<a name="test-validate-deployment"></a>

AWS Elemental MediaTailor deployment validation is a critical step for broadcast professionals before going live. This section guides you through testing your deployment to ensure ads are being inserted properly and content is delivered smoothly.

After deploying the CloudFormation template, follow these steps to verify that your setup is working correctly:

**To test your MediaTailor and CloudFront integration**

1. Verify that all resources were created successfully in the CloudFormation console.

1. Check that the MediaTailor playback configuration is active in the [MediaTailor console](https://console.aws.amazon.com/mediatailor/home).

1. Verify that the CloudFront distribution is deployed and enabled in the [CloudFront console](https://console.aws.amazon.com/CloudFront/home).

1. Test playback using a sample manifest:

   1. Construct the full playback URL as described in [Construct playback URLs](use-deployed-resources.md#construct-playback-urls).

   1. Use a video player that supports HLS or DASH (like VLC, JW Player, or the AWS console player).

   1. Verify that content plays and ads are inserted at the expected break points.

1. Check the MediaTailor logs in CloudWatch for any ad insertion errors.

When testing ad insertion, look for these indicators of success:
+ Smooth transitions between content and ads
+ Ads appear at the expected break points (pre-roll, mid-roll, post-roll)
+ Ad quality matches the content quality
+ No buffering or playback errors during ad transitions

For more detailed testing procedures, see [Understanding AWS Elemental MediaTailor ad insertion behavior](ad-behavior.md). For comprehensive CDN integration testing and validation, see [Testing and validation for CDN and MediaTailor integrations](cdn-integration-testing.md).