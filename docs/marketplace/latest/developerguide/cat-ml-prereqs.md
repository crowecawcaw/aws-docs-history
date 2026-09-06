

The AWS Marketplace API Reference was restructured. For more information about the supported API operations, see the [AWS Marketplace API Reference](https://docs.aws.amazon.com/marketplace/latest/APIReference/Welcome.html).

# Prerequisites for publishing ML product listings
<a name="cat-ml-prereqs"></a>

Ensure that you have the following before getting started with publishing your machine learning product listing:
+ Registration as a seller in AWS Marketplace. For more information, refer to [Register as an AWS Marketplace seller](https://docs.aws.amazon.com/marketplace/latest/userguide/seller-registration-process.html).
+ An IAM user with `AWSMarketplaceSellerFullAccess` permission.
+ A publicly accessible Amazon Simple Storage Service (Amazon S3) bucket to host your company logo and EULA, if you provide one. You enter the URL for the S3 bucket in your `ChangeSet` JSON file.
+ A valid SageMaker AI ARN of the model package or algorithm resource you want to list.
+ A valid IAM role that has a trust relationship with the AWS Marketplace service principal and provides access to your package. For more information about the role, refer to *IAM role for the AWS Marketplace service principal* in the [Prerequisites](https://docs.aws.amazon.com/marketplace/latest/userguide/ml-publishing-prereq.html) page for machine learning products.