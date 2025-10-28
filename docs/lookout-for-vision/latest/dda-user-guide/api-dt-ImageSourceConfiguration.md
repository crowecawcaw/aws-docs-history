Defect Detection App is in preview release and is subject to change.

# ImageSourceConfiguration

Defines the gain, exposure, and processing pipeline settings for using a
camera as an input source ([ImageSource](api-dt-ImageSource.md "api-dt-ImageSource.md")). If you are not using a camera as an input source, you
don't need to specify an image source configuration. An image source configuration
is independent from a workflow and you can use an individual image source
configuration with more than one image source.

An image source can exist without an image source configuration for the
camera, for example when the camera is newly discovered.

## creationTime

The unix timestamp for the creation of the image source
configuration. Defect Detection App creates this value.

Type: Timestamp

## exposure

The amount of time, in milliseconds, that the image sensor is exposed to light when capturing an image. The default
value is `4000`.

Type: Number

Required: No

## gain

The raw gain setting for the camera. The default value is
`10`.

Type: Number

Required: No

## imageSourceConfigurationId

The ID for the image source configuration.

Type: String

## processingPipeline

The gstreamer processing pipeling settings for the camera. The default value is
`video/x-bayer, format=bggr ! bayer2rgb ! video/x-raw,
 format=RGBA`.

Type: String

Required: No
