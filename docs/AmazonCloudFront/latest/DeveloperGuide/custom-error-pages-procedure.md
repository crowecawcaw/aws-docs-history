# Configure error response

behavior

You have several options to manage how CloudFront responds when there’s an error. To
configure custom error responses, you can use the CloudFront console, the CloudFront API, or AWS CloudFormation.
Regardless of how you choose to update the configuration, consider the following tips
and recommendations:

- Save your custom error pages in a location that is accessible to CloudFront. We
  recommend that you store them in an Amazon S3 bucket, and that you [don’t store them in the
  same place as the rest of your website or application’s content](custom-error-pages-different-locations.md "custom-error-pages-different-locations.md"). If
  you store the custom error pages on the same origin as your website or
  application, and the origin starts to return 5xx errors, CloudFront can’t get the
  custom error pages because the origin server is unavailable. For more
  information, see [Store objects and custom
  error pages in different locations](custom-error-pages-different-locations.md "custom-error-pages-different-locations.md").
- Make sure that CloudFront has permission to get your custom error pages. If the
  custom error pages are stored in Amazon S3, the pages must be publicly accessible or
  you must configure a CloudFront [origin access control
  (OAC)](private-content-restricting-access-to-s3.md "private-content-restricting-access-to-s3.md"). If the custom error pages are stored in a custom origin, the
  pages must be publicly accessible.
- (Optional) Configure your origin to add a `Cache-Control` or
  `Expires` header along with the custom error pages, if you want.
  You can also use the **Error Caching Minimum TTL** setting to
  control how long CloudFront caches the custom error pages. For more information, see
  [Control how long CloudFront caches
  errors](custom-error-pages-expiration.md "custom-error-pages-expiration.md").

## Configure custom error responses

To configure custom error responses in the CloudFront console, you must have a CloudFront
distribution. In the console, the configuration settings for custom error responses
are only available for existing distributions. To learn how to create a
distribution, see [Get started with a CloudFront standard distribution](GettingStarted.md "GettingStarted.md").

Console

###### To configure custom error responses (console)

1. Sign in to the AWS Management Console and open the **Distributions**
   page in the CloudFront console at [https://console.aws.amazon.com/cloudfront/v4/home#distributions](https://console.aws.amazon.com/cloudfront/v4/home#distributions "https://console.aws.amazon.com/cloudfront/v4/home#distributions").
2. In the list of distributions, choose the distribution to update.
3. Choose the **Error Pages** tab, then choose
   **Create Custom Error Response**.
4. Enter the applicable values. For more information, see [Custom error pages and error
   caching](DownloadDistValuesErrorPages.md "DownloadDistValuesErrorPages.md").
5. After entering the desired values, choose
   **Create**.

CloudFront API or AWS CloudFormationTo configure custom error responses with the CloudFront API or AWS CloudFormation, use the
`CustomErrorResponse` type in a distribution. For more information,
see the following:

- [AWS::CloudFront::Distribution CustomErrorResponse](../../../AWSCloudFormation/latest/UserGuide/aws-properties-cloudfront-distribution-customerrorresponse.md "../../../AWSCloudFormation/latest/UserGuide/aws-properties-cloudfront-distribution-customerrorresponse.md") in the
  _AWS CloudFormation User Guide_
- [CustomErrorResponse](../../../cloudfront/latest/APIReference/API_CustomErrorResponse.md "../../../cloudfront/latest/APIReference/API_CustomErrorResponse.md") in the _Amazon CloudFront API Reference_
