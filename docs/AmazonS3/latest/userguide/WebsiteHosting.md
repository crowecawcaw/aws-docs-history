# Hosting a static website using Amazon S3

You can use Amazon S3 to host a static website. On a *static* website,
 individual webpages include static content. They might also contain client-side
 scripts.

###### Note

We recommend that you use [AWS Amplify Hosting](https://docs.aws.amazon.com/amplify/latest/userguide/welcome.html.html "https://docs.aws.amazon.com/amplify/latest/userguide/welcome.html.html") to
 host static website content stored on S3. Amplify Hosting is a fully managed service
 that makes it easy to deploy your websites on a globally available content delivery
 network (CDN) powered by Amazon CloudFront, allowing secure static website hosting. 

With AWS Amplify Hosting, you can select the location of your objects within your
 general purpose bucket, deploy your content to a managed CDN, and generate a public
 HTTPS URL for your website to be accessible anywhere. For more information about Amplify
 Hosting, see [Deploying a static
 website to AWS Amplify Hosting from an S3 general purpose bucket](website-hosting-amplify.md "website-hosting-amplify.md") and
 [Deploying a static
 website from S3 using the Amplify console](https://docs.aws.amazon.com/amplify/latest/userguide/deploy--from-amplify-console.html "https://docs.aws.amazon.com/amplify/latest/userguide/deploy--from-amplify-console.html") in the *AWS Amplify
 Console User Guide*.

For more information about hosting a static website on Amazon S3, including instructions and
 step-by-step walkthroughs, see the following topics.

###### Important

If the bucket that you're using to host your static website has been encrypted using server-side
 encryption with AWS Key Management Service (AWS KMS) keys (SSE-KMS), you must create an Amazon CloudFront distribution to serve your
 website because SSE-KMS doesn't support anonymous users. When you create your CloudFront distribution, you
 must use origin access control (OAC) instead of origin access identity (OAI) to secure the origin. OAI
 doesn't support SSE-KMS, so you must use OAC instead.

For more information about OAC, see [Restrict
 access to an Amazon S3 origin](https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/private-content-restricting-access-to-s3.html "https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/private-content-restricting-access-to-s3.html") in the *Amazon CloudFront Developer Guide*. For a tutorial that shows
 how to host a static website using Amazon CloudFront, see [Tutorial: Hosting on-demand
 streaming video with Amazon S3, Amazon CloudFront, and Amazon Route 53](tutorial-s3-cloudfront-route53-video-streaming.md "tutorial-s3-cloudfront-route53-video-streaming.md").

###### Topics

* [Website endpoints](WebsiteEndpoints.md "WebsiteEndpoints.md")
* [Enabling website hosting](EnableWebsiteHosting.md "EnableWebsiteHosting.md")
* [Configuring an index document](IndexDocumentSupport.md "IndexDocumentSupport.md")
* [Configuring a custom error document](CustomErrorDocSupport.md "CustomErrorDocSupport.md")
* [Setting permissions for website
 access](WebsiteAccessPermissionsReqd.md "WebsiteAccessPermissionsReqd.md")
* [(Optional) Logging web traffic](LoggingWebsiteTraffic.md "LoggingWebsiteTraffic.md")
* [(Optional) Configuring a webpage redirect](how-to-page-redirect.md "how-to-page-redirect.md")
* [Using cross-origin resource sharing (CORS)](cors.md "cors.md")
* [Static website tutorials](static-website-tutorials.md "static-website-tutorials.md")
