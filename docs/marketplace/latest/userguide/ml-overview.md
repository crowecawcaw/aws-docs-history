

# Understanding machine learning products
<a name="ml-overview"></a>

 AWS Marketplace supports two machine learning product types, using Amazon SageMaker AI. Both types, the model package products and the algorithm products, produce a deployable inference model for making predictions.

## SageMaker AI model package
<a name="ml-amazon-sagemaker-model-package"></a>

 An [ Amazon SageMaker AI model package](https://docs.aws.amazon.com/sagemaker/latest/dg/sagemaker-marketplace.html#sagemaker-mkt-model-package) product contains a pre-trained model. Pre-trained models can be deployed in SageMaker AI to make inferences or predictions in real time or in batches. This product contains a trained inference component with model artifacts, if any. As a seller, you can train a model using SageMaker AI or bring your own model. 

## SageMaker AI algorithm
<a name="ml-amazon-sagemaker-algorithm"></a>

 Buyers can use a [SageMaker AI algorithm](https://docs.aws.amazon.com/sagemaker/latest/dg/sagemaker-marketplace.html#sagemaker-mkt-algorithm) product to perform complete machine learning workloads. An algorithm product has two logical components: training and inference. In SageMaker AI, buyers use their own datasets to create a training job with your training component. When the algorithm in your training component completes, it generates the model artifacts of the machine learning model. SageMaker AI saves the model artifacts in the buyers’ Amazon Simple Storage Service (Amazon S3) bucket. In SageMaker AI, buyers can then deploy your inference component along with those generated model artifacts to perform inference (or prediction) in real time or in batches. 

## Deploying an inference model
<a name="ml-deploying-an-inference-model"></a>

 Whether the inference model is created from a model package or an algorithm, there are two methods to deploy them: 
+  **Endpoint** – This method uses SageMaker AI to deploy the model and create an API endpoint. The buyer can use this endpoint as part of their backend service to power their applications. When data is sent to the endpoint, SageMaker AI passes it to the model container and returns the results in an API response. The endpoint and the container continue to run until stopped by the buyer.
**Note**  
 In AWS Marketplace, the endpoint method is referred to as *real-time inference*, and in the SageMaker AI documentation, it is referred to as *hosting services*. For more information, see [Deploy a Model in Amazon SageMaker AI](https://docs.aws.amazon.com/sagemaker/latest/dg/how-it-works-deployment.html). 
+  **Batch transform job** – In this method, a buyer stores datasets for inference in Amazon S3. When the batch transform job starts, SageMaker AI deploys the model, passes data from an S3 bucket to the model’s container, and then returns the results to an Amazon S3 bucket. When the job completes, SageMaker AI stops the job. For more information, see [Use Batch Transform](https://docs.aws.amazon.com/sagemaker/latest/dg/batch-transform.html).
**Note**  
 Both methods are transparent to the model because SageMaker AI passes data to the model and returns results to the buyer. 