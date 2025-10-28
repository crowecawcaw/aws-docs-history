Defect Detection App is in preview release and is subject to change.

# Image

A based64 encoded image returned in the response from [POST
/image-sources/{imageSourceId}/preview](api-post-image-sources-preview.md "api-post-image-sources-preview.md") and [POST
/image-sources/{imageSourceId}/capture](api-post-image-sources-capture.md "api-post-image-sources-capture.md").

Depending on the type of the image source, either `image` or
`imageFileName` is returned, but not both.

## image

If the image source is a camera, `image` contains a base64 encoded
image from the camera.

Type: String

## imageFileName

If the image source is a folder, `imageFileName` contains the file
name of the next image in the folder that is available for processing.

Type: String
