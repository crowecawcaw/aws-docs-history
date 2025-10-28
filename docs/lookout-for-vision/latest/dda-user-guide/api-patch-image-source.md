Defect Detection App is in preview release and is subject to change.

# PATCH

/image-sources/{imageSourceId}

Updates an individual image source.

You can't change the camera assigned to an image source.

For more information, see [ImageSource](api-dt-ImageSource.md "api-dt-ImageSource.md").

## Endpoint

```
PATCH /image-sources/{imageSourceId}
```

`imageSourceId` is the identifier for the image source that you
want to update.

## Request

parameters

Information about the image source that you want to update.

Type: JSON

Required: Yes

### description

The description for the workflow.

Type: String

Required: No

### imageSourceConfiguration

An image source configuration for the workflow.

Type: [ImageSourceConfiguration](api-dt-ImageSourceConfiguration.md "api-dt-ImageSourceConfiguration.md")

Required: Yes

### location

If the image source `type` is `Folder`,
specifies the absolute path to the folder that provides images to a
workflow. The folder location must be under the `/aws_dda/`
folder on the edge device. Don't specify `location` if the
image source type is `Camera`.

Type: String

Required: Yes, if the image source `type` is `Folder`.

### name

The name for the image source.

Type: String

Required: No

## Response

The ID for the updated workflow.

Format: JSON
