Defect Detection App is in preview release and is subject to change.

# DELETE /captured-images

Deletes the image in the specified path. To delete images captured from an image
source, specify the `filePath` request parameter as
`/aws_dda/image-capture/`imageSourceId``/`imageFileName`.
 Replace `imageSourceId`with the ID of the image source that you want to
 delete the image from. Replace`imageFileName` with the name of the image
that you want to delete.

You can get the ID for each image source on the Defect Detection Station App by calling the [GET /image-sources](api-get-image-sources.md "api-get-image-sources.md")
operation. Call [GET /captured-images](api-get-captured-images.md "api-get-captured-images.md") to get the most recent 12 images in a
folder.

## Endpoint

```
DELETE /captured-images
```

## Request

parameters

### filePath

The path and file name of the image that you want to delete.

## Response

The file name of the deleted file.

Format: String
