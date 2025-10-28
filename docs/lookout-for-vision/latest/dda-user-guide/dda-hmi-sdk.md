Defect Detection App is in preview release and is subject to change.

# Creating a Station App application

You can use Defect Detection Station App SDK operations to create your own Station App application. For
example, you might want to create a Station App application that only works with specific
workflows or image sources.

The Defect Detection Station App SDK provides operations that are useful for building a Station App. These operations cover the following tasks (the links are to the equivalent
Station App console tasks):

- [Adding an image source](dda-configure-image-source.md "dda-configure-image-source.md")
- [Collecting images for your datasets](dda-collect-images.md "dda-collect-images.md")
- [Configuring a workflow](dda-configure-workflow.md "dda-configure-workflow.md")
- [Running a workflow manually](dda-run-workflow.md "dda-run-workflow.md")
- [Viewing digital input signal results](dda-run-workflow-view-results.md "dda-run-workflow-view-results.md")
- [Getting all workflow results](dda-run-workflow-results.md "dda-run-workflow-results.md")
- [Viewing the models deployed to a station](dda-view-models-hmi.md "dda-view-models-hmi.md")
- [Managing station health](dda-managing-system-health.md "dda-managing-system-health.md")
  To familiarlize yourself with the Station App, do the following:

1. Read [Understanding Defect Detection App](dda-understanding-usage.md "dda-understanding-usage.md").
2. Set up a station on your edge device. For more information, see [Setting up a station](dda-setting-up-station.md "dda-setting-up-station.md").
3. Train and deploy a model to your edge device. For more information, see [Training and deploying a model](dda-train-deploy-model.md "dda-train-deploy-model.md"),
4. Use the Station App to configure and run a workflow. For more information, see
   [Analyzing images with the Defect Detection Station App](dda-inference.md "dda-inference.md").
   The Defect Detection App API is available from the local station once it is provisioned. It is
   accessible from port 5000. For example, the following request returns the list of available cameras:

```
curl -X GET `0.0.0.0`:5000/cameras
```

The Defect Detection App API reference is available in OpenAPI format. Open a browser and navigate to
`x.x.x.x:5000/docs`, where x.x.x.x is the IP address of the station.

###### Topics

