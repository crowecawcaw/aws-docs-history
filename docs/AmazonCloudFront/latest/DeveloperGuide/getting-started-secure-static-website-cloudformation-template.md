# Get started with a secure static website

You can get started with Amazon CloudFront by using the solution described in this topic to create
a secure static website for your domain name. A _static
website_ uses only static files—like HTML, CSS, JavaScript, images, and videos—and
doesn’t need servers or server-side processing. With this solution, your website gets the
following benefits:

- **Uses the durable storage of [Amazon Simple Storage Service
  (Amazon S3)](../../../AmazonS3/latest/dev/Welcome.md "../../../AmazonS3/latest/dev/Welcome.md")** – This solution creates an Amazon S3 bucket to host your
  static website’s content. To update your website, just upload your new files to the
  S3 bucket.
- **Is sped up by the Amazon CloudFront content delivery
  network** – This solution creates a CloudFront distribution to serve
  your website to viewers with low latency. The distribution is configured with [origin access control](private-content-restricting-access-to-s3.md "private-content-restricting-access-to-s3.md")
  (OAC) to make sure that the website is accessible only through CloudFront, not directly
  from S3.
- **Is secured by HTTPS and security headers** –
  This solution creates an SSL/TLS certificate in [AWS Certificate Manager
  (ACM)](../../../acm/latest/userguide/acm-overview.md "../../../acm/latest/userguide/acm-overview.md"), and attaches it to the CloudFront distribution. This certificate
  enables the distribution to serve your domain’s website securely with HTTPS.
