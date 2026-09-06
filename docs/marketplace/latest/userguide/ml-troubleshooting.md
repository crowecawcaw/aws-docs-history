

# Troubleshooting issues with machine learning products
<a name="ml-troubleshooting"></a>

 This section provides help for some common errors that you might encounter during the publishing process for your machine learning product. If your issue isn't listed, contact the [AWS Marketplace Seller Operations](https://aws.amazon.com/marketplace/management/contact-us/) team. 

## General: I get a 400 error when I add the Amazon Resource Name (ARN) of my model package or algorithm in the AWS Marketplace Management Portal
<a name="troubleshooting_error_code_400"></a>

### Common cause
<a name="troubleshooting_common_cause"></a>

 When creating your machine learning product in SageMaker AI, you didn't choose to publish your product in AWS Marketplace. 

### Resolution
<a name="troubleshooting_resolution"></a>

 If you used the Amazon SageMaker AI console to create your resource, you must choose **Yes** on the final page of the process for **Publish this model package in AWS Marketplace** or **Yes** for **Publish this algorithm in AWS Marketplace**. You can't choose **No** and later publish it. Selecting **Yes** doesn't publish the model package or algorithm. However, it validates your model package or algorithm resource when it is created, which is necessary for use in AWS Marketplace.

 If you're using the AWS SDK to [create a model package](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_CreateModelPackage.html#sagemaker-CreateModelPackage-request-CertifyForMarketplace) or [ create an algorithm](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_CreateAlgorithm.html#sagemaker-CreateAlgorithm-request-CertifyForMarketplace), ensure that the parameter `CertifyForMarketplace` is set to `true`. 

After you re-create your certified and validated model package or algorithm resource, add the new ARN in the AWS Marketplace Management Portal. 

## General: I get a 404 error when I add the ARN of my model package or algorithm in the AWS Marketplace Management Portal
<a name="troubleshooting_error_code_404"></a>

### Common cause
<a name="troubleshooting_common_cause"></a>

 This error can happen for several reasons: 
+  The ARN might be invalid. 
+  The model package or algorithm resource wasn't created in the same AWS account as the seller account. 
+  The user or role that you use for publishing doesn't have the correct IAM permissions to access the model package or algorithm resource. 

### Resolution
<a name="troubleshooting_resolution"></a>

1.  Check the ARN to ensure it is the correct ARN and is in the expected format: 

    For model packages, the ARNs should look similar to `arn:aws:sagemaker:us-east-2:000123456789:model-package/my-model-package-name`. 

    For algorithms, the ARNs should look similar to `arn:aws:sagemaker:us-east-2:000123456789:algorithm/my-algorithm`. 

1.  Ensure that all resources and assets for publishing are in the seller account that you are publishing from. 

1.  Ensure that your user or role has the following permissions: 

    For model packages, the action `sagemaker:DescribeModelPackage` on the model package resource must be allowed. 

    For algorithms, the action `sagemaker:DescribeAlgorithm` on the algorithm resource must be allowed. 

## Amazon SageMaker AI: I get a “Client error: Access denied for registry” failure message when I create a model package or algorithm resource
<a name="troubleshooting_error_sm_access_denied"></a>

### Common cause
<a name="troubleshooting_common_cause"></a>

This error can happen when the image that is being used to create the model package or algorithm is stored in an [Amazon ECR](https://aws.amazon.com/ecr/) repository that belongs to another AWS account. Model package or algorithm validation does not support cross-account images.

### Resolution
<a name="troubleshooting_resolution"></a>

Copy the image to an Amazon ECR repository owned by the AWS account that you are using to publish. Then, proceed with creating the resource using the new image location.

## Amazon SageMaker AI: I get “Not Started” and “Client error: No scan scheduled...” failure messages when I create a model package or algorithm resource
<a name="troubleshooting_error_sm_failure"></a>

### Common cause
<a name="troubleshooting_common_cause"></a>

This error can happen when SageMaker AI fails to start a scan of your Docker container image stored in Amazon ECR.

### Resolution
<a name="troubleshooting_resolution"></a>

If this happens, open the [ Amazon ECR console](https://console.aws.amazon.com/ecr/repositories?region=us-east-2), find the repository where your image was uploaded to, choose the image, and then choose **Scan**.