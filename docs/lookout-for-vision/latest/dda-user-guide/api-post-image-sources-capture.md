Defect Detection App is in preview release and is subject to change.

# POST

/image-sources/{imageSourceId}/capture

Captures an image from the specified image source. You can use this operation
to capture images for your datasets.

For more information, see [ImageSource](api-dt-ImageSource.md "api-dt-ImageSource.md").

The response is the base64 encoded image. To get the location of the image, call the [GET
/image-sources/{imageSourceId}](api-get-image-source.md "api-get-image-source.md")
operation and check the `imageCapturePath` field in the response.

## Endpoint

```
POST /image-sources/{imageSourceId}/capture
```

`imageSourceId` is the identifier for the image source that you
want to capture an image from.

## Request

parameters

### filePrefix

An optional prefix to add to the filename of the captured
image.

Type: String

Required: No

## Response

An [Image](api-dt-Image.md "api-dt-Image.md") object that includes the preview image.

Format: [Image](api-dt-Image.md "api-dt-Image.md")