- **Is configured and deployed with [AWS CloudFormation](../../../AWSCloudFormation/latest/UserGuide/Welcome.md "../../../AWSCloudFormation/latest/UserGuide/Welcome.md")** – This solution uses an CloudFormation template to set
  up all the components, so you can focus more on your website’s content and less on
  configuring components.
  This solution is open source on GitHub. To view the code, submit a pull request, or open
  an issue, go to [https://github.com/aws-samples/amazon-cloudfront-secure-static-site](https://github.com/aws-samples/amazon-cloudfront-secure-static-site "https://github.com/aws-samples/amazon-cloudfront-secure-static-site").

###### Topics

- [Solution overview](#cloudformation-website-overview "#cloudformation-website-overview")
- [Deploy the solution](#deploy-secure-static-website-cloudformation "#deploy-secure-static-website-cloudformation")

## Solution overview

The following diagram shows an overview of how this static
website solution works:

![Overview diagram of a secure static website with CloudFront](images/cloudfront-secure-static-website-overview-github.png)

1. The viewer requests the website at www.example.com.
2. If the requested object is cached, CloudFront returns the object from its cache to
   the viewer.
3. If the object is not in the CloudFront cache, CloudFront requests the object from the
   origin (an S3 bucket).
4. S3 returns the object to CloudFront.
5. CloudFront caches the object.
6. The objects is returned to the viewer. Subsequent requests for the object that
   come to the same CloudFront edge location are served from the CloudFront cache.

## Deploy the solution

To deploy this secure static website solution, you can choose from either of the
following options:

- Use the CloudFormation console to deploy the solution with default content, then upload
  your website content to Amazon S3.
- Clone the solution to your computer to add your website content. Then, deploy
  the solution with the AWS Command Line Interface
  (AWS CLI).

###### Note

You must use the US East (N. Virginia) Region to deploy the CloudFormation template.

###### Topics

- [Prerequisites](#deploy-website-cloudformation-prerequisites "#deploy-website-cloudformation-prerequisites")
- [Use the CloudFormation console](#deploy-website-cloudformation-console "#deploy-website-cloudformation-console")
- [Clone the solution locally](#deploy-website-cloudformation-clone "#deploy-website-cloudformation-clone")
- [Finding access logs](#deploy-website-cloudformation-logs "#deploy-website-cloudformation-logs")

### Prerequisites

To use this solution, you must have the following prerequisites:

- A registered domain name, such as example.com, that’s pointed to an
  Amazon Route 53 hosted zone. The hosted zone must be in the same AWS account
  where you deploy this solution. If you don’t have a registered domain name,
  you can [register one with Route 53](../../../Route53/latest/DeveloperGuide/registrar.md "../../../Route53/latest/DeveloperGuide/registrar.md"). If you have a
  registered domain name but it’s not pointed to a Route 53 hosted zone, [configure Route 53 as your DNS service](../../../Route53/latest/DeveloperGuide/dns-configuring.md "../../../Route53/latest/DeveloperGuide/dns-configuring.md").
- AWS Identity and Access Management (IAM) permissions to launch CloudFormation templates that create
  IAM roles, and permissions to create all the AWS resources in the
  solution. For more information, see [Controlling access with AWS Identity and Access Management](../../../AWSCloudFormation/latest/UserGuide/using-iam-template.md "../../../AWSCloudFormation/latest/UserGuide/using-iam-template.md") in the
  _AWS CloudFormation User Guide_.

You are responsible for the costs incurred while using this solution. For more
information about costs, see [the pricing pages
for each AWS service](https://aws.amazon.com/pricing/ "https://aws.amazon.com/pricing/").

### Use the CloudFormation console

###### To deploy using the CloudFormation console

1. [Launch this solution in the CloudFormation console](https://console.aws.amazon.com/cloudformation/home?region=us-east-1#/stacks/new?stackName=amazon-cloudfront-secure-static-site-templates-main&templateURL=https://s3.amazonaws.com/solution-builders-us-east-1/amazon-cloudfront-secure-static-site/latest/main.yaml "https://console.aws.amazon.com/cloudformation/home?region=us-east-1#/stacks/new?stackName=amazon-cloudfront-secure-static-site-templates-main&templateURL=https://s3.amazonaws.com/solution-builders-us-east-1/amazon-cloudfront-secure-static-site/latest/main.yaml"). If necessary, sign in to your AWS account.
2. The **Create stack** wizard opens in the CloudFormation
   console, with prepopulated fields that specify this solution’s CloudFormation
   template.

At the bottom of the page, choose **Next**. 3. On the **Specify stack details** page, enter values for
the following fields:

    * **SubDomain** – Enter the subdomain to use
     for your website. For example, if the subdomain is *www*, your website is available at
     `www.example.com.` (Replace example.com
     with your domain name, as explained in the following bullet.)
    * **DomainName** – Enter your domain name,
     such as `example.com`. This domain must be
     pointed to a Route 53 hosted zone.
    * **HostedZoneId** – The Route 53
     hosted zone ID of your domain name.
    * **CreateApex** – (Optional)
     Create an alias to the domain apex (example.com) in your CloudFront
     configuration.

4. When finished, choose **Next**.
5. (Optional) On the **Configure stack options** page,
   [add tags and other stack options](../../../AWSCloudFormation/latest/UserGuide/cfn-console-add-tags.md "../../../AWSCloudFormation/latest/UserGuide/cfn-console-add-tags.md").
6. When finished, choose **Next**.
7. On the **Review** page, scroll to the bottom of the page,
   then select the two boxes in the **Capabilities** section.
   These capabilities allow CloudFormation to create an IAM role that allows
   access to the stack’s resources, and to name the resources
   dynamically.
8. Choose **Create stack**.
9. Wait for the stack to finish creating. The stack creates some nested
   stacks, and can take several minutes to finish. When it’s finished, the
   **Status** changes to
   **CREATE_COMPLETE**.

When the status is **CREATE_COMPLETE**, go to
https://`www.example.com` to view your website
(replace www.example.com with the subdomain and domain name that you
specified in step 3). You should see the website’s default content:

![This solution’s static website default content. It says: “I am a static website!”](images/cloudfront-secure-static-website-content.png)

###### To replace the website’s default content with your own

1. Open the Amazon S3 console at
   [https://console.aws.amazon.com/s3/](https://console.aws.amazon.com/s3/ "https://console.aws.amazon.com/s3/").
2. Choose the bucket whose name begins with
   **amazon-cloudfront-secure-static-site-s3bucketroot-**.

###### Note

Make sure to choose the bucket with **s3bucketroot**
in its name, not **s3bucketlogs**. The bucket with
**s3bucketroot** in its name contains the website
content. The one with **s3bucketlogs** contains only
log files. 3. Delete the website’s default content, then upload your own.

###### Note

If you viewed your website with this solution’s default content, then
it’s likely that some of the default content is cached in a CloudFront edge
location. To make sure that viewers see your updated website content,
_invalidate_ the files to remove the
cached copies from CloudFront edge locations. For more information, see [Invalidate files to remove content](Invalidation.md "Invalidation.md").

### Clone the solution locally

**Prerequisites**

To add your website content before deploying this solution, you must package the
solution’s artifacts locally, which requires Node.js and npm. For more information,
see [https://www.npmjs.com/get-npm](https://www.npmjs.com/get-npm "https://www.npmjs.com/get-npm").

###### To add your website content and deploy the solution

1. Clone or download the solution from [https://github.com/aws-samples/amazon-cloudfront-secure-static-site](https://github.com/aws-samples/amazon-cloudfront-secure-static-site "https://github.com/aws-samples/amazon-cloudfront-secure-static-site").
   After you clone or download it, open a command prompt or terminal and
   navigate to the `amazon-cloudfront-secure-static-site`
   folder.
2. Run the following command to install and package the solution’s
   artifacts:

```
make package-static
```

3. Copy your website’s content into the `www` folder,
   overwriting the default website content.
4. Run the following AWS CLI command to create an Amazon S3 bucket to store the
   solution’s artifacts. Replace
   `amzn-s3-demo-bucket-for-artifacts` with your own bucket
   name.

```
aws s3 mb s3://`amzn-s3-demo-bucket-for-artifacts` --region us-east-1
```

5. Run the following AWS CLI command to package the solution’s artifacts as a
   CloudFormation template. Replace
   `amzn-s3-demo-bucket-for-artifacts` with the name of
   the bucket that you created in the previous step.

```
aws cloudformation package \
    --region us-east-1 \
    --template-file templates/main.yaml \
    --s3-bucket `amzn-s3-demo-bucket-for-artifacts` \
    --output-template-file packaged.template
```

6. Run the following command to deploy the solution with CloudFormation,
   replacing the following values:
   - `your-CloudFormation-stack-name` –
     Replace with a name for the CloudFormation stack.
   - `example.com` – Replace with your
     domain name. This domain must be pointed to a Route 53 hosted zone in
     the same AWS account.
   - `www` – Replace with the subdomain
     to use for your website. For example, if the subdomain is _www_, your website is available at
     www.example.com.
   - `hosted-zone-ID` – Replace with
     the Route 53 hosted zone ID of your domain name.

```
aws cloudformation deploy \
    --region us-east-1 \
    --stack-name `your-CloudFormation-stack-name` \
    --template-file packaged.template \
    --capabilities CAPABILITY_NAMED_IAM CAPABILITY_AUTO_EXPAND \
    --parameter-overrides DomainName=`example.com` SubDomain=`www` HostedZoneId=`hosted-zone-ID`
```

    1. (Optional) To deploy the stack with a domain apex, run the
     following command instead.



    ```
    aws --region us-east-1 cloudformation deploy \
        --stack-name `your-CloudFormation-stack-name` \
        --template-file packaged.template \
        --capabilities CAPABILITY_NAMED_IAM CAPABILITY_AUTO_EXPAND \
        --parameter-overrides  DomainName=`example.com` SubDomain=`www` HostedZoneId=`hosted-zone-ID` CreateApex=yes
    ```

7. Wait for the CloudFormation stack to finish creating. The stack creates some
   nested stacks, and can take several minutes to finish. When it’s finished,
   the **Status** changes to
   **CREATE_COMPLETE**.

When the status changes to **CREATE_COMPLETE**, go to
https://www.example.com to view your website (replace www.example.com with
the subdomain and domain name that you specified in the previous step). You
should see your website’s content.

### Finding access logs

This solution enables [access logs](AccessLogs.md "AccessLogs.md") for the CloudFront
distribution. Complete the following steps to locate the distribution’s access
logs.

###### To locate the distribution’s access logs

1. Open the Amazon S3 console at
   [https://console.aws.amazon.com/s3/](https://console.aws.amazon.com/s3/ "https://console.aws.amazon.com/s3/").
2. Choose the bucket whose name begins with
   **amazon-cloudfront-secure-static-site-s3bucketlogs-**.

###### Note

Make sure to choose the bucket with **s3bucketlogs**
in its name, not **s3bucketroot**. The bucket with
**s3bucketlogs** in its name contains log files. The
one with **s3bucketroot** contains the website
content. 3. The folder named **cdn** contains the CloudFront access
logs.
