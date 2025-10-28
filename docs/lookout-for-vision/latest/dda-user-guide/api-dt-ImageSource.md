Defect Detection App is in preview release and is subject to change.

# ImageSource

Defines the source for images that a workflow consumes. An image source can be
a camera on the local network or a folder on the edge device.

To create an image source, see [POST /image-sources](api-post-image-sources.md "api-post-image-sources.md").

## cameraId

The ID of the physical camera that the image source uses. To get the ID
for a camera, you call the `GET /cameras` operation to get the
discovered cameras.

Type: String

Required: Yes, if the image source `type` is `Camera`.

## creationTime

The unix timestamp for the creation of the image source. Defect Detection App creates this value.

Type: Timestamp

## description

The description of the image source.

Type: String

Required: No

## imageSourceConfiguration

If the image source `type` is `Camera`, specifies
the gain, exposure, processing pipeline settings for the camera.

Don't specify `imageSourceConfiguration` if the image source
`type` is `Folder`.

Type: [ImageSourceConfiguration](api-dt-ImageSourceConfiguration.md "api-dt-ImageSourceConfiguration.md")

Required: No

## imageSourceId

The unique ID for the image source.

Type: String

## lastUpdateTime

The Unix timestamp for the last update of the ImageSource. Defect Detection App creates this value.

Type: Timestamp

Required: No

## location

If the image source `type` is `Folder`, specifies
the absolute path to the folder that provides images to a workflow. The
folder location must be under the `/aws_dda/` folder on the edge
device. Don't specify `location` if the image source `type` is
`Camera`.

Type: String

Required: Yes, if the image source `type` is `Folder`.

## name

The name of the image source.

Type: String

## imageCapturePath

The absolute path to the folder where the camera saves captured images. You can use these
images in your datasets.
Only applicable if the image source `type` is `Camera`.

Type: String

Required: Yes, if the image source `type` is `Camera`.

## type

The type of the image source (Camera or Folder).

Type: String

Pattern: `Camera | Folder`
