Defect Detection App is in preview release and is subject to change.

# WorkflowResult

Contains the analysis results for an image. A `WorkflowResult` object
is returned from a call to [POST /workflows/{workflowId}/run](api-post-workflow-run.md "api-post-workflow-run.md") and
from [GET /workflows/{workflowId}/images](api-get-workflow-images.md "api-get-workflow-images.md").

Format: JSON

## creationTime

The timestamp for the date and time that the workflow started running.

Type: Timestamp

## image

The base64 encoded image that the model analyzed.

Type: String

## imageDataFilePath

The path to the analyzed image (`image`). If the model is a segmentation model or a heatmap model,
`imageDataFilePath` contains the analyzed image with colored masks covering the
predicted locations of anomalies. Each type of anomaly has a different color.
The image is in JPEG format. The file name is the same as the image provided for analysis
with the `.out.jpg` extension added.

Type: String

## inferenceFilePath

A JSON file containing device fleet auxiliary inputs information.

Type: String

## inferenceResult

The prediction that the model makes for the image.

Type: [InferenceResult](api-dt-inferenceResult.md "api-dt-inferenceResult.md")

## captureID

The ID of the captured image.

Type: String

## inputImageFilePath

The path to the input image file path.

Type: String

## processingTime

The amount of time, in milliseconds, that it took to run the workflow.

Type: float
