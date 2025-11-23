# Troubleshoot common CloudFormation deployment

issues for CDN and MediaTailor integrations

AWS Elemental MediaTailor deployment issues can occur even with automation during deployment or playback. As a broadcast
professional, understanding how to troubleshoot these issues will help you maintain a
reliable streaming service with ad insertion.

If you encounter issues with your CloudFormation deployment or the resulting MediaTailor and CloudFront
integration, refer to these common problems and solutions:

## CloudFormation deployment issues

Stack creation fails with "Resource creation failed" error

**Possible causes:**

- Invalid content origin domain name format
- Insufficient permissions to create resources

**Solution:** Check the specific resource
error in the CloudFormation events tab. Verify that the content origin domain
name is correctly formatted without protocol prefixes or paths. Ensure
your IAM role has sufficient permissions to create all required
resources.

CloudFront distribution takes a long time to deploy

**Cause:** CloudFront distributions typically
take 15-30 minutes to fully deploy.

**Solution:** This is normal behavior.
Wait for the distribution to reach the "Deployed" state before
testing.

## Playback and ad insertion issues

Content plays but no ads are inserted

**Possible causes:**

- Ad decision server not responding or returning empty
  VAST
- Content does not contain ad markers

**Solution:** Verify that your ad server
is accessible and returning valid VAST responses. Check that your
content has proper ad markers (SCTE-35 markers for live content or ad
break tags for VOD).

403 Forbidden errors when accessing content

**Possible causes:**

- Origin access control not configured correctly
- Origin bucket or endpoint permissions issues

**Solution:** For Amazon S3 origins, verify
that the bucket policy allows access from the CloudFront distribution. For
MediaPackage origins, check that the origin access control is properly
configured and that the endpoint is accessible.

Playback errors or buffering

**Possible causes:**

- Cache behavior path patterns not matching content paths
- Incorrect origin domain configuration

**Solution:** Verify that your cache
behaviors have the correct path patterns to route requests to the
appropriate origins. Check CloudFront logs to see which origin is handling the
requests and confirm it's the expected one.

For broadcast professionals, these additional troubleshooting tips may
help:

- Use the Amazon CloudWatch Logs Insights to search for specific error patterns in MediaTailor
  logs
- Test with a simple VAST ad server first (like the default one provided in
  the template) before using your production ad server
- Verify your content's ad markers using the MediaTailor manifest inspector tool
  in the console
- Check network traffic in your browser's developer tools to see if requests
  to the ad server are being made correctly

For additional troubleshooting, check the CloudWatch logs for both MediaTailor and CloudFront to
identify specific errors.
