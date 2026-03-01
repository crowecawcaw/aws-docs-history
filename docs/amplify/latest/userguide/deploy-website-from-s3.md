# Deploying a static website to Amplify from an Amazon S3 bucket

You can use the integration between Amplify Hosting and Amazon S3 to host static website
content stored on S3 with just a few clicks. Deploying to Amplify Hosting
provides you with the following benefits and features.

- Automatic deployment to the globally available AWS content delivery network
  (CDN) powered by CloudFront
- HTTPS support
- Easily connect your website to a custom domain using the Amplify console
- Bring your own Custom SSL certificates
- Monitor your website with built in access logs and CloudWatch metrics
- Set up password protection for your website
- Create redirect and rewrites rules in the Amplify console
  You can start the deployment process from the Amplify console, the AWS CLI, or the AWS
  SDKs. You can only deploy to Amplify from an Amazon S3 general purpose bucket located in your own
  account. Amplify doesn't support cross-account S3 bucket access.

When you deploy your application from an Amazon S3 general purpose bucket to Amplify Hosting, AWS charges
are based on Amplify's pricing model. For more information, see [AWS Amplify Pricing](https://aws.amazon.com/amplify/pricing/ "https://aws.amazon.com/amplify/pricing/").

###### Important

Amplify Hosting is not available in all of the AWS Regions where Amazon S3 is
available. To deploy a static website to Amplify Hosting, the Amazon S3 general purpose
bucket containing your website must be located in a region where Amplify is available.
For the list of regions where Amplify is available, see [Amplify endpoints](../../../general/latest/gr/amplify.md#amplify_region "../../../general/latest/gr/amplify.md#amplify_region") in
the _Amazon Web Services General Reference_.

See the following topics to learn how to deploy and update a static website from Amazon S3 to
Amplify Hosting.

###### Topics

- [Deploying a static website from S3 using the Amplify console](deploy--from-amplify-console.md "deploy--from-amplify-console.md")
- [Creating a bucket policy to deploy a static website from S3 using the AWS SDKs](deploy-with-sdks.md "deploy-with-sdks.md")
- [Updating a static website deployed to Amplify from an S3 bucket](update-website-deployed-from-s3.md "update-website-deployed-from-s3.md")
- [Updating an S3 deployment to use a bucket and prefix instead of a .zip file](update-s3-zip-to-bucket.md "update-s3-zip-to-bucket.md")
