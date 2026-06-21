The AWS Marketplace API Reference was restructured. For more information about the supported API operations, see the [AWS Marketplace API Reference](../APIReference/Welcome.md "../APIReference/Welcome.md").

# Prerequisites for publishing ML product listings

Ensure that you have the following before getting started with publishing your machine learning product listing:

- Registration as a seller in AWS Marketplace. For more information, refer to [Register as an AWS Marketplace seller](../userguide/seller-registration-process.md "../userguide/seller-registration-process.md").
- An IAM user with `AWSMarketplaceSellerFullAccess` permission.
- A publicly accessible Amazon Simple Storage Service (Amazon S3) bucket to
  host your company logo and EULA, if you provide one. You enter the URL for the
  S3 bucket in your `ChangeSet` JSON file.
- A valid SageMaker AI ARN of the model package or algorithm resource you want to list.
- A valid IAM role that has a trust relationship with the AWS Marketplace service
  principal and provides access to your package. For more information about the
  role, refer to _IAM role for the AWS Marketplace service
  principal_ in the [Prerequisites](../userguide/ml-publishing-prereq.md "../userguide/ml-publishing-prereq.md") page for machine learning products.
