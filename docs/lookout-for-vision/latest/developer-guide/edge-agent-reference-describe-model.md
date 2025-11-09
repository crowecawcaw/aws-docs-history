End of support notice: On October 31, 2025, AWS
will discontinue support for Amazon Lookout for Vision. After October 31, 2025, you will
no longer be able to access the Lookout for Vision console or Lookout for Vision resources.
For more information, visit this [blog post](https://aws.amazon.com/blogs/machine-learning/exploring-alternatives-and-seamlessly-migrating-data-from-amazon-lookout-for-vision "https://aws.amazon.com/blogs/machine-learning/exploring-alternatives-and-seamlessly-migrating-data-from-amazon-lookout-for-vision").

# DescribeModel

Describes an Amazon Lookout for Vision model that's deployed to an AWS IoT Greengrass Version 2 core device.

```
rpc DescribeModel(DescribeModelRequest) returns (DescribeModelResponse);

```

## DescribeModelRequest

```

message DescribeModelRequest {
  string model_component = 1;
}
```

###### model_component

The name of the AWS IoT Greengrass V2 component that contains the model you want to describe.

## DescribeModelResponse

```
message ModelDescription {
  string model_component = 1;
  string lookout_vision_model_arn = 2;
  ModelStatus status = 3;
  string status_message = 4;
}
```

```

message DescribeModelResponse {
  ModelDescription model_description = 1;
}
```

### ModelDescription

###### model_component

The name of AWS IoT Greengrass Version 2 component that contains the Amazon Lookout for Vision model.

###### lookout_vision_model_arn

The Amazon Resource Name ARN of the Amazon Lookout for Vision model that was used to
generate the AWS IoT Greengrass V2 component.

###### status

The current status of the model. For more information,
see [ModelStatus](edge-agent-reference-enums-model-status.md "edge-agent-reference-enums-model-status.md").

###### status_message

The status message for the model.

## Status codes

| Code             | Number | Description                                                                            |
| ---------------- | ------ | -------------------------------------------------------------------------------------- |
| OK               | 0      | The call was successful.                                                               |
| UNKNOWN          | 2      | An unknown error has occurred.                                                         |
| INVALID_ARGUMENT | 3      | One or more input parameters are invalid. Check the error<br>message for more details. |
| NOT_FOUND        | 5      | A model with the supplied name wasn't found.                                           |
| INTERNAL         | 13     | An internal error has occurred.                                                        |
