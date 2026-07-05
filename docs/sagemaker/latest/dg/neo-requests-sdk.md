# Request Inferences from a Deployed Service (Amazon SageMaker SDK)

Use the following the code examples to request inferences from your deployed
service based on the framework you used to train your model. The code examples for the different
frameworks are similar. The main difference is that TensorFlow requires
`application/json` as the content type.

## PyTorch and MXNet

If you are using **PyTorch v1.4 or later** or **MXNet 1.7.0 or later** and you have
an Amazon SageMaker AI endpoint `InService`, you can make inference requests using the `predictor` package of the
SageMaker AI SDK for Python.

###### Note

The API varies based on the SageMaker AI SDK for Python version:

- For version 1.x, use the [`RealTimePredictor`](https://sagemaker.readthedocs.io/en/v1.72.0/api/inference/predictors.html#sagemaker.predictor.RealTimePredictor "https://sagemaker.readthedocs.io/en/v1.72.0/api/inference/predictors.html#sagemaker.predictor.RealTimePredictor") and
  [`Predict`](https://sagemaker.readthedocs.io/en/v1.72.0/api/inference/predictors.html#sagemaker.predictor.RealTimePredictor.predict "https://sagemaker.readthedocs.io/en/v1.72.0/api/inference/predictors.html#sagemaker.predictor.RealTimePredictor.predict") API.
- For version 3.x, use the
  [`Endpoint`](https://sagemaker.readthedocs.io/en/stable/api/sagemaker_serve.html "https://sagemaker.readthedocs.io/en/stable/api/sagemaker_serve.html") and
  the
  [`invoke`](https://sagemaker.readthedocs.io/en/stable/api/sagemaker_core.html "https://sagemaker.readthedocs.io/en/stable/api/sagemaker_core.html") API.

The following code example shows how to use these APIs to send an
image for inference:

```
from sagemaker.core.resources import Endpoint

endpoint_name = `'insert name of your endpoint here'`

# Read image into memory
payload = None
with open("image.jpg", 'rb') as f:
    payload = f.read()

endpoint = Endpoint(endpoint_name=endpoint_name)
inference_response = endpoint.invoke(body=payload, content_type='application/x-image')
print(inference_response.body.read().decode('utf-8'))
```

## TensorFlow

The following code example shows how to use the SageMaker Python SDK
API to send an image for inference:

```
from sagemaker.core.resources import Endpoint
from PIL import Image
import numpy as np
import json

endpoint_name = `'insert the name of your endpoint here'`

# Read image into memory
image = Image.open(input_file)
batch_size = 1
image = np.asarray(image.resize((224, 224)))
image = image / 128 - 1
image = np.concatenate([image[np.newaxis, :, :]] * batch_size)
body = json.dumps({"instances": image.tolist()})

endpoint = Endpoint(endpoint_name=endpoint_name)
inference_response = endpoint.invoke(body=body, content_type='application/json')
print(inference_response)
```
