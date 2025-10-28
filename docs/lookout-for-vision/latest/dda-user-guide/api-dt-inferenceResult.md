Defect Detection App is in preview release and is subject to change.

# InferenceResult

The prediction that the model makes for an image. For more information,
see [POST /workflows/{workflowId}/run](api-post-workflow-run.md "api-post-workflow-run.md").

## anomalies

If the model is a segmentation model or a heatmap model, `anomalies` contains the
information about each anomaly type, such as the color information needed to map
a mask color to the mask color on the image. The following example JSON from a heatmap model shows
the color map. `class-name` is the type of the anomaly. Wwith a heatmap model, the value is always
`anomaly`. With segmentation models, the value depends on the anomaly labels used to train the model.
`hex-color` is the color for the type of the anomaly.
`total-percentage-area` is the percentage of the image that the
anomaly type covers (A float avalue from 0-1).

```
{
      "anomalies": {
            "1": {
                "class-name": "anomaly",
                "hex-color": "#23a436",
                "total-percentage-area": 0.0008588588680140674
            }
        }
```

## anomaly_score

A number that quantifies how much anomalies predicted for an image
deviate from an images without anomalies. `anomaly_score` is a
float value ranging from `0.0` to (lowest deviation from a normal
image) to `1.0` (highest deviation from a normal image).

Defect Detection App returns a value for `anomaly_score`, even if the prediction for
an image is normal.

Type: float

## anomaly_threshold

A number in the Anomaly Score scale that is calculated at training time which
determines the boundary between what the models think is anomalous and
normal.

A number that determines when the predicted classification for an image is
normal or anomalous. Images with an `anomaly_score` that is equal to or
above the value of `anomaly_threshold` are deemed anomalous. A
`anomaly_score` value that is below `anomaly_threshold` indicates
a normal image.

The value of `anomaly_threshold` that a model uses is calculated by
Defect Detection App when you train the model. You can't set or change the value of
`anomaly_threshold`. If the model predicts too many images with the wrong
classification, consider retraining the model with better training images.
Alternatively, calculate a custom threshold value by using values greater or
smaller than the value of `anomaly_threshold`. Values lower than
`anomaly_threshold` result in more images predicted as anomalous

Values higher than `anomaly_threshold` result in less images predicted
as anomlalous.

To use your custom `anomaly_threshold` value, you need to implement
code in your solution that compares the value of `anomaly_score` with
your custom `threshold_value` value.

Type: float

## confidence

The confidence that the model has in the accuracy of its prediction. `confidence`
is a `float` value ranging from `0.0` (lowest confidence) to 1.0 (highest confidence).

Type: float

## inference_result

The classification for the image. `Normal` for an image with no predicted anomalies. `Anomaly`
for an image with predicted anomalies.

Type: string

## mask_background

If the model is a segmentation model or a heatmap model
`mask_background` contains information about the mask background,
such as the color information for the image background. in the following JSON
example: `class-name` is the type of the anomaly. For the background,
the class name is `background`. `rgb-color` is the RGB color
for the image background. `total-percentage-area` is the percentage
of the image that the anomaly type covers (A float avalue from 0-1).

```

       "mask_background": {
            "class-name": "background",
            "rgb-color": [
                255,
                255,
                255
            ],
            "total-percentage-area": 0.9991411566734314
       }
```

## mask_image

The base64 encoded mask image for the analyzed image.
