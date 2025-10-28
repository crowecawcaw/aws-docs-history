# Add models to a private hub

After creating a private hub, you can then add allow-listed models. For the full
list of available JumpStart models, see the [Built-in Algorithms with pre-trained Model Table](https://sagemaker.readthedocs.io/en/stable/doc_utils/pretrainedmodels.html "https://sagemaker.readthedocs.io/en/stable/doc_utils/pretrainedmodels.html") in the SageMaker Python SDK
reference.

1. You can filter through the available models programmatically using the
   `hub.list_sagemaker_public_hub_models()` method. You can
   optionally filter by categories such as framework (`"framework ==
pytorch"`), tasks such as image classification (`"task ==
ic"`), and more. For more information about filters, see [`notebook_utils.py`](https://github.com/aws/sagemaker-python-sdk/blob/master/src/sagemaker/jumpstart/notebook_utils.py "https://github.com/aws/sagemaker-python-sdk/blob/master/src/sagemaker/jumpstart/notebook_utils.py"). The filter parameter in the
   `hub.list_sagemaker_public_hub_models()` method is optional.

```
filter_value = `"framework == meta"`
response = hub.list_sagemaker_public_hub_models(filter=`filter_value`)
models = response["hub_content_summaries"]
while response["next_token"]:
    response = hub.list_sagemaker_public_hub_models(filter=filter_value, next_token=response["next_token"])
    models.extend(response["hub_content_summaries"])

print(models)
```

2. You can then add the filtered models by specifying the model ARN in the
   `hub.create_model_reference()` method.

```
for model in models:
    print(f"Adding {model.get('hub_content_name')} to Hub")
    hub.create_model_reference(model_arn=model.get("hub_content_arn"), model_name=model.get("hub_content_name"))
```
