

# Packaging your product

Machine learning products in AWS Marketplace use Amazon SageMaker AI to create and run the machine learning logic you provide for buyers. SageMaker AI runs Docker container images that contain your logic. SageMaker AI runs these containers in a secure and scalable infrastructure. For more information, see [Security and intellectual property with Amazon SageMaker AI](ml-security-and-intellectual-property.md). The following sections provide information about how to package your code into Docker container images for SageMaker AI.

**Topics**
+ [Which type of container image do I create?](#ml-which-type-of-container-image-do-i-create)
+ [Creating model package images](ml-model-package-images.md)
+ [Reporting usage for inference pricing](ml-inference-metering.md)
+ [Creating algorithm images](ml-algorithm-images.md)

## Which type of container image do I create?
<a name="ml-which-type-of-container-image-do-i-create"></a>

 The two types of container images are an inference image and a training image. 

 To create a model package product, you need only an inference image. For detailed instructions, see [Creating model package images](ml-model-package-images.md). 

 To create an algorithm product, you need both training and inference images. For detailed instructions, see [Creating algorithm images](ml-algorithm-images.md). 

 To package code properly into a container image, the container must adhere to the SageMaker AI file structure. The container must expose the correct endpoints to ensure that the service can pass data to and from your container. The following sections explain the details of this process. 

**Important**  
 For security purposes, when a buyer subscribes to your containerized product, the Docker containers run in an isolated environment without an internet connection. When you create your containers, don't rely on outgoing calls over the internet because they will fail. Calls to AWS services will also fail. For more information, see the [Security and intellectual property with Amazon SageMaker AI](ml-security-and-intellectual-property.md) section. 

 Optionally, when creating your inference and training images, use a container from [Available Deep Learning Containers Images](https://docs.aws.amazon.com/deep-learning-containers/latest/devguide/deep-learning-containers-images.html) in the *AWS Deep Learning Containers Developer Guide* as a starting point. The images are already properly packaged with different machine learning frameworks. 