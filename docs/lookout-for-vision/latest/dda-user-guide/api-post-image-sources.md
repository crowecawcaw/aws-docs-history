Defect Detection App is in preview release and is subject to change.

# POST /image-sources

Creates an image source. For more information, see [ImageSource](api-dt-ImageSource.md "api-dt-ImageSource.md").

Station App configures the image source configuration with default values.
Use the [PATCH
/image-sources/{imageSourceId}](api-patch-image-source.md "api-patch-image-source.md") operation
to change the image source configuration.
For more information about image source configuration, see [ImageSourceConfiguration](api-dt-ImageSourceConfiguration.md "api-dt-ImageSourceConfiguration.md").

## Endpoint

```
POST /image-sources
```

## Request

parameters

Information about the image source that you want to update.

Type: JSON

Required: Yes

### cameraId

The ID of the physical camera that the image source uses. To get the
ID for a camera, call the [GET /cameras](api-get-cameras.md "api-get-cameras.md") operation.

Type: String

Required: Yes, if the image source `type` is `Camera`.

### description

The description for the workflow.

Type: String

Required: No

### location

If the image source `type` is `Folder`,
specifies the absolute path to the folder that provides images to a
workflow. The folder location must be under the `/aws_dda/`
folder on the edge device. Don't specify `location` if the
image source `type` is `Camera`.

Type: String

Required: Yes, if the image source `type` is `Folder`.

### name

The name for the image source.

Type: String

Required: No

### type

The type of the image source (Camera or Folder).

Type: String

Pattern: `Camera | Folder`

Required: Yes

## Response

The ID for the created image source.

Format: String
