

# Online explainability with SageMaker Clarify
<a name="clarify-online-explainability"></a>

This guide shows how to configure online explainability with SageMaker Clarify. With SageMaker AI [real-time inference](https://docs.aws.amazon.com/sagemaker/latest/dg/realtime-endpoints.html) endpoints, you can analyze explainability in real time, continuously. The online explainability function fits into the **Deploy to production** part of the[ Amazon SageMaker AI Machine Learning workflow](https://docs.aws.amazon.com/sagemaker/latest/dg/how-it-works-mlconcepts.html).

## How Clarify Online Explainability Works
<a name="clarify-online-explainability-how-it-works"></a>

The following graphic depicts SageMaker AI architecture for hosting an endpoint that serves explainability requests. It depicts interactions between an endpoint, the model container, and the SageMaker Clarify explainer.

![SageMaker AI architecture showing hosting an endpoint that serves on-demand explainability requests.](http://docs.aws.amazon.com/sagemaker/latest/dg/images/clarify/DeveloperGuideArchitecture.png)


Here's how Clarify online explainability works. The application sends a REST-style `InvokeEndpoint` request to the SageMaker AI Runtime Service. The service routes this request to a SageMaker AI endpoint to obtain predictions and explanations. Then, the service receives the response from the endpoint. Lastly, the service sends the response back to the application.

To increase the endpoint availability, SageMaker AI automatically attempts to distribute endpoint instances in multiple Availability Zones, according to the instance count in the endpoint configuration. On an endpoint instance, upon a new explainability request, the SageMaker Clarify explainer calls the model container for predictions. Then it computes and returns the feature attributions.

Here are the four steps to create an endpoint that uses SageMaker Clarify online explainability:

1. Check if your pre-trained SageMaker AI model is compatible with online explainability by following the [pre-check](https://docs.aws.amazon.com/sagemaker/latest/dg/clarify-online-explainability-precheck.html) steps.

1. [Create an endpoint configuration](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_CreateEndpointConfig.html) with the SageMaker Clarify explainer configuration using the `CreateEndpointConfig` API.

1. [Create an endpoint](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_CreateEndpoint.html) and provide the endpoint configuration to SageMaker AI using the `CreateEndpoint` API. The service launches the ML compute instance and deploys the model as specified in the configuration.

1. [Invoke the endpoint](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_runtime_InvokeEndpoint.html): After the endpoint is in service, call the SageMaker AI Runtime API `InvokeEndpoint` to send requests to the endpoint. The endpoint then returns explanations and predictions.