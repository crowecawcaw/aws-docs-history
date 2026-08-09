# Static website tutorials

The following tutorials or walkthroughs present complete procedures for how to create and
configure an Amazon S3 general purpose bucket for static website hosting and hosting on-demand
video streaming. The purpose of these tutorials is to provide general guidance. These
tutorials are intended for a lab-type environment, and they use example bucket names, user
names, and so on. They are not intended for direct use in a production environment without
careful review and adaptation to meet the unique needs of your organization's environment.

- [Hosting on-demand
  streaming video with Amazon S3, Amazon CloudFront, and Amazon Route 53](tutorial-s3-cloudfront-route53-video-streaming.md "tutorial-s3-cloudfront-route53-video-streaming.md") – You can use Amazon S3 with Amazon CloudFront
  to host videos for on-demand viewing in a secure and scalable way. After your video is packaged into
  the right formats, you can store it on a server or in an S3 general purpose bucket, and then deliver it with
  CloudFront as viewers request it. In this tutorial, you will learn how to configure your general purpose bucket to
  host on-demand video streaming using CloudFront for delivery and Amazon Route 53 for Domain Name System (DNS) and
  custom domain management. CloudFront serves the video from its cache, retrieving it from your
  general purpose bucket only if it is not already cached. This caching management feature accelerates the
  delivery of your video to viewers globally with low latency, high throughput, and high transfer
  speeds. For more information about CloudFront caching management, see [Optimizing caching and
  availability](../../../AmazonCloudFront/latest/DeveloperGuide/ConfiguringCaching.md "../../../AmazonCloudFront/latest/DeveloperGuide/ConfiguringCaching.md") in the _Amazon CloudFront Developer Guide_.
- [Configuring a
  static website](HostingWebsiteOnS3Setup.md "HostingWebsiteOnS3Setup.md") – You can configure a general purpose bucket to function
  like a website. This tutorial walks you through the steps of hosting a website on
  Amazon S3 including creating a bucket, enabling static website hosting in the S3
  console, creating an index document and creating an error document. For more
  information, see [Hosting a static website
  using Amazon S3](WebsiteHosting.md "WebsiteHosting.md").
- [Configuring a static website using a custom domain registered with Route
  53](website-hosting-custom-domain-walkthrough.md "website-hosting-custom-domain-walkthrough.md") – You can create and configure a general purpose bucket to host a
  static website and create redirects on S3 for a website with a custom domain name
  that is registered with Amazon Route 53. You use Route 53 to register domains and to
  define where you want to route internet traffic for your domain. This tutorial shows
  how to create Route 53 alias records that routes traffic for your domain and
  subdomain to your general purpose bucket that contains an HTML file. For more information,
  see [Use your domain for
  a static website in an Amazon S3 bucket](../../../Route53/latest/DeveloperGuide/getting-started-s3.md "../../../Route53/latest/DeveloperGuide/getting-started-s3.md") in the _Amazon Route 53
  Developer Guide_. After you complete this tutorial, you can optionally
  use CloudFront to improve the performance of your website. For more information, see
  [Speeding up your website with Amazon CloudFront](website-hosting-cloudfront-walkthrough.md "website-hosting-cloudfront-walkthrough.md").
- [Deploying a static website to AWS Amplify Hosting from an S3 general purpose bucket](website-hosting-amplify.md "website-hosting-amplify.md") –
  We recommend that you use [AWS Amplify Hosting](../../../amplify/latest/userguide/welcome.md "../../../amplify/latest/userguide/welcome.md")
  to host static website content stored on S3. Amplify Hosting is a fully managed service that makes it easy to deploy your websites on a
  globally available content delivery network (CDN) powered by Amazon CloudFront, allowing secure static website hosting without extensive setup. With AWS Amplify Hosting, you can select the location of your objects within your general purpose bucket, deploy your content to a managed CDN, and generate a public HTTPS URL for your website to be accessible anywhere. For more information, see [Deploying a static
  website from S3 using the Amplify console](../../../amplify/latest/userguide/deploy--from-amplify-console.md "../../../amplify/latest/userguide/deploy--from-amplify-console.md") in the _AWS Amplify Hosting
  User Guide_.
