# Deploying a static website to AWS Amplify Hosting from an S3 general purpose bucket

We recommend that you use [AWS Amplify Hosting](https://docs.aws.amazon.com/amplify/latest/userguide/welcome.html.html "https://docs.aws.amazon.com/amplify/latest/userguide/welcome.html.html") 
 to host static website content stored on S3. 
 Amplify Hosting is a fully managed service that makes
 it easy to deploy your websites on a globally available content delivery network (CDN)
 powered by Amazon CloudFront, allowing secure static website hosting without extensive
 setup. With AWS Amplify Hosting, you can select the location of your objects within your general purpose bucket, deploy your content to a managed CDN, 
 and generate a public HTTPS URL for your website to be accessible anywhere. 
 Deploying a static website using Amplify Hosting provides you with the following
 benefits and features:


* **Deployment to the AWS content delivery network (CDN) powered by Amazon
 CloudFront** - CloudFront is a web service that speeds up distribution
 of your static and dynamic web content to your users. CloudFront delivers your
 content through a worldwide network of data centers called edge locations. When a
 user requests content that you're serving with CloudFront, the request is routed to
 the edge location that provides the lowest latency (time delay), so that content is
 delivered with the best possible performance, increased reliability and
 availability. For more information, see [How CloudFront delivers
 content](https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/HowCloudFrontWorks.html "https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/HowCloudFrontWorks.html") in the *Amazon CloudFront Developer
 Guide*.
* **HTTPS support** - Provides secure communication and data transfer between your website and a user’s web browser.
* **Custom domains** - Easily connect your website to a custom URL purchased
 from a domain registrar such as Amazon Route 53.
* **Custom SSL certificates** - When you set up your custom domain, you can use the default managed certificate that Amplify provisions for you or you can use your own custom certificate purchased from the third-party certificate authority of your choice.
* **Built in metrics and CloudWatch monitoring** - Monitor traffic, errors, data transfer, and latency for your website.
* **Password protection** - Restrict access to your website, by setting up a
 username and password requirement in the Amplify console.
* **Redirects and rewrites**  - Create redirect and rewrite rules in the Amplify console to enable a web server to reroute navigation from one URL to another.
When you deploy your application from an Amazon S3 general purpose bucket to Amplify Hosting, AWS charges
 are based on Amplify's pricing model. For more information, see [AWS Amplify Pricing](https://aws.amazon.com/amplify/pricing/ "https://aws.amazon.com/amplify/pricing/").

###### Important

Amplify Hosting is not available in all of the AWS Regions where Amazon S3 is
 available. To deploy a static website to Amplify Hosting, the Amazon S3 general purpose
 bucket containing your website must be located in a region where Amplify is available.
 For the list of regions where Amplify is available, see [Amplify endpoints](https://docs.aws.amazon.com/general/latest/gr/amplify.html#amplify_region "https://docs.aws.amazon.com/general/latest/gr/amplify.html#amplify_region") in
 the *Amazon Web Services General Reference*.

You can start the deployment process from the Amazon S3 console, the Amplify console, the AWS CLI, or the AWS SDKs. You can only deploy to Amplify from a general purpose bucket located in your own account. Amplify doesn't support cross-account bucket access. 

Use the following instructions to deploy a static website from an Amazon S3 general
 purpose bucket to Amplify Hosting starting from the Amazon S3 console.


## Deploying a static website to Amplify from the S3
 console


###### To deploy a static website from the Amazon S3 console

1. Sign in to the AWS Management Console and open the Amazon S3 console at
 [https://console.aws.amazon.com/s3/](https://console.aws.amazon.com/s3/ "https://console.aws.amazon.com/s3/").
2. In the left navigation pane, choose **Buckets**.
3. In the **Buckets** list, choose the general purpose bucket that contains the website you want to deploy to Amplify Hosting.
4. Choose the **Properties** tab.
5. Under **Static website hosting**, choose **Create Amplify app**. At this step, the deployment process will move to the Amplify console.
6. On the **Deploy with S3**  page, do the following steps.


	1. For **App name**, enter the name of your app or
	 website.
	2. For **Branch name**, enter the name of your app's
	 backend.
	3. For **S3 location of objects to host**, either enter
	 the directory path to your general purpose bucket or choose
	 **Browse S3** to locate and select it.
7. Choose **Save and deploy**.

###### Note

 If you update any of the objects for a static website in your general purpose bucket hosted on Amplify, you must redeploy the application to Amplify Hosting to 
 cause the changes to take effect. Amplify Hosting doesn't automatically detect changes to your bucket. For more information, see [Updating a static website deployed to Amplify from an S3 bucket](https://docs.aws.amazon.com/amplify/latest/userguide/update-website-deployed-from-s3.html "https://docs.aws.amazon.com/amplify/latest/userguide/update-website-deployed-from-s3.html") in the *AWS Amplify Hosting
 User Guide*.
 


To start directly from the Amplify console, see [Deploying a static
 website from S3 using the Amplify console](https://docs.aws.amazon.com/amplify/latest/userguide/deploy--from-amplify-console.html "https://docs.aws.amazon.com/amplify/latest/userguide/deploy--from-amplify-console.html") in the *AWS Amplify Hosting
 User Guide*.


To get started using the AWS SDKs, see [Creating a bucket policy to deploy
 a static website from S3 using the AWS SDKs](https://docs.aws.amazon.com/amplify/latest/userguide/deploy-with-sdks.html "https://docs.aws.amazon.com/amplify/latest/userguide/deploy-with-sdks.html") in the *AWS Amplify
 Hosting User Guide*.
