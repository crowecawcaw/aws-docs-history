#

Understanding machine learning products

AWS Marketplace supports two machine learning product types, using Amazon SageMaker AI. Both types, the model
package products and the algorithm products, produce a deployable inference model for making
predictions.

## SageMaker AI model package

An [Amazon SageMaker AI model package](../../../sagemaker/latest/dg/sagemaker-marketplace.md#sagemaker-mkt-model-package "../../../sagemaker/latest/dg/sagemaker-marketplace.md#sagemaker-mkt-model-package") product contains a pre-trained model. Pre-trained
models can be deployed in SageMaker AI to make inferences or predictions in real time or in
batches. This product contains a trained inference component with model artifacts, if
any. As a seller, you can train a model using SageMaker AI or bring your own model.

## SageMaker AI algorithm

Buyers can use a [SageMaker AI
algorithm](../../../sagemaker/latest/dg/sagemaker-marketplace.md#sagemaker-mkt-algorithm "../../../sagemaker/latest/dg/sagemaker-marketplace.md#sagemaker-mkt-algorithm") product to perform complete machine learning workloads. An
algorithm product has two logical components: training and inference. In SageMaker AI, buyers
use their own datasets to create a training job with your training component. When the
algorithm in your training component completes, it generates the model artifacts of the
machine learning model. SageMaker AI saves the model artifacts in the buyers’ Amazon Simple Storage Service (Amazon S3)
bucket. In SageMaker AI, buyers can then deploy your inference component along with those
generated model artifacts to perform inference (or prediction) in real time or in
batches.

## Deploying an inference model

Whether the inference model is created from a model package or
an algorithm, there are two methods to deploy them:

- **Endpoint** – This method uses SageMaker AI to
  deploy the model and create an API endpoint. The buyer can use this endpoint as
  part of their backend service to power their applications. When data is sent to
  the endpoint, SageMaker AI passes it to the model container and returns the results in
  an API response. The endpoint and the container continue to run until stopped by
  the buyer.

###### Note

In AWS Marketplace, the endpoint method is referred to as _real-time inference_, and in the SageMaker AI documentation, it is
referred to as _hosting services_. For more
information, see [Deploy a Model in
Amazon SageMaker AI](../../../sagemaker/latest/dg/how-it-works-deployment.md "../../../sagemaker/latest/dg/how-it-works-deployment.md").

- **Batch transform job** – In this method,
  a buyer stores datasets for inference in Amazon S3. When the batch transform job
  starts, SageMaker AI deploys the model, passes data from an S3 bucket to the model’s
  container, and then returns the results to an Amazon S3 bucket. When the job completes,
  SageMaker AI stops the job. For more information, see [Use Batch
  Transform](../../../sagemaker/latest/dg/batch-transform.md "../../../sagemaker/latest/dg/batch-transform.md").

###### Note

Both methods are transparent to the model because SageMaker AI
passes data to the model and returns results to the buyer.
