

# Update your access endpoint with a custom URL
<a name="webapp-customize"></a>

The default access endpoint that is created with your web app contains service-generated identifiers. To provide a branded experience, you may want to provide a custom URL for your users to access your Transfer Family web app. This topic describes how to update your access endpoint with a custom URL.

**To customize your web app URL**

1. Set up TLS termination and forwarding for your custom domain name. The steps differ depending on whether you use a public or VPC web app.

   1. For a public web app, create a CloudFront distribution by using the Transfer Family supplied AWS CloudFormation template, [CloudFormation stack template](https://s3.amazonaws.com/aws-transfer-resources/custom-domain-templates/aws-transfer-web-app-custom-domain-distribution.template.yml).

      1. Open the CloudFormation console at [https://console.aws.amazon.com/cloudformation](https://console.aws.amazon.com/cloudformation/).

      1. Choose **Create stack** and specify the following.
         + In the **Prerequisite - Prepare template** section, choose **Choose an existing template**.
         + In the **Specify template** section, choose **Upload a template file**.
         + Save the [CloudFormation stack template](https://s3.amazonaws.com/aws-transfer-resources/custom-domain-templates/aws-transfer-web-app-custom-domain-distribution.template.yml) file, and then upload it here.

      1. Choose **Next** and provide the following information.
         + **WebAppEndpoint**: copy the value from your web app
         + **AccessEndpoint**: provide the custom domain name that you want to use
         + **AcmCertificateArn**: provide the ARN for a public or private SSL/TLS certificate that is stored in AWS Certificate Manager 

      1. Complete the CloudFormation wizard until your new stack is created.

      1. After the stack is created, you need to create DNS records to route traffic for your custom domain name to the CloudFront distribution. If you're using Route 53 for DNS, you can create an Alias or CNAME record to the CloudFront distribution name. For information about using Amazon Route 53 with CloudFront, see [Configuring Amazon Route 53 to route traffic to a CloudFront distribution](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/routing-to-cloudfront-distribution.html#routing-to-cloudfront-distribution-config).

   1. For a VPC web app, you must provide your own TLS termination solution for your custom domain. Your solution must use a valid SSL/TLS certificate for your custom domain. Configure your solution to forward traffic to your web app's PrivateLink DNS name.
**Note**  
For your own forwarding solution, configure the following:  
Ensure that you are using HTTPS.
Forward all HTTP methods: GET, HEAD, OPTIONS, PUT, POST, PATCH, DELETE.
Forward all HTTP headers in the request and response, except the `Host` header. The `Host` header sent to the web app should be the WebAppEndpoint value.
Disable all response caching.

1. In your web app, edit the **Access endpoint**, updating the **Custom URL** to the URL that you want to use.  
![Screen showing a custom access endpoint for a Transfer Family web app.](https://docs.aws.amazon.com/transfer/latest/userguide/images/webapp-custom-name.png)

1. Update your cross-origin resource sharing policy by replacing the default access endpoint with the following line in the `AllowedOrigins` code block:

   ```
    "https://{{custom-url}}"
   ```

   You need to make this change for each bucket used by your web app.

   After you make your update, the `AllowedOrigins` section of your CORS policy should look like the following:

   ```
   "AllowedOrigins": [
       "https://{{custom-url}}"],
   ```

   You need only a single AllowedOrigins entry for each Transfer Family web app.

   See the [Set up Cross-origin resource sharing (CORS) for your Amazon S3 bucket](access-grant-cors.md#cors-configure) procedure for more details.

You can now visit your custom access endpoint, and share this link with your end users.