Defect Detection App is in preview release and is subject to change.

# POST

/image-sources/{imageSourceId}/preview

Gets a preview image from the specified image source. You can use this
operation to check that the camera is configured properly and is returning
images.

For more information, see [ImageSource](api-dt-ImageSource.md "api-dt-ImageSource.md").

## Endpoint

```
POST /image-sources/{imageSourceId}/preview
```

`imageSourceId` is the identifier for the image source that you
want to get a preview image from.

## Request

parameters

### imageSourceConfiguration

An optional image source configuration for the workflow. Use to test the image source
configuration with different options. Once the image source configuration is correct, update
the image source with a call to [PATCH
/image-sources/{imageSourceId}](api-patch-image-source.md "api-patch-image-source.md")
and an updated `imageSourceConfiguration` field.

Type: [ImageSourceConfiguration](api-dt-ImageSourceConfiguration.md "api-dt-ImageSourceConfiguration.md")

Required: No

## Response

An [Image](api-dt-Image.md "api-dt-Image.md") object that includes the preview image.

Format: [Image](api-dt-Image.md "api-dt-Image.md")
