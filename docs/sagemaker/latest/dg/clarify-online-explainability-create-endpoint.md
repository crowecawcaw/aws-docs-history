# Configure and create an

endpoint

Create a new endpoint configuration to fit your model, and use this configuration to
create the endpoint. You can use the model container validated in the [pre-check step](clarify-online-explainability-precheck.md "clarify-online-explainability-precheck.md") to create an endpoint and enable the SageMaker Clarify online explainability
feature.

Use the `sagemaker_client` object to create an endpoint using the [CreateEndpointConfig](../APIReference/API_CreateEndpointConfig.md "../APIReference/API_CreateEndpointConfig.md") API. Set the member
`ClarifyExplainerConfig` inside the `ExplainerConfig`
parameter as follows:

```
sagemaker_client.create_endpoint_config(
    EndpointConfigName='name-of-your-endpoint-config',
    ExplainerConfig={
        'ClarifyExplainerConfig': {
            'EnableExplanations': '`true`',
            'InferenceConfig': {
                ...
            },
            'ShapConfig': {
                ...
            }
        },
    },
    ProductionVariants=[{
        'VariantName': 'AllTraffic',
        'ModelName': 'name-of-your-model',
        'InitialInstanceCount': 1,
        'InstanceType': 'ml.m5.xlarge',
    }]
     ...
)
sagemaker_client.create_endpoint(
    EndpointName='name-of-your-endpoint',
    EndpointConfigName='name-of-your-endpoint-config'
)
```

The first call to the `sagemaker_client` object creates a new endpoint
configuration with the explainability feature enabled. The second call uses the endpoint
configuration to launch the endpoint.

###### Note

You can also host multiple models in one container behind a [SageMaker AI
real-time inference multi-model endpoint](multi-model-endpoints.md "multi-model-endpoints.md") and configure online
explainability with SageMaker Clarify.
