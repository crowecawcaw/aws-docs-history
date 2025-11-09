# Tips for Setting Up CloudFront

As you set up CloudFront to serve your AWS GovCloud (US) content, keep the following in mind:

- You will be setting up CloudFront to distribute content from a custom origin server.
- Because you will be using a custom origin server, you do not have the option to restrict bucket access using a CloudFront Origin Access Identity.
- If you want to restrict viewer access and use signed URLs, you must:
  - Use your standard AWS account and one of its CloudFront key pairs to create the signed URLs. As with other AWS Regions, you use the CloudFront key pair with your code or third-party console to create the signed URLs.
  - You can further restrict access to your content by blocking requests not originating from CloudFront IP addresses. You can use bucket policies to accomplish this for original content stored in AWS GovCloud (US)
    Amazon S3 buckets. A list of IP addresses is maintained on a best-effort basis at [https://forums.aws.amazon.com/ann.jspa?annID=2051](https://forums.aws.amazon.com/ann.jspa?annID=2051 "https://forums.aws.amazon.com/ann.jspa?annID=2051"). For more information, see [AWS IP Address Ranges](../../../general/latest/gr/aws-ip-ranges.md "../../../general/latest/gr/aws-ip-ranges.md").

- If you want CloudFront to log all viewer requests for files in your distribution, select an Amazon S3 bucket in an AWS standard Region as a destination for the log files.
- Since CloudFront is not within AWS GovCloud (US) Regions, CloudFront is not within the ITAR boundary. If you want to use CloudFront to distribute your export-controlled data, encrypt your content in transit.
- Integrated support for CloudFront Live Streaming is not available for origins located in the AWS GovCloud (US) Regions.
- For detailed information about CloudFront, see the [CloudFront documentation](https://aws.amazon.com/documentation/cloudfront/ "https://aws.amazon.com/documentation/cloudfront/").
