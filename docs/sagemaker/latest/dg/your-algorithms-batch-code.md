# Custom Inference Code with Batch

Transform

This section explains how Amazon SageMaker AI interacts with a Docker container that runs your own
inference code for batch transform. Use this information to write inference code and create
a Docker image.

###### Topics

- [How SageMaker AI Runs Your Inference
  Image](#your-algorithms-batch-code-run-image "#your-algorithms-batch-code-run-image")
- [How SageMaker AI Loads Your Model
  Artifacts](#your-algorithms-batch-code-load-artifacts "#your-algorithms-batch-code-load-artifacts")
- [How Containers
  Serve Requests](#your-algorithms-batch-code-how-containe-serves-requests "#your-algorithms-batch-code-how-containe-serves-requests")
- [How Your Container Should Respond to Inference Requests](#your-algorithms-batch-code-how-containers-should-respond-to-inferences "#your-algorithms-batch-code-how-containers-should-respond-to-inferences")
- [How Your Container Should
  Respond to Health Check (Ping) Requests](#your-algorithms-batch-algo-ping-requests "#your-algorithms-batch-algo-ping-requests")

## How SageMaker AI Runs Your Inference

Image

To configure a container to run as an executable, use an `ENTRYPOINT`
instruction in a Dockerfile. Note the following:

- For batch transforms, SageMaker AI invokes the model on your behalf. SageMaker AI runs the
  container as:

```
docker run `image` serve
```

The input to batch transforms must be of a format that can be split into
smaller files to process in parallel. These formats include CSV, [JSON](https://www.json.org/json-en.html "https://www.json.org/json-en.html"), [JSON Lines](https://jsonlines.org/ "https://jsonlines.org/"), [TFRecord](https://www.tensorflow.org/tutorials/load_data/tfrecord "https://www.tensorflow.org/tutorials/load_data/tfrecord") and [RecordIO](https://mesos.apache.org/documentation/latest/recordio/ "https://mesos.apache.org/documentation/latest/recordio/").

SageMaker AI overrides default `CMD` statements in a container by
specifying the `serve` argument after the image name. The
`serve` argument overrides arguments that you provide with the
`CMD` command in the Dockerfile.

- We recommend that you use the `exec` form of the
  `ENTRYPOINT` instruction:

```
ENTRYPOINT ["executable", "param1", "param2"]
```

For example:

```
ENTRYPOINT ["python", "k_means_inference.py"]
```

- SageMaker AI sets environment variables specified in [`CreateModel`](../APIReference/API_CreateModel.md "../APIReference/API_CreateModel.md") and [`CreateTransformJob`](../APIReference/API_CreateTransformJob.md "../APIReference/API_CreateTransformJob.md") on your container. Additionally, the
  following environment variables are populated:
  - `SAGEMAKER_BATCH` is set to `true` when the
    container runs batch transforms.
  - `SAGEMAKER_MAX_PAYLOAD_IN_MB` is set to the largest size
    payload that is sent to the container via HTTP.
  - `SAGEMAKER_BATCH_STRATEGY` is set to
    `SINGLE_RECORD` when the container is sent a single
    record per call to invocations and `MULTI_RECORD` when the
    container gets as many records as will fit in the payload.
  - `SAGEMAKER_MAX_CONCURRENT_TRANSFORMS` is set to the maximum
    number of `/invocations` requests that can be opened
    simultaneously.

###### Note

The last three environment variables come from the API call made by the
user. If the user doesn’t set values for them, they aren't passed. In that
case, either the default values or the values requested by the algorithm (in
response to the `/execution-parameters`) are used.

- If you plan to use GPU devices for model inferences (by specifying GPU-based
  ML compute instances in your `CreateTransformJob` request), make sure
  that your containers are nvidia-docker compatible. Don't bundle NVIDIA drivers
  with the image. For more information about nvidia-docker, see [NVIDIA/nvidia-docker](https://github.com/NVIDIA/nvidia-docker "https://github.com/NVIDIA/nvidia-docker").
- You can't use the `init` initializer as your entry point in SageMaker AI
  containers because it gets confused by the train and serve arguments.

## How SageMaker AI Loads Your Model

Artifacts

In a [`CreateModel`](../APIReference/API_CreateModel.md "../APIReference/API_CreateModel.md") request, container definitions include the
`ModelDataUrl` parameter, which identifies the location in Amazon S3 where
model artifacts are stored. When you use SageMaker AI to run inferences, it uses this
information to determine from where to copy the model artifacts. It copies the artifacts
to the `/opt/ml/model` directory in the Docker container for use by
your inference code.

The `ModelDataUrl` parameter must point to a tar.gz file. Otherwise, SageMaker AI
can't download the file. If you train a model in SageMaker AI, it saves the artifacts as a
single compressed tar file in Amazon S3. If you train a model in another framework, you need
to store the model artifacts in Amazon S3 as a compressed tar file. SageMaker AI decompresses this
tar file and saves it in the `/opt/ml/model` directory in the
container before the batch transform job starts.

## How Containers

Serve Requests

Containers must implement a web server that responds to invocations and ping requests
on port 8080. For batch transforms, you have the option to set algorithms to implement
execution-parameters requests to provide a dynamic runtime configuration to SageMaker AI. SageMaker AI
uses the following endpoints:

- `ping`—Used to periodically check the health of the
  container. SageMaker AI waits for an HTTP `200` status code and an empty body
  for a successful ping request before sending an invocations request. You might
  use a ping request to load a model into memory to generate inference when
  invocations requests are sent.
- (Optional) `execution-parameters`—Allows the algorithm to
  provide the optimal tuning parameters for a job during runtime. Based on the
  memory and CPUs available for a container, the algorithm chooses the appropriate
  `MaxConcurrentTransforms`, `BatchStrategy`, and
  `MaxPayloadInMB` values for the job.

Before calling the invocations request, SageMaker AI attempts to invoke the
execution-parameters request. When you create a batch transform job, you can provide
values for the `MaxConcurrentTransforms`, `BatchStrategy`, and
`MaxPayloadInMB` parameters. SageMaker AI determines the values for these
parameters using this order of precedence:

1. The parameter values that you provide when you create the
   `CreateTransformJob` request.
2. The values that the model container returns when SageMaker AI invokes the
   execution-parameters endpoint>
3. The default parameter values, listed in the following table.

| Parameter                 | Default Values |
| ------------------------- | -------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `MaxConcurrentTransforms` | 1              |
| `BatchStrategy`           | `MULTI_RECORD` |
| `MaxPayloadInMB`          | 6              | The response for a `GET` execution-parameters request is a JSON object with keys for `MaxConcurrentTransforms`, `BatchStrategy`, and `MaxPayloadInMB` parameters. This is an example of a valid response: `{ “MaxConcurrentTransforms”: 8, “BatchStrategy": "MULTI_RECORD", "MaxPayloadInMB": 6 }` ## How Your Container Should Respond to Inference Requests To obtain inferences, Amazon SageMaker AI sends a POST request to the inference container. The POST request body contains data from Amazon S3. Amazon SageMaker AI passes the request to the container, and returns the inference result from the container, saving the data from the response to Amazon S3. To receive inference requests, the container must have a web server listening on port 8080 and must accept POST requests to the `/invocations` endpoint. The inference request timeout and max retries can be configured through `ModelClientConfig`. ## How Your Container Should Respond to Health Check (Ping) Requests The simplest requirement on the container is to respond with an HTTP 200 status code and an empty body. This indicates to SageMaker AI that the container is ready to accept inference requests at the `/invocations` endpoint. While the minimum bar is for the container to return a static 200, a container developer can use this functionality to perform deeper checks. The request timeout on `/ping` attempts is 2 seconds. |
