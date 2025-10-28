# Recommendations for facial

comparison input images

The models used for face comparison operations are designed to work for a wide variety
of poses, facial expressions, age ranges, rotations, lighting conditions, and sizes. We
recommend that you use the following guidelines when choosing reference photos for
[CompareFaces](../APIReference/API_CompareFaces.md "../APIReference/API_CompareFaces.md") or
for adding faces to a collection using [IndexFaces](../APIReference/API_IndexFaces.md "../APIReference/API_IndexFaces.md").

## General

recommendations for input images for face operations

- Use images that are bright and sharp. Avoid using images that may be
  blurry due to subject and camera motion as much as possible. [DetectFaces](../APIReference/API_DetectFaces.md "../APIReference/API_DetectFaces.md") can be used to determine the brightness and
  sharpness of a face.
- For the purposes of gaze detection, it's recommended that you upload the
  original image at original size and quality.
- Use an image with a face that is within the recommended range of angles.
  The pitch should be less than 30 degrees face down and less than 45 degrees
  face up. The yaw should be less than 45 degrees in either direction. There
  is no restriction on the roll.
- Use an image of a face with both eyes open and visible.
- Use an image of a face that is not obscured or tightly cropped. The image
  should contain the full head and shoulders of the person. It should not be
  cropped to the face bounding box.
- Avoid items that block the face, such as headbands and masks.
- Use an image of a face that occupies a large proportion of the image.
  Images where the face occupies a larger portion of the image are matched
  with greater accuracy.
- Ensure that images are sufficiently large in terms of resolution.
  Amazon Rekognition can recognize faces as small as 50 x 50 pixels in image
  resolutions up to 1920 x 1080. Higher-resolution images require a larger
  minimum face size. Faces larger than the minimum size provide a more
  accurate set of facial comparison results.
- Use color images.
- Use images with flat lighting on the face, as opposed to varied lighting
  such as shadows.
- Use images that have sufficient contrast with the background. A
  high-contrast monochrome background works well.
- Use images of faces with neutral facial expressions with mouth closed and
  little to no smile for applications that require high precision.
