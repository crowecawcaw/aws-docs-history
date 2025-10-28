# Request Inferences from a Deployed Service (AWS CLI)

Inference requests can be made with the [`sagemaker-runtime invoke-endpoint`](../../../cli/latest/reference/sagemaker-runtime/invoke-endpoint.md "../../../cli/latest/reference/sagemaker-runtime/invoke-endpoint.md") once you have an Amazon SageMaker AI
endpoint `InService`. You can make inference requests with the AWS Command Line Interface
(AWS CLI). The following example shows how to send an image for inference:

```
aws sagemaker-runtime invoke-endpoint --endpoint-name `'insert name of your endpoint here'` --body fileb://image.jpg --content-type=application/x-image output_file.txt
```

An `output_file.txt` with information about your inference requests is made
if the inference was successful.

For TensorFlow submit an input with `application/json` as the content type.

```
aws sagemaker-runtime invoke-endpoint --endpoint-name `'insert name of your endpoint here'` --body fileb://input.json --content-type=application/json output_file.txt
```
