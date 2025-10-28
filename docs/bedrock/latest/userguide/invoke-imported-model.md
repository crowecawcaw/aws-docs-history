# Invoke your imported model

The model import job can take several minutes to import your model after you send [CreateModelImportJob](../APIReference/API_CreateModelImportJob.md "../APIReference/API_CreateModelImportJob.md")
request. You can check the status of your import job in the console or by calling the
[GetModelImportJob](../APIReference/API_GetModelImportJob.md "../APIReference/API_GetModelImportJob.md") operation and checking the `Status` field in the response.
The import job is complete if the Status for the model is **Complete**.

After your imported model is available in Amazon Bedrock, you can use the model with on demand throughput by sending [InvokeModel](../APIReference/API_runtime_InvokeModel.md "../APIReference/API_runtime_InvokeModel.md") or [InvokeModelWithResponseStream](../APIReference/API_runtime_InvokeModelWithResponseStream.md "../APIReference/API_runtime_InvokeModelWithResponseStream.md") requests to make inference calls to the model. For more information,
see [Submit a single prompt with InvokeModel](inference-invoke.md "inference-invoke.md").

To interface with your imported model using the messages format, you can call the [Converse](../APIReference/API_runtime_Converse.md "../APIReference/API_runtime_Converse.md") or [ConverseStream](../APIReference/API_runtime_ConverseStream.md "../APIReference/API_runtime_ConverseStream.md") operations. For more information, see [Using the Converse
API](conversation-inference-call.md "conversation-inference-call.md").

###### Note

Converse API is not supported for Qwen2.5, Qwen2-VL, and Qwen2.5-VL models.

You'll need the model ARN to make inference calls to your newly imported model. After the
successful completion of the import job and after your imported model is active, you can get
the model ARN of your imported model in the console or by sending a [ListImportedModels](../APIReference/API_ListImportedModels.md "../APIReference/API_ListImportedModels.md") request.

To invoke your imported model, make sure to use the same inference parameters that is
mentioned for the customized foundation model you are importing. For information on the
inference parameters to use for the model you are importing, see [Inference request parameters and response fields for foundation models](model-parameters.md "model-parameters.md"). If you are using
inference parameters that do not match with the inference parameters mentioned for that
model, those parameters will be ignored.

###### Note

When providing multi modal inputs, you will need to include the appropriate placeholders for multi modal tokens in your text prompt.
For example, when sending an image input to a Qwen-VL model, the prompt should include `<|vision_start|><|image_pad|><|vision_end|>`. These notations are specific to the model’s tokenizer and can be applied using the following chat template.

```
from transformers import AutoProcessor, AutoTokenizer

if vision_model:
    processor = AutoProcessor.from_pretrained(model)
else:
    processor = AutoTokenizer.from_pretrained(model)


# Create messages
messages = [
    {
        "role": "user",
        "content": [
            {
                "type": "image",
                "image": "base64 encoded image",
            },
            {
                "type": "text",
                "text": "Describe this image.",
            },
        ],
    }
]

# Apply chat template
prompt = processor.apply_chat_template(messages, tokenize=False, add_generation_prompt=True)
"""
prompt = '''
<|im_start|>system\nYou are a helpful assistant.<|im_end|>\n
<|im_start|>user\n<|vision_start|><|image_pad|><|vision_end|>
Describe this image.<|im_end|>\n<|im_start|>assistant\n'''
"""

response = client.invoke_model(
                modelId=model_id,
                body=json.dumps({
                    'prompt': prompt,
                    'temperature': temperature,
                    'max_gen_len': max_tokens,
                    'top_p': top_p,
                    'images': ["base64 encoded image"]
                }),
                accept='application/json',
                contentType='application/json'
            )

```

When you invoke your imported model using `InvokeModel` or `InvokeModelWithStream`,
your request is served within 5 minutes or you might get `ModelNotReadyException`.
To understand the ModelNotReadyException, follow the steps in this next section for handling ModelNotreadyException.

## Handling ModelNotReadyException

Amazon Bedrock Custom Model Import optimizes the hardware utilization by removing the models that are not active. If you try to invoke
a model that has been removed, you'll get a `ModelNotReadyException`. After the model is removed and you invoke the model for the first time, Custom Model Import
starts to restore the model. The restoration time depends on the on-demand fleet size and the model size.

If your `InvokeModel` or `InvokeModelWithStream` request returns `ModelNotReadyException`,
follow the steps to handle the exception.

1. ###### Configure retries

By default, the request is automatically retried with exponential backoff. You can configure the maximum number of retries.

The following example shows how to configure the retry. Replace `${region-name}`, `${model-arn}`, and `10` with your Region, model ARN, and maximum attempts.

```
import json
import boto3
from botocore.config import Config


REGION_NAME = `${region-name}`
MODEL_ID= '`${model-arn}`'

config = Config(
    retries={
        'total_max_attempts': `10`, //customizable
        'mode': 'standard'
    }
)
message = "Hello"


session = boto3.session.Session()
br_runtime = session.client(service_name = 'bedrock-runtime',
                                 region_name=REGION_NAME,
                                 config=config)

try:
    invoke_response = br_runtime.invoke_model(modelId=MODEL_ID,
                                            body=json.dumps({'prompt': message}),
                                            accept="application/json",
                                            contentType="application/json")
    invoke_response["body"] = json.loads(invoke_response["body"].read().decode("utf-8"))
    print(json.dumps(invoke_response, indent=4))
except Exception as e:
    print(e)
    print(e.__repr__())


```

2. ###### Monitor response codes during retry attempts

Each retry attempt starts model restoration process. The restoration time depends on the availability of the on-demand fleet and the model size.
Monitor the response codes while the restoration process is going on.

If the retries are consistently failing, continue with the next steps. 3. ###### Verify model was successfully imported

You can verify if the model was successfully imported by checking the status of your import job in the console or by calling the
[GetModelImportJob](../APIReference/API_GetModelImportJob.md "../APIReference/API_GetModelImportJob.md") operation.
Check the `Status` field in the response. The import job is successful if the Status for the model is **Complete**. 4. ###### Contact Support for further investigation

Open a ticket with Support For more information, see [Creating support cases](../../../awssupport/latest/user/case-management.md "../../../awssupport/latest/user/case-management.md").

Include relevant details such as model ID and timestamps in the support ticket.
