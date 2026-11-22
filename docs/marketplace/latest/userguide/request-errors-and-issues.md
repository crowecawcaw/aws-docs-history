

# Troubleshooting common errors for change requests on AWS Marketplace

When you make changes to your product's information on AWS Marketplace, you might run into errors. This topic explains some common errors and provides suggestions for how to fix them.
+ **Scanning your AMI** – Several issues could happen when scanning your AMI:
  + You have not granted AWS Marketplace permissions to scan your AMI. Grant AWS Marketplace permissions to access it. Or you have granted permissions, but the permissions boundary is too restrictive. For more information, see [Giving AWS Marketplace access to your AMI](single-ami-marketplace-ami-access.md).
  + If scanning finds security issues or Common Vulnerabilities and Exposures (CVEs) in your AMI, make sure you're using the latest patches for the operating system in your image. For more information, see [AMI-based product requirements for AWS Marketplace](product-and-ami-policies.md).

  For general guidelines about building an AMI, see [Best practices for building AMIs for use with AWS Marketplace](best-practices-for-building-your-amis.md).
+ **AWS Partner Central fields** – Some fields require specific information:
  + If you are unsure about what the field is requesting, try checking the details in the console. Most fields have text descriptions above the field, and formatting requirements below the field.
  + Each invalid field shows an error message. If a request is rejected when you submit it, the page shows the error code and message. If a request fails after you submit it, choose its name on the product's **Change history** tab, and review the **Failure details**.
  +  If you're asked to provide an ARN, you will typically find it elsewhere in the console. For example, the ARN for the IAM role that you created to give AWS Marketplace access to your AMI is found on the [ Roles page](https://console.aws.amazon.com/iam/home?region=us-east-1#/roles) in the IAM console. ARNs all have a similar format. For example, an IAM role ARN is in the form *arn:aws:iam::123456789012:role/exampleRole*. 
  + Upload your logo, images, and videos from your computer, or import them from Amazon S3. Files that you import from Amazon S3 must be publicly accessible. For more information about logo formats, see [Company and product logo requirements](product-submission.md#seller-and-product-logos).

  For more information about submitting products and version change requests, see [Submitting your product for publication on AWS Marketplace](product-submission.md). 
+ **Request in Progress** – Some requests can't happen in parallel. You can only have one request to update specific information in progress for a product at a time.
  + You can't update version information when an update (to add or restrict) a version is ongoing.
  + If there is a request pending from the AWS Marketplace Seller Operations team, you can't submit any new changes.

  Your product's **Change history** tab lists its requests. To cancel a request that you didn't intend, choose its name, and then choose **Cancel request**. You can cancel a request only while its status is **Preparing**.
+ **Unexplained error** – If your submission fails with no explanation, try again. Occasionally, server load causes a submission to fail.

If you're still having problems with a change request, contact the AWS Marketplace support team on the [AWS Partner Central and Marketplace Support page](https://us-east-1.console.aws.amazon.com/partnercentral/support?region=us-east-1) in the AWS Partner Central console.