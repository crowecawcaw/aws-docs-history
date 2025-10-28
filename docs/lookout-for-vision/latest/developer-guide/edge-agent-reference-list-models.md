End of support notice: On October 31, 2025, AWS
will discontinue support for Amazon Lookout for Vision. After October 31, 2025, you will
no longer be able to access the Lookout for Vision console or Lookout for Vision resources.
For more information, visit this [blog post](https://aws.amazon.com/blogs/machine-learning/exploring-alternatives-and-seamlessly-migrating-data-from-amazon-lookout-for-vision "https://aws.amazon.com/blogs/machine-learning/exploring-alternatives-and-seamlessly-migrating-data-from-amazon-lookout-for-vision").

# ListModels

Lists the models deployed to an AWS IoT Greengrass Version 2 core device.

```
rpc ListModels(ListModelsRequest) returns (ListModelsResponse);
```

## ListModelsRequest

```
message ListModelsRequest {}
```

## ListModelsResponse

```


message ModelMetadata {
  string model_component = 1;
  string lookout_vision_model_arn = 2;
  ModelStatus status = 3;
  string status_message = 4;
}
```

```
message ListModelsResponse {
  repeated ModelMetadata models = 1;
}
```

### ModelMetadata

###### model_component

The name of AWS IoT Greengrass Version 2 component that contains an Amazon Lookout for Vision model.

###### lookout_vision_model_arn

The Amazon Resource Name (ARN) of the Amazon Lookout for Vision model that was used to
generate the AWS IoT Greengrass V2 component.

###### status

The current status of the model. For more information,
see [ModelStatus](edge-agent-reference-enums-model-status.md "edge-agent-reference-enums-model-status.md").

###### status_message

The status message for the model.

## Status codes

| Code     | Number | Description                     |
| -------- | ------ | ------------------------------- |
| OK       | 0      | The call was successful.        |
| UNKNOWN  | 2      | An unknown error has occurred.  |
| INTERNAL | 13     | An internal error has occurred. |
