# Autopilot model deployment and

predictions

After fine-tuning a large language model (LLM), you can deploy the model for real-time
text generation by setting up an endpoint to obtain interactive predictions.

###### Note

We recommend running real-time inference jobs on `ml.g5.12xlarge` for better
performances. Alternatively, `ml.g5.8xlarge` instances are suitable for
Falcon-7B-Instruct and MPT-7B-Instruct text generation tasks.

You can find the specifics of these instances within the [Accelerated Computing](https://aws.amazon.com/ec2/instance-types/ "https://aws.amazon.com/ec2/instance-types/") category in the selection of
instance types provided by Amazon EC2.

## Real-time text generation

You can use SageMaker APIs to manually deploy your fine-tuned model to a SageMaker AI Hosting [real-time inference
endpoint](realtime-endpoints.md "realtime-endpoints.md"), then begin making predictions by invoking the endpoint as
follows.

###### Note

Alternatively, you can chose the automatic deployment option when creating your
fine-tuning experiment in Autopilot. For information on setting up the automatic deployment
of models, see [How to enable automatic
deployment](autopilot-create-experiment-finetune-llms.md#autopilot-llms-finetuning-auto-model-deployment "autopilot-create-experiment-finetune-llms.md#autopilot-llms-finetuning-auto-model-deployment").

You can also use the SageMaker Python SDK and the `JumpStartModel` class to
perform inferences with models fine-tuned by Autopilot. This can be done by specifying a
custom location for the model's artifact in Amazon S3. For information on defining your model
as a JumpStart model and deploying your model for inference, see [Low-code deployment with the JumpStartModel class](https://sagemaker.readthedocs.io/en/stable/overview.html#deploy-a-pre-trained-model-directly-to-a-sagemaker-endpoint "https://sagemaker.readthedocs.io/en/stable/overview.html#deploy-a-pre-trained-model-directly-to-a-sagemaker-endpoint").

1. **Obtain the candidate inference container
   definitions**

You can find the `InferenceContainerDefinitions` within the
`BestCandidate` object retrieved from the response to the [DescribeAutoMLJobV2](../APIReference/API_DescribeAutoMLJobV2.md#API_DescribeAutoMLJobV2_ResponseSyntax "../APIReference/API_DescribeAutoMLJobV2.md#API_DescribeAutoMLJobV2_ResponseSyntax") API call. A container definition for inference refers to
the containerized environment designed for deploying and running your trained model to
make predictions.

The following AWS CLI command example uses the [DescribeAutoMLJobV2](../APIReference/API_DescribeAutoMLJobV2.md "../APIReference/API_DescribeAutoMLJobV2.md") API to obtain recommended container definitions for your
job name.

```
aws sagemaker describe-auto-ml-job-v2 --auto-ml-job-name `job-name` --region `region`
```

2. **Create a SageMaker AI model**

Use the container definitions from the previous step to create a SageMaker AI model by using
the [CreateModel](../APIReference/API_CreateModel.md "../APIReference/API_CreateModel.md") API. See the following AWS CLI command as an example. Use the
`CandidateName` for your model name.

```
aws sagemaker create-model --model-name '`<your-candidate-name>`' \
                    --primary-container '`<container-definition`' \
                    --execution-role-arn '`<execution-role-arn>`' --region '`<region>`
```

3. **Create an endpoint configuration**

The following AWS CLI command example uses the [CreateEndpointConfig](../APIReference/API_CreateEndpointConfig.md "../APIReference/API_CreateEndpointConfig.md") API to create an endpoint configuration.

###### Note

To prevent the endpoint creation from timing out due to a lengthy model download,
we recommend setting `ModelDataDownloadTimeoutInSeconds = 3600` and
`ContainerStartupHealthCheckTimeoutInSeconds = 3600`.

```
aws sagemaker create-endpoint-config --endpoint-config-name '`<your-endpoint-config-name>`' \
                    --production-variants '`<list-of-production-variants>`' ModelDataDownloadTimeoutInSeconds=3600 ContainerStartupHealthCheckTimeoutInSeconds=3600 \
                    --region '`<region>`'
```

4. **Create the endpoint**

The following AWS CLI example uses the [CreateEndpoint](../APIReference/API_CreateEndpoint.md "../APIReference/API_CreateEndpoint.md") API
to create the endpoint.

```
aws sagemaker create-endpoint --endpoint-name '`<your-endpoint-name>`' \
                    --endpoint-config-name '`<endpoint-config-name-you-just-created>`' \
                    --region '`<region>`'
```

Check the progress of your endpoint deployment by using the [DescribeEndpoint](../APIReference/API_DescribeEndpoint.md "../APIReference/API_DescribeEndpoint.md") API. See the following AWS CLI command as an example.

```
aws sagemaker describe-endpoint —endpoint-name '`<endpoint-name>`' —region `<region>`
```

After the `EndpointStatus` changes to `InService`, the
endpoint is ready to use for real-time inference. 5. **Invoke the endpoint**

The following command invokes the endpoint for real-time inferencing. Your prompt
needs to be encoded in bytes.

###### Note

The format of your input prompt depends on the language model. For more
information on the format of text generation prompts, see [Request format for text
generation models real-time inference](#autopilot-llms-finetuning-realtime-prompt-examples "#autopilot-llms-finetuning-realtime-prompt-examples").

```
aws sagemaker invoke-endpoint --endpoint-name '`<endpoint-name>`' \
                  --region '`<region>`' --body '`<your-promt-in-bytes>`' [--content-type] 'application/json' `<outfile>`
```

## Request format for text

generation models real-time inference

Different large language models (LLMs) may have specific software dependencies, runtime
environments, and hardware requirements influencing Autopilot's recommended container to host
the model for inference. Additionally, each model dictates the required input data format
and the expected format for predictions and outputs.

Here are example inputs for some models and recommended containers.

- For Falcon models with the recommended container
  `huggingface-pytorch-tgi-inference:2.0.1-tgi1.0.3-gpu-py39-cu118-ubuntu20.04`:

```
payload = {
    "inputs": "Large language model fine-tuning is defined as",
    "parameters": {
        "do_sample": false,
        "top_p": 0.9,
        "temperature": 0.1,
        "max_new_tokens": 128,
        "stop": ["<|endoftext|>", "</s>"]
    }
}
```

- For all other models with the recommended container
  `djl-inference:0.22.1-fastertransformer5.3.0-cu118`:

```
payload= {
    "text_inputs": "Large language model fine-tuning is defined as"
}
```
