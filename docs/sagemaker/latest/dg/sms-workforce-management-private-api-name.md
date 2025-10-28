# Find your workforce name

Some of the SageMaker AI workforce-related API operations require your workforce name as input.
You can see your Amazon Cognito or OIDC IdP private and vendor workforce names in an AWS Region
using the `ListWorkforces` API operation in that AWS Region.
If you created your workforce using your own OIDC IdP, you can find your workforce name
in the Ground Truth area of the SageMaker AI console.

###### To find your workforce name in the SageMaker AI console

1. Go to the Ground Truth area of the SageMaker AI console: [https://console.aws.amazon.com/sagemaker/groundtruth](https://console.aws.amazon.com/sagemaker/groundtruth "https://console.aws.amazon.com/sagemaker/groundtruth").
2. Select **Labeling workforces**.
3. Select **Private**.
4. In the **Private workforce summary** section, locate your
   workforce ARN. Your workforce name is located at the end of this ARN. For example,
   if the ARN is
   `arn:aws:sagemaker:us-east-2:111122223333:workforce/example-workforce`,
   the workforce name is `example-workforce`.
