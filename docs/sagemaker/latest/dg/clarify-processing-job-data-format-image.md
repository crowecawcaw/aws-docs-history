# Image data requirements

A SageMaker Clarify processing job provides support for explaining images. This topic provides the
data format requirements for image data. For information about processing the image data, see [computer vision](clarify-processing-job-run.md#clarify-processing-job-run-cv "clarify-processing-job-run.md#clarify-processing-job-run-cv").

An image dataset contains one or more image files. To identify an input dataset to
the SageMaker Clarify processing job, set either a [ProcessingInput](../APIReference/API_CreateProcessingJob.md#sagemaker-CreateProcessingJob-request-ProcessingInputs "../APIReference/API_CreateProcessingJob.md#sagemaker-CreateProcessingJob-request-ProcessingInputs") named `dataset` or the analysis
configuration `dataset_uri` parameter to an Amazon S3 URI prefix of your image
files.

The supported image file formats and file extensions are listed in the following
table.

| Image format | File extension |
| ------------ | -------------- |
| JPEG         | jpg, jpeg      |
| PNG          | png            |

Set the analysis configuration `dataset_type` parameter to
`application/x-image`. Because the type is not a specific
image file format, the `content_type` will be used to decide the image
file format and extension.

The SageMaker Clarify processing job loads each image file to a 3-dimensional [NumPy
array](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html "https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html") for further processing. The three dimensions include height,
width, and RGB values of each pixel.

The SageMaker Clarify processing job converts the raw RGB data of an image into a compatible
image format, such as JPEG. It does this before it sends the data to the endpoint
for predictions. The supported image formats are as follows.

| Data Format | MIME type           | File extension |
| ----------- | ------------------- | -------------- |
| JPEG        | `image/jpeg`        | jpg, jpeg      |
| PNG         | `image/png`         | png            |
| NPY         | `application/x-npy` | All above      |

Specify the data format of the request payload by using the analysis configuration
parameter `content_type`. If the `content_type` is not
provided, the data format defaults to `image/jpeg`.

Upon receiving the response of an inference endpoint invocation, the SageMaker Clarify
processing job deserializes response payload and then extracts the predictions from
it.

### Image

classification problem

The data format of the response payload should be specified by the analysis
configuration parameter accept_type. If `accept_type` is not
provided, the data format defaults to `application/json`. The
supported formats are the same as those described in the **Endpoint response for tabular data** in the tabular data
section.

See [Inference with the Image Classification
Algorithm](image-classification.md#IC-inference "image-classification.md#IC-inference") for an example
of a SageMaker AI built-in image classification algorithm that accepts a single image
and then returns an array of probability values (scores), each for a
class.

As shown in the following table, when the `content_type` parameter
is set to `application/jsonlines`, the response is a JSON
object.

| Endpoint request payload | Endpoint response payload (string representation) |
| ------------------------ | ------------------------------------------------- |
| Single image             | '{"prediction":[0.1,0.6,0.3]}'                    |

In the previous example, set the `probability` parameter to
JMESPath expression "prediction" to extract the scores.

When the `content_type` is set to `application/json`,
the response is a JSON object, as shown in the following table.

| Endpoint request payload | Endpoint response payload (string representation) |
| ------------------------ | ------------------------------------------------- |
| Single image             | '[0.1,0.6,0.3]'                                   |

In the previous example, set `probability` to JMESPath expression
"[\*]" to extract all the elements of the array. In the previous example,
[`0.1, 0.6, 0.3]`is extracted. Alternatively, if you skip
 setting the`probability` configuration parameter, then all the
elements of the array are also extracted. This is because the entire payload is
deserialized as the predictions.

### Object detection problem

The analysis configuration `accept_type` defaults to
`application/json` and the only supported format is the Object
Detection Inference Format. For more information about response formats, see
[Response Formats](object-detection-in-formats.md#object-detection-recordio "object-detection-in-formats.md#object-detection-recordio").

The following table is an example response from an endpoint that outputs an
array. Each element of the array is an array of values containing the class
index, the confidence score, and the bounding box coordinates of the detected
object.

| Endpoint request payload   | Endpoint response payload (string representation)                                                                                                                                                                                      |
| -------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Single image (one object)  | '[[4.0, 0.86419455409049988, 0.3088374733924866,<br>0.07030484080314636, 0.7110607028007507,<br>0.9345266819000244]]'                                                                                                                  |
| Single image (two objects) | '[[4.0, 0.86419455409049988, 0.3088374733924866,<br>0.07030484080314636, 0.7110607028007507,<br>0.9345266819000244],[0.0, 0.73376623392105103,<br>0.5714187026023865, 0.40427327156066895, 0.827075183391571,<br>0.9712159633636475]]' |

The following table is an example response from an endpoint that outputs a
JSON object with a key referring to the array. Set the analysis configuration
`probability` to the key "prediction" to extract the
values.

| Endpoint request payload   | Endpoint response payload (string representation)                                                                                                                                                                                                     |
| -------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Single image (one object)  | '{"prediction":[[4.0, 0.86419455409049988,<br>0.3088374733924866, 0.07030484080314636, 0.7110607028007507,<br>0.9345266819000244]]}'                                                                                                                  |
| Single image (two objects) | '{"prediction":[[4.0, 0.86419455409049988,<br>0.3088374733924866, 0.07030484080314636, 0.7110607028007507,<br>0.9345266819000244],[0.0, 0.73376623392105103,<br>0.5714187026023865, 0.40427327156066895, 0.827075183391571,<br>0.9712159633636475]]}' |

## Pre-check

endpoint request and response for image data

We recommend that you deploy your model to a SageMaker AI real-time inference endpoint,
and send requests to the endpoint. Manually examine the requests and responses. Make
sure that both are compliant with the requirements in the **Endpoint request for image data** section and **Endpoint response for image data** section.

The following are two code examples showing how to send requests and examine the
responses for both image classification and object detection problems.

### Image

classification problem

The following example code instructs an endpoint to read a PNG file and then
classifies it.

```
aws sagemaker-runtime invoke-endpoint \
  --endpoint-name test-endpoint-sagemaker-image-classification \
  --content-type "image/png" \
  --accept "application/json" \
  --body fileb://./test.png  \
  /dev/stderr 1>/dev/null
```

From the previous code example, the response output follows.

```
[0.1,0.6,0.3]
```

### Object detection problem

The following example code instructs an endpoint to read a JPEG file and then
detects the objects in it.

```
aws sagemaker-runtime invoke-endpoint \
  --endpoint-name test-endpoint-sagemaker-object-detection \
  --content-type "image/jpg" \
  --accept "application/json" \
  --body fileb://./test.jpg  \
  /dev/stderr 1>/dev/null
```

From the previous code example, the response output follows.

```
{"prediction":[[4.0, 0.86419455409049988, 0.3088374733924866, 0.07030484080314636, 0.7110607028007507, 0.9345266819000244],[0.0, 0.73376623392105103, 0.5714187026023865, 0.40427327156066895, 0.827075183391571, 0.9712159633636475],[4.0, 0.32643985450267792, 0.3677481412887573, 0.034883320331573486, 0.6318609714508057, 0.5967587828636169],[8.0, 0.22552496790885925, 0.6152569651603699, 0.5722782611846924, 0.882301390171051, 0.8985623121261597],[3.0, 0.42260299175977707, 0.019305512309074402, 0.08386176824569702, 0.39093565940856934, 0.9574796557426453]]}
```