- [Displaying the station name (SDK)](#dda-hmi-sdk-station-name "#dda-hmi-sdk-station-name")
- [Adding an image source (SDK)](#dda-hmi-sdk-image-source "#dda-hmi-sdk-image-source")
- [Capturing images for a dataset (SDK)](#dda-hmi-sdk-image-source-capture-images "#dda-hmi-sdk-image-source-capture-images")
- [Configuring a workflow
  (SDK)](#dda-hmi-sdk-configure-workflow "#dda-hmi-sdk-configure-workflow")
- [Manually running a workflow (SDK)](#dda-hmi-sdk-run-workflow-manual "#dda-hmi-sdk-run-workflow-manual")
- [Viewing the workflow results from a digital input signal (SDK)](#dda-hmi-sdk-view-di-results "#dda-hmi-sdk-view-di-results")
- [Getting all workflow results (SDK)](#dda-hmi-sdk-get-all-workflow-results "#dda-hmi-sdk-get-all-workflow-results")
- [Listing the models deployed to a station (SDK)](#dda-hmi-sdk-view-models "#dda-hmi-sdk-view-models")
- [Managing station health (SDK)](#dda-hmi-sdk-system-health "#dda-hmi-sdk-system-health")

## Displaying the station name (SDK)

Your application should display the name of the station that's on the edge device.
You can use the following operation to get the station name:

```
curl -X GET 0.0.0.0:5000/system/station
```

The JSON response is the name of the station that's on the edge device, along with
other information.

```
{
  "name": "string",
  "version": "string",
  "webuxUrl": "string",
  "tenantId": "string",
  "deviceId": "string",
  "logoImage": "string"}
```

## Adding an image source (SDK)

An image source is the location where Station App gets the images to analyze. The input to an image
source can be a camera attached to the station or a folder on the stations's hard drive.
Your application can use an image source to [collect
dataset images](dda-collect-images.md "dda-collect-images.md") before training a model and to provide images for analysis by
a [workflow](dda-inference.md "dda-inference.md").

The following sections describe how to add a camera or a folder as the image source.

###### Topics

- [Adding a camera as an image source](#dda-hmi-sdk-image-source-camera "#dda-hmi-sdk-image-source-camera")
- [Configuring the image source](#dda-hmi-sdk-image-source-camera-update "#dda-hmi-sdk-image-source-camera-update")
- [Adding a folder as an image source](#dda-hmi-sdk-image-source-folder "#dda-hmi-sdk-image-source-folder")

### Adding a camera as an image source

To add a camera image source, use the `Get /cameras` operation to get a
list of cameras that Station App has discovered on the network.

```
curl -X GET 0.0.0.0:5000/cameras
```

Note the `id` (`Fake_1`) in the response. You use the ID to associate the
camera with the image source.

```
[
    {
        address: "0.0.0.0",
        **id: "Fake\_1"**,
        model: "Fake",
        physical_id: "Fake_1",
        protocol: "Fake",
        serial: "1",
        vendor: "Aravis"
    }
]
```

In the call to `POST /image-sources` you include
the camera Id in the `cameraId` field. You also specify a name, description,
and image source configuration for the image source. For more information,
see [Configuring the camera](dda-set-up-camera-position.md "dda-set-up-camera-position.md").

```
curl -X POST 0.0.0.0:5000/image-sources -H "Content-Type: application/json" -d '{
    "cameraId": "Fake_1",
    "description": "My camera 2",
    "imageSourceConfiguration": {
        "exposure": 4000,
        "gain": 10,
        "imageSourceConfigId": "7cd3e65e-c6b7-4e02-886c-a3243ca63b55",
        "processingPipeline": "video/x-bayer, format=bggr ! bayer2rgb ! video/x-raw, format=RGBA ! videoconvert"
    },
    "name": "Camera 2",
    "type": "Camera"
}'
```

The response is the ID (`imageSourceId`) for the new image source.

```
{"imageSourceId":"d2pnwrmy"}
```

### Configuring the image source

The following example configures a camera image source. You specify the xx
in the `imageSourceConfiguration` field. You also
specify a name, description, and type for the image source.

```
curl -X PATCH 0.0.0.0:5000/image-sources/my_image_source_id  -H "Content-Type: application/json" -d '{
    "cameraId": "Fake_1",
    "description": "My camera 2",
    "imageSourceConfiguration": {
        "exposure": 4000,
        "gain": 10,
        "imageSourceConfigId": "7cd3e65e-c6b7-4e02-886c-a3243ca63b55",
        "processingPipeline": "video/x-bayer, format=bggr ! bayer2rgb ! video/x-raw, format=RGBA ! videoconvert"
    },
    "name": "Camera 2",
    "type": "Camera"
}'

```

The response is the ID (`imageSourceId`) for the image source.

```
{"imageSourceId":"nzyxmiyn"}
```

### Adding a folder as an image source

The following example creates an image source for a folder. You specify the folder
location in the `location` field. You also
specify a name, description, and type for the image source.

```
curl -X POST 0.0.0.0:5000/image-sources -H "Content-Type: application/json" -d '{
    "description": "My folder 3",
    "location": "/aws_dda/images",
    "name": "My_folder_3",
    "type": "Folder"
}'

```

The response is the ID (`imageSourceId`) for the new image source.

```
{"imageSourceId":"nzyxmiyn"}
```

## Capturing images for a dataset (SDK)

To train a model, you need images for your datasets. In your application, you can use
the SDK to show preview images and capture images from a camera image source. If
you don't know the ID of the image source, you can call
GET /image-sources to retrieve a list of the image sources on the Defect Detection App.

### Getting a preview image (SDK)

Use the SDK to get a preview image for display in your application.
Consider how often you need to refresh the image. The Station App refreshes the
preview image every 500ms. The following example gets a preview image from
a camera image source with the ID `d2pnwrmy`.

```
curl -X POST 0.0.0.0:5000/image-sources/d2pnwrmy/preview
```

The response is the base64 encoded image that you can show in your application.

```
{"image":"/9j/7..."}
```

### Capturing an image (SDK)

You can capture images for a dataset and save them as files on your station. Optionally, you can
use the `filePrefix` field to specify a file prefix for the captured
images. The following example captures an image from a camera image source with the
ID `d2pnwrmy`. The image file names names are prefixed with
`my_prefix`.

```
curl -X POST 0.0.0.0:5000/image-sources/d2pnwrmy/capture  -H "Content-Type: application/json" -d '{"filePrefix": "my_prefix"}'

```

The response is the base64 encoded image that you can show in your application.

```
{"image":"/9j/7..."}
```

To get the location where the operation saves the image for an image source, call the
`GET /image-source` operation and check the `imageCapturePath` field in the response.

```
curl -X GET 0.0.0.0:5000/image-sources/d2pnwrmy
```

```
{
    "cameraId": "Fake_1",
    "creationTime": 1688054152532,
    "description": "My camera 2",
    **"imageCapturePath": "/aws\_dda/image-capture/d2pnwrmy"**,
    "imageSourceConfiguration": {
        "creationTime": 1688054152532,
        "exposure": 4000,
        "gain": 10,
        "imageSourceConfigId": "0yjafpr8",
        "processingPipeline": "video/x-bayer, format=bggr ! bayer2rgb ! video/x-raw, format=RGBA ! videoconvert"
    },
    "imageSourceId": "d2pnwrmy",
    "lastUpdateTime": 1688054152532,
    "location": null,
    "name": "Camera 2",
    "type": "Camera"
}
```

To add the images to a dataset, you need to upload the images to a project by
using the Defect Detection App. For more information, see [Creating your datasets](dda-create-dataset.md "dda-create-dataset.md").

### Getting captured images (SDK)

The Station App shows the last 12 images captured by an image source. The Station App
also allows you to delete any of the those images. For more information see [Collecting images for your datasets](dda-collect-images.md "dda-collect-images.md").

To get the last 12 images, call the `GET /captured-images` operation and specify the `path` in the
request parameter. Replace `imageSourceId`
with the ID of the image source that you want to use.

```
curl -X GET 0.0.0.0:5000/captured-images?path=/aws_dda/image-capture/`imageSourceId`
```

The response is an array containing the base64 encoded image and the location of
the image, for each of the last 12 captured images.

```
[{
  image:"base64 image string"
  path:"/aws_dda/image-capture/s9cxrzje/s9cxrzje-1691604255851.jpg"
},
{
  image:"base64 image string"
  path:"/aws_dda/image-capture/s9cxrzje/s9cxrzje-1685649711750.jpg"
},
{
  image:"base64 image string"
  path:"/aws_dda/image-capture/s…xrzje-1685649709455.jpg"
}]
```

To delete an image, call `DELETE /captured-images`. Replace `imageSourceId`
with the ID of the image source that you want to delete the image from. In the
`FilePath` request paramter, replace `imageFileName` with
the name of the image that you want to delete.

```
curl -X DELETE  0.0.0.0:5000/captured-images?filePath=/aws_dda/image-capture/`imageSourceId`/`imageFileName`
```

The response is the filename of the delete image.

## Configuring a workflow

(SDK)

To configure a workflow you use the `PATCH /workflow` operation. It requires the
`workflowId` for the workflow that you want to configure.

###### Topics

- [Getting the workflow ID](#dda-hmi-sdk-get-workflow-id "#dda-hmi-sdk-get-workflow-id")
- [Configuring the workflow](#dda-hmi-sdk-patch-workflow "#dda-hmi-sdk-patch-workflow")

### Getting the workflow ID

To get the workflow ID, call the `GET /workflows` method.
For example, the following curl command gets the workflows on a station.

```
curl -X GET 0.0.0.0:5000/workflows
```

The response is a list of the workflows that are on the station. Each workflow
has an ID (`workflowId`) that you use to identify the workflow that
you want to configure. In the example, workflow `bx7aue6i` isn't
configured. You configure this workflow in [Configuring the workflow](#dda-hmi-sdk-patch-workflow "#dda-hmi-sdk-patch-workflow").

```
[
    {
        "creationTime": 1684516880477,
        "description": "",
        "featureConfigurations": [
            {
                "modelName": "model-jmbqzfir",
                "type": "LFVModel"
            }
        ],
        "imageSources": [
            {
                "cameraId": "Fake_1",
                "creationTime": 1684517367683,
                "description": "",
                "imageCapturePath": "/aws_dda/image-capture/f02d24675c54414989971a08526",
                "imageSourceConfiguration": {
                    "creationTime": 1684517367683,
                    "exposure": 4000,
                    "gain": 10,
                    "imageSourceConfigId": "7cd3e65e-c6b7-4e02-886c-a3243ca63b55",
                    "processingPipeline": "video/x-bayer, format=bggr ! bayer2rgb ! video/x-raw, format=RGBA ! videoconvert"
                },
                "imageSourceId": "f02d24675c54414989971a08526",
                "lastUpdateTime": 1684517432122,
                "location": null,
                "name": "Fake_1 Camera",
                "type": "Camera"
            }
        ],
        "inputConfigurations": [],
        "lastUpdatedTime": 1684517954108,
        "name": "workflow_czaudzmn",
        "outputConfigurations": [],
        "workflowId": "czaudzmn",
        "workflowOutputPath": "/aws_dda/inference-results/czaudzmn"
    },
    {
        "creationTime": 1684875910909,
        "description": "Updated bx7aue6i workflow",
        "featureConfigurations": [
            {
                "modelName": "model-jmbqzfir",
                "type": "LFVModel"
            }
        ],
        "imageSources": [
            {
                "cameraId": "Fake_1",
                "creationTime": 1684517367683,
                "description": "",
                "imageCapturePath": "/aws_dda/image-capture/f02d24675c54414989971a08526",
                "imageSourceConfiguration": {
                    "creationTime": 1684517367683,
                    "exposure": 4000,
                    "gain": 10,
                    "imageSourceConfigId": "7cd3e65e-c6b7-4e02-886c-a3243ca63b55",
                    "processingPipeline": "video/x-bayer, format=bggr ! bayer2rgb ! video/x-raw, format=RGBA ! videoconvert"
                },
                "imageSourceId": "f02d24675c54414989971a08526",
                "lastUpdateTime": 1684517432122,
                "location": null,
                "name": "Fake_1 Camera",
                "type": "Camera"
            }
        ],
        "inputConfigurations": [],
        "lastUpdatedTime": 1684878833016,
        "name": "workflow_bx7aue6i",
        "outputConfigurations": [],
        "workflowId": "bx7aue6i",
        "workflowOutputPath": "/aws_dda/inference-results/bx7aue6i"
    },
    {
        "creationTime": 1684875911486,
        "description": "",
        "featureConfigurations": [
            {
                "modelName": "model-jmbqzfir",
                "type": "LFVModel"
            }
        ],
        "imageSources": [
            {
                "cameraId": "Fake_1",
                "creationTime": 1684517367683,
                "description": "",
                "imageCapturePath": "/aws_dda/image-capture/f02d24675c54414989971a08526",
                "imageSourceConfiguration": {
                    "creationTime": 1684517367683,
                    "exposure": 4000,
                    "gain": 10,
                    "imageSourceConfigId": "7cd3e65e-c6b7-4e02-886c-a3243ca63b55",
                    "processingPipeline": "video/x-bayer, format=bggr ! bayer2rgb ! video/x-raw, format=RGBA ! videoconvert"
                },
                "imageSourceId": "f02d24675c54414989971a08526",
                "lastUpdateTime": 1684517432122,
                "location": null,
                "name": "Fake_1 Camera",
                "type": "Camera"
            }
        ],
        "inputConfigurations": [],
        "lastUpdatedTime": 1685563499204,
        "name": "workflow_ajapogmm",
        "outputConfigurations": [],
        "workflowId": "ajapogmm",
        "workflowOutputPath": "/aws_dda/inference-results/ajapogmm"
    },
    {
        "creationTime": 1687471602871,
        "description": "",
        "featureConfigurations": [
            {
                "modelName": "model-1ruvp1c0",
                "type": "LFVModel"
            }
        ],
        "imageSources": [
            {
                "cameraId": null,
                "creationTime": 1684517469059,
                "description": "My folder",
                "imageCapturePath": "/aws_dda/image-capture/2032cebfe51346bdaaa7259c053",
                "imageSourceConfiguration": {},
                "imageSourceId": "2032cebfe51346bdaaa7259c053",
                "lastUpdateTime": 1684517469059,
                "location": "/aws_dda//images/",
                "name": "My_folder",
                "type": "Folder"
            }
        ],
        "inputConfigurations": [
            {
                "creationTime": 1687539121353,
                "debounceTime": 750,
                "inputConfigurationId": "hcxog3q5",
                "pin": "1",
                "triggerState": "GPIO.RISING"
            }
        ],
        "lastUpdatedTime": 1687539121353,
        "name": "workflow_881au41e",
        "outputConfigurations": [],
        "workflowId": "881au41e",
        "workflowOutputPath": "/aws_dda/inference-results/881au41e"
    }
]
```

###### Tip

You can change the number
of workflows by editing the station with the Defect Detection Station App cloud application.

### Configuring the workflow

To configure a workflow, use the `PATCH /workflow` operation.

In the call to `PATCH /workflows/{workflowId}`, include the
following:

- **feature configurations**
  (featureConfigurations) — The feature that you want to use to
  analyze an image. Currently, Defect Detection App only supports Amazon Lookout for Vision models
  and you must specify `LFVModel` in the feature configuration.
- **input configurations** —
  (Optional) Specifies the digital input signal that starts the running of
  a workflow.

The digital input becomes active as soon as you update the workflow.
To deactivate a digital input, update the workflow by removing the input
configuration. In this example, the input configuration isn't configured
and you can only run the workflow manually. For more information, see
[Running a workflow manually](dda-run-workflow.md "dda-run-workflow.md").

- **imageSources** — A list of [image sources](dda-configure-workflow.md#dda-workflow-image-source "dda-configure-workflow.md#dda-workflow-image-source") for the
  workflow. Currently, Defect Detection App supports only one image source.
- **outputConfigurations** — A list
  of output configurations for where the workflow stores the analysis
  results for images analyzed by the model.

For example, you can use the following curl command.

```
curl \
  0.0.0.0:5000/workflows/bx7aue6i \
  --request PATCH \
  --header "Content-Type: application/json" \
  --data @- << EOF
  {
    "description": "Updated bx7aue6i workflow",
    "featureConfigurations": [
        {
            "modelName": "model-jmbqzfir",
            "type": "LFVModel"
        }
    ],
    "imageSources": [
        {
            "cameraId": "Fake_1",
            "description": "Image source for bx7aue6i",
            "imageCapturePath": "/aws_dda/image-capture/f02d24675c54414989971a085",
            "imageSourceConfiguration": {
                "exposure": 4000,
                "gain": 10,
                "imageSourceConfigId": "7cd3e65e-c6b7-4e02-886c-a3243ca63b55",
                "processingPipeline": "video/x-bayer, format=bggr ! bayer2rgb ! video/x-raw, format=RGBA ! videoconvert"
            },
            "imageSourceId": "f02d24675c54414989971a08526f",
            "location": null,
            "name": "Fake_1 Camera",
            "type": "Camera"
        }
    ],
    "inputConfigurations": [],
    "name": "workflow_bx7aue6i",
    "outputConfigurations": []
  }

EOF
```

## Manually running a workflow (SDK)

To manually run a workflow with the SDK, use the following curl
command. Replace the following:

- `0.0.0.0` — with the IP address of the edge device. You
  can leave unchanged if you are running the command on the edge
  device.
- `workflowId` — with the ID for the workflow. To get the
  ID, call `GET /workflows`.

```
curl -X POST `0.0.0.0`:5000/workflows/`workflowId`/run
```

The response JSON includes the base64 encoded image (`image`) that was analyzed by the workflow and the
predicted classification for the image.

A workflow automatically saves analysis results to a folder
(`inferenceFilePath`) on the edge device. You can also get the location
by calling GET /workflow and checking the `workflowOutputPath` field.

The following JSON
is an example response from `POST /workflows/{workflowId}/run`.

```
{
    "creationTime": "2023-10-06T20:40:32",
    "imageDataFilePath": "//aws_dda/inference-results/881au41e/881au41e-1696624830804-2.overlay.jpg",
    "inferenceResult": {
        "anomalies": {
            "1": {
                "class-name": "anomaly",
                "hex-color": "#23a436",
                "total-percentage-area": 0.0008588588680140674
            }
        },
        "confidence": 0.5222712159156799,
        "anomaly_score": 0.4777287542819977,
        "anomaly_threshold": 0.4642670154571533,
        "inference_result": "Anomaly",
        "mask_background": {
            "class-name": "background",
            "rgb-color": [
                255,
                255,
                255
            ],
            "total-percentage-area": 0.9991411566734314
        },
        "mask_image": "iVBZ.."
    },
    "inferenceFilePath": "/aws_dda/inference-results/881au41e/881au41e-1696624830804.jsonl",
    "image": "/9BR...",
    "captureId": "881au41e-1696624830804",
    "inputImageFilePath": "//aws_dda/inference-results/881au41e/881au41e-1696624830804-1.jpg",
    "processingTime": 1749.32
}
```

## Viewing the workflow results from a digital input signal (SDK)

To get the analysis results for a workflow, including those triggered by a digital input signal, you call
the `GET /workflows/{workflowId}/images` operation.
To poll for digital input signals at the same rate as the Station App, call
`GET /workflows/{workflowId}/images` at 500 millisecond intervals.

To call `GET /workflows/{workflowId}/images`, you can use the following curl
command. Replace the following:

- `0.0.0.0` — with the IP address of the edge device. You
  can leave unchanged if you are running the command on the edge
  device.
- `workflowId` — with the ID for the workflow. To get the
  ID, call `GET /workflows`.

```
curl -X GET `0.0.0.0`:5000/workflows/`workflowId`/images
```

The following JSON is an example response from `GET
 /workflows/{workflowId}/images`.

```
{
    "images": [
        {
            "creationTime": "2023-05-23T22:46:14",
            "image": "xxx...",
            "imageDataFilePath": "file:///aws_dda/inference-results/czaudzmn/dda_eminfer_l4v_emdatacapture//czaudzmn-1684868316848-1.jpg",
            "inferenceFilePath": "/aws_dda/inference-results/czaudzmn/dda_eminfer_l4v_emdatacapture/czaudzmn-1684868316848.jsonl",
            "inferenceResult": {
                "confidence": 0.5,
                "inference_result": "Anomaly"
            }
        }
    ],
    "nextStartingPoint": 2
}
```

The response of is an array (`images`) of two `WorkflowResult`
objects that contain the analysis
results for the last 2 analyzed images (one `WorkflowObject` for each
image). To determine the results for the latest image analyzed, check the
`creationTime` field in the `WorkflowResult`
object.

A `WorkflowResult` object
includes the bas64 encoded
image (`image`) that was analyzed by the workflow and the predicted
classification for the image (inferenceResult).

If your model is a segmentation model, the image in the `image` field
is the anomaly labels mask image. Information about the predicted anomaly
labels and image mask is located in the `inferenceFilePath`. You can
also get the location by calling `GET /workflows/{workflowId}` and checking the
`workflowOutputPath` field.

## Getting all workflow results (SDK)

A call to `GET/workflows/{workflowId}/images`
gets the analysis results for the last two analyzed images. To see
the results for all analyzed images, you need to look at the files that the workflow
stores for each image it analyzes. You set the location for these file when you
configure the workflow. For more information, see [Configuring a workflow](dda-configure-workflow.md "dda-configure-workflow.md"). If necessary, you can get the location
from the workflow configuration page in the Station App. You can also get the location by
using the `GET /workflows/{workflowId}`
operation. For an example, see [Configuring a workflow
(SDK)](#dda-hmi-sdk-configure-workflow "#dda-hmi-sdk-configure-workflow").

For each analyzed image, the folder contains the analyzed image and the analysis results. If the model
is a segmentation model, the analyzed image includes the location masks for any anomalies found on the image. The analysis
results are in JSON format, as shown in the following example.

```
{
    "deviceFleetAuxiliaryInputs": [
        {
            "data-ref": "file:///aws_dda/inference-results/ajapogmm/dda_eminfer_l4v_emdatacapture//ajapogmm-1685563523430-1.jpg",
            "encoding": "NONE",
            "mode": "Input",
            "name": "Input-1",
            "observedContentType": "jpg"
        }
    ],
    "deviceFleetAuxiliaryOutputs": [
        {
            "data": "eyJDb25maWRlbmNlIjowLjUsIkVycm9yIG1zZyI6IiIsIkluZmVyZW5jZSByZXN1bHQiOiJBbm9tYWx5IiwiSW5mZXJlbmNlIHN0YXR1cyI6InN1Y2Nlc3MifQ==",
            "encoding": "BASE64",
            "mode": "Output",
            "name": "Output-1",
            "observedContentType": "json"
        }
    ],
    "deviceFleetInputs": [],
    "deviceFleetOutputs": [],
    "eventMetadata": {
        "deviceFleetName": "dda_fleet",
        "deviceId": "li1tn5qb",
        "eventId": "ajapogmm-1685563523430",
        "inferenceTime": "2023-05-31T20:05:24",
        "modelName": "model-jmbqzfir",
        "modelVersion": "1.0"
    },
    "eventVersion": "0"
}
```

`deviceFleetAuxiliaryInputs` contains information about the input image.
`deviceFleetAuxiliaryOutputs` contains the analysis
results in the `data` field. To view the analysis results, you need to decode
`data` as it is base64 encoded. After decoding, the results should be
similar to the following:

```
{
    "Confidence": 0.5,
    "Error msg": "",
    "Inference result": "Anomaly",
    "Inference status": "success"
}
```

`Confidence` is the model's confidence in the accuracy of its prediction.
`Inference result` is the prediction the model has made.
`Normal` if no anomalies are predicted, `Anomaly` if anomalies
are predicted. If the workflow successfully analyzed the image, the value of
`Inference status` is `success`, otherwise an error has
occurred and `Error msg` contains an error message.

## Listing the models deployed to a station (SDK)

You can use the `GET/feature-configurations` operation to get a list
of the models that you have deployed to a station.

```
curl -X GET 0.0.0.0:5000/feature-configurations
```

For each model, the response includes the model name and model type.

```
[
    {
        "modelName": "model-1ruvp1c0",
        "type": "LFVModel"
    },
    {
        "modelName": "model-jmbqzfir",
        "type": "LFVModel"
    },
    {
        "modelName": "model-is2ky1al",
        "type": "LFVModel"
    }
]
```

## Managing station health (SDK)

You can use station health operations to get information about the health of a station
and fix issues that you encounter.

###### Topics

- [Getting the current status of a station (SDK)](#dda-hmi-sdk-get-current-status "#dda-hmi-sdk-get-current-status")
- [Getting the health of a station (SDK)](#dda-hmi-sdk-get-system-health "#dda-hmi-sdk-get-system-health")
- [Getting the stations logs (SDK)](#dda-hmi-sdk-get-station-logs "#dda-hmi-sdk-get-station-logs")
- [Restarting the Defect Detection Station App (SDK)](#dda-hmi-sdk-restart-station-app "#dda-hmi-sdk-restart-station-app")

### Getting the current status of a station (SDK)

You can use the `GET/dda-component-status` operation to get the current health of a station.

```
curl -X GET 0.0.0.0:5000/dda-component-status
```

If the station is healthy, the response is `HEALTHY`, otherwise the
response is `UNHEALTHY`. To get more information about the health of the
station, call `GET /system-health`.

### Getting the health of a station (SDK)

You can use the `GET /system-health` operation to get the current health of a station.
Station health information is calculated when you call the `GET /system-health` operation.
Note that the Defect Detection Station App uses the `GET /system-health` operation
to update the user interface every two seconds.

```
curl -X GET 0.0.0.0:5000/system-health
```

The response is a `SystemHealth` object as shown
in the following example.

```
{
    "cpuUsagePercent": 0.6,
    "diskTotalSize": "97GB",
    "diskUsagePercent": 14.9,
    "diskUsedSize": "14GB",
    "memoryUsagePercent": 15.5
}
```

### Getting the stations logs (SDK)

You can get the station logs with the API. First call `GET /snapshot`
to get the location of the logs.

```
curl -X POST 0.0.0.0:5000/snapshot
```

The response is the location of the logs. Then call `GET/snapshotfile/{path}`
to get the TAR file that contains the logs. Replace `file-name`
with response from `GET /snapshot`.

```
curl -X GET 0.0.0.0:5000/snapshotfile/`file-name`
```

### Restarting the Defect Detection Station App (SDK)

Common issues might be fixed by restarting the Defect Detection Station App. To restart the
Station App, call `POST/restart-dda`. During restart, You can call
`GET/dda-component-status` to get the current status. The
response is `UNHEALTHY` until the restart completes.

```
curl -X POST 0.0.0.0:5000/dda-restart
```

If the restart begins successfully, the response is `Success`.
