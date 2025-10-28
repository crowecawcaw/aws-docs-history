# Security and intellectual

property with Amazon SageMaker AI

Amazon SageMaker AI protects both your intellectual property and buyer data for models and
algorithms obtained from AWS Marketplace. The following sections provide more information about
the ways that SageMaker AI protects intellectual property and the security of customer data.

###### Topics

- [Protecting intellectual property](#ml-protecting-intellectual-property "#ml-protecting-intellectual-property")
- [No network access](#ml-no-network-access "#ml-no-network-access")
- [Security of customer data](#ml-security-of-customer-data "#ml-security-of-customer-data")

##

Protecting intellectual property

When you create a product, the code is packaged in Docker
container images. For more information, see
[Preparing your product in SageMaker AI](ml-prepare-your-product-in-sagemaker.md "ml-prepare-your-product-in-sagemaker.md"),
later in this guide. When you
upload a container image, the image and artifacts are encrypted
in transit and at rest. The images are also scanned for
vulnerabilities before being published.

To help safeguard your intellectual property, SageMaker AI allows only buyers to access
your product through AWS service endpoints. Buyers cannot directly access or pull
container images or model artifacts, nor can they access the underlying infrastructure.

## No network access

Unlike SageMaker AI models and algorithms that buyers create, when buyers launch your
product from AWS Marketplace, the models and algorithms are deployed without network access. SageMaker AI
deploys images in an environment with no access to the network or AWS service
endpoints. For example, a container image can't make outbound API calls to services on
the internet, [VPC endpoints](../../../vpc/latest/userguide/vpc-endpoints.md "../../../vpc/latest/userguide/vpc-endpoints.md"), or any other AWS services.

##

Security of customer data

Your product runs in SageMaker AI within the buyer’s AWS account. So, when a buyer uses
your product to perform data inference, you as the seller can't access their data.

For algorithm products, model artifacts are outputted by your training image
after each training job. Model artifacts are stored in the buyer’s account. The model
artifacts from the training job are used when the buyer deploys the model with your
inference image. To protect any intellectual property that may be contained in the model
artifact, encrypt them before outputting them.

###### Important

This security model prevents your code from accessing the internet during
runtime. Therefore, your code can't use resources or libraries from the internet, so
package your dependencies in the Docker container image. This is especially
important if you choose to encrypt your outputted artifacts from the training job.
The keys to encrypt and decrypt artifacts can't be accessed over the internet at
runtime. They must be packaged with your image.

For more information, see
[Security
in Amazon SageMaker AI](../../../sagemaker/latest/dg/security.md "../../../sagemaker/latest/dg/security.md").
