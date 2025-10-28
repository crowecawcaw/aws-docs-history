# Getting started with Amazon Route 53

Get started with the basic steps by registering a domain with Amazon Route 53 and configuring Route 53 to respond to DNS queries that resolve to
a static website. The first tutorial hosts a static website in an open Amazon S3 bucket, and the second tutorial uses Amazon CloudFront distribution to serve the website
with SSL/TLS.

**Estimated cost**

- There's an annual fee to register a domain, ranging from $9 to several hundred dollars, depending on the top-level domain,
  such as .com. For more information, see
  [Route 53 Pricing for Domain Registration](https://d32ze2gidvkk54.cloudfront.net/Amazon_Route_53_Domain_Registration_Pricing_20140731.pdf "https://d32ze2gidvkk54.cloudfront.net/Amazon_Route_53_Domain_Registration_Pricing_20140731.pdf").
  This fee is not refundable.
- When you register a domain, we automatically create a hosted zone that has the same name as the domain. You use the hosted zone
  to specify where you want Route 53 to route traffic for your domain.
- During this tutorial, you create an Amazon S3 bucket and upload a sample web page. If you're a new AWS customer,
  you can get started with Amazon S3 for free. If you're an existing AWS customer, charges are based on how much data you store,
  on the number of requests for your data, and on the amount of data transferred. For more information, see
  [Amazon S3 Pricing](https://aws.amazon.com/s3/pricing/ "https://aws.amazon.com/s3/pricing/").
- CloudFront charges are based on the number of requests for your data, the number of edge locations
  you use, and on the amount of data transferred. For more information, see [CloudFront Pricing](https://aws.amazon.com/cloudfront/pricing/ "https://aws.amazon.com/cloudfront/pricing/").

###### Topics

- [Set up](setting-up-route-53.md "setting-up-route-53.md")
- [Route DNS traffic to an Amazon S3 static
  website](getting-started-s3.md "getting-started-s3.md")
- [Route DNS traffic to a CloudFront
  distribution](getting-started-cloudfront-overview.md "getting-started-cloudfront-overview.md")
