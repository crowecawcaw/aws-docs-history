# Update a multi-container endpoint

To update an Amazon SageMaker AI multi-container endpoint, complete the following steps.

1. Call [create_model](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sagemaker.html#SageMaker.Client.create_model "https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sagemaker.html#SageMaker.Client.create_model") to create a new model with a new value for the
   `Mode` parameter in the `InferenceExecutionConfig`
   field.
2. Call [create_endpoint_config](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sagemaker.html#SageMaker.Client.create_endpoint_config "https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sagemaker.html#SageMaker.Client.create_endpoint_config") to create a new endpoint config with a
   different name by using the new model you created in the previous step.
3. Call [update_endpoint](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sagemaker.html#SageMaker.Client.update_endpoint "https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sagemaker.html#SageMaker.Client.update_endpoint") to update the endpoint with the new endpoint config
   you created in the previous step.
