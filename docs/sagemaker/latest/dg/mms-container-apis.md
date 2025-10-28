# Custom Containers Contract for Multi-Model

Endpoints

To handle multiple models, your container must support a set of APIs that enable
Amazon SageMaker AI to communicate with the container for loading, listing, getting, and unloading
models as required. The `model_name` is used in the new set of APIs as the key
input parameter. The customer container is expected to keep track of the loaded models using
`model_name` as the mapping key. Also, the `model_name` is an opaque
identifier and is not necessarily the value of the `TargetModel` parameter passed
into the `InvokeEndpoint` API. The original `TargetModel` value in the
`InvokeEndpoint` request is passed to container in the APIs as a
`X-Amzn-SageMaker-Target-Model` header that can be used for logging
purposes.

###### Note

Multi-model endpoints for GPU backed instances are currently supported only with
SageMaker AI's [NVIDIA Triton
Inference Server container](triton.md "triton.md"). This container already implements the contract
defined below. Customers can directly use this container with their multi-model GPU
endpoints, without any additional work.

You can configure the following APIs on your containers for CPU backed multi-model
endpoints.

###### Topics

- [Load Model API](#multi-model-api-load-model "#multi-model-api-load-model")
- [List Model API](#multi-model-api-list-model "#multi-model-api-list-model")
- [Get Model API](#multi-model-api-get-model "#multi-model-api-get-model")
- [Unload Model API](#multi-model-api-unload-model "#multi-model-api-unload-model")
- [Invoke Model API](#multi-model-api-invoke-model "#multi-model-api-invoke-model")

## Load Model API

Instructs the container to load a particular model present in the `url`
field of the body into the memory of the customer container and to keep track of it with
the assigned `model_name`. After a model is loaded, the container should be
ready to serve inference requests using this `model_name`.

```
POST /models HTTP/1.1
Content-Type: application/json
Accept: application/json

{
     "model_name" : "{model_name}",
     "url" : "/opt/ml/models/{model_name}/model",
}
```

###### Note

If `model_name` is already loaded, this API should return 409. Any time a
model cannot be loaded due to lack of memory or to any other resource, this API should
return a 507 HTTP status code to SageMaker AI, which then initiates unloading unused models to
reclaim.

## List Model API

Returns the list of models loaded into the memory of the customer container.

```
GET /models HTTP/1.1
Accept: application/json

Response =
{
    "models": [
        {
             "modelName" : "{model_name}",
             "modelUrl" : "/opt/ml/models/{model_name}/model",
        },
        {
            "modelName" : "{model_name}",
            "modelUrl" : "/opt/ml/models/{model_name}/model",
        },
        ....
    ]
}
```

This API also supports pagination.

```
GET /models HTTP/1.1
Accept: application/json

Response =
{
    "models": [
        {
             "modelName" : "{model_name}",
             "modelUrl" : "/opt/ml/models/{model_name}/model",
        },
        {
            "modelName" : "{model_name}",
            "modelUrl" : "/opt/ml/models/{model_name}/model",
        },
        ....
    ]
}
```

SageMaker AI can initially call the List Models API without providing a value for
`next_page_token`. If a `nextPageToken` field is returned as part
of the response, it will be provided as the value for `next_page_token` in a
subsequent List Models call. If a `nextPageToken` is not returned, it means
that there are no more models to return.

## Get Model API

This is a simple read API on the `model_name` entity.

```

GET /models/{model_name} HTTP/1.1
Accept: application/json

{
     "modelName" : "{model_name}",
     "modelUrl" : "/opt/ml/models/{model_name}/model",
}
```

###### Note

If `model_name` is not loaded, this API should return 404.

## Unload Model API

Instructs the SageMaker AI platform to instruct the customer container to unload a model from
memory. This initiates the eviction of a candidate model as determined by the platform
when starting the process of loading a new model. The resources provisioned to
`model_name` should be reclaimed by the container when this API returns a
response.

```
DELETE /models/{model_name}
```

###### Note

If `model_name` is not loaded, this API should return 404.

## Invoke Model API

Makes a prediction request from the particular `model_name` supplied. The
SageMaker AI Runtime `InvokeEndpoint` request supports
`X-Amzn-SageMaker-Target-Model` as a new header that takes the relative path
of the model specified for invocation. The SageMaker AI system constructs the absolute path of the
model by combining the prefix that is provided as part of the `CreateModel` API
call with the relative path of the model.

```
POST /models/{model_name}/invoke HTTP/1.1
Content-Type: ContentType
Accept: Accept
X-Amzn-SageMaker-Custom-Attributes: CustomAttributes
X-Amzn-SageMaker-Target-Model: [relativePath]/{artifactName}.tar.gz
```

###### Note

If `model_name` is not loaded, this API should return 404.

Additionally, on GPU instances, if `InvokeEndpoint` fails due to a lack of
memory or other resources, this API should return a 507 HTTP status code to SageMaker AI, which
then initiates unloading unused models to reclaim.
