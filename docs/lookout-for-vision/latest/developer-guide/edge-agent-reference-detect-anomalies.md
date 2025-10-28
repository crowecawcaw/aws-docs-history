End of support notice: On October 31, 2025, AWS
will discontinue support for Amazon Lookout for Vision. After October 31, 2025, you will
no longer be able to access the Lookout for Vision console or Lookout for Vision resources.
For more information, visit this [blog post](https://aws.amazon.com/blogs/machine-learning/exploring-alternatives-and-seamlessly-migrating-data-from-amazon-lookout-for-vision "https://aws.amazon.com/blogs/machine-learning/exploring-alternatives-and-seamlessly-migrating-data-from-amazon-lookout-for-vision").

# DetectAnomalies

Detects anomalies in the supplied image.

The response from `DetectAnomalies` includes a Boolean prediction that
the image contains one or more anomalies and a confidence value for the prediction.
If the model is a segmentation model, the response includes the following:

- A mask image that covers each anomaly type in a unique color. You
  can have `DetectAnomalies` store the mask image in shared memory, or
  return the mask as image bytes.
- The percentage area of the image that an anomaly type covers.
- The hex color for an anomaly type on the mask image.

###### Note

The model that you use with `DetectAnomalies` must be running. You
can get the current status by calling [DescribeModel](edge-agent-reference-describe-model.md "edge-agent-reference-describe-model.md").
To start running a model, see
[StartModel](edge-agent-reference-start-model.md "edge-agent-reference-start-model.md").

`DetectAnomalies` supports packed bitmaps (images) in interleaved RGB888 format.
The first byte represents the red channel, the second byte represents the green channel, and the third byte represents the blue channel.
If you provide the image in a different format, such as BGR, the predictions from DetectAnomalies are incorrect.

By default, OpenCV uses the BGR format for image bitmaps. If you are using OpenCV to capture images for analysis with
`DetectAnomalies`, you must convert the image to RGB888 format before you pass the image to `DetectAnomalies`.

The minimum supported image dimension is 64x64 pixels. The maximum supported image dimension is 4096x4096 pixels.

You can send the image in the protobuf message or through a shared memory segment.
Serializing large images into the protobuf message can significantly increase the
latency of calls to `DetectAnomalies`. For the least latency, we
recommended that you use shared memory.

```
rpc DetectAnomalies(DetectAnomaliesRequest) returns (DetectAnomaliesResponse);

```

## DetectAnomaliesRequest

The input parameters for `DetectAnomalies`.

```

message Bitmap {
  int32 width = 1;
  int32 height = 2;
  oneof data {
    bytes byte_data = 3;
    SharedMemoryHandle shared_memory_handle = 4;
  }
}
```

```

message SharedMemoryHandle {
  string name = 1;
  uint64 size = 2;
  uint64 offset = 3;
}

```

```

message AnomalyMaskParams {
SharedMemoryHandle shared_memory_handle = 2;
}
```

```
message DetectAnomaliesRequest {
string model_component = 1;
Bitmap bitmap = 2;
AnomalyMaskParams anomaly_mask_params = 3;
}
```

### Bitmap

The image that you want to analyze with `DetectAnomalies`.

###### width

The width of the image in pixels.

###### height

The height of the image in pixels.

###### byte_data

Image bytes passed in protobuf message.

###### shared_memory_handle

Image bytes passed in shared memory segment.

#### SharedMemoryHandle

Represents a POSIX shared memory segment.

###### name

The name of the POSIX memory segment. For information about creating shared memory, see
[shm_open](https://man7.org/linux/man-pages/man3/shm_open.3.html "https://man7.org/linux/man-pages/man3/shm_open.3.html").

###### size

The image buffer size in bytes starting from the offset.

###### offset

The offset, in bytes, to the beginning of the image buffer
from the start of the shared memory segment.

### AnomalyMaskParams

Parameters for outputting an anomaly mask. (Segmentation model).

###### shared_memory_handle

Contains the image bytes for the mask, if `shared_memory_handle` wasn't provided.

### DetectAnomaliesRequest

###### model_component

The name of the AWS IoT Greengrass V2 component that contains the model you want to use.

###### bitmap

The image that you want analyze with `DetectAnomalies`.

###### anomaly_mask_params

Optional parameters for outputting the mask. (Segmentation model).

## DetectAnomaliesResponse

The response from `DetectAnomalies`.

```
message DetectAnomalyResult {
bool is_anomalous = 1;
float confidence = 2;
Bitmap anomaly_mask = 3;
repeated Anomaly anomalies = 4;
float anomaly_score = 5;
float anomaly_threshold = 6;
}
```

```

message Anomaly {
string name = 1;
PixelAnomaly pixel_anomaly = 2;
```

```

message PixelAnomaly {
float total_percentage_area = 1;
string hex_color = 2;
}
```

```
message DetectAnomaliesResponse {
  DetectAnomalyResult detect_anomaly_result = 1;
}
```

### Anomaly

Represents an anomaly found on an image. (Segmentation model).

###### name

The name of an anomaly type found in an image. `name` maps to an anomaly
type in the training dataset.
The service automatically inserts the background anomaly type into the
response from DetectAnomalies.

###### pixel_anomaly

Information about the pixel mask that covers an anomaly type.

### PixelAnomaly

Information about the pixel mask that covers an anomaly type. (Segmentation model).

###### total_percentage_area

The percentage area of the image that the anomaly type covers.

###### hex_color

A hex color value that represents the anomaly type on the image. The color maps to the color of the anomaly type used in the training dataset.

### DetectAnomalyResult

###### is_anomalous

Indicates if the image contains an anomaly. `true` if the
image contains an anomaly. `false` if the image is
normal.

###### confidence

The confidence that `DetectAnomalies` has in the accuracy
of the prediction. `confidence` is a floating point value
between 0 and 1.

###### anomaly_mask

if shared_memory_handle wasn't provided, contains the image bytes for
the mask. (Segmentation model).

###### anomalies

A list of 0 or more anomalies found within the input image.
(Segmentation model).

###### anomaly_score

A number that quantifies how much anomalies predicted for an image
deviate from an image without anomalies. `anomaly_score` is a
float value ranging from `0.0` to (lowest deviation from a
normal image) to 1.0 (highest deviation from a normal image). Amazon Lookout for Vision
returns a value for `anomaly_score`, even if the prediction
for an image is normal.

###### anomaly_threshold

A number (float) that determines when the predicted classification for an image is
normal or anomalous. Images with an `anomaly_score` that is equal to or
above the value of `anomaly_threshold` are deemed anomalous. A
`anomaly_score` value that is below `anomaly_threshold` indicates
a normal image. The value of `anomaly_threshold` that a model uses is calculated by
by Amazon Lookout for Vision when you train the model. You can't set or change the value of
`anomaly_threshold`

### Status codes

| Code                | Number | Description                                                                                                                                                                                                  |
| ------------------- | ------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| OK                  | 0      | `DetectAnomalies` successfully made a prediction                                                                                                                                                             |
| UNKNOWN             | 2      | An unknown error has occurred.                                                                                                                                                                               |
| INVALID_ARGUMENT    | 3      | One or more input parameters are invalid. Check the error message for more details.                                                                                                                          |
| NOT_FOUND           | 5      | A model with the specified name wasn't found.                                                                                                                                                                |
| RESOURCE_EXHAUSTED  | 8      | There aren't enough resources to perform this operation. For example, The Lookout for Vision Edge Agent can't keep up with the rate of calls to `DetectAnomalies`. Check the error message for more details. |
| FAILED_PRECONDITION | 9      | `DetectAnomalies` was called for model that is not in the RUNNING state.                                                                                                                                     |
| INTERNAL            | 13     | An internal error has occurred.                                                                                                                                                                              |
