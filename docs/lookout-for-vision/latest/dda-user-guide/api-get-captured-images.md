Defect Detection App is in preview release and is subject to change.

# GET /captured-images

Gets the 12 most recent images in the specified path. To get the last 12 images
captured by an image source, specify the `path` request parameter as
`/aws_dda/image-capture/`imageSourceId``.
 Replace `imageSourceId` with the ID of the image source that you want to
use. You can get the ID for each image source on the Defect Detection Station App by calling the
[GET /image-sources](api-get-image-sources.md "api-get-image-sources.md")
operation.

## Endpoint

```
GET /captured-images
```

## Request

parameters

### path

The path to the folder that you want to get images from.

## Response

An array [CapturedImage](api-dt-CapturedImage.md "api-dt-CapturedImage.md") objects. Each
object represents a single image.

Format: String
