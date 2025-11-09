End of support notice: On October 31, 2025, AWS
will discontinue support for Amazon Lookout for Vision. After October 31, 2025, you will
no longer be able to access the Lookout for Vision console or Lookout for Vision resources.
For more information, visit this [blog post](https://aws.amazon.com/blogs/machine-learning/exploring-alternatives-and-seamlessly-migrating-data-from-amazon-lookout-for-vision "https://aws.amazon.com/blogs/machine-learning/exploring-alternatives-and-seamlessly-migrating-data-from-amazon-lookout-for-vision").

# StopModel

Stops a model running on an AWS IoT Greengrass Version 2 core device.
`StopModel` returns after the model has stopped.
The model has stopped successfully if the `Status` field in the response is `STOPPED`.

```
  rpc StopModel(StopModelRequest) returns (StopModelResponse);
```

## StopModelRequest

```

message StopModelRequest {
  string model_component = 1;
}
```

###### model_component

The name of the AWS IoT Greengrass Version 2 component that contains the model you want to stop.

## StopModelResponse

```
message StopModelResponse {
  ModelStatus status = 1;
}
```

###### status

The current status of the model. The response is `STOPPED` if the call
succeeds. For more information,
see [ModelStatus](edge-agent-reference-enums-model-status.md "edge-agent-reference-enums-model-status.md").

## Status codes

| Code                | Number | Description                                                                            |
| ------------------- | ------ | -------------------------------------------------------------------------------------- |
| OK                  | 0      | The model is stopping.                                                                 |
| UNKNOWN             | 2      | An unknown error has occurred.                                                         |
| INVALID_ARGUMENT    | 3      | One or more input parameters are invalid. Check<br>the error message for more details. |
| NOT_FOUND           | 5      | A model with the supplied name wasn't found.                                           |
| FAILED_PRECONDITION | 9      | The method was called for a model that is not in the<br>RUNNING state.                 |
| INTERNAL            | 13     | An internal error has occurred.                                                        |
