

# Monitor and troubleshoot your CloudFront and MediaTailor integration
<a name="monitoring-and-troubleshooting"></a>

AWS Elemental MediaTailor integration with Amazon CloudFront requires ongoing monitoring and troubleshooting to maintain optimal performance. After implementing your CloudFront and MediaTailor integration, monitor performance and prepare to troubleshoot any issues. The content delivery network (CDN) provides tools to help you understand how your distribution performs and identify potential problems.

## Setting up monitoring for your integration
<a name="cf-monitoring-setup"></a>

Implement these monitoring strategies to track the performance of your CloudFront and MediaTailor integration:

**To set up monitoring for your CloudFront and MediaTailor integration**

1. Enable CloudFront standard logging:

   1. In the CloudFront console, select your distribution.

   1. Choose the **Logs** tab.

   1. Under **Standard logs**, choose **Edit**.

   1. Select **On** and configure an Amazon S3 bucket for log storage.

   1. Choose **Save changes**.

1. Set up CloudFront real-time logs:

   1. In the CloudFront console, select your distribution.

   1. Choose the **Logs** tab.

   1. Under **Real-time logs**, choose **Edit**.

   1. Select **On** and configure an Amazon Kinesis Data Streams or Amazon Data Firehose delivery stream.

   1. Include these fields in your log configuration:
      + `time-to-first-byte` - Response time
      + `sc-status` - HTTP status code
      + `c-ip` - Viewer IP address
      + `cs-uri-stem` - Request URI path
      + `cs-user-agent` - User agent
      + `x-edge-result-type` - Result type (Hit, Miss, Error)

   1. Choose **Save changes**.

1. Create CloudWatch dashboards:

   1. In the CloudWatch console, choose **Dashboards**.

   1. Choose **Create dashboard**.

   1. Add widgets for these CloudFront metrics:
      + Requests
      + BytesDownloaded
      + 4xxErrorRate
      + 5xxErrorRate
      + TotalErrorRate
      + CacheHitRate

1. Set up CloudWatch alarms:

   1. In the CloudWatch console, choose **Alarms**.

   1. Choose **Create alarm**.

   1. Create alarms for these conditions:
      + 5xxErrorRate > 1% for 5 minutes
      + 4xxErrorRate greater than 5% for 5 minutes
      + CacheHitRate less than 80% for 30 minutes

## Monitoring MQAR performance
<a name="mqar-monitoring"></a>

When using MQAR, monitoring helps you understand how CloudFront selects between your origins and whether the quality scores meet expectations. Real-time logs show these decisions as they happen.

**To monitor MQAR performance**

1. Enable real-time logs for your CloudFront distribution.

1. Include these fields in your log configuration:
   + `r-host` - The hostname of the selected origin
   + `sr-reason` - The reason for origin selection
   + `x-edge-mqcs` - The media quality confidence score

1. Set up a log destination in Amazon Kinesis Data Streams or Amazon Data Firehose.

1. Create dashboards or alerts based on these metrics to monitor quality scores and origin selection decisions.

**Example Sample CloudWatch dashboard for MQAR monitoring**  
Create a CloudWatch dashboard with these metrics:  
+ Origin selection counts by Region
+ Average quality scores over time
+ Failover events
+ 4xx and 5xx error rates by origin

For more information about setting up real-time logs, see [Real-time logs](https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/real-time-logs.html) in the CloudFront developer guide.

## Troubleshooting common issues
<a name="troubleshooting-common-issues"></a>

Issues can arise with your CloudFront and MediaTailor integration even with careful planning. Understanding common problems and solutions helps you resolve issues quickly and minimize viewer impact.

If you encounter issues with your CloudFront and MediaTailor integration, check these common problems and solutions:

Manifest caching issues  
**Symptom:** Stale manifests or ads not updating  
**Solution:** Verify you're using the `CachingDisabled` cache policy for multivariant playlist, media playlist, and MPD paths. Check that your configuration forwards query parameters correctly.

CORS errors  
**Symptom:** Browser console shows CORS errors when accessing content  
**Solution:** Configure a response headers policy with appropriate CORS headers and associate it with your cache behavior.

MQAR not working  
**Symptom:** Origin selection ignores quality scores  
**Solution:** Check that you've enabled the Media quality score option in your origin group settings. Verify you're not using Lambda@Edge origin-facing triggers.

Ad insertion failures  
**Symptom:** Ads not inserting properly  
**Solution:** Verify your MediaTailor configuration points to your CloudFront distribution for content segment prefix. Check that your setup forwards all required headers.

For more complex issues, you can use these troubleshooting approaches:

1. Check CloudFront distribution logs for error patterns

1. Use browser developer tools to inspect network requests

1. Compare manifest content from MediaTailor directly compared to content delivered through CloudFront

1. Test with a simple player that supports detailed logging

For more troubleshooting assistance, see the [Troubleshooting](https://docs.aws.amazon.com/mediatailor/latest/ug/troubleshooting.html) section in the MediaTailor user guide.

## Troubleshooting workflow
<a name="troubleshooting-workflow"></a>

Follow this systematic approach to troubleshoot issues with your CloudFront and MediaTailor integration:

**To troubleshoot CloudFront and MediaTailor integration issues**

1. Identify the specific issue:

   1. Determine if the issue affects all viewers or only some

   1. Identify which content types are affected (manifests, segments, or both)

   1. Note any error messages or symptoms

1. Check CloudFront logs:

   1. Look for error status codes (4xx or 5xx)

   1. Check cache hit/miss patterns

   1. Verify that requests are being routed to the correct origin

1. Verify configuration:

   1. Check cache behaviors for correct path patterns

   1. Verify cache policies are correctly applied

   1. Confirm that origin request policies are forwarding necessary headers

1. Test direct access:

   1. Try accessing content directly from MediaTailor (bypassing CloudFront)

   1. Compare responses between direct access and CloudFront access

1. Implement solution:

   1. Apply the appropriate fix based on your findings

   1. Test to verify the issue is resolved

   1. Document the issue and solution for future reference

## Next steps
<a name="monitoring-next-steps"></a>

After setting up monitoring and troubleshooting for your CloudFront and MediaTailor integration, consider these next steps:
+ Implement automated deployment using AWS CloudFormation (see [Automate MediaTailor and CDN with CloudFormation](automating-cdn-integration.md))
+ Create runbooks for common operational scenarios and troubleshooting procedures
+ Set up automated remediation for common issues