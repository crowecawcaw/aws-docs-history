

# Updating end user license agreement (EULA) for your AMI-based AWS Marketplace product
<a name="single-ami-update-eula"></a>

As an AWS Marketplace seller, you can update the end user license agreement (EULA) that will govern the use of your single Amazon Machine Image (AMI) product. Your EULA is located on the product listing page for public software listings on AWS Marketplace. You can either apply your own EULA or use the [Standard Contract for AWS Marketplace (SCMP)](standardized-license-terms.md). The following procedure shows you how to update the EULA for your single-AMI product.

For more information about the EULA, see [Using standardized contracts in AWS Marketplace](standardized-license-terms.md).

**To update a EULA**

1. Open the AWS Marketplace Management Portal at [https://us-east-1.console.aws.amazon.com/partnercentral/home](https://us-east-1.console.aws.amazon.com/partnercentral/home), and then sign in to your seller account.

1. Choose the [**Server products**](https://aws.amazon.com/marketplace/management/products/server) tab, on the **Current server product** tab, select the product that you want to modify.

1. From the **Request changes** dropdown, choose **Update end-user license agreement**.

1. You can select the [Standard Contract for AWS Marketplace (SCMP) ](https://docs.aws.amazon.com/marketplace/latest/userguide/standardized-license-terms.html) or submit your own custom EULA. For a custom EULA, you must provide the URL for your custom contract from an Amazon S3 bucket.
**Note**  
Public accessibility must be enabled on your Amazon S3 bucket.

1. Choose **Submit change request** to submit your request for review.

1. Verify that the **Requests** tab shows the **Request status** as **Under review**. When the request completes, the status becomes **Succeeded**.